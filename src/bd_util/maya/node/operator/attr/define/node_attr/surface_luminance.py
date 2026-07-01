# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class LightDataArrayPlugOperator(
    LightDataPlugOperator["LightDataArrayAttrOperator"]
):
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

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayField(
    LightDataField[LightDataArrayAttrOperator, LightDataArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataArrayAttrOperator
    PLUG_CLS = LightDataArrayPlugOperator
