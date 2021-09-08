# MACROPAD Hotkeys example: Universal Numpad
from macro_actions import K, L, Tone
import time

def onoff(pad, key, idx):
    # pad.display.brightness = 0
    pad.group.hidden = not pad.group.hidden
    pad.display.refresh()
    if pad.group.hidden:
        pad.pixels.fill(0)
        pad.pixels.show()

beep = Tone(("C6", 0.08), 0.05, ("E6", 0.10))

def entering(pad, prev_app, next_app):
    beep.action()

def leaving(pad, prev_app, next_app):
    pad.group.hidden = False
    pad.display.refresh()

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Test Macros', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', K("A")),
        (0x202000, '8', K("8")),
        (0x202000, '9', K("9")),
        # 2nd row ----------
        (0x202000, '4', K("4")),
        (0x202000, '5', K("5")),
        (0x202000, '6', K("6")),
        # 3rd row ----------
        (0x202000, '1', Tone( ("A4", 0.5) ) ),
        (0x202000, '2', Tone(
            ("A5", 0.2), 0.2,
            ("B5", 0.2), ("C6", 0.2), 0.2,
            ("D6", 0.2), ("D#6", 0.2)
        ) ),
        (0x202000, '3', Tone(
            ("C6", 0.2), ("E6", 0.2), ("G6", 0.2), ("C7", 0.2),
            ("G6", 0.2), ("E6", 0.2), ("C6", 0.5),
        ) ),
        # 4th row ----------
        (0x101010, '*', K("A")),
        (0x800000, '0', K("M")),
        (0x101010, '#', L("Hello 123")),
        # Encoder button ---
        (0x000000, '', onoff)
    ],
    'enter' : entering,
    'leave' : leaving,
}
