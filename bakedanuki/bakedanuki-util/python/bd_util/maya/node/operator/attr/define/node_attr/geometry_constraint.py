# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.numeric.range.double import DoubleField


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetGeometry", "tgm"),
        ("targetWeight", "tw"),
    )

    targetGeometry = GenericField()
    tgm = targetGeometry

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetGeometry = GenericField()
    tgm = targetGeometry

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator
