# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class NurbsTessellate(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsTessellate"

    format = FormatEnumField()
    f = format

    polygonType = PolygonTypeEnumField()
    pt = polygonType

    polygonCount = LongField()
    pc = polygonCount

    chordHeightRatio = DoubleField()
    chr = chordHeightRatio

    pre70ChordHeightRatio = BoolField()
    pchr = pre70ChordHeightRatio

    fractionalTolerance = DoubleField()
    ft = fractionalTolerance

    minEdgeLength = DoubleLinearField()
    mel = minEdgeLength

    delta = DoubleLinearField()
    d = delta

    uType = UTypeEnumField()
    ut = uType

    uNumber = LongField()
    un = uNumber

    vType = VTypeEnumField()
    vt = vType

    vNumber = LongField()
    vn = vNumber

    useChordHeight = BoolField()
    uch = useChordHeight

    useChordHeightRatio = BoolField()
    ucr = useChordHeightRatio

    chordHeight = DoubleLinearField()
    cht = chordHeight

    edgeSwap = BoolField()
    es = edgeSwap

    matchNormalDir = BoolField()
    mnd = matchNormalDir

    normalizeTrimmedUVRange = BoolField()
    ntr = normalizeTrimmedUVRange

    outputPolygon = DataMeshField()
    op = outputPolygon

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    smoothEdge = BoolField()
    ues = smoothEdge

    smoothEdgeRatio = DoubleField()
    esr = smoothEdgeRatio

    explicitTessellationAttributes = BoolField()
    eta = explicitTessellationAttributes

    uDivisionsFactor = DoubleField()
    nuf = uDivisionsFactor

    vDivisionsFactor = DoubleField()
    nvf = vDivisionsFactor

    curvatureTolerance = CurvatureToleranceEnumField()
    cvt = curvatureTolerance
