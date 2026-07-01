# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ramp_shader import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


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


class RampShader(DG):
    __slots__ = ()

    NODE_TYPE = "rampShader"

    objectId = AddrField()
    oi = objectId

    primitiveId = LongField()
    pi = primitiveId

    raySampler = AddrField()
    rtr = raySampler

    rayDepth = ShortField()
    rd = rayDepth

    rayInstance = LongField()
    ryi = rayInstance

    refractionLimit = ShortField()
    rdl = refractionLimit

    refractiveIndex = FloatField()
    rfi = refractiveIndex

    mediumRefractiveIndex = FloatField()
    mrfi = mediumRefractiveIndex

    refractions = BoolField()
    rfc = refractions

    diffuse = FloatField()
    dc = diffuse

    forwardScatter = FloatField()
    fsc = forwardScatter

    rayDirection = RayDirectionField()
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

    colorInput = ColorInputEnumField()
    cin = colorInput

    shadowMode = ShadowModeEnumField()
    smd = shadowMode

    shadowColor = ShadowColorField()
    shc = shadowColor
    shadowColorR = shadowColor.shadowColorR
    shr = shadowColorR
    shadowColorG = shadowColor.shadowColorG
    shg = shadowColorG
    shadowColorB = shadowColor.shadowColorB
    shb = shadowColorB

    shadowThreshold = FloatField()
    sht = shadowThreshold

    transparency = TransparencyField(multi=True)
    it = transparency

    transparency_ColorR = FloatField()
    itcr = transparency_ColorR

    transparency_ColorG = FloatField()
    itcg = transparency_ColorG

    transparency_ColorB = FloatField()
    itcb = transparency_ColorB

    ambientColor = AmbientColorField()
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

    translucence = FloatField()
    tc = translucence

    translucenceFocus = FloatField()
    tcf = translucenceFocus

    translucenceDepth = FloatField()
    trsd = translucenceDepth

    opacityDepth = FloatField()
    opad = opacityDepth

    glowIntensity = FloatField()
    gi = glowIntensity

    specularGlow = FloatField()
    spg = specularGlow

    hideSource = BoolField()
    hs = hideSource

    surfaceThickness = FloatField()
    thik = surfaceThickness

    shadowAttenuation = FloatField()
    fakc = shadowAttenuation

    transparencyDepth = FloatField()
    trdp = transparencyDepth

    lightAbsorbance = FloatField()
    absb = lightAbsorbance

    chromaticAberration = BoolField()
    crab = chromaticAberration

    eccentricity = FloatField()
    ec = eccentricity

    specularity = FloatField()
    spl = specularity

    specularRollOff = SpecularRollOffField(multi=True)
    sro = specularRollOff

    reflectionLimit = ShortField()
    fll = reflectionLimit

    specularColor = SpecularColorField(multi=True)
    sc = specularColor

    specularColor_ColorR = FloatField()
    sccr = specularColor_ColorR

    specularColor_ColorG = FloatField()
    sccg = specularColor_ColorG

    specularColor_ColorB = FloatField()
    sccb = specularColor_ColorB

    reflectivity = ReflectivityField(multi=True)
    rfl = reflectivity

    environment = EnvironmentField(multi=True)
    env = environment

    environment_ColorR = FloatField()
    envcr = environment_ColorR

    environment_ColorG = FloatField()
    envcg = environment_ColorG

    environment_ColorB = FloatField()
    envcb = environment_ColorB

    reflectedColor = ReflectedColorField()
    rc = reflectedColor
    reflectedColorR = reflectedColor.reflectedColorR
    rr = reflectedColorR
    reflectedColorG = reflectedColor.reflectedColorG
    rg = reflectedColorG
    reflectedColorB = reflectedColor.reflectedColorB
    rb = reflectedColorB

    triangleNormalCamera = TriangleNormalCameraField()
    tnc = triangleNormalCamera
    triangleNormalCameraX = triangleNormalCamera.triangleNormalCameraX
    tnx = triangleNormalCameraX
    triangleNormalCameraY = triangleNormalCamera.triangleNormalCameraY
    tny = triangleNormalCameraY
    triangleNormalCameraZ = triangleNormalCamera.triangleNormalCameraZ
    tnz = triangleNormalCameraZ

    reflectionSpecularity = FloatField()
    rsp = reflectionSpecularity

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outGlowColor = OutGlowColorField()
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    pointCamera = PointCameraField()
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    lightDataArray = LightDataArrayField(multi=True)
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

    matteOpacityMode = MatteOpacityModeEnumField()
    mom = matteOpacityMode

    matteOpacity = FloatField()
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField()
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB
