# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.membrane import (
    GravityDirectionField,
    TurbulenceOffsetField,
    WindDirectionField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class SelfCollisionFlagEnumPlugOperator(
    EnumPlugOperator["SelfCollisionFlagEnumAttrOperator"]
):
    __slots__ = ()

    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    FULL_SURFACE = 4


class SelfCollisionFlagEnumAttrOperator(
    EnumAttrOperator[SelfCollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    FULL_SURFACE = 4

    NAME_MAP = {
        VERTEX: "Vertex",
        VERTEXEDGE: "VertexEdge",
        VERTEXFACE: "VertexFace",
        FULL_SURFACE: "Full Surface",
    }


class SelfCollisionFlagEnumField(
    EnumField[
        SelfCollisionFlagEnumAttrOperator, SelfCollisionFlagEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SelfCollisionFlagEnumAttrOperator
    PLUG_CLS = SelfCollisionFlagEnumPlugOperator


class PressureMethodEnumPlugOperator(
    EnumPlugOperator["PressureMethodEnumAttrOperator"]
):
    __slots__ = ()

    MANUAL_PRESSURE_SETTING = 0
    VOLUME_TRACKING_MODEL = 1


class PressureMethodEnumAttrOperator(
    EnumAttrOperator[PressureMethodEnumPlugOperator]
):
    __slots__ = ()

    MANUAL_PRESSURE_SETTING = 0
    VOLUME_TRACKING_MODEL = 1

    NAME_MAP = {
        MANUAL_PRESSURE_SETTING: "Manual Pressure Setting",
        VOLUME_TRACKING_MODEL: "Volume Tracking Model",
    }


class PressureMethodEnumField(
    EnumField[PressureMethodEnumAttrOperator, PressureMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMethodEnumAttrOperator
    PLUG_CLS = PressureMethodEnumPlugOperator


class GeneratedMembrane(DG):
    __slots__ = ()

    NODE_TYPE = "membrane"

    inputMesh = DataMeshField()
    imsh = inputMesh

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    collideMesh = DataMeshField()
    cmsh = collideMesh

    restShapeMesh = DataMeshField()
    rsmh = restShapeMesh

    outputMesh = DataMeshField()
    omsh = outputMesh

    enable = BoolField(default_value=True)
    enb = enable

    gravity = FloatField(
        default_value=9.800000190734863,
        soft_min_value=0.0,
        soft_max_value=100.0,
    )
    grty = gravity

    gravityDirection = GravityDirectionField(default_value=(0.0, -1.0, 0.0))
    grdi = gravityDirection
    gravityDirectionX = gravityDirection.gravityDirectionX
    grdx = gravityDirectionX
    gravityDirectionY = gravityDirection.gravityDirectionY
    grdy = gravityDirectionY
    gravityDirectionZ = gravityDirection.gravityDirectionZ
    grdz = gravityDirectionZ

    windSpeed = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=50.0
    )
    wisp = windSpeed

    windDirection = WindDirectionField(default_value=(1.0, 0.0, 0.0))
    widi = windDirection
    windDirectionX = windDirection.windDirectionX
    widx = windDirectionX
    windDirectionY = windDirection.windDirectionY
    widy = windDirectionY
    windDirectionZ = windDirection.windDirectionZ
    widz = windDirectionZ

    turbulence = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    trb = turbulence

    turbulenceTime = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    trt = turbulenceTime

    turbulenceFrequency = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    tf = turbulenceFrequency

    turbulenceOffset = TurbulenceOffsetField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(-10.0, -10.0, -10.0),
        soft_max_value=(10.0, 10.0, 10.0),
    )
    to = turbulenceOffset
    turbulenceOffsetX = turbulenceOffset.turbulenceOffsetX
    tox = turbulenceOffsetX
    turbulenceOffsetY = turbulenceOffset.turbulenceOffsetY
    toy = turbulenceOffsetY
    turbulenceOffsetZ = turbulenceOffset.turbulenceOffsetZ
    toz = turbulenceOffsetZ

    lift = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    lft = lift

    drag = FloatField(
        default_value=0.05000000074505806,
        soft_min_value=0.0,
        soft_max_value=2.0,
    )
    drg = drag

    tangentialDrag = FloatField(
        default_value=0.30000001192092896,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    tdrg = tangentialDrag

    steps = LongField(default_value=1, soft_min_value=1, soft_max_value=20)
    stps = steps

    subSteps = LongField(default_value=3, soft_min_value=1, soft_max_value=20)
    sstp = subSteps

    stepSize = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    stsz = stepSize

    spaceScale = FloatField(
        default_value=1.0, soft_min_value=0.01, soft_max_value=10.0
    )
    spsc = spaceScale

    thickness = FloatField(
        default_value=0.05000000074505806,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    thss = thickness

    friction = FloatField(
        default_value=0.10000000149011612,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    fron = friction

    selfCollisionFlag = SelfCollisionFlagEnumField(default_value=3)
    scfl = selfCollisionFlag

    restLengthScale = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=2.0
    )
    rlsc = restLengthScale

    collide = BoolField(default_value=True)
    cold = collide

    selfCollide = BoolField(default_value=False)
    scld = selfCollide

    selfCollideWidthScale = FloatField(
        default_value=1.0, soft_min_value=0.001, soft_max_value=2.0
    )
    scws = selfCollideWidthScale

    pushOut = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    pou = pushOut

    pushOutRadius = FloatField(
        default_value=2.0, min_value=0.0, soft_max_value=100.0
    )
    por = pushOutRadius

    stretchResistance = FloatField(
        default_value=10.0, soft_min_value=0.0, soft_max_value=200.0
    )
    stch = stretchResistance

    compressionResistance = FloatField(
        default_value=10.0, soft_min_value=0.0, soft_max_value=200.0
    )
    comr = compressionResistance

    bendResistance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=200.0
    )
    bnd = bendResistance

    bendAngleDropoff = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    bnad = bendAngleDropoff

    shearResistance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=200.0
    )
    shr = shearResistance

    bendAngleScale = FloatField(
        default_value=1.0, soft_min_value=-2.0, soft_max_value=2.0
    )
    basc = bendAngleScale

    rigidity = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    rity = rigidity

    pressure = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    pres = pressure

    pressureMethod = PressureMethodEnumField(default_value=0)
    pmth = pressureMethod

    weightPerVertex = DataDoubleArrayField()
    wepv = weightPerVertex

    thicknessPerVertex = DataDoubleArrayField()
    thpv = thicknessPerVertex

    turbulencePerVertex = DataDoubleArrayField()
    tupv = turbulencePerVertex
