# coding: utf-8
from ..._core import DAG
from .....attr.define.node_attr.transform import (
    BoundingBoxField,
    CenterField,
    DrawOverrideField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    InstObjGroupsField,
    MaxRotLimitEnableField,
    MaxRotLimitField,
    MaxScaleLimitEnableField,
    MaxScaleLimitField,
    MaxTransLimitEnableField,
    MaxTransLimitField,
    MinRotLimitEnableField,
    MinRotLimitField,
    MinScaleLimitEnableField,
    MinScaleLimitField,
    MinTransLimitEnableField,
    MinTransLimitField,
    ObjectColorRGBField,
    OutlinerColorField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    RotateAxisField,
    RotateField,
    RotatePivotField,
    RotatePivotTranslateField,
    RotateQuaternionField,
    ScaleField,
    ScalePivotField,
    ScalePivotTranslateField,
    SelectHandleField,
    ShearField,
    TransMinusRotatePivotField,
    TranslateField,
    WireColorRGBField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.generic import GenericField
from .....attr.define.std.at.matrix import MatrixField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.string import DataStringField


class ViewModeEnumPlugOperator(EnumPlugOperator["ViewModeEnumAttrOperator"]):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator[ViewModeEnumPlugOperator]):
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


class UiTreatmentEnumPlugOperator(
    EnumPlugOperator["UiTreatmentEnumAttrOperator"]
):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(
    EnumAttrOperator[UiTreatmentEnumPlugOperator]
):
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


class UseObjectColorEnumPlugOperator(
    EnumPlugOperator["UseObjectColorEnumAttrOperator"]
):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(
    EnumAttrOperator[UseObjectColorEnumPlugOperator]
):
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


class GhostingModeEnumPlugOperator(
    EnumPlugOperator["GhostingModeEnumAttrOperator"]
):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(
    EnumAttrOperator[GhostingModeEnumPlugOperator]
):
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


