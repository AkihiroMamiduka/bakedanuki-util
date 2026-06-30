# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField


class SubdivisionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    QUADS = 0
    TRIANGLES = 1
    PIE = 2
    CAPS = 3
    CIRCLE = 4


class SubdivisionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    QUADS = 0
    TRIANGLES = 1
    PIE = 2
    CAPS = 3
    CIRCLE = 4

    NAME_MAP = {
        QUADS: "Quads",
        TRIANGLES: "Triangles",
        PIE: "Pie",
        CAPS: "Caps",
        CIRCLE: "Circle",
    }


class SubdivisionModeEnumField(
    EnumField[SubdivisionModeEnumAttrOperator, SubdivisionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubdivisionModeEnumAttrOperator
    PLUG_CLS = SubdivisionModeEnumPlugOperator


class PolyDisc(DG):
    __slots__ = ()

    NODE_TYPE = "polyDisc"

    output = DataMeshField()

    sides = LongField()

    subdivisionMode = SubdivisionModeEnumField()

    subdivisions = LongField()

    radius = DoubleLinearField()

    heightBaseline = FloatField()
