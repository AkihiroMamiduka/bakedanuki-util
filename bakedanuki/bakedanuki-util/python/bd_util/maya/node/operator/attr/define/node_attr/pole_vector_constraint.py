# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Target_targetTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Target_targetTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslateX", "ttx"),
        ("targetTranslateY", "tty"),
        ("targetTranslateZ", "ttz"),
    )

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetTranslatePlugOperator]
):
    __slots__ = ()

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetTranslateAttrOperator, Target_targetTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetTranslateAttrOperator
    PLUG_CLS = Target_targetTranslatePlugOperator

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetRotatePivotAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotatePivotX", "trpx"),
        ("targetRotatePivotY", "trpy"),
        ("targetRotatePivotZ", "trpz"),
    )

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetRotatePivotPlugOperator]
):
    __slots__ = ()

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotatePivotField(
    DoubleLinear3CompoundBaseField[
        Target_targetRotatePivotAttrOperator,
        Target_targetRotatePivotPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotatePivotAttrOperator
    PLUG_CLS = Target_targetRotatePivotPlugOperator

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetRotateTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateTranslateX", "trtx"),
        ("targetRotateTranslateY", "trty"),
        ("targetRotateTranslateZ", "trtz"),
    )

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Target_targetRotateTranslatePlugOperator
    ]
):
    __slots__ = ()

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetRotateTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetRotateTranslateAttrOperator,
        Target_targetRotateTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateTranslateAttrOperator
    PLUG_CLS = Target_targetRotateTranslatePlugOperator

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslate", "tt"),
        ("targetRotatePivot", "trp"),
        ("targetRotateTranslate", "trt"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
    )

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotatePivot = Target_targetRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    trp = targetRotatePivot

    targetRotateTranslate = Target_targetRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotatePivot = Target_targetRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    trp = targetRotatePivot

    targetRotateTranslate = Target_targetRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
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
    DoubleLinear3CompoundBaseField[
        ConstraintRotatePivotAttrOperator, ConstraintRotatePivotPlugOperator
    ]
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
    DoubleLinear3CompoundBasePlugOperator[
        "ConstraintRotateTranslateAttrOperator"
    ]
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
    DoubleLinear3CompoundBaseAttrOperator[
        ConstraintRotateTranslatePlugOperator
    ]
):
    __slots__ = ()

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateField(
    DoubleLinear3CompoundBaseField[
        ConstraintRotateTranslateAttrOperator,
        ConstraintRotateTranslatePlugOperator,
    ]
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
    DoubleLinear3CompoundBaseField[
        ConstraintTranslateAttrOperator, ConstraintTranslatePlugOperator
    ]
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
    DoubleLinear3CompoundBaseField[
        RestTranslateAttrOperator, RestTranslatePlugOperator
    ]
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
