# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.membrane import (
    GravityDirectionField,
    TurbulenceOffsetField,
    WindDirectionField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class SelfCollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    FULL_SURFACE = 4


class SelfCollisionFlagEnumAttrOperator(EnumAttrOperator):
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
    EnumField[SelfCollisionFlagEnumAttrOperator, SelfCollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfCollisionFlagEnumAttrOperator
    PLUG_CLS = SelfCollisionFlagEnumPlugOperator


class PressureMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MANUAL_PRESSURE_SETTING = 0
    VOLUME_TRACKING_MODEL = 1


class PressureMethodEnumAttrOperator(EnumAttrOperator):
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


class Membrane(DG):
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

    enable = BoolField()
    enb = enable

    gravity = FloatField()
    grty = gravity

    gravityDirection = GravityDirectionField()
    grdi = gravityDirection
    gravityDirectionX = gravityDirection.gravityDirectionX
    grdx = gravityDirectionX
    gravityDirectionY = gravityDirection.gravityDirectionY
    grdy = gravityDirectionY
    gravityDirectionZ = gravityDirection.gravityDirectionZ
    grdz = gravityDirectionZ

    windSpeed = FloatField()
    wisp = windSpeed

    windDirection = WindDirectionField()
    widi = windDirection
    windDirectionX = windDirection.windDirectionX
    widx = windDirectionX
    windDirectionY = windDirection.windDirectionY
    widy = windDirectionY
    windDirectionZ = windDirection.windDirectionZ
    widz = windDirectionZ

    turbulence = FloatField()
    trb = turbulence

    turbulenceTime = FloatField()
    trt = turbulenceTime

    turbulenceFrequency = FloatField()
    tf = turbulenceFrequency

    turbulenceOffset = TurbulenceOffsetField()
    to = turbulenceOffset
    turbulenceOffsetX = turbulenceOffset.turbulenceOffsetX
    tox = turbulenceOffsetX
    turbulenceOffsetY = turbulenceOffset.turbulenceOffsetY
    toy = turbulenceOffsetY
    turbulenceOffsetZ = turbulenceOffset.turbulenceOffsetZ
    toz = turbulenceOffsetZ

    lift = FloatField()
    lft = lift

    drag = FloatField()
    drg = drag

    tangentialDrag = FloatField()
    tdrg = tangentialDrag

    steps = LongField()
    stps = steps

    subSteps = LongField()
    sstp = subSteps

    stepSize = FloatField()
    stsz = stepSize

    spaceScale = FloatField()
    spsc = spaceScale

    thickness = FloatField()
    thss = thickness

    friction = FloatField()
    fron = friction

    selfCollisionFlag = SelfCollisionFlagEnumField()
    scfl = selfCollisionFlag

    restLengthScale = FloatField()
    rlsc = restLengthScale

    collide = BoolField()
    cold = collide

    selfCollide = BoolField()
    scld = selfCollide

    selfCollideWidthScale = FloatField()
    scws = selfCollideWidthScale

    pushOut = FloatField()
    pou = pushOut

    pushOutRadius = FloatField()
    por = pushOutRadius

    stretchResistance = FloatField()
    stch = stretchResistance

    compressionResistance = FloatField()
    comr = compressionResistance

    bendResistance = FloatField()
    bnd = bendResistance

    bendAngleDropoff = FloatField()
    bnad = bendAngleDropoff

    shearResistance = FloatField()
    shr = shearResistance

    bendAngleScale = FloatField()
    basc = bendAngleScale

    rigidity = FloatField()
    rity = rigidity

    pressure = FloatField()
    pres = pressure

    pressureMethod = PressureMethodEnumField()
    pmth = pressureMethod

    weightPerVertex = DataDoubleArrayField()
    wepv = weightPerVertex

    thicknessPerVertex = DataDoubleArrayField()
    thpv = thicknessPerVertex

    turbulencePerVertex = DataDoubleArrayField()
    tupv = turbulencePerVertex
