# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_composite import (
    AField,
    BField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    A = 0
    B = 1
    ATOP = 2
    AVERAGE = 3
    COJOINT_OVER = 4
    DIFFERENCE = 5
    DISJOINT_OVER = 6
    DIVIDE = 7
    EXCLUSION = 8
    FROM = 9
    GEOMETRIC = 10
    HARD_LIGHT = 11
    HYPOT_DIAGONAL = 12
    IN = 13
    MASK = 14
    MATTE = 15
    MAX = 16
    MIN = 17
    MINUS = 18
    MULTIPLY = 19
    OUT = 20
    OVER = 21
    OVERLAY = 22
    PLUS = 23
    SCREEN = 24
    SOFT_LIGHT = 25
    STENCIL = 26
    UNDER = 27
    XOR = 28


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    A = 0
    B = 1
    ATOP = 2
    AVERAGE = 3
    COJOINT_OVER = 4
    DIFFERENCE = 5
    DISJOINT_OVER = 6
    DIVIDE = 7
    EXCLUSION = 8
    FROM = 9
    GEOMETRIC = 10
    HARD_LIGHT = 11
    HYPOT_DIAGONAL = 12
    IN = 13
    MASK = 14
    MATTE = 15
    MAX = 16
    MIN = 17
    MINUS = 18
    MULTIPLY = 19
    OUT = 20
    OVER = 21
    OVERLAY = 22
    PLUS = 23
    SCREEN = 24
    SOFT_LIGHT = 25
    STENCIL = 26
    UNDER = 27
    XOR = 28

    NAME_MAP = {
        A: "A",
        B: "B",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        HARD_LIGHT: "hard_light",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PLUS: "plus",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        UNDER: "under",
        XOR: "xor",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class AlphaOperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SAME = 0
    A = 1
    B = 2


class AlphaOperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SAME = 0
    A = 1
    B = 2

    NAME_MAP = {
        SAME: "same",
        A: "A",
        B: "B",
    }


class AlphaOperationEnumField(
    EnumField[AlphaOperationEnumAttrOperator, AlphaOperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaOperationEnumAttrOperator
    PLUG_CLS = AlphaOperationEnumPlugOperator


class GeneratedAiComposite(DG):
    __slots__ = ()

    NODE_TYPE = "aiComposite"

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

    AA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    Aa = AA

    A = AField(default_value=(1.0, 0.0, 0.0))
    AR = A.AR
    Ar = AR
    AG = A.AG
    Ag = AG
    AB = A.AB
    Ab = AB

    BA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    Ba = BA

    B = BField(default_value=(0.0, 1.0, 0.0))
    BR = B.BR
    Br = BR
    BG = B.BG
    Bg = BG
    BB = B.BB
    Bb = BB

    operation = OperationEnumField(default_value=21)

    alphaOperation = AlphaOperationEnumField(default_value=0)
    alpha_operation = alphaOperation
