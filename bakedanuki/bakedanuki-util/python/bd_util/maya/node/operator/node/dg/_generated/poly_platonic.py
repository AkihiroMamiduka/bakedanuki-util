# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField


class PrimitiveEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TETRAHEDRON = 0
    CUBE = 1
    OCTAHEDRON = 2
    DODECAHEDRON = 3
    ICOSAHEDRON = 4


class PrimitiveEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TETRAHEDRON = 0
    CUBE = 1
    OCTAHEDRON = 2
    DODECAHEDRON = 3
    ICOSAHEDRON = 4

    NAME_MAP = {
        TETRAHEDRON: "Tetrahedron",
        CUBE: "Cube",
        OCTAHEDRON: "Octahedron",
        DODECAHEDRON: "Dodecahedron",
        ICOSAHEDRON: "Icosahedron",
    }


class PrimitiveEnumField(
    EnumField[PrimitiveEnumAttrOperator, PrimitiveEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PrimitiveEnumAttrOperator
    PLUG_CLS = PrimitiveEnumPlugOperator


class SubdivisionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    QUADS = 0
    TRIANGLES = 1
    PIE = 2
    CAPS = 3


class SubdivisionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    QUADS = 0
    TRIANGLES = 1
    PIE = 2
    CAPS = 3

    NAME_MAP = {
        QUADS: "Quads",
        TRIANGLES: "Triangles",
        PIE: "Pie",
        CAPS: "Caps",
    }


class SubdivisionModeEnumField(
    EnumField[SubdivisionModeEnumAttrOperator, SubdivisionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubdivisionModeEnumAttrOperator
    PLUG_CLS = SubdivisionModeEnumPlugOperator


class _GeneratedPolyPlatonic(DG):
    __slots__ = ()

    NODE_TYPE = "polyPlatonic"

    output = DataMeshField(writable=False)

    primitive = PrimitiveEnumField(default_value=4)

    subdivisionMode = SubdivisionModeEnumField(default_value=0)

    subdivisions = LongField(default_value=0, min_value=0, soft_max_value=6)

    radius = DoubleLinearField(default_value=1.0, min_value=0.001, soft_max_value=100.0)

    heightBaseline = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)

    sphericalInflation = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
