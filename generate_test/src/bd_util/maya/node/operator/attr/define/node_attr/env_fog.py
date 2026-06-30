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


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "pwx"),
        ("pointWorldY", "pwy"),
        ("pointWorldZ", "pwz"),
    )

    pointWorldX = FloatField()
    pwx = pointWorldX

    pointWorldY = FloatField()
    pwy = pointWorldY

    pointWorldZ = FloatField()
    pwz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField()
    pwx = pointWorldX

    pointWorldY = FloatField()
    pwy = pointWorldY

    pointWorldZ = FloatField()
    pwz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField()
    pwx = pointWorldX

    pointWorldY = FloatField()
    pwy = pointWorldY

    pointWorldZ = FloatField()
    pwz = pointWorldZ


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rx"),
        ("rayDirectionY", "ry"),
        ("rayDirectionZ", "rz"),
    )

    rayDirectionX = FloatField()
    rx = rayDirectionX

    rayDirectionY = FloatField()
    ry = rayDirectionY

    rayDirectionZ = FloatField()
    rz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField()
    rx = rayDirectionX

    rayDirectionY = FloatField()
    ry = rayDirectionY

    rayDirectionZ = FloatField()
    rz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField()
    rx = rayDirectionX

    rayDirectionY = FloatField()
    ry = rayDirectionY

    rayDirectionZ = FloatField()
    rz = rayDirectionZ


class FogColorPlugOperator(
    Float3CompoundBasePlugOperator["FogColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fogColorR", "fcr"),
        ("fogColorG", "fcg"),
        ("fogColorB", "fcb"),
    )

    fogColorR = FloatField()
    fcr = fogColorR

    fogColorG = FloatField()
    fcg = fogColorG

    fogColorB = FloatField()
    fcb = fogColorB


class FogColorAttrOperator(
    Float3CompoundBaseAttrOperator[FogColorPlugOperator]
):
    __slots__ = ()

    fogColorR = FloatField()
    fcr = fogColorR

    fogColorG = FloatField()
    fcg = fogColorG

    fogColorB = FloatField()
    fcb = fogColorB


