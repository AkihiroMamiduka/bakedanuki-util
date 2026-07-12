# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.fluid_emitter import (
    DirectionField,
    OwnerCentroidField,
    ParticleColorField,
    RandStateField,
    TextureRateField,
    TurbulenceFrequencyField,
    TurbulenceOffsetField,
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


class TurbulenceTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GRADIENT = 0
    RANDOM = 1


class TurbulenceTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    GRADIENT = 0
    RANDOM = 1

    NAME_MAP = {
        GRADIENT: "Gradient",
        RANDOM: "Random",
    }


class TurbulenceTypeEnumField(
    EnumField[TurbulenceTypeEnumAttrOperator, TurbulenceTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceTypeEnumAttrOperator
    PLUG_CLS = TurbulenceTypeEnumPlugOperator


class DensityMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2


class DensityMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2

    NAME_MAP = {
        NO_EMISSION: "No Emission",
        ADD: "Add",
        REPLACE: "Replace",
    }


class DensityMethodEnumField(
    EnumField[DensityMethodEnumAttrOperator, DensityMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DensityMethodEnumAttrOperator
    PLUG_CLS = DensityMethodEnumPlugOperator


class HeatMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2


class HeatMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2

    NAME_MAP = {
        NO_EMISSION: "No Emission",
        ADD: "Add",
        REPLACE: "Replace",
    }


class HeatMethodEnumField(
    EnumField[HeatMethodEnumAttrOperator, HeatMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeatMethodEnumAttrOperator
    PLUG_CLS = HeatMethodEnumPlugOperator


class FuelMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2


class FuelMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2

    NAME_MAP = {
        NO_EMISSION: "No Emission",
        ADD: "Add",
        REPLACE: "Replace",
    }


class FuelMethodEnumField(
    EnumField[FuelMethodEnumAttrOperator, FuelMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FuelMethodEnumAttrOperator
    PLUG_CLS = FuelMethodEnumPlugOperator


class SpeedMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2


class SpeedMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_EMISSION = 0
    ADD = 1
    REPLACE = 2

    NAME_MAP = {
        NO_EMISSION: "No Emission",
        ADD: "Add",
        REPLACE: "Replace",
    }


class SpeedMethodEnumField(
    EnumField[SpeedMethodEnumAttrOperator, SpeedMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpeedMethodEnumAttrOperator
    PLUG_CLS = SpeedMethodEnumPlugOperator


class StartFrameEmissionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    START_AND_ALL_FRAMES = 1
    START_FRAME_ONLY = 2


class StartFrameEmissionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    START_AND_ALL_FRAMES = 1
    START_FRAME_ONLY = 2

    NAME_MAP = {
        OFF: "Off",
        START_AND_ALL_FRAMES: "Start and All frames",
        START_FRAME_ONLY: "Start Frame Only",
    }


class StartFrameEmissionEnumField(
    EnumField[StartFrameEmissionEnumAttrOperator, StartFrameEmissionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StartFrameEmissionEnumAttrOperator
    PLUG_CLS = StartFrameEmissionEnumPlugOperator


class FluidEmitter(Transform):
    __slots__ = ()

    NODE_TYPE = "fluidEmitter"

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

    fluidDropoff = DoubleField(default_value=2.0, min_value=0.0, soft_max_value=10.0)
    fdo = fluidDropoff

    normalizedDropoff = BoolField(default_value=True)
    nzd = normalizedDropoff

    useDistance = BoolField(default_value=False)
    usd = useDistance

    fillObject = BoolField(default_value=False)
    fiob = fillObject

    turbulenceType = TurbulenceTypeEnumField(default_value=0)
    trt = turbulenceType

    fluidJitter = BoolField(default_value=True)
    fjt = fluidJitter

    turbulence = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    trb = turbulence

    turbulenceSpeed = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    trs = turbulenceSpeed

    turbulenceFrequency = TurbulenceFrequencyField(default_value=(1.0, 1.0, 1.0), soft_min_value=(0.0, 0.0, 0.0), soft_max_value=(10.0, 10.0, 10.0))
    tf = turbulenceFrequency
    turbulenceFrequencyX = turbulenceFrequency.turbulenceFrequencyX
    tfx = turbulenceFrequencyX
    turbulenceFrequencyY = turbulenceFrequency.turbulenceFrequencyY
    tfy = turbulenceFrequencyY
    turbulenceFrequencyZ = turbulenceFrequency.turbulenceFrequencyZ
    tfz = turbulenceFrequencyZ

    turbulenceOffset = TurbulenceOffsetField(default_value=(0.0, 0.0, 0.0), soft_min_value=(-10.0, -10.0, -10.0), soft_max_value=(10.0, 10.0, 10.0))
    to = turbulenceOffset
    turbulenceOffsetX = turbulenceOffset.turbulenceOffsetX
    tox = turbulenceOffsetX
    turbulenceOffsetY = turbulenceOffset.turbulenceOffsetY
    toy = turbulenceOffsetY
    turbulenceOffsetZ = turbulenceOffset.turbulenceOffsetZ
    toz = turbulenceOffsetZ

    detailTurbulence = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dtr = detailTurbulence

    densityMethod = DensityMethodEnumField(default_value=1)
    dmth = densityMethod

    fluidDensityEmission = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    fde = fluidDensityEmission

    densityEmissionMap = DoubleField(default_value=1.0)
    dem = densityEmissionMap

    heatMethod = HeatMethodEnumField(default_value=1)
    hmth = heatMethod

    fluidHeatEmission = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fhe = fluidHeatEmission

    heatEmissionMap = DoubleField(default_value=1.0)
    hem = heatEmissionMap

    fuelMethod = FuelMethodEnumField(default_value=1)
    fmth = fuelMethod

    fluidFuelEmission = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ffe = fluidFuelEmission

    fuelEmissionMap = DoubleField(default_value=1.0)
    fem = fuelEmissionMap

    emitFluidColor = BoolField(default_value=False)
    efc = emitFluidColor

    emissionFunction = TypedField(writable=False)
    ef = emissionFunction

    speedMethod = SpeedMethodEnumField(default_value=0)
    smth = speedMethod

    inheritVelocity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    invl = inheritVelocity

    motionStreak = BoolField(default_value=False)
    mstr = motionStreak

    startFrameEmission = StartFrameEmissionEnumField(default_value=0)
    sfe = startFrameEmission

    useParticleRadius = BoolField(default_value=False)
    uprd = useParticleRadius

    radiusPP = DataDoubleArrayField(readable=False)
    rdpp = radiusPP
