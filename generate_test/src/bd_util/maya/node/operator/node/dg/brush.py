# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.brush import (
    BudColorField,
    Color1Field,
    Color2Field,
    EnvironmentField,
    GlowColorField,
    Incandescence1Field,
    Incandescence2Field,
    LeafColor1Field,
    LeafColor2Field,
    LeafCurlField,
    LeafWidthScaleField,
    LightDirectionField,
    PetalColor1Field,
    PetalColor2Field,
    PetalCurlField,
    PetalWidthScaleField,
    ReflectionRolloffField,
    SpecularColorField,
    SunDirectionField,
    TexColor1Field,
    TexColor2Field,
    ThornBaseColorField,
    ThornTipColorField,
    Transparency1Field,
    Transparency2Field,
    TurbulenceOffsetField,
    TwigLengthScaleField,
    UniformForceField,
    WidthScaleField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class BrushTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PAINT = 0
    SMEAR = 1
    BLUR = 2
    ERASE = 3
    THINLINE = 4
    MESH = 5


class BrushTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PAINT = 0
    SMEAR = 1
    BLUR = 2
    ERASE = 3
    THINLINE = 4
    MESH = 5

    NAME_MAP = {
        PAINT: "Paint",
        SMEAR: "Smear",
        BLUR: "Blur",
        ERASE: "Erase",
        THINLINE: "ThinLine",
        MESH: "Mesh",
    }


