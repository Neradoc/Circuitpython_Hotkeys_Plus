# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows
from macro_actions import K, L

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Windows Edge', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', K("ALT", "LEFT_ARROW")),
        (0x004000, 'Fwd >', K("ALT", "RIGHT_ARROW")),
        (0x400000, 'Up', K("SHIFT", ' ')),      # Scroll up
        # 2nd row ----------
        (0x202000, '- Size', K("CONTROL", "KEYPAD_MINUS")),
        (0x202000, 'Size +', K("CONTROL", "KEYPAD_PLUS")),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', K("CONTROL", "R")),
        (0x000040, 'Home', K("ALT", "HOME")),
        (0x000040, 'Private', K("CONTROL", "SHIFT", 'N')),
        # 4th row ----------
        (0x000000, 'Ada', [K("CONTROL", "N"), 0,
                           L('www.adafruit.com\n')]),   # Adafruit in new window
        (0x800000, 'Digi', [K("CONTROL", "N"), 0,
                            L('www.digikey.com\n')]),   # Digi-Key in new window
        (0x101010, 'Hacks', [K("CONTROL", "N"), 0,
                             L('www.hackaday.com\n')]), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', K("CONTROL", "W")) # Close tab
    ]
}
