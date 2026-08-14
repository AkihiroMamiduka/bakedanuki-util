# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("enableTarget", "umt"),
        ("weight", "wgt"),
        ("targetMatrix", "tmat"),
        ("offsetMatrix", "ofm"),
    )

    enableTarget = BoolField(default_value=True)
    umt = enableTarget

    weight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    wgt = weight

    targetMatrix = MatrixField()
    tmat = targetMatrix

    offsetMatrix = MatrixField()
    ofm = offsetMatrix


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    enableTarget = BoolField(default_value=True)
    umt = enableTarget

    weight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    wgt = weight

    targetMatrix = MatrixField()
    tmat = targetMatrix

    offsetMatrix = MatrixField()
    ofm = offsetMatrix


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator
