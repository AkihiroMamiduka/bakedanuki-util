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

    valueX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vx = valueX

    valueY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vz = valueZ


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vx = valueX

    valueY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vz = valueZ


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vx = valueX

    valueY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vy = valueY

    valueZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    vz = valueZ


class ContrastPlugOperator(
    Float3CompoundBasePlugOperator["ContrastAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("contrastX", "cx"),
        ("contrastY", "cy"),
        ("contrastZ", "cz"),
    )

    contrastX = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cx = contrastX

    contrastY = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cy = contrastY

    contrastZ = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cz = contrastZ


class ContrastAttrOperator(
    Float3CompoundBaseAttrOperator[ContrastPlugOperator]
):
    __slots__ = ()

    contrastX = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cx = contrastX

    contrastY = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cy = contrastY

    contrastZ = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cz = contrastZ


class ContrastField(
    Float3CompoundBaseField[ContrastAttrOperator, ContrastPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContrastAttrOperator
    PLUG_CLS = ContrastPlugOperator

    contrastX = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cx = contrastX

    contrastY = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cy = contrastY

    contrastZ = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=5.0)
    cz = contrastZ


class BiasPlugOperator(
    Float3CompoundBasePlugOperator["BiasAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("biasX", "bx"),
        ("biasY", "by"),
        ("biasZ", "bz"),
    )

    biasX = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    bx = biasX

    biasY = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    by = biasY

    biasZ = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    bz = biasZ


class BiasAttrOperator(
    Float3CompoundBaseAttrOperator[BiasPlugOperator]
):
    __slots__ = ()

    biasX = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    bx = biasX

    biasY = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    by = biasY

    biasZ = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    bz = biasZ


class BiasField(
    Float3CompoundBaseField[BiasAttrOperator, BiasPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasAttrOperator
    PLUG_CLS = BiasPlugOperator

    biasX = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    bx = biasX

    biasY = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    by = biasY

    biasZ = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    bz = biasZ


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
