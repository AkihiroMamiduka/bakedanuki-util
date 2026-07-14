# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.curve_warp import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    ScaleCurveField,
    TwistCurveField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class AlignmentModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 1
    X = 2
    Y = 3
    Z = 4


class AlignmentModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 1
    X = 2
    Y = 3
    Z = 4

    NAME_MAP = {
        AUTO: "Auto",
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class AlignmentModeEnumField(
    EnumField[AlignmentModeEnumAttrOperator, AlignmentModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignmentModeEnumAttrOperator
    PLUG_CLS = AlignmentModeEnumPlugOperator


class AimCurveModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    U_VALUE_FAST = 1
    CLOSEST_POINT_SLOW = 2


class AimCurveModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    U_VALUE_FAST = 1
    CLOSEST_POINT_SLOW = 2

    NAME_MAP = {
        U_VALUE_FAST: "U Value (fast)",
        CLOSEST_POINT_SLOW: "Closest Point (slow)",
    }


class AimCurveModeEnumField(
    EnumField[AimCurveModeEnumAttrOperator, AimCurveModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AimCurveModeEnumAttrOperator
    PLUG_CLS = AimCurveModeEnumPlugOperator


class AimModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CURVE_NORMALS = 1
    AUTO_NORMALS = 2
    AIM_CURVE = 3


class AimModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CURVE_NORMALS = 1
    AUTO_NORMALS = 2
    AIM_CURVE = 3

    NAME_MAP = {
        CURVE_NORMALS: "Curve Normals",
        AUTO_NORMALS: "Auto Normals",
        AIM_CURVE: "Aim Curve",
    }


class AimModeEnumField(
    EnumField[AimModeEnumAttrOperator, AimModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AimModeEnumAttrOperator
    PLUG_CLS = AimModeEnumPlugOperator


class CurveWarp(DG):
    __slots__ = ()

    NODE_TYPE = "curveWarp"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    rotation = DoubleField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    twistRotation = DoubleField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    offset = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    lengthScale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)

    samplingAccuracy = DoubleField(default_value=1.0, min_value=0.01, soft_max_value=2.0)

    maxScale = DoubleField(default_value=2.0, soft_min_value=0.0, soft_max_value=10.0)

    flipAxis = BoolField(default_value=False)

    loopClosedCurves = BoolField(default_value=False)

    keepLength = BoolField(default_value=True)

    alignmentMode = AlignmentModeEnumField(default_value=1)

    aimCurveMode = AimCurveModeEnumField(default_value=2)

    aimMode = AimModeEnumField(default_value=2)

    scaleCurve = ScaleCurveField(multi=True, default_value=(0.0, 0.0))

    twistCurve = TwistCurveField(multi=True, default_value=(0.0, 0.0))

    inputCurve = DataNurbsCurveField()

    aimCurve = DataNurbsCurveField()

    curveParams = DataDoubleArrayField()

    legacy2017 = BoolField(default_value=False)
