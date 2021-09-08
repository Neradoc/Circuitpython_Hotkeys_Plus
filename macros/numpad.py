# MACROPAD Hotkeys example: Universal Numpad
from macro_actions import Shortcut

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', Shortcut("7")),
        (0x202000, '8', Shortcut("8")),
        (0x202000, '9', Shortcut("9")),
        # 2nd row ----------
        (0x202000, '4', Shortcut("4")),
        (0x202000, '5', Shortcut("5")),
        (0x202000, '6', Shortcut("6")),
        # 3rd row ----------
        (0x202000, '1', Shortcut("1")),
        (0x202000, '2', Shortcut("2")),
        (0x202000, '3', Shortcut("3")),
        # 4th row ----------
        (0x101010, '*', Shortcut("*")),
        (0x800000, '0', Shortcut("0")),
        (0x101010, '#', Shortcut("#")),
        # Encoder button ---
        (0x000000, '', Shortcut("BACKSPACE"))
    ]
}
