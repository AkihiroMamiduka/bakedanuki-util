# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.ik_handle import (
    DTwistRampField,
    DTwistStartEndField,
    DWorldUpVectorEndField,
    DWorldUpVectorField,
    PoleVectorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class StickinessEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    STICKY = 1


class StickinessEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    STICKY = 1

    NAME_MAP = {
        OFF: "off",
        STICKY: "sticky",
    }


class StickinessEnumField(
    EnumField[StickinessEnumAttrOperator, StickinessEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessEnumAttrOperator
    PLUG_CLS = StickinessEnumPlugOperator


class TwistTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    EASE_IN = 1
    EASE_OUT = 2
    EASE_IN_OUT = 3


class TwistTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    EASE_IN = 1
    EASE_OUT = 2
    EASE_IN_OUT = 3

    NAME_MAP = {
        LINEAR: "Linear",
        EASE_IN: "Ease In",
        EASE_OUT: "Ease Out",
        EASE_IN_OUT: "Ease In Out",
    }


class TwistTypeEnumField(
    EnumField[TwistTypeEnumAttrOperator, TwistTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwistTypeEnumAttrOperator
    PLUG_CLS = TwistTypeEnumPlugOperator


class DWorldUpTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_UP_START_SLASH_END = 2
    OBJECT_ROTATION_UP = 3
    OBJECT_ROTATION_UP_START_SLASH_END = 4
    VECTOR = 5
    VECTOR_START_SLASH_END = 6
    RELATIVE = 7


class DWorldUpTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_UP_START_SLASH_END = 2
    OBJECT_ROTATION_UP = 3
    OBJECT_ROTATION_UP_START_SLASH_END = 4
    VECTOR = 5
    VECTOR_START_SLASH_END = 6
    RELATIVE = 7

    NAME_MAP = {
        SCENE_UP: "Scene Up",
        OBJECT_UP: "Object Up",
        OBJECT_UP_START_SLASH_END: "Object Up (Start/End)",
        OBJECT_ROTATION_UP: "Object Rotation Up",
        OBJECT_ROTATION_UP_START_SLASH_END: "Object Rotation Up (Start/End)",
        VECTOR: "Vector",
        VECTOR_START_SLASH_END: "Vector (Start/End)",
        RELATIVE: "Relative",
    }


class DWorldUpTypeEnumField(
    EnumField[DWorldUpTypeEnumAttrOperator, DWorldUpTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpTypeEnumAttrOperator
    PLUG_CLS = DWorldUpTypeEnumPlugOperator


class DForwardAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITIVE_X = 0
    NEGATIVE_X = 1
    POSITIVE_Y = 2
    NEGATIVE_Y = 3
    POSITIVE_Z = 4
    NEGATIVE_Z = 5


class DForwardAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITIVE_X = 0
    NEGATIVE_X = 1
    POSITIVE_Y = 2
    NEGATIVE_Y = 3
    POSITIVE_Z = 4
    NEGATIVE_Z = 5

    NAME_MAP = {
        POSITIVE_X: "Positive X",
        NEGATIVE_X: "Negative X",
        POSITIVE_Y: "Positive Y",
        NEGATIVE_Y: "Negative Y",
        POSITIVE_Z: "Positive Z",
        NEGATIVE_Z: "Negative Z",
    }


class DForwardAxisEnumField(
    EnumField[DForwardAxisEnumAttrOperator, DForwardAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DForwardAxisEnumAttrOperator
    PLUG_CLS = DForwardAxisEnumPlugOperator


class DWorldUpAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITIVE_Y = 0
    NEGATIVE_Y = 1
    CLOSEST_Y = 2
    POSITIVE_Z = 3
    NEGATIVE_Z = 4
    CLOSEST_Z = 5
    POSITIVE_X = 6
    NEGATIVE_X = 7
    CLOSEST_X = 8


class DWorldUpAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITIVE_Y = 0
    NEGATIVE_Y = 1
    CLOSEST_Y = 2
    POSITIVE_Z = 3
    NEGATIVE_Z = 4
    CLOSEST_Z = 5
    POSITIVE_X = 6
    NEGATIVE_X = 7
    CLOSEST_X = 8

    NAME_MAP = {
        POSITIVE_Y: "Positive Y",
        NEGATIVE_Y: "Negative Y",
        CLOSEST_Y: "Closest Y",
        POSITIVE_Z: "Positive Z",
        NEGATIVE_Z: "Negative Z",
        CLOSEST_Z: "Closest Z",
        POSITIVE_X: "Positive X",
        NEGATIVE_X: "Negative X",
        CLOSEST_X: "Closest X",
    }


class DWorldUpAxisEnumField(
    EnumField[DWorldUpAxisEnumAttrOperator, DWorldUpAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpAxisEnumAttrOperator
    PLUG_CLS = DWorldUpAxisEnumPlugOperator


class DTwistValueTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TOTAL = 0
    START_SLASH_END = 1
    RAMP = 2


class DTwistValueTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TOTAL = 0
    START_SLASH_END = 1
    RAMP = 2

    NAME_MAP = {
        TOTAL: "Total",
        START_SLASH_END: "Start/End",
        RAMP: "Ramp",
    }


class DTwistValueTypeEnumField(
    EnumField[DTwistValueTypeEnumAttrOperator, DTwistValueTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DTwistValueTypeEnumAttrOperator
    PLUG_CLS = DTwistValueTypeEnumPlugOperator


class IkHandle(Transform):
    __slots__ = ()

    NODE_TYPE = "ikHandle"

    startJoint = MessageField()
    hsj = startJoint

    endEffector = MessageField()
    hee = endEffector

    ikSolver = MessageField()
    hsv = ikSolver

    snapEnable = BoolField(default_value=True)
    hsh = snapEnable

    stickiness = StickinessEnumField(default_value=0)
    hs = stickiness

    priority = LongField(default_value=1, min_value=1, soft_max_value=20)
    hpr = priority

    weight = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=100.0)
    hw = weight

    poWeight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    hpo = poWeight

    poleVector = PoleVectorField(default_value=(0.0, 0.0, 1.0))
    pv = poleVector
    poleVectorX = poleVector.poleVectorX
    pvx = poleVectorX
    poleVectorY = poleVector.poleVectorY
    pvy = poleVectorY
    poleVectorZ = poleVector.poleVectorZ
    pvz = poleVectorZ

    inCurve = DataNurbsCurveField()
    ic = inCurve

    offset = DoubleField(default_value=0.0)
    off = offset

    roll = DoubleAngleField(default_value=0.0)
    rol = roll

    twist = DoubleAngleField(default_value=0.0)
    twi = twist

    rootOnCurve = BoolField(default_value=False)
    roc = rootOnCurve

    twistType = TwistTypeEnumField(default_value=0)
    twt = twistType

    rootTwistMode = BoolField(default_value=False)
    rtm = rootTwistMode

    ikBlend = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    ikb = ikBlend

    handleDirtyFlag = BoolField(default_value=False)
    hdf = handleDirtyFlag

    checkSnappingFlag = BoolField(default_value=False)
    csf = checkSnappingFlag

    owningHandleGroup = TypedField()
    ohg = owningHandleGroup

    dofList = TypedField()
    dfl = dofList

    dofListDirtyFlag = BoolField(default_value=False)
    dld = dofListDirtyFlag

    skeletonDirtyFlag = BoolField(default_value=False)
    ods = skeletonDirtyFlag

    ikFkManipulation = BoolField(default_value=False)
    eik = ikFkManipulation

    dWorldUpType = DWorldUpTypeEnumField(default_value=0)
    dwut = dWorldUpType

    dForwardAxis = DForwardAxisEnumField(default_value=0)
    dpa = dForwardAxis

    dWorldUpAxis = DWorldUpAxisEnumField(default_value=0)
    dwua = dWorldUpAxis

    dWorldUpVector = DWorldUpVectorField(default_value=(0.0, 1.0, 0.0))
    dwuv = dWorldUpVector
    dWorldUpVectorX = dWorldUpVector.dWorldUpVectorX
    dwux = dWorldUpVectorX
    dWorldUpVectorY = dWorldUpVector.dWorldUpVectorY
    dwuy = dWorldUpVectorY
    dWorldUpVectorZ = dWorldUpVector.dWorldUpVectorZ
    dwuz = dWorldUpVectorZ

    dWorldUpVectorEnd = DWorldUpVectorEndField(default_value=(0.0, 1.0, 0.0))
    dwve = dWorldUpVectorEnd
    dWorldUpVectorEndX = dWorldUpVectorEnd.dWorldUpVectorEndX
    dwvx = dWorldUpVectorEndX
    dWorldUpVectorEndY = dWorldUpVectorEnd.dWorldUpVectorEndY
    dwvy = dWorldUpVectorEndY
    dWorldUpVectorEndZ = dWorldUpVectorEnd.dWorldUpVectorEndZ
    dwvz = dWorldUpVectorEndZ

    dWorldUpMatrix = MatrixField()
    dwum = dWorldUpMatrix

    dWorldUpMatrixEnd = MatrixField()
    dwue = dWorldUpMatrixEnd

    dTwistValueType = DTwistValueTypeEnumField(default_value=0)
    dtvt = dTwistValueType

    dTwistStartEnd = DTwistStartEndField(default_value=(0.0, 0.0))
    dtse = dTwistStartEnd
    dTwistStart = dTwistStartEnd.dTwistStart
    dtst = dTwistStart
    dTwistEnd = dTwistStartEnd.dTwistEnd
    dten = dTwistEnd

    dTwistRamp = DTwistRampField(default_value=(0.0, 0.0, 0.0))
    dtra = dTwistRamp
    dTwistRampR = dTwistRamp.dTwistRampR
    dtrr = dTwistRampR
    dTwistRampG = dTwistRamp.dTwistRampG
    dtrg = dTwistRampG
    dTwistRampB = dTwistRamp.dTwistRampB
    dtrb = dTwistRampB

    dTwistRampMult = DoubleField(default_value=90.0)
    dtrm = dTwistRampMult

    dTwistControlEnable = BoolField(default_value=False)
    dtce = dTwistControlEnable

    splineIkOldStyle = BoolField(default_value=False)
    sio = splineIkOldStyle
