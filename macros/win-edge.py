# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows
from macro_actions import Shortcut, Type

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Windows Edge', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', Shortcut("ALT", "LEFT_ARROW")),
        (0x004000, 'Fwd >', Shortcut("ALT", "RIGHT_ARROW")),
        (0x400000, 'Up', Shortcut("SHIFT", ' ')),      # Scroll up
        # 2nd row ----------
        (0x202000, '- Size', Shortcut("CONTROL", "KEYPAD_MINUS")),
        (0x202000, 'Size +', Shortcut("CONTROL", "KEYPAD_PLUS")),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', Shortcut("CONTROL", "R")),
        (0x000040, 'Home', Shortcut("ALT", "HOME")),
        (0x000040, 'Private', Shortcut("CONTROL", "SHIFT", 'N')),
        # 4th row ----------
        (0x000000, 'Ada', [Shortcut("CONTROL", "N"), 0,
                           Type('www.adafruit.com\n')]),   # Adafruit in new window
        (0x800000, 'Digi', [Shortcut("CONTROL", "N"), 0,
                            Type('www.digikey.com\n')]),   # Digi-Key in new window
        (0x101010, 'Hacks', [Shortcut("CONTROL", "N"), 0,
                             Type('www.hackaday.com\n')]), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', Shortcut("CONTROL", "W")) # Close tab
    ]
}
