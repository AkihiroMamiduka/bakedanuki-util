# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.particle import (
    CachedWorldCentroidField,
    CentroidField,
    CollisionDataField,
    CompInstObjGroupsField,
    ComponentTagsField,
    EmitterDataField,
    EventRandStateField,
    FieldDataField,
    IdMappingField,
    InstanceDataField,
    RandStateField,
    WorldCentroidField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.generic import GenericField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.double_array import DataDoubleArrayField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.string import DataStringField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class LifespanModeEnumPlugOperator(
    EnumPlugOperator["LifespanModeEnumAttrOperator"]
):
    __slots__ = ()

    LIVE_FOREVER = 0
    CONSTANT = 1
    RANDOM_RANGE = 2
    LIFESPANPP_ONLY = 3


class LifespanModeEnumAttrOperator(
    EnumAttrOperator[LifespanModeEnumPlugOperator]
):
    __slots__ = ()

    LIVE_FOREVER = 0
    CONSTANT = 1
    RANDOM_RANGE = 2
    LIFESPANPP_ONLY = 3

    NAME_MAP = {
        LIVE_FOREVER: "Live forever",
        CONSTANT: "Constant",
        RANDOM_RANGE: "Random range",
        LIFESPANPP_ONLY: "lifespanPP only",
    }


