# MACROPAD Hotkeys example: Adobe Photoshop for Windows
from macro_actions import Shortcut

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Win Photoshop', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Undo', Shortcut("CONTROL", "Z")),
        (0x004000, 'Redo', Shortcut("CONTROL", "SHIFT", "Z")),
        (0x000040, 'Brush', Shortcut("SHIFT", "B")),   # Cycle brush modes
        # 2nd row ----------
        (0x101010, 'B&W', Shortcut("D")),     # Default colors
        (0x101010, 'Marquee', Shortcut("SHIFT", "M")), # Cycle rect/ellipse marquee (select)
        (0x000040, 'Eraser', Shortcut("SHIFT", "E")),  # Cycle eraser modes
        # 3rd row ----------
        (0x101010, 'Swap', Shortcut("SHIFT", "X")),    # Swap foreground/background colors
        (0x101010, 'Move', Shortcut("V")),    # Move layer
        (0x000040, 'Fill', Shortcut("SHIFT", "G")),    # Cycle fill/gradient modes
        # 4th row ----------
        (0x101010, 'Eyedrop', Shortcut("SHIFT", "I")), # Cycle eyedropper/measure modes
        (0x101010, 'Wand', Shortcut("SHIFT", "W")),    # Cycle "magic wand" (selection) modes
        (0x000040, 'Heal', Shortcut("SHIFT", "J")),    # Cycle "healing" modes
        # Encoder button ---
        (0x000000, '', Shortcut("CONTROL", "ALT", "SHIFT", "S")) # Save for web
    ]
}
