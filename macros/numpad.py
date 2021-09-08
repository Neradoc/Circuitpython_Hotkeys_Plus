# MACROPAD Hotkeys example: Universal Numpad
from macro_actions import K

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
        (0x000000, '', K("BACKSPACE"))
    ]
}
