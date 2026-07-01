# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


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


class LightDataPlugOperator(
    LightDataPlugOperator["LightDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionOut", "ldo"),
        ("lightIntensityOut", "lw"),
        ("lightAmbientOut", "lya"),
        ("lightDiffuseOut", "lyf"),
        ("lightSpecularOut", "lys"),
        ("lightShadowFractionOut", "sfo"),
        ("preShadowIntensityOut", "psio"),
        ("lightBlindDataOut", "lbdo"),
    )

    lightDirectionOut = Float3Field()
    ldo = lightDirectionOut

    lightIntensityOut = Float3Field()
    lw = lightIntensityOut

    lightAmbientOut = BoolField()
    lya = lightAmbientOut

    lightDiffuseOut = BoolField()
    lyf = lightDiffuseOut

    lightSpecularOut = BoolField()
    lys = lightSpecularOut

    lightShadowFractionOut = FloatField()
    sfo = lightShadowFractionOut

    preShadowIntensityOut = FloatField()
    psio = preShadowIntensityOut

    lightBlindDataOut = AddrField()
    lbdo = lightBlindDataOut


class LightDataAttrOperator(
    LightDataAttrOperator[LightDataPlugOperator]
):
    __slots__ = ()

    lightDirectionOut = Float3Field()
    ldo = lightDirectionOut

    lightIntensityOut = Float3Field()
    lw = lightIntensityOut

    lightAmbientOut = BoolField()
    lya = lightAmbientOut

    lightDiffuseOut = BoolField()
    lyf = lightDiffuseOut

    lightSpecularOut = BoolField()
    lys = lightSpecularOut

    lightShadowFractionOut = FloatField()
    sfo = lightShadowFractionOut

    preShadowIntensityOut = FloatField()
    psio = preShadowIntensityOut

    lightBlindDataOut = AddrField()
    lbdo = lightBlindDataOut


class LightDataField(
    LightDataField[LightDataAttrOperator, LightDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataAttrOperator
    PLUG_CLS = LightDataPlugOperator

    lightDirectionOut = Float3Field()
    ldo = lightDirectionOut

    lightIntensityOut = Float3Field()
    lw = lightIntensityOut

    lightAmbientOut = BoolField()
    lya = lightAmbientOut

    lightDiffuseOut = BoolField()
    lyf = lightDiffuseOut

    lightSpecularOut = BoolField()
    lys = lightSpecularOut

    lightShadowFractionOut = FloatField()
    sfo = lightShadowFractionOut

    preShadowIntensityOut = FloatField()
    psio = preShadowIntensityOut

    lightBlindDataOut = AddrField()
    lbdo = lightBlindDataOut
