# MACROPAD Hotkeys example: Firefox web browser for Linux

from macro_actions import Shortcut, Type

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Linux Firefox', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [ Shortcut("CONTROL", "LEFT_BRACKET") ]),
        (0x004000, 'Fwd >', [ Shortcut("CONTROL", "RIGHT_BRACKET") ]),
        (0x400000, 'Up', [ Shortcut("SHIFT", " ") ]),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [ Shortcut("CONTROL"), Shortcut("SHIFT"), Shortcut("TAB") ]),
        (0x202000, 'Tab >', [ Shortcut("CONTROL"), Shortcut("TAB") ]),
        (0x400000, 'Down', Shortcut(' ')),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [ Shortcut("CONTROL", 'R') ]),
        (0x000040, 'Home', [ Shortcut("CONTROL", 'H') ]),
        (0x000040, 'Private', [ Shortcut("CONTROL", "SHIFT", 'P') ]),
        # 4th row ----------
        (0x101010, 'Ada', [ Shortcut("CONTROL", "T"), 0,        # ctrl-T and release
                            Type('www.adafruit.com\n') ]),  # adafruit.com in a new tab
        (0x000040, 'Dev Mode', [ Shortcut("F12") ]),  # dev mode
        (0x101010, 'Digi', [ Shortcut("CONTROL", 'T'), 0,   # ctrl-T and release
                             Type('digikey.com\n') ]),  # digikey in a new tab
        # Encoder button ---
        (0x000000, '', [ Shortcut("CONTROL", 'W') ]) # Close window/tab
    ]
}
