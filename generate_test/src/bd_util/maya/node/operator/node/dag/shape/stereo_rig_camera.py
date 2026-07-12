# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.stereo_rig_camera import (
    AiLensShiftField,
    AiLensTiltAngleField,
    AiLookAtField,
    AiPositionField,
    AiRayDirectionField,
    AiRayOriginField,
    AiScreenWindowMaxField,
    AiScreenWindowMinField,
    AiShutterCurveField,
    AiUpField,
    AiUvRemapField,
    BackgroundColorField,
    BoundingBoxField,
    CameraApertureField,
    CenterField,
    DisplayGateMaskColorField,
    DrawOverrideField,
    FilmOffsetField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    ObjectColorRGBField,
    OutlinerColorField,
    PanField,
    PostProjectionField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    SafeVolumeColorField,
    ShakeField,
    TumblePivotField,
    WireColorRGBField,
    ZeroParallaxColorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2

    NAME_MAP = {
        FLAT: "Flat",
        USE_TEMPLATE: "Use Template",
        GROUP_BY_NODE: "Group By Node",
    }


class ViewModeEnumField(
    EnumField[ViewModeEnumAttrOperator, ViewModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewModeEnumAttrOperator
    PLUG_CLS = ViewModeEnumPlugOperator


class UiTreatmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000

    NAME_MAP = {
        STANDARD: "Standard",
        SHADER: "Shader",
        CUSTOM: "Custom",
    }


class UiTreatmentEnumField(
    EnumField[UiTreatmentEnumAttrOperator, UiTreatmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UiTreatmentEnumAttrOperator
    PLUG_CLS = UiTreatmentEnumPlugOperator


class UseObjectColorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2

    NAME_MAP = {
        DEFAULT: "Default",
        INDEXED: "Indexed",
        RGB: "RGB",
    }


class UseObjectColorEnumField(
    EnumField[UseObjectColorEnumAttrOperator, UseObjectColorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseObjectColorEnumAttrOperator
    PLUG_CLS = UseObjectColorEnumPlugOperator


class GhostingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5

    NAME_MAP = {
        PRE_AND_POST_FRAMES: "Pre And Post Frames",
        PRE_FRAMES: "Pre Frames",
        POST_FRAMES: "Post Frames",
        CUSTOM_FRAMES: "Custom Frames",
        PRE_AND_POST_KEYFRAMES: "Pre And Post Keyframes",
        ALL_KEYFRAMES: "All Keyframes",
    }


class GhostingModeEnumField(
    EnumField[GhostingModeEnumAttrOperator, GhostingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostingModeEnumAttrOperator
    PLUG_CLS = GhostingModeEnumPlugOperator


class FilmFitEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FILL = 0
    HORIZONTAL = 1
    VERTICAL = 2
    OVERSCAN = 3


class FilmFitEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FILL = 0
    HORIZONTAL = 1
    VERTICAL = 2
    OVERSCAN = 3

    NAME_MAP = {
        FILL: "Fill",
        HORIZONTAL: "Horizontal",
        VERTICAL: "Vertical",
        OVERSCAN: "Overscan",
    }


class FilmFitEnumField(
    EnumField[FilmFitEnumAttrOperator, FilmFitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilmFitEnumAttrOperator
    PLUG_CLS = FilmFitEnumPlugOperator


class DepthTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST_VISIBLE_DEPTH = 0
    FURTHEST_VISIBLE_DEPTH = 1


class DepthTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST_VISIBLE_DEPTH = 0
    FURTHEST_VISIBLE_DEPTH = 1

    NAME_MAP = {
        CLOSEST_VISIBLE_DEPTH: "Closest Visible Depth",
        FURTHEST_VISIBLE_DEPTH: "Furthest Visible Depth",
    }


class DepthTypeEnumField(
    EnumField[DepthTypeEnumAttrOperator, DepthTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DepthTypeEnumAttrOperator
    PLUG_CLS = DepthTypeEnumPlugOperator


class AiHandednessEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RIGHT = 0
    LEFT = 1


class AiHandednessEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RIGHT = 0
    LEFT = 1

    NAME_MAP = {
        RIGHT: "right",
        LEFT: "left",
    }


class AiHandednessEnumField(
    EnumField[AiHandednessEnumAttrOperator, AiHandednessEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiHandednessEnumAttrOperator
    PLUG_CLS = AiHandednessEnumPlugOperator


class AiShutterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOX = 0
    TRIANGLE = 1
    CURVE = 2


class AiShutterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOX = 0
    TRIANGLE = 1
    CURVE = 2

    NAME_MAP = {
        BOX: "box",
        TRIANGLE: "triangle",
        CURVE: "curve",
    }


class AiShutterTypeEnumField(
    EnumField[AiShutterTypeEnumAttrOperator, AiShutterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiShutterTypeEnumAttrOperator
    PLUG_CLS = AiShutterTypeEnumPlugOperator


class AiRollingShutterEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4


class AiRollingShutterEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4

    NAME_MAP = {
        OFF: "off",
        TOP: "top",
        BOTTOM: "bottom",
        LEFT: "left",
        RIGHT: "right",
    }


class AiRollingShutterEnumField(
    EnumField[AiRollingShutterEnumAttrOperator, AiRollingShutterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiRollingShutterEnumAttrOperator
    PLUG_CLS = AiRollingShutterEnumPlugOperator


class AiModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SIDE_BY_SIDE = 0
    OVER_UNDER = 1
    LEFT_EYE = 2
    RIGHT_EYE = 3


class AiModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SIDE_BY_SIDE = 0
    OVER_UNDER = 1
    LEFT_EYE = 2
    RIGHT_EYE = 3

    NAME_MAP = {
        SIDE_BY_SIDE: "side_by_side",
        OVER_UNDER: "over_under",
        LEFT_EYE: "left_eye",
        RIGHT_EYE: "right_eye",
    }


class AiModeEnumField(
    EnumField[AiModeEnumAttrOperator, AiModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiModeEnumAttrOperator
    PLUG_CLS = AiModeEnumPlugOperator


class AiProjectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LATLONG = 0
    CUBEMAP_6X1 = 1
    CUBEMAP_3X2 = 2


class AiProjectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LATLONG = 0
    CUBEMAP_6X1 = 1
    CUBEMAP_3X2 = 2

    NAME_MAP = {
        LATLONG: "latlong",
        CUBEMAP_6X1: "cubemap_6x1",
        CUBEMAP_3X2: "cubemap_3x2",
    }


class AiProjectionEnumField(
    EnumField[AiProjectionEnumAttrOperator, AiProjectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiProjectionEnumAttrOperator
    PLUG_CLS = AiProjectionEnumPlugOperator


class AiTopMergeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    COSINE = 1
    SHADER = 2


class AiTopMergeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    COSINE = 1
    SHADER = 2

    NAME_MAP = {
        NONE: "none",
        COSINE: "cosine",
        SHADER: "shader",
    }


class AiTopMergeModeEnumField(
    EnumField[AiTopMergeModeEnumAttrOperator, AiTopMergeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiTopMergeModeEnumAttrOperator
    PLUG_CLS = AiTopMergeModeEnumPlugOperator


class AiBottomMergeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    COSINE = 1
    SHADER = 2


class AiBottomMergeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    COSINE = 1
    SHADER = 2

    NAME_MAP = {
        NONE: "none",
        COSINE: "cosine",
        SHADER: "shader",
    }


class AiBottomMergeModeEnumField(
    EnumField[AiBottomMergeModeEnumAttrOperator, AiBottomMergeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiBottomMergeModeEnumAttrOperator
    PLUG_CLS = AiBottomMergeModeEnumPlugOperator


class AiRadialDistortionTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CUBIC = 0
    CUBIC_INVERSE = 1


class AiRadialDistortionTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CUBIC = 0
    CUBIC_INVERSE = 1

    NAME_MAP = {
        CUBIC: "cubic",
        CUBIC_INVERSE: "cubic_inverse",
    }


class AiRadialDistortionTypeEnumField(
    EnumField[AiRadialDistortionTypeEnumAttrOperator, AiRadialDistortionTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiRadialDistortionTypeEnumAttrOperator
    PLUG_CLS = AiRadialDistortionTypeEnumPlugOperator


class MotionBlurOverrideEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    USE_GLOBAL_SETTINGS = 0
    ON = 1
    OFF = 2


class MotionBlurOverrideEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    USE_GLOBAL_SETTINGS = 0
    ON = 1
    OFF = 2

    NAME_MAP = {
        USE_GLOBAL_SETTINGS: "Use Global Settings",
        ON: "On",
        OFF: "Off",
    }


class MotionBlurOverrideEnumField(
    EnumField[MotionBlurOverrideEnumAttrOperator, MotionBlurOverrideEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurOverrideEnumAttrOperator
    PLUG_CLS = MotionBlurOverrideEnumPlugOperator


class StereoEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    CONVERGED = 1
    OFF_MINUS_AXIS = 2
    PARALLEL = 3


class StereoEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    CONVERGED = 1
    OFF_MINUS_AXIS = 2
    PARALLEL = 3

    NAME_MAP = {
        OFF: "Off",
        CONVERGED: "Converged",
        OFF_MINUS_AXIS: "Off-axis",
        PARALLEL: "Parallel",
    }


class StereoEnumField(
    EnumField[StereoEnumAttrOperator, StereoEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StereoEnumAttrOperator
    PLUG_CLS = StereoEnumPlugOperator


class DisplayNearClipEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LEFT = 1
    RIGHT = 2
    LEFTRIGHT = 3
    CENTER = 4
    ALL = 5


class DisplayNearClipEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LEFT = 1
    RIGHT = 2
    LEFTRIGHT = 3
    CENTER = 4
    ALL = 5

    NAME_MAP = {
        NONE: "None",
        LEFT: "Left",
        RIGHT: "Right",
        LEFTRIGHT: "LeftRight",
        CENTER: "Center",
        ALL: "All",
    }


class DisplayNearClipEnumField(
    EnumField[DisplayNearClipEnumAttrOperator, DisplayNearClipEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayNearClipEnumAttrOperator
    PLUG_CLS = DisplayNearClipEnumPlugOperator


class DisplayFarClipEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LEFT = 1
    RIGHT = 2
    LEFTRIGHT = 3
    CENTER = 4
    ALL = 5


class DisplayFarClipEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LEFT = 1
    RIGHT = 2
    LEFTRIGHT = 3
    CENTER = 4
    ALL = 5

    NAME_MAP = {
        NONE: "None",
        LEFT: "Left",
        RIGHT: "Right",
        LEFTRIGHT: "LeftRight",
        CENTER: "Center",
        ALL: "All",
    }


class DisplayFarClipEnumField(
    EnumField[DisplayFarClipEnumAttrOperator, DisplayFarClipEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayFarClipEnumAttrOperator
    PLUG_CLS = DisplayFarClipEnumPlugOperator


class DisplayFrustumEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LEFT = 1
    RIGHT = 2
    LEFTRIGHT = 3
    CENTER = 4
    ALL = 5


class DisplayFrustumEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LEFT = 1
    RIGHT = 2
    LEFTRIGHT = 3
    CENTER = 4
    ALL = 5

    NAME_MAP = {
        NONE: "None",
        LEFT: "Left",
        RIGHT: "Right",
        LEFTRIGHT: "LeftRight",
        CENTER: "Center",
        ALL: "All",
    }


class DisplayFrustumEnumField(
    EnumField[DisplayFrustumEnumAttrOperator, DisplayFrustumEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayFrustumEnumAttrOperator
    PLUG_CLS = DisplayFrustumEnumPlugOperator


class StereoRigCamera(Shape):
    __slots__ = ()

    NODE_TYPE = "stereoRigCamera"

    hyperLayout = MessageField()
    hl = hyperLayout

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    blackBox = BoolField(default_value=False)
    bbx = blackBox

    borderConnections = MessageField(multi=True)
    boc = borderConnections

    isHierarchicalConnection = BoolField(multi=True, default_value=False)
    ish = isHierarchicalConnection

    publishedNodeInfo = PublishedNodeInfoField(multi=True)
    pni = publishedNodeInfo

    rmbCommand = DataStringField()
    rmc = rmbCommand

    templateName = DataStringField()
    tna = templateName

    templatePath = DataStringField()
    tpt = templatePath

    viewName = DataStringField()
    vwn = viewName

    iconName = DataStringField()
    icn = iconName

    viewMode = ViewModeEnumField(default_value=2)
    vwm = viewMode

    templateVersion = LongField(default_value=0)
    tpv = templateVersion

    uiTreatment = UiTreatmentEnumField(default_value=0)
    uit = uiTreatment

    customTreatment = DataStringField()
    ctrt = customTreatment

    creator = DataStringField()
    ctor = creator

    creationDate = DataStringField()
    cdat = creationDate

    containerType = DataStringField()
    ctyp = containerType

    boundingBox = BoundingBoxField(writable=False)
    bb = boundingBox
    boundingBoxMin = boundingBox.boundingBoxMin
    bbmn = boundingBoxMin
    boundingBoxMax = boundingBox.boundingBoxMax
    bbmx = boundingBoxMax
    boundingBoxSize = boundingBox.boundingBoxSize
    bbsi = boundingBoxSize

    center = CenterField(default_value=(0.0, 0.0, 0.0), writable=False)
    c = center
    boundingBoxCenterX = center.boundingBoxCenterX
    bcx = boundingBoxCenterX
    boundingBoxCenterY = center.boundingBoxCenterY
    bcy = boundingBoxCenterY
    boundingBoxCenterZ = center.boundingBoxCenterZ
    bcz = boundingBoxCenterZ

    matrix = DataMatrixField(writable=False)
    m = matrix

    inverseMatrix = DataMatrixField(writable=False)
    im = inverseMatrix

    worldMatrix = DataMatrixField(multi=True, writable=False)
    wm = worldMatrix

    worldInverseMatrix = DataMatrixField(multi=True, writable=False)
    wim = worldInverseMatrix

    parentMatrix = DataMatrixField(multi=True, writable=False)
    pm = parentMatrix

    parentInverseMatrix = DataMatrixField(multi=True, writable=False)
    pim = parentInverseMatrix

    visibility = BoolField(default_value=True)
    v = visibility

    intermediateObject = BoolField(default_value=False)
    io = intermediateObject

    template = BoolField(default_value=False)
    tmp = template

    instObjGroups = InstObjGroupsField(multi=True)
    iog = instObjGroups

    objectColorRGB = ObjectColorRGBField(default_value=(0.0, 0.0, 0.0))
    obcc = objectColorRGB
    objectColorR = objectColorRGB.objectColorR
    obcr = objectColorR
    objectColorG = objectColorRGB.objectColorG
    obcg = objectColorG
    objectColorB = objectColorRGB.objectColorB
    obcb = objectColorB

    wireColorRGB = WireColorRGBField(default_value=(0.0, 0.0, 0.0))
    wfcc = wireColorRGB
    wireColorR = wireColorRGB.wireColorR
    wfcr = wireColorR
    wireColorG = wireColorRGB.wireColorG
    wfcg = wireColorG
    wireColorB = wireColorRGB.wireColorB
    wfcb = wireColorB

    useObjectColor = UseObjectColorEnumField(default_value=0)
    uoc = useObjectColor

    objectColor = ShortField(default_value=0, min_value=0, max_value=7)
    oc = objectColor

    drawOverride = DrawOverrideField()
    do = drawOverride
    overrideDisplayType = drawOverride.overrideDisplayType
    ovdt = overrideDisplayType
    overrideLevelOfDetail = drawOverride.overrideLevelOfDetail
    ovlod = overrideLevelOfDetail
    overrideShading = drawOverride.overrideShading
    ovs = overrideShading
    overrideTexturing = drawOverride.overrideTexturing
    ovt = overrideTexturing
    overridePlayback = drawOverride.overridePlayback
    ovp = overridePlayback
    overrideEnabled = drawOverride.overrideEnabled
    ove = overrideEnabled
    overrideVisibility = drawOverride.overrideVisibility
    ovv = overrideVisibility
    hideOnPlayback = drawOverride.hideOnPlayback
    hpb = hideOnPlayback
    overrideRGBColors = drawOverride.overrideRGBColors
    ovrgbf = overrideRGBColors
    overrideColor = drawOverride.overrideColor
    ovc = overrideColor
    overrideColorRGB = drawOverride.overrideColorRGB
    ovrgb = overrideColorRGB
    overrideColorA = drawOverride.overrideColorA
    ovca = overrideColorA

    lodVisibility = BoolField(default_value=True)
    lodv = lodVisibility

    selectionChildHighlighting = BoolField(default_value=True)
    sech = selectionChildHighlighting

    renderInfo = RenderInfoField(default_value=(0.0, 1.0, 0.0))
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    layerRenderable = renderInfo.layerRenderable
    rndr = layerRenderable
    layerOverrideColor = renderInfo.layerOverrideColor
    lovc = layerOverrideColor

    renderLayerInfo = RenderLayerInfoField(multi=True, default_value=(0.0, 1.0, 0.0))
    rlio = renderLayerInfo

    ghosting = BoolField(default_value=False)
    gh = ghosting

    ghostingMode = GhostingModeEnumField(default_value=0)
    gm = ghostingMode

    ghostCustomSteps = GhostCustomStepsField(default_value=(3.0, 3.0, 1.0))
    gcs = ghostCustomSteps
    ghostPreFrames = ghostCustomSteps.ghostPreFrames
    gprf = ghostPreFrames
    ghostPostFrames = ghostCustomSteps.ghostPostFrames
    gpof = ghostPostFrames
    ghostsStep = ghostCustomSteps.ghostsStep
    gstp = ghostsStep

    ghostFrames = TypedField()
    gf = ghostFrames

    ghostOpacityRange = GhostOpacityRangeField(default_value=(0.15000000596046448, 0.5), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(default_value=(0.44699999690055847, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(default_value=(0.878000020980835, 0.6779999732971191, 0.6629999876022339), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gac = ghostColorPost
    ghostColorPostR = ghostColorPost.ghostColorPostR
    gar = ghostColorPostR
    ghostColorPostG = ghostColorPost.ghostColorPostG
    gag = ghostColorPostG
    ghostColorPostB = ghostColorPost.ghostColorPostB
    gab = ghostColorPostB

    ghostDriver = MessageField()
    gdr = ghostDriver

    ghostUseDriver = BoolField(default_value=False)
    gud = ghostUseDriver

    hiddenInOutliner = BoolField(default_value=False)
    hio = hiddenInOutliner

    useOutlinerColor = BoolField(default_value=False)
    uocol = useOutlinerColor

    outlinerColor = OutlinerColorField(default_value=(0.0, 0.0, 0.0))
    oclr = outlinerColor
    outlinerColorR = outlinerColor.outlinerColorR
    oclrr = outlinerColorR
    outlinerColorG = outlinerColor.outlinerColorG
    oclrg = outlinerColorG
    outlinerColorB = outlinerColor.outlinerColorB
    oclrb = outlinerColorB

    renderable = BoolField(default_value=True)
    rnd = renderable

    cameraAperture = CameraApertureField(default_value=(1.4173200000000001, 0.94488), min_value=(3.9370000000000004e-05, 3.9370000000000004e-05), max_value=(1200.0, 1200.0), soft_min_value=(0.1, 0.1), soft_max_value=(10.0, 10.0))
    cap = cameraAperture
    horizontalFilmAperture = cameraAperture.horizontalFilmAperture
    hfa = horizontalFilmAperture
    verticalFilmAperture = cameraAperture.verticalFilmAperture
    vfa = verticalFilmAperture

    shakeOverscan = DoubleField(default_value=1.0, min_value=1e-10)
    sos = shakeOverscan

    shakeOverscanEnabled = BoolField(default_value=False)
    soe = shakeOverscanEnabled

    filmOffset = FilmOffsetField(default_value=(0.0, 0.0))
    fio = filmOffset
    horizontalFilmOffset = filmOffset.horizontalFilmOffset
    hfo = horizontalFilmOffset
    verticalFilmOffset = filmOffset.verticalFilmOffset
    vfo = verticalFilmOffset

    shakeEnabled = BoolField(default_value=False)
    se = shakeEnabled

    shake = ShakeField(default_value=(0.0, 0.0))
    shk = shake
    horizontalShake = shake.horizontalShake
    hs = horizontalShake
    verticalShake = shake.verticalShake
    vs = verticalShake

    stereoHorizontalImageTranslateEnabled = BoolField(default_value=False)
    hte = stereoHorizontalImageTranslateEnabled

    stereoHorizontalImageTranslate = DoubleField(default_value=0.0)
    hit = stereoHorizontalImageTranslate

    postProjection = PostProjectionField()
    ppj = postProjection
    preScale = postProjection.preScale
    psc = preScale
    filmTranslate = postProjection.filmTranslate
    ct = filmTranslate
    filmRollControl = postProjection.filmRollControl
    frc = filmRollControl
    postScale = postProjection.postScale
    ptsc = postScale

    filmFit = FilmFitEnumField(default_value=1)
    ff = filmFit

    filmFitOffset = DoubleField(default_value=0.0)
    ffo = filmFitOffset

    overscan = DoubleField(default_value=1.0, min_value=1e-10)
    ovr = overscan

    panZoomEnabled = BoolField(default_value=False)
    pze = panZoomEnabled

    renderPanZoom = BoolField(default_value=False)
    rpz = renderPanZoom

    pan = PanField(default_value=(0.0, 0.0))
    pn = pan
    horizontalPan = pan.horizontalPan
    hpn = horizontalPan
    verticalPan = pan.verticalPan
    vpn = verticalPan

    zoom = DoubleField(default_value=1.0, min_value=1e-10)
    zom = zoom

    focalLength = DoubleField(default_value=35.0, min_value=0.5, max_value=100000.0, soft_min_value=2.5, soft_max_value=3500.0)
    fl = focalLength

    lensSqueezeRatio = DoubleField(default_value=1.0, min_value=1e-10)
    lsr = lensSqueezeRatio

    cameraScale = DoubleField(default_value=1.0, min_value=1e-10)
    cs = cameraScale

    triggerUpdate = DoubleField(default_value=0.0)
    tu = triggerUpdate

    nearClipPlane = DoubleLinearField(default_value=0.1, min_value=0.001)
    ncp = nearClipPlane

    farClipPlane = DoubleLinearField(default_value=10000.0, min_value=0.001)
    fcp = farClipPlane

    fStop = DoubleField(default_value=5.6, min_value=1.0, max_value=64.0)
    fs = fStop

    focusDistance = DoubleLinearField(default_value=5.0, min_value=1e-10)
    fd = focusDistance

    shutterAngle = DoubleAngleField(default_value=144.0)
    sa = shutterAngle

    centerOfInterest = DoubleLinearField(default_value=5.0, min_value=1e-10)
    coi = centerOfInterest

    orthographicWidth = DoubleLinearField(default_value=10.0, min_value=1e-10)
    ow = orthographicWidth

    imageName = DataStringField()
    imn = imageName

    depthName = DataStringField()
    den = depthName

    maskName = DataStringField()
    man = maskName

    tumblePivot = TumblePivotField(default_value=(0.0, 0.0, 0.0))
    tp = tumblePivot
    tumblePivotX = tumblePivot.tumblePivotX
    tpx = tumblePivotX
    tumblePivotY = tumblePivot.tumblePivotY
    tpy = tumblePivotY
    tumblePivotZ = tumblePivot.tumblePivotZ
    tpz = tumblePivotZ

    autoSetPivot = BoolField(default_value=False)
    asp = autoSetPivot

    usePivotAsLocalSpace = BoolField(default_value=False)
    uls = usePivotAsLocalSpace

    imagePlane = MessageField(multi=True, readable=False)
    ip = imagePlane

    homeCommand = DataStringField()
    hc = homeCommand

    bookmarks = MessageField(multi=True, readable=False)
    b = bookmarks

    locatorScale = DoubleField(default_value=1.0, min_value=1e-10)
    lls = locatorScale

    displayGateMaskOpacity = FloatField(default_value=0.699999988079071, min_value=0.0, max_value=1.0)
    dgo = displayGateMaskOpacity

    displayGateMask = BoolField(default_value=True)
    dgm = displayGateMask

    bookmarksEnabled = BoolField(default_value=True)
    ben = bookmarksEnabled

    displayFilmGate = BoolField(default_value=False)
    dfg = displayFilmGate

    displayResolution = BoolField(default_value=False)
    dr = displayResolution

    displaySafeAction = BoolField(default_value=False)
    dsa = displaySafeAction

    displaySafeTitle = BoolField(default_value=False)
    dst = displaySafeTitle

    displayFieldChart = BoolField(default_value=False)
    dfc = displayFieldChart

    displayFilmPivot = BoolField(default_value=False)
    dfp = displayFilmPivot

    displayFilmOrigin = BoolField(default_value=False)
    dfo = displayFilmOrigin

    clippingPlanes = BoolField(default_value=True)
    cp = clippingPlanes

    bestFitClippingPlanes = BoolField(default_value=True)
    bfc = bestFitClippingPlanes

    depthOfField = BoolField(default_value=False)
    dof = depthOfField

    motionBlur = BoolField(default_value=False)
    mb = motionBlur

    orthographic = BoolField(default_value=False)
    o = orthographic

    journalCommand = BoolField(default_value=False)
    jc = journalCommand

    image = BoolField(default_value=True)
    img = image

    depth = BoolField(default_value=False)
    dep = depth

    transparencyBasedDepth = BoolField(default_value=True)
    tdth = transparencyBasedDepth

    threshold = DoubleField(default_value=0.9, min_value=0.0, max_value=1.0)
    tthd = threshold

    depthType = DepthTypeEnumField(default_value=1)
    dptp = depthType

    useExploreDepthFormat = BoolField(default_value=False)
    uexd = useExploreDepthFormat

    mask = BoolField(default_value=True)
    ma = mask

    displayGateMaskColor = DisplayGateMaskColorField(default_value=(0.5, 0.5, 0.5))
    dgc = displayGateMaskColor
    displayGateMaskColorR = displayGateMaskColor.displayGateMaskColorR
    dgcr = displayGateMaskColorR
    displayGateMaskColorG = displayGateMaskColor.displayGateMaskColorG
    dgcg = displayGateMaskColorG
    displayGateMaskColorB = displayGateMaskColor.displayGateMaskColorB
    dgcb = displayGateMaskColorB

    backgroundColor = BackgroundColorField(default_value=(0.0, 0.0, 0.0))
    col = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    colr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    colg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    colb = backgroundColorB

    focusRegionScale = DoubleField(default_value=1.0, min_value=1e-10)
    frs = focusRegionScale

    displayCameraNearClip = BoolField(default_value=False)
    cnc = displayCameraNearClip

    displayCameraFarClip = BoolField(default_value=False)
    cfp = displayCameraFarClip

    displayCameraFrustum = BoolField(default_value=False)
    dcf = displayCameraFrustum

    cameraPrecompTemplate = DataStringField()
    cpt = cameraPrecompTemplate

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiPosition = AiPositionField(multi=True, default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_position = aiPosition

    aiLookAt = AiLookAtField(multi=True, default_value=(0.0, 0.0, -1.0), category="arnold")
    ai_look_at = aiLookAt

    aiUp = AiUpField(multi=True, default_value=(0.0, 1.0, 0.0), category="arnold")
    ai_up = aiUp

    aiMatrix = FltMatrixField(category="arnold")
    ai_matrix = aiMatrix

    aiHandedness = AiHandednessEnumField(default_value=0, category="arnold")
    ai_handedness = aiHandedness

    aiNearClip = FloatField(default_value=9.999999747378752e-05, category="arnold")
    ai_near_clip = aiNearClip

    aiFarClip = FloatField(default_value=1.0000000150474662e+30, category="arnold")
    ai_far_clip = aiFarClip

    aiScreenWindowMin = AiScreenWindowMinField(multi=True, default_value=(-1.0, -1.0), category="arnold")
    ai_screen_window_min = aiScreenWindowMin

    aiScreenWindowMax = AiScreenWindowMaxField(multi=True, default_value=(1.0, 1.0), category="arnold")
    ai_screen_window_max = aiScreenWindowMax

    aiShutterStart = FloatField(default_value=0.0, category="arnold")
    ai_shutter_start = aiShutterStart

    aiShutterEnd = FloatField(default_value=0.0, category="arnold")
    ai_shutter_end = aiShutterEnd

    aiShutterType = AiShutterTypeEnumField(default_value=0, category="arnold")
    ai_shutter_type = aiShutterType

    aiShutterCurve = AiShutterCurveField(multi=True, default_value=(3.957190478076633e-13, 6.6982066594726256e-43), category="arnold")
    ai_shutter_curve = aiShutterCurve

    aiRollingShutter = AiRollingShutterEnumField(default_value=0, category="arnold")
    ai_rolling_shutter = aiRollingShutter

    aiRollingShutterDuration = FloatField(default_value=0.0, category="arnold")
    ai_rolling_shutter_duration = aiRollingShutterDuration

    aiMotionStart = FloatField(default_value=0.0, category="arnold")
    ai_motion_start = aiMotionStart

    aiMotionEnd = FloatField(default_value=1.0, category="arnold")
    ai_motion_end = aiMotionEnd

    aiExposure = FloatField(default_value=0.0, category="arnold")
    ai_exposure = aiExposure

    aiFiltermap = MessageField(category="arnold")
    ai_filtermap = aiFiltermap

    aiMesh = MessageField(category="arnold")
    ai_mesh = aiMesh

    aiOffset = FloatField(default_value=0.10000000149011612, category="arnold")
    ai_offset = aiOffset

    aiGridSize = LongField(default_value=16, category="arnold")
    ai_grid_size = aiGridSize

    aiUOffset = FloatField(default_value=0.0, category="arnold")
    ai_u_offset = aiUOffset

    aiVOffset = FloatField(default_value=0.0, category="arnold")
    ai_v_offset = aiVOffset

    aiUvSet = DataStringField(category="arnold")
    ai_uv_set = aiUvSet

    aiUScale = FloatField(default_value=1.0, category="arnold")
    ai_u_scale = aiUScale

    aiVScale = FloatField(default_value=1.0, category="arnold")
    ai_v_scale = aiVScale

    aiExtendEdges = BoolField(default_value=True, category="arnold")
    ai_extend_edges = aiExtendEdges

    aiRayOrigin = AiRayOriginField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_ray_origin = aiRayOrigin
    aiRayOriginX = aiRayOrigin.aiRayOriginX
    ai_ray_originx = aiRayOriginX
    aiRayOriginY = aiRayOrigin.aiRayOriginY
    ai_ray_originy = aiRayOriginY
    aiRayOriginZ = aiRayOrigin.aiRayOriginZ
    ai_ray_originz = aiRayOriginZ

    aiRayDirection = AiRayDirectionField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_ray_direction = aiRayDirection
    aiRayDirectionX = aiRayDirection.aiRayDirectionX
    ai_ray_directionx = aiRayDirectionX
    aiRayDirectionY = aiRayDirection.aiRayDirectionY
    ai_ray_directiony = aiRayDirectionY
    aiRayDirectionZ = aiRayDirection.aiRayDirectionZ
    ai_ray_directionz = aiRayDirectionZ

    aiPostBake = MessageField(category="arnold")
    ai_post_bake = aiPostBake

    aiUseGlobalShutter = BoolField(default_value=True, category="arnold")
    ai_ugs = aiUseGlobalShutter

    aiProjective = BoolField(default_value=True, category="arnold")
    ai_projective = aiProjective

    aiHorizontalFov = FloatField(default_value=60.0, category="arnold")
    ai_horizontal_fov = aiHorizontalFov

    aiVerticalFov = FloatField(default_value=90.0, category="arnold")
    ai_vertical_fov = aiVerticalFov

    aiMode = AiModeEnumField(default_value=0, category="arnold")
    ai_mode = aiMode

    aiProjection = AiProjectionEnumField(default_value=0, category="arnold")
    ai_projection = aiProjection

    aiEyeSeparation = FloatField(default_value=0.6499999761581421, soft_min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_eye_separation = aiEyeSeparation

    aiEyeToNeck = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_eye_to_neck = aiEyeToNeck

    aiTopMergeMode = AiTopMergeModeEnumField(default_value=1, category="arnold")
    ai_top_merge_mode = aiTopMergeMode

    aiTopMergeAngle = FloatField(default_value=90.0, min_value=0.0, max_value=180.0, soft_min_value=0.0, soft_max_value=90.0, category="arnold")
    ai_top_merge_angle = aiTopMergeAngle

    aiBottomMergeMode = AiBottomMergeModeEnumField(default_value=1, category="arnold")
    ai_bottom_merge_mode = aiBottomMergeMode

    aiBottomMergeAngle = FloatField(default_value=90.0, min_value=0.0, max_value=180.0, soft_min_value=0.0, soft_max_value=90.0, category="arnold")
    ai_bottom_merge_angle = aiBottomMergeAngle

    aiMergeShader = FloatField(default_value=0.0, category="arnold")
    ai_merge_shader = aiMergeShader

    aiFocusDistance = FloatField(default_value=5.0, min_value=0.0, max_value=1000000000.0, soft_min_value=0.0, soft_max_value=200.0, category="arnold")
    ai_focus_distance = aiFocusDistance

    aiApertureSize = FloatField(default_value=0.0, min_value=0.0, max_value=20.0, soft_min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_aperture_size = aiApertureSize

    aiApertureBlades = LongField(default_value=0, min_value=0, max_value=40, category="arnold")
    ai_aperture_blades = aiApertureBlades

    aiApertureBladeCurvature = FloatField(default_value=0.0, min_value=-20.0, max_value=20.0, soft_min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_aperture_blade_curvature = aiApertureBladeCurvature

    aiApertureRotation = FloatField(default_value=0.0, min_value=0.0, max_value=360.0, soft_min_value=0.0, soft_max_value=50.0, category="arnold")
    ai_aperture_rotation = aiApertureRotation

    aiApertureAspectRatio = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0, category="arnold")
    ai_aperture_aspect_ratio = aiApertureAspectRatio

    aiEnableDOF = BoolField(default_value=False, category="arnold")
    ai_edof = aiEnableDOF

    aiUvRemapA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_uv_remapa = aiUvRemapA

    aiUvRemap = AiUvRemapField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_uv_remap = aiUvRemap
    aiUvRemapR = aiUvRemap.aiUvRemapR
    ai_uv_remapr = aiUvRemapR
    aiUvRemapG = aiUvRemap.aiUvRemapG
    ai_uv_remapg = aiUvRemapG
    aiUvRemapB = aiUvRemap.aiUvRemapB
    ai_uv_remapb = aiUvRemapB

    aiRadialDistortion = FloatField(default_value=0.0, soft_min_value=-0.20000000298023224, soft_max_value=2.0, category="arnold")
    ai_radial_distortion = aiRadialDistortion

    aiRadialDistortionType = AiRadialDistortionTypeEnumField(default_value=0, category="arnold")
    ai_radial_distortion_type = aiRadialDistortionType

    aiLensTiltAngle = AiLensTiltAngleField(default_value=(0.0, 0.0), category="arnold")
    ai_lens_tilt_angle = aiLensTiltAngle
    aiLensTiltAngleX = aiLensTiltAngle.aiLensTiltAngleX
    ai_lens_tilt_anglex = aiLensTiltAngleX
    aiLensTiltAngleY = aiLensTiltAngle.aiLensTiltAngleY
    ai_lens_tilt_angley = aiLensTiltAngleY

    aiLensShift = AiLensShiftField(default_value=(0.0, 0.0), category="arnold")
    ai_lens_shift = aiLensShift
    aiLensShiftX = aiLensShift.aiLensShiftX
    ai_lens_shiftx = aiLensShiftX
    aiLensShiftY = aiLensShift.aiLensShiftY
    ai_lens_shifty = aiLensShiftY

    motionBlurOverride = MotionBlurOverrideEnumField(default_value=0, category="arnold")
    motion_blur_override = motionBlurOverride

    aiFov = FloatField(default_value=90.0, category="arnold")
    ai_fov = aiFov

    aiAutocrop = BoolField(default_value=False, category="arnold")
    ai_autocrop = aiAutocrop

    aiTranslator = DataStringField(category="arnold")
    ai_translator = aiTranslator

    stereo = StereoEnumField(default_value=0)
    sm = stereo

    interaxialSeparation = DoubleLinearField(default_value=6.35, min_value=0.0, soft_min_value=0.0, soft_max_value=20.0)
    isep = interaxialSeparation

    zeroParallax = DoubleLinearField(default_value=254.0, min_value=0.001, soft_min_value=0.001, soft_max_value=1000.0)
    zp = zeroParallax

    toeInAdjust = DoubleAngleField(default_value=0.0, min_value=-90.0, max_value=90.0, soft_min_value=0.0, soft_max_value=29.999999999999996)
    tia = toeInAdjust

    filmOffsetRightCam = FloatField(default_value=0.0)
    fofr = filmOffsetRightCam

    filmOffsetLeftCam = FloatField(default_value=0.0)
    fofl = filmOffsetLeftCam

    displayNearClip = DisplayNearClipEnumField(default_value=0)
    dncp = displayNearClip

    displayFarClip = DisplayFarClipEnumField(default_value=0)
    dfcp = displayFarClip

    displayFrustum = DisplayFrustumEnumField(default_value=0)
    df = displayFrustum

    zeroParallaxPlane = BoolField(default_value=False)
    zpp = zeroParallaxPlane

    zeroParallaxTransparency = FloatField(default_value=0.25, min_value=0.0, max_value=1.0)
    zpt = zeroParallaxTransparency

    zeroParallaxColor = ZeroParallaxColorField(default_value=(0.8299999833106995, 0.23000000417232513, 0.10000000149011612))
    zpc = zeroParallaxColor
    zeroParallaxColorRed = zeroParallaxColor.zeroParallaxColorRed
    zpcr = zeroParallaxColorRed
    zeroParallaxColorGreen = zeroParallaxColor.zeroParallaxColorGreen
    zpcg = zeroParallaxColorGreen
    zeroParallaxColorBlue = zeroParallaxColor.zeroParallaxColorBlue
    zpcb = zeroParallaxColorBlue

    safeViewingVolume = BoolField(default_value=False)
    svv = safeViewingVolume

    safeVolumeTransparency = FloatField(default_value=0.25, min_value=0.0, max_value=1.0)
    svt = safeVolumeTransparency

    safeVolumeColor = SafeVolumeColorField(default_value=(0.23800000548362732, 0.8080000281333923, 1.0))
    svc = safeVolumeColor
    safeVolumeColorRed = safeVolumeColor.safeVolumeColorRed
    svcr = safeVolumeColorRed
    safeVolumeColorGreen = safeVolumeColor.safeVolumeColorGreen
    svcg = safeVolumeColorGreen
    safeVolumeColorBlue = safeVolumeColor.safeVolumeColorBlue
    svcb = safeVolumeColorBlue

    safeStereo = BoolField(default_value=True)
    ss = safeStereo
