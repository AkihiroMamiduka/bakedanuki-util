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

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True)
    wl = weightList

    rotation = DoubleField()

    twistRotation = DoubleField()

    offset = DoubleField()

    lengthScale = DoubleField()

    samplingAccuracy = DoubleField()

    maxScale = DoubleField()

    flipAxis = BoolField()

    loopClosedCurves = BoolField()

    keepLength = BoolField()

    alignmentMode = AlignmentModeEnumField()

    aimCurveMode = AimCurveModeEnumField()

    aimMode = AimModeEnumField()

    scaleCurve = ScaleCurveField(multi=True)

    twistCurve = TwistCurveField(multi=True)

    inputCurve = DataNurbsCurveField()

    aimCurve = DataNurbsCurveField()

    curveParams = DataDoubleArrayField()

    legacy2017 = BoolField()
