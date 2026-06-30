# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.result_curve_time_to_unitless import (
    CurveColorField,
    KeyTimeValueField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField


class TangentTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED = 1
    LINEAR = 2
    FLAT = 3
    STEPPED = 5
    SLOW = 6
    FAST = 7
    SPLINE = 9
    CLAMPED = 10
    PLATEAU = 16
    STEPNEXT = 17
    AUTO = 18
    AUTOMIX = 27
    AUTOEASE = 28
    AUTOCUSTOM = 29


class TangentTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED = 1
    LINEAR = 2
    FLAT = 3
    STEPPED = 5
    SLOW = 6
    FAST = 7
    SPLINE = 9
    CLAMPED = 10
    PLATEAU = 16
    STEPNEXT = 17
    AUTO = 18
    AUTOMIX = 27
    AUTOEASE = 28
    AUTOCUSTOM = 29

    NAME_MAP = {
        FIXED: "Fixed",
        LINEAR: "Linear",
        FLAT: "Flat",
        STEPPED: "Stepped",
        SLOW: "Slow",
        FAST: "Fast",
        SPLINE: "Spline",
        CLAMPED: "Clamped",
        PLATEAU: "Plateau",
        STEPNEXT: "StepNext",
        AUTO: "Auto",
        AUTOMIX: "AutoMix",
        AUTOEASE: "AutoEase",
        AUTOCUSTOM: "AutoCustom",
    }


