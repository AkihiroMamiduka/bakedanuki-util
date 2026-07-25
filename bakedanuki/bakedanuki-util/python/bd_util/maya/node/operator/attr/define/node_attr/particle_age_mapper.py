# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class OutUvCoordPlugOperator(
    Float2CompoundBasePlugOperator["OutUvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outUCoord", "ouc"),
        ("outVCoord", "ovc"),
    )

    outUCoord = FloatField(default_value=0.0, writable=False)
    ouc = outUCoord

    outVCoord = FloatField(default_value=0.0, writable=False)
    ovc = outVCoord


class OutUvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[OutUvCoordPlugOperator]
):
    __slots__ = ()

    outUCoord = FloatField(default_value=0.0, writable=False)
    ouc = outUCoord

    outVCoord = FloatField(default_value=0.0, writable=False)
    ovc = outVCoord


class OutUvCoordField(
    Float2CompoundBaseField[OutUvCoordAttrOperator, OutUvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUvCoordAttrOperator
    PLUG_CLS = OutUvCoordPlugOperator

    outUCoord = FloatField(default_value=0.0, writable=False)
    ouc = outUCoord

    outVCoord = FloatField(default_value=0.0, writable=False)
    ovc = outVCoord
