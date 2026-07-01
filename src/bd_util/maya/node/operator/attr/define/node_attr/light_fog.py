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


class FilterSizePlugOperator(
    Float3CompoundBasePlugOperator["FilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filterSizeX", "fsx"),
        ("filterSizeY", "fsy"),
        ("filterSizeZ", "fsz"),
    )

    filterSizeX = FloatField()
    fsx = filterSizeX

    filterSizeY = FloatField()
    fsy = filterSizeY

    filterSizeZ = FloatField()
    fsz = filterSizeZ


class FilterSizeAttrOperator(
    Float3CompoundBaseAttrOperator[FilterSizePlugOperator]
):
    __slots__ = ()

    filterSizeX = FloatField()
    fsx = filterSizeX

    filterSizeY = FloatField()
    fsy = filterSizeY

    filterSizeZ = FloatField()
    fsz = filterSizeZ


class FilterSizeField(
    Float3CompoundBaseField[FilterSizeAttrOperator, FilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterSizeAttrOperator
    PLUG_CLS = FilterSizePlugOperator

    filterSizeX = FloatField()
    fsx = filterSizeX

    filterSizeY = FloatField()
    fsy = filterSizeY

    filterSizeZ = FloatField()
    fsz = filterSizeZ


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


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class OutMatteOpacityPlugOperator(
    Float3CompoundBasePlugOperator["OutMatteOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outMatteOpacityR", "omor"),
        ("outMatteOpacityG", "omog"),
        ("outMatteOpacityB", "omob"),
    )

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField()
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField()
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField()
    omob = outMatteOpacityB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB
