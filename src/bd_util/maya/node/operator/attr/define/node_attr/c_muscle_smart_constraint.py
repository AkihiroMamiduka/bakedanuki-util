# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar_range.double import DoubleField


class AxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class AxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Y_MINUS_AXIS: "Y-Axis",
        Z_MINUS_AXIS: "Z-Axis",
        NEG_X_MINUS_AXIS: "Neg X-Axis",
        NEG_Y_MINUS_AXIS: "Neg Y-Axis",
        NEG_Z_MINUS_AXIS: "Neg Z-Axis",
    }


class AxisEnumField(
    EnumField[AxisEnumAttrOperator, AxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisEnumAttrOperator
    PLUG_CLS = AxisEnumPlugOperator


class ConstrainDataPlugOperator(
    CompoundPlugOperator["ConstrainDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixA", "wma"),
        ("worldMatrixB", "wmb"),
        ("worldMatrixABase", "wmab"),
        ("worldMatrixBBase", "wmbb"),
        ("axis", "ax"),
        ("triggerMin", "trgmin"),
        ("bias", "bis"),
        ("biasAdjust", "bisadj"),
    )

    worldMatrixA = MatrixField()
    wma = worldMatrixA

    worldMatrixB = MatrixField()
    wmb = worldMatrixB

    worldMatrixABase = MatrixField()
    wmab = worldMatrixABase

    worldMatrixBBase = MatrixField()
    wmbb = worldMatrixBBase

    axis = AxisEnumField(default_value=1)
    ax = axis

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    bias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bis = bias

    biasAdjust = DoubleField(default_value=0.0, min_value=-2.0, max_value=2.0)
    bisadj = biasAdjust


class ConstrainDataAttrOperator(
    CompoundAttrOperator[ConstrainDataPlugOperator]
):
    __slots__ = ()

    worldMatrixA = MatrixField()
    wma = worldMatrixA

    worldMatrixB = MatrixField()
    wmb = worldMatrixB

    worldMatrixABase = MatrixField()
    wmab = worldMatrixABase

    worldMatrixBBase = MatrixField()
    wmbb = worldMatrixBBase

    axis = AxisEnumField(default_value=1)
    ax = axis

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    bias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bis = bias

    biasAdjust = DoubleField(default_value=0.0, min_value=-2.0, max_value=2.0)
    bisadj = biasAdjust


class ConstrainDataField(
    CompoundField[ConstrainDataAttrOperator, ConstrainDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstrainDataAttrOperator
    PLUG_CLS = ConstrainDataPlugOperator

    worldMatrixA = MatrixField()
    wma = worldMatrixA

    worldMatrixB = MatrixField()
    wmb = worldMatrixB

    worldMatrixABase = MatrixField()
    wmab = worldMatrixABase

    worldMatrixBBase = MatrixField()
    wmbb = worldMatrixBBase

    axis = AxisEnumField(default_value=1)
    ax = axis

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    bias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bis = bias

    biasAdjust = DoubleField(default_value=0.0, min_value=-2.0, max_value=2.0)
    bisadj = biasAdjust


class OutDataPlugOperator(
    CompoundPlugOperator["OutDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTranslate", "ot"),
        ("outRotate", "or"),
        ("outTrigger", "otrg"),
    )

    outTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    ot = outTranslate

    outRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    or_ = outRotate

    outTrigger = DoubleField(default_value=0.0)
    otrg = outTrigger


class OutDataAttrOperator(
    CompoundAttrOperator[OutDataPlugOperator]
):
    __slots__ = ()

    outTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    ot = outTranslate

    outRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    or_ = outRotate

    outTrigger = DoubleField(default_value=0.0)
    otrg = outTrigger


class OutDataField(
    CompoundField[OutDataAttrOperator, OutDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutDataAttrOperator
    PLUG_CLS = OutDataPlugOperator

    outTranslate = CompoundField(default_value=(0.0, 0.0, 0.0))
    ot = outTranslate

    outRotate = CompoundField(default_value=(0.0, 0.0, 0.0))
    or_ = outRotate

    outTrigger = DoubleField(default_value=0.0)
    otrg = outTrigger
