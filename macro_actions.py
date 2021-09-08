import os
import time
import usb_hid
import usb_midi
from adafruit_midi import MIDI
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard

common_keyboard = Keyboard(usb_hid.devices)

# config in macros_config.py
RELEASE_DELAY = 0.02

BASE_NOTES = { "C": 24, "D": 26, "E": 28, "F": 29, "G": 31, "A": 33, "B": 35 }

_default_keycode = None

def default_keycode():
    global _default_keycode
    if _default_keycode:
        return _default_keycode
    try:
        import macros_config
        _default_keycode = macros_config.default_keycode
        return _default_keycode
    except Exception as ex:
        import traceback
        traceback.print_exception(ex,ex,ex.__traceback__)
        from adafruit_hid import keycode
        _default_keycode = keycode.Keycode
        return _default_keycode

_default_layout = None

def default_layout():
    global _default_layout
    if _default_layout:
        return _default_layout
    try:
        import macros_config
        _default_layout = macros_config.default_layout(common_keyboard)
        return _default_layout
    except Exception as ex:
        import traceback
        traceback.print_exception(ex,ex,ex.__traceback__)
        from adafruit_hid import keyboard_layout_us
        _default_layout = keyboard_layout_us.KeyboardLayoutUS(common_keyboard)
        return _default_layout

def code_to_note(code):
    if isinstance(code, str):
        if len(code) and code[0] in BASE_NOTES:
            note = BASE_NOTES[code[0]]
        else:
            raise ValueError("Unknown note: "+repr(code))
        delta = ""
        for nn in code[1:]:
            if nn == "-":
                delta = nn
            if nn in "0123456789":
                note = note + 12 * int(delta + nn)
            if nn == "#":
                note = note + 1
        return note
    return code

class MacroAction:
    """
    Parent action class.
    An action describes a group of keys to press or release together.
    A normal action is for a press, a negative action is for release.
    """
    def __init__(self, *actions, neg=False):
        self.actions = actions
        self.neg = neg
    def press(self):
        raise NotImplementedError("MacroAction must be subclassed to press()")
    def release(self):
        raise NotImplementedError("MacroAction must be subclassed to release()")
    def action(self):
        if self.neg:
            self.release()
        else:
            self.press()
    def send(self):
        self.press()
        time.sleep(RELEASE_DELAY)
        self.release()
    def __neg__(self):
        return self.__class__(*self.actions, neg = not self.neg)
    def __repr__(self):
        return ("-" if self.neg else "+") + repr(self.actions)

class K(MacroAction):
    """
    Action to press/release a list of keycodes together.
    Do multiple actions to press/release independently.
    The Keycode class used can be changed at the class level.
    Takes ints or converts strings using getattr on the Keycode class.
    """
    keyboard = common_keyboard
    keycode = None
    def __init__(self, *actions, neg=False):
        if K.keycode == None:
            K.keycode = default_keycode()
        acts = []
        for action in actions:
            if isinstance(action, int):
                acts.append(action)
            elif isinstance(action, str):
                if hasattr(self.keycode, action):
                    code = getattr(self.keycode, action)
                    acts.append(code)
                elif len(action) == 1:
                    L.layout = default_layout()
                    acts += L.layout.keycodes(action)
            else:
                raise ValueError("Bad type of K action:" + repr(action))
        super().__init__(*acts, neg=neg)
    def press(self):
        self.keyboard.press(*self.actions)
    def release(self):
        self.keyboard.release(*self.actions)
    def send(self):
        self.keyboard.send(*self.actions)

class C(MacroAction):
    """
    Action to press/release a ConsumerControl key (only one at a time).
    """
    control = ConsumerControl(usb_hid.devices)
    def __init__(self, action, *, neg=False):
        if isinstance(action, int):
            code = action
        elif isinstance(action, str):
            code = getattr(ConsumerControlCode, action)
        else:
            raise ValueError("Bad type of C action:" + repr(action))
        super().__init__(code, neg=neg)
    def press(self):
        self.control.press(*self.actions)
    def release(self):
        self.control.release()  # only one key at a time anyway
    def send(self):
        self.control.send(*self.actions)

class M(MacroAction):
    """
    Action to press/release a list of midi keys together.
    """
    midi = MIDI(midi_out=usb_midi.ports[1], out_channel=0)
    def __init__(self, *actions, neg=False):
        acts = []
        for data in actions:
            velocity = 127
            if isinstance(data, (tuple, list)):
                note = code_to_note(data[0])
                if len(data) > 1:
                    velocity = data[1]
            else:
                note = code_to_note(data)
            acts.append( (note, velocity) )
        super().__init__(*acts, neg=neg)
    def press(self):
        for note, velocity in self.actions:
            self.midi.send(NoteOn(note, velocity))
    def release(self):
        for note, velocity in self.actions:
            self.midi.send(NoteOff(note, 0))
    def send(self):
        self.press()
        time.sleep(RELEASE_DELAY)
        self.release()

class L(MacroAction):
    """
    Action to write a string with a layout, use via a LayoutFactory,
    so you don't have to repeat the "layout" argument in your macros.
    """
    layout = None
    def __init__(self, *actions, neg=False):
        super().__init__(*actions, neg=neg)
        if self.layout == None:
            L.layout = default_layout()
    def press(self):
        for action in self.actions:
            self.layout.write(action)
    def release(self):
        pass
    def send(self):
        self.press()

class Color:
    """
    Encodes the default color of the button.
    Encodes the temporary color when pressed, with -Color(x).
    A color value can be:
    - an int: 0xRRGGBB
    - a css color: "#RRGGBB"
    - a tuple (r, g, b)
    """
    def __init__(self, color, *, press=False):
        self.press = press
        if isinstance(color, tuple):
            self.color = color
        elif isinstance(color, int):
            c = color
            self.color = (c >> 16 & 0xFF, c >> 8 & 0xFF, c & 0xFF)
        elif isinstance(color, str):
            c = int(color.replace("#",""), 16)
            self.color = (c >> 16 & 0xFF, c >> 8 & 0xFF, c & 0xFF)
        else:
            raise ValueError("Color value invalid, give tuple, int or hexa string")
    def __repr__(self):
        return ("+" if self.press else "-") + f"Color{self.color}"
    def __neg__(self):
        return self.__class__(self.color, press = not self.press)
