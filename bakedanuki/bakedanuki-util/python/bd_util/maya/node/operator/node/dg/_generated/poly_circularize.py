# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class NormalOrientationEnumPlugOperator(
    EnumPlugOperator["NormalOrientationEnumAttrOperator"]
):
    __slots__ = ()

    AUTOMATIC = 0
    FACE_AVERAGE = 1
    EDGE_LOOP = 2


class NormalOrientationEnumAttrOperator(
    EnumAttrOperator[NormalOrientationEnumPlugOperator]
):
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
    EnumField[
        NormalOrientationEnumAttrOperator, NormalOrientationEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalOrientationEnumAttrOperator
    PLUG_CLS = NormalOrientationEnumPlugOperator


class AlignmentEnumPlugOperator(EnumPlugOperator["AlignmentEnumAttrOperator"]):
    __slots__ = ()

    AUTOMATIC = 0
    SURFACE_PER_MINUS_VERTEX = 1
    SURFACE_AVERAGE = 2


class AlignmentEnumAttrOperator(EnumAttrOperator[AlignmentEnumPlugOperator]):
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


class SupportingEdgesEnumPlugOperator(
    EnumPlugOperator["SupportingEdgesEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    EXTERIOR = 1
    INTERIOR = 2
    BOTH_SIDES = 3


class SupportingEdgesEnumAttrOperator(
    EnumAttrOperator[SupportingEdgesEnumPlugOperator]
):
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


class GeneratedPolyCircularize(DG):
    __slots__ = ()

    NODE_TYPE = "polyCircularize"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    normalOrientation = NormalOrientationEnumField(default_value=0)
    nor = normalOrientation

    normalOffset = FloatField(default_value=0.0)
    no = normalOffset

    alignment = AlignmentEnumField(default_value=0)
    al = alignment

    evenlyDistribute = BoolField(default_value=True)
    ed = evenlyDistribute

    radialOffset = FloatField(default_value=0.0)
    ro = radialOffset

    smoothingAngle = FloatField(
        default_value=30.0, min_value=0.0, max_value=180.0
    )
    sa = smoothingAngle

    divisions = LongField(default_value=0, min_value=0)
    d = divisions

    supportingEdges = SupportingEdgesEnumField(default_value=0)
    se = supportingEdges

    twist = FloatField(default_value=0.0, min_value=-180.0, max_value=180.0)
    t = twist

    relaxInterior = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ri = relaxInterior
