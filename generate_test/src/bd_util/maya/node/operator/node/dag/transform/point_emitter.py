# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.point_emitter import (
    DirectionField,
    OwnerCentroidField,
    ParticleColorField,
    RandStateField,
    TextureRateField,
    VolumeOffsetField,
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
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class EmitterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DIRECTIONAL = 0
    OMNI = 1
    SURFACE = 2
    CURVE = 3
    VOLUME = 4


class EmitterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DIRECTIONAL = 0
    OMNI = 1
    SURFACE = 2
    CURVE = 3
    VOLUME = 4

    NAME_MAP = {
        DIRECTIONAL: "Directional",
        OMNI: "Omni",
        SURFACE: "Surface",
        CURVE: "Curve",
        VOLUME: "Volume",
    }


class EmitterTypeEnumField(
    EnumField[EmitterTypeEnumAttrOperator, EmitterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmitterTypeEnumAttrOperator
    PLUG_CLS = EmitterTypeEnumPlugOperator


class CycleEmissionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE_TIMERANDOM_OFF = 0
    FRAME_TIMERANDOM_ON = 1


class CycleEmissionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE_TIMERANDOM_OFF = 0
    FRAME_TIMERANDOM_ON = 1

    NAME_MAP = {
        NONE_TIMERANDOM_OFF: "None (timeRandom off)",
        FRAME_TIMERANDOM_ON: "Frame (timeRandom on)",
    }


class CycleEmissionEnumField(
    EnumField[CycleEmissionEnumAttrOperator, CycleEmissionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CycleEmissionEnumAttrOperator
    PLUG_CLS = CycleEmissionEnumPlugOperator


class VolumeShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CUBE = 0
    SPHERE = 1
    CYLINDER = 2
    CONE = 3
    TORUS = 4


class VolumeShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CUBE = 0
    SPHERE = 1
    CYLINDER = 2
    CONE = 3
    TORUS = 4

    NAME_MAP = {
        CUBE: "Cube",
        SPHERE: "Sphere",
        CYLINDER: "Cylinder",
        CONE: "Cone",
        TORUS: "Torus",
    }


class VolumeShapeEnumField(
    EnumField[VolumeShapeEnumAttrOperator, VolumeShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeShapeEnumAttrOperator
    PLUG_CLS = VolumeShapeEnumPlugOperator


class PointEmitter(Transform):
    __slots__ = ()

    NODE_TYPE = "pointEmitter"

    owner = MessageField()
    ow = owner

    fromWhere = ShortField(default_value=0)
    fw = fromWhere

    subsetId = LongField(default_value=-1)
    sid = subsetId

    positional = BoolField(default_value=False, writable=False)
    psl = positional

    ownerCentroid = OwnerCentroidField(default_value=(0.0, 0.0, 0.0))
    ocd = ownerCentroid
    ownerCentroidX = ownerCentroid.ownerCentroidX
    ocx = ownerCentroidX
    ownerCentroidY = ownerCentroid.ownerCentroidY
    ocy = ownerCentroidY
    ownerCentroidZ = ownerCentroid.ownerCentroidZ
    ocz = ownerCentroidZ

    ownerPosData = DataVectorArrayField()
    opd = ownerPosData

    ownerVelData = DataVectorArrayField()
    ovd = ownerVelData

    emitterType = EmitterTypeEnumField(default_value=1)
    emt = emitterType

    rate = DoubleField(default_value=100.0, min_value=0.0, soft_max_value=500.0)
    rat = rate

    scaleRateByObjectSize = BoolField(default_value=True)
    sro = scaleRateByObjectSize

    scaleRateBySpeed = BoolField(default_value=False)
    srs = scaleRateBySpeed

    useRatePP = BoolField(default_value=False)
    urpp = useRatePP

    needParentUV = BoolField(default_value=False)
    npuv = needParentUV

    cycleEmission = CycleEmissionEnumField(default_value=0)
    cye = cycleEmission

    cycleInterval = LongField(default_value=1, min_value=1, soft_max_value=100)
    cyi = cycleInterval

    deltaTimeCycle = TimeField(multi=True, default_value=0.0)
    dtc = deltaTimeCycle

    maxDistance = DoubleLinearField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    max = maxDistance

    minDistance = DoubleLinearField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    min = minDistance

    direction = DirectionField(default_value=(1.0, 0.0, 0.0), soft_min_value=(-10.0, -10.0, -10.0), soft_max_value=(10.0, 10.0, 10.0))
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    spread = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    spr = spread

    speed = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    spd = speed

    speedRandom = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    srnd = speedRandom

    tangentSpeed = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    tspd = tangentSpeed

    normalSpeed = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    nspd = normalSpeed

    currentTime = TimeField(default_value=0.0)
    ct = currentTime

    inheritFactor = DoubleField(multi=True, default_value=0.0)
    inh = inheritFactor

    isFull = BoolField(multi=True, default_value=False)
    full = isFull

    startTime = TimeField(multi=True, default_value=0.0)
    stt = startTime

    deltaTime = TimeField(multi=True, default_value=0.0)
    dt = deltaTime

    emitCountRemainder = DataDoubleArrayField(multi=True)
    ecr = emitCountRemainder

    ratePP = DataDoubleArrayField(readable=False)
    rpp = ratePP

    parentId = DataDoubleArrayField(readable=False)
    paid = parentId

    sweptGeometry = TypedField()
    swge = sweptGeometry

    output = TypedField(multi=True, writable=False)
    ot = output

    seed = LongField(multi=True, default_value=0)
    sd = seed

    randState = RandStateField(multi=True, default_value=(0, 0, 0))
    rst = randState

    enableTextureRate = BoolField(default_value=False)
    etr = enableTextureRate

    textureRate = TextureRateField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    txr = textureRate
    textureRateR = textureRate.textureRateR
    txrr = textureRateR
    textureRateG = textureRate.textureRateG
    txrg = textureRateG
    textureRateB = textureRate.textureRateB
    txrb = textureRateB

    emitFromDark = BoolField(default_value=False)
    efd = emitFromDark

    inheritColor = BoolField(default_value=False)
    inhc = inheritColor

    inheritOpacity = BoolField(default_value=False)
    inho = inheritOpacity

    invertOpacity = BoolField(default_value=False)
    invo = invertOpacity

    useLuminance = BoolField(default_value=False)
    usel = useLuminance

    particleColor = ParticleColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    pc = particleColor
    particleColorR = particleColor.particleColorR
    pcr = particleColorR
    particleColorG = particleColor.particleColorG
    pcg = particleColorG
    particleColorB = particleColor.particleColorB
    pcb = particleColorB

    volumeShape = VolumeShapeEnumField(default_value=0)
    vol = volumeShape

    volumeOffset = VolumeOffsetField(default_value=(0.0, 0.0, 0.0))
    vof = volumeOffset
    volumeOffsetX = volumeOffset.volumeOffsetX
    vfx = volumeOffsetX
    volumeOffsetY = volumeOffset.volumeOffsetY
    vfy = volumeOffsetY
    volumeOffsetZ = volumeOffset.volumeOffsetZ
    vfz = volumeOffsetZ

    volumeEfficiency = DoubleField(default_value=0.0, writable=False)
    vef = volumeEfficiency

    volumeSweep = DoubleAngleField(default_value=360.0, min_value=0.0, max_value=360.0)
    vsw = volumeSweep

    sectionRadius = DoubleLinearField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    vsr = sectionRadius

    awayFromCenter = DoubleField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    afc = awayFromCenter

    awayFromAxis = DoubleField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    afa = awayFromAxis

    alongAxis = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    alx = alongAxis

    aroundAxis = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    arx = aroundAxis

    randomDirection = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    rnd = randomDirection

    directionalSpeed = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    drs = directionalSpeed

    scaleSpeedBySize = BoolField(default_value=False)
    ssz = scaleSpeedBySize

    displaySpeed = BoolField(default_value=True)
    dss = displaySpeed
