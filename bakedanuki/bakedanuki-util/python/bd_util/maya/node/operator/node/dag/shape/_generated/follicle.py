# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.follicle import (
    AttractionScaleField,
    ClumpWidthScaleField,
    ColorField,
    OutNormalField,
    OutRotateField,
    OutTangentField,
    OutTranslateField,
    StiffnessScaleField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.mesh import DataMeshField
from .....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from .....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField
from .....attr.define.std.dt.string import DataStringField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class RestPoseEnumPlugOperator(EnumPlugOperator["RestPoseEnumAttrOperator"]):
    __slots__ = ()

    STRAIGHT = 0
    SAME_AS_START = 1
    START_MINUS_GRAVITY = 2
    FROM_CURVE = 3


class RestPoseEnumAttrOperator(EnumAttrOperator[RestPoseEnumPlugOperator]):
    __slots__ = ()

    STRAIGHT = 0
    SAME_AS_START = 1
    START_MINUS_GRAVITY = 2
    FROM_CURVE = 3

    NAME_MAP = {
        STRAIGHT: "Straight",
        SAME_AS_START: "Same As Start",
        START_MINUS_GRAVITY: "Start Minus Gravity",
        FROM_CURVE: "From Curve",
    }


class RestPoseEnumField(
    EnumField[RestPoseEnumAttrOperator, RestPoseEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestPoseEnumAttrOperator
    PLUG_CLS = RestPoseEnumPlugOperator


class PointLockEnumPlugOperator(EnumPlugOperator["PointLockEnumAttrOperator"]):
    __slots__ = ()

    NO_ATTACH = 0
    BASE = 1
    TIP = 2
    BOTHENDS = 3


class PointLockEnumAttrOperator(EnumAttrOperator[PointLockEnumPlugOperator]):
    __slots__ = ()

    NO_ATTACH = 0
    BASE = 1
    TIP = 2
    BOTHENDS = 3

    NAME_MAP = {
        NO_ATTACH: "No Attach",
        BASE: "Base",
        TIP: "Tip",
        BOTHENDS: "BothEnds",
    }


class PointLockEnumField(
    EnumField[PointLockEnumAttrOperator, PointLockEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointLockEnumAttrOperator
    PLUG_CLS = PointLockEnumPlugOperator


class SimulationMethodEnumPlugOperator(
    EnumPlugOperator["SimulationMethodEnumAttrOperator"]
):
    __slots__ = ()

    STATIC = 0
    PASSIVE = 1
    DYNAMIC = 2


class SimulationMethodEnumAttrOperator(
    EnumAttrOperator[SimulationMethodEnumPlugOperator]
):
    __slots__ = ()

    STATIC = 0
    PASSIVE = 1
    DYNAMIC = 2

    NAME_MAP = {
        STATIC: "Static",
        PASSIVE: "Passive",
        DYNAMIC: "Dynamic",
    }


class SimulationMethodEnumField(
    EnumField[
        SimulationMethodEnumAttrOperator, SimulationMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SimulationMethodEnumAttrOperator
    PLUG_CLS = SimulationMethodEnumPlugOperator


class StartDirectionEnumPlugOperator(
    EnumPlugOperator["StartDirectionEnumAttrOperator"]
):
    __slots__ = ()

    SURFACE_NORMAL = 0
    START_CURVE_BASE = 1


class StartDirectionEnumAttrOperator(
    EnumAttrOperator[StartDirectionEnumPlugOperator]
):
    __slots__ = ()

    SURFACE_NORMAL = 0
    START_CURVE_BASE = 1

    NAME_MAP = {
        SURFACE_NORMAL: "Surface Normal",
        START_CURVE_BASE: "Start Curve Base",
    }


class StartDirectionEnumField(
    EnumField[StartDirectionEnumAttrOperator, StartDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StartDirectionEnumAttrOperator
    PLUG_CLS = StartDirectionEnumPlugOperator


class GeneratedFollicle(Shape):
    __slots__ = ()

    NODE_TYPE = "follicle"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    inputMesh = DataMeshField()
    inm = inputMesh

    inputWorldMatrix = DataMatrixField()
    iwm = inputWorldMatrix

    startPositionMatrix = DataMatrixField()
    spm = startPositionMatrix

    parameterU = DoubleField(default_value=0.0)
    pu = parameterU

    parameterV = DoubleField(default_value=0.0)
    pv = parameterV

    startPosition = DataNurbsCurveField()
    sp = startPosition

    restPosition = DataNurbsCurveField()
    rp = restPosition

    currentPosition = DataVectorArrayField()
    crp = currentPosition

    restPose = RestPoseEnumField(default_value=0)
    rsp = restPose

    pointLock = PointLockEnumField(default_value=1)
    ptl = pointLock

    simulationMethod = SimulationMethodEnumField(default_value=2)
    sim = simulationMethod

    startDirection = StartDirectionEnumField(default_value=0)
    sdr = startDirection

    flipDirection = BoolField(default_value=False)
    fld = flipDirection

    hairSysGravity = DoubleField(default_value=1.0)
    hsg = hairSysGravity

    hairSysStiffness = DoubleField(default_value=0.5)
    hss = hairSysStiffness

    overrideDynamics = BoolField(default_value=False)
    ovd = overrideDynamics

    collide = BoolField(default_value=True)
    cld = collide

    damp = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    dmp = damp

    stiffness = DoubleField(default_value=0.15, min_value=0.0, max_value=1.0)
    stf = stiffness

    stiffnessScale = StiffnessScaleField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    sts = stiffnessScale

    lengthFlex = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    lfl = lengthFlex

    clumpWidthMult = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    cwm = clumpWidthMult

    clumpWidthScale = ClumpWidthScaleField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    cws = clumpWidthScale

    startCurveAttract = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    sct = startCurveAttract

    attractionScale = AttractionScaleField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    ats = attractionScale

    attractionDamp = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    ad = attractionDamp

    densityMult = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    dml = densityMult

    curlMult = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    cml = curlMult

    clumpTwistOffset = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    ctf = clumpTwistOffset

    braid = BoolField(default_value=False)
    brd = braid

    colorBlend = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    cbl = colorBlend

    color = ColorField(default_value=(0.0, 0.0, 0.0))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    fixedSegmentLength = BoolField(default_value=False)
    fsl = fixedSegmentLength

    segmentLength = DoubleLinearField(default_value=1.0, min_value=0.005)
    sgl = segmentLength

    sampleDensity = DoubleField(
        default_value=1.0, min_value=0.0, soft_max_value=10.0
    )
    sdn = sampleDensity

    degree = LongField(default_value=2, min_value=1, max_value=3)
    dgr = degree

    clumpWidth = FloatField(
        default_value=0.30000001192092896, min_value=0.0, soft_max_value=1.0
    )
    cw = clumpWidth

    outTranslate = OutTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTranslate
    outTranslateX = outTranslate.outTranslateX
    otx = outTranslateX
    outTranslateY = outTranslate.outTranslateY
    oty = outTranslateY
    outTranslateZ = outTranslate.outTranslateZ
    otz = outTranslateZ

    outRotate = OutRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    or_ = outRotate
    outRotateX = outRotate.outRotateX
    orx = outRotateX
    outRotateY = outRotate.outRotateY
    ory = outRotateY
    outRotateZ = outRotate.outRotateZ
    orz = outRotateZ

    outTangent = OutTangentField(default_value=(1.0, 0.0, 0.0), writable=False)
    otn = outTangent
    outTangentX = outTangent.outTangentX
    otnx = outTangentX
    outTangentY = outTangent.outTangentY
    otny = outTangentY
    outTangentZ = outTangent.outTangentZ
    otnz = outTangentZ

    outNormal = OutNormalField(default_value=(0.0, 0.0, 1.0), writable=False)
    onm = outNormal
    outNormalX = outNormal.outNormalX
    onx = outNormalX
    outNormalY = outNormal.outNormalY
    ony = outNormalY
    outNormalZ = outNormal.outNormalZ
    onz = outNormalZ

    outHair = TypedField(writable=False)
    oha = outHair

    outCurve = DataNurbsCurveField(writable=False)
    ocr = outCurve

    validUv = BoolField(default_value=True, writable=False)
    vuv = validUv

    mapSetName = DataStringField()
    msn = mapSetName
