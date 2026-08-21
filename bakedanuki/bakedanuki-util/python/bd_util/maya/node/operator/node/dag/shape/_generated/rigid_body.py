# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.rigid_body import (
    CenterOfMassField,
    ContactPositionField,
    FieldDataField,
    ForceField,
    GeneralForceField,
    ImpulseField,
    ImpulsePositionField,
    InitialOrientationField,
    InitialPositionField,
    InitialSpinField,
    InitialVelocityField,
    LastPositionField,
    LastRotationField,
    SpinField,
    SpinImpulseField,
    TorqueField,
    VelocityField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.double_array import DataDoubleArrayField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.string import DataStringField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class StandInEnumPlugOperator(EnumPlugOperator["StandInEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    CUBE = 1
    SPHERE = 2


class StandInEnumAttrOperator(EnumAttrOperator[StandInEnumPlugOperator]):
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


class ApplyForceAtEnumPlugOperator(
    EnumPlugOperator["ApplyForceAtEnumAttrOperator"]
):
    __slots__ = ()

    CENTEROFMASS = 0
    BOUNDINGBOX = 1
    VERTICESORCVS = 2


class ApplyForceAtEnumAttrOperator(
    EnumAttrOperator[ApplyForceAtEnumPlugOperator]
):
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


class GeneratedRigidBody(Shape):
    __slots__ = ()

    NODE_TYPE = "rigidBody"

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

    lastPosition = LastPositionField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    lp = lastPosition
    lastPositionX = lastPosition.lastPositionX
    lpx = lastPositionX
    lastPositionY = lastPosition.lastPositionY
    lpy = lastPositionY
    lastPositionZ = lastPosition.lastPositionZ
    lpz = lastPositionZ

    lastRotation = LastRotationField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
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

    bounciness = DoubleField(
        default_value=0.6, min_value=0.0, soft_max_value=2.0
    )
    b = bounciness

    damping = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    dp = damping

    staticFriction = DoubleField(
        default_value=0.2, min_value=0.0, soft_max_value=1.0
    )
    sf = staticFriction

    dynamicFriction = DoubleField(
        default_value=0.2, min_value=0.0, soft_max_value=1.0
    )
    df = dynamicFriction

    collisionLayer = LongField(
        default_value=0, min_value=-1, soft_max_value=10
    )
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

    tessellationFactor = LongField(
        default_value=200, min_value=10, soft_max_value=500
    )
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

    contactPosition = ContactPositionField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
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
