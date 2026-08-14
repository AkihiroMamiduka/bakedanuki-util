# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import Float3Field


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

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, readable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, readable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, readable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, readable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, readable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, readable=False)
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, readable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, readable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, readable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, readable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, readable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, readable=False)
    lbd = lightBlindData


class LightDataArrayField(
    LightDataField[LightDataArrayAttrOperator, LightDataArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataArrayAttrOperator
    PLUG_CLS = LightDataArrayPlugOperator


class LightDataPlugOperator(LightDataPlugOperator["LightDataAttrOperator"]):
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

    lightDirectionOut = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ldo = lightDirectionOut

    lightIntensityOut = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    lw = lightIntensityOut

    lightAmbientOut = BoolField(default_value=False, writable=False)
    lya = lightAmbientOut

    lightDiffuseOut = BoolField(default_value=False, writable=False)
    lyf = lightDiffuseOut

    lightSpecularOut = BoolField(default_value=False, writable=False)
    lys = lightSpecularOut

    lightShadowFractionOut = FloatField(default_value=0.0, writable=False)
    sfo = lightShadowFractionOut

    preShadowIntensityOut = FloatField(default_value=0.0, writable=False)
    psio = preShadowIntensityOut

    lightBlindDataOut = AddrField(default_value=0.0, writable=False)
    lbdo = lightBlindDataOut


class LightDataAttrOperator(LightDataAttrOperator[LightDataPlugOperator]):
    __slots__ = ()

    lightDirectionOut = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ldo = lightDirectionOut

    lightIntensityOut = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    lw = lightIntensityOut

    lightAmbientOut = BoolField(default_value=False, writable=False)
    lya = lightAmbientOut

    lightDiffuseOut = BoolField(default_value=False, writable=False)
    lyf = lightDiffuseOut

    lightSpecularOut = BoolField(default_value=False, writable=False)
    lys = lightSpecularOut

    lightShadowFractionOut = FloatField(default_value=0.0, writable=False)
    sfo = lightShadowFractionOut

    preShadowIntensityOut = FloatField(default_value=0.0, writable=False)
    psio = preShadowIntensityOut

    lightBlindDataOut = AddrField(default_value=0.0, writable=False)
    lbdo = lightBlindDataOut


class LightDataField(
    LightDataField[LightDataAttrOperator, LightDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataAttrOperator
    PLUG_CLS = LightDataPlugOperator

    lightDirectionOut = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ldo = lightDirectionOut

    lightIntensityOut = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    lw = lightIntensityOut

    lightAmbientOut = BoolField(default_value=False, writable=False)
    lya = lightAmbientOut

    lightDiffuseOut = BoolField(default_value=False, writable=False)
    lyf = lightDiffuseOut

    lightSpecularOut = BoolField(default_value=False, writable=False)
    lys = lightSpecularOut

    lightShadowFractionOut = FloatField(default_value=0.0, writable=False)
    sfo = lightShadowFractionOut

    preShadowIntensityOut = FloatField(default_value=0.0, writable=False)
    psio = preShadowIntensityOut

    lightBlindDataOut = AddrField(default_value=0.0, writable=False)
    lbdo = lightBlindDataOut
