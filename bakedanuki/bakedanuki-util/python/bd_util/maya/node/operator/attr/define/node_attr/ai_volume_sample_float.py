# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


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
