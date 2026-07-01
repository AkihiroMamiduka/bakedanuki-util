# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.anisotropic import (
    AmbientColorField,
    ColorField,
    HardwareShaderField,
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
    SpecularColorField,
    TangentUCameraField,
    TangentVCameraField,
    TransparencyField,
    TriangleNormalCameraField,
    VrEdgeColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class VrFillObjectEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT_FILL = 0
    SINGLE_COLOR = 1
    TWO_COLOR = 2
    FOUR_COLOR = 3
    FULL_COLOR = 4
    AVERAGE_COLOR = 5
    AREA_GRADIENT = 6
    MESH_GRADIENT = 7
    NO_FILL = 8


class VrFillObjectEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT_FILL = 0
    SINGLE_COLOR = 1
    TWO_COLOR = 2
    FOUR_COLOR = 3
    FULL_COLOR = 4
    AVERAGE_COLOR = 5
    AREA_GRADIENT = 6
    MESH_GRADIENT = 7
    NO_FILL = 8

    NAME_MAP = {
        DEFAULT_FILL: "Default Fill",
        SINGLE_COLOR: "Single Color",
        TWO_COLOR: "Two Color",
        FOUR_COLOR: "Four Color",
        FULL_COLOR: "Full Color",
        AVERAGE_COLOR: "Average Color",
        AREA_GRADIENT: "Area Gradient",
        MESH_GRADIENT: "Mesh Gradient",
        NO_FILL: "No Fill",
    }


class VrFillObjectEnumField(
    EnumField[VrFillObjectEnumAttrOperator, VrFillObjectEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VrFillObjectEnumAttrOperator
    PLUG_CLS = VrFillObjectEnumPlugOperator


class VrEdgeStyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    OUTLINES = 1
    ENTIRE_MESH = 2
    NO_EDGES = 3


class VrEdgeStyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    OUTLINES = 1
    ENTIRE_MESH = 2
    NO_EDGES = 3

    NAME_MAP = {
        DEFAULT: "Default",
        OUTLINES: "Outlines",
        ENTIRE_MESH: "Entire Mesh",
        NO_EDGES: "No Edges",
    }


class VrEdgeStyleEnumField(
    EnumField[VrEdgeStyleEnumAttrOperator, VrEdgeStyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VrEdgeStyleEnumAttrOperator
    PLUG_CLS = VrEdgeStyleEnumPlugOperator


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


class Anisotropic(DG):
    __slots__ = ()

    NODE_TYPE = "anisotropic"

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

    rayDirection = RayDirectionField()
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    color = ColorField()
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    transparency = TransparencyField()
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    ambientColor = AmbientColorField()
    ambc = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField()
    ic = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

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

    vrOverwriteDefaults = BoolField()
    vrod = vrOverwriteDefaults

    vrFillObject = VrFillObjectEnumField()
    vrfo = vrFillObject

    vrEdgeWeight = DoubleField()
    vrew = vrEdgeWeight

    vrEdgeColor = VrEdgeColorField()
    vrec = vrEdgeColor
    vrEdgeColorR = vrEdgeColor.vrEdgeColorR
    vecr = vrEdgeColorR
    vrEdgeColorG = vrEdgeColor.vrEdgeColorG
    vecg = vrEdgeColorG
    vrEdgeColorB = vrEdgeColor.vrEdgeColorB
    vecb = vrEdgeColorB

    vrEdgeStyle = VrEdgeStyleEnumField()
    vres = vrEdgeStyle

    vrEdgePriority = LongField()
    vrep = vrEdgePriority

    vrHiddenEdges = BoolField()
    vrhe = vrHiddenEdges

    vrHiddenEdgesOnTransparent = BoolField()
    vrht = vrHiddenEdgesOnTransparent

    vrOutlinesAtIntersections = BoolField()
    vroi = vrOutlinesAtIntersections

    materialAlphaGain = FloatField()
    maga = materialAlphaGain

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

    hardwareShader = HardwareShaderField()
    hws = hardwareShader
    hardwareShaderR = hardwareShader.hardwareShaderR
    hwr = hardwareShaderR
    hardwareShaderG = hardwareShader.hardwareShaderG
    hwg = hardwareShaderG
    hardwareShaderB = hardwareShader.hardwareShaderB
    hwb = hardwareShaderB

    reflectionLimit = ShortField()
    fll = reflectionLimit

    specularColor = SpecularColorField()
    sc = specularColor
    specularColorR = specularColor.specularColorR
    sr = specularColorR
    specularColorG = specularColor.specularColorG
    sg = specularColorG
    specularColorB = specularColor.specularColorB
    sb = specularColorB

    reflectivity = FloatField()
    rfl = reflectivity

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

    tangentUCamera = TangentUCameraField()
    utan = tangentUCamera
    tangentUCameraX = tangentUCamera.tangentUCameraX
    utnx = tangentUCameraX
    tangentUCameraY = tangentUCamera.tangentUCameraY
    utny = tangentUCameraY
    tangentUCameraZ = tangentUCamera.tangentUCameraZ
    utnz = tangentUCameraZ

    tangentVCamera = TangentVCameraField()
    vtan = tangentVCamera
    tangentVCameraX = tangentVCamera.tangentVCameraX
    vtnx = tangentVCameraX
    tangentVCameraY = tangentVCamera.tangentVCameraY
    vtny = tangentVCameraY
    tangentVCameraZ = tangentVCamera.tangentVCameraZ
    vtnz = tangentVCameraZ

    spreadX = FloatField()
    sprx = spreadX

    spreadY = FloatField()
    spry = spreadY

    roughness = FloatField()
    roug = roughness

    angle = FloatField()
    angl = angle

    fresnelRefractiveIndex = FloatField()
    frfi = fresnelRefractiveIndex

    anisotropicReflectivity = BoolField()
    arfl = anisotropicReflectivity
