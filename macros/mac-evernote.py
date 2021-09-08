# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc
from macro_actions import K

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Mac Evernote', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'New Nt', K("COMMAND", "N")),
        (0x004000, 'New Bk', K("SHIFT", "COMMAND", "N")),
        (0x004000, 'CP Lnk', K("CONTROL", "OPTION", "COMMAND", "C")),
        # 2nd row ----------
        (0x004000, 'Move', K("CONTROL", "COMMAND", "M")),
        (0x004000, 'Find', K("OPTION", "COMMAND", "F")),
        (0x004000, 'Emoji', K("CONTROL", "COMMAND", " ")),
        # 3rd row ----------
        (0x004000, 'Bullets', K("SHIFT", "COMMAND", "U")),
        (0x004000, 'Nums', K("SHIFT", "COMMAND", "O")),
        (0x004000, 'Check', K("SHIFT", "COMMAND", "T")),
        # 4th row ----------
        (0x004000, 'Date', K("SHIFT", "COMMAND", "D" )),
        (0x004000, 'Time', K("OPTION", "SHIFT", "COMMAND", "D" )),
        (0x004000, 'Divider', K("SHIFT", "COMMAND", "H")),
        # Encoder button ---
        (0x000000, '', K("COMMAND", "W")) # Close window/tab
    ]
}
