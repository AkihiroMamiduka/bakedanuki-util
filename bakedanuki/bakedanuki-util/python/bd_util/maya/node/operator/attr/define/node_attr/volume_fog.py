# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float3Field,
)


class ColorRamp_InterpEnumPlugOperator(
    EnumPlugOperator["ColorRamp_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ColorRamp_InterpEnumAttrOperator(
    EnumAttrOperator[ColorRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class ColorRamp_InterpEnumField(
    EnumField[
        ColorRamp_InterpEnumAttrOperator, ColorRamp_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorRamp_InterpEnumAttrOperator
    PLUG_CLS = ColorRamp_InterpEnumPlugOperator


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rdx"),
        ("rayDirectionY", "rdy"),
        ("rayDirectionZ", "rdz"),
    )

    rayDirectionX = FloatField(default_value=0.0)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rdz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField(default_value=0.0)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rdz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField(default_value=0.0)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rdz = rayDirectionZ


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


class FarPointWorldPlugOperator(
    Float3CompoundBasePlugOperator["FarPointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farPointWorldX", "fwx"),
        ("farPointWorldY", "fwy"),
        ("farPointWorldZ", "fwz"),
    )

    farPointWorldX = FloatField(default_value=1.0)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0)
    fwz = farPointWorldZ


class FarPointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[FarPointWorldPlugOperator]
):
    __slots__ = ()

    farPointWorldX = FloatField(default_value=1.0)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0)
    fwz = farPointWorldZ


class FarPointWorldField(
    Float3CompoundBaseField[
        FarPointWorldAttrOperator, FarPointWorldPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FarPointWorldAttrOperator
    PLUG_CLS = FarPointWorldPlugOperator

    farPointWorldX = FloatField(default_value=1.0)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0)
    fwz = farPointWorldZ


class PointObjPlugOperator(
    Float3CompoundBasePlugOperator["PointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointObjX", "pox"),
        ("pointObjY", "poy"),
        ("pointObjZ", "poz"),
    )

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class FarPointObjPlugOperator(
    Float3CompoundBasePlugOperator["FarPointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farPointObjectX", "fox"),
        ("farPointObjectY", "foy"),
        ("farPointObjectZ", "foz"),
    )

    farPointObjectX = FloatField(default_value=1.0)
    fox = farPointObjectX

    farPointObjectY = FloatField(default_value=1.0)
    foy = farPointObjectY

    farPointObjectZ = FloatField(default_value=1.0)
    foz = farPointObjectZ


class FarPointObjAttrOperator(
    Float3CompoundBaseAttrOperator[FarPointObjPlugOperator]
):
    __slots__ = ()

    farPointObjectX = FloatField(default_value=1.0)
    fox = farPointObjectX

    farPointObjectY = FloatField(default_value=1.0)
    foy = farPointObjectY

    farPointObjectZ = FloatField(default_value=1.0)
    foz = farPointObjectZ


class FarPointObjField(
    Float3CompoundBaseField[FarPointObjAttrOperator, FarPointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FarPointObjAttrOperator
    PLUG_CLS = FarPointObjPlugOperator

    farPointObjectX = FloatField(default_value=1.0)
    fox = farPointObjectX

    farPointObjectY = FloatField(default_value=1.0)
    foy = farPointObjectY

    farPointObjectZ = FloatField(default_value=1.0)
    foz = farPointObjectZ


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

    colorR = FloatField(default_value=0.8999999761581421)
    cr = colorR

    colorG = FloatField(default_value=0.8999999761581421)
    cg = colorG

    colorB = FloatField(default_value=0.8999999761581421)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.8999999761581421)
    cr = colorR

    colorG = FloatField(default_value=0.8999999761581421)
    cg = colorG

    colorB = FloatField(default_value=0.8999999761581421)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.8999999761581421)
    cr = colorR

    colorG = FloatField(default_value=0.8999999761581421)
    cg = colorG

    colorB = FloatField(default_value=0.8999999761581421)
    cb = colorB


class ColorRampPlugOperator(CompoundPlugOperator["ColorRampAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRamp_Position", "crmp"),
        ("colorRamp_Color", "crmc"),
        ("colorRamp_Interp", "crmi"),
    )

    colorRamp_Position = FloatField(default_value=0.0)
    crmp = colorRamp_Position

    colorRamp_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    crmc = colorRamp_Color

    colorRamp_Interp = ColorRamp_InterpEnumField(default_value=0)
    crmi = colorRamp_Interp


class ColorRampAttrOperator(CompoundAttrOperator[ColorRampPlugOperator]):
    __slots__ = ()

    colorRamp_Position = FloatField(default_value=0.0)
    crmp = colorRamp_Position

    colorRamp_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    crmc = colorRamp_Color

    colorRamp_Interp = ColorRamp_InterpEnumField(default_value=0)
    crmi = colorRamp_Interp


class ColorRampField(
    CompoundField[ColorRampAttrOperator, ColorRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorRampAttrOperator
    PLUG_CLS = ColorRampPlugOperator


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "tr"),
        ("transparencyG", "tg"),
        ("transparencyB", "tb"),
    )

    transparencyR = FloatField(default_value=0.5)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.5)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.5)
    tb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.5)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.5)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.5)
    tb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.5)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.5)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.5)
    tb = transparencyB


class IncandescencePlugOperator(
    Float3CompoundBasePlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescenceR", "ir"),
        ("incandescenceG", "ig"),
        ("incandescenceB", "ib"),
    )

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[
        IncandescenceAttrOperator, IncandescencePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


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


class OutMatteOpacityPlugOperator(
    Float3CompoundBasePlugOperator["OutMatteOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outMatteOpacityR", "omor"),
        ("outMatteOpacityG", "omog"),
        ("outMatteOpacityB", "omob"),
    )

    outMatteOpacityR = FloatField(default_value=1.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=1.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=1.0, writable=False)
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField(default_value=1.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=1.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=1.0, writable=False)
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[
        OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField(default_value=1.0, writable=False)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=1.0, writable=False)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=1.0, writable=False)
    omob = outMatteOpacityB
