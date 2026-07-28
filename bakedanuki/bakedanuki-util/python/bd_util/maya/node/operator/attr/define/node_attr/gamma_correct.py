# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ValuePlugOperator(Float3CompoundBasePlugOperator["ValueAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = FloatField(default_value=0.0)
    vx = valueX

    valueY = FloatField(default_value=0.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0)
    vz = valueZ


class ValueAttrOperator(Float3CompoundBaseAttrOperator[ValuePlugOperator]):
    __slots__ = ()

    valueX = FloatField(default_value=0.0)
    vx = valueX

    valueY = FloatField(default_value=0.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0)
    vz = valueZ


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = FloatField(default_value=0.0)
    vx = valueX

    valueY = FloatField(default_value=0.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0)
    vz = valueZ


class GammaPlugOperator(Float3CompoundBasePlugOperator["GammaAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gammaX", "gx"),
        ("gammaY", "gy"),
        ("gammaZ", "gz"),
    )

    gammaX = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gx = gammaX

    gammaY = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gy = gammaY

    gammaZ = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gz = gammaZ


class GammaAttrOperator(Float3CompoundBaseAttrOperator[GammaPlugOperator]):
    __slots__ = ()

    gammaX = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gx = gammaX

    gammaY = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gy = gammaY

    gammaZ = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gz = gammaZ


class GammaField(
    Float3CompoundBaseField[GammaAttrOperator, GammaPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GammaAttrOperator
    PLUG_CLS = GammaPlugOperator

    gammaX = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gx = gammaX

    gammaY = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
    gy = gammaY

    gammaZ = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=5.0
    )
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

    outValueX = FloatField(default_value=0.0, writable=False)
    ox = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    oy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    oz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField(default_value=0.0, writable=False)
    ox = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    oy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    oz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField(default_value=0.0, writable=False)
    ox = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    oy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    oz = outValueZ
