# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ValuePlugOperator(
    Float3CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = FloatField()
    vx = valueX

    valueY = FloatField()
    vy = valueY

    valueZ = FloatField()
    vz = valueZ


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueX = FloatField()
    vx = valueX

    valueY = FloatField()
    vy = valueY

    valueZ = FloatField()
    vz = valueZ


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = FloatField()
    vx = valueX

    valueY = FloatField()
    vy = valueY

    valueZ = FloatField()
    vz = valueZ


class GammaPlugOperator(
    Float3CompoundBasePlugOperator["GammaAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gammaX", "gx"),
        ("gammaY", "gy"),
        ("gammaZ", "gz"),
    )

    gammaX = FloatField()
    gx = gammaX

    gammaY = FloatField()
    gy = gammaY

    gammaZ = FloatField()
    gz = gammaZ


class GammaAttrOperator(
    Float3CompoundBaseAttrOperator[GammaPlugOperator]
):
    __slots__ = ()

    gammaX = FloatField()
    gx = gammaX

    gammaY = FloatField()
    gy = gammaY

    gammaZ = FloatField()
    gz = gammaZ


class GammaField(
    Float3CompoundBaseField[GammaAttrOperator, GammaPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GammaAttrOperator
    PLUG_CLS = GammaPlugOperator

    gammaX = FloatField()
    gx = gammaX

    gammaY = FloatField()
    gy = gammaY

    gammaZ = FloatField()
    gz = gammaZ


class OutValuePlugOperator(
    Float3CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "ox"),
        ("outValueY", "oy"),
        ("outValueZ", "oz"),
    )

    outValueX = FloatField()
    ox = outValueX

    outValueY = FloatField()
    oy = outValueY

    outValueZ = FloatField()
    oz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField()
    ox = outValueX

    outValueY = FloatField()
    oy = outValueY

    outValueZ = FloatField()
    oz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField()
    ox = outValueX

    outValueY = FloatField()
    oy = outValueY

    outValueZ = FloatField()
    oz = outValueZ
