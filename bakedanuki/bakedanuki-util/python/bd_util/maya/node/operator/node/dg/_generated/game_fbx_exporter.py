# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.game_fbx_exporter import AnimClipsField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedGameFbxExporter(DG):
    __slots__ = ()

    NODE_TYPE = "gameFbxExporter"

    presetName = DataStringField()
    pn = presetName

    overridePresetValue = LongField(default_value=0)
    opv = overridePresetValue

    isTheLastOneSelected = BoolField(default_value=False)
    ils = isTheLastOneSelected

    isTheLastOneUsed = BoolField(default_value=False)
    ilu = isTheLastOneUsed

    useFilenameAsPrefix = BoolField(default_value=True)
    ufp = useFilenameAsPrefix

    viewInFBXReview = BoolField(default_value=False)
    vfr = viewInFBXReview

    exportTypeIndex = LongField(default_value=1)
    eti = exportTypeIndex

    exportSetIndex = LongField(default_value=1)
    esi = exportSetIndex

    selectionSetName = DataStringField()
    ssn = selectionSetName

    modelFileMode = LongField(default_value=1)
    mfm = modelFileMode

    moveToOrigin = BoolField(default_value=False)
    mto = moveToOrigin

    smoothingGroups = BoolField(default_value=True)
    smg = smoothingGroups

    splitVertexNormals = BoolField(default_value=False)
    svn = splitVertexNormals

    tangentsBinormals = BoolField(default_value=True)
    tbi = tangentsBinormals

    smoothMesh = BoolField(default_value=False)
    smm = smoothMesh

    selectionSets = BoolField(default_value=False)
    sst = selectionSets

    convertToNullObj = BoolField(default_value=False)
    ctn = convertToNullObj

    preserveInstances = BoolField(default_value=False)
    pri = preserveInstances

    referencedAssetsContent = BoolField(default_value=False)
    rac = referencedAssetsContent

    triangulate = BoolField(default_value=False)
    tri = triangulate

    convertNurbsSurfaceTo = DataStringField()
    cns = convertNurbsSurfaceTo

    exportAnimation = BoolField(default_value=False)
    ean = exportAnimation

    useSceneName = BoolField(default_value=False)
    usn = useSceneName

    removeSingleKey = BoolField(default_value=False)
    rsk = removeSingleKey

    quarternionInterpMode = DataStringField()
    qim = quarternionInterpMode

    animClips = AnimClipsField(multi=True)
    ac = animClips

    fileSplitType = LongField(default_value=1)
    spt = fileSplitType

    includeCombinedClips = BoolField(default_value=False)
    icc = includeCombinedClips

    bakeAnimation = BoolField(default_value=True)
    ba = bakeAnimation

    bakeAnimStart = LongField(default_value=0)
    bas = bakeAnimStart

    bakeAnimEnd = LongField(default_value=0)
    bae = bakeAnimEnd

    bakeAnimStep = LongField(default_value=0)
    bst = bakeAnimStep

    resampleAll = BoolField(default_value=False)
    ral = resampleAll

    deformedModels = BoolField(default_value=False)
    dm = deformedModels

    skinning = BoolField(default_value=True)
    ski = skinning

    blendshapes = BoolField(default_value=True)
    bsh = blendshapes

    curveFilters = BoolField(default_value=False)
    cf = curveFilters

    constantKeyReducer = BoolField(default_value=False)
    ckr = constantKeyReducer

    ckrTranslationPrecision = FloatField(default_value=0.0)
    rtp = ckrTranslationPrecision

    ckrRotationPrecision = FloatField(default_value=0.0)
    rrp = ckrRotationPrecision

    ckrScalingPrecision = FloatField(default_value=0.0)
    rsp = ckrScalingPrecision

    ckrOtherPrecision = FloatField(default_value=0.0)
    rop = ckrOtherPrecision

    ckrAutoTangentOnly = BoolField(default_value=False)
    ato = ckrAutoTangentOnly

    constraints = BoolField(default_value=False)
    co = constraints

    skeletonDefinitions = BoolField(default_value=False)
    sd = skeletonDefinitions

    includeCameras = BoolField(default_value=True)
    ic = includeCameras

    includeLights = BoolField(default_value=True)
    li = includeLights

    upAxis = LongField(default_value=1)
    uax = upAxis

    embedMedia = BoolField(default_value=False)
    ebm = embedMedia

    includeChildren = BoolField(default_value=False)
    ich = includeChildren

    inputConnections = BoolField(default_value=False)
    inc = inputConnections

    autoScaleFactor = BoolField(default_value=False)
    asf = autoScaleFactor

    unitConversion = DataStringField()
    uc = unitConversion

    showWarningManager = BoolField(default_value=False)
    swm = showWarningManager

    generateLogData = BoolField(default_value=False)
    gld = generateLogData

    fileType = LongField(default_value=0)
    ft = fileType

    fileVersion = DataStringField()
    fv = fileVersion

    exportPath = DataStringField()
    exp = exportPath

    exportFilename = DataStringField()
    exf = exportFilename
