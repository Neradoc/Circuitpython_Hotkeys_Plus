# MACROPAD Hotkeys example: Safari web browser for Mac
from macro_actions import K, L

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Mac Safari', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', K("COMMAND", 'LEFT_BRACKET')),
        (0x004000, 'Fwd >', K("COMMAND", 'RIGHT_BRACKET')),
        (0x400000, 'Up', K("SHIFT", ' ')),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', K("CONTROL", "SHIFT", "TAB")),
        (0x202000, 'Tab >', K("CONTROL", "TAB")),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', K("COMMAND", 'r')),
        (0x000040, 'Home', K("COMMAND", 'H')),
        (0x000040, 'Private', K("COMMAND", 'N')),
        # 4th row ----------
        (0x000000, 'Ada', [K("COMMAND", 'n'), 0,
                           L('www.adafruit.com\n')]),   # Adafruit in new window
        (0x800000, 'Digi', [K("COMMAND", 'n'), 0,
                            L('www.digikey.com\n')]),   # Digi-Key in new window
        (0x101010, 'Hacks', [K("COMMAND", 'n'), 0,
                             L('www.hackaday.com\n')]), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', K("COMMAND", 'w')) # Close window/tab
    ]
}