class BrushTypeEnumField(
    EnumField[BrushTypeEnumAttrOperator, BrushTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BrushTypeEnumAttrOperator
    PLUG_CLS = BrushTypeEnumPlugOperator


class FakeShadowEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    _2D_OFFSET = 1
    _3D_CAST = 2


class FakeShadowEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    _2D_OFFSET = 1
    _3D_CAST = 2

    NAME_MAP = {
        NONE: "None",
        _2D_OFFSET: "2D Offset",
        _3D_CAST: "3D Cast",
    }


class FakeShadowEnumField(
    EnumField[FakeShadowEnumAttrOperator, FakeShadowEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FakeShadowEnumAttrOperator
    PLUG_CLS = FakeShadowEnumPlugOperator


class DepthShadowTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SURFACEDEPTH = 0
    PATHDIST = 1


class DepthShadowTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SURFACEDEPTH = 0
    PATHDIST = 1

    NAME_MAP = {
        SURFACEDEPTH: "SurfaceDepth",
        PATHDIST: "PathDist",
    }


class DepthShadowTypeEnumField(
    EnumField[DepthShadowTypeEnumAttrOperator, DepthShadowTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DepthShadowTypeEnumAttrOperator
    PLUG_CLS = DepthShadowTypeEnumPlugOperator


class TubeDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALONG_NORMAL = 0
    ALONG_PATH = 1


class TubeDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALONG_NORMAL = 0
    ALONG_PATH = 1

    NAME_MAP = {
        ALONG_NORMAL: "Along Normal",
        ALONG_PATH: "Along Path",
    }


class TubeDirectionEnumField(
    EnumField[TubeDirectionEnumAttrOperator, TubeDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TubeDirectionEnumAttrOperator
    PLUG_CLS = TubeDirectionEnumPlugOperator


class TurbulenceTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    LOCAL_FORCE = 1
    WORLD_FORCE = 2
    LOCAL_DISPLACEMENT = 3
    WORLD_DISPLACEMENT = 4
    GRASS_WIND = 5
    TREE_WIND = 6


class TurbulenceTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    LOCAL_FORCE = 1
    WORLD_FORCE = 2
    LOCAL_DISPLACEMENT = 3
    WORLD_DISPLACEMENT = 4
    GRASS_WIND = 5
    TREE_WIND = 6

    NAME_MAP = {
        OFF: "Off",
        LOCAL_FORCE: "Local Force",
        WORLD_FORCE: "World Force",
        LOCAL_DISPLACEMENT: "Local Displacement",
        WORLD_DISPLACEMENT: "World Displacement",
        GRASS_WIND: "Grass Wind",
        TREE_WIND: "Tree Wind",
    }


class TurbulenceTypeEnumField(
    EnumField[TurbulenceTypeEnumAttrOperator, TurbulenceTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceTypeEnumAttrOperator
    PLUG_CLS = TurbulenceTypeEnumPlugOperator


class TurbulenceInterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH_OVER_TIME = 1
    SMOOTH_OVER_TIME_AND_SPACE = 2


class TurbulenceInterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    SMOOTH_OVER_TIME = 1
    SMOOTH_OVER_TIME_AND_SPACE = 2

    NAME_MAP = {
        LINEAR: "Linear",
        SMOOTH_OVER_TIME: "Smooth over Time",
        SMOOTH_OVER_TIME_AND_SPACE: "Smooth over Time and Space",
    }


class TurbulenceInterpolationEnumField(
    EnumField[TurbulenceInterpolationEnumAttrOperator, TurbulenceInterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceInterpolationEnumAttrOperator
    PLUG_CLS = TurbulenceInterpolationEnumPlugOperator


class CollideMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OUTSIDE = 0
    INSIDE = 1
    BOTH_SIDES = 2


class CollideMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OUTSIDE = 0
    INSIDE = 1
    BOTH_SIDES = 2

    NAME_MAP = {
        OUTSIDE: "Outside",
        INSIDE: "Inside",
        BOTH_SIDES: "Both Sides",
    }


class CollideMethodEnumField(
    EnumField[CollideMethodEnumAttrOperator, CollideMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideMethodEnumAttrOperator
    PLUG_CLS = CollideMethodEnumPlugOperator


class LeafLocationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ON_ALL = 0
    ON_SECONDARY_BRANCHES_ONLY = 1
    ON_TWIGS_ONLY = 2


class LeafLocationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ON_ALL = 0
    ON_SECONDARY_BRANCHES_ONLY = 1
    ON_TWIGS_ONLY = 2

    NAME_MAP = {
        ON_ALL: "On All",
        ON_SECONDARY_BRANCHES_ONLY: "On Secondary Branches Only",
        ON_TWIGS_ONLY: "On Twigs Only",
    }


class LeafLocationEnumField(
    EnumField[LeafLocationEnumAttrOperator, LeafLocationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLocationEnumAttrOperator
    PLUG_CLS = LeafLocationEnumPlugOperator


class FlowerLocationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ON_ALL = 0
    ON_SECONDARY_BRANCHES_ONLY = 1
    ON_TWIGS_ONLY = 2


class FlowerLocationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ON_ALL = 0
    ON_SECONDARY_BRANCHES_ONLY = 1
    ON_TWIGS_ONLY = 2

    NAME_MAP = {
        ON_ALL: "On All",
        ON_SECONDARY_BRANCHES_ONLY: "On Secondary Branches Only",
        ON_TWIGS_ONLY: "On Twigs Only",
    }


class FlowerLocationEnumField(
    EnumField[FlowerLocationEnumAttrOperator, FlowerLocationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlowerLocationEnumAttrOperator
    PLUG_CLS = FlowerLocationEnumPlugOperator


class SimplifyMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TUBES_PER_STEP = 0
    SEGMENTS = 1
    TUBES_AND_SEGMENTS = 2


class SimplifyMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TUBES_PER_STEP = 0
    SEGMENTS = 1
    TUBES_AND_SEGMENTS = 2

    NAME_MAP = {
        TUBES_PER_STEP: "Tubes Per Step",
        SEGMENTS: "Segments",
        TUBES_AND_SEGMENTS: "Tubes and Segments",
    }


class SimplifyMethodEnumField(
    EnumField[SimplifyMethodEnumAttrOperator, SimplifyMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SimplifyMethodEnumAttrOperator
    PLUG_CLS = SimplifyMethodEnumPlugOperator


class ColorLengthMapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1


class ColorLengthMapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1

    NAME_MAP = {
        LENGTH: "length",
        MAXLENGTH: "maxLength",
    }


class ColorLengthMapEnumField(
    EnumField[ColorLengthMapEnumAttrOperator, ColorLengthMapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorLengthMapEnumAttrOperator
    PLUG_CLS = ColorLengthMapEnumPlugOperator


class TranspLengthMapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1


class TranspLengthMapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1

    NAME_MAP = {
        LENGTH: "length",
        MAXLENGTH: "maxLength",
    }


class TranspLengthMapEnumField(
    EnumField[TranspLengthMapEnumAttrOperator, TranspLengthMapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranspLengthMapEnumAttrOperator
    PLUG_CLS = TranspLengthMapEnumPlugOperator


class IncandLengthMapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1


class IncandLengthMapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1

    NAME_MAP = {
        LENGTH: "length",
        MAXLENGTH: "maxLength",
    }


class IncandLengthMapEnumField(
    EnumField[IncandLengthMapEnumAttrOperator, IncandLengthMapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandLengthMapEnumAttrOperator
    PLUG_CLS = IncandLengthMapEnumPlugOperator


class WidthLengthMapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1


class WidthLengthMapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1

    NAME_MAP = {
        LENGTH: "length",
        MAXLENGTH: "maxLength",
    }


class WidthLengthMapEnumField(
    EnumField[WidthLengthMapEnumAttrOperator, WidthLengthMapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WidthLengthMapEnumAttrOperator
    PLUG_CLS = WidthLengthMapEnumPlugOperator


class SplitLengthMapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1


class SplitLengthMapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LENGTH = 0
    MAXLENGTH = 1

    NAME_MAP = {
        LENGTH: "length",
        MAXLENGTH: "maxLength",
    }


class SplitLengthMapEnumField(
    EnumField[SplitLengthMapEnumAttrOperator, SplitLengthMapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SplitLengthMapEnumAttrOperator
    PLUG_CLS = SplitLengthMapEnumPlugOperator


class TextureTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CHECKER = 0
    U_RAMP = 1
    V_RAMP = 2
    FRACTAL = 3
    FILE = 4


class TextureTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CHECKER = 0
    U_RAMP = 1
    V_RAMP = 2
    FRACTAL = 3
    FILE = 4

    NAME_MAP = {
        CHECKER: "Checker",
        U_RAMP: "U Ramp",
        V_RAMP: "V Ramp",
        FRACTAL: "Fractal",
        FILE: "File",
    }


class TextureTypeEnumField(
    EnumField[TextureTypeEnumAttrOperator, TextureTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureTypeEnumAttrOperator
    PLUG_CLS = TextureTypeEnumPlugOperator


class MapMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FULL_VIEW = 0
    BRUSH_START = 1
    TUBE_2D = 2
    TUBE_3D = 3


class MapMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FULL_VIEW = 0
    BRUSH_START = 1
    TUBE_2D = 2
    TUBE_3D = 3

    NAME_MAP = {
        FULL_VIEW: "Full View",
        BRUSH_START: "Brush Start",
        TUBE_2D: "Tube 2D",
        TUBE_3D: "Tube 3D",
    }


class MapMethodEnumField(
    EnumField[MapMethodEnumAttrOperator, MapMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapMethodEnumAttrOperator
    PLUG_CLS = MapMethodEnumPlugOperator


class Brush(DG):
    __slots__ = ()

    NODE_TYPE = "brush"

    outBrush = TypedField()
    obr = outBrush

    time = TimeField()
    tim = time

    globalScale = DoubleField()
    gsc = globalScale

    depth = BoolField()
    dep = depth

    modifyDepth = BoolField()
    mdp = modifyDepth

    modifyColor = BoolField()
    mdc = modifyColor

    modifyAlpha = BoolField()
    mda = modifyAlpha

    illuminated = BoolField()
    ill = illuminated

    castShadows = BoolField()
    csd = castShadows

    lightingBasedWidth = DoubleField()
    lbw = lightingBasedWidth

    branches = BoolField()
    brc = branches

    twigs = BoolField()
    twg = twigs

    buds = BoolField()
    bud = buds

    leaves = BoolField()
    lvs = leaves

    flowers = BoolField()
    flw = flowers

    brushType = BrushTypeEnumField()
    brt = brushType

    brushWidth = DoubleField()
    bwd = brushWidth

    screenspaceWidth = BoolField()
    spw = screenspaceWidth

    distanceScaling = DoubleField()
    dsl = distanceScaling

    minPixelWidth = DoubleField()
    mpw = minPixelWidth

    maxPixelWidth = DoubleField()
    mxp = maxPixelWidth

    stampDensity = DoubleField()
    sdn = stampDensity

    softness = DoubleField()
    sft = softness

    edgeAntialias = BoolField()
    eaa = edgeAntialias

    edgeClip = BoolField()
    ecl = edgeClip

    edgeClipDepth = DoubleField()
    ecd = edgeClipDepth

    occlusionWidthScale = BoolField()
    ows = occlusionWidthScale

    blurIntensity = LongField()
    bin = blurIntensity

    color1 = Color1Field()
    cl1 = color1
    color1R = color1.color1R
    c1r = color1R
    color1G = color1.color1G
    c1g = color1G
    color1B = color1.color1B
    c1b = color1B

    color2 = Color2Field()
    cl2 = color2
    color2R = color2.color2R
    c2r = color2R
    color2G = color2.color2G
    c2g = color2G
    color2B = color2.color2B
    c2b = color2B

    transparency1 = Transparency1Field()
    tn1 = transparency1
    transparency1R = transparency1.transparency1R
    t1r = transparency1R
    transparency1G = transparency1.transparency1G
    t1g = transparency1G
    transparency1B = transparency1.transparency1B
    t1b = transparency1B

    transparency2 = Transparency2Field()
    tn2 = transparency2
    transparency2R = transparency2.transparency2R
    t2r = transparency2R
    transparency2G = transparency2.transparency2G
    t2g = transparency2G
    transparency2B = transparency2.transparency2B
    t2b = transparency2B

    incandescence1 = Incandescence1Field()
    in1 = incandescence1
    incandescence1R = incandescence1.incandescence1R
    i1r = incandescence1R
    incandescence1G = incandescence1.incandescence1G
    i1g = incandescence1G
    incandescence1B = incandescence1.incandescence1B
    i1b = incandescence1B

    incandescence2 = Incandescence2Field()
    in2 = incandescence2
    incandescence2R = incandescence2.incandescence2R
    i2r = incandescence2R
    incandescence2G = incandescence2.incandescence2G
    i2g = incandescence2G
    incandescence2B = incandescence2.incandescence2B
    i2b = incandescence2B

    specularColor = SpecularColorField()
    spc = specularColor
    specularColorR = specularColor.specularColorR
    spr = specularColorR
    specularColorG = specularColor.specularColorG
    spg = specularColorG
    specularColorB = specularColor.specularColorB
    spb = specularColorB

    specular = DoubleField()
    spe = specular

    specularPower = DoubleField()
    spp = specularPower

    translucence = DoubleField()
    trn = translucence

    glow = DoubleField()
    glw = glow

    glowColor = GlowColorField()
    glc = glowColor
    glowColorR = glowColor.glowColorR
    glr = glowColorR
    glowColorG = glowColor.glowColorG
    glg = glowColorG
    glowColorB = glowColor.glowColorB
    glb = glowColorB

    glowSpread = DoubleField()
    gls = glowSpread

    shaderGlow = DoubleField()
    sgl = shaderGlow

    hueRand = DoubleField()
    chr = hueRand

    satRand = DoubleField()
    csr = satRand

    valRand = DoubleField()
    cvr = valRand

    rootFade = DoubleField()
    rfd = rootFade

    tipFade = DoubleField()
    tfd = tipFade

    fakeShadow = FakeShadowEnumField()
    fks = fakeShadow

    shadowOffset = DoubleField()
    sof = shadowOffset

    shadowDiffusion = DoubleField()
    sdf = shadowDiffusion

    shadowTransparency = DoubleField()
    stn = shadowTransparency

    backShadow = DoubleField()
    bks = backShadow

    brightnessRand = DoubleField()
    brn = brightnessRand

    centerShadow = DoubleField()
    cns = centerShadow

    depthShadowType = DepthShadowTypeEnumField()
    dpt = depthShadowType

    depthShadow = DoubleField()
    dpl = depthShadow

    depthShadowDepth = DoubleField()
    dps = depthShadowDepth

    realLights = BoolField()
    rll = realLights

    lightDirection = LightDirectionField()
    ldr = lightDirection
    lightDirectionX = lightDirection.lightDirectionX
    ldx = lightDirectionX
    lightDirectionY = lightDirection.lightDirectionY
    ldy = lightDirectionY
    lightDirectionZ = lightDirection.lightDirectionZ
    ldz = lightDirectionZ

    gapSize = DoubleField()
    gsz = gapSize

    gapSpacing = DoubleField()
    gsp = gapSpacing

    gapRand = DoubleField()
    grn = gapRand

    flowSpeed = DoubleField()
    fws = flowSpeed

    textureFlow = BoolField()
    tfl = textureFlow

    timeClip = BoolField()
    tcl = timeClip

    strokeTime = BoolField()
    srm = strokeTime

    startTime = DoubleField()
    sti = startTime

    endTime = DoubleField()
    eti = endTime

    tubes = BoolField()
    tub = tubes

    creationScript = DataStringField()
    csc = creationScript

    runtimeScript = DataStringField()
    rsc = runtimeScript

    tubeCompletion = BoolField()
    tcm = tubeCompletion

    tubesPerStep = DoubleField()
    tps = tubesPerStep

    tubeRand = DoubleField()
    trd = tubeRand

    startTubes = LongField()
    stb = startTubes

    lengthMax = DoubleField()
    lnx = lengthMax

    lengthMin = DoubleField()
    lnn = lengthMin

    segments = LongField()
    sgm = segments

    tubeWidth1 = DoubleField()
    tw1 = tubeWidth1

    tubeWidth2 = DoubleField()
    tw2 = tubeWidth2

    widthRand = DoubleField()
    wdr = widthRand

    widthBias = DoubleField()
    wdb = widthBias

    lengthFlex = DoubleField()
    lfx = lengthFlex

    segmentLengthBias = DoubleField()
    sgb = segmentLengthBias

    segmentWidthBias = DoubleField()
    swb = segmentWidthBias

    tubeDirection = TubeDirectionEnumField()
    tdr = tubeDirection

    elevationMin = DoubleField()
    elm = elevationMin

    elevationMax = DoubleField()
    elx = elevationMax

    azimuthMin = DoubleField()
    azn = azimuthMin

    azimuthMax = DoubleField()
    azx = azimuthMax

    flatness1 = DoubleField()
    fl1 = flatness1

    flatness2 = DoubleField()
    fl2 = flatness2

    twist = DoubleField()
    twi = twist

    twistRate = DoubleField()
    twr = twistRate

    twistRand = DoubleField()
    twd = twistRand

    spiralMin = DoubleField()
    spm = spiralMin

    spiralMax = DoubleField()
    spx = spiralMax

    spiralDecay = DoubleField()
    spd = spiralDecay

    bend = DoubleField()
    ben = bend

    bendBias = DoubleField()
    bnb = bendBias

    displacementDelay = DoubleField()
    ddl = displacementDelay

    wiggle = DoubleField()
    wgl = wiggle

    wiggleFrequency = DoubleField()
    wgf = wiggleFrequency

    wiggleOffset = DoubleField()
    wgo = wiggleOffset

    curl = DoubleField()
    crl = curl

    curlFrequency = DoubleField()
    crf = curlFrequency

    curlOffset = DoubleField()
    cro = curlOffset

    noise = DoubleField()
    noi = noise

    noiseFrequency = DoubleField()
    nof = noiseFrequency

    noiseOffset = DoubleField()
    noo = noiseOffset

    splitMaxDepth = DoubleField()
    smd = splitMaxDepth

    splitRand = DoubleField()
    srd = splitRand

    splitAngle = DoubleField()
    spa = splitAngle

    splitSizeDecay = DoubleField()
    ssd = splitSizeDecay

    splitBias = DoubleField()
    slb = splitBias

    splitTwist = DoubleField()
    slt = splitTwist

    startBranches = DoubleField()
    sbr = startBranches

    numBranches = LongField()
    nbr = numBranches

    branchDropout = DoubleField()
    bdr = branchDropout

    middleBranch = BoolField()
    mbr = middleBranch

    minSize = DoubleField()
    mms = minSize

    pathFollow = DoubleField()
    pfl = pathFollow

    pathAttract = DoubleField()
    pat = pathAttract

    curveFollow = DoubleField()
    cfw = curveFollow

    curveAttract = DoubleField()
    cva = curveAttract

    curveMaxDist = DoubleField()
    cmd = curveMaxDist

    surfaceAttract = DoubleField()
    sfa = surfaceAttract

    maxAttractDistance = DoubleField()
    mad = maxAttractDistance

    uniformForce = UniformForceField()
    ufr = uniformForce
    uniformForceX = uniformForce.uniformForceX
    ufx = uniformForceX
    uniformForceY = uniformForce.uniformForceY
    ufy = uniformForceY
    uniformForceZ = uniformForce.uniformForceZ
    ufz = uniformForceZ

    turbulenceType = TurbulenceTypeEnumField()
    trt = turbulenceType

    turbulenceInterpolation = TurbulenceInterpolationEnumField()
    tin = turbulenceInterpolation

    turbulence = DoubleField()
    tur = turbulence

    turbulenceFrequency = DoubleField()
    trf = turbulenceFrequency

    turbulenceSpeed = DoubleField()
    trs = turbulenceSpeed

    turbulenceOffset = TurbulenceOffsetField()
    tro = turbulenceOffset
    turbulenceOffsetX = turbulenceOffset.turbulenceOffsetX
    trx = turbulenceOffsetX
    turbulenceOffsetY = turbulenceOffset.turbulenceOffsetY
    try_ = turbulenceOffsetY
    turbulenceOffsetZ = turbulenceOffset.turbulenceOffsetZ
    trz = turbulenceOffsetZ

    random = DoubleField()
    ran = random

    gravity = DoubleField()
    grv = gravity

    momentum = DoubleField()
    mmt = momentum

    surfaceCollide = BoolField()
    scl = surfaceCollide

    collideMethod = CollideMethodEnumField()
    clmp = collideMethod

    surfaceSnap = BoolField()
    ssn = surfaceSnap

    deflection = BoolField()
    def_ = deflection

    deflectionMin = DoubleField()
    dfm = deflectionMin

    deflectionMax = DoubleField()
    dfx = deflectionMax

    sunDirection = SunDirectionField()
    snd = sunDirection
    sunDirectionX = sunDirection.sunDirectionX
    sndx = sunDirectionX
    sunDirectionY = sunDirection.sunDirectionY
    sndy = sunDirectionY
    sunDirectionZ = sunDirection.sunDirectionZ
    sndz = sunDirectionZ

    twigsInCluster = LongField()
    tic = twigsInCluster

    twigDropout = DoubleField()
    tdp = twigDropout

    twigAngle1 = DoubleField()
    ta1 = twigAngle1

    twigAngle2 = DoubleField()
    ta2 = twigAngle2

    twigTwist = DoubleField()
    ttw = twigTwist

    twigLength = DoubleField()
    twl = twigLength

    twigStart = DoubleField()
    tst = twigStart

    numTwigClusters = DoubleField()
    ntc = numTwigClusters

    twigBaseWidth = DoubleField()
    twb = twigBaseWidth

    twigTipWidth = DoubleField()
    twt = twigTipWidth

    twigStiffness = DoubleField()
    tgs = twigStiffness

    branchAfterTwigs = BoolField()
    bat = branchAfterTwigs

    leavesInCluster = LongField()
    lic = leavesInCluster

    leafLocation = LeafLocationEnumField()
    llo = leafLocation

    leafDropout = DoubleField()
    ldp = leafDropout

    leafAngle1 = DoubleField()
    ll1 = leafAngle1

    leafAngle2 = DoubleField()
    ll2 = leafAngle2

    leafTwist = DoubleField()
    ltw = leafTwist

    leafBend = DoubleField()
    lbn = leafBend

    leafCurl = LeafCurlField(multi=True)
    lcl = leafCurl

    leafTwirl = DoubleField()
    ltwl = leafTwirl

    leafFaceSun = DoubleField()
    lfcs = leafFaceSun

    leafSegments = LongField()
    lsg = leafSegments

    leafStart = DoubleField()
    lst = leafStart

    numLeafClusters = DoubleField()
    nlc = numLeafClusters

    leafFlatness = DoubleField()
    lft = leafFlatness

    leafLength = DoubleField()
    lln = leafLength

    leafBaseWidth = DoubleField()
    leb = leafBaseWidth

    leafTipWidth = DoubleField()
    let = leafTipWidth

    leafSizeDecay = DoubleField()
    lsd = leafSizeDecay

    leafSizeRand = DoubleField()
    lzr = leafSizeRand

    leafTranslucence = DoubleField()
    ltr = leafTranslucence

    leafSpecular = DoubleField()
    lsp = leafSpecular

    terminalLeaf = BoolField()
    tml = terminalLeaf

    leafColor1 = LeafColor1Field()
    lc1 = leafColor1
    leafColor1R = leafColor1.leafColor1R
    lr1 = leafColor1R
    leafColor1G = leafColor1.leafColor1G
    lg1 = leafColor1G
    leafColor1B = leafColor1.leafColor1B
    lb1 = leafColor1B

    leafColor2 = LeafColor2Field()
    lc2 = leafColor2
    leafColor2R = leafColor2.leafColor2R
    lr2 = leafColor2R
    leafColor2G = leafColor2.leafColor2G
    lg2 = leafColor2G
    leafColor2B = leafColor2.leafColor2B
    lb2 = leafColor2B

    leafHueRand = DoubleField()
    lhr = leafHueRand

    leafSatRand = DoubleField()
    lsr = leafSatRand

    leafValRand = DoubleField()
    lvr = leafValRand

    leafUseBranchTex = BoolField()
    lub = leafUseBranchTex

    leafImage = DataStringField()
    lim = leafImage

    leafStiffness = DoubleField()
    lfs = leafStiffness

    budSize = DoubleField()
    bds = budSize

    budColor = BudColorField()
    bcr = budColor
    budColorR = budColor.budColorR
    bur = budColorR
    budColorG = budColor.budColorG
    bug = budColorG
    budColorB = budColor.budColorB
    bub = budColorB

    petalsInFlower = LongField()
    pif = petalsInFlower

    flowerLocation = FlowerLocationEnumField()
    flc = flowerLocation

    petalDropout = DoubleField()
    pdp = petalDropout

    flowerAngle1 = DoubleField()
    fw1 = flowerAngle1

    flowerAngle2 = DoubleField()
    fw2 = flowerAngle2

    flowerTwist = DoubleField()
    ftw = flowerTwist

    petalBend = DoubleField()
    pbn = petalBend

    petalCurl = PetalCurlField(multi=True)
    pcl = petalCurl

    petalTwirl = DoubleField()
    lpwl = petalTwirl

    flowerFaceSun = DoubleField()
    ffcs = flowerFaceSun

    petalSegments = LongField()
    psg = petalSegments

    flowerStart = DoubleField()
    fst = flowerStart

    numFlowers = DoubleField()
    nfl = numFlowers

    petalFlatness = DoubleField()
    pft = petalFlatness

    petalLength = DoubleField()
    pln = petalLength

    petalBaseWidth = DoubleField()
    ptb = petalBaseWidth

    petalTipWidth = DoubleField()
    ptt = petalTipWidth

    flowerSizeDecay = DoubleField()
    fsd = flowerSizeDecay

    flowerSizeRand = DoubleField()
    fzr = flowerSizeRand

    flowerTranslucence = DoubleField()
    ftr = flowerTranslucence

    flowerSpecular = DoubleField()
    fsp = flowerSpecular

    petalColor1 = PetalColor1Field()
    pc1 = petalColor1
    petalColor1R = petalColor1.petalColor1R
    pr1 = petalColor1R
    petalColor1G = petalColor1.petalColor1G
    pg1 = petalColor1G
    petalColor1B = petalColor1.petalColor1B
    pb1 = petalColor1B

    petalColor2 = PetalColor2Field()
    pc2 = petalColor2
    petalColor2R = petalColor2.petalColor2R
    pr2 = petalColor2R
    petalColor2G = petalColor2.petalColor2G
    pg2 = petalColor2G
    petalColor2B = petalColor2.petalColor2B
    pb2 = petalColor2B

    flowerHueRand = DoubleField()
    fhr = flowerHueRand

    flowerSatRand = DoubleField()
    fsr = flowerSatRand

    flowerValRand = DoubleField()
    fvr = flowerValRand

    flowerUseBranchTex = BoolField()
    fub = flowerUseBranchTex

    flowerImage = DataStringField()
    fim = flowerImage

    flowerStiffness = DoubleField()
    fls = flowerStiffness

    simplifyMethod = SimplifyMethodEnumField()
    smp = simplifyMethod

    colorLengthMap = ColorLengthMapEnumField()
    clm = colorLengthMap

    transpLengthMap = TranspLengthMapEnumField()
    tlm = transpLengthMap

    incandLengthMap = IncandLengthMapEnumField()
    ilm = incandLengthMap

    widthLengthMap = WidthLengthMapEnumField()
    wlm = widthLengthMap

    splitLengthMap = SplitLengthMapEnumField()
    spl = splitLengthMap

    mapColor = BoolField()
    mcl = mapColor

    mapOpacity = BoolField()
    mop = mapOpacity

    mapDisplacement = BoolField()
    mds = mapDisplacement

    textureType = TextureTypeEnumField()
    txt = textureType

    mapMethod = MapMethodEnumField()
    mmd = mapMethod

    texColorScale = DoubleField()
    tcs = texColorScale

    texColorOffset = DoubleField()
    tco = texColorOffset

    texOpacityScale = DoubleField()
    tos = texOpacityScale

    texOpacityOffset = DoubleField()
    too = texOpacityOffset

    displacementScale = DoubleField()
    dsc = displacementScale

    displacementOffset = DoubleField()
    dof = displacementOffset

    bumpIntensity = DoubleField()
    bmi = bumpIntensity

    bumpBlur = DoubleField()
    bbl = bumpBlur

    luminanceIsDisplacement = BoolField()
    lid = luminanceIsDisplacement

    texColor1 = TexColor1Field()
    tc1 = texColor1
    texColor1R = texColor1.texColor1R
    x1r = texColor1R
    texColor1G = texColor1.texColor1G
    x1g = texColor1G
    texColor1B = texColor1.texColor1B
    x1b = texColor1B

    texColor2 = TexColor2Field()
    tc2 = texColor2
    texColor2R = texColor2.texColor2R
    x2r = texColor2R
    texColor2G = texColor2.texColor2G
    x2g = texColor2G
    texColor2B = texColor2.texColor2B
    x2b = texColor2B

    texAlpha1 = DoubleField()
    al1 = texAlpha1

    texAlpha2 = DoubleField()
    al2 = texAlpha2

    texUniformity = DoubleField()
    txu = texUniformity

    fringeRemoval = BoolField()
    frm = fringeRemoval

    repeatU = DoubleField()
    rpu = repeatU

    repeatV = DoubleField()
    rpv = repeatV

    offsetU = DoubleField()
    ofu = offsetU

    offsetV = DoubleField()
    ofv = offsetV

    blurMult = DoubleField()
    bmt = blurMult

    smear = DoubleField()
    smr = smear

    smearU = DoubleField()
    sru = smearU

    smearV = DoubleField()
    srv = smearV

    imageName = DataStringField()
    imn = imageName

    useFrameExtension = BoolField()
    ufe = useFrameExtension

    frameExtension = LongField()
    fe = frameExtension

    fractalRatio = DoubleField()
    fra = fractalRatio

    fractalAmplitude = DoubleField()
    fam = fractalAmplitude

    fractalThreshold = DoubleField()
    fth = fractalThreshold

    multiStreaks = LongField()
    mst = multiStreaks

    multiStreakSpread1 = DoubleField()
    ms1 = multiStreakSpread1

    multiStreakSpread2 = DoubleField()
    ms2 = multiStreakSpread2

    multiStreakDiffuseRand = DoubleField()
    msdr = multiStreakDiffuseRand

    multiStreakSpecularRand = DoubleField()
    mssr = multiStreakSpecularRand

    multiStreakLightAll = BoolField()
    msla = multiStreakLightAll

    singleSided = BoolField()
    snsd = singleSided

    tubeSections = LongField()
    tbs = tubeSections

    subSegments = LongField()
    ssg = subSegments

    perPixelLighting = BoolField()
    ppl = perPixelLighting

    widthScale = WidthScaleField(multi=True)
    wsc = widthScale

    leafWidthScale = LeafWidthScaleField(multi=True)
    lws = leafWidthScale

    petalWidthScale = PetalWidthScaleField(multi=True)
    pws = petalWidthScale

    twigLengthScale = TwigLengthScaleField(multi=True)
    tls = twigLengthScale

    branchThorns = BoolField()
    bth = branchThorns

    twigThorns = BoolField()
    tth = twigThorns

    leafThorns = BoolField()
    lth = leafThorns

    flowerThorns = BoolField()
    flt = flowerThorns

    thornDensity = DoubleField()
    nth = thornDensity

    thornLength = DoubleField()
    tln = thornLength

    thornBaseWidth = DoubleField()
    tbwd = thornBaseWidth

    thornTipWidth = DoubleField()
    ttwd = thornTipWidth

    thornElevation = DoubleField()
    tel = thornElevation

    thornSpecular = DoubleField()
    tsp = thornSpecular

    thornBaseColor = ThornBaseColorField()
    tbc = thornBaseColor
    thornBaseColorR = thornBaseColor.thornBaseColorR
    tbcr = thornBaseColorR
    thornBaseColorG = thornBaseColor.thornBaseColorG
    tbcg = thornBaseColorG
    thornBaseColorB = thornBaseColor.thornBaseColorB
    tbcb = thornBaseColorB

    thornTipColor = ThornTipColorField()
    ttc = thornTipColor
    thornTipColorR = thornTipColor.thornTipColorR
    ttcr = thornTipColorR
    thornTipColorG = thornTipColor.thornTipColorG
    ttcg = thornTipColorG
    thornTipColorB = thornTipColor.thornTipColorB
    ttcb = thornTipColorB

    environment = EnvironmentField(multi=True)
    env = environment

    # TODO: environment.environment_ColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: environment.environment_ColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: environment.environment_ColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    reflectionRolloff = ReflectionRolloffField(multi=True)
    rro = reflectionRolloff

    branchReflectivity = DoubleField()
    brf = branchReflectivity

    leafReflectivity = DoubleField()
    lrf = leafReflectivity

    flowerReflectivity = DoubleField()
    frf = flowerReflectivity

    forwardTwist = BoolField()
    fwt = forwardTwist

    leafForwardTwist = BoolField()
    lfwt = leafForwardTwist

    petalForwardTwist = BoolField()
    lpwt = petalForwardTwist

    endCaps = BoolField()
    edc = endCaps

    hardEdges = BoolField()
    hde = hardEdges

    surfaceSampleDensity = LongField()
    susd = surfaceSampleDensity

    occupyAttraction = DoubleField()
    ocat = occupyAttraction

    attractRadiusScale = DoubleField()
    ocar = attractRadiusScale

    attractRadiusOffset = DoubleField()
    ocao = attractRadiusOffset

    occupyRadiusScale = DoubleField()
    ocrs = occupyRadiusScale

    occupyRadiusOffset = DoubleField()
    ocro = occupyRadiusOffset

    occupyBranchTermination = BoolField()
    ocbt = occupyBranchTermination
