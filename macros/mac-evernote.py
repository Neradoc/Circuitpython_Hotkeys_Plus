# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc
from macro_actions import Shortcut

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Mac Evernote', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'New Nt', Shortcut("COMMAND", "N")),
        (0x004000, 'New Bk', Shortcut("SHIFT", "COMMAND", "N")),
        (0x004000, 'CP Lnk', Shortcut("CONTROL", "OPTION", "COMMAND", "C")),
        # 2nd row ----------
        (0x004000, 'Move', Shortcut("CONTROL", "COMMAND", "M")),
        (0x004000, 'Find', Shortcut("OPTION", "COMMAND", "F")),
        (0x004000, 'Emoji', Shortcut("CONTROL", "COMMAND", " ")),
        # 3rd row ----------
        (0x004000, 'Bullets', Shortcut("SHIFT", "COMMAND", "U")),
        (0x004000, 'Nums', Shortcut("SHIFT", "COMMAND", "O")),
        (0x004000, 'Check', Shortcut("SHIFT", "COMMAND", "T")),
        # 4th row ----------
        (0x004000, 'Date', Shortcut("SHIFT", "COMMAND", "D" )),
        (0x004000, 'Time', Shortcut("OPTION", "SHIFT", "COMMAND", "D" )),
        (0x004000, 'Divider', Shortcut("SHIFT", "COMMAND", "H")),
        # Encoder button ---
        (0x000000, '', Shortcut("COMMAND", "W")) # Close window/tab
    ]
}
