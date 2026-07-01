# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rdx"),
        ("rayDirectionY", "rdy"),
        ("rayDirectionZ", "rdz"),
    )

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField()
    rdx = rayDirectionX

    rayDirectionY = FloatField()
    rdy = rayDirectionY

    rayDirectionZ = FloatField()
    rdz = rayDirectionZ


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


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "itr"),
        ("transparencyG", "itg"),
        ("transparencyB", "itb"),
    )

    transparencyR = FloatField()
    itr = transparencyR

    transparencyG = FloatField()
    itg = transparencyG

    transparencyB = FloatField()
    itb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField()
    itr = transparencyR

    transparencyG = FloatField()
    itg = transparencyG

    transparencyB = FloatField()
    itb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField()
    itr = transparencyR

    transparencyG = FloatField()
    itg = transparencyG

    transparencyB = FloatField()
    itb = transparencyB


class AmbientColorPlugOperator(
    Float3CompoundBasePlugOperator["AmbientColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ambientColorR", "acr"),
        ("ambientColorG", "acg"),
        ("ambientColorB", "acb"),
    )

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class IncandescencePlugOperator(
    Float3CompoundBasePlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescenceR", "ir"),
        ("incandescenceG", "ig"),
        ("incandescenceB", "ib"),
    )

    incandescenceR = FloatField()
    ir = incandescenceR

    incandescenceG = FloatField()
    ig = incandescenceG

    incandescenceB = FloatField()
    ib = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField()
    ir = incandescenceR

    incandescenceG = FloatField()
    ig = incandescenceG

    incandescenceB = FloatField()
    ib = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField()
    ir = incandescenceR

    incandescenceG = FloatField()
    ig = incandescenceG

    incandescenceB = FloatField()
    ib = incandescenceB


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "sr"),
        ("specularColorG", "sg"),
        ("specularColorB", "sb"),
    )

    specularColorR = FloatField()
    sr = specularColorR

    specularColorG = FloatField()
    sg = specularColorG

    specularColorB = FloatField()
    sb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField()
    sr = specularColorR

    specularColorG = FloatField()
    sg = specularColorG

    specularColorB = FloatField()
    sb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField()
    sr = specularColorR

    specularColorG = FloatField()
    sg = specularColorG

    specularColorB = FloatField()
    sb = specularColorB


