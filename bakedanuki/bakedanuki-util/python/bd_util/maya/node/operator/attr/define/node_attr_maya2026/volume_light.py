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
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class ColorRange_colorRange_InterpEnumPlugOperator(
    EnumPlugOperator["ColorRange_colorRange_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ColorRange_colorRange_InterpEnumAttrOperator(
    EnumAttrOperator[ColorRange_colorRange_InterpEnumPlugOperator]
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


class ColorRange_colorRange_InterpEnumField(
    EnumField[
        ColorRange_colorRange_InterpEnumAttrOperator,
        ColorRange_colorRange_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorRange_colorRange_InterpEnumAttrOperator
    PLUG_CLS = ColorRange_colorRange_InterpEnumPlugOperator


class Penumbra_penumbra_InterpEnumPlugOperator(
    EnumPlugOperator["Penumbra_penumbra_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Penumbra_penumbra_InterpEnumAttrOperator(
    EnumAttrOperator[Penumbra_penumbra_InterpEnumPlugOperator]
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


class Penumbra_penumbra_InterpEnumField(
    EnumField[
        Penumbra_penumbra_InterpEnumAttrOperator,
        Penumbra_penumbra_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Penumbra_penumbra_InterpEnumAttrOperator
    PLUG_CLS = Penumbra_penumbra_InterpEnumPlugOperator


class LightData_lightDirectionPlugOperator(
    Float3CompoundBasePlugOperator["LightData_lightDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionX", "ldx"),
        ("lightDirectionY", "ldy"),
        ("lightDirectionZ", "ldz"),
    )

    lightDirectionX = FloatField(default_value=0.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=0.0, writable=False)
    ldz = lightDirectionZ


class LightData_lightDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[LightData_lightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = FloatField(default_value=0.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=0.0, writable=False)
    ldz = lightDirectionZ


class LightData_lightDirectionField(
    Float3CompoundBaseField[
        LightData_lightDirectionAttrOperator,
        LightData_lightDirectionPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = LightData_lightDirectionAttrOperator
    PLUG_CLS = LightData_lightDirectionPlugOperator

    lightDirectionX = FloatField(default_value=0.0, writable=False)
    ldx = lightDirectionX

    lightDirectionY = FloatField(default_value=0.0, writable=False)
    ldy = lightDirectionY

    lightDirectionZ = FloatField(default_value=0.0, writable=False)
    ldz = lightDirectionZ


class LightData_lightIntensityPlugOperator(
    Float3CompoundBasePlugOperator["LightData_lightIntensityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightIntensityR", "lir"),
        ("lightIntensityG", "lig"),
        ("lightIntensityB", "lib"),
    )

    lightIntensityR = FloatField(default_value=0.0, writable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=0.0, writable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(default_value=0.0, writable=False)
    lib = lightIntensityB


class LightData_lightIntensityAttrOperator(
    Float3CompoundBaseAttrOperator[LightData_lightIntensityPlugOperator]
):
    __slots__ = ()

    lightIntensityR = FloatField(default_value=0.0, writable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=0.0, writable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(default_value=0.0, writable=False)
    lib = lightIntensityB


class LightData_lightIntensityField(
    Float3CompoundBaseField[
        LightData_lightIntensityAttrOperator,
        LightData_lightIntensityPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = LightData_lightIntensityAttrOperator
    PLUG_CLS = LightData_lightIntensityPlugOperator

    lightIntensityR = FloatField(default_value=0.0, writable=False)
    lir = lightIntensityR

    lightIntensityG = FloatField(default_value=0.0, writable=False)
    lig = lightIntensityG

    lightIntensityB = FloatField(default_value=0.0, writable=False)
    lib = lightIntensityB


class ColorRange_colorRange_ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorRange_colorRange_ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRange_ColorR", "crgcr"),
        ("colorRange_ColorG", "crgcg"),
        ("colorRange_ColorB", "crgcb"),
    )

    colorRange_ColorR = FloatField(default_value=0.0)
    crgcr = colorRange_ColorR

    colorRange_ColorG = FloatField(default_value=0.0)
    crgcg = colorRange_ColorG

    colorRange_ColorB = FloatField(default_value=0.0)
    crgcb = colorRange_ColorB


class ColorRange_colorRange_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorRange_colorRange_ColorPlugOperator]
):
    __slots__ = ()

    colorRange_ColorR = FloatField(default_value=0.0)
    crgcr = colorRange_ColorR

    colorRange_ColorG = FloatField(default_value=0.0)
    crgcg = colorRange_ColorG

    colorRange_ColorB = FloatField(default_value=0.0)
    crgcb = colorRange_ColorB


class ColorRange_colorRange_ColorField(
    Float3CompoundBaseField[
        ColorRange_colorRange_ColorAttrOperator,
        ColorRange_colorRange_ColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorRange_colorRange_ColorAttrOperator
    PLUG_CLS = ColorRange_colorRange_ColorPlugOperator

    colorRange_ColorR = FloatField(default_value=0.0)
    crgcr = colorRange_ColorR

    colorRange_ColorG = FloatField(default_value=0.0)
    crgcg = colorRange_ColorG

    colorRange_ColorB = FloatField(default_value=0.0)
    crgcb = colorRange_ColorB


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0)
    cb = colorB


class ShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["ShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadColorR", "scr"),
        ("shadColorG", "scg"),
        ("shadColorB", "scb"),
    )

    shadColorR = FloatField(default_value=0.0)
    scr = shadColorR

    shadColorG = FloatField(default_value=0.0)
    scg = shadColorG

    shadColorB = FloatField(default_value=0.0)
    scb = shadColorB


class ShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowColorPlugOperator]
):
    __slots__ = ()

    shadColorR = FloatField(default_value=0.0)
    scr = shadColorR

    shadColorG = FloatField(default_value=0.0)
    scg = shadColorG

    shadColorB = FloatField(default_value=0.0)
    scb = shadColorB


class ShadowColorField(
    Float3CompoundBaseField[ShadowColorAttrOperator, ShadowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowColorAttrOperator
    PLUG_CLS = ShadowColorPlugOperator

    shadColorR = FloatField(default_value=0.0)
    scr = shadColorR

    shadColorG = FloatField(default_value=0.0)
    scg = shadColorG

    shadColorB = FloatField(default_value=0.0)
    scb = shadColorB


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


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "uu"),
        ("vCoord", "vv"),
    )

    uCoord = FloatField(default_value=0.0, writable=False)
    uu = uCoord

    vCoord = FloatField(default_value=0.0, writable=False)
    vv = vCoord


class UvCoordAttrOperator(Float2CompoundBaseAttrOperator[UvCoordPlugOperator]):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0, writable=False)
    uu = uCoord

    vCoord = FloatField(default_value=0.0, writable=False)
    vv = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0, writable=False)
    uu = uCoord

    vCoord = FloatField(default_value=0.0, writable=False)
    vv = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class LightDataValuePlugOperator(
    LightDataPlugOperator["LightDataValueAttrOperator"]
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
        ("lightBlindData", "lbl"),
    )

    lightDirection = LightData_lightDirectionField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ld = lightDirection

    lightIntensity = LightData_lightIntensityField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
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
    lbl = lightBlindData


class LightDataValueAttrOperator(
    LightDataAttrOperator[LightDataValuePlugOperator]
):
    __slots__ = ()

    lightDirection = LightData_lightDirectionField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ld = lightDirection

    lightIntensity = LightData_lightIntensityField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
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
    lbl = lightBlindData


class LightDataValueField(
    LightDataField[LightDataValueAttrOperator, LightDataValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataValueAttrOperator
    PLUG_CLS = LightDataValuePlugOperator

    lightDirection = LightData_lightDirectionField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ld = lightDirection

    lightIntensity = LightData_lightIntensityField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
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
    lbl = lightBlindData


class OpticalFXvisibilityPlugOperator(
    Float3CompoundBasePlugOperator["OpticalFXvisibilityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opticalFXvisibilityR", "ovr"),
        ("opticalFXvisibilityG", "ovg"),
        ("opticalFXvisibilityB", "ovb"),
    )

    opticalFXvisibilityR = FloatField(default_value=1.0, writable=False)
    ovr = opticalFXvisibilityR

    opticalFXvisibilityG = FloatField(default_value=1.0, writable=False)
    ovg = opticalFXvisibilityG

    opticalFXvisibilityB = FloatField(default_value=1.0, writable=False)
    ovb = opticalFXvisibilityB


class OpticalFXvisibilityAttrOperator(
    Float3CompoundBaseAttrOperator[OpticalFXvisibilityPlugOperator]
):
    __slots__ = ()

    opticalFXvisibilityR = FloatField(default_value=1.0, writable=False)
    ovr = opticalFXvisibilityR

    opticalFXvisibilityG = FloatField(default_value=1.0, writable=False)
    ovg = opticalFXvisibilityG

    opticalFXvisibilityB = FloatField(default_value=1.0, writable=False)
    ovb = opticalFXvisibilityB


class OpticalFXvisibilityField(
    Float3CompoundBaseField[
        OpticalFXvisibilityAttrOperator, OpticalFXvisibilityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OpticalFXvisibilityAttrOperator
    PLUG_CLS = OpticalFXvisibilityPlugOperator

    opticalFXvisibilityR = FloatField(default_value=1.0, writable=False)
    ovr = opticalFXvisibilityR

    opticalFXvisibilityG = FloatField(default_value=1.0, writable=False)
    ovg = opticalFXvisibilityG

    opticalFXvisibilityB = FloatField(default_value=1.0, writable=False)
    ovb = opticalFXvisibilityB


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "tx"),
        ("pointWorldY", "ty"),
        ("pointWorldZ", "tz"),
    )

    pointWorldX = FloatField(default_value=1.0, readable=False)
    tx = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    ty = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    tz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=1.0, readable=False)
    tx = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    ty = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    tz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=1.0, readable=False)
    tx = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    ty = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    tz = pointWorldZ


class FarPointWorldPlugOperator(
    Float3CompoundBasePlugOperator["FarPointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farPointWorldX", "fwx"),
        ("farPointWorldY", "fwy"),
        ("farPointWorldZ", "fwz"),
    )

    farPointWorldX = FloatField(default_value=1.0, readable=False)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0, readable=False)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0, readable=False)
    fwz = farPointWorldZ


class FarPointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[FarPointWorldPlugOperator]
):
    __slots__ = ()

    farPointWorldX = FloatField(default_value=1.0, readable=False)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0, readable=False)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0, readable=False)
    fwz = farPointWorldZ


class FarPointWorldField(
    Float3CompoundBaseField[
        FarPointWorldAttrOperator, FarPointWorldPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FarPointWorldAttrOperator
    PLUG_CLS = FarPointWorldPlugOperator

    farPointWorldX = FloatField(default_value=1.0, readable=False)
    fwx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0, readable=False)
    fwy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0, readable=False)
    fwz = farPointWorldZ


class ColorRangePlugOperator(CompoundPlugOperator["ColorRangeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRange_Position", "crgp"),
        ("colorRange_Color", "crgc"),
        ("colorRange_Interp", "crgi"),
    )

    colorRange_Position = FloatField(default_value=0.0)
    crgp = colorRange_Position

    colorRange_Color = ColorRange_colorRange_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    crgc = colorRange_Color

    colorRange_Interp = ColorRange_colorRange_InterpEnumField(default_value=0)
    crgi = colorRange_Interp


class ColorRangeAttrOperator(CompoundAttrOperator[ColorRangePlugOperator]):
    __slots__ = ()

    colorRange_Position = FloatField(default_value=0.0)
    crgp = colorRange_Position

    colorRange_Color = ColorRange_colorRange_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    crgc = colorRange_Color

    colorRange_Interp = ColorRange_colorRange_InterpEnumField(default_value=0)
    crgi = colorRange_Interp


class ColorRangeField(
    CompoundField[ColorRangeAttrOperator, ColorRangePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorRangeAttrOperator
    PLUG_CLS = ColorRangePlugOperator


class PenumbraPlugOperator(CompoundPlugOperator["PenumbraAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("penumbra_Position", "penp"),
        ("penumbra_FloatValue", "penfv"),
        ("penumbra_Interp", "peni"),
    )

    penumbra_Position = FloatField(default_value=0.0)
    penp = penumbra_Position

    penumbra_FloatValue = FloatField(default_value=0.0)
    penfv = penumbra_FloatValue

    penumbra_Interp = Penumbra_penumbra_InterpEnumField(default_value=0)
    peni = penumbra_Interp


class PenumbraAttrOperator(CompoundAttrOperator[PenumbraPlugOperator]):
    __slots__ = ()

    penumbra_Position = FloatField(default_value=0.0)
    penp = penumbra_Position

    penumbra_FloatValue = FloatField(default_value=0.0)
    penfv = penumbra_FloatValue

    penumbra_Interp = Penumbra_penumbra_InterpEnumField(default_value=0)
    peni = penumbra_Interp


class PenumbraField(CompoundField[PenumbraAttrOperator, PenumbraPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PenumbraAttrOperator
    PLUG_CLS = PenumbraPlugOperator
