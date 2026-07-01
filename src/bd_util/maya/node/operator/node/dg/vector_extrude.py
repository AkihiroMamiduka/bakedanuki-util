# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.vector_extrude import (
    BackBevelCurveField,
    ExtrudeCurveField,
    FrontBevelCurveField,
    GroupIdsField,
    GroupingField,
    OutComponentsField,
    OuterBevelCurveField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.mesh import DataMeshField


class BevelStyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OUTER = 1
    INNER = 2


class BevelStyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OUTER = 1
    INNER = 2

    NAME_MAP = {
        OUTER: "Outer",
        INNER: "Inner",
    }


class BevelStyleEnumField(
    EnumField[BevelStyleEnumAttrOperator, BevelStyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BevelStyleEnumAttrOperator
    PLUG_CLS = BevelStyleEnumPlugOperator


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISTANCE_FIELD = 0
    NORMALS = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISTANCE_FIELD = 0
    NORMALS = 1

    NAME_MAP = {
        DISTANCE_FIELD: "Distance Field",
        NORMALS: "Normals",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class BevelEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    INSIDE = 1
    OUTSIDE = 2


class BevelEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    INSIDE = 1
    OUTSIDE = 2

    NAME_MAP = {
        OFF: "Off",
        INSIDE: "Inside",
        OUTSIDE: "Outside",
    }


class BevelEnumField(
    EnumField[BevelEnumAttrOperator, BevelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BevelEnumAttrOperator
    PLUG_CLS = BevelEnumPlugOperator


class VectorExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "vectorExtrude"

    grouping = GroupingField()
    solidsPerCharacter = grouping.solidsPerCharacter
    solidsPerWord = grouping.solidsPerWord
    solidsPerLine = grouping.solidsPerLine

    groupIds = GroupIdsField()
    capGroupId = groupIds.capGroupId
    bevelGroupId = groupIds.bevelGroupId
    extrudeGroupId = groupIds.extrudeGroupId
    charGroupId = groupIds.charGroupId

    outComponents = OutComponentsField()
    capComponents = outComponents.capComponents
    bevelComponents = outComponents.bevelComponents
    extrusionComponents = outComponents.extrusionComponents

    outputMesh = DataMeshField()

    enablePlanarCapUVs = BoolField()

    inputMesh = DataMeshField()

    extrudeDistance = FloatField()

    extrudeDivisions = LongField()

    extrudeOffset = FloatField()

    bevelDistance = FloatField()

    bevelOffset = FloatField()

    outerBevelDistance = FloatField()

    outerBevelDivisions = LongField()

    bevelDivisions = LongField()

    backBevelDistance = FloatField()

    backBevelOffset = FloatField()

    backBevelDivisions = LongField()

    frontBevelAdaptivity = FloatField()

    inputComponents = TypedField()
    ics = inputComponents

    extrudeDistancePP = DataDoubleArrayField()

    extrudeDistanceScalePP = DataDoubleArrayField()

    enableExtrusion = BoolField()

    enableFrontBevel = BoolField()

    enableBackBevel = BoolField()

    enableOuterBevel = BoolField()

    offsetFrontBevelAsFraction = BoolField()

    offsetBackBevelAsFraction = BoolField()

    offsetExtrudeAsFraction = BoolField()

    keepFacesTogether = BoolField()

    deleteCaps = BoolField()

    rearBevelUsesFront = BoolField()

    vertsPerChar = DataDoubleArrayField()

    vertexGroupIds = TypedField()

    frontBevelCurve = FrontBevelCurveField(multi=True)

    backBevelCurve = BackBevelCurveField(multi=True)

    extrudeCurve = ExtrudeCurveField(multi=True)

    outerBevelCurve = OuterBevelCurveField(multi=True)

    bevelStyle = BevelStyleEnumField()

    mode = ModeEnumField()
    md = mode

    bevel = BevelEnumField()
    bv = bevel
