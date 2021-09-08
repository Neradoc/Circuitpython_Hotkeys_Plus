# MACROPAD Hotkeys example: Safari web browser for Mac
from macro_actions import Shortcut, Type

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Mac Safari', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', Shortcut("COMMAND", 'LEFT_BRACKET')),
        (0x004000, 'Fwd >', Shortcut("COMMAND", 'RIGHT_BRACKET')),
        (0x400000, 'Up', Shortcut("SHIFT", ' ')),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', Shortcut("CONTROL", "SHIFT", "TAB")),
        (0x202000, 'Tab >', Shortcut("CONTROL", "TAB")),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', Shortcut("COMMAND", 'r')),
        (0x000040, 'Home', Shortcut("COMMAND", 'H')),
        (0x000040, 'Private', Shortcut("COMMAND", 'N')),
        # 4th row ----------
        (0x000000, 'Ada', [Shortcut("COMMAND", 'n'), 0,
                           Type('www.adafruit.com\n')]),   # Adafruit in new window
        (0x800000, 'Digi', [Shortcut("COMMAND", 'n'), 0,
                            Type('www.digikey.com\n')]),   # Digi-Key in new window
        (0x101010, 'Hacks', [Shortcut("COMMAND", 'n'), 0,
                             Type('www.hackaday.com\n')]), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', Shortcut("COMMAND", 'w')) # Close window/tab
    ]
}
