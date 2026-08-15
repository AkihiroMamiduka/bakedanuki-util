# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.motion_trail_shape import (
    ActiveKeyframeColorField,
    BeadColorField,
    ColorSetField,
    CompInstObjGroupsField,
    ComponentTagsField,
    ControlPointsField,
    ExtraKeyframeColorField,
    ExtraTrailColorField,
    FastTrailColorField,
    FrameMarkerColorField,
    KeyframeColorField,
    LocalPositionField,
    SlowTrailColorField,
    TangentPointsField,
    TrailColorField,
    UvPivotField,
    UvSetField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.double_array import DataDoubleArrayField
from .....attr.define.std.dt.point_array import DataPointArrayField
from .....attr.define.std.dt.string import DataStringField


class TrailDrawModeEnumPlugOperator(
    EnumPlugOperator["TrailDrawModeEnumAttrOperator"]
):
    __slots__ = ()

    CONSTANT = 0
    ALTERNATING_FRAMES = 1
    PAST_SLASH_FUTURE = 2
    VELOCITY = 3


class TrailDrawModeEnumAttrOperator(
    EnumAttrOperator[TrailDrawModeEnumPlugOperator]
):
    __slots__ = ()

    CONSTANT = 0
    ALTERNATING_FRAMES = 1
    PAST_SLASH_FUTURE = 2
    VELOCITY = 3

    NAME_MAP = {
        CONSTANT: "Constant",
        ALTERNATING_FRAMES: "Alternating Frames",
        PAST_SLASH_FUTURE: "Past / Future",
        VELOCITY: "Velocity",
    }


