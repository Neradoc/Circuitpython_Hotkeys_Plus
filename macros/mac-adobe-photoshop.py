# MACROPAD Hotkeys example: Adobe Photoshop for Mac
from macro_actions import K

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Mac Photoshop', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Undo', K("COMMAND", 'Z')),
        (0x004000, 'Redo', K("COMMAND", "SHIFT", 'Z')),
        (0x000040, 'Brush', K("SHIFT", 'B')),   # Cycle brush modes
        # 2nd row ----------
        (0x101010, 'B&W',  K('D')),     # Default colors
        (0x101010, 'Marquee', K("SHIFT", 'M')), # Cycle rect/ellipse marquee (select)
        (0x000040, 'Eraser', K("SHIFT", 'E')),  # Cycle eraser modes
        # 3rd row ----------
        (0x101010, 'Swap',  K('X')),    # Swap foreground/background colors
        (0x101010, 'Move', K('V')),    # Move layer
        (0x000040, 'Fill', K("SHIFT", 'G')),    # Cycle fill/gradient modes
        # 4th row ----------
        (0x101010, 'Eyedrop', K("SHIFT", 'I')), # Cycle eyedropper/measure modes
        (0x101010, 'Wand', K("SHIFT", 'W')),    # Cycle "magic wand" (selection) modes
        (0x000040, 'Heal', K("SHIFT", 'J')),    # Cycle "healing" modes
        # Encoder button ---
        (0x000000, '', K("COMMAND", "OPTION", 'S')) # Save for web
    ]
}