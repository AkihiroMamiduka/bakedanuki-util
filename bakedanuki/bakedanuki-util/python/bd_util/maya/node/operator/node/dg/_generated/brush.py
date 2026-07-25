# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.brush import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedBrush(DG):
    __slots__ = ()

    NODE_TYPE = "brush"

    outBrush = TypedField(writable=False)
    obr = outBrush

    time = TimeField(default_value=0.0)
    tim = time

    globalScale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    gsc = globalScale

    depth = BoolField(default_value=False)
    dep = depth

    modifyDepth = BoolField(default_value=True)
    mdp = modifyDepth

    modifyColor = BoolField(default_value=True)
    mdc = modifyColor

    modifyAlpha = BoolField(default_value=True)
    mda = modifyAlpha

    illuminated = BoolField(default_value=False)
    ill = illuminated

    castShadows = BoolField(default_value=False)
    csd = castShadows

    lightingBasedWidth = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lbw = lightingBasedWidth

    branches = BoolField(default_value=False)
    brc = branches

    twigs = BoolField(default_value=False)
    twg = twigs

    buds = BoolField(default_value=False)
    bud = buds

    leaves = BoolField(default_value=False)
    lvs = leaves

    flowers = BoolField(default_value=False)
    flw = flowers

    brushType = BrushTypeEnumField(default_value=0)
    brt = brushType

    brushWidth = DoubleField(default_value=0.05, soft_min_value=0.0, soft_max_value=0.5)
    bwd = brushWidth

    screenspaceWidth = BoolField(default_value=False)
    spw = screenspaceWidth

    distanceScaling = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dsl = distanceScaling

    minPixelWidth = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    mpw = minPixelWidth

    maxPixelWidth = DoubleField(default_value=1000.0, soft_min_value=0.0, soft_max_value=1000.0)
    mxp = maxPixelWidth

    stampDensity = DoubleField(default_value=8.0, soft_min_value=0.0, soft_max_value=50.0)
    sdn = stampDensity

    softness = DoubleField(default_value=0.2, soft_min_value=-1.0, soft_max_value=1.0)
    sft = softness

    edgeAntialias = BoolField(default_value=True)
    eaa = edgeAntialias

    edgeClip = BoolField(default_value=False)
    ecl = edgeClip

    edgeClipDepth = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    ecd = edgeClipDepth

    occlusionWidthScale = BoolField(default_value=False)
    ows = occlusionWidthScale

    blurIntensity = LongField(default_value=4, soft_min_value=1, soft_max_value=20)
    bin = blurIntensity

    color1 = Color1Field(default_value=(0.0, 0.0, 0.0))
    cl1 = color1
    color1R = color1.color1R
    c1r = color1R
    color1G = color1.color1G
    c1g = color1G
    color1B = color1.color1B
    c1b = color1B

    color2 = Color2Field(default_value=(1.0, 1.0, 1.0))
    cl2 = color2
    color2R = color2.color2R
    c2r = color2R
    color2G = color2.color2G
    c2g = color2G
    color2B = color2.color2B
    c2b = color2B

    transparency1 = Transparency1Field(default_value=(0.0, 0.0, 0.0))
    tn1 = transparency1
    transparency1R = transparency1.transparency1R
    t1r = transparency1R
    transparency1G = transparency1.transparency1G
    t1g = transparency1G
    transparency1B = transparency1.transparency1B
    t1b = transparency1B

    transparency2 = Transparency2Field(default_value=(0.0, 0.0, 0.0))
    tn2 = transparency2
    transparency2R = transparency2.transparency2R
    t2r = transparency2R
    transparency2G = transparency2.transparency2G
    t2g = transparency2G
    transparency2B = transparency2.transparency2B
    t2b = transparency2B

    incandescence1 = Incandescence1Field(default_value=(0.0, 0.0, 0.0))
    in1 = incandescence1
    incandescence1R = incandescence1.incandescence1R
    i1r = incandescence1R
    incandescence1G = incandescence1.incandescence1G
    i1g = incandescence1G
    incandescence1B = incandescence1.incandescence1B
    i1b = incandescence1B

    incandescence2 = Incandescence2Field(default_value=(0.0, 0.0, 0.0))
    in2 = incandescence2
    incandescence2R = incandescence2.incandescence2R
    i2r = incandescence2R
    incandescence2G = incandescence2.incandescence2G
    i2g = incandescence2G
    incandescence2B = incandescence2.incandescence2B
    i2b = incandescence2B

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    spc = specularColor
    specularColorR = specularColor.specularColorR
    spr = specularColorR
    specularColorG = specularColor.specularColorG
    spg = specularColorG
    specularColorB = specularColor.specularColorB
    spb = specularColorB

    specular = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    spe = specular

    specularPower = DoubleField(default_value=10.0, soft_min_value=0.0, soft_max_value=20.0)
    spp = specularPower

    translucence = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    trn = translucence

    glow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    glw = glow

    glowColor = GlowColorField(default_value=(0.5, 0.5, 0.5))
    glc = glowColor
    glowColorR = glowColor.glowColorR
    glr = glowColorR
    glowColorG = glowColor.glowColorG
    glg = glowColorG
    glowColorB = glowColor.glowColorB
    glb = glowColorB

    glowSpread = DoubleField(default_value=3.0, soft_min_value=1.0, soft_max_value=10.0)
    gls = glowSpread

    shaderGlow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    sgl = shaderGlow

    hueRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    chr = hueRand

    satRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    csr = satRand

    valRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cvr = valRand

    rootFade = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    rfd = rootFade

    tipFade = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tfd = tipFade

    fakeShadow = FakeShadowEnumField(default_value=0)
    fks = fakeShadow

    shadowOffset = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    sof = shadowOffset

    shadowDiffusion = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    sdf = shadowDiffusion

    shadowTransparency = DoubleField(default_value=0.8, soft_min_value=0.0, soft_max_value=1.0)
    stn = shadowTransparency

    backShadow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    bks = backShadow

    brightnessRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    brn = brightnessRand

    centerShadow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cns = centerShadow

    depthShadowType = DepthShadowTypeEnumField(default_value=0)
    dpt = depthShadowType

    depthShadow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dpl = depthShadow

    depthShadowDepth = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dps = depthShadowDepth

    realLights = BoolField(default_value=False)
    rll = realLights

    lightDirection = LightDirectionField(default_value=(0.5, 0.5, -0.5))
    ldr = lightDirection
    lightDirectionX = lightDirection.lightDirectionX
    ldx = lightDirectionX
    lightDirectionY = lightDirection.lightDirectionY
    ldy = lightDirectionY
    lightDirectionZ = lightDirection.lightDirectionZ
    ldz = lightDirectionZ

    gapSize = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gsz = gapSize

    gapSpacing = DoubleField(default_value=1.0, soft_min_value=0.02, soft_max_value=1.0)
    gsp = gapSpacing

    gapRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    grn = gapRand

    flowSpeed = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    fws = flowSpeed

    textureFlow = BoolField(default_value=True)
    tfl = textureFlow

    timeClip = BoolField(default_value=False)
    tcl = timeClip

    strokeTime = BoolField(default_value=False)
    srm = strokeTime

    startTime = DoubleField(default_value=0.0, soft_min_value=-1000.0, soft_max_value=1000.0)
    sti = startTime

    endTime = DoubleField(default_value=1000.0, soft_min_value=0.0, soft_max_value=1000.0)
    eti = endTime

    tubes = BoolField(default_value=False)
    tub = tubes

    creationScript = DataStringField()
    csc = creationScript

    runtimeScript = DataStringField()
    rsc = runtimeScript

    tubeCompletion = BoolField(default_value=True)
    tcm = tubeCompletion

    tubesPerStep = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=10.0)
    tps = tubesPerStep

    tubeRand = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    trd = tubeRand

    startTubes = LongField(default_value=0, soft_min_value=0, soft_max_value=100)
    stb = startTubes

    lengthMax = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    lnx = lengthMax

    lengthMin = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    lnn = lengthMin

    segments = LongField(default_value=10, soft_min_value=1, soft_max_value=100)
    sgm = segments

    tubeWidth1 = DoubleField(default_value=0.01, soft_min_value=0.0, soft_max_value=0.1)
    tw1 = tubeWidth1

    tubeWidth2 = DoubleField(default_value=0.01, soft_min_value=0.0, soft_max_value=0.1)
    tw2 = tubeWidth2

    widthRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    wdr = widthRand

    widthBias = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    wdb = widthBias

    lengthFlex = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lfx = lengthFlex

    segmentLengthBias = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sgb = segmentLengthBias

    segmentWidthBias = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    swb = segmentWidthBias

    tubeDirection = TubeDirectionEnumField(default_value=0)
    tdr = tubeDirection

    elevationMin = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    elm = elevationMin

    elevationMax = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    elx = elevationMax

    azimuthMin = DoubleField(default_value=-0.1, soft_min_value=-1.0, soft_max_value=1.0)
    azn = azimuthMin

    azimuthMax = DoubleField(default_value=0.1, soft_min_value=-1.0, soft_max_value=1.0)
    azx = azimuthMax

    flatness1 = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fl1 = flatness1

    flatness2 = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fl2 = flatness2

    twist = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    twi = twist

    twistRate = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    twr = twistRate

    twistRand = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    twd = twistRand

    spiralMin = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    spm = spiralMin

    spiralMax = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    spx = spiralMax

    spiralDecay = DoubleField(default_value=0.0, soft_min_value=-0.01, soft_max_value=0.01)
    spd = spiralDecay

    bend = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    ben = bend

    bendBias = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    bnb = bendBias

    displacementDelay = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    ddl = displacementDelay

    wiggle = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    wgl = wiggle

    wiggleFrequency = DoubleField(default_value=3.0, soft_min_value=0.0001, soft_max_value=100.0)
    wgf = wiggleFrequency

    wiggleOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    wgo = wiggleOffset

    curl = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    crl = curl

    curlFrequency = DoubleField(default_value=1.0, soft_min_value=0.0001, soft_max_value=100.0)
    crf = curlFrequency

    curlOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    cro = curlOffset

    noise = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    noi = noise

    noiseFrequency = DoubleField(default_value=0.2, soft_min_value=0.0001, soft_max_value=1.0)
    nof = noiseFrequency

    noiseOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.1)
    noo = noiseOffset

    splitMaxDepth = DoubleField(default_value=2.0, soft_min_value=0.0, soft_max_value=8.0)
    smd = splitMaxDepth

    splitRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    srd = splitRand

    splitAngle = DoubleField(default_value=30.0, soft_min_value=0.0, soft_max_value=180.0)
    spa = splitAngle

    splitSizeDecay = DoubleField(default_value=0.7, soft_min_value=0.5, soft_max_value=2.0)
    ssd = splitSizeDecay

    splitBias = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    slb = splitBias

    splitTwist = DoubleField(default_value=0.5, soft_min_value=-1.0, soft_max_value=1.0)
    slt = splitTwist

    startBranches = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    sbr = startBranches

    numBranches = LongField(default_value=2, soft_min_value=1, soft_max_value=10)
    nbr = numBranches

    branchDropout = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    bdr = branchDropout

    middleBranch = BoolField(default_value=False)
    mbr = middleBranch

    minSize = DoubleField(default_value=0.0001, soft_min_value=0.0, soft_max_value=0.1)
    mms = minSize

    pathFollow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    pfl = pathFollow

    pathAttract = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    pat = pathAttract

    curveFollow = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    cfw = curveFollow

    curveAttract = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    cva = curveAttract

    curveMaxDist = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    cmd = curveMaxDist

    surfaceAttract = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    sfa = surfaceAttract

    maxAttractDistance = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    mad = maxAttractDistance

    uniformForce = UniformForceField(default_value=(0.0, 0.0, 0.0), soft_min_value=(-1.0, -1.0, -1.0), soft_max_value=(1.0, 1.0, 1.0))
    ufr = uniformForce
    uniformForceX = uniformForce.uniformForceX
    ufx = uniformForceX
    uniformForceY = uniformForce.uniformForceY
    ufy = uniformForceY
    uniformForceZ = uniformForce.uniformForceZ
    ufz = uniformForceZ

    turbulenceType = TurbulenceTypeEnumField(default_value=0)
    trt = turbulenceType

    turbulenceInterpolation = TurbulenceInterpolationEnumField(default_value=0)
    tin = turbulenceInterpolation

    turbulence = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    tur = turbulence

    turbulenceFrequency = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    trf = turbulenceFrequency

    turbulenceSpeed = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    trs = turbulenceSpeed

    turbulenceOffset = TurbulenceOffsetField(default_value=(0.0, 0.0, 0.0), soft_min_value=(-1.0, -1.0, -1.0), soft_max_value=(1.0, 1.0, 1.0))
    tro = turbulenceOffset
    turbulenceOffsetX = turbulenceOffset.turbulenceOffsetX
    trx = turbulenceOffsetX
    turbulenceOffsetY = turbulenceOffset.turbulenceOffsetY
    try_ = turbulenceOffsetY
    turbulenceOffsetZ = turbulenceOffset.turbulenceOffsetZ
    trz = turbulenceOffsetZ

    random = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ran = random

    gravity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    grv = gravity

    momentum = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mmt = momentum

    surfaceCollide = BoolField(default_value=False)
    scl = surfaceCollide

    collideMethod = CollideMethodEnumField(default_value=0)
    clmp = collideMethod

    surfaceSnap = BoolField(default_value=False)
    ssn = surfaceSnap

    deflection = BoolField(default_value=False)
    def_ = deflection

    deflectionMin = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    dfm = deflectionMin

    deflectionMax = DoubleField(default_value=0.3, soft_min_value=0.0, soft_max_value=1.0)
    dfx = deflectionMax

    sunDirection = SunDirectionField(default_value=(0.0, 1.0, 0.0), soft_min_value=(-1.0, -1.0, -1.0), soft_max_value=(1.0, 1.0, 1.0))
    snd = sunDirection
    sunDirectionX = sunDirection.sunDirectionX
    sndx = sunDirectionX
    sunDirectionY = sunDirection.sunDirectionY
    sndy = sunDirectionY
    sunDirectionZ = sunDirection.sunDirectionZ
    sndz = sunDirectionZ

    twigsInCluster = LongField(default_value=1, soft_min_value=1, soft_max_value=8)
    tic = twigsInCluster

    twigDropout = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tdp = twigDropout

    twigAngle1 = DoubleField(default_value=90.0, soft_min_value=0.0, soft_max_value=180.0)
    ta1 = twigAngle1

    twigAngle2 = DoubleField(default_value=80.0, soft_min_value=0.0, soft_max_value=180.0)
    ta2 = twigAngle2

    twigTwist = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ttw = twigTwist

    twigLength = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=10.0)
    twl = twigLength

    twigStart = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    tst = twigStart

    numTwigClusters = DoubleField(default_value=4.0, soft_min_value=1.0, soft_max_value=100.0)
    ntc = numTwigClusters

    twigBaseWidth = DoubleField(default_value=0.4, soft_min_value=0.0, soft_max_value=1.0)
    twb = twigBaseWidth

    twigTipWidth = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    twt = twigTipWidth

    twigStiffness = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    tgs = twigStiffness

    branchAfterTwigs = BoolField(default_value=False)
    bat = branchAfterTwigs

    leavesInCluster = LongField(default_value=1, soft_min_value=1, soft_max_value=8)
    lic = leavesInCluster

    leafLocation = LeafLocationEnumField(default_value=0)
    llo = leafLocation

    leafDropout = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ldp = leafDropout

    leafAngle1 = DoubleField(default_value=75.0, soft_min_value=0.0, soft_max_value=180.0)
    ll1 = leafAngle1

    leafAngle2 = DoubleField(default_value=25.0, soft_min_value=0.0, soft_max_value=180.0)
    ll2 = leafAngle2

    leafTwist = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ltw = leafTwist

    leafBend = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    lbn = leafBend

    leafCurl = LeafCurlField(multi=True, default_value=(0.0, 0.0, 0.0))
    lcl = leafCurl

    leafTwirl = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    ltwl = leafTwirl

    leafFaceSun = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lfcs = leafFaceSun

    leafSegments = LongField(default_value=5, soft_min_value=1, soft_max_value=100)
    lsg = leafSegments

    leafStart = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    lst = leafStart

    numLeafClusters = DoubleField(default_value=3.0, soft_min_value=1.0, soft_max_value=100.0)
    nlc = numLeafClusters

    leafFlatness = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    lft = leafFlatness

    leafLength = DoubleField(default_value=0.3, soft_min_value=0.0, soft_max_value=0.0)
    lln = leafLength

    leafBaseWidth = DoubleField(default_value=0.15, soft_min_value=0.0, soft_max_value=1.0)
    leb = leafBaseWidth

    leafTipWidth = DoubleField(default_value=0.05, soft_min_value=0.0, soft_max_value=1.0)
    let = leafTipWidth

    leafSizeDecay = DoubleField(default_value=0.7, soft_min_value=0.0, soft_max_value=2.0)
    lsd = leafSizeDecay

    leafSizeRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lzr = leafSizeRand

    leafTranslucence = DoubleField(default_value=0.7, soft_min_value=0.0, soft_max_value=1.0)
    ltr = leafTranslucence

    leafSpecular = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lsp = leafSpecular

    terminalLeaf = BoolField(default_value=False)
    tml = terminalLeaf

    leafColor1 = LeafColor1Field(default_value=(0.20000000298023224, 0.6000000238418579, 0.30000001192092896))
    lc1 = leafColor1
    leafColor1R = leafColor1.leafColor1R
    lr1 = leafColor1R
    leafColor1G = leafColor1.leafColor1G
    lg1 = leafColor1G
    leafColor1B = leafColor1.leafColor1B
    lb1 = leafColor1B

    leafColor2 = LeafColor2Field(default_value=(0.4000000059604645, 0.6000000238418579, 0.30000001192092896))
    lc2 = leafColor2
    leafColor2R = leafColor2.leafColor2R
    lr2 = leafColor2R
    leafColor2G = leafColor2.leafColor2G
    lg2 = leafColor2G
    leafColor2B = leafColor2.leafColor2B
    lb2 = leafColor2B

    leafHueRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lhr = leafHueRand

    leafSatRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lsr = leafSatRand

    leafValRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lvr = leafValRand

    leafUseBranchTex = BoolField(default_value=True)
    lub = leafUseBranchTex

    leafImage = DataStringField()
    lim = leafImage

    leafStiffness = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    lfs = leafStiffness

    budSize = DoubleField(default_value=0.03, soft_min_value=0.0, soft_max_value=1.0)
    bds = budSize

    budColor = BudColorField(default_value=(0.4000000059604645, 0.800000011920929, 0.20000000298023224))
    bcr = budColor
    budColorR = budColor.budColorR
    bur = budColorR
    budColorG = budColor.budColorG
    bug = budColorG
    budColorB = budColor.budColorB
    bub = budColorB

    petalsInFlower = LongField(default_value=1, soft_min_value=0, soft_max_value=8)
    pif = petalsInFlower

    flowerLocation = FlowerLocationEnumField(default_value=0)
    flc = flowerLocation

    petalDropout = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    pdp = petalDropout

    flowerAngle1 = DoubleField(default_value=75.0, soft_min_value=0.0, soft_max_value=180.0)
    fw1 = flowerAngle1

    flowerAngle2 = DoubleField(default_value=25.0, soft_min_value=0.0, soft_max_value=180.0)
    fw2 = flowerAngle2

    flowerTwist = DoubleField(default_value=0.23, soft_min_value=-1.0, soft_max_value=1.0)
    ftw = flowerTwist

    petalBend = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    pbn = petalBend

    petalCurl = PetalCurlField(multi=True, default_value=(0.0, 0.0, 0.0))
    pcl = petalCurl

    petalTwirl = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    lpwl = petalTwirl

    flowerFaceSun = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    ffcs = flowerFaceSun

    petalSegments = LongField(default_value=5, soft_min_value=1, soft_max_value=100)
    psg = petalSegments

    flowerStart = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    fst = flowerStart

    numFlowers = DoubleField(default_value=10.0, soft_min_value=1.0, soft_max_value=100.0)
    nfl = numFlowers

    petalFlatness = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    pft = petalFlatness

    petalLength = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    pln = petalLength

    petalBaseWidth = DoubleField(default_value=0.05, soft_min_value=0.0, soft_max_value=1.0)
    ptb = petalBaseWidth

    petalTipWidth = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    ptt = petalTipWidth

    flowerSizeDecay = DoubleField(default_value=0.7, soft_min_value=0.0, soft_max_value=2.0)
    fsd = flowerSizeDecay

    flowerSizeRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fzr = flowerSizeRand

    flowerTranslucence = DoubleField(default_value=0.7, soft_min_value=0.0, soft_max_value=1.0)
    ftr = flowerTranslucence

    flowerSpecular = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fsp = flowerSpecular

    petalColor1 = PetalColor1Field(default_value=(0.800000011920929, 0.20000000298023224, 0.10000000149011612))
    pc1 = petalColor1
    petalColor1R = petalColor1.petalColor1R
    pr1 = petalColor1R
    petalColor1G = petalColor1.petalColor1G
    pg1 = petalColor1G
    petalColor1B = petalColor1.petalColor1B
    pb1 = petalColor1B

    petalColor2 = PetalColor2Field(default_value=(1.0, 1.0, 1.0))
    pc2 = petalColor2
    petalColor2R = petalColor2.petalColor2R
    pr2 = petalColor2R
    petalColor2G = petalColor2.petalColor2G
    pg2 = petalColor2G
    petalColor2B = petalColor2.petalColor2B
    pb2 = petalColor2B

    flowerHueRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fhr = flowerHueRand

    flowerSatRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fsr = flowerSatRand

    flowerValRand = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fvr = flowerValRand

    flowerUseBranchTex = BoolField(default_value=True)
    fub = flowerUseBranchTex

    flowerImage = DataStringField()
    fim = flowerImage

    flowerStiffness = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    fls = flowerStiffness

    simplifyMethod = SimplifyMethodEnumField(default_value=2)
    smp = simplifyMethod

    colorLengthMap = ColorLengthMapEnumField(default_value=0)
    clm = colorLengthMap

    transpLengthMap = TranspLengthMapEnumField(default_value=0)
    tlm = transpLengthMap

    incandLengthMap = IncandLengthMapEnumField(default_value=0)
    ilm = incandLengthMap

    widthLengthMap = WidthLengthMapEnumField(default_value=0)
    wlm = widthLengthMap

    splitLengthMap = SplitLengthMapEnumField(default_value=0)
    spl = splitLengthMap

    mapColor = BoolField(default_value=False)
    mcl = mapColor

    mapOpacity = BoolField(default_value=False)
    mop = mapOpacity

    mapDisplacement = BoolField(default_value=False)
    mds = mapDisplacement

    textureType = TextureTypeEnumField(default_value=0)
    txt = textureType

    mapMethod = MapMethodEnumField(default_value=2)
    mmd = mapMethod

    texColorScale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    tcs = texColorScale

    texColorOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tco = texColorOffset

    texOpacityScale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    tos = texOpacityScale

    texOpacityOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    too = texOpacityOffset

    displacementScale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    dsc = displacementScale

    displacementOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dof = displacementOffset

    bumpIntensity = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    bmi = bumpIntensity

    bumpBlur = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=2.0)
    bbl = bumpBlur

    luminanceIsDisplacement = BoolField(default_value=True)
    lid = luminanceIsDisplacement

    texColor1 = TexColor1Field(default_value=(1.0, 1.0, 1.0))
    tc1 = texColor1
    texColor1R = texColor1.texColor1R
    x1r = texColor1R
    texColor1G = texColor1.texColor1G
    x1g = texColor1G
    texColor1B = texColor1.texColor1B
    x1b = texColor1B

    texColor2 = TexColor2Field(default_value=(0.0, 0.0, 0.0))
    tc2 = texColor2
    texColor2R = texColor2.texColor2R
    x2r = texColor2R
    texColor2G = texColor2.texColor2G
    x2g = texColor2G
    texColor2B = texColor2.texColor2B
    x2b = texColor2B

    texAlpha1 = DoubleField(default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    al1 = texAlpha1

    texAlpha2 = DoubleField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    al2 = texAlpha2

    texUniformity = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    txu = texUniformity

    fringeRemoval = BoolField(default_value=True)
    frm = fringeRemoval

    repeatU = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    rpu = repeatU

    repeatV = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    rpv = repeatV

    offsetU = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ofu = offsetU

    offsetV = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ofv = offsetV

    blurMult = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    bmt = blurMult

    smear = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    smr = smear

    smearU = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    sru = smearU

    smearV = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    srv = smearV

    imageName = DataStringField()
    imn = imageName

    useFrameExtension = BoolField(default_value=False)
    ufe = useFrameExtension

    frameExtension = LongField(default_value=1)
    fe = frameExtension

    fractalRatio = DoubleField(default_value=0.7, soft_min_value=0.0, soft_max_value=1.0)
    fra = fractalRatio

    fractalAmplitude = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    fam = fractalAmplitude

    fractalThreshold = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fth = fractalThreshold

    multiStreaks = LongField(default_value=0, min_value=0, max_value=100, soft_max_value=20)
    mst = multiStreaks

    multiStreakSpread1 = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    ms1 = multiStreakSpread1

    multiStreakSpread2 = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    ms2 = multiStreakSpread2

    multiStreakDiffuseRand = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    msdr = multiStreakDiffuseRand

    multiStreakSpecularRand = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    mssr = multiStreakSpecularRand

    multiStreakLightAll = BoolField(default_value=False)
    msla = multiStreakLightAll

    singleSided = BoolField(default_value=False)
    snsd = singleSided

    tubeSections = LongField(default_value=6, min_value=3, max_value=100, soft_max_value=30)
    tbs = tubeSections

    subSegments = LongField(default_value=1, min_value=1, max_value=1000, soft_max_value=20)
    ssg = subSegments

    perPixelLighting = BoolField(default_value=False)
    ppl = perPixelLighting

    widthScale = WidthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    wsc = widthScale

    leafWidthScale = LeafWidthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    lws = leafWidthScale

    petalWidthScale = PetalWidthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    pws = petalWidthScale

    twigLengthScale = TwigLengthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    tls = twigLengthScale

    branchThorns = BoolField(default_value=False)
    bth = branchThorns

    twigThorns = BoolField(default_value=False)
    tth = twigThorns

    leafThorns = BoolField(default_value=False)
    lth = leafThorns

    flowerThorns = BoolField(default_value=False)
    flt = flowerThorns

    thornDensity = DoubleField(default_value=10.0, min_value=0.0, soft_max_value=100.0)
    nth = thornDensity

    thornLength = DoubleField(default_value=0.5, min_value=0.0, soft_max_value=2.0)
    tln = thornLength

    thornBaseWidth = DoubleField(default_value=0.05, min_value=0.0, soft_max_value=0.5)
    tbwd = thornBaseWidth

    thornTipWidth = DoubleField(default_value=0.01, min_value=0.0, soft_max_value=0.5)
    ttwd = thornTipWidth

    thornElevation = DoubleField(default_value=0.6, soft_min_value=0.0, soft_max_value=2.0)
    tel = thornElevation

    thornSpecular = DoubleField(default_value=0.4, soft_min_value=0.0, soft_max_value=1.0)
    tsp = thornSpecular

    thornBaseColor = ThornBaseColorField(default_value=(0.5, 0.5, 0.5))
    tbc = thornBaseColor
    thornBaseColorR = thornBaseColor.thornBaseColorR
    tbcr = thornBaseColorR
    thornBaseColorG = thornBaseColor.thornBaseColorG
    tbcg = thornBaseColorG
    thornBaseColorB = thornBaseColor.thornBaseColorB
    tbcb = thornBaseColorB

    thornTipColor = ThornTipColorField(default_value=(0.5, 0.5, 0.5))
    ttc = thornTipColor
    thornTipColorR = thornTipColor.thornTipColorR
    ttcr = thornTipColorR
    thornTipColorG = thornTipColor.thornTipColorG
    ttcg = thornTipColorG
    thornTipColorB = thornTipColor.thornTipColorB
    ttcb = thornTipColorB

    environment = EnvironmentField(multi=True)
    env = environment

    environment_ColorR = FloatField()
    envcr = environment_ColorR

    environment_ColorG = FloatField()
    envcg = environment_ColorG

    environment_ColorB = FloatField()
    envcb = environment_ColorB

    reflectionRolloff = ReflectionRolloffField(multi=True, default_value=(0.0, 0.0, 0.0))
    rro = reflectionRolloff

    branchReflectivity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    brf = branchReflectivity

    leafReflectivity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    lrf = leafReflectivity

    flowerReflectivity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    frf = flowerReflectivity

    forwardTwist = BoolField(default_value=False)
    fwt = forwardTwist

    leafForwardTwist = BoolField(default_value=False)
    lfwt = leafForwardTwist

    petalForwardTwist = BoolField(default_value=False)
    lpwt = petalForwardTwist

    endCaps = BoolField(default_value=False)
    edc = endCaps

    hardEdges = BoolField(default_value=False)
    hde = hardEdges

    surfaceSampleDensity = LongField(default_value=50, min_value=1, soft_max_value=200)
    susd = surfaceSampleDensity

    occupyAttraction = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    ocat = occupyAttraction

    attractRadiusScale = DoubleField(default_value=4.0, soft_min_value=0.0, soft_max_value=10.0)
    ocar = attractRadiusScale

    attractRadiusOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ocao = attractRadiusOffset

    occupyRadiusScale = DoubleField(default_value=1.5, soft_min_value=0.0, soft_max_value=10.0)
    ocrs = occupyRadiusScale

    occupyRadiusOffset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ocro = occupyRadiusOffset

    occupyBranchTermination = BoolField(default_value=False)
    ocbt = occupyBranchTermination