class TrailDrawModeEnumField(
    EnumField[TrailDrawModeEnumAttrOperator, TrailDrawModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrailDrawModeEnumAttrOperator
    PLUG_CLS = TrailDrawModeEnumPlugOperator


class TrailPathModeEnumPlugOperator(
    EnumPlugOperator["TrailPathModeEnumAttrOperator"]
):
    __slots__ = ()

    BEFORE_CURRENT_FRAME = 0
    ALL_FRAMES = 1
    AFTER_CURRENT_FRAME = 2


class TrailPathModeEnumAttrOperator(
    EnumAttrOperator[TrailPathModeEnumPlugOperator]
):
    __slots__ = ()

    BEFORE_CURRENT_FRAME = 0
    ALL_FRAMES = 1
    AFTER_CURRENT_FRAME = 2

    NAME_MAP = {
        BEFORE_CURRENT_FRAME: "Before Current Frame",
        ALL_FRAMES: "All Frames",
        AFTER_CURRENT_FRAME: "After Current Frame",
    }


class TrailPathModeEnumField(
    EnumField[TrailPathModeEnumAttrOperator, TrailPathModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrailPathModeEnumAttrOperator
    PLUG_CLS = TrailPathModeEnumPlugOperator


class GeneratedMotionTrailShape(Shape):
    __slots__ = ()

    NODE_TYPE = "motionTrailShape"

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    tweak = BoolField(default_value=False)
    tw = tweak

    relativeTweak = BoolField(default_value=True)
    rtw = relativeTweak

    controlPoints = ControlPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    cp = controlPoints

    weights = DoubleField(multi=True, default_value=1.0)
    wt = weights

    tweakLocation = TypedField(readable=False)
    twl = tweakLocation

    blindDataNodes = MessageField(multi=True, readable=False)
    bn = blindDataNodes

    uvPivot = UvPivotField(default_value=(0.0, 0.0))
    pv = uvPivot
    uvPivotX = uvPivot.uvPivotX
    pvx = uvPivotX
    uvPivotY = uvPivot.uvPivotY
    pvy = uvPivotY

    uvSet = UvSetField(multi=True)
    uvst = uvSet

    currentUVSet = DataStringField()
    cuvs = currentUVSet

    displayImmediate = BoolField(default_value=False)
    di = displayImmediate

    displayColors = BoolField(default_value=False)
    dcol = displayColors

    displayColorChannel = DataStringField()
    dcc = displayColorChannel

    currentColorSet = DataStringField()
    ccls = currentColorSet

    colorSet = ColorSetField(multi=True)
    clst = colorSet

    points = DataPointArrayField()
    pts = points

    frames = TypedField()
    f = frames

    showFrames = BoolField(default_value=False)
    sf = showFrames

    transformToMove = MessageField()
    tr = transformToMove

    localPosition = LocalPositionField(default_value=(0.0, 0.0, 0.0))
    lp = localPosition
    localPositionX = localPosition.localPositionX
    lpx = localPositionX
    localPositionY = localPosition.localPositionY
    lpy = localPositionY
    localPositionZ = localPosition.localPositionZ
    lpz = localPositionZ

    keyframeTimes = DataDoubleArrayField()
    kt = keyframeTimes

    keyframeFlags = TypedField()
    fk = keyframeFlags

    extraKeyframeTimes = DataDoubleArrayField()
    ekt = extraKeyframeTimes

    trailThickness = LongField(default_value=1, min_value=1, max_value=20)
    tt = trailThickness

    fadeInoutFrames = LongField(
        default_value=0, min_value=0, soft_max_value=10
    )
    fi = fadeInoutFrames

    showKeyframes = BoolField(default_value=True)
    skf = showKeyframes

    keyframeSize = LongField(default_value=1, min_value=0, max_value=20)
    ks = keyframeSize

    preFrame = LongField(default_value=0, min_value=0, soft_max_value=10)
    bf = preFrame

    postFrame = LongField(default_value=0, min_value=0, soft_max_value=10)
    af = postFrame

    pinned = BoolField(default_value=True)
    pd = pinned

    trailColor = TrailColorField(
        default_value=(0.49000000953674316, 0.09799999743700027, 0.125)
    )
    tc = trailColor
    trailColorR = trailColor.trailColorR
    tcr = trailColorR
    trailColorG = trailColor.trailColorG
    tcg = trailColorG
    trailColorB = trailColor.trailColorB
    tcb = trailColorB

    extraTrailColor = ExtraTrailColorField(
        default_value=(0.125, 0.09799999743700027, 0.49000000953674316)
    )
    etc = extraTrailColor
    extraTrailColorR = extraTrailColor.extraTrailColorR
    etcr = extraTrailColorR
    extraTrailColorG = extraTrailColor.extraTrailColorG
    etcg = extraTrailColorG
    extraTrailColorB = extraTrailColor.extraTrailColorB
    etcb = extraTrailColorB

    keyframeColor = KeyframeColorField(default_value=(1.0, 1.0, 1.0))
    kc = keyframeColor
    keyframeColorR = keyframeColor.keyframeColorR
    kcr = keyframeColorR
    keyframeColorG = keyframeColor.keyframeColorG
    kcg = keyframeColorG
    keyframeColorB = keyframeColor.keyframeColorB
    kcb = keyframeColorB

    activeKeyframeColor = ActiveKeyframeColorField(
        default_value=(1.0, 1.0, 0.0)
    )
    ak = activeKeyframeColor
    activeKeyframeColorR = activeKeyframeColor.activeKeyframeColorR
    akr = activeKeyframeColorR
    activeKeyframeColorG = activeKeyframeColor.activeKeyframeColorG
    akg = activeKeyframeColorG
    activeKeyframeColorB = activeKeyframeColor.activeKeyframeColorB
    akb = activeKeyframeColorB

    beadColor = BeadColorField(default_value=(1.0, 0.0, 1.0))
    bc = beadColor
    beadColorR = beadColor.beadColorR
    bcr = beadColorR
    beadColorG = beadColor.beadColorG
    bcg = beadColorG
    beadColorB = beadColor.beadColorB
    bcb = beadColorB

    slowTrailColor = SlowTrailColorField(
        default_value=(
            0.23000000417232513,
            0.07100000232458115,
            0.40400001406669617,
        )
    )
    stc = slowTrailColor
    slowTrailColorR = slowTrailColor.slowTrailColorR
    str = slowTrailColorR
    slowTrailColorG = slowTrailColor.slowTrailColorG
    stg = slowTrailColorG
    slowTrailColorB = slowTrailColor.slowTrailColorB
    stb = slowTrailColorB

    fastTrailColor = FastTrailColorField(
        default_value=(0.6119999885559082, 0.0, 0.0)
    )
    ftc = fastTrailColor
    fastTrailColorR = fastTrailColor.fastTrailColorR
    ftr = fastTrailColorR
    fastTrailColorG = fastTrailColor.fastTrailColorG
    ftg = fastTrailColorG
    fastTrailColorB = fastTrailColor.fastTrailColorB
    ftb = fastTrailColorB

    startTime = TimeField(default_value=0.0)
    s = startTime

    increment = TimeField(default_value=1.0)
    b = increment

    tangentPoints = TangentPointsField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    tps = tangentPoints

    showInTangent = BoolField(default_value=False)
    sit = showInTangent

    showOutTangent = BoolField(default_value=False)
    sot = showOutTangent

    showInBead = BoolField(default_value=False)
    sib = showInBead

    showOutBead = BoolField(default_value=False)
    sob = showOutBead

    modifyKeys = BoolField(default_value=False)
    mok = modifyKeys

    xrayDraw = BoolField(default_value=True)
    xd = xrayDraw

    frameMarkerColor = FrameMarkerColorField(
        default_value=(
            0.1550000011920929,
            0.5529999732971191,
            0.11100000143051147,
        )
    )
    fc = frameMarkerColor
    frameMarkerColorR = frameMarkerColor.frameMarkerColorR
    fcr = frameMarkerColorR
    frameMarkerColorG = frameMarkerColor.frameMarkerColorG
    fcg = frameMarkerColorG
    frameMarkerColorB = frameMarkerColor.frameMarkerColorB
    fcb = frameMarkerColorB

    showFrameMarkers = BoolField(default_value=False)
    sfm = showFrameMarkers

    showFrameMarkerFrames = BoolField(default_value=False)
    sff = showFrameMarkerFrames

    frameMarkerSize = LongField(default_value=1, min_value=0, max_value=20)
    fs = frameMarkerSize

    showExtraKeys = BoolField(default_value=False)
    sek = showExtraKeys

    extraKeyframeColor = ExtraKeyframeColorField(
        default_value=(
            0.45100000500679016,
            0.45100000500679016,
            0.45100000500679016,
        )
    )
    ec = extraKeyframeColor
    extraKeyframeColorR = extraKeyframeColor.extraKeyframeColorR
    ecr = extraKeyframeColorR
    extraKeyframeColorG = extraKeyframeColor.extraKeyframeColorG
    ecg = extraKeyframeColorG
    extraKeyframeColorB = extraKeyframeColor.extraKeyframeColorB
    ecb = extraKeyframeColorB

    trailDrawMode = TrailDrawModeEnumField(default_value=2)
    tdm = trailDrawMode

    trailPathMode = TrailPathModeEnumField(default_value=1)
    tpm = trailPathMode
