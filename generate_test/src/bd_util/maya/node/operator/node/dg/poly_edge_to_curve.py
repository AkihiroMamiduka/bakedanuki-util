# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class DisplaySmoothMeshEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BASE_MESH_ONLY = 0
    BASE_AND_SMOOTH_MESH = 1
    SMOOTH_MESH_ONLY = 2


class DisplaySmoothMeshEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BASE_MESH_ONLY = 0
    BASE_AND_SMOOTH_MESH = 1
    SMOOTH_MESH_ONLY = 2

    NAME_MAP = {
        BASE_MESH_ONLY: "Base Mesh Only",
        BASE_AND_SMOOTH_MESH: "Base and Smooth Mesh",
        SMOOTH_MESH_ONLY: "Smooth Mesh Only",
    }


class DisplaySmoothMeshEnumField(
    EnumField[DisplaySmoothMeshEnumAttrOperator, DisplaySmoothMeshEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplaySmoothMeshEnumAttrOperator
    PLUG_CLS = DisplaySmoothMeshEnumPlugOperator


class FormEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OPEN = 0
    PERIODIC = 1
    BEST_GUESS = 2


class FormEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OPEN = 0
    PERIODIC = 1
    BEST_GUESS = 2

    NAME_MAP = {
        OPEN: "Open",
        PERIODIC: "Periodic",
        BEST_GUESS: "Best guess",
    }


class FormEnumField(
    EnumField[FormEnumAttrOperator, FormEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormEnumAttrOperator
    PLUG_CLS = FormEnumPlugOperator


class DegreeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _1 = 1
    _2 = 2
    _3 = 3
    _5 = 5
    _7 = 7


class DegreeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _1 = 1
    _2 = 2
    _3 = 3
    _5 = 5
    _7 = 7

    NAME_MAP = {
        _1: "1",
        _2: "2",
        _3: "3",
        _5: "5",
        _7: "7",
    }


class DegreeEnumField(
    EnumField[DegreeEnumAttrOperator, DegreeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeEnumAttrOperator
    PLUG_CLS = DegreeEnumPlugOperator


class PolyEdgeToCurve(DG):
    __slots__ = ()

    NODE_TYPE = "polyEdgeToCurve"

    inputPolymesh = DataMeshField()
    ipm = inputPolymesh

    inputSmoothPolymesh = DataMeshField()
    ism = inputSmoothPolymesh

    displaySmoothMesh = DisplaySmoothMeshEnumField()
    dsm = displaySmoothMesh

    smoothLevel = ShortField()
    lev = smoothLevel

    conformToSmoothMeshPreview = BoolField()
    usm = conformToSmoothMeshPreview

    inputMat = DataMatrixField()
    im = inputMat

    outputcurve = DataNurbsCurveField()
    oc = outputcurve

    inputComponents = TypedField()
    ics = inputComponents

    form = FormEnumField()
    f = form

    degree = DegreeEnumField()
    dg = degree
