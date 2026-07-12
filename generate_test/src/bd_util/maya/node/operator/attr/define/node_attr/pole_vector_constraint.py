# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslate", "tt"),
        ("targetRotatePivot", "trp"),
        ("targetRotateTranslate", "trt"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
    )

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotatePivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    trp = targetRotatePivot

    targetRotateTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotatePivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    trp = targetRotatePivot

    targetRotateTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator


class ConstraintRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotatePivotX", "crpx"),
        ("constraintRotatePivotY", "crpy"),
        ("constraintRotatePivotZ", "crpz"),
    )

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotField(
    DoubleLinear3CompoundBaseField[ConstraintRotatePivotAttrOperator, ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotatePivotAttrOperator
    PLUG_CLS = ConstraintRotatePivotPlugOperator

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotateTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateTranslateX", "crtx"),
        ("constraintRotateTranslateY", "crty"),
        ("constraintRotateTranslateZ", "crtz"),
    )

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotateTranslatePlugOperator]
):
    __slots__ = ()

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintRotateTranslateAttrOperator, ConstraintRotateTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateTranslateAttrOperator
    PLUG_CLS = ConstraintRotateTranslatePlugOperator

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class OffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ox"),
        ("offsetY", "oy"),
        ("offsetZ", "oz"),
    )

    offsetX = DoubleLinearField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleLinearField(default_value=0.0)
    oy = offsetY

    offsetZ = DoubleLinearField(default_value=0.0)
    oz = offsetZ


class OffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = DoubleLinearField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleLinearField(default_value=0.0)
    oy = offsetY

    offsetZ = DoubleLinearField(default_value=0.0)
    oz = offsetZ


class OffsetField(
    DoubleLinear3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = DoubleLinearField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleLinearField(default_value=0.0)
    oy = offsetY

    offsetZ = DoubleLinearField(default_value=0.0)
    oz = offsetZ


class ConstraintTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslateX", "ctx"),
        ("constraintTranslateY", "cty"),
        ("constraintTranslateZ", "ctz"),
    )

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintTranslateAttrOperator, ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTranslateAttrOperator
    PLUG_CLS = ConstraintTranslatePlugOperator

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class RestTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RestTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restTranslateX", "rtx"),
        ("restTranslateY", "rty"),
        ("restTranslateZ", "rtz"),
    )

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RestTranslatePlugOperator]
):
    __slots__ = ()

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateField(
    DoubleLinear3CompoundBaseField[RestTranslateAttrOperator, RestTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestTranslateAttrOperator
    PLUG_CLS = RestTranslatePlugOperator

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ
