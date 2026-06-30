# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar_range.double import DoubleField


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

    axis = EnumField()
    ax = axis

    triggerMin = DoubleField()
    trgmin = triggerMin

    bias = DoubleField()
    bis = bias

    biasAdjust = DoubleField()
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

    axis = EnumField()
    ax = axis

    triggerMin = DoubleField()
    trgmin = triggerMin

    bias = DoubleField()
    bis = bias

    biasAdjust = DoubleField()
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

    axis = EnumField()
    ax = axis

    triggerMin = DoubleField()
    trgmin = triggerMin

    bias = DoubleField()
    bis = bias

    biasAdjust = DoubleField()
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

    outTranslate = CompoundField()
    ot = outTranslate

    outRotate = CompoundField()
    or_ = outRotate

    outTrigger = DoubleField()
    otrg = outTrigger


class OutDataAttrOperator(
    CompoundAttrOperator[OutDataPlugOperator]
):
    __slots__ = ()

    outTranslate = CompoundField()
    ot = outTranslate

    outRotate = CompoundField()
    or_ = outRotate

    outTrigger = DoubleField()
    otrg = outTrigger


class OutDataField(
    CompoundField[OutDataAttrOperator, OutDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutDataAttrOperator
    PLUG_CLS = OutDataPlugOperator

    outTranslate = CompoundField()
    ot = outTranslate

    outRotate = CompoundField()
    or_ = outRotate

    outTrigger = DoubleField()
    otrg = outTrigger
