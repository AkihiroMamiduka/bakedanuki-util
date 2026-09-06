# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class Ramp_ramp_InterpEnumPlugOperator(
    EnumPlugOperator["Ramp_ramp_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Ramp_ramp_InterpEnumAttrOperator(
    EnumAttrOperator[Ramp_ramp_InterpEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Ramp_ramp_InterpEnumField(
    EnumField[
        Ramp_ramp_InterpEnumAttrOperator, Ramp_ramp_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Ramp_ramp_InterpEnumAttrOperator
    PLUG_CLS = Ramp_ramp_InterpEnumPlugOperator


class Ramp_ramp_ColorPlugOperator(
    Float3CompoundBasePlugOperator["Ramp_ramp_ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ramp_ColorR", "aiRampcvr"),
        ("ramp_ColorG", "aiRampcvg"),
        ("ramp_ColorB", "aiRampcvb"),
    )

    ramp_ColorR = FloatField()
    aiRampcvr = ramp_ColorR

    ramp_ColorG = FloatField()
    aiRampcvg = ramp_ColorG

    ramp_ColorB = FloatField()
    aiRampcvb = ramp_ColorB


class Ramp_ramp_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[Ramp_ramp_ColorPlugOperator]
):
    __slots__ = ()

    ramp_ColorR = FloatField()
    aiRampcvr = ramp_ColorR

    ramp_ColorG = FloatField()
    aiRampcvg = ramp_ColorG

    ramp_ColorB = FloatField()
    aiRampcvb = ramp_ColorB


class Ramp_ramp_ColorField(
    Float3CompoundBaseField[
        Ramp_ramp_ColorAttrOperator, Ramp_ramp_ColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Ramp_ramp_ColorAttrOperator
    PLUG_CLS = Ramp_ramp_ColorPlugOperator

    ramp_ColorR = FloatField()
    aiRampcvr = ramp_ColorR

    ramp_ColorG = FloatField()
    aiRampcvg = ramp_ColorG

    ramp_ColorB = FloatField()
    aiRampcvb = ramp_ColorB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class StartPlugOperator(Float3CompoundBasePlugOperator["StartAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("startX", "startx"),
        ("startY", "starty"),
        ("startZ", "startz"),
    )

    startX = FloatField(default_value=0.0)
    startx = startX

    startY = FloatField(default_value=0.0)
    starty = startY

    startZ = FloatField(default_value=0.0)
    startz = startZ


class StartAttrOperator(Float3CompoundBaseAttrOperator[StartPlugOperator]):
    __slots__ = ()

    startX = FloatField(default_value=0.0)
    startx = startX

    startY = FloatField(default_value=0.0)
    starty = startY

    startZ = FloatField(default_value=0.0)
    startz = startZ


class StartField(
    Float3CompoundBaseField[StartAttrOperator, StartPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StartAttrOperator
    PLUG_CLS = StartPlugOperator

    startX = FloatField(default_value=0.0)
    startx = startX

    startY = FloatField(default_value=0.0)
    starty = startY

    startZ = FloatField(default_value=0.0)
    startz = startZ


class EndPlugOperator(Float3CompoundBasePlugOperator["EndAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("endX", "endx"),
        ("endY", "endy"),
        ("endZ", "endz"),
    )

    endX = FloatField(default_value=1.0)
    endx = endX

    endY = FloatField(default_value=1.0)
    endy = endY

    endZ = FloatField(default_value=1.0)
    endz = endZ


class EndAttrOperator(Float3CompoundBaseAttrOperator[EndPlugOperator]):
    __slots__ = ()

    endX = FloatField(default_value=1.0)
    endx = endX

    endY = FloatField(default_value=1.0)
    endy = endY

    endZ = FloatField(default_value=1.0)
    endz = endZ


class EndField(Float3CompoundBaseField[EndAttrOperator, EndPlugOperator]):
    __slots__ = ()

    ATTR_CLS = EndAttrOperator
    PLUG_CLS = EndPlugOperator

    endX = FloatField(default_value=1.0)
    endx = endX

    endY = FloatField(default_value=1.0)
    endy = endY

    endZ = FloatField(default_value=1.0)
    endz = endZ


class RampPlugOperator(CompoundPlugOperator["RampAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ramp_Position", "aiRampp"),
        ("ramp_Color", "aiRampcv"),
        ("ramp_Interp", "aiRampi"),
    )

    ramp_Position = FloatField(default_value=0.0)
    aiRampp = ramp_Position

    ramp_Color = Ramp_ramp_ColorField(default_value=(0.0, 0.0, 0.0))
    aiRampcv = ramp_Color

    ramp_Interp = Ramp_ramp_InterpEnumField(default_value=1)
    aiRampi = ramp_Interp


class RampAttrOperator(CompoundAttrOperator[RampPlugOperator]):
    __slots__ = ()

    ramp_Position = FloatField(default_value=0.0)
    aiRampp = ramp_Position

    ramp_Color = Ramp_ramp_ColorField(default_value=(0.0, 0.0, 0.0))
    aiRampcv = ramp_Color

    ramp_Interp = Ramp_ramp_InterpEnumField(default_value=1)
    aiRampi = ramp_Interp


class RampField(CompoundField[RampAttrOperator, RampPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RampAttrOperator
    PLUG_CLS = RampPlugOperator
