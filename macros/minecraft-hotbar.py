# MACROPAD Hotkeys example: Minecraft hotbar (inventory)

# Note: Must enable "full keyboad gameplay" for Prev/Next buttons to work.
#       This is found under "settings", then "keyboard and mouse".

from macro_actions import K, L

app = {                          # REQUIRED dict, must be named 'app'
    'name' : 'Minecraft Hotbar', # Application name
    'macros' : [                 # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', K('7')),
        (0x202000, '8', K('8')),
        (0x202000, '9', K('9')),
        # 2nd row ----------
        (0x202000, '4', K('4')),
        (0x202000, '5', K('5')),
        (0x202000, '6', K('6')),
        # 3rd row ----------
        (0x202000, '1', K('1')),
        (0x202000, '2', K('2')),
        (0x202000, '3', K('3')),
        # 4th row ----------
        (0x002020, 'Prev', [K("PAGE_UP")]),
        (0x000000, '', []),
        (0x002020, 'Next', [K("PAGE_DOWN")]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
