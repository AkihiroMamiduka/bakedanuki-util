# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rdx"),
        ("rayDirectionY", "rdy"),
        ("rayDirectionZ", "rdz"),
    )

    rayDirectionX = FloatField(default_value=0.0, readable=False)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0, readable=False)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0, readable=False)
    rdz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField(default_value=0.0, readable=False)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0, readable=False)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0, readable=False)
    rdz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField(default_value=0.0, readable=False)
    rdx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0, readable=False)
    rdy = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0, readable=False)
    rdz = rayDirectionZ


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=0.5)
    cr = colorR

    colorG = FloatField(default_value=0.5)
    cg = colorG

    colorB = FloatField(default_value=0.5)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.5)
    cr = colorR

    colorG = FloatField(default_value=0.5)
    cg = colorG

    colorB = FloatField(default_value=0.5)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.5)
    cr = colorR

    colorG = FloatField(default_value=0.5)
    cg = colorG

    colorB = FloatField(default_value=0.5)
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

    transparencyR = FloatField(default_value=0.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    itb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    itb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0)
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

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
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


class VrEdgeColorPlugOperator(
    Float3CompoundBasePlugOperator["VrEdgeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vrEdgeColorR", "vecr"),
        ("vrEdgeColorG", "vecg"),
        ("vrEdgeColorB", "vecb"),
    )

    vrEdgeColorR = FloatField(default_value=0.5)
    vecr = vrEdgeColorR

    vrEdgeColorG = FloatField(default_value=0.5)
    vecg = vrEdgeColorG

    vrEdgeColorB = FloatField(default_value=0.5)
    vecb = vrEdgeColorB


class VrEdgeColorAttrOperator(
    Float3CompoundBaseAttrOperator[VrEdgeColorPlugOperator]
):
    __slots__ = ()

    vrEdgeColorR = FloatField(default_value=0.5)
    vecr = vrEdgeColorR

    vrEdgeColorG = FloatField(default_value=0.5)
    vecg = vrEdgeColorG

    vrEdgeColorB = FloatField(default_value=0.5)
    vecb = vrEdgeColorB


class VrEdgeColorField(
    Float3CompoundBaseField[VrEdgeColorAttrOperator, VrEdgeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VrEdgeColorAttrOperator
    PLUG_CLS = VrEdgeColorPlugOperator

    vrEdgeColorR = FloatField(default_value=0.5)
    vecr = vrEdgeColorR

    vrEdgeColorG = FloatField(default_value=0.5)
    vecg = vrEdgeColorG

    vrEdgeColorB = FloatField(default_value=0.5)
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


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField(default_value=1.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=1.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=1.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0)
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

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
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


class HardwareShaderPlugOperator(
    Float3CompoundBasePlugOperator["HardwareShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareShaderR", "hwr"),
        ("hardwareShaderG", "hwg"),
        ("hardwareShaderB", "hwb"),
    )

    hardwareShaderR = FloatField(default_value=0.0)
    hwr = hardwareShaderR

    hardwareShaderG = FloatField(default_value=0.0)
    hwg = hardwareShaderG

    hardwareShaderB = FloatField(default_value=0.0)
    hwb = hardwareShaderB


class HardwareShaderAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareShaderPlugOperator]
):
    __slots__ = ()

    hardwareShaderR = FloatField(default_value=0.0)
    hwr = hardwareShaderR

    hardwareShaderG = FloatField(default_value=0.0)
    hwg = hardwareShaderG

    hardwareShaderB = FloatField(default_value=0.0)
    hwb = hardwareShaderB


class HardwareShaderField(
    Float3CompoundBaseField[
        HardwareShaderAttrOperator, HardwareShaderPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HardwareShaderAttrOperator
    PLUG_CLS = HardwareShaderPlugOperator

    hardwareShaderR = FloatField(default_value=0.0)
    hwr = hardwareShaderR

    hardwareShaderG = FloatField(default_value=0.0)
    hwg = hardwareShaderG

    hardwareShaderB = FloatField(default_value=0.0)
    hwb = hardwareShaderB
