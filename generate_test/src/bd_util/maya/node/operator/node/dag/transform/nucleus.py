# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.nucleus import (
    GravityDirectionField,
    PlaneNormalField,
    PlaneOriginField,
    WindDirectionField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField


class CollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    EDGEEDGE = 4
    EDGEFACE = 5
    ALLCOMBINATIONS = 8


class CollisionFlagEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    EDGEEDGE = 4
    EDGEFACE = 5
    ALLCOMBINATIONS = 8

    NAME_MAP = {
        NONE: "None",
        VERTEX: "Vertex",
        VERTEXEDGE: "VertexEdge",
        VERTEXFACE: "VertexFace",
        EDGEEDGE: "EdgeEdge",
        EDGEFACE: "EdgeFace",
        ALLCOMBINATIONS: "AllCombinations",
    }


class CollisionFlagEnumField(
    EnumField[CollisionFlagEnumAttrOperator, CollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionFlagEnumAttrOperator
    PLUG_CLS = CollisionFlagEnumPlugOperator


class SelfCollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    EDGEEDGE = 4
    EDGEFACE = 5


class SelfCollisionFlagEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    EDGEEDGE = 4
    EDGEFACE = 5

    NAME_MAP = {
        NONE: "None",
        VERTEX: "Vertex",
        VERTEXEDGE: "VertexEdge",
        VERTEXFACE: "VertexFace",
        EDGEEDGE: "EdgeEdge",
        EDGEFACE: "EdgeFace",
    }


class SelfCollisionFlagEnumField(
    EnumField[SelfCollisionFlagEnumAttrOperator, SelfCollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfCollisionFlagEnumAttrOperator
    PLUG_CLS = SelfCollisionFlagEnumPlugOperator


class TimingOutputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    FRAME = 1
    SUBFRAME = 2


class TimingOutputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    FRAME = 1
    SUBFRAME = 2

    NAME_MAP = {
        NONE: "None",
        FRAME: "Frame",
        SUBFRAME: "Subframe",
    }


class TimingOutputEnumField(
    EnumField[TimingOutputEnumAttrOperator, TimingOutputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TimingOutputEnumAttrOperator
    PLUG_CLS = TimingOutputEnumPlugOperator


class Nucleus(Transform):
    __slots__ = ()

    NODE_TYPE = "nucleus"

    inputStart = TypedField(multi=True)
    is_ = inputStart

    inputCurrent = TypedField(multi=True)
    ic = inputCurrent

    inputActive = GenericField(multi=True)
    niao = inputActive

    inputPassive = GenericField(multi=True)
    nipo = inputPassive

    inputActiveStart = GenericField(multi=True)
    nias = inputActiveStart

    inputPassiveStart = GenericField(multi=True)
    nips = inputPassiveStart

    outputObjects = GenericField(multi=True)
    noao = outputObjects

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    lastTime = TimeField(default_value=-3921501716349.82)
    lti = lastTime

    evalId = TimeField(default_value=-3921501716349.82)
    eid = evalId

    skipSetup = BoolField(default_value=False)
    sksp = skipSetup

    startTime = TimeField(default_value=2.5)
    sti = startTime

    startFrame = DoubleField(default_value=1.0)
    stf = startFrame

    frameJumpLimit = LongField(default_value=1, min_value=1, soft_min_value=1, soft_max_value=10)
    fjlt = frameJumpLimit

    forceDynamics = BoolField(default_value=False, readable=False, writable=False)
    fdn = forceDynamics

    enable = BoolField(default_value=True)
    ena = enable

    useTransform = BoolField(default_value=True)
    ustf = useTransform

    gravity = FloatField(default_value=9.800000190734863, soft_min_value=0.0, soft_max_value=100.0)
    grty = gravity

    gravityDirection = GravityDirectionField(default_value=(0.0, -1.0, 0.0))
    grdi = gravityDirection
    gravityDirectionX = gravityDirection.gravityDirectionX
    grdx = gravityDirectionX
    gravityDirectionY = gravityDirection.gravityDirectionY
    grdy = gravityDirectionY
    gravityDirectionZ = gravityDirection.gravityDirectionZ
    grdz = gravityDirectionZ

    airDensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    ady = airDensity

    windSpeed = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)
    wisp = windSpeed

    windDirection = WindDirectionField(default_value=(1.0, 0.0, 0.0))
    widi = windDirection
    windDirectionX = windDirection.windDirectionX
    widx = windDirectionX
    windDirectionY = windDirection.windDirectionY
    widy = windDirectionY
    windDirectionZ = windDirection.windDirectionZ
    widz = windDirectionZ

    windNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    wnoi = windNoise

    collisionLayerRange = FloatField(default_value=4.0, soft_min_value=1.0, soft_max_value=10.0)
    clra = collisionLayerRange

    collisionSoftness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    clso = collisionSoftness

    usePlane = BoolField(default_value=False)
    nupl = usePlane

    planeOrigin = PlaneOriginField(default_value=(0.0, 0.0, 0.0))
    npor = planeOrigin
    planeOriginX = planeOrigin.planeOriginX
    npox = planeOriginX
    planeOriginY = planeOrigin.planeOriginY
    npoy = planeOriginY
    planeOriginZ = planeOrigin.planeOriginZ
    npoz = planeOriginZ

    planeNormal = PlaneNormalField(default_value=(0.0, 1.0, 0.0))
    npun = planeNormal
    planeNormalX = planeNormal.planeNormalX
    npnx = planeNormalX
    planeNormalY = planeNormal.planeNormalY
    npny = planeNormalY
    planeNormalZ = planeNormal.planeNormalZ
    npnz = planeNormalZ

    planeBounce = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    npbc = planeBounce

    planeFriction = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=1.0)
    npfr = planeFriction

    planeStickiness = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    npst = planeStickiness

    subSteps = LongField(default_value=3, soft_min_value=1, soft_max_value=20)
    sstp = subSteps

    maxCollisionIterations = LongField(default_value=4, soft_min_value=0, soft_max_value=100)
    mcit = maxCollisionIterations

    collisionFlag = CollisionFlagEnumField(default_value=4)
    cofl = collisionFlag

    selfCollisionFlag = SelfCollisionFlagEnumField(default_value=1)
    scfl = selfCollisionFlag

    timeScale = FloatField(default_value=1.0, min_value=0.0001, soft_min_value=0.01, soft_max_value=10.0)
    tisc = timeScale

    spaceScale = FloatField(default_value=1.0, soft_min_value=0.01, soft_max_value=10.0)
    spsc = spaceScale

    timingOutput = TimingOutputEnumField(default_value=0)
    to = timingOutput
