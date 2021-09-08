# MACROPAD Hotkeys example: Universal Numpad
from macro_actions import K

def onoff(pad, key, idx):
    # pad.display.brightness = 0
    pad.group.hidden = not pad.group.hidden
    pad.display.refresh()
    if pad.group.hidden:
        pad.pixels.fill(0)
        pad.pixels.show()

def leaving(pad, prev_app, next_app):
    pad.group.hidden = False
    pad.display.refresh()

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', K("7")),
        (0x202000, '8', K("8")),
        (0x202000, '9', K("9")),
        # 2nd row ----------
        (0x202000, '4', K("4")),
        (0x202000, '5', K("5")),
        (0x202000, '6', K("6")),
        # 3rd row ----------
        (0x202000, '1', K("1")),
        (0x202000, '2', K("2")),
        (0x202000, '3', K("3")),
        # 4th row ----------
        (0x101010, '*', K("*")),
        (0x800000, '0', K("0")),
        (0x101010, '#', K("#")),
        # Encoder button ---
        (0x000000, '', onoff)
    ],
    'enter' : None,
    'leave' : leaving,
}
