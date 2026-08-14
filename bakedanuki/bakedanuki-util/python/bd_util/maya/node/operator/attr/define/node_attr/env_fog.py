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


class FilterSizePlugOperator(
    Float3CompoundBasePlugOperator["FilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filterSizeX", "fsx"),
        ("filterSizeY", "fsy"),
        ("filterSizeZ", "fsz"),
    )

    filterSizeX = FloatField(default_value=0.0, readable=False)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0, readable=False)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0, readable=False)
    fsz = filterSizeZ


class FilterSizeAttrOperator(
    Float3CompoundBaseAttrOperator[FilterSizePlugOperator]
):
    __slots__ = ()

    filterSizeX = FloatField(default_value=0.0, readable=False)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0, readable=False)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0, readable=False)
    fsz = filterSizeZ


class FilterSizeField(
    Float3CompoundBaseField[FilterSizeAttrOperator, FilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterSizeAttrOperator
    PLUG_CLS = FilterSizePlugOperator

    filterSizeX = FloatField(default_value=0.0, readable=False)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0, readable=False)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0, readable=False)
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

    lightDirection = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, readable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, readable=False)
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

    lightDirection = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=True, readable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True, readable=False)
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


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
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

    outMatteOpacityR = FloatField(default_value=0.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=0.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=0.0, writable=False)
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField(default_value=0.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=0.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=0.0, writable=False)
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[
        OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField(default_value=0.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=0.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=0.0, writable=False)
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

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
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

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
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

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
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

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
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

    rayDirectionX = FloatField(default_value=0.0)
    rx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    ry = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField(default_value=0.0)
    rx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    ry = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField(default_value=0.0)
    rx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    ry = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
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

    fogColorR = FloatField(default_value=1.0)
    fcr = fogColorR

    fogColorG = FloatField(default_value=1.0)
    fcg = fogColorG

    fogColorB = FloatField(default_value=1.0)
    fcb = fogColorB


class FogColorAttrOperator(
    Float3CompoundBaseAttrOperator[FogColorPlugOperator]
):
    __slots__ = ()

    fogColorR = FloatField(default_value=1.0)
    fcr = fogColorR

    fogColorG = FloatField(default_value=1.0)
    fcg = fogColorG

    fogColorB = FloatField(default_value=1.0)
    fcb = fogColorB


class FogColorField(
    Float3CompoundBaseField[FogColorAttrOperator, FogColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogColorAttrOperator
    PLUG_CLS = FogColorPlugOperator

    fogColorR = FloatField(default_value=1.0)
    fcr = fogColorR

    fogColorG = FloatField(default_value=1.0)
    fcg = fogColorG

    fogColorB = FloatField(default_value=1.0)
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

    fogOpacityR = FloatField(default_value=0.5)
    for_ = fogOpacityR

    fogOpacityG = FloatField(default_value=0.5)
    fog = fogOpacityG

    fogOpacityB = FloatField(default_value=0.5)
    fob = fogOpacityB


class FogOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[FogOpacityPlugOperator]
):
    __slots__ = ()

    fogOpacityR = FloatField(default_value=0.5)
    for_ = fogOpacityR

    fogOpacityG = FloatField(default_value=0.5)
    fog = fogOpacityG

    fogOpacityB = FloatField(default_value=0.5)
    fob = fogOpacityB


class FogOpacityField(
    Float3CompoundBaseField[FogOpacityAttrOperator, FogOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogOpacityAttrOperator
    PLUG_CLS = FogOpacityPlugOperator

    fogOpacityR = FloatField(default_value=0.5)
    for_ = fogOpacityR

    fogOpacityG = FloatField(default_value=0.5)
    fog = fogOpacityG

    fogOpacityB = FloatField(default_value=0.5)
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

    airColorR = FloatField(default_value=0.6000000238418579)
    acr = airColorR

    airColorG = FloatField(default_value=0.800000011920929)
    acg = airColorG

    airColorB = FloatField(default_value=1.0)
    acb = airColorB


class AirColorAttrOperator(
    Float3CompoundBaseAttrOperator[AirColorPlugOperator]
):
    __slots__ = ()

    airColorR = FloatField(default_value=0.6000000238418579)
    acr = airColorR

    airColorG = FloatField(default_value=0.800000011920929)
    acg = airColorG

    airColorB = FloatField(default_value=1.0)
    acb = airColorB


class AirColorField(
    Float3CompoundBaseField[AirColorAttrOperator, AirColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AirColorAttrOperator
    PLUG_CLS = AirColorPlugOperator

    airColorR = FloatField(default_value=0.6000000238418579)
    acr = airColorR

    airColorG = FloatField(default_value=0.800000011920929)
    acg = airColorG

    airColorB = FloatField(default_value=1.0)
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

    airOpacityR = FloatField(default_value=0.3700000047683716)
    aor = airOpacityR

    airOpacityG = FloatField(default_value=0.4699999988079071)
    aog = airOpacityG

    airOpacityB = FloatField(default_value=0.8999999761581421)
    aob = airOpacityB


class AirOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[AirOpacityPlugOperator]
):
    __slots__ = ()

    airOpacityR = FloatField(default_value=0.3700000047683716)
    aor = airOpacityR

    airOpacityG = FloatField(default_value=0.4699999988079071)
    aog = airOpacityG

    airOpacityB = FloatField(default_value=0.8999999761581421)
    aob = airOpacityB


class AirOpacityField(
    Float3CompoundBaseField[AirOpacityAttrOperator, AirOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AirOpacityAttrOperator
    PLUG_CLS = AirOpacityPlugOperator

    airOpacityR = FloatField(default_value=0.3700000047683716)
    aor = airOpacityR

    airOpacityG = FloatField(default_value=0.4699999988079071)
    aog = airOpacityG

    airOpacityB = FloatField(default_value=0.8999999761581421)
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

    waterColorR = FloatField(default_value=0.6000000238418579)
    wcr = waterColorR

    waterColorG = FloatField(default_value=0.800000011920929)
    wcg = waterColorG

    waterColorB = FloatField(default_value=1.0)
    wcb = waterColorB


class WaterColorAttrOperator(
    Float3CompoundBaseAttrOperator[WaterColorPlugOperator]
):
    __slots__ = ()

    waterColorR = FloatField(default_value=0.6000000238418579)
    wcr = waterColorR

    waterColorG = FloatField(default_value=0.800000011920929)
    wcg = waterColorG

    waterColorB = FloatField(default_value=1.0)
    wcb = waterColorB


class WaterColorField(
    Float3CompoundBaseField[WaterColorAttrOperator, WaterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaterColorAttrOperator
    PLUG_CLS = WaterColorPlugOperator

    waterColorR = FloatField(default_value=0.6000000238418579)
    wcr = waterColorR

    waterColorG = FloatField(default_value=0.800000011920929)
    wcg = waterColorG

    waterColorB = FloatField(default_value=1.0)
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

    waterOpacityR = FloatField(default_value=0.3700000047683716)
    wor = waterOpacityR

    waterOpacityG = FloatField(default_value=0.4699999988079071)
    wog = waterOpacityG

    waterOpacityB = FloatField(default_value=0.8999999761581421)
    wob = waterOpacityB


class WaterOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[WaterOpacityPlugOperator]
):
    __slots__ = ()

    waterOpacityR = FloatField(default_value=0.3700000047683716)
    wor = waterOpacityR

    waterOpacityG = FloatField(default_value=0.4699999988079071)
    wog = waterOpacityG

    waterOpacityB = FloatField(default_value=0.8999999761581421)
    wob = waterOpacityB


class WaterOpacityField(
    Float3CompoundBaseField[WaterOpacityAttrOperator, WaterOpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaterOpacityAttrOperator
    PLUG_CLS = WaterOpacityPlugOperator

    waterOpacityR = FloatField(default_value=0.3700000047683716)
    wor = waterOpacityR

    waterOpacityG = FloatField(default_value=0.4699999988079071)
    wog = waterOpacityG

    waterOpacityB = FloatField(default_value=0.8999999761581421)
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

    sunColorR = FloatField(default_value=1.0)
    snr = sunColorR

    sunColorG = FloatField(default_value=1.0)
    sng = sunColorG

    sunColorB = FloatField(default_value=1.0)
    snb = sunColorB


class SunColorAttrOperator(
    Float3CompoundBaseAttrOperator[SunColorPlugOperator]
):
    __slots__ = ()

    sunColorR = FloatField(default_value=1.0)
    snr = sunColorR

    sunColorG = FloatField(default_value=1.0)
    sng = sunColorG

    sunColorB = FloatField(default_value=1.0)
    snb = sunColorB


class SunColorField(
    Float3CompoundBaseField[SunColorAttrOperator, SunColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunColorAttrOperator
    PLUG_CLS = SunColorPlugOperator

    sunColorR = FloatField(default_value=1.0)
    snr = sunColorR

    sunColorG = FloatField(default_value=1.0)
    sng = sunColorG

    sunColorB = FloatField(default_value=1.0)
    snb = sunColorB