class EnvironmentPlugOperator(
    CompoundPlugOperator["EnvironmentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("environment_Position", "envp"),
        ("environment_Color", "envc"),
        ("environment_Interp", "envi"),
    )

    environment_Position = FloatField()
    envp = environment_Position

    environment_Color = Float3Field()
    envc = environment_Color

    environment_Interp = EnumField()
    envi = environment_Interp


class EnvironmentAttrOperator(
    CompoundAttrOperator[EnvironmentPlugOperator]
):
    __slots__ = ()

    environment_Position = FloatField()
    envp = environment_Position

    environment_Color = Float3Field()
    envc = environment_Color

    environment_Interp = EnumField()
    envi = environment_Interp


class EnvironmentField(
    CompoundField[EnvironmentAttrOperator, EnvironmentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvironmentAttrOperator
    PLUG_CLS = EnvironmentPlugOperator


class ReflectedColorPlugOperator(
    Float3CompoundBasePlugOperator["ReflectedColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectedColorR", "rr"),
        ("reflectedColorG", "rg"),
        ("reflectedColorB", "rb"),
    )

    reflectedColorR = FloatField()
    rr = reflectedColorR

    reflectedColorG = FloatField()
    rg = reflectedColorG

    reflectedColorB = FloatField()
    rb = reflectedColorB


class ReflectedColorAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectedColorPlugOperator]
):
    __slots__ = ()

    reflectedColorR = FloatField()
    rr = reflectedColorR

    reflectedColorG = FloatField()
    rg = reflectedColorG

    reflectedColorB = FloatField()
    rb = reflectedColorB


class ReflectedColorField(
    Float3CompoundBaseField[ReflectedColorAttrOperator, ReflectedColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectedColorAttrOperator
    PLUG_CLS = ReflectedColorPlugOperator

    reflectedColorR = FloatField()
    rr = reflectedColorR

    reflectedColorG = FloatField()
    rg = reflectedColorG

    reflectedColorB = FloatField()
    rb = reflectedColorB


class TriangleNormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["TriangleNormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("triangleNormalCameraX", "tnx"),
        ("triangleNormalCameraY", "tny"),
        ("triangleNormalCameraZ", "tnz"),
    )

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class TriangleNormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


class TriangleNormalCameraField(
    Float3CompoundBaseField[TriangleNormalCameraAttrOperator, TriangleNormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TriangleNormalCameraAttrOperator
    PLUG_CLS = TriangleNormalCameraPlugOperator

    triangleNormalCameraX = FloatField()
    tnx = triangleNormalCameraX

    triangleNormalCameraY = FloatField()
    tny = triangleNormalCameraY

    triangleNormalCameraZ = FloatField()
    tnz = triangleNormalCameraZ


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


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


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


class WindUVPlugOperator(
    Float2CompoundBasePlugOperator["WindUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("windU", "wiu"),
        ("windV", "wiv"),
    )

    windU = FloatField()
    wiu = windU

    windV = FloatField()
    wiv = windV


class WindUVAttrOperator(
    Float2CompoundBaseAttrOperator[WindUVPlugOperator]
):
    __slots__ = ()

    windU = FloatField()
    wiu = windU

    windV = FloatField()
    wiv = windV


class WindUVField(
    Float2CompoundBaseField[WindUVAttrOperator, WindUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WindUVAttrOperator
    PLUG_CLS = WindUVPlugOperator

    windU = FloatField()
    wiu = windU

    windV = FloatField()
    wiv = windV


class WaveHeightPlugOperator(
    CompoundPlugOperator["WaveHeightAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveHeight_Position", "whp"),
        ("waveHeight_FloatValue", "whfv"),
        ("waveHeight_Interp", "whi"),
    )

    waveHeight_Position = FloatField()
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField()
    whfv = waveHeight_FloatValue

    waveHeight_Interp = EnumField()
    whi = waveHeight_Interp


class WaveHeightAttrOperator(
    CompoundAttrOperator[WaveHeightPlugOperator]
):
    __slots__ = ()

    waveHeight_Position = FloatField()
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField()
    whfv = waveHeight_FloatValue

    waveHeight_Interp = EnumField()
    whi = waveHeight_Interp


class WaveHeightField(
    CompoundField[WaveHeightAttrOperator, WaveHeightPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveHeightAttrOperator
    PLUG_CLS = WaveHeightPlugOperator


class WaveTurbulencePlugOperator(
    CompoundPlugOperator["WaveTurbulenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveTurbulence_Position", "wtbp"),
        ("waveTurbulence_FloatValue", "wtbfv"),
        ("waveTurbulence_Interp", "wtbi"),
    )

    waveTurbulence_Position = FloatField()
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField()
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = EnumField()
    wtbi = waveTurbulence_Interp


class WaveTurbulenceAttrOperator(
    CompoundAttrOperator[WaveTurbulencePlugOperator]
):
    __slots__ = ()

    waveTurbulence_Position = FloatField()
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField()
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = EnumField()
    wtbi = waveTurbulence_Interp


class WaveTurbulenceField(
    CompoundField[WaveTurbulenceAttrOperator, WaveTurbulencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulenceAttrOperator
    PLUG_CLS = WaveTurbulencePlugOperator


class WavePeakingPlugOperator(
    CompoundPlugOperator["WavePeakingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("wavePeaking_Position", "wpp"),
        ("wavePeaking_FloatValue", "wpfv"),
        ("wavePeaking_Interp", "wpi"),
    )

    wavePeaking_Position = FloatField()
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField()
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = EnumField()
    wpi = wavePeaking_Interp


class WavePeakingAttrOperator(
    CompoundAttrOperator[WavePeakingPlugOperator]
):
    __slots__ = ()

    wavePeaking_Position = FloatField()
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField()
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = EnumField()
    wpi = wavePeaking_Interp


class WavePeakingField(
    CompoundField[WavePeakingAttrOperator, WavePeakingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WavePeakingAttrOperator
    PLUG_CLS = WavePeakingPlugOperator


class FoamColorPlugOperator(
    Float3CompoundBasePlugOperator["FoamColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("foamColorR", "fcr"),
        ("foamColorG", "fcg"),
        ("foamColorB", "fcb"),
    )

    foamColorR = FloatField()
    fcr = foamColorR

    foamColorG = FloatField()
    fcg = foamColorG

    foamColorB = FloatField()
    fcb = foamColorB


class FoamColorAttrOperator(
    Float3CompoundBaseAttrOperator[FoamColorPlugOperator]
):
    __slots__ = ()

    foamColorR = FloatField()
    fcr = foamColorR

    foamColorG = FloatField()
    fcg = foamColorG

    foamColorB = FloatField()
    fcb = foamColorB


class FoamColorField(
    Float3CompoundBaseField[FoamColorAttrOperator, FoamColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FoamColorAttrOperator
    PLUG_CLS = FoamColorPlugOperator

    foamColorR = FloatField()
    fcr = foamColorR

    foamColorG = FloatField()
    fcg = foamColorG

    foamColorB = FloatField()
    fcb = foamColorB


class RefPointCameraPlugOperator(
    Float3CompoundBasePlugOperator["RefPointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("refPointCameraX", "rcx"),
        ("refPointCameraY", "rcy"),
        ("refPointCameraZ", "rcz"),
    )

    refPointCameraX = FloatField()
    rcx = refPointCameraX

    refPointCameraY = FloatField()
    rcy = refPointCameraY

    refPointCameraZ = FloatField()
    rcz = refPointCameraZ


class RefPointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointCameraPlugOperator]
):
    __slots__ = ()

    refPointCameraX = FloatField()
    rcx = refPointCameraX

    refPointCameraY = FloatField()
    rcy = refPointCameraY

    refPointCameraZ = FloatField()
    rcz = refPointCameraZ


class RefPointCameraField(
    Float3CompoundBaseField[RefPointCameraAttrOperator, RefPointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointCameraAttrOperator
    PLUG_CLS = RefPointCameraPlugOperator

    refPointCameraX = FloatField()
    rcx = refPointCameraX

    refPointCameraY = FloatField()
    rcy = refPointCameraY

    refPointCameraZ = FloatField()
    rcz = refPointCameraZ
