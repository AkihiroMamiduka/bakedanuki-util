# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.game_fbx_exporter import AnimClipsField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class GameFbxExporter(DG):
    __slots__ = ()

    NODE_TYPE = "gameFbxExporter"

    presetName = DataStringField()
    pn = presetName

    overridePresetValue = LongField()
    opv = overridePresetValue

    isTheLastOneSelected = BoolField()
    ils = isTheLastOneSelected

    isTheLastOneUsed = BoolField()
    ilu = isTheLastOneUsed

    useFilenameAsPrefix = BoolField()
    ufp = useFilenameAsPrefix

    viewInFBXReview = BoolField()
    vfr = viewInFBXReview

    exportTypeIndex = LongField()
    eti = exportTypeIndex

    exportSetIndex = LongField()
    esi = exportSetIndex

    selectionSetName = DataStringField()
    ssn = selectionSetName

    modelFileMode = LongField()
    mfm = modelFileMode

    moveToOrigin = BoolField()
    mto = moveToOrigin

    smoothingGroups = BoolField()
    smg = smoothingGroups

    splitVertexNormals = BoolField()
    svn = splitVertexNormals

    tangentsBinormals = BoolField()
    tbi = tangentsBinormals

    smoothMesh = BoolField()
    smm = smoothMesh

    selectionSets = BoolField()
    sst = selectionSets

    convertToNullObj = BoolField()
    ctn = convertToNullObj

    preserveInstances = BoolField()
    pri = preserveInstances

    referencedAssetsContent = BoolField()
    rac = referencedAssetsContent

    triangulate = BoolField()
    tri = triangulate

    convertNurbsSurfaceTo = DataStringField()
    cns = convertNurbsSurfaceTo

    exportAnimation = BoolField()
    ean = exportAnimation

    useSceneName = BoolField()
    usn = useSceneName

    removeSingleKey = BoolField()
    rsk = removeSingleKey

    quarternionInterpMode = DataStringField()
    qim = quarternionInterpMode

    animClips = AnimClipsField(multi=True)
    ac = animClips

    fileSplitType = LongField()
    spt = fileSplitType

    includeCombinedClips = BoolField()
    icc = includeCombinedClips

    bakeAnimation = BoolField()
    ba = bakeAnimation

    bakeAnimStart = LongField()
    bas = bakeAnimStart

    bakeAnimEnd = LongField()
    bae = bakeAnimEnd

    bakeAnimStep = LongField()
    bst = bakeAnimStep

    resampleAll = BoolField()
    ral = resampleAll

    deformedModels = BoolField()
    dm = deformedModels

    skinning = BoolField()
    ski = skinning

    blendshapes = BoolField()
    bsh = blendshapes

    curveFilters = BoolField()
    cf = curveFilters

    constantKeyReducer = BoolField()
    ckr = constantKeyReducer

    ckrTranslationPrecision = FloatField()
    rtp = ckrTranslationPrecision

    ckrRotationPrecision = FloatField()
    rrp = ckrRotationPrecision

    ckrScalingPrecision = FloatField()
    rsp = ckrScalingPrecision

    ckrOtherPrecision = FloatField()
    rop = ckrOtherPrecision

    ckrAutoTangentOnly = BoolField()
    ato = ckrAutoTangentOnly

    constraints = BoolField()
    co = constraints

    skeletonDefinitions = BoolField()
    sd = skeletonDefinitions

    includeCameras = BoolField()
    ic = includeCameras

    includeLights = BoolField()
    li = includeLights

    upAxis = LongField()
    uax = upAxis

    embedMedia = BoolField()
    ebm = embedMedia

    includeChildren = BoolField()
    ich = includeChildren

    inputConnections = BoolField()
    inc = inputConnections

    autoScaleFactor = BoolField()
    asf = autoScaleFactor

    unitConversion = DataStringField()
    uc = unitConversion

    showWarningManager = BoolField()
    swm = showWarningManager

    generateLogData = BoolField()
    gld = generateLogData

    fileType = LongField()
    ft = fileType

    fileVersion = DataStringField()
    fv = fileVersion

    exportPath = DataStringField()
    exp = exportPath

    exportFilename = DataStringField()
    exf = exportFilename
