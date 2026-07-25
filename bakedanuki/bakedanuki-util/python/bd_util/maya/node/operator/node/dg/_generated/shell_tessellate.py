# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField


class FormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    COUNT = 0
    FIT = 1
    GENERAL = 2
    CVS = 3


class FormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    COUNT = 0
    FIT = 1
    GENERAL = 2
    CVS = 3

    NAME_MAP = {
        COUNT: "Count",
        FIT: "Fit",
        GENERAL: "General",
        CVS: "CVs",
    }


class FormatEnumField(
    EnumField[FormatEnumAttrOperator, FormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormatEnumAttrOperator
    PLUG_CLS = FormatEnumPlugOperator


class PolygonTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRIANGLES = 0
    QUADS = 1


class PolygonTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRIANGLES = 0
    QUADS = 1

    NAME_MAP = {
        TRIANGLES: "Triangles",
        QUADS: "Quads",
    }


class PolygonTypeEnumField(
    EnumField[PolygonTypeEnumAttrOperator, PolygonTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolygonTypeEnumAttrOperator
    PLUG_CLS = PolygonTypeEnumPlugOperator


class UTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3


class UTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3

    NAME_MAP = {
        PER_SURF_HASH_OF_ISOPARMS_IN_3D: "Per Surf # of Isoparms in 3D",
        PER_SURF_HASH_OF_ISOPARMS: "Per Surf # of Isoparms",
        PER_SPAN_HASH_OF_ISOPARMS: "Per Span # of Isoparms",
    }


class UTypeEnumField(
    EnumField[UTypeEnumAttrOperator, UTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UTypeEnumAttrOperator
    PLUG_CLS = UTypeEnumPlugOperator


class VTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3


class VTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_SURF_HASH_OF_ISOPARMS_IN_3D = 1
    PER_SURF_HASH_OF_ISOPARMS = 2
    PER_SPAN_HASH_OF_ISOPARMS = 3

    NAME_MAP = {
        PER_SURF_HASH_OF_ISOPARMS_IN_3D: "Per Surf # of Isoparms in 3D",
        PER_SURF_HASH_OF_ISOPARMS: "Per Surf # of Isoparms",
        PER_SPAN_HASH_OF_ISOPARMS: "Per Span # of Isoparms",
    }


class VTypeEnumField(
    EnumField[VTypeEnumAttrOperator, VTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VTypeEnumAttrOperator
    PLUG_CLS = VTypeEnumPlugOperator


class _GeneratedShellTessellate(DG):
    __slots__ = ()

    NODE_TYPE = "shellTessellate"

    format = FormatEnumField(default_value=1)
    f = format

    polygonType = PolygonTypeEnumField(default_value=0)
    pt = polygonType

    polygonCount = LongField(default_value=200, min_value=1, soft_max_value=1000)
    pc = polygonCount

    chordHeightRatio = DoubleField(default_value=0.983, min_value=0.01, max_value=0.999, soft_min_value=0.9)
    chr = chordHeightRatio

    pre70ChordHeightRatio = BoolField(default_value=False)
    pchr = pre70ChordHeightRatio

    fractionalTolerance = DoubleField(default_value=0.01, min_value=1e-06, soft_min_value=0.001, soft_max_value=1.0)
    ft = fractionalTolerance

    minEdgeLength = DoubleLinearField(default_value=0.001, min_value=0.0001, soft_min_value=0.0001, soft_max_value=1.0)
    mel = minEdgeLength

    delta = DoubleLinearField(default_value=0.1, min_value=0.0001, soft_min_value=0.01, soft_max_value=1.0)
    d = delta

    uType = UTypeEnumField(default_value=3)
    ut = uType

    uNumber = LongField(default_value=3, min_value=1, soft_max_value=32)
    un = uNumber

    vType = VTypeEnumField(default_value=3)
    vt = vType

    vNumber = LongField(default_value=3, min_value=1, soft_max_value=32)
    vn = vNumber

    useChordHeight = BoolField(default_value=False)
    uch = useChordHeight

    useChordHeightRatio = BoolField(default_value=True)
    ucr = useChordHeightRatio

    chordHeight = DoubleLinearField(default_value=0.1, min_value=0.01, soft_min_value=0.05, soft_max_value=0.2)
    cht = chordHeight

    edgeSwap = BoolField(default_value=False)
    es = edgeSwap

    matchNormalDir = BoolField(default_value=False)
    mnd = matchNormalDir

    normalizeTrimmedUVRange = BoolField(default_value=True)
    ntr = normalizeTrimmedUVRange

    outputPolygon = DataMeshField(writable=False)
    op = outputPolygon

    inputShell = TypedField()
    is_ = inputShell
