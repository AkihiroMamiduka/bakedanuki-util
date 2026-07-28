# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bevel_plus import PositionField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class PolyOutMethodEnumPlugOperator(
    EnumPlugOperator["PolyOutMethodEnumAttrOperator"]
):
    __slots__ = ()

    COUNT = 0
    SAMPLING = 2


class PolyOutMethodEnumAttrOperator(
    EnumAttrOperator[PolyOutMethodEnumPlugOperator]
):
    __slots__ = ()

    COUNT = 0
    SAMPLING = 2

    NAME_MAP = {
        COUNT: "Count",
        SAMPLING: "Sampling",
    }


class PolyOutMethodEnumField(
    EnumField[PolyOutMethodEnumAttrOperator, PolyOutMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolyOutMethodEnumAttrOperator
    PLUG_CLS = PolyOutMethodEnumPlugOperator


class PolyOutExtrusionTypeEnumPlugOperator(
    EnumPlugOperator["PolyOutExtrusionTypeEnumAttrOperator"]
):
    __slots__ = ()

    COMPLETE_EXTRUSION = 2
    EXTRUSION_SECTION = 3


class PolyOutExtrusionTypeEnumAttrOperator(
    EnumAttrOperator[PolyOutExtrusionTypeEnumPlugOperator]
):
    __slots__ = ()

    COMPLETE_EXTRUSION = 2
    EXTRUSION_SECTION = 3

    NAME_MAP = {
        COMPLETE_EXTRUSION: "Complete Extrusion",
        EXTRUSION_SECTION: "Extrusion Section",
    }


class PolyOutExtrusionTypeEnumField(
    EnumField[
        PolyOutExtrusionTypeEnumAttrOperator,
        PolyOutExtrusionTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PolyOutExtrusionTypeEnumAttrOperator
    PLUG_CLS = PolyOutExtrusionTypeEnumPlugOperator


class PolyOutCurveTypeEnumPlugOperator(
    EnumPlugOperator["PolyOutCurveTypeEnumAttrOperator"]
):
    __slots__ = ()

    COMPLETE_CURVE = 2
    CURVE_SPAN = 3


class PolyOutCurveTypeEnumAttrOperator(
    EnumAttrOperator[PolyOutCurveTypeEnumPlugOperator]
):
    __slots__ = ()

    COMPLETE_CURVE = 2
    CURVE_SPAN = 3

    NAME_MAP = {
        COMPLETE_CURVE: "Complete Curve",
        CURVE_SPAN: "Curve Span",
    }


class PolyOutCurveTypeEnumField(
    EnumField[
        PolyOutCurveTypeEnumAttrOperator, PolyOutCurveTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PolyOutCurveTypeEnumAttrOperator
    PLUG_CLS = PolyOutCurveTypeEnumPlugOperator


class GeneratedBevelPlus(DG):
    __slots__ = ()

    NODE_TYPE = "bevelPlus"

    inputCurves = DataNurbsCurveField(multi=True)
    ics = inputCurves

    outerStyleCurve = DataNurbsCurveField()
    osc = outerStyleCurve

    innerStyleCurve = DataNurbsCurveField()
    isc = innerStyleCurve

    outputPoly = DataMeshField(writable=False)
    op = outputPoly

    startCapSurface = DataNurbsSurfaceField(writable=False)
    scs = startCapSurface

    endCapSurface = DataNurbsSurfaceField(writable=False)
    ecs = endCapSurface

    outputSurfaces = DataNurbsSurfaceField(multi=True, writable=False)
    os1 = outputSurfaces

    bevelInside = BoolField(default_value=False)
    bin = bevelInside

    count = LongField(multi=True, default_value=0)
    c = count

    position = PositionField(multi=True, default_value=(0.0, 0.0, 0.0))
    p = position

    tolerance = DoubleLinearField(
        default_value=0.01,
        min_value=1e-05,
        soft_min_value=0.001,
        soft_max_value=0.1,
    )
    tol = tolerance

    width = DoubleLinearField(
        default_value=0.1, soft_min_value=-1.0, soft_max_value=1.0
    )
    w = width

    depth = DoubleLinearField(
        default_value=0.1, soft_min_value=0.0, soft_max_value=1.0
    )
    d = depth

    extrudeDepth = DoubleLinearField(
        default_value=0.25, soft_min_value=0.0, soft_max_value=4.0
    )
    ed = extrudeDepth

    numberOfSides = LongField(default_value=4, min_value=1, max_value=4)
    ns = numberOfSides

    capSides = LongField(default_value=1, min_value=1, max_value=4)
    cap = capSides

    joinSurfaces = BoolField(default_value=True)
    js = joinSurfaces

    orderedCurves = BoolField(default_value=False)
    oc = orderedCurves

    normalsOutwards = BoolField(default_value=False)
    no = normalsOutwards

    polyOutMethod = PolyOutMethodEnumField(default_value=2)
    pom = polyOutMethod

    polyOutCount = LongField(
        default_value=200, min_value=2, soft_max_value=1000
    )
    poc = polyOutCount

    polyOutExtrusionType = PolyOutExtrusionTypeEnumField(default_value=3)
    pet = polyOutExtrusionType

    polyOutExtrusionSamples = LongField(
        default_value=2, min_value=1, soft_max_value=8
    )
    pes = polyOutExtrusionSamples

    polyOutCurveType = PolyOutCurveTypeEnumField(default_value=3)
    pct = polyOutCurveType

    polyOutCurveSamples = LongField(
        default_value=6, min_value=1, soft_max_value=32
    )
    pcs = polyOutCurveSamples

    polyOutUseChordHeight = BoolField(default_value=False)
    uch = polyOutUseChordHeight

    polyOutChordHeight = DoubleLinearField(
        default_value=0.1,
        min_value=0.01,
        soft_min_value=0.05,
        soft_max_value=0.2,
    )
    cht = polyOutChordHeight

    polyOutUseChordHeightRatio = BoolField(default_value=True)
    ucr = polyOutUseChordHeightRatio

    polyOutChordHeightRatio = DoubleField(
        default_value=0.1,
        min_value=0.01,
        soft_min_value=0.05,
        soft_max_value=0.2,
    )
    chr = polyOutChordHeightRatio
