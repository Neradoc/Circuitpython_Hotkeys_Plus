# MACROPAD Hotkeys example: Minecraft hotbar (inventory)

# Note: Must enable "full keyboad gameplay" for Prev/Next buttons to work.
#       This is found under "settings", then "keyboard and mouse".

from macro_actions import Shortcut

app = {                          # REQUIRED dict, must be named 'app'
    'name' : 'Minecraft Hotbar', # Application name
    'macros' : [                 # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', Shortcut('7')),
        (0x202000, '8', Shortcut('8')),
        (0x202000, '9', Shortcut('9')),
        # 2nd row ----------
        (0x202000, '4', Shortcut('4')),
        (0x202000, '5', Shortcut('5')),
        (0x202000, '6', Shortcut('6')),
        # 3rd row ----------
        (0x202000, '1', Shortcut('1')),
        (0x202000, '2', Shortcut('2')),
        (0x202000, '3', Shortcut('3')),
        # 4th row ----------
        (0x002020, 'Prev', [Shortcut("PAGE_UP")]),
        (0x000000, '', []),
        (0x002020, 'Next', [Shortcut("PAGE_DOWN")]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
