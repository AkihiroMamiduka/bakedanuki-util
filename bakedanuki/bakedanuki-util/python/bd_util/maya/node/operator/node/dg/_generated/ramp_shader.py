# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ramp_shader import (
    AmbientColorField,
    ColorField,
    EnvironmentField,
    IncandescenceField,
    LightDataArrayField,
    NormalCameraField,
    OutColorField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    PointCameraField,
    RayDirectionField,
    ReflectedColorField,
    ReflectivityField,
    ShadowColorField,
    SpecularColorField,
    SpecularRollOffField,
    TransparencyField,
    TriangleNormalCameraField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField


class ColorInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LIGHT_ANGLE = 0
    FACING_ANGLE = 1
    BRIGHTNESS = 2
    NORMALIZED_BRIGHTNESS = 3


class ColorInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LIGHT_ANGLE = 0
    FACING_ANGLE = 1
    BRIGHTNESS = 2
    NORMALIZED_BRIGHTNESS = 3

    NAME_MAP = {
        LIGHT_ANGLE: "Light Angle",
        FACING_ANGLE: "Facing Angle",
        BRIGHTNESS: "Brightness",
        NORMALIZED_BRIGHTNESS: "Normalized Brightness",
    }


class ColorInputEnumField(
    EnumField[ColorInputEnumAttrOperator, ColorInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorInputEnumAttrOperator
    PLUG_CLS = ColorInputEnumPlugOperator


class ShadowModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    SHADED_COLOR = 1
    CONSTANT_COLOR = 2


class ShadowModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    SHADED_COLOR = 1
    CONSTANT_COLOR = 2

    NAME_MAP = {
        NORMAL: "Normal",
        SHADED_COLOR: "Shaded Color",
        CONSTANT_COLOR: "Constant Color",
    }


class ShadowModeEnumField(
    EnumField[ShadowModeEnumAttrOperator, ShadowModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowModeEnumAttrOperator
    PLUG_CLS = ShadowModeEnumPlugOperator


class MatteOpacityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2


class MatteOpacityModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2

    NAME_MAP = {
        BLACK_HOLE: "Black Hole",
        SOLID_MATTE: "Solid Matte",
        OPACITY_GAIN: "Opacity Gain",
    }


class MatteOpacityModeEnumField(
    EnumField[MatteOpacityModeEnumAttrOperator, MatteOpacityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MatteOpacityModeEnumAttrOperator
    PLUG_CLS = MatteOpacityModeEnumPlugOperator


class GeneratedRampShader(DG):
    __slots__ = ()

    NODE_TYPE = "rampShader"

    objectId = AddrField(default_value=0.0, readable=False)
    oi = objectId

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    raySampler = AddrField(default_value=0.0, readable=False)
    rtr = raySampler

    rayDepth = ShortField(default_value=0, readable=False)
    rd = rayDepth

    rayInstance = LongField(default_value=0, readable=False)
    ryi = rayInstance

    refractionLimit = ShortField(default_value=6, min_value=0, soft_max_value=10)
    rdl = refractionLimit

    refractiveIndex = FloatField(default_value=1.0, min_value=0.01, soft_max_value=3.0)
    rfi = refractiveIndex

    mediumRefractiveIndex = FloatField(default_value=1.0, readable=False)
    mrfi = mediumRefractiveIndex

    refractions = BoolField(default_value=False)
    rfc = refractions

    diffuse = FloatField(default_value=0.800000011920929, soft_min_value=0.0, soft_max_value=1.0)
    dc = diffuse

    forwardScatter = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fsc = forwardScatter

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0), readable=False)
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    color = ColorField(multi=True)
    clr = color

    color_ColorR = FloatField()
    clrcr = color_ColorR

    color_ColorG = FloatField()
    clrcg = color_ColorG

    color_ColorB = FloatField()
    clrcb = color_ColorB

    colorInput = ColorInputEnumField(default_value=0)
    cin = colorInput

    shadowMode = ShadowModeEnumField(default_value=0)
    smd = shadowMode

    shadowColor = ShadowColorField(default_value=(0.0, 0.0, 0.0))
    shc = shadowColor
    shadowColorR = shadowColor.shadowColorR
    shr = shadowColorR
    shadowColorG = shadowColor.shadowColorG
    shg = shadowColorG
    shadowColorB = shadowColor.shadowColorB
    shb = shadowColorB

    shadowThreshold = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    sht = shadowThreshold

    transparency = TransparencyField(multi=True)
    it = transparency

    transparency_ColorR = FloatField()
    itcr = transparency_ColorR

    transparency_ColorG = FloatField()
    itcg = transparency_ColorG

    transparency_ColorB = FloatField()
    itcb = transparency_ColorB

    ambientColor = AmbientColorField(default_value=(0.0, 0.0, 0.0))
    ambc = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField(multi=True)
    ic = incandescence

    incandescence_ColorR = FloatField()
    iccr = incandescence_ColorR

    incandescence_ColorG = FloatField()
    iccg = incandescence_ColorG

    incandescence_ColorB = FloatField()
    iccb = incandescence_ColorB

    translucence = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tc = translucence

    translucenceFocus = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tcf = translucenceFocus

    translucenceDepth = FloatField(default_value=0.05000000074505806, soft_min_value=0.0, soft_max_value=5.0)
    trsd = translucenceDepth

    opacityDepth = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    opad = opacityDepth

    glowIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gi = glowIntensity

    specularGlow = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    spg = specularGlow

    hideSource = BoolField(default_value=False)
    hs = hideSource

    surfaceThickness = FloatField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    thik = surfaceThickness

    shadowAttenuation = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    fakc = shadowAttenuation

    transparencyDepth = FloatField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    trdp = transparencyDepth

    lightAbsorbance = FloatField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    absb = lightAbsorbance

    chromaticAberration = BoolField(default_value=False)
    crab = chromaticAberration

    eccentricity = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=1.0)
    ec = eccentricity

    specularity = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=1.0)
    spl = specularity

    specularRollOff = SpecularRollOffField(multi=True, default_value=(0.0, 0.0, 0.0))
    sro = specularRollOff

    reflectionLimit = ShortField(default_value=1, min_value=0, soft_max_value=10)
    fll = reflectionLimit

    specularColor = SpecularColorField(multi=True)
    sc = specularColor

    specularColor_ColorR = FloatField()
    sccr = specularColor_ColorR

    specularColor_ColorG = FloatField()
    sccg = specularColor_ColorG

    specularColor_ColorB = FloatField()
    sccb = specularColor_ColorB

    reflectivity = ReflectivityField(multi=True, default_value=(0.0, 0.0, 0.0))
    rfl = reflectivity

    environment = EnvironmentField(multi=True)
    env = environment

    environment_ColorR = FloatField()
    envcr = environment_ColorR

    environment_ColorG = FloatField()
    envcg = environment_ColorG

    environment_ColorB = FloatField()
    envcb = environment_ColorB

    reflectedColor = ReflectedColorField(default_value=(0.0, 0.0, 0.0))
    rc = reflectedColor
    reflectedColorR = reflectedColor.reflectedColorR
    rr = reflectedColorR
    reflectedColorG = reflectedColor.reflectedColorG
    rg = reflectedColorG
    reflectedColorB = reflectedColor.reflectedColorB
    rb = reflectedColorB

    triangleNormalCamera = TriangleNormalCameraField(default_value=(0.0, 1.0, 0.0))
    tnc = triangleNormalCamera
    triangleNormalCameraX = triangleNormalCamera.triangleNormalCameraX
    tnx = triangleNormalCameraX
    triangleNormalCameraY = triangleNormalCamera.triangleNormalCameraY
    tny = triangleNormalCameraY
    triangleNormalCameraZ = triangleNormalCamera.triangleNormalCameraZ
    tnz = triangleNormalCameraZ

    reflectionSpecularity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    rsp = reflectionSpecularity

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    pointCamera = PointCameraField(default_value=(1.0, 1.0, 1.0))
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    lightDataArray = LightDataArrayField(multi=True, readable=False)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    matteOpacityMode = MatteOpacityModeEnumField(default_value=2)
    mom = matteOpacityMode

    matteOpacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField(default_value=(0.0, 0.0, 0.0), writable=False)
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB
