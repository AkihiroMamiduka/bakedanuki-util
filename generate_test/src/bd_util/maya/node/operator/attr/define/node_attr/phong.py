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


class VrEdgeColorPlugOperator(
    Float3CompoundBasePlugOperator["VrEdgeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vrEdgeColorR", "vecr"),
        ("vrEdgeColorG", "vecg"),
        ("vrEdgeColorB", "vecb"),
    )

    vrEdgeColorR = FloatField()
    vecr = vrEdgeColorR

    vrEdgeColorG = FloatField()
    vecg = vrEdgeColorG

    vrEdgeColorB = FloatField()
    vecb = vrEdgeColorB


class VrEdgeColorAttrOperator(
    Float3CompoundBaseAttrOperator[VrEdgeColorPlugOperator]
):
    __slots__ = ()

    vrEdgeColorR = FloatField()
    vecr = vrEdgeColorR

    vrEdgeColorG = FloatField()
    vecg = vrEdgeColorG

    vrEdgeColorB = FloatField()
    vecb = vrEdgeColorB


class VrEdgeColorField(
    Float3CompoundBaseField[VrEdgeColorAttrOperator, VrEdgeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VrEdgeColorAttrOperator
    PLUG_CLS = VrEdgeColorPlugOperator

    vrEdgeColorR = FloatField()
    vecr = vrEdgeColorR

    vrEdgeColorG = FloatField()
    vecg = vrEdgeColorG

    vrEdgeColorB = FloatField()
    vecb = vrEdgeColorB


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


class HardwareShaderPlugOperator(
    Float3CompoundBasePlugOperator["HardwareShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareShaderR", "hwr"),
        ("hardwareShaderG", "hwg"),
        ("hardwareShaderB", "hwb"),
    )

    hardwareShaderR = FloatField()
    hwr = hardwareShaderR

    hardwareShaderG = FloatField()
    hwg = hardwareShaderG

    hardwareShaderB = FloatField()
    hwb = hardwareShaderB


class HardwareShaderAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareShaderPlugOperator]
):
    __slots__ = ()

    hardwareShaderR = FloatField()
    hwr = hardwareShaderR

    hardwareShaderG = FloatField()
    hwg = hardwareShaderG

    hardwareShaderB = FloatField()
    hwb = hardwareShaderB


class HardwareShaderField(
    Float3CompoundBaseField[HardwareShaderAttrOperator, HardwareShaderPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HardwareShaderAttrOperator
    PLUG_CLS = HardwareShaderPlugOperator

    hardwareShaderR = FloatField()
    hwr = hardwareShaderR

    hardwareShaderG = FloatField()
    hwg = hardwareShaderG

    hardwareShaderB = FloatField()
    hwb = hardwareShaderB


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
