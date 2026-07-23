# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.lambert import (
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
    TransparencyField,
    VrEdgeColorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField


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


class _GeneratedLambert(DG):
    __slots__ = ()

    NODE_TYPE = "lambert"

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

    diffuse = FloatField(default_value=0.800000011920929, min_value=0.0, soft_max_value=1.0)
    dc = diffuse

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0), readable=False)
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    color = ColorField(default_value=(0.5, 0.5, 0.5))
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    transparency = TransparencyField(default_value=(0.0, 0.0, 0.0))
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    ambientColor = AmbientColorField(default_value=(0.0, 0.0, 0.0))
    ambc = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField(default_value=(0.0, 0.0, 0.0))
    ic = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    translucence = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tc = translucence

    translucenceFocus = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    tcf = translucenceFocus

    translucenceDepth = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=5.0)
    trsd = translucenceDepth

    opacityDepth = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    opad = opacityDepth

    glowIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gi = glowIntensity

    vrOverwriteDefaults = BoolField(default_value=False)
    vrod = vrOverwriteDefaults

    vrFillObject = VrFillObjectEnumField(default_value=0)
    vrfo = vrFillObject

    vrEdgeWeight = DoubleField(default_value=0.0)
    vrew = vrEdgeWeight

    vrEdgeColor = VrEdgeColorField(default_value=(0.5, 0.5, 0.5))
    vrec = vrEdgeColor
    vrEdgeColorR = vrEdgeColor.vrEdgeColorR
    vecr = vrEdgeColorR
    vrEdgeColorG = vrEdgeColor.vrEdgeColorG
    vecg = vrEdgeColorG
    vrEdgeColorB = vrEdgeColor.vrEdgeColorB
    vecb = vrEdgeColorB

    vrEdgeStyle = VrEdgeStyleEnumField(default_value=0)
    vres = vrEdgeStyle

    vrEdgePriority = LongField(default_value=0, min_value=0)
    vrep = vrEdgePriority

    vrHiddenEdges = BoolField(default_value=False)
    vrhe = vrHiddenEdges

    vrHiddenEdgesOnTransparent = BoolField(default_value=False)
    vrht = vrHiddenEdgesOnTransparent

    vrOutlinesAtIntersections = BoolField(default_value=True)
    vroi = vrOutlinesAtIntersections

    materialAlphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    maga = materialAlphaGain

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

    hardwareShader = HardwareShaderField(default_value=(0.0, 0.0, 0.0))
    hws = hardwareShader
    hardwareShaderR = hardwareShader.hardwareShaderR
    hwr = hardwareShaderR
    hardwareShaderG = hardwareShader.hardwareShaderG
    hwg = hardwareShaderG
    hardwareShaderB = hardwareShader.hardwareShaderB
    hwb = hardwareShaderB