class TangentTypeEnumField(
    EnumField[TangentTypeEnumAttrOperator, TangentTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentTypeEnumAttrOperator
    PLUG_CLS = TangentTypeEnumPlugOperator


class KeyTanInTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED = 1
    LINEAR = 2
    FLAT = 3
    STEPPED = 5
    SLOW = 6
    FAST = 7
    SPLINE = 9
    CLAMPED = 10
    PLATEAU = 16
    STEPNEXT = 17
    AUTO = 18
    AUTOMIX = 27
    AUTOEASE = 28
    AUTOCUSTOM = 29


class KeyTanInTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED = 1
    LINEAR = 2
    FLAT = 3
    STEPPED = 5
    SLOW = 6
    FAST = 7
    SPLINE = 9
    CLAMPED = 10
    PLATEAU = 16
    STEPNEXT = 17
    AUTO = 18
    AUTOMIX = 27
    AUTOEASE = 28
    AUTOCUSTOM = 29

    NAME_MAP = {
        FIXED: "Fixed",
        LINEAR: "Linear",
        FLAT: "Flat",
        STEPPED: "Stepped",
        SLOW: "Slow",
        FAST: "Fast",
        SPLINE: "Spline",
        CLAMPED: "Clamped",
        PLATEAU: "Plateau",
        STEPNEXT: "StepNext",
        AUTO: "Auto",
        AUTOMIX: "AutoMix",
        AUTOEASE: "AutoEase",
        AUTOCUSTOM: "AutoCustom",
    }


class KeyTanInTypeEnumField(
    EnumField[KeyTanInTypeEnumAttrOperator, KeyTanInTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeyTanInTypeEnumAttrOperator
    PLUG_CLS = KeyTanInTypeEnumPlugOperator


class KeyTanOutTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED = 1
    LINEAR = 2
    FLAT = 3
    STEPPED = 5
    SLOW = 6
    FAST = 7
    SPLINE = 9
    CLAMPED = 10
    PLATEAU = 16
    STEPNEXT = 17
    AUTO = 18
    AUTOMIX = 27
    AUTOEASE = 28
    AUTOCUSTOM = 29


class KeyTanOutTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED = 1
    LINEAR = 2
    FLAT = 3
    STEPPED = 5
    SLOW = 6
    FAST = 7
    SPLINE = 9
    CLAMPED = 10
    PLATEAU = 16
    STEPNEXT = 17
    AUTO = 18
    AUTOMIX = 27
    AUTOEASE = 28
    AUTOCUSTOM = 29

    NAME_MAP = {
        FIXED: "Fixed",
        LINEAR: "Linear",
        FLAT: "Flat",
        STEPPED: "Stepped",
        SLOW: "Slow",
        FAST: "Fast",
        SPLINE: "Spline",
        CLAMPED: "Clamped",
        PLATEAU: "Plateau",
        STEPNEXT: "StepNext",
        AUTO: "Auto",
        AUTOMIX: "AutoMix",
        AUTOEASE: "AutoEase",
        AUTOCUSTOM: "AutoCustom",
    }


class KeyTanOutTypeEnumField(
    EnumField[KeyTanOutTypeEnumAttrOperator, KeyTanOutTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeyTanOutTypeEnumAttrOperator
    PLUG_CLS = KeyTanOutTypeEnumPlugOperator


class RotationInterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 1
    EULER = 2
    QUATERNION_TANGENT_DEPENDENT = 3
    QUATERNION_SLERP = 4
    QUATERNION_SQUAD = 5


class RotationInterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 1
    EULER = 2
    QUATERNION_TANGENT_DEPENDENT = 3
    QUATERNION_SLERP = 4
    QUATERNION_SQUAD = 5

    NAME_MAP = {
        NONE: "None",
        EULER: "Euler",
        QUATERNION_TANGENT_DEPENDENT: "Quaternion Tangent Dependent",
        QUATERNION_SLERP: "Quaternion Slerp",
        QUATERNION_SQUAD: "Quaternion Squad",
    }


class RotationInterpolationEnumField(
    EnumField[RotationInterpolationEnumAttrOperator, RotationInterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationInterpolationEnumAttrOperator
    PLUG_CLS = RotationInterpolationEnumPlugOperator


class PreInfinityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    LINEAR = 1
    CYCLE = 3
    CYCLE_WITH_OFFSET = 4
    OSCILLATE = 5


class PreInfinityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    LINEAR = 1
    CYCLE = 3
    CYCLE_WITH_OFFSET = 4
    OSCILLATE = 5

    NAME_MAP = {
        CONSTANT: "Constant",
        LINEAR: "Linear",
        CYCLE: "Cycle",
        CYCLE_WITH_OFFSET: "Cycle with offset",
        OSCILLATE: "Oscillate",
    }


class PreInfinityEnumField(
    EnumField[PreInfinityEnumAttrOperator, PreInfinityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PreInfinityEnumAttrOperator
    PLUG_CLS = PreInfinityEnumPlugOperator


class PostInfinityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    LINEAR = 1
    CYCLE = 3
    CYCLE_WITH_OFFSET = 4
    OSCILLATE = 5


class PostInfinityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    LINEAR = 1
    CYCLE = 3
    CYCLE_WITH_OFFSET = 4
    OSCILLATE = 5

    NAME_MAP = {
        CONSTANT: "Constant",
        LINEAR: "Linear",
        CYCLE: "Cycle",
        CYCLE_WITH_OFFSET: "Cycle with offset",
        OSCILLATE: "Oscillate",
    }


class PostInfinityEnumField(
    EnumField[PostInfinityEnumAttrOperator, PostInfinityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostInfinityEnumAttrOperator
    PLUG_CLS = PostInfinityEnumPlugOperator


class StipplePatternEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SOLID = 0
    DOTTED = 1
    LONG_DOTTED = 2
    SHORT_DOTTED = 3
    DASHED = 4
    LONG_DASHED = 5
    SHORT_DASHED = 6


class StipplePatternEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SOLID = 0
    DOTTED = 1
    LONG_DOTTED = 2
    SHORT_DOTTED = 3
    DASHED = 4
    LONG_DASHED = 5
    SHORT_DASHED = 6

    NAME_MAP = {
        SOLID: "solid",
        DOTTED: "dotted",
        LONG_DOTTED: "long dotted",
        SHORT_DOTTED: "short dotted",
        DASHED: "dashed",
        LONG_DASHED: "long dashed",
        SHORT_DASHED: "short dashed",
    }


class StipplePatternEnumField(
    EnumField[StipplePatternEnumAttrOperator, StipplePatternEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StipplePatternEnumAttrOperator
    PLUG_CLS = StipplePatternEnumPlugOperator


class ResultCurveTimeToUnitless(DG):
    __slots__ = ()

    NODE_TYPE = "resultCurveTimeToUnitless"

    apply = TypedField()
    a = apply

    tangentType = TangentTypeEnumField()
    tan = tangentType

    weightedTangents = BoolField()
    wgt = weightedTangents

    keyTanLocked = BoolField(multi=True)
    ktl = keyTanLocked

    keyWeightLocked = BoolField(multi=True)
    kwl = keyWeightLocked

    keyTanInX = DoubleField(multi=True)
    kix = keyTanInX

    keyTanInY = DoubleField(multi=True)
    kiy = keyTanInY

    keyTanOutX = DoubleField(multi=True)
    kox = keyTanOutX

    keyTanOutY = DoubleField(multi=True)
    koy = keyTanOutY

    keyTanInType = KeyTanInTypeEnumField(multi=True)
    kit = keyTanInType

    keyTanOutType = KeyTanOutTypeEnumField(multi=True)
    kot = keyTanOutType

    keyBreakdown = BoolField(multi=True)
    kbd = keyBreakdown

    keyTickDrawSpecial = BoolField(multi=True)
    kyts = keyTickDrawSpecial

    rotationInterpolation = RotationInterpolationEnumField()
    roti = rotationInterpolation

    preInfinity = PreInfinityEnumField()
    pre = preInfinity

    postInfinity = PostInfinityEnumField()
    pst = postInfinity

    stipplePattern = StipplePatternEnumField()
    sp = stipplePattern

    outStippleThreshold = DoubleField()
    ot = outStippleThreshold

    outStippleRange = DataDoubleArrayField()
    osr = outStippleRange

    inStippleRange = DataDoubleArrayField()
    isr = inStippleRange

    stippleReverse = BoolField()
    sr = stippleReverse

    useCurveColor = BoolField()
    ucc = useCurveColor

    curveColor = CurveColorField()
    cc = curveColor
    curveColorR = curveColor.curveColorR
    ccr = curveColorR
    curveColorG = curveColor.curveColorG
    ccg = curveColorG
    curveColorB = curveColor.curveColorB
    ccb = curveColorB

    start = TimeField()
    st = start

    end = TimeField()
    et = end

    sampleBy = TimeField()
    sby = sampleBy

    input = TimeField()
    i = input

    output = DoubleField()
    o = output

    keyTimeValue = KeyTimeValueField(multi=True)
    ktv = keyTimeValue

    inputResult = DoubleField()
    ir = inputResult
