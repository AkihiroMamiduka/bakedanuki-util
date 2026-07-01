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


class SampleTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ENTIRE_DOMAIN = 1
    G1_SEGMENTS = 2
    PER_SPAN = 3
    KNOT_VALUES = 4
    ADAPTIVELY = 5


class SampleTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ENTIRE_DOMAIN = 1
    G1_SEGMENTS = 2
    PER_SPAN = 3
    KNOT_VALUES = 4
    ADAPTIVELY = 5

    NAME_MAP = {
        ENTIRE_DOMAIN: "Entire Domain",
        G1_SEGMENTS: "G1 Segments",
        PER_SPAN: "Per Span",
        KNOT_VALUES: "Knot Values",
        ADAPTIVELY: "Adaptively",
    }


class SampleTypeEnumField(
    EnumField[SampleTypeEnumAttrOperator, SampleTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SampleTypeEnumAttrOperator
    PLUG_CLS = SampleTypeEnumPlugOperator


class ArubaTessellate(DG):
    __slots__ = ()

    NODE_TYPE = "arubaTessellate"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    outMesh = DataMeshField()
    om = outMesh

    chordalDeviation = DoubleField()
    cd = chordalDeviation

    minChordLength = DoubleField()
    icl = minChordLength

    maxChordLength = DoubleField()
    mcl = maxChordLength

    sampleType = SampleTypeEnumField()
    st = sampleType

    adaptive = BoolField()
    adp = adaptive

    samples = LongField()
    smp = samples

    normalTolerance = DoubleField()
    ntl = normalTolerance

    tolerance = DoubleLinearField()
    tol = tolerance