class RotateOrderEnumPlugOperator(
    EnumPlugOperator["RotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(
    EnumAttrOperator[RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class ShowManipDefaultEnumPlugOperator(
    EnumPlugOperator["ShowManipDefaultEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    TRANSLATE = 1
    ROTATE = 2
    SCALE = 3
    TRANSFORM = 4
    GLOBAL_DEFAULT = 5
    SMART = 6
    SPECIFIED = 7


class ShowManipDefaultEnumAttrOperator(
    EnumAttrOperator[ShowManipDefaultEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    TRANSLATE = 1
    ROTATE = 2
    SCALE = 3
    TRANSFORM = 4
    GLOBAL_DEFAULT = 5
    SMART = 6
    SPECIFIED = 7

    NAME_MAP = {
        NONE: "None",
        TRANSLATE: "Translate",
        ROTATE: "Rotate",
        SCALE: "Scale",
        TRANSFORM: "Transform",
        GLOBAL_DEFAULT: "Global default",
        SMART: "Smart",
        SPECIFIED: "Specified",
    }


class ShowManipDefaultEnumField(
    EnumField[
        ShowManipDefaultEnumAttrOperator, ShowManipDefaultEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShowManipDefaultEnumAttrOperator
    PLUG_CLS = ShowManipDefaultEnumPlugOperator


class RotationInterpolationEnumPlugOperator(
    EnumPlugOperator["RotationInterpolationEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 1
    EULER = 2
    QUATERNION = 3


class RotationInterpolationEnumAttrOperator(
    EnumAttrOperator[RotationInterpolationEnumPlugOperator]
):
    __slots__ = ()

    NONE = 1
    EULER = 2
    QUATERNION = 3

    NAME_MAP = {
        NONE: "None",
        EULER: "Euler",
        QUATERNION: "Quaternion",
    }


class RotationInterpolationEnumField(
    EnumField[
        RotationInterpolationEnumAttrOperator,
        RotationInterpolationEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationInterpolationEnumAttrOperator
    PLUG_CLS = RotationInterpolationEnumPlugOperator


class GeneratedTransform(DAG):
    __slots__ = ()

    NODE_TYPE = "transform"

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

    renderLayerInfo = RenderLayerInfoField(
        multi=True, default_value=(0.0, 1.0, 0.0)
    )
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

    ghostOpacityRange = GhostOpacityRangeField(
        default_value=(0.15000000596046448, 0.5),
        min_value=(0.0, 0.0),
        max_value=(1.0, 1.0),
    )
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(
        default_value=(0.44699999690055847, 1.0, 1.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(
        default_value=(
            0.878000020980835,
            0.6779999732971191,
            0.6629999876022339,
        ),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
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

    translate = TranslateField(default_value=(0.0, 0.0, 0.0))
    t = translate
    translateX = translate.translateX
    tx = translateX
    translateY = translate.translateY
    ty = translateY
    translateZ = translate.translateZ
    tz = translateZ

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    r = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    s = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    shear = ShearField(default_value=(0.0, 0.0, 0.0))
    sh = shear
    shearXY = shear.shearXY
    shxy = shearXY
    shearXZ = shear.shearXZ
    shxz = shearXZ
    shearYZ = shear.shearYZ
    shyz = shearYZ

    rotatePivot = RotatePivotField(default_value=(0.0, 0.0, 0.0))
    rp = rotatePivot
    rotatePivotX = rotatePivot.rotatePivotX
    rpx = rotatePivotX
    rotatePivotY = rotatePivot.rotatePivotY
    rpy = rotatePivotY
    rotatePivotZ = rotatePivot.rotatePivotZ
    rpz = rotatePivotZ

    rotatePivotTranslate = RotatePivotTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    rpt = rotatePivotTranslate
    rotatePivotTranslateX = rotatePivotTranslate.rotatePivotTranslateX
    rptx = rotatePivotTranslateX
    rotatePivotTranslateY = rotatePivotTranslate.rotatePivotTranslateY
    rpty = rotatePivotTranslateY
    rotatePivotTranslateZ = rotatePivotTranslate.rotatePivotTranslateZ
    rptz = rotatePivotTranslateZ

    scalePivot = ScalePivotField(default_value=(0.0, 0.0, 0.0))
    sp = scalePivot
    scalePivotX = scalePivot.scalePivotX
    spx = scalePivotX
    scalePivotY = scalePivot.scalePivotY
    spy = scalePivotY
    scalePivotZ = scalePivot.scalePivotZ
    spz = scalePivotZ

    scalePivotTranslate = ScalePivotTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    spt = scalePivotTranslate
    scalePivotTranslateX = scalePivotTranslate.scalePivotTranslateX
    sptx = scalePivotTranslateX
    scalePivotTranslateY = scalePivotTranslate.scalePivotTranslateY
    spty = scalePivotTranslateY
    scalePivotTranslateZ = scalePivotTranslate.scalePivotTranslateZ
    sptz = scalePivotTranslateZ

    rotateAxis = RotateAxisField(default_value=(0.0, 0.0, 0.0))
    ra = rotateAxis
    rotateAxisX = rotateAxis.rotateAxisX
    rax = rotateAxisX
    rotateAxisY = rotateAxis.rotateAxisY
    ray = rotateAxisY
    rotateAxisZ = rotateAxis.rotateAxisZ
    raz = rotateAxisZ

    transMinusRotatePivot = TransMinusRotatePivotField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    tmrp = transMinusRotatePivot
    transMinusRotatePivotX = transMinusRotatePivot.transMinusRotatePivotX
    tmrx = transMinusRotatePivotX
    transMinusRotatePivotY = transMinusRotatePivot.transMinusRotatePivotY
    tmry = transMinusRotatePivotY
    transMinusRotatePivotZ = transMinusRotatePivot.transMinusRotatePivotZ
    tmrz = transMinusRotatePivotZ

    minTransLimit = MinTransLimitField(default_value=(-1.0, -1.0, -1.0))
    mntl = minTransLimit
    minTransXLimit = minTransLimit.minTransXLimit
    mtxl = minTransXLimit
    minTransYLimit = minTransLimit.minTransYLimit
    mtyl = minTransYLimit
    minTransZLimit = minTransLimit.minTransZLimit
    mtzl = minTransZLimit

    maxTransLimit = MaxTransLimitField(default_value=(1.0, 1.0, 1.0))
    mxtl = maxTransLimit
    maxTransXLimit = maxTransLimit.maxTransXLimit
    xtxl = maxTransXLimit
    maxTransYLimit = maxTransLimit.maxTransYLimit
    xtyl = maxTransYLimit
    maxTransZLimit = maxTransLimit.maxTransZLimit
    xtzl = maxTransZLimit

    minTransLimitEnable = MinTransLimitEnableField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    mtle = minTransLimitEnable
    minTransXLimitEnable = minTransLimitEnable.minTransXLimitEnable
    mtxe = minTransXLimitEnable
    minTransYLimitEnable = minTransLimitEnable.minTransYLimitEnable
    mtye = minTransYLimitEnable
    minTransZLimitEnable = minTransLimitEnable.minTransZLimitEnable
    mtze = minTransZLimitEnable

    maxTransLimitEnable = MaxTransLimitEnableField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    xtle = maxTransLimitEnable
    maxTransXLimitEnable = maxTransLimitEnable.maxTransXLimitEnable
    xtxe = maxTransXLimitEnable
    maxTransYLimitEnable = maxTransLimitEnable.maxTransYLimitEnable
    xtye = maxTransYLimitEnable
    maxTransZLimitEnable = maxTransLimitEnable.maxTransZLimitEnable
    xtze = maxTransZLimitEnable

    minRotLimit = MinRotLimitField(
        default_value=(
            -0.7853981633974483,
            -0.7853981633974483,
            -0.7853981633974483,
        )
    )
    mnrl = minRotLimit
    minRotXLimit = minRotLimit.minRotXLimit
    mrxl = minRotXLimit
    minRotYLimit = minRotLimit.minRotYLimit
    mryl = minRotYLimit
    minRotZLimit = minRotLimit.minRotZLimit
    mrzl = minRotZLimit

    maxRotLimit = MaxRotLimitField(
        default_value=(
            0.7853981633974483,
            0.7853981633974483,
            0.7853981633974483,
        )
    )
    mxrl = maxRotLimit
    maxRotXLimit = maxRotLimit.maxRotXLimit
    xrxl = maxRotXLimit
    maxRotYLimit = maxRotLimit.maxRotYLimit
    xryl = maxRotYLimit
    maxRotZLimit = maxRotLimit.maxRotZLimit
    xrzl = maxRotZLimit

    minRotLimitEnable = MinRotLimitEnableField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    mrle = minRotLimitEnable
    minRotXLimitEnable = minRotLimitEnable.minRotXLimitEnable
    mrxe = minRotXLimitEnable
    minRotYLimitEnable = minRotLimitEnable.minRotYLimitEnable
    mrye = minRotYLimitEnable
    minRotZLimitEnable = minRotLimitEnable.minRotZLimitEnable
    mrze = minRotZLimitEnable

    maxRotLimitEnable = MaxRotLimitEnableField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    xrle = maxRotLimitEnable
    maxRotXLimitEnable = maxRotLimitEnable.maxRotXLimitEnable
    xrxe = maxRotXLimitEnable
    maxRotYLimitEnable = maxRotLimitEnable.maxRotYLimitEnable
    xrye = maxRotYLimitEnable
    maxRotZLimitEnable = maxRotLimitEnable.maxRotZLimitEnable
    xrze = maxRotZLimitEnable

    minScaleLimit = MinScaleLimitField(default_value=(-1.0, -1.0, -1.0))
    mnsl = minScaleLimit
    minScaleXLimit = minScaleLimit.minScaleXLimit
    msxl = minScaleXLimit
    minScaleYLimit = minScaleLimit.minScaleYLimit
    msyl = minScaleYLimit
    minScaleZLimit = minScaleLimit.minScaleZLimit
    mszl = minScaleZLimit

    maxScaleLimit = MaxScaleLimitField(default_value=(1.0, 1.0, 1.0))
    mxsl = maxScaleLimit
    maxScaleXLimit = maxScaleLimit.maxScaleXLimit
    xsxl = maxScaleXLimit
    maxScaleYLimit = maxScaleLimit.maxScaleYLimit
    xsyl = maxScaleYLimit
    maxScaleZLimit = maxScaleLimit.maxScaleZLimit
    xszl = maxScaleZLimit

    minScaleLimitEnable = MinScaleLimitEnableField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    msle = minScaleLimitEnable
    minScaleXLimitEnable = minScaleLimitEnable.minScaleXLimitEnable
    msxe = minScaleXLimitEnable
    minScaleYLimitEnable = minScaleLimitEnable.minScaleYLimitEnable
    msye = minScaleYLimitEnable
    minScaleZLimitEnable = minScaleLimitEnable.minScaleZLimitEnable
    msze = minScaleZLimitEnable

    maxScaleLimitEnable = MaxScaleLimitEnableField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    xsle = maxScaleLimitEnable
    maxScaleXLimitEnable = maxScaleLimitEnable.maxScaleXLimitEnable
    xsxe = maxScaleXLimitEnable
    maxScaleYLimitEnable = maxScaleLimitEnable.maxScaleYLimitEnable
    xsye = maxScaleYLimitEnable
    maxScaleZLimitEnable = maxScaleLimitEnable.maxScaleZLimitEnable
    xsze = maxScaleZLimitEnable

    offsetParentMatrix = MatrixField()
    opm = offsetParentMatrix

    dagLocalMatrix = MatrixField(writable=False)
    dlm = dagLocalMatrix

    dagLocalInverseMatrix = MatrixField(writable=False)
    dlim = dagLocalInverseMatrix

    geometry = GenericField(readable=False)
    g = geometry

    xformMatrix = DataMatrixField(writable=False)
    xm = xformMatrix

    selectHandle = SelectHandleField(default_value=(0.0, 0.0, 0.0))
    hdl = selectHandle
    selectHandleX = selectHandle.selectHandleX
    hdlx = selectHandleX
    selectHandleY = selectHandle.selectHandleY
    hdly = selectHandleY
    selectHandleZ = selectHandle.selectHandleZ
    hdlz = selectHandleZ

    inheritsTransform = BoolField(default_value=True)
    it = inheritsTransform

    displayHandle = BoolField(default_value=False)
    dh = displayHandle

    displayScalePivot = BoolField(default_value=False)
    dsp = displayScalePivot

    displayRotatePivot = BoolField(default_value=False)
    drp = displayRotatePivot

    displayLocalAxis = BoolField(default_value=False)
    dla = displayLocalAxis

    dynamics = BoolField(default_value=False, readable=False)
    dyn = dynamics

    showManipDefault = ShowManipDefaultEnumField(default_value=0)
    smd = showManipDefault

    specifiedManipLocation = TypedField(readable=False)
    sml = specifiedManipLocation

    rotateQuaternion = RotateQuaternionField(
        default_value=(0.0, 0.0, 0.0, 0.0)
    )
    rq = rotateQuaternion
    rotateQuaternionX = rotateQuaternion.rotateQuaternionX
    rqx = rotateQuaternionX
    rotateQuaternionY = rotateQuaternion.rotateQuaternionY
    rqy = rotateQuaternionY
    rotateQuaternionZ = rotateQuaternion.rotateQuaternionZ
    rqz = rotateQuaternionZ
    rotateQuaternionW = rotateQuaternion.rotateQuaternionW
    rqw = rotateQuaternionW

    rotationInterpolation = RotationInterpolationEnumField(
        default_value=1, writable=False
    )
    roi = rotationInterpolation
