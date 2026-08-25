# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class Target_targetScalePlugOperator(
    Double3CompoundBasePlugOperator["Target_targetScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetScaleX", "tsx"),
        ("targetScaleY", "tsy"),
        ("targetScaleZ", "tsz"),
    )

    targetScaleX = DoubleField(default_value=1.0)
    tsx = targetScaleX

    targetScaleY = DoubleField(default_value=1.0)
    tsy = targetScaleY

    targetScaleZ = DoubleField(default_value=1.0)
    tsz = targetScaleZ


class Target_targetScaleAttrOperator(
    Double3CompoundBaseAttrOperator[Target_targetScalePlugOperator]
):
    __slots__ = ()

    targetScaleX = DoubleField(default_value=1.0)
    tsx = targetScaleX

    targetScaleY = DoubleField(default_value=1.0)
    tsy = targetScaleY

    targetScaleZ = DoubleField(default_value=1.0)
    tsz = targetScaleZ


class Target_targetScaleField(
    Double3CompoundBaseField[
        Target_targetScaleAttrOperator, Target_targetScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetScaleAttrOperator
    PLUG_CLS = Target_targetScalePlugOperator

    targetScaleX = DoubleField(default_value=1.0)
    tsx = targetScaleX

    targetScaleY = DoubleField(default_value=1.0)
    tsy = targetScaleY

    targetScaleZ = DoubleField(default_value=1.0)
    tsz = targetScaleZ


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetScale", "ts"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
    )

    targetScale = Target_targetScaleField(default_value=(1.0, 1.0, 1.0))
    ts = targetScale

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetScale = Target_targetScaleField(default_value=(1.0, 1.0, 1.0))
    ts = targetScale

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator


class OffsetPlugOperator(
    Double3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ox"),
        ("offsetY", "oy"),
        ("offsetZ", "oz"),
    )

    offsetX = DoubleField(default_value=1.0)
    ox = offsetX

    offsetY = DoubleField(default_value=1.0)
    oy = offsetY

    offsetZ = DoubleField(default_value=1.0)
    oz = offsetZ


class OffsetAttrOperator(Double3CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetX = DoubleField(default_value=1.0)
    ox = offsetX

    offsetY = DoubleField(default_value=1.0)
    oy = offsetY

    offsetZ = DoubleField(default_value=1.0)
    oz = offsetZ


class OffsetField(
    Double3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = DoubleField(default_value=1.0)
    ox = offsetX

    offsetY = DoubleField(default_value=1.0)
    oy = offsetY

    offsetZ = DoubleField(default_value=1.0)
    oz = offsetZ


class ConstraintScalePlugOperator(
    Double3CompoundBasePlugOperator["ConstraintScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintScaleX", "csx"),
        ("constraintScaleY", "csy"),
        ("constraintScaleZ", "csz"),
    )

    constraintScaleX = DoubleField(default_value=1.0, writable=False)
    csx = constraintScaleX

    constraintScaleY = DoubleField(default_value=1.0, writable=False)
    csy = constraintScaleY

    constraintScaleZ = DoubleField(default_value=1.0, writable=False)
    csz = constraintScaleZ


class ConstraintScaleAttrOperator(
    Double3CompoundBaseAttrOperator[ConstraintScalePlugOperator]
):
    __slots__ = ()

    constraintScaleX = DoubleField(default_value=1.0, writable=False)
    csx = constraintScaleX

    constraintScaleY = DoubleField(default_value=1.0, writable=False)
    csy = constraintScaleY

    constraintScaleZ = DoubleField(default_value=1.0, writable=False)
    csz = constraintScaleZ


class ConstraintScaleField(
    Double3CompoundBaseField[
        ConstraintScaleAttrOperator, ConstraintScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintScaleAttrOperator
    PLUG_CLS = ConstraintScalePlugOperator

    constraintScaleX = DoubleField(default_value=1.0, writable=False)
    csx = constraintScaleX

    constraintScaleY = DoubleField(default_value=1.0, writable=False)
    csy = constraintScaleY

    constraintScaleZ = DoubleField(default_value=1.0, writable=False)
    csz = constraintScaleZ


class RestScalePlugOperator(
    Double3CompoundBasePlugOperator["RestScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restScaleX", "rsx"),
        ("restScaleY", "rsy"),
        ("restScaleZ", "rsz"),
    )

    restScaleX = DoubleField(default_value=1.0, writable=False)
    rsx = restScaleX

    restScaleY = DoubleField(default_value=1.0, writable=False)
    rsy = restScaleY

    restScaleZ = DoubleField(default_value=1.0, writable=False)
    rsz = restScaleZ


class RestScaleAttrOperator(
    Double3CompoundBaseAttrOperator[RestScalePlugOperator]
):
    __slots__ = ()

    restScaleX = DoubleField(default_value=1.0, writable=False)
    rsx = restScaleX

    restScaleY = DoubleField(default_value=1.0, writable=False)
    rsy = restScaleY

    restScaleZ = DoubleField(default_value=1.0, writable=False)
    rsz = restScaleZ


class RestScaleField(
    Double3CompoundBaseField[RestScaleAttrOperator, RestScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestScaleAttrOperator
    PLUG_CLS = RestScalePlugOperator

    restScaleX = DoubleField(default_value=1.0, writable=False)
    rsx = restScaleX

    restScaleY = DoubleField(default_value=1.0, writable=False)
    rsy = restScaleY

    restScaleZ = DoubleField(default_value=1.0, writable=False)
    rsz = restScaleZ