class LifespanModeEnumField(
    EnumField[LifespanModeEnumAttrOperator, LifespanModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LifespanModeEnumAttrOperator
    PLUG_CLS = LifespanModeEnumPlugOperator


class InputGeometrySpaceEnumPlugOperator(
    EnumPlugOperator["InputGeometrySpaceEnumAttrOperator"]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2


class InputGeometrySpaceEnumAttrOperator(
    EnumAttrOperator[InputGeometrySpaceEnumPlugOperator]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2

    NAME_MAP = {
        GEOMETRY_LOCAL: "Geometry Local",
        WORLD: "World",
        PARTICLE_LOCAL: "Particle Local",
    }


class InputGeometrySpaceEnumField(
    EnumField[
        InputGeometrySpaceEnumAttrOperator, InputGeometrySpaceEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputGeometrySpaceEnumAttrOperator
    PLUG_CLS = InputGeometrySpaceEnumPlugOperator


class TargetGeometrySpaceEnumPlugOperator(
    EnumPlugOperator["TargetGeometrySpaceEnumAttrOperator"]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2


class TargetGeometrySpaceEnumAttrOperator(
    EnumAttrOperator[TargetGeometrySpaceEnumPlugOperator]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2

    NAME_MAP = {
        GEOMETRY_LOCAL: "Geometry Local",
        WORLD: "World",
        PARTICLE_LOCAL: "Particle Local",
    }


class TargetGeometrySpaceEnumField(
    EnumField[
        TargetGeometrySpaceEnumAttrOperator,
        TargetGeometrySpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TargetGeometrySpaceEnumAttrOperator
    PLUG_CLS = TargetGeometrySpaceEnumPlugOperator


class ParticleRenderTypeEnumPlugOperator(
    EnumPlugOperator["ParticleRenderTypeEnumAttrOperator"]
):
    __slots__ = ()

    MULTIPOINT = 0
    MULTISTREAK = 1
    NUMERIC = 2
    POINTS = 3
    SPHERES = 4
    SPRITES = 5
    STREAK = 6
    BLOBBY_SURFACE_S_SLASH_W = 7
    CLOUD_S_SLASH_W = 8
    TUBE_S_SLASH_W = 9


class ParticleRenderTypeEnumAttrOperator(
    EnumAttrOperator[ParticleRenderTypeEnumPlugOperator]
):
    __slots__ = ()

    MULTIPOINT = 0
    MULTISTREAK = 1
    NUMERIC = 2
    POINTS = 3
    SPHERES = 4
    SPRITES = 5
    STREAK = 6
    BLOBBY_SURFACE_S_SLASH_W = 7
    CLOUD_S_SLASH_W = 8
    TUBE_S_SLASH_W = 9

    NAME_MAP = {
        MULTIPOINT: "MultiPoint",
        MULTISTREAK: "MultiStreak",
        NUMERIC: "Numeric",
        POINTS: "Points",
        SPHERES: "Spheres",
        SPRITES: "Sprites",
        STREAK: "Streak",
        BLOBBY_SURFACE_S_SLASH_W: "Blobby Surface (s/w)",
        CLOUD_S_SLASH_W: "Cloud (s/w)",
        TUBE_S_SLASH_W: "Tube (s/w)",
    }


class ParticleRenderTypeEnumField(
    EnumField[
        ParticleRenderTypeEnumAttrOperator, ParticleRenderTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleRenderTypeEnumAttrOperator
    PLUG_CLS = ParticleRenderTypeEnumPlugOperator


class AiRenderPointsAsEnumPlugOperator(
    EnumPlugOperator["AiRenderPointsAsEnumAttrOperator"]
):
    __slots__ = ()

    POINTS = 0
    SPHERES = 1
    QUADS = 2


class AiRenderPointsAsEnumAttrOperator(
    EnumAttrOperator[AiRenderPointsAsEnumPlugOperator]
):
    __slots__ = ()

    POINTS = 0
    SPHERES = 1
    QUADS = 2

    NAME_MAP = {
        POINTS: "points",
        SPHERES: "spheres",
        QUADS: "quads",
    }


class AiRenderPointsAsEnumField(
    EnumField[
        AiRenderPointsAsEnumAttrOperator, AiRenderPointsAsEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiRenderPointsAsEnumAttrOperator
    PLUG_CLS = AiRenderPointsAsEnumPlugOperator


class GeneratedParticle(Shape):
    __slots__ = ()

    NODE_TYPE = "particle"

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

    position = DataVectorArrayField()
    pos = position

    rampPosition = DataVectorArrayField()
    rps = rampPosition

    centroid = CentroidField(default_value=(0.0, 0.0, 0.0), writable=False)
    ctd = centroid
    centroidX = centroid.centroidX
    ctdx = centroidX
    centroidY = centroid.centroidY
    ctdy = centroidY
    centroidZ = centroid.centroidZ
    ctdz = centroidZ

    lastPosition = DataVectorArrayField(writable=False)
    lpos = lastPosition

    velocity = DataVectorArrayField()
    vel = velocity

    rampVelocity = DataVectorArrayField()
    rvl = rampVelocity

    lastVelocity = DataVectorArrayField(writable=False)
    lvel = lastVelocity

    acceleration = DataVectorArrayField()
    acc = acceleration

    rampAcceleration = DataVectorArrayField()
    rac = rampAcceleration

    force = DataVectorArrayField(writable=False)
    frc = force

    inputForce = DataVectorArrayField(multi=True)
    ifc = inputForce

    worldPosition = DataVectorArrayField(writable=False)
    wps = worldPosition

    worldCentroid = WorldCentroidField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    wctn = worldCentroid
    worldCentroidX = worldCentroid.worldCentroidX
    wctx = worldCentroidX
    worldCentroidY = worldCentroid.worldCentroidY
    wcty = worldCentroidY
    worldCentroidZ = worldCentroid.worldCentroidZ
    wctz = worldCentroidZ

    lastWorldPosition = DataVectorArrayField(writable=False)
    lwps = lastWorldPosition

    worldVelocity = DataVectorArrayField(writable=False)
    wvl = worldVelocity

    worldVelocityInObjectSpace = DataVectorArrayField()
    wvo = worldVelocityInObjectSpace

    lastWorldVelocity = DataVectorArrayField(writable=False)
    lwvl = lastWorldVelocity

    lastWorldMatrix = DataMatrixField(writable=False)
    lwm = lastWorldMatrix

    position0 = DataVectorArrayField()
    pos0 = position0

    velocity0 = DataVectorArrayField()
    vel0 = velocity0

    acceleration0 = DataVectorArrayField()
    acc0 = acceleration0

    emitterId0 = DataDoubleArrayField(writable=False)
    eid0 = emitterId0

    useStartupCache = BoolField(default_value=False)
    usc = useStartupCache

    startupCachePath = DataStringField()
    scp = startupCachePath

    startupCacheFrame = LongField(default_value=0)
    scf = startupCacheFrame

    cachedPosition = DataVectorArrayField(writable=False)
    cpos = cachedPosition

    lastCachedPosition = DataVectorArrayField(writable=False)
    lcps = lastCachedPosition

    cachedWorldPosition = DataVectorArrayField(writable=False)
    cwps = cachedWorldPosition

    cachedWorldCentroid = CachedWorldCentroidField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cwcn = cachedWorldCentroid
    cachedWorldCentroidX = cachedWorldCentroid.cachedWorldCentroidX
    cwcx = cachedWorldCentroidX
    cachedWorldCentroidY = cachedWorldCentroid.cachedWorldCentroidY
    cwcy = cachedWorldCentroidY
    cachedWorldCentroidZ = cachedWorldCentroid.cachedWorldCentroidZ
    cwcz = cachedWorldCentroidZ

    cachedVelocity = DataVectorArrayField(writable=False)
    cvel = cachedVelocity

    cachedWorldVelocity = DataVectorArrayField(writable=False)
    cwvl = cachedWorldVelocity

    count = LongField(default_value=0, writable=False)
    cnt = count

    computingCount = BoolField(default_value=False)
    cmp = computingCount

    mass = DataDoubleArrayField()
    mas = mass

    mass0 = DataDoubleArrayField()
    mas0 = mass0

    massCache = DataDoubleArrayField(writable=False)
    masc = massCache

    particleId = DataDoubleArrayField(writable=False)
    id = particleId

    particleId0 = DataDoubleArrayField()
    id0 = particleId0

    idCache = DataDoubleArrayField(writable=False)
    idc = idCache

    idMapping = IdMappingField(writable=False)
    idm = idMapping
    sortedId = idMapping.sortedId
    sid = sortedId
    idIndex = idMapping.idIndex
    idix = idIndex

    nextId = LongField(default_value=0)
    nid = nextId

    nextId0 = LongField(default_value=0)
    nid0 = nextId0

    birthTime = DataDoubleArrayField(writable=False)
    bt = birthTime

    birthTime0 = DataDoubleArrayField()
    bt0 = birthTime0

    birthTimeCache = DataDoubleArrayField()
    btc = birthTimeCache

    age = DataDoubleArrayField(writable=False)
    ag = age

    age0 = DataDoubleArrayField()
    ag0 = age0

    ageCache = DataDoubleArrayField(writable=False)
    agc = ageCache

    emission = TypedField(writable=False)
    emt = emission

    emitterId = DataDoubleArrayField(writable=False)
    eid = emitterId

    dieOnEmissionVolumeExit = BoolField(default_value=False)
    dve = dieOnEmissionVolumeExit

    isFull = BoolField(default_value=False, writable=False)
    ifl = isFull

    newParticles = TypedField(multi=True, readable=False)
    npt = newParticles

    collisionEvents = BoolField(
        default_value=False, readable=False, writable=False
    )
    cev = collisionEvents

    death = BoolField(default_value=False, readable=False, writable=False)
    dth = death

    lifespanMode = LifespanModeEnumField(default_value=0)
    lfm = lifespanMode

    lifespanRandom = DoubleField(default_value=0.0)
    lfr = lifespanRandom

    finalLifespanPP = DataDoubleArrayField(writable=False)
    flp = finalLifespanPP

    generalSeed = LongField(default_value=0)
    gsd = generalSeed

    randState = RandStateField(default_value=(0, 0, 0))
    rnst = randState
    randStateX = randState.randStateX
    rstx = randStateX
    randStateY = randState.randStateY
    rsty = randStateY
    randStateZ = randState.randStateZ
    rstz = randStateZ

    expressionsAfterDynamics = BoolField(default_value=False)
    ead = expressionsAfterDynamics

    executeCreationExpression = BoolField(
        default_value=False, readable=False, writable=False
    )
    ece = executeCreationExpression

    executeRuntimeBeforeDynamicsExpression = BoolField(
        default_value=False, readable=False, writable=False
    )
    erbe = executeRuntimeBeforeDynamicsExpression

    executeRuntimeAfterDynamicsExpression = BoolField(
        default_value=False, readable=False, writable=False
    )
    erae = executeRuntimeAfterDynamicsExpression

    input = GenericField(multi=True)
    xi = input

    output = GenericField(multi=True, writable=False)
    xo = output

    time = TimeField(default_value=0.0, readable=False)
    tim = time

    frame = TimeField(default_value=0.0, readable=False)
    frm = frame

    internalRuntimeExpression = DataStringField()
    irx = internalRuntimeExpression

    internalRuntimeBeforeDynamicsExpression = DataStringField()
    irbx = internalRuntimeBeforeDynamicsExpression

    internalRuntimeAfterDynamicsExpression = DataStringField()
    irax = internalRuntimeAfterDynamicsExpression

    internalCreationExpression = DataStringField()
    icx = internalCreationExpression

    currentParticle = LongField(
        default_value=0, readable=False, writable=False
    )
    xcp = currentParticle

    diedLastTime = LongField(default_value=0)
    dlt = diedLastTime

    netEmittedLastTime = LongField(default_value=0)
    nlt = netEmittedLastTime

    startEmittedIndex = LongField(default_value=-1)
    sei = startEmittedIndex

    isDynamic = BoolField(default_value=True)
    isd = isDynamic

    dynamicsWeight = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    dw = dynamicsWeight

    forcesInWorld = BoolField(default_value=True)
    fiw = forcesInWorld

    conserve = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    con = conserve

    emissionInWorld = BoolField(default_value=True)
    eiw = emissionInWorld

    maxCount = LongField(default_value=-1)
    mxc = maxCount

    levelOfDetail = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    lod = levelOfDetail

    inheritFactor = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    inh = inheritFactor

    seed = LongField(multi=True, default_value=1)
    sd = seed

    fieldData = FieldDataField(writable=False)
    fd = fieldData
    fieldDataPosition = fieldData.fieldDataPosition
    fdp = fieldDataPosition
    fieldDataVelocity = fieldData.fieldDataVelocity
    fdv = fieldDataVelocity
    fieldDataMass = fieldData.fieldDataMass
    fdm = fieldDataMass
    fieldDataDeltaTime = fieldData.fieldDataDeltaTime
    fdt = fieldDataDeltaTime

    emitterData = EmitterDataField(writable=False)
    ed = emitterData
    emitterDataPosition = emitterData.emitterDataPosition
    edp = emitterDataPosition
    emitterDataVelocity = emitterData.emitterDataVelocity
    edv = emitterDataVelocity
    emitterDataDeltaTime = emitterData.emitterDataDeltaTime
    edt = emitterDataDeltaTime

    forceDynamics = BoolField(
        default_value=False, readable=False, writable=False
    )
    fdn = forceDynamics

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    currentTimeSave = TimeField(default_value=0.0)
    cts = currentTimeSave

    evaluationTime = TimeField(default_value=0.0)
    eti = evaluationTime

    currentSceneTime = TimeField(default_value=1.0)
    cst = currentSceneTime

    lastTimeEvaluated = TimeField(default_value=0.0, writable=False)
    lti = lastTimeEvaluated

    lastSceneTime = TimeField(default_value=0.0)
    lst = lastSceneTime

    cachedTime = TimeField(default_value=0.0, writable=False)
    chti = cachedTime

    timeStepSize = TimeField(default_value=0.0, writable=False)
    tss = timeStepSize

    sceneTimeStepSize = TimeField(default_value=0.0, writable=False)
    sts = sceneTimeStepSize

    startFrame = DoubleField(default_value=1.0)
    stf = startFrame

    startTime = TimeField(default_value=0.0, writable=False)
    stt = startTime

    inputGeometry = GenericField()
    igeo = inputGeometry

    inputGeometryPoints = DataVectorArrayField(writable=False)
    igpt = inputGeometryPoints

    inputGeometrySpace = InputGeometrySpaceEnumField(default_value=0)
    igs = inputGeometrySpace

    enforceCountFromHistory = BoolField(default_value=True)
    ecfh = enforceCountFromHistory

    targetGeometry = GenericField(writable=False)
    tgeo = targetGeometry

    targetGeometryWorldMatrix = DataMatrixField()
    tgm = targetGeometryWorldMatrix

    targetGeometrySpace = TargetGeometrySpaceEnumField(default_value=2)
    tgs = targetGeometrySpace

    goalSmoothness = DoubleField(
        default_value=3.0, min_value=0.0, soft_max_value=10.0
    )
    gsm = goalSmoothness

    goalGeometry = GenericField(multi=True)
    ggeo = goalGeometry

    goalWeight = DoubleField(
        multi=True,
        default_value=0.0,
        min_value=0.0,
        max_value=1.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    gw = goalWeight

    goalActive = BoolField(multi=True, default_value=True)
    ga = goalActive

    goalUvSetName = DataStringField(multi=True)
    guv = goalUvSetName

    cacheData = BoolField(default_value=False)
    chd = cacheData

    cacheWidth = LongField(default_value=1)
    chw = cacheWidth

    collisions = BoolField(default_value=False, readable=False, writable=False)
    col = collisions

    traceDepth = LongField(default_value=10, min_value=0)
    trd = traceDepth

    collisionData = CollisionDataField()
    cda = collisionData
    collisionGeometry = collisionData.collisionGeometry
    cge = collisionGeometry
    collisionResilience = collisionData.collisionResilience
    crs = collisionResilience
    collisionFriction = collisionData.collisionFriction
    cfr = collisionFriction
    collisionOffset = collisionData.collisionOffset
    cof = collisionOffset

    collisionRecords = TypedField(writable=False)
    crc = collisionRecords

    totalEventCount = LongField(default_value=0, writable=False)
    tec = totalEventCount

    eventTest = BoolField(default_value=False, writable=False)
    evt = eventTest

    lastTotalEventCount = LongField(default_value=0)
    ltec = lastTotalEventCount

    eventSeed = LongField(default_value=0)
    esd = eventSeed

    eventRandState = EventRandStateField(default_value=(0, 0, 0))
    erst = eventRandState
    eventRandStateX = eventRandState.eventRandStateX
    ersx = eventRandStateX
    eventRandStateY = eventRandState.eventRandStateY
    ersy = eventRandStateY
    eventRandStateZ = eventRandState.eventRandStateZ
    ersz = eventRandStateZ

    eventTarget = MessageField(multi=True)
    etg = eventTarget

    eventName = DataStringField(multi=True)
    evn = eventName

    eventValid = LongField(multi=True, default_value=-1)
    evv = eventValid

    eventCount = ShortField(multi=True, default_value=-1)
    ecp = eventCount

    eventEmit = ShortField(multi=True, default_value=-1)
    eve = eventEmit

    eventSplit = ShortField(multi=True, default_value=-1)
    evs = eventSplit

    eventDie = ShortField(multi=True, default_value=-1)
    evd = eventDie

    eventRandom = ShortField(multi=True, default_value=-1)
    evr = eventRandom

    eventSpread = DoubleField(multi=True, default_value=-1.0)
    esp = eventSpread

    eventProc = DataStringField(multi=True)
    epr = eventProc

    instanceData = InstanceDataField(multi=True)
    idt = instanceData

    debugDraw = ShortField(default_value=0)
    dbd = debugDraw

    numberOfEvents = ShortField(default_value=0)
    nev = numberOfEvents

    eventNameCount = ShortField(default_value=0)
    enc = eventNameCount

    fieldConnections = MessageField(multi=True)
    fc = fieldConnections

    collisionConnections = MessageField(multi=True)
    cc = collisionConnections

    connectionsToMe = MessageField(multi=True)
    ct = connectionsToMe

    auxiliariesOwned = MessageField()
    ao = auxiliariesOwned

    emitterConnections = MessageField(multi=True)
    ec = emitterConnections

    inheritColor = BoolField(default_value=False)
    inc = inheritColor

    shapeNameMsg = MessageField()
    snmg = shapeNameMsg

    doDynamics = BoolField(default_value=False)
    ddy = doDynamics

    doEmission = BoolField(default_value=False)
    dem = doEmission

    forceEmission = BoolField(default_value=False)
    fem = forceEmission

    doAge = BoolField(default_value=False)
    dag = doAge

    agesLastDone = DoubleField(default_value=0.0)
    agld = agesLastDone

    timeLastComputed = DoubleField(default_value=0.0)
    tlc = timeLastComputed

    parentMatrixDirty = BoolField(default_value=False)
    pmd = parentMatrixDirty

    newFileFormat = ShortField(default_value=0)
    nff = newFileFormat

    depthSort = BoolField(default_value=False)
    ds = depthSort

    particleRenderType = ParticleRenderTypeEnumField(default_value=3)
    prt = particleRenderType

    disableCloudAxis = BoolField(default_value=False)
    dca = disableCloudAxis

    normalizeVelocity = BoolField(default_value=False)
    nvl = normalizeVelocity

    samplerPerParticleData = TypedField(writable=False)
    spd = samplerPerParticleData

    ppFieldData = TypedField(multi=True, writable=False)
    ppfd = ppFieldData

    ownerPPFieldData = TypedField(multi=True, writable=False)
    opfd = ownerPPFieldData

    deformedPosition = GenericField()
    dpos = deformedPosition

    useCustomCache = BoolField(default_value=False)
    ucc = useCustomCache

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiSelfShadows = BoolField(default_value=True, category="arnold")
    ai_self_shadows = aiSelfShadows

    aiOpaque = BoolField(default_value=True, category="arnold")
    ai_opaque = aiOpaque

    aiMatte = BoolField(default_value=False, category="arnold")
    ai_matte = aiMatte

    aiTraceSets = DataStringField(category="arnold")
    trace_sets = aiTraceSets

    aiSssSetname = DataStringField(category="arnold")
    ai_sss_setname = aiSssSetname

    aiToonId = DataStringField(category="arnold")
    ai_toon_id = aiToonId

    aiVisibleInDiffuseReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    aiExportParticleIDs = BoolField(default_value=False, category="arnold")
    ai_export_particle_ids = aiExportParticleIDs

    aiExportAttributes = DataStringField(category="arnold")
    ai_export_attributes = aiExportAttributes

    aiRenderPointsAs = AiRenderPointsAsEnumField(
        default_value=0, category="arnold"
    )
    ai_render_points_as = aiRenderPointsAs

    aiMinParticleRadius = FloatField(default_value=0.0, category="arnold")
    ai_min_particle_radius = aiMinParticleRadius

    aiRadiusMultiplier = FloatField(default_value=1.0, category="arnold")
    ai_radius_multiplier = aiRadiusMultiplier

    aiMaxParticleRadius = FloatField(
        default_value=1000000.0, category="arnold"
    )
    ai_max_particle_radius = aiMaxParticleRadius

    aiMinPixelWidth = FloatField(default_value=0.0, category="arnold")
    ai_min_pixel_width = aiMinPixelWidth

    aiFalloffExponent = FloatField(default_value=0.0, category="arnold")
    ai_falloff_exponent = aiFalloffExponent

    aiSmoothStepFalloff = BoolField(default_value=True, category="arnold")
    ai_smooth_step_falloff = aiSmoothStepFalloff

    aiImplicitSamples = LongField(
        default_value=10, min_value=1, category="arnold"
    )
    ai_implicit_samples = aiImplicitSamples

    aiStepSize = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=2.0, category="arnold"
    )
    ai_step_size = aiStepSize

    aiStepScale = FloatField(
        default_value=1.0,
        min_value=0.0,
        soft_max_value=10.0,
        category="arnold",
    )
    ai_step_scale = aiStepScale

    aiDeleteDeadParticles = BoolField(default_value=False, category="arnold")
    ai_delete_dead_particles = aiDeleteDeadParticles

    aiInterpolateBlur = BoolField(default_value=True, category="arnold")
    ai_interpolate_blur = aiInterpolateBlur

    aiEvaluateEvery = FloatField(
        default_value=1.0,
        min_value=9.999999747378752e-05,
        soft_min_value=0.10000000149011612,
        soft_max_value=2.0,
        category="arnold",
    )
    ai_evaluate_every = aiEvaluateEvery
