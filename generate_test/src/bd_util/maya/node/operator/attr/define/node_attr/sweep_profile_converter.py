# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.typed import TypedField
from ..std.dt.mesh import DataMeshField
from ..std.dt.nurbs_curve import DataNurbsCurveField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class InObjectArrayPlugOperator(
    CompoundPlugOperator["InObjectArrayAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputType", "inputType"),
        ("mesh", "mesh"),
        ("curve", "curve"),
        ("components", "components"),
        ("worldMatrix", "worldMatrix"),
        ("curvePrecision", "curvePrecision"),
        ("curveOptimize", "curveOptimize"),
    )

    inputType = EnumField()

    mesh = DataMeshField()

    curve = DataNurbsCurveField()

    components = TypedField()

    worldMatrix = MatrixField()

    curvePrecision = FloatField()

    curveOptimize = BoolField()


class InObjectArrayAttrOperator(
    CompoundAttrOperator[InObjectArrayPlugOperator]
):
    __slots__ = ()

    inputType = EnumField()

    mesh = DataMeshField()

    curve = DataNurbsCurveField()

    components = TypedField()

    worldMatrix = MatrixField()

    curvePrecision = FloatField()

    curveOptimize = BoolField()


class InObjectArrayField(
    CompoundField[InObjectArrayAttrOperator, InObjectArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InObjectArrayAttrOperator
    PLUG_CLS = InObjectArrayPlugOperator


class CachedLocalZCompoundArrayPlugOperator(
    CompoundPlugOperator["CachedLocalZCompoundArrayAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cachedLocalZNodeUUID", "cachedLocalZNodeUUID"),
        ("cachedLocalZVector", "cachedLocalZVector"),
    )

    cachedLocalZNodeUUID = DataStringField()

    cachedLocalZVector = Double3Field()


class CachedLocalZCompoundArrayAttrOperator(
    CompoundAttrOperator[CachedLocalZCompoundArrayPlugOperator]
):
    __slots__ = ()

    cachedLocalZNodeUUID = DataStringField()

    cachedLocalZVector = Double3Field()


class CachedLocalZCompoundArrayField(
    CompoundField[CachedLocalZCompoundArrayAttrOperator, CachedLocalZCompoundArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CachedLocalZCompoundArrayAttrOperator
    PLUG_CLS = CachedLocalZCompoundArrayPlugOperator
