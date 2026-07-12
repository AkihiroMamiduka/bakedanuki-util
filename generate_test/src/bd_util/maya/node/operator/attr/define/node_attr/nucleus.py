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


class PlaneOriginPlugOperator(
    Float3CompoundBasePlugOperator["PlaneOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("planeOriginX", "npox"),
        ("planeOriginY", "npoy"),
        ("planeOriginZ", "npoz"),
    )

    planeOriginX = FloatField(default_value=0.0)
    npox = planeOriginX

    planeOriginY = FloatField(default_value=0.0)
    npoy = planeOriginY

    planeOriginZ = FloatField(default_value=0.0)
    npoz = planeOriginZ


class PlaneOriginAttrOperator(
    Float3CompoundBaseAttrOperator[PlaneOriginPlugOperator]
):
    __slots__ = ()

    planeOriginX = FloatField(default_value=0.0)
    npox = planeOriginX

    planeOriginY = FloatField(default_value=0.0)
    npoy = planeOriginY

    planeOriginZ = FloatField(default_value=0.0)
    npoz = planeOriginZ


class PlaneOriginField(
    Float3CompoundBaseField[PlaneOriginAttrOperator, PlaneOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PlaneOriginAttrOperator
    PLUG_CLS = PlaneOriginPlugOperator

    planeOriginX = FloatField(default_value=0.0)
    npox = planeOriginX

    planeOriginY = FloatField(default_value=0.0)
    npoy = planeOriginY

    planeOriginZ = FloatField(default_value=0.0)
    npoz = planeOriginZ


class PlaneNormalPlugOperator(
    Float3CompoundBasePlugOperator["PlaneNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("planeNormalX", "npnx"),
        ("planeNormalY", "npny"),
        ("planeNormalZ", "npnz"),
    )

    planeNormalX = FloatField(default_value=0.0)
    npnx = planeNormalX

    planeNormalY = FloatField(default_value=1.0)
    npny = planeNormalY

    planeNormalZ = FloatField(default_value=0.0)
    npnz = planeNormalZ


class PlaneNormalAttrOperator(
    Float3CompoundBaseAttrOperator[PlaneNormalPlugOperator]
):
    __slots__ = ()

    planeNormalX = FloatField(default_value=0.0)
    npnx = planeNormalX

    planeNormalY = FloatField(default_value=1.0)
    npny = planeNormalY

    planeNormalZ = FloatField(default_value=0.0)
    npnz = planeNormalZ


class PlaneNormalField(
    Float3CompoundBaseField[PlaneNormalAttrOperator, PlaneNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PlaneNormalAttrOperator
    PLUG_CLS = PlaneNormalPlugOperator

    planeNormalX = FloatField(default_value=0.0)
    npnx = planeNormalX

    planeNormalY = FloatField(default_value=1.0)
    npny = planeNormalY

    planeNormalZ = FloatField(default_value=0.0)
    npnz = planeNormalZ
