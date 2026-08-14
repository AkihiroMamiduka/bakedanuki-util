# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float3Field,
)


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField(default_value=1.0, readable=False)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0, readable=False)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0, readable=False)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=1.0, readable=False)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0, readable=False)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0, readable=False)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=1.0, readable=False)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0, readable=False)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0, readable=False)
    pz = pointCameraZ


class LightDataPlugOperator(LightDataPlugOperator["LightDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirection", "ld"),
        ("lightIntensity", "li"),
        ("lightAmbient", "la"),
        ("lightDiffuse", "ldf"),
        ("lightSpecular", "ls"),
        ("lightShadowFraction", "lsf"),
        ("preShadowIntensity", "psi"),
        ("lightBlindData", "lbd"),
    )

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbd = lightBlindData


class LightDataAttrOperator(LightDataAttrOperator[LightDataPlugOperator]):
    __slots__ = ()

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbd = lightBlindData


class LightDataField(
    LightDataField[LightDataAttrOperator, LightDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataAttrOperator
    PLUG_CLS = LightDataPlugOperator

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbd = lightBlindData
