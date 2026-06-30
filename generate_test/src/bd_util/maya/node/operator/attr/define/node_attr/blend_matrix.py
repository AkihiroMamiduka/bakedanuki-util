# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetMatrix", "tmat"),
        ("useMatrix", "umt"),
        ("weight", "wgt"),
        ("scaleWeight", "sca"),
        ("translateWeight", "tra"),
        ("rotateWeight", "rot"),
        ("shearWeight", "she"),
    )

    targetMatrix = MatrixField()
    tmat = targetMatrix

    useMatrix = BoolField()
    umt = useMatrix

    weight = DoubleField()
    wgt = weight

    scaleWeight = DoubleField()
    sca = scaleWeight

    translateWeight = DoubleField()
    tra = translateWeight

    rotateWeight = DoubleField()
    rot = rotateWeight

    shearWeight = DoubleField()
    she = shearWeight


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetMatrix = MatrixField()
    tmat = targetMatrix

    useMatrix = BoolField()
    umt = useMatrix

    weight = DoubleField()
    wgt = weight

    scaleWeight = DoubleField()
    sca = scaleWeight

    translateWeight = DoubleField()
    tra = translateWeight

    rotateWeight = DoubleField()
    rot = rotateWeight

    shearWeight = DoubleField()
    she = shearWeight


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator
