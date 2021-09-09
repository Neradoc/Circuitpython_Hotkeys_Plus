"""
A fairly straightforward macro/hotkey program for Adafruit MACROPAD.
Macro key setups are stored in the /macros folder (configurable below),
load up just the ones you're likely to use. Plug into computer's USB port,
use dial to select an application macro set, press MACROPAD keys to send
key sequences.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import time
import displayio
import terminalio
import traceback
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from macro_actions import MacroAction, Tone, Type


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'


# CLASSES AND FUNCTIONS ----------------

class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']
        self._enter = None
        if "enter" in appdata and callable(appdata['enter']):
            self._enter = appdata['enter']
        self._leave = None
        if "leave" in appdata and callable(appdata['leave']):
            self._leave = appdata['leave']


    def switch(self, prev_app=None):
        """ Activate application settings; update OLED labels and LED
            colors. """
        # the previous app's "leave" custom code
        if prev_app and prev_app._leave:
            prev_app._leave(pad=macropad, prev_app=prev_app, next_app=self)
        # do the switch
        group[13].text = self.name   # Application name
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ''
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()
        # the current app's "enter" custom code
        if self._enter:
            self._enter(pad=macropad, prev_app=prev_app, next_app=self)


# INITIALIZATION -----------------------

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

def play_tone(note, duration):
    macropad.play_tone(note, duration)

Tone.play_tone = play_tone

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((macropad.display.width - 1) * x / 2,
                                                macropad.display.height - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x / 2, 1.0)))
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -2),
                         anchor_point=(0.5, 0.0)))
macropad.display.show(group)
macropad.group = group

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py') and filename[0] != ".":
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    while True:
        pass

# the last position being None makes the loop start with switching to a page
last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0


# MAIN LOOP ----------------------------

while True:
    # Read encoder position. If it's changed, switch apps.
    position = macropad.encoder
    if position != last_position:
        prev_app_index = app_index
        app_index = position % len(apps)
        apps[app_index].switch(apps[prev_app_index])
        last_position = position

    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue    # No 13th macro, just resume main loop
        key_number = 12 # else process below as 13th macro
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    sequence = apps[app_index].macros[key_number][2]
    if not isinstance(sequence, (list, tuple)):
        sequence = (sequence,)
    if pressed:
        # the sequence is arbitrary-length
        # each item in the sequence is either
        # an action instance or a floating point value
        # Action   ==>  execute the action
        # Float    ==>  sleep in seconds
        # Funciton ==>  call it with context
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = 0xFFFFFF
            macropad.pixels.show()
        past_items = []
        past_keycodes = set()  # for compatibility
        for index,item in enumerate(sequence):
            past_items.append(item)
            if item == 0:
                for item in sequence:
                    if isinstance(item, MacroAction):
                        item.release()
            elif isinstance(item, MacroAction):
                item.action()
            elif isinstance(item, float):
                time.sleep(item)
            elif callable(item):
                item(pad=macropad, key=key_number, idx=index)
            elif isinstance(item, int):
                # compatibility
                if item > 0:
                    macropad.keyboard.press(item)
                    past_keycodes.add(item)
                else:
                    macropad.keyboard.release(item)
                    past_keycodes.remove(item)
            elif isinstance(item, str):
                # compatibility
                Type.write(item)
            else:
                print("Unkown action", item)
    else:
        # Release any still-pressed keys
        for item in sequence:
            if isinstance(item, MacroAction):
                item.release()
            # compatibility
            if isinstance(item, int) and item >= 0:
                macropad.keyboard.release(item)
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
