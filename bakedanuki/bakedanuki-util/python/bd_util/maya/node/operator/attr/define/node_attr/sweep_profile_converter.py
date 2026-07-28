# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.typed import TypedField
from ..std.dt.mesh import DataMeshField
from ..std.dt.nurbs_curve import DataNurbsCurveField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import (
    Double3Field,
)


class InputTypeEnumPlugOperator(EnumPlugOperator["InputTypeEnumAttrOperator"]):
    __slots__ = ()

    POLY_OBJECT = 0
    POLY_FACE = 1
    POLY_EDGE = 2
    CURVE_OBJECT = 3


class InputTypeEnumAttrOperator(EnumAttrOperator[InputTypeEnumPlugOperator]):
    __slots__ = ()

    POLY_OBJECT = 0
    POLY_FACE = 1
    POLY_EDGE = 2
    CURVE_OBJECT = 3

    NAME_MAP = {
        POLY_OBJECT: "Poly Object",
        POLY_FACE: "Poly Face",
        POLY_EDGE: "Poly Edge",
        CURVE_OBJECT: "Curve Object",
    }


class InputTypeEnumField(
    EnumField[InputTypeEnumAttrOperator, InputTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputTypeEnumAttrOperator
    PLUG_CLS = InputTypeEnumPlugOperator


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

    inputType = InputTypeEnumField(default_value=3)

    mesh = DataMeshField(readable=False)

    curve = DataNurbsCurveField(readable=False)

    components = TypedField()

    worldMatrix = MatrixField()

    curvePrecision = FloatField(
        default_value=80.0, min_value=0.0, max_value=100.0
    )

    curveOptimize = BoolField(default_value=True)


class InObjectArrayAttrOperator(
    CompoundAttrOperator[InObjectArrayPlugOperator]
):
    __slots__ = ()

    inputType = InputTypeEnumField(default_value=3)

    mesh = DataMeshField(readable=False)

    curve = DataNurbsCurveField(readable=False)

    components = TypedField()

    worldMatrix = MatrixField()

    curvePrecision = FloatField(
        default_value=80.0, min_value=0.0, max_value=100.0
    )

    curveOptimize = BoolField(default_value=True)


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

    cachedLocalZVector = Double3Field(default_value=(0.0, 0.0, 0.0))


class CachedLocalZCompoundArrayAttrOperator(
    CompoundAttrOperator[CachedLocalZCompoundArrayPlugOperator]
):
    __slots__ = ()

    cachedLocalZNodeUUID = DataStringField()

    cachedLocalZVector = Double3Field(default_value=(0.0, 0.0, 0.0))


class CachedLocalZCompoundArrayField(
    CompoundField[
        CachedLocalZCompoundArrayAttrOperator,
        CachedLocalZCompoundArrayPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CachedLocalZCompoundArrayAttrOperator
    PLUG_CLS = CachedLocalZCompoundArrayPlugOperator
