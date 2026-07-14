# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_layer_rgba import (
    Input1Field,
    Input2Field,
    Input3Field,
    Input4Field,
    Input5Field,
    Input6Field,
    Input7Field,
    Input8Field,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class Operation1EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation1EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation1EnumField(
    EnumField[Operation1EnumAttrOperator, Operation1EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation1EnumAttrOperator
    PLUG_CLS = Operation1EnumPlugOperator


class AlphaOperation1EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation1EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation1EnumField(
    EnumField[AlphaOperation1EnumAttrOperator, AlphaOperation1EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation1EnumAttrOperator
    PLUG_CLS = AlphaOperation1EnumPlugOperator


class Operation2EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation2EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation2EnumField(
    EnumField[Operation2EnumAttrOperator, Operation2EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation2EnumAttrOperator
    PLUG_CLS = Operation2EnumPlugOperator


class AlphaOperation2EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation2EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation2EnumField(
    EnumField[AlphaOperation2EnumAttrOperator, AlphaOperation2EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation2EnumAttrOperator
    PLUG_CLS = AlphaOperation2EnumPlugOperator


class Operation3EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation3EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation3EnumField(
    EnumField[Operation3EnumAttrOperator, Operation3EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation3EnumAttrOperator
    PLUG_CLS = Operation3EnumPlugOperator


class AlphaOperation3EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation3EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation3EnumField(
    EnumField[AlphaOperation3EnumAttrOperator, AlphaOperation3EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation3EnumAttrOperator
    PLUG_CLS = AlphaOperation3EnumPlugOperator


class Operation4EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation4EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation4EnumField(
    EnumField[Operation4EnumAttrOperator, Operation4EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation4EnumAttrOperator
    PLUG_CLS = Operation4EnumPlugOperator


class AlphaOperation4EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation4EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation4EnumField(
    EnumField[AlphaOperation4EnumAttrOperator, AlphaOperation4EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation4EnumAttrOperator
    PLUG_CLS = AlphaOperation4EnumPlugOperator


class Operation5EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation5EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation5EnumField(
    EnumField[Operation5EnumAttrOperator, Operation5EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation5EnumAttrOperator
    PLUG_CLS = Operation5EnumPlugOperator


class AlphaOperation5EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation5EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation5EnumField(
    EnumField[AlphaOperation5EnumAttrOperator, AlphaOperation5EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation5EnumAttrOperator
    PLUG_CLS = AlphaOperation5EnumPlugOperator


class Operation6EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation6EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation6EnumField(
    EnumField[Operation6EnumAttrOperator, Operation6EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation6EnumAttrOperator
    PLUG_CLS = Operation6EnumPlugOperator


class AlphaOperation6EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation6EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation6EnumField(
    EnumField[AlphaOperation6EnumAttrOperator, AlphaOperation6EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation6EnumAttrOperator
    PLUG_CLS = AlphaOperation6EnumPlugOperator


class Operation7EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation7EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation7EnumField(
    EnumField[Operation7EnumAttrOperator, Operation7EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation7EnumAttrOperator
    PLUG_CLS = Operation7EnumPlugOperator


class AlphaOperation7EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation7EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation7EnumField(
    EnumField[AlphaOperation7EnumAttrOperator, AlphaOperation7EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation7EnumAttrOperator
    PLUG_CLS = AlphaOperation7EnumPlugOperator


class Operation8EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class Operation8EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class Operation8EnumField(
    EnumField[Operation8EnumAttrOperator, Operation8EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Operation8EnumAttrOperator
    PLUG_CLS = Operation8EnumPlugOperator


class AlphaOperation8EnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3


class AlphaOperation8EnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RESULT = 0
    MASK = 1
    PRESERVE = 2
    OVERWRITE = 3

    NAME_MAP = {
        RESULT: "result",
        MASK: "mask",
        PRESERVE: "preserve",
        OVERWRITE: "overwrite",
    }


class AlphaOperation8EnumField(
    EnumField[AlphaOperation8EnumAttrOperator, AlphaOperation8EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperation8EnumAttrOperator
    PLUG_CLS = AlphaOperation8EnumPlugOperator


class AiLayerRgba(DG):
    __slots__ = ()

    NODE_TYPE = "aiLayerRgba"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    enable1 = BoolField(default_value=False)

    name1 = DataStringField()

    input1A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input1a = input1A

    input1 = Input1Field(default_value=(0.0, 0.0, 0.0))
    input1R = input1.input1R
    input1r = input1R
    input1G = input1.input1G
    input1g = input1G
    input1B = input1.input1B
    input1b = input1B

    mix1 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation1 = Operation1EnumField(default_value=26)

    alphaOperation1 = AlphaOperation1EnumField(default_value=0)
    alpha_operation1 = alphaOperation1

    enable2 = BoolField(default_value=False)

    name2 = DataStringField()

    input2A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input2a = input2A

    input2 = Input2Field(default_value=(0.0, 0.0, 0.0))
    input2R = input2.input2R
    input2r = input2R
    input2G = input2.input2G
    input2g = input2G
    input2B = input2.input2B
    input2b = input2B

    mix2 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation2 = Operation2EnumField(default_value=26)

    alphaOperation2 = AlphaOperation2EnumField(default_value=0)
    alpha_operation2 = alphaOperation2

    enable3 = BoolField(default_value=False)

    name3 = DataStringField()

    input3A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input3a = input3A

    input3 = Input3Field(default_value=(0.0, 0.0, 0.0))
    input3R = input3.input3R
    input3r = input3R
    input3G = input3.input3G
    input3g = input3G
    input3B = input3.input3B
    input3b = input3B

    mix3 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation3 = Operation3EnumField(default_value=26)

    alphaOperation3 = AlphaOperation3EnumField(default_value=0)
    alpha_operation3 = alphaOperation3

    enable4 = BoolField(default_value=False)

    name4 = DataStringField()

    input4A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input4a = input4A

    input4 = Input4Field(default_value=(0.0, 0.0, 0.0))
    input4R = input4.input4R
    input4r = input4R
    input4G = input4.input4G
    input4g = input4G
    input4B = input4.input4B
    input4b = input4B

    mix4 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation4 = Operation4EnumField(default_value=26)

    alphaOperation4 = AlphaOperation4EnumField(default_value=0)
    alpha_operation4 = alphaOperation4

    enable5 = BoolField(default_value=False)

    name5 = DataStringField()

    input5A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input5a = input5A

    input5 = Input5Field(default_value=(0.0, 0.0, 0.0))
    input5R = input5.input5R
    input5r = input5R
    input5G = input5.input5G
    input5g = input5G
    input5B = input5.input5B
    input5b = input5B

    mix5 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation5 = Operation5EnumField(default_value=26)

    alphaOperation5 = AlphaOperation5EnumField(default_value=0)
    alpha_operation5 = alphaOperation5

    enable6 = BoolField(default_value=False)

    name6 = DataStringField()

    input6A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input6a = input6A

    input6 = Input6Field(default_value=(0.0, 0.0, 0.0))
    input6R = input6.input6R
    input6r = input6R
    input6G = input6.input6G
    input6g = input6G
    input6B = input6.input6B
    input6b = input6B

    mix6 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation6 = Operation6EnumField(default_value=26)

    alphaOperation6 = AlphaOperation6EnumField(default_value=0)
    alpha_operation6 = alphaOperation6

    enable7 = BoolField(default_value=False)

    name7 = DataStringField()

    input7A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input7a = input7A

    input7 = Input7Field(default_value=(0.0, 0.0, 0.0))
    input7R = input7.input7R
    input7r = input7R
    input7G = input7.input7G
    input7g = input7G
    input7B = input7.input7B
    input7b = input7B

    mix7 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation7 = Operation7EnumField(default_value=26)

    alphaOperation7 = AlphaOperation7EnumField(default_value=0)
    alpha_operation7 = alphaOperation7

    enable8 = BoolField(default_value=False)

    name8 = DataStringField()

    input8A = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    input8a = input8A

    input8 = Input8Field(default_value=(0.0, 0.0, 0.0))
    input8R = input8.input8R
    input8r = input8R
    input8G = input8.input8G
    input8g = input8G
    input8B = input8.input8B
    input8b = input8B

    mix8 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    operation8 = Operation8EnumField(default_value=26)

    alphaOperation8 = AlphaOperation8EnumField(default_value=0)
    alpha_operation8 = alphaOperation8

    clamp = BoolField(default_value=False)