class FogColorField(
    Float3CompoundBaseField[FogColorAttrOperator, FogColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogColorAttrOperator
    PLUG_CLS = FogColorPlugOperator

    fogColorR = FloatField()
    fcr = fogColorR

    fogColorG = FloatField()
    fcg = fogColorG

    fogColorB = FloatField()
    fcb = fogColorB


class FogOpacityPlugOperator(
    Float3CompoundBasePlugOperator["FogOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fogOpacityR", "for"),
        ("fogOpacityG", "fog"),
        ("fogOpacityB", "fob"),
    )

    fogOpacityR = FloatField()
    for_ = fogOpacityR

    fogOpacityG = FloatField()
    fog = fogOpacityG

    fogOpacityB = FloatField()
    fob = fogOpacityB


class FogOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[FogOpacityPlugOperator]
):
    __slots__ = ()

    fogOpacityR = FloatField()
    for_ = fogOpacityR

    fogOpacityG = FloatField()
    fog = fogOpacityG

    fogOpacityB = FloatField()
    fob = fogOpacityB


class FogOpacityField(
    Float3CompoundBaseField[FogOpacityAttrOperator, FogOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogOpacityAttrOperator
    PLUG_CLS = FogOpacityPlugOperator

    fogOpacityR = FloatField()
    for_ = fogOpacityR

    fogOpacityG = FloatField()
    fog = fogOpacityG

    fogOpacityB = FloatField()
    fob = fogOpacityB


class AirColorPlugOperator(
    Float3CompoundBasePlugOperator["AirColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("airColorR", "acr"),
        ("airColorG", "acg"),
        ("airColorB", "acb"),
    )

    airColorR = FloatField()
    acr = airColorR

    airColorG = FloatField()
    acg = airColorG

    airColorB = FloatField()
    acb = airColorB


class AirColorAttrOperator(
    Float3CompoundBaseAttrOperator[AirColorPlugOperator]
):
    __slots__ = ()

    airColorR = FloatField()
    acr = airColorR

    airColorG = FloatField()
    acg = airColorG

    airColorB = FloatField()
    acb = airColorB


class AirColorField(
    Float3CompoundBaseField[AirColorAttrOperator, AirColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AirColorAttrOperator
    PLUG_CLS = AirColorPlugOperator

    airColorR = FloatField()
    acr = airColorR

    airColorG = FloatField()
    acg = airColorG

    airColorB = FloatField()
    acb = airColorB


class AirOpacityPlugOperator(
    Float3CompoundBasePlugOperator["AirOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("airOpacityR", "aor"),
        ("airOpacityG", "aog"),
        ("airOpacityB", "aob"),
    )

    airOpacityR = FloatField()
    aor = airOpacityR

    airOpacityG = FloatField()
    aog = airOpacityG

    airOpacityB = FloatField()
    aob = airOpacityB


class AirOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[AirOpacityPlugOperator]
):
    __slots__ = ()

    airOpacityR = FloatField()
    aor = airOpacityR

    airOpacityG = FloatField()
    aog = airOpacityG

    airOpacityB = FloatField()
    aob = airOpacityB


class AirOpacityField(
    Float3CompoundBaseField[AirOpacityAttrOperator, AirOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AirOpacityAttrOperator
    PLUG_CLS = AirOpacityPlugOperator

    airOpacityR = FloatField()
    aor = airOpacityR

    airOpacityG = FloatField()
    aog = airOpacityG

    airOpacityB = FloatField()
    aob = airOpacityB


class WaterColorPlugOperator(
    Float3CompoundBasePlugOperator["WaterColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waterColorR", "wcr"),
        ("waterColorG", "wcg"),
        ("waterColorB", "wcb"),
    )

    waterColorR = FloatField()
    wcr = waterColorR

    waterColorG = FloatField()
    wcg = waterColorG

    waterColorB = FloatField()
    wcb = waterColorB


class WaterColorAttrOperator(
    Float3CompoundBaseAttrOperator[WaterColorPlugOperator]
):
    __slots__ = ()

    waterColorR = FloatField()
    wcr = waterColorR

    waterColorG = FloatField()
    wcg = waterColorG

    waterColorB = FloatField()
    wcb = waterColorB


class WaterColorField(
    Float3CompoundBaseField[WaterColorAttrOperator, WaterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaterColorAttrOperator
    PLUG_CLS = WaterColorPlugOperator

    waterColorR = FloatField()
    wcr = waterColorR

    waterColorG = FloatField()
    wcg = waterColorG

    waterColorB = FloatField()
    wcb = waterColorB


class WaterOpacityPlugOperator(
    Float3CompoundBasePlugOperator["WaterOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waterOpacityR", "wor"),
        ("waterOpacityG", "wog"),
        ("waterOpacityB", "wob"),
    )

    waterOpacityR = FloatField()
    wor = waterOpacityR

    waterOpacityG = FloatField()
    wog = waterOpacityG

    waterOpacityB = FloatField()
    wob = waterOpacityB


class WaterOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[WaterOpacityPlugOperator]
):
    __slots__ = ()

    waterOpacityR = FloatField()
    wor = waterOpacityR

    waterOpacityG = FloatField()
    wog = waterOpacityG

    waterOpacityB = FloatField()
    wob = waterOpacityB


class WaterOpacityField(
    Float3CompoundBaseField[WaterOpacityAttrOperator, WaterOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaterOpacityAttrOperator
    PLUG_CLS = WaterOpacityPlugOperator

    waterOpacityR = FloatField()
    wor = waterOpacityR

    waterOpacityG = FloatField()
    wog = waterOpacityG

    waterOpacityB = FloatField()
    wob = waterOpacityB


class SunColorPlugOperator(
    Float3CompoundBasePlugOperator["SunColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunColorR", "snr"),
        ("sunColorG", "sng"),
        ("sunColorB", "snb"),
    )

    sunColorR = FloatField()
    snr = sunColorR

    sunColorG = FloatField()
    sng = sunColorG

    sunColorB = FloatField()
    snb = sunColorB


class SunColorAttrOperator(
    Float3CompoundBaseAttrOperator[SunColorPlugOperator]
):
    __slots__ = ()

    sunColorR = FloatField()
    snr = sunColorR

    sunColorG = FloatField()
    sng = sunColorG

    sunColorB = FloatField()
    snb = sunColorB


class SunColorField(
    Float3CompoundBaseField[SunColorAttrOperator, SunColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunColorAttrOperator
    PLUG_CLS = SunColorPlugOperator

    sunColorR = FloatField()
    snr = sunColorR

    sunColorG = FloatField()
    sng = sunColorG

    sunColorB = FloatField()
    snb = sunColorB
