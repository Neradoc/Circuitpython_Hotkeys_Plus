# MACROPAD Hotkeys example: Adobe Illustrator for Mac
from macro_actions import Shortcut

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Mac Illustrator', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Undo', [ Shortcut("COMMAND", 'Z') ]),
        (0x004000, 'Redo', [ Shortcut("COMMAND", "SHIFT", 'Z') ]),
        (0x303000, 'Pen', Shortcut('P')),     # Path-drawing tool
        # 2nd row ----------

        (0x101010, 'Select', Shortcut("V")),  # Select (path)
        (0x400000, 'Reflect', Shortcut("O")), # Reflect selection
        (0x303000, 'Rect', Shortcut("M")),    # Draw rectangle
        # 3rd row ----------
        (0x101010, 'Direct', Shortcut("A")),  # Direct (point) selection
        (0x400000, 'Rotate', Shortcut("R")),  # Rotate selection
        (0x303000, 'Oval', Shortcut("L")),    # Draw ellipse
        # 4th row ----------
        (0x101010, 'Eyedrop', Shortcut("I")), # Cycle eyedropper/measure modes
        (0x400000, 'Scale', Shortcut("S")),   # Scale selection
        (0x303000, 'Text', Shortcut("T")),    # Type tool
        # Encoder button ---
        (0x000000, '', Shortcut("COMMAND", "OPTION", "SHIFT", 'S')) # Save for web
    ]
}
