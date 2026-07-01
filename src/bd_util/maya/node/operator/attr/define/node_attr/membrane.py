# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class GravityDirectionPlugOperator(
    Float3CompoundBasePlugOperator["GravityDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gravityDirectionX", "grdx"),
        ("gravityDirectionY", "grdy"),
        ("gravityDirectionZ", "grdz"),
    )

    gravityDirectionX = FloatField()
    grdx = gravityDirectionX

    gravityDirectionY = FloatField()
    grdy = gravityDirectionY

    gravityDirectionZ = FloatField()
    grdz = gravityDirectionZ


class GravityDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[GravityDirectionPlugOperator]
):
    __slots__ = ()

    gravityDirectionX = FloatField()
    grdx = gravityDirectionX

    gravityDirectionY = FloatField()
    grdy = gravityDirectionY

    gravityDirectionZ = FloatField()
    grdz = gravityDirectionZ


class GravityDirectionField(
    Float3CompoundBaseField[GravityDirectionAttrOperator, GravityDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravityDirectionAttrOperator
    PLUG_CLS = GravityDirectionPlugOperator

    gravityDirectionX = FloatField()
    grdx = gravityDirectionX

    gravityDirectionY = FloatField()
    grdy = gravityDirectionY

    gravityDirectionZ = FloatField()
    grdz = gravityDirectionZ


class WindDirectionPlugOperator(
    Float3CompoundBasePlugOperator["WindDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("windDirectionX", "widx"),
        ("windDirectionY", "widy"),
        ("windDirectionZ", "widz"),
    )

    windDirectionX = FloatField()
    widx = windDirectionX

    windDirectionY = FloatField()
    widy = windDirectionY

    windDirectionZ = FloatField()
    widz = windDirectionZ


class WindDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[WindDirectionPlugOperator]
):
    __slots__ = ()

    windDirectionX = FloatField()
    widx = windDirectionX

    windDirectionY = FloatField()
    widy = windDirectionY

    windDirectionZ = FloatField()
    widz = windDirectionZ


class WindDirectionField(
    Float3CompoundBaseField[WindDirectionAttrOperator, WindDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WindDirectionAttrOperator
    PLUG_CLS = WindDirectionPlugOperator

    windDirectionX = FloatField()
    widx = windDirectionX

    windDirectionY = FloatField()
    widy = windDirectionY

    windDirectionZ = FloatField()
    widz = windDirectionZ


class TurbulenceOffsetPlugOperator(
    Float3CompoundBasePlugOperator["TurbulenceOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("turbulenceOffsetX", "tox"),
        ("turbulenceOffsetY", "toy"),
        ("turbulenceOffsetZ", "toz"),
    )

    turbulenceOffsetX = FloatField()
    tox = turbulenceOffsetX

    turbulenceOffsetY = FloatField()
    toy = turbulenceOffsetY

    turbulenceOffsetZ = FloatField()
    toz = turbulenceOffsetZ


class TurbulenceOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    turbulenceOffsetX = FloatField()
    tox = turbulenceOffsetX

    turbulenceOffsetY = FloatField()
    toy = turbulenceOffsetY

    turbulenceOffsetZ = FloatField()
    toz = turbulenceOffsetZ


class TurbulenceOffsetField(
    Float3CompoundBaseField[TurbulenceOffsetAttrOperator, TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceOffsetAttrOperator
    PLUG_CLS = TurbulenceOffsetPlugOperator

    turbulenceOffsetX = FloatField()
    tox = turbulenceOffsetX

    turbulenceOffsetY = FloatField()
    toy = turbulenceOffsetY

    turbulenceOffsetZ = FloatField()
    toz = turbulenceOffsetZ
