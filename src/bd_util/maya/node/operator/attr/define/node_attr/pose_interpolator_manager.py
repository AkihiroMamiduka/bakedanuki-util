# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField


class PoseInterpolatorDirectoryPlugOperator(
    CompoundPlugOperator["PoseInterpolatorDirectoryAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("childIndices", "tpcd"),
        ("parentIndex", "tppi"),
        ("directoryName", "tpdn"),
    )

    childIndices = TypedField()
    tpcd = childIndices

    parentIndex = LongField(default_value=0)
    tppi = parentIndex

    directoryName = DataStringField()
    tpdn = directoryName


class PoseInterpolatorDirectoryAttrOperator(
    CompoundAttrOperator[PoseInterpolatorDirectoryPlugOperator]
):
    __slots__ = ()

    childIndices = TypedField()
    tpcd = childIndices

    parentIndex = LongField(default_value=0)
    tppi = parentIndex

    directoryName = DataStringField()
    tpdn = directoryName


class PoseInterpolatorDirectoryField(
    CompoundField[PoseInterpolatorDirectoryAttrOperator, PoseInterpolatorDirectoryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoseInterpolatorDirectoryAttrOperator
    PLUG_CLS = PoseInterpolatorDirectoryPlugOperator
