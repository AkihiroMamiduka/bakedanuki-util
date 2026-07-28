# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


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


class PositionOffsetPlugOperator(
    Float3CompoundBasePlugOperator["PositionOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOffsetX", "position_offsetx"),
        ("positionOffsetY", "position_offsety"),
        ("positionOffsetZ", "position_offsetz"),
    )

    positionOffsetX = FloatField(default_value=0.0)
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField(default_value=0.0)
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField(default_value=0.0)
    position_offsetz = positionOffsetZ


class PositionOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[PositionOffsetPlugOperator]
):
    __slots__ = ()

    positionOffsetX = FloatField(default_value=0.0)
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField(default_value=0.0)
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField(default_value=0.0)
    position_offsetz = positionOffsetZ


class PositionOffsetField(
    Float3CompoundBaseField[
        PositionOffsetAttrOperator, PositionOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PositionOffsetAttrOperator
    PLUG_CLS = PositionOffsetPlugOperator

    positionOffsetX = FloatField(default_value=0.0)
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField(default_value=0.0)
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField(default_value=0.0)
    position_offsetz = positionOffsetZ
