# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
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

    positionOffsetX = FloatField()
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField()
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField()
    position_offsetz = positionOffsetZ


class PositionOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[PositionOffsetPlugOperator]
):
    __slots__ = ()

    positionOffsetX = FloatField()
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField()
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField()
    position_offsetz = positionOffsetZ


class PositionOffsetField(
    Float3CompoundBaseField[PositionOffsetAttrOperator, PositionOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionOffsetAttrOperator
    PLUG_CLS = PositionOffsetPlugOperator

    positionOffsetX = FloatField()
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField()
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField()
    position_offsetz = positionOffsetZ
