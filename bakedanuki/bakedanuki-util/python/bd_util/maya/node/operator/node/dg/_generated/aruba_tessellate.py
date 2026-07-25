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


class _GeneratedArubaTessellate(DG):
    __slots__ = ()

    NODE_TYPE = "arubaTessellate"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    outMesh = DataMeshField(writable=False)
    om = outMesh

    chordalDeviation = DoubleField(default_value=0.0015, min_value=0.001, max_value=5.0, soft_min_value=0.001)
    cd = chordalDeviation

    minChordLength = DoubleField(default_value=0.01, min_value=0.01, max_value=10.0, soft_min_value=0.01)
    icl = minChordLength

    maxChordLength = DoubleField(default_value=100.0, min_value=1.0, max_value=100.0, soft_min_value=0.01)
    mcl = maxChordLength

    sampleType = SampleTypeEnumField(default_value=3)
    st = sampleType

    adaptive = BoolField(default_value=True)
    adp = adaptive

    samples = LongField(default_value=8, min_value=1, max_value=64)
    smp = samples

    normalTolerance = DoubleField(default_value=0.0, min_value=0.0, max_value=90.0)
    ntl = normalTolerance

    tolerance = DoubleLinearField(default_value=0.1, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance
