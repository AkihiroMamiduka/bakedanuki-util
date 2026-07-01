# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class NormalOrientationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTOMATIC = 0
    FACE_AVERAGE = 1
    EDGE_LOOP = 2


class NormalOrientationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTOMATIC = 0
    FACE_AVERAGE = 1
    EDGE_LOOP = 2

    NAME_MAP = {
        AUTOMATIC: "Automatic",
        FACE_AVERAGE: "Face Average",
        EDGE_LOOP: "Edge Loop",
    }


class NormalOrientationEnumField(
    EnumField[NormalOrientationEnumAttrOperator, NormalOrientationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalOrientationEnumAttrOperator
    PLUG_CLS = NormalOrientationEnumPlugOperator


class AlignmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTOMATIC = 0
    SURFACE_PER_MINUS_VERTEX = 1
    SURFACE_AVERAGE = 2


class AlignmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTOMATIC = 0
    SURFACE_PER_MINUS_VERTEX = 1
    SURFACE_AVERAGE = 2

    NAME_MAP = {
        AUTOMATIC: "Automatic",
        SURFACE_PER_MINUS_VERTEX: "Surface (per-vertex)",
        SURFACE_AVERAGE: "Surface (average)",
    }


class AlignmentEnumField(
    EnumField[AlignmentEnumAttrOperator, AlignmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignmentEnumAttrOperator
    PLUG_CLS = AlignmentEnumPlugOperator


class SupportingEdgesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    EXTERIOR = 1
    INTERIOR = 2
    BOTH_SIDES = 3


class SupportingEdgesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    EXTERIOR = 1
    INTERIOR = 2
    BOTH_SIDES = 3

    NAME_MAP = {
        OFF: "Off",
        EXTERIOR: "Exterior",
        INTERIOR: "Interior",
        BOTH_SIDES: "Both sides",
    }


class SupportingEdgesEnumField(
    EnumField[SupportingEdgesEnumAttrOperator, SupportingEdgesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SupportingEdgesEnumAttrOperator
    PLUG_CLS = SupportingEdgesEnumPlugOperator


class PolyCircularize(DG):
    __slots__ = ()

    NODE_TYPE = "polyCircularize"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    normalOrientation = NormalOrientationEnumField()
    nor = normalOrientation

    normalOffset = FloatField()
    no = normalOffset

    alignment = AlignmentEnumField()
    al = alignment

    evenlyDistribute = BoolField()
    ed = evenlyDistribute

    radialOffset = FloatField()
    ro = radialOffset

    smoothingAngle = FloatField()
    sa = smoothingAngle

    divisions = LongField()
    d = divisions

    supportingEdges = SupportingEdgesEnumField()
    se = supportingEdges

    twist = FloatField()
    t = twist

    relaxInterior = FloatField()
    ri = relaxInterior
