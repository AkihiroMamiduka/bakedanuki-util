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
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class CurvatureToleranceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3
    NO_CURVATURE_CHECK = 4


class CurvatureToleranceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3
    NO_CURVATURE_CHECK = 4

    NAME_MAP = {
        HIGHEST_QUALITY: "Highest Quality",
        HIGH_QUALITY: "High Quality",
        MEDIUM_QUALITY: "Medium Quality",
        LOW_QUALITY: "Low Quality",
        NO_CURVATURE_CHECK: "No Curvature Check",
    }


class CurvatureToleranceEnumField(
    EnumField[CurvatureToleranceEnumAttrOperator, CurvatureToleranceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurvatureToleranceEnumAttrOperator
    PLUG_CLS = CurvatureToleranceEnumPlugOperator


class _GeneratedNurbsTessellate(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsTessellate"

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

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    smoothEdge = BoolField(default_value=False)
    ues = smoothEdge

    smoothEdgeRatio = DoubleField(default_value=0.99, min_value=0.1, max_value=0.999, soft_min_value=0.95)
    esr = smoothEdgeRatio

    explicitTessellationAttributes = BoolField(default_value=True)
    eta = explicitTessellationAttributes

    uDivisionsFactor = DoubleField(default_value=1.5, min_value=0.1, soft_max_value=5.0)
    nuf = uDivisionsFactor

    vDivisionsFactor = DoubleField(default_value=1.5, min_value=0.1, soft_max_value=5.0)
    nvf = vDivisionsFactor

    curvatureTolerance = CurvatureToleranceEnumField(default_value=2)
    cvt = curvatureTolerance
