# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.deform_wave import (
    BoundingBoxField,
    CenterField,
    DrawOverrideField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    ObjectColorRGBField,
    OutlinerColorField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    WireColorRGBField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
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


class DeformWave(Shape):
    __slots__ = ()

    NODE_TYPE = "deformWave"

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

    deformerData = DataDoubleArrayField()
    dd = deformerData

    handleWidth = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=50.0)
    hw = handleWidth

    maxRadius = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    mxr = maxRadius

    minRadius = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    mnr = minRadius

    amplitude = DoubleField(default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0)
    amp = amplitude

    wavelength = DoubleField(default_value=1.0, min_value=0.1, soft_min_value=0.1, soft_max_value=10.0)
    wav = wavelength

    dropoff = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    dr = dropoff

    dropoffPosition = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    dp = dropoffPosition

    offset = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    off = offset
