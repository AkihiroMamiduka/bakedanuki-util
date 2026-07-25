# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField


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

    useMatrix = BoolField(default_value=True)
    umt = useMatrix

    weight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    wgt = weight

    scaleWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    sca = scaleWeight

    translateWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    tra = translateWeight

    rotateWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    rot = rotateWeight

    shearWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    she = shearWeight


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetMatrix = MatrixField()
    tmat = targetMatrix

    useMatrix = BoolField(default_value=True)
    umt = useMatrix

    weight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    wgt = weight

    scaleWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    sca = scaleWeight

    translateWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    tra = translateWeight

    rotateWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    rot = rotateWeight

    shearWeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    she = shearWeight


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator
