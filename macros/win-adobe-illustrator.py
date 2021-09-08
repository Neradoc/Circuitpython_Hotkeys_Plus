# MACROPAD Hotkeys example: Adobe Illustrator for Windows
from macro_actions import K, L

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Win Illustrator', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Undo', K("CONTROL", 'Z')),
        (0x004000, 'Redo', K("CONTROL", "SHIFT", 'Z')),
        (0x303000, 'Pen', K("P")),     # Path-drawing tool
        # 2nd row ----------

        (0x101010, 'Select', K("V")),  # Select (path)
        (0x400000, 'Reflect', K("O")), # Reflect selection
        (0x303000, 'Rect', K("M")),    # Draw rectangle
        # 3rd row ----------
        (0x101010, 'Direct', K("A")),  # Direct (point) selection
        (0x400000, 'Rotate', K("R")),  # Rotate selection
        (0x303000, 'Oval', K("L")),    # Draw ellipse
        # 4th row ----------
        (0x101010, 'Eyedrop', K("I")), # Cycle eyedropper/measure modes
        (0x400000, 'Scale', K("S")),   # Scale selection
        (0x303000, 'Text', K("T")),    # Type tool
        # Encoder button ---
        (0x000000, '', K("CONTROL", "ALT", "SHIFT", 'S')) # Save for web
    ]
}
