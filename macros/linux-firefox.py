# MACROPAD Hotkeys example: Firefox web browser for Linux

from macro_actions import K, L

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Linux Firefox', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [ K("CONTROL", "LEFT_BRACKET") ]),
        (0x004000, 'Fwd >', [ K("CONTROL", "RIGHT_BRACKET") ]),
        (0x400000, 'Up', [ K("SHIFT", " ") ]),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [ K("CONTROL"), K("SHIFT"), K("TAB") ]),
        (0x202000, 'Tab >', [ K("CONTROL"), K("TAB") ]),
        (0x400000, 'Down', K(' ')),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [ K("CONTROL", 'R') ]),
        (0x000040, 'Home', [ K("CONTROL", 'H') ]),
        (0x000040, 'Private', [ K("CONTROL", "SHIFT", 'P') ]),
        # 4th row ----------
        (0x101010, 'Ada', [ K("CONTROL", "T"), 0,        # ctrl-T and release
                            L('www.adafruit.com\n') ]),  # adafruit.com in a new tab
        (0x000040, 'Dev Mode', [ K("F12") ]),  # dev mode
        (0x101010, 'Digi', [ K("CONTROL", 'T'), 0,   # ctrl-T and release
                             L('digikey.com\n') ]),  # digikey in a new tab
        # Encoder button ---
        (0x000000, '', [ K("CONTROL", 'W') ]) # Close window/tab
    ]
}
