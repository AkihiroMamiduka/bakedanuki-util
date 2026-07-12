# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.grease_plane import (
    AiOffscreenColorField,
    BoundingBoxField,
    CenterField,
    ColorGainField,
    ColorOffsetField,
    CoverageField,
    CoverageOriginField,
    DrawOverrideField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    ImageCenterField,
    InstObjGroupsField,
    ObjectColorRGBField,
    OffsetField,
    OutlinerColorField,
    OutputImageDimensionsField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    RenderPlaneRotateField,
    RenderPlaneScaleField,
    RenderPlaneTranslateField,
    SizeField,
    SourcePlaneRotateField,
    SourcePlaneScaleField,
    SourcePlaneTranslateField,
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


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    IMAGE_FILE = 0
    TEXTURE = 1
    MOVIE = 2


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    IMAGE_FILE = 0
    TEXTURE = 1
    MOVIE = 2

    NAME_MAP = {
        IMAGE_FILE: "Image File",
        TEXTURE: "Texture",
        MOVIE: "Movie",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class FitEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FILL = 0
    BEST = 1
    HORIZONTAL = 2
    VERTICAL = 3
    TO_SIZE = 4


class FitEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FILL = 0
    BEST = 1
    HORIZONTAL = 2
    VERTICAL = 3
    TO_SIZE = 4

    NAME_MAP = {
        FILL: "Fill",
        BEST: "Best",
        HORIZONTAL: "Horizontal",
        VERTICAL: "Vertical",
        TO_SIZE: "To Size",
    }


class FitEnumField(
    EnumField[FitEnumAttrOperator, FitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FitEnumAttrOperator
    PLUG_CLS = FitEnumPlugOperator


class DisplayModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    OUTLINE = 1
    RGB = 2
    RGBA = 3
    LUMINANCE = 4
    ALPHA = 5


class DisplayModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    OUTLINE = 1
    RGB = 2
    RGBA = 3
    LUMINANCE = 4
    ALPHA = 5

    NAME_MAP = {
        NONE: "None",
        OUTLINE: "Outline",
        RGB: "RGB",
        RGBA: "RGBA",
        LUMINANCE: "Luminance",
        ALPHA: "Alpha",
    }


class DisplayModeEnumField(
    EnumField[DisplayModeEnumAttrOperator, DisplayModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayModeEnumAttrOperator
    PLUG_CLS = DisplayModeEnumPlugOperator


class TextureFilterEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NEAREST_UNFILTERED = 0
    BILINEAR = 1
    MIPMAP_NEAREST = 2
    MIPMAP_LINEAR = 3
    MIPMAP_BILINEAR = 4
    MIPMAP_TRILINEAR = 5


class TextureFilterEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NEAREST_UNFILTERED = 0
    BILINEAR = 1
    MIPMAP_NEAREST = 2
    MIPMAP_LINEAR = 3
    MIPMAP_BILINEAR = 4
    MIPMAP_TRILINEAR = 5

    NAME_MAP = {
        NEAREST_UNFILTERED: "Nearest(Unfiltered)",
        BILINEAR: "Bilinear",
        MIPMAP_NEAREST: "Mipmap Nearest",
        MIPMAP_LINEAR: "Mipmap Linear",
        MIPMAP_BILINEAR: "Mipmap Bilinear",
        MIPMAP_TRILINEAR: "MipMap Trilinear",
    }


class TextureFilterEnumField(
    EnumField[TextureFilterEnumAttrOperator, TextureFilterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureFilterEnumAttrOperator
    PLUG_CLS = TextureFilterEnumPlugOperator


class GreasePlane(Shape):
    __slots__ = ()

    NODE_TYPE = "greasePlane"

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

    type = TypeEnumField(default_value=0)
    t = type

    frameCache = LongField(default_value=24, min_value=0, max_value=2147483647, soft_max_value=100)
    fc = frameCache

    imageName = DataStringField()
    imn = imageName

    useFrameExtension = BoolField(default_value=False)
    ufe = useFrameExtension

    outputImageDimensions = OutputImageDimensionsField(default_value=(0, 0, 0), writable=False)
    oid = outputImageDimensions
    outputImageWidth = outputImageDimensions.outputImageWidth
    oiw = outputImageWidth
    outputImageHeight = outputImageDimensions.outputImageHeight
    oih = outputImageHeight
    outputImageFrames = outputImageDimensions.outputImageFrames
    oif = outputImageFrames

    outputImageFlags = LongField(default_value=0, writable=False)
    oig = outputImageFlags

    frameExtension = LongField(default_value=1)
    fe = frameExtension

    frameOffset = LongField(default_value=0)
    fo = frameOffset

    frameIn = LongField(default_value=-1)
    fin = frameIn

    frameOut = LongField(default_value=-1)
    fot = frameOut

    outputFrameExtension = LongField(default_value=0, writable=False)
    ofe = outputFrameExtension

    resolvedFilePath = DataStringField(writable=False)
    rfp = resolvedFilePath

    coverage = CoverageField(default_value=(-1, -1), min_value=(1, 1), max_value=(32767, 32767))
    cov = coverage
    coverageX = coverage.coverageX
    cvx = coverageX
    coverageY = coverage.coverageY
    cvy = coverageY

    coverageOrigin = CoverageOriginField(default_value=(0, 0), min_value=(-32767, -32767), max_value=(32767, 32767))
    co = coverageOrigin
    coverageOriginX = coverageOrigin.coverageOriginX
    cox = coverageOriginX
    coverageOriginY = coverageOrigin.coverageOriginY
    coy = coverageOriginY

    sourceTexture = MessageField()
    stx = sourceTexture

    fit = FitEnumField(default_value=1)
    f = fit

    displayMode = DisplayModeEnumField(default_value=3)
    dm = displayMode

    displayOnlyIfCurrent = BoolField(default_value=False)
    dic = displayOnlyIfCurrent

    lookThroughCamera = MessageField()
    ltc = lookThroughCamera

    colorGain = ColorGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    cof = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    ag = alphaGain

    shadingSamplesOverride = BoolField(default_value=True)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
    msa = maxShadingSamples

    lockedToCamera = BoolField(default_value=True)
    dlc = lockedToCamera

    depth = DoubleLinearField(default_value=100.0, min_value=1e-10)
    d = depth

    squeezeCorrection = DoubleField(default_value=1.0, min_value=0.0)
    sqc = squeezeCorrection

    size = SizeField(default_value=(1.4173200000000001, 0.94488), min_value=(0.0, 0.0))
    s = size
    sizeX = size.sizeX
    sx = sizeX
    sizeY = size.sizeY
    sy = sizeY

    offset = OffsetField(default_value=(0.0, 0.0))
    o = offset
    offsetX = offset.offsetX
    ox = offsetX
    offsetY = offset.offsetY
    oy = offsetY

    imageCenter = ImageCenterField(default_value=(0.0, 0.0, 0.0))
    ic = imageCenter
    imageCenterX = imageCenter.imageCenterX
    icx = imageCenterX
    imageCenterY = imageCenter.imageCenterY
    icy = imageCenterY
    imageCenterZ = imageCenter.imageCenterZ
    icz = imageCenterZ

    width = DoubleLinearField(default_value=0.0, min_value=0.0)
    w = width

    height = DoubleLinearField(default_value=0.0, min_value=0.0)
    h = height

    maintainRatio = BoolField(default_value=True)
    mr = maintainRatio

    frameVisibility = BoolField(default_value=False)
    fvt = frameVisibility

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    rotate = DoubleAngleField(default_value=0.0)
    r = rotate

    useDepthMap = BoolField(default_value=False)
    udm = useDepthMap

    compositeDepth = BoolField(default_value=True)
    cmp = compositeDepth

    alreadyPremult = BoolField(default_value=False)
    pre = alreadyPremult

    depthOversample = BoolField(default_value=False)
    osp = depthOversample

    separateDepth = BoolField(default_value=False)
    sd = separateDepth

    depthFile = DataStringField()
    df = depthFile

    depthBias = DoubleLinearField(default_value=0.0)
    dg = depthBias

    depthScale = DoubleField(default_value=1.0, min_value=9.999999747378752e-06)
    ds = depthScale

    textureFilter = TextureFilterEnumField(default_value=0)
    tf = textureFilter

    colorSpace = DataStringField()
    cs = colorSpace

    ignoreColorSpaceFileRules = BoolField(default_value=False)
    ifr = ignoreColorSpaceFileRules

    viewNameUsed = BoolField(default_value=False)
    vnu = viewNameUsed

    viewNameStr = DataStringField()
    vns = viewNameStr

    workingSpace = DataStringField()
    ws = workingSpace

    colorManagementEnabled = BoolField(default_value=False)
    cme = colorManagementEnabled

    colorManagementConfigFileEnabled = BoolField(default_value=False)
    cmcf = colorManagementConfigFileEnabled

    colorManagementConfigFilePath = DataStringField()
    cmcp = colorManagementConfigFilePath

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiAutoTx = BoolField(default_value=True, category="arnold")
    autotx = aiAutoTx

    aiOffscreenColor = AiOffscreenColorField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_offrscreen_color = aiOffscreenColor
    aiOffscreenColorR = aiOffscreenColor.aiOffscreenColorR
    ai_offrscreen_colorr = aiOffscreenColorR
    aiOffscreenColorG = aiOffscreenColor.aiOffscreenColorG
    ai_offrscreen_colorg = aiOffscreenColorG
    aiOffscreenColorB = aiOffscreenColor.aiOffscreenColorB
    ai_offrscreen_colorb = aiOffscreenColorB

    aiOffscreenColorA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_offrscreen_colora = aiOffscreenColorA

    sourcePlane = MessageField()
    spl = sourcePlane

    renderPlane = MessageField()
    rpl = renderPlane

    greaseSequence = MessageField()
    gsq = greaseSequence

    sourceDepth = DoubleLinearField(default_value=2000.0, min_value=1e-10)
    srd = sourceDepth

    renderPlaneTranslate = RenderPlaneTranslateField(default_value=(0.0, 0.0, 0.0), writable=False)
    rptr = renderPlaneTranslate
    renderPlaneTranslateX = renderPlaneTranslate.renderPlaneTranslateX
    rptx = renderPlaneTranslateX
    renderPlaneTranslateY = renderPlaneTranslate.renderPlaneTranslateY
    rpty = renderPlaneTranslateY
    renderPlaneTranslateZ = renderPlaneTranslate.renderPlaneTranslateZ
    rptz = renderPlaneTranslateZ

    sourcePlaneTranslate = SourcePlaneTranslateField(default_value=(0.0, 0.0, 0.0), writable=False)
    sptr = sourcePlaneTranslate
    sourcePlaneTranslateX = sourcePlaneTranslate.sourcePlaneTranslateX
    sptx = sourcePlaneTranslateX
    sourcePlaneTranslateY = sourcePlaneTranslate.sourcePlaneTranslateY
    spty = sourcePlaneTranslateY
    sourcePlaneTranslateZ = sourcePlaneTranslate.sourcePlaneTranslateZ
    sptz = sourcePlaneTranslateZ

    renderPlaneRotate = RenderPlaneRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    rpr = renderPlaneRotate
    renderPlaneRotateX = renderPlaneRotate.renderPlaneRotateX
    rprx = renderPlaneRotateX
    renderPlaneRotateY = renderPlaneRotate.renderPlaneRotateY
    rpry = renderPlaneRotateY
    renderPlaneRotateZ = renderPlaneRotate.renderPlaneRotateZ
    rprz = renderPlaneRotateZ

    sourcePlaneRotate = SourcePlaneRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    spr = sourcePlaneRotate
    sourcePlaneRotateX = sourcePlaneRotate.sourcePlaneRotateX
    sprx = sourcePlaneRotateX
    sourcePlaneRotateY = sourcePlaneRotate.sourcePlaneRotateY
    spry = sourcePlaneRotateY
    sourcePlaneRotateZ = sourcePlaneRotate.sourcePlaneRotateZ
    sprz = sourcePlaneRotateZ

    renderPlaneScale = RenderPlaneScaleField(default_value=(1.0, 1.0, 1.0), writable=False)
    rps = renderPlaneScale
    renderPlaneScaleX = renderPlaneScale.renderPlaneScaleX
    rpsx = renderPlaneScaleX
    renderPlaneScaleY = renderPlaneScale.renderPlaneScaleY
    rpsy = renderPlaneScaleY
    renderPlaneScaleZ = renderPlaneScale.renderPlaneScaleZ
    rpsz = renderPlaneScaleZ

    sourcePlaneScale = SourcePlaneScaleField(default_value=(1.0, 1.0, 1.0), writable=False)
    sps = sourcePlaneScale
    sourcePlaneScaleX = sourcePlaneScale.sourcePlaneScaleX
    spsx = sourcePlaneScaleX
    sourcePlaneScaleY = sourcePlaneScale.sourcePlaneScaleY
    spsy = sourcePlaneScaleY
    sourcePlaneScaleZ = sourcePlaneScale.sourcePlaneScaleZ
    spsz = sourcePlaneScaleZ
