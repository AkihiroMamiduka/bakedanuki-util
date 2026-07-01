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


class ContrastPlugOperator(
    Float3CompoundBasePlugOperator["ContrastAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("contrastX", "cx"),
        ("contrastY", "cy"),
        ("contrastZ", "cz"),
    )

    contrastX = FloatField()
    cx = contrastX

    contrastY = FloatField()
    cy = contrastY

    contrastZ = FloatField()
    cz = contrastZ


class ContrastAttrOperator(
    Float3CompoundBaseAttrOperator[ContrastPlugOperator]
):
    __slots__ = ()

    contrastX = FloatField()
    cx = contrastX

    contrastY = FloatField()
    cy = contrastY

    contrastZ = FloatField()
    cz = contrastZ


class ContrastField(
    Float3CompoundBaseField[ContrastAttrOperator, ContrastPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContrastAttrOperator
    PLUG_CLS = ContrastPlugOperator

    contrastX = FloatField()
    cx = contrastX

    contrastY = FloatField()
    cy = contrastY

    contrastZ = FloatField()
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

    biasX = FloatField()
    bx = biasX

    biasY = FloatField()
    by = biasY

    biasZ = FloatField()
    bz = biasZ


class BiasAttrOperator(
    Float3CompoundBaseAttrOperator[BiasPlugOperator]
):
    __slots__ = ()

    biasX = FloatField()
    bx = biasX

    biasY = FloatField()
    by = biasY

    biasZ = FloatField()
    bz = biasZ


class BiasField(
    Float3CompoundBaseField[BiasAttrOperator, BiasPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasAttrOperator
    PLUG_CLS = BiasPlugOperator

    biasX = FloatField()
    bx = biasX

    biasY = FloatField()
    by = biasY

    biasZ = FloatField()
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
