# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField


class BlendShapeDirectoryPlugOperator(
    CompoundPlugOperator["BlendShapeDirectoryAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("childIndices", "bscd"),
        ("parentIndex", "bspi"),
        ("directoryName", "bsdn"),
        ("directoryVisibility", "bsdv"),
        ("directoryParentVisibility", "bdpv"),
    )

    childIndices = TypedField()
    bscd = childIndices

    parentIndex = LongField()
    bspi = parentIndex

    directoryName = DataStringField()
    bsdn = directoryName

    directoryVisibility = BoolField()
    bsdv = directoryVisibility

    directoryParentVisibility = BoolField()
    bdpv = directoryParentVisibility


class BlendShapeDirectoryAttrOperator(
    CompoundAttrOperator[BlendShapeDirectoryPlugOperator]
):
    __slots__ = ()

    childIndices = TypedField()
    bscd = childIndices

    parentIndex = LongField()
    bspi = parentIndex

    directoryName = DataStringField()
    bsdn = directoryName

    directoryVisibility = BoolField()
    bsdv = directoryVisibility

    directoryParentVisibility = BoolField()
    bdpv = directoryParentVisibility


class BlendShapeDirectoryField(
    CompoundField[BlendShapeDirectoryAttrOperator, BlendShapeDirectoryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendShapeDirectoryAttrOperator
    PLUG_CLS = BlendShapeDirectoryPlugOperator
