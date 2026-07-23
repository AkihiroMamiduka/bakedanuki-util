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

    gravityDirectionX = FloatField(default_value=0.0)
    grdx = gravityDirectionX

    gravityDirectionY = FloatField(default_value=-1.0)
    grdy = gravityDirectionY

    gravityDirectionZ = FloatField(default_value=0.0)
    grdz = gravityDirectionZ


class GravityDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[GravityDirectionPlugOperator]
):
    __slots__ = ()

    gravityDirectionX = FloatField(default_value=0.0)
    grdx = gravityDirectionX

    gravityDirectionY = FloatField(default_value=-1.0)
    grdy = gravityDirectionY

    gravityDirectionZ = FloatField(default_value=0.0)
    grdz = gravityDirectionZ


class GravityDirectionField(
    Float3CompoundBaseField[GravityDirectionAttrOperator, GravityDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravityDirectionAttrOperator
    PLUG_CLS = GravityDirectionPlugOperator

    gravityDirectionX = FloatField(default_value=0.0)
    grdx = gravityDirectionX

    gravityDirectionY = FloatField(default_value=-1.0)
    grdy = gravityDirectionY

    gravityDirectionZ = FloatField(default_value=0.0)
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

    windDirectionX = FloatField(default_value=1.0)
    widx = windDirectionX

    windDirectionY = FloatField(default_value=0.0)
    widy = windDirectionY

    windDirectionZ = FloatField(default_value=0.0)
    widz = windDirectionZ


class WindDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[WindDirectionPlugOperator]
):
    __slots__ = ()

    windDirectionX = FloatField(default_value=1.0)
    widx = windDirectionX

    windDirectionY = FloatField(default_value=0.0)
    widy = windDirectionY

    windDirectionZ = FloatField(default_value=0.0)
    widz = windDirectionZ


class WindDirectionField(
    Float3CompoundBaseField[WindDirectionAttrOperator, WindDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WindDirectionAttrOperator
    PLUG_CLS = WindDirectionPlugOperator

    windDirectionX = FloatField(default_value=1.0)
    widx = windDirectionX

    windDirectionY = FloatField(default_value=0.0)
    widy = windDirectionY

    windDirectionZ = FloatField(default_value=0.0)
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

    turbulenceOffsetX = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    tox = turbulenceOffsetX

    turbulenceOffsetY = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toy = turbulenceOffsetY

    turbulenceOffsetZ = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toz = turbulenceOffsetZ


class TurbulenceOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    turbulenceOffsetX = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    tox = turbulenceOffsetX

    turbulenceOffsetY = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toy = turbulenceOffsetY

    turbulenceOffsetZ = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toz = turbulenceOffsetZ


class TurbulenceOffsetField(
    Float3CompoundBaseField[TurbulenceOffsetAttrOperator, TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceOffsetAttrOperator
    PLUG_CLS = TurbulenceOffsetPlugOperator

    turbulenceOffsetX = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    tox = turbulenceOffsetX

    turbulenceOffsetY = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toy = turbulenceOffsetY

    turbulenceOffsetZ = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toz = turbulenceOffsetZ
