# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.rigid_body import (
    BoundingBoxField,
    CenterField,
    CenterOfMassField,
    ContactPositionField,
    DrawOverrideField,
    FieldDataField,
    ForceField,
    GeneralForceField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    ImpulseField,
    ImpulsePositionField,
    InitialOrientationField,
    InitialPositionField,
    InitialSpinField,
    InitialVelocityField,
    InstObjGroupsField,
    LastPositionField,
    LastRotationField,
    ObjectColorRGBField,
    OutlinerColorField,
    PublishedNodeInfoField,
    RenderInfoField,
    RenderLayerInfoField,
    SpinField,
    SpinImpulseField,
    TorqueField,
    VelocityField,
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
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


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


class StandInEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    CUBE = 1
    SPHERE = 2


class StandInEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    CUBE = 1
    SPHERE = 2

    NAME_MAP = {
        NONE: "none",
        CUBE: "cube",
        SPHERE: "sphere",
    }


class StandInEnumField(
    EnumField[StandInEnumAttrOperator, StandInEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StandInEnumAttrOperator
    PLUG_CLS = StandInEnumPlugOperator


class ApplyForceAtEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CENTEROFMASS = 0
    BOUNDINGBOX = 1
    VERTICESORCVS = 2


class ApplyForceAtEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CENTEROFMASS = 0
    BOUNDINGBOX = 1
    VERTICESORCVS = 2

    NAME_MAP = {
        CENTEROFMASS: "centerOfMass",
        BOUNDINGBOX: "boundingBox",
        VERTICESORCVS: "verticesOrCVs",
    }


class ApplyForceAtEnumField(
    EnumField[ApplyForceAtEnumAttrOperator, ApplyForceAtEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ApplyForceAtEnumAttrOperator
    PLUG_CLS = ApplyForceAtEnumPlugOperator


class RigidBody(Shape):
    __slots__ = ()

    NODE_TYPE = "rigidBody"

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

    currentTime = TimeField(default_value=0.0)
    ct = currentTime

    rigidWorldMatrix = DataMatrixField()
    rmx = rigidWorldMatrix

    inputGeometryMsg = MessageField(multi=True, readable=False)
    igm = inputGeometryMsg

    fieldConnections = MessageField(multi=True)
    fc = fieldConnections

    runUpCache = DataDoubleArrayField()
    rc = runUpCache

    dataCache = DataDoubleArrayField()
    dc = dataCache

    firstCachedFrame = LongField(default_value=0)
    fcf = firstCachedFrame

    lastCachedFrame = LongField(default_value=0)
    lcf = lastCachedFrame

    cachedFrameCount = LongField(default_value=0)
    cfc = cachedFrameCount

    cacheDirtyArray = TypedField()
    cda = cacheDirtyArray

    contactName = DataStringField(multi=True)
    cnn = contactName

    interpenetrateWith = MessageField(multi=True)
    itw = interpenetrateWith

    initialPosition = InitialPositionField(default_value=(0.0, 0.0, 0.0))
    ip = initialPosition
    initialPositionX = initialPosition.initialPositionX
    ipx = initialPositionX
    initialPositionY = initialPosition.initialPositionY
    ipy = initialPositionY
    initialPositionZ = initialPosition.initialPositionZ
    ipz = initialPositionZ

    lastPosition = LastPositionField(default_value=(0.0, 0.0, 0.0), writable=False)
    lp = lastPosition
    lastPositionX = lastPosition.lastPositionX
    lpx = lastPositionX
    lastPositionY = lastPosition.lastPositionY
    lpy = lastPositionY
    lastPositionZ = lastPosition.lastPositionZ
    lpz = lastPositionZ

    lastRotation = LastRotationField(default_value=(0.0, 0.0, 0.0), writable=False)
    lr = lastRotation
    lastRotationX = lastRotation.lastRotationX
    lrx = lastRotationX
    lastRotationY = lastRotation.lastRotationY
    lry = lastRotationY
    lastRotationZ = lastRotation.lastRotationZ
    lrz = lastRotationZ

    initialOrientation = InitialOrientationField(default_value=(0.0, 0.0, 0.0))
    ior = initialOrientation
    initialOrientationX = initialOrientation.initialOrientationX
    iox = initialOrientationX
    initialOrientationY = initialOrientation.initialOrientationY
    ioy = initialOrientationY
    initialOrientationZ = initialOrientation.initialOrientationZ
    ioz = initialOrientationZ

    initialVelocity = InitialVelocityField(default_value=(0.0, 0.0, 0.0))
    iv = initialVelocity
    initialVelocityX = initialVelocity.initialVelocityX
    ivx = initialVelocityX
    initialVelocityY = initialVelocity.initialVelocityY
    ivy = initialVelocityY
    initialVelocityZ = initialVelocity.initialVelocityZ
    ivz = initialVelocityZ

    initialSpin = InitialSpinField(default_value=(0.0, 0.0, 0.0))
    is_ = initialSpin
    initialSpinX = initialSpin.initialSpinX
    isx = initialSpinX
    initialSpinY = initialSpin.initialSpinY
    isy = initialSpinY
    initialSpinZ = initialSpin.initialSpinZ
    isz = initialSpinZ

    centerOfMass = CenterOfMassField(default_value=(0.0, 0.0, 0.0))
    com = centerOfMass
    centerOfMassX = centerOfMass.centerOfMassX
    cmx = centerOfMassX
    centerOfMassY = centerOfMass.centerOfMassY
    cmy = centerOfMassY
    centerOfMassZ = centerOfMass.centerOfMassZ
    cmz = centerOfMassZ

    impulse = ImpulseField(default_value=(0.0, 0.0, 0.0))
    imp = impulse
    impulseX = impulse.impulseX
    imx = impulseX
    impulseY = impulse.impulseY
    imy = impulseY
    impulseZ = impulse.impulseZ
    imz = impulseZ

    impulsePosition = ImpulsePositionField(default_value=(0.0, 0.0, 0.0))
    ipo = impulsePosition
    impulsePositionX = impulsePosition.impulsePositionX
    pix = impulsePositionX
    impulsePositionY = impulsePosition.impulsePositionY
    piy = impulsePositionY
    impulsePositionZ = impulsePosition.impulsePositionZ
    piz = impulsePositionZ

    spinImpulse = SpinImpulseField(default_value=(0.0, 0.0, 0.0))
    sim = spinImpulse
    spinImpulseX = spinImpulse.spinImpulseX
    six = spinImpulseX
    spinImpulseY = spinImpulse.spinImpulseY
    siy = spinImpulseY
    spinImpulseZ = spinImpulse.spinImpulseZ
    siz = spinImpulseZ

    mass = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=100.0)
    mas = mass

    volume = DoubleField(default_value=0.0, writable=False)
    vol = volume

    bounciness = DoubleField(default_value=0.6, min_value=0.0, soft_max_value=2.0)
    b = bounciness

    damping = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dp = damping

    staticFriction = DoubleField(default_value=0.2, min_value=0.0, soft_max_value=1.0)
    sf = staticFriction

    dynamicFriction = DoubleField(default_value=0.2, min_value=0.0, soft_max_value=1.0)
    df = dynamicFriction

    collisionLayer = LongField(default_value=0, min_value=-1, soft_max_value=10)
    cl = collisionLayer

    standIn = StandInEnumField(default_value=0)
    si = standIn

    inputGeometryCnt = LongField(default_value=0)
    igc = inputGeometryCnt

    active = BoolField(default_value=True)
    act = active

    choice = LongField(default_value=0)
    chc = choice

    isKinematic = BoolField(default_value=False)
    kin = isKinematic

    isKeyframed = BoolField(default_value=False)
    key = isKeyframed

    isParented = BoolField(default_value=False)
    par = isParented

    particleCollision = BoolField(default_value=False)
    pc = particleCollision

    autoInit = BoolField(default_value=True)
    ai = autoInit

    allowDisconnection = BoolField(default_value=False)
    ad = allowDisconnection

    cacheData = BoolField(default_value=False)
    idc = cacheData

    tessellationFactor = LongField(default_value=200, min_value=10, soft_max_value=500)
    tes = tessellationFactor

    velocity = VelocityField(default_value=(0.0, 0.0, 0.0), writable=False)
    vel = velocity
    velocityX = velocity.velocityX
    vx = velocityX
    velocityY = velocity.velocityY
    vy = velocityY
    velocityZ = velocity.velocityZ
    vz = velocityZ

    spin = SpinField(default_value=(0.0, 0.0, 0.0), writable=False)
    sp = spin
    spinX = spin.spinX
    spx = spinX
    spinY = spin.spinY
    spy = spinY
    spinZ = spin.spinZ
    spz = spinZ

    contactCount = LongField(default_value=0, writable=False)
    cct = contactCount

    contactPosition = ContactPositionField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    cnp = contactPosition

    force = ForceField(default_value=(0.0, 0.0, 0.0), writable=False)
    for_ = force
    forceX = force.forceX
    fx = forceX
    forceY = force.forceY
    fy = forceY
    forceZ = force.forceZ
    fz = forceZ

    torque = TorqueField(default_value=(0.0, 0.0, 0.0), writable=False)
    tor = torque
    torqueX = torque.torqueX
    trx = torqueX
    torqueY = torque.torqueY
    try_ = torqueY
    torqueZ = torque.torqueZ
    trz = torqueZ

    lastSceneTime = TimeField(default_value=0.0)
    lst = lastSceneTime

    fieldData = FieldDataField()
    fld = fieldData
    fieldDataPosition = fieldData.fieldDataPosition
    fdp = fieldDataPosition
    fieldDataVelocity = fieldData.fieldDataVelocity
    fdv = fieldDataVelocity
    fieldDataMass = fieldData.fieldDataMass
    fdm = fieldDataMass
    deltaTime = fieldData.deltaTime
    dt = deltaTime

    inputForce = DataVectorArrayField(multi=True)
    ifr = inputForce

    inputForceType = BoolField(multi=True, default_value=False)
    ift = inputForceType

    collisionRecords = TypedField(multi=True)
    crc = collisionRecords

    generalForce = GeneralForceField()
    gfr = generalForce
    outputForce = generalForce.outputForce
    ofr = outputForce
    outputTorque = generalForce.outputTorque
    otr = outputTorque

    solverId = LongField(default_value=-1)
    sid = solverId

    bakeSimulationIndex = LongField(default_value=-1)
    bsi = bakeSimulationIndex

    shapeChanged = LongField(default_value=0, writable=False)
    sc = shapeChanged

    lockCenterOfMass = BoolField(default_value=False)
    lcm = lockCenterOfMass

    ignore = BoolField(default_value=False)
    ign = ignore

    collisions = BoolField(default_value=True)
    col = collisions

    applyForceAt = ApplyForceAtEnumField(default_value=1)
    afa = applyForceAt

    debugDraw = BoolField(default_value=False)
    dd = debugDraw
