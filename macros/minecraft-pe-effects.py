# MACROPAD Hotkeys example: Minecraft Effects (Creative) for Bedrock Edition

# NOTE: There appears to be a line length limit. Exceeding that limit appears
#       to result in silent failure.  Therefore, the key sequences are split
#       across multiple lines.

from macro_actions import S, Type

# See https://minecraft.fandom.com/wiki/Effect

DELAY_AFTER_SLASH   = 0.80 # required so minecraft has time to bring up command screen
DELAY_BEFORE_RETURN = 0.10 # give minecraft time to show all the keys pressed...

app = {                                 # REQUIRED dict, must be named 'app'
    'name' : 'Minecraft PE (effect)',   # Application name
    #
    # /effect <player: target> <effect: Effect>
    #         [seconds: int] [amplifier: int] [hideParticles: Boolean]
    #
    'macros' : [                        # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x002000, 'speed',  [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s speed           999999999 1 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x002000, 'str',    [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s strength        999999999 1 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x002000, 'haste',  [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s haste           999999999 1 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        # 2nd row ----------
        (0x002000, 'jump',   [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s jump_boost      999999999 1 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x000030, 'breath', [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s water_breathing 999999999 0 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x202020, 'darkv',  [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s night_vision    999999999 0 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        # 3rd row ----------
        (0x300000, 'health', [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s health_boost    999999999 4 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x300000, 'regen',  [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s regeneration    999999999 4 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x002000, 'absorb', [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s absorption      999999999 3 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        # 4th row ---------
        (0x002000, 'resist', [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s resistance      999999999 3 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x101010, 'invis',  [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s invisibility    999999999 0 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        (0x300000, 'fire_r', [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s fire_resistance 999999999 0 true"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
        # Encoder button --- Remove all status effects....
        (0x000000, '', [
            Type("/"), DELAY_AFTER_SLASH,
            Type("effect @s clear"),
            DELAY_BEFORE_RETURN, S("RETURN"), -S("RETURN")]),
    ]
}
