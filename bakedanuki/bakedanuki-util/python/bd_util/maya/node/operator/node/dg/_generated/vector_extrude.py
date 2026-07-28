# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.vector_extrude import (
    BackBevelCurveField,
    ExtrudeCurveField,
    FrontBevelCurveField,
    GroupIdsField,
    GroupingField,
    OutComponentsField,
    OuterBevelCurveField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.mesh import DataMeshField


class BevelStyleEnumPlugOperator(
    EnumPlugOperator["BevelStyleEnumAttrOperator"]
):
    __slots__ = ()

    OUTER = 1
    INNER = 2


class BevelStyleEnumAttrOperator(EnumAttrOperator[BevelStyleEnumPlugOperator]):
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


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    DISTANCE_FIELD = 0
    NORMALS = 1


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    DISTANCE_FIELD = 0
    NORMALS = 1

    NAME_MAP = {
        DISTANCE_FIELD: "Distance Field",
        NORMALS: "Normals",
    }


class ModeEnumField(EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class BevelEnumPlugOperator(EnumPlugOperator["BevelEnumAttrOperator"]):
    __slots__ = ()

    OFF = 0
    INSIDE = 1
    OUTSIDE = 2


class BevelEnumAttrOperator(EnumAttrOperator[BevelEnumPlugOperator]):
    __slots__ = ()

    OFF = 0
    INSIDE = 1
    OUTSIDE = 2

    NAME_MAP = {
        OFF: "Off",
        INSIDE: "Inside",
        OUTSIDE: "Outside",
    }


class BevelEnumField(EnumField[BevelEnumAttrOperator, BevelEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = BevelEnumAttrOperator
    PLUG_CLS = BevelEnumPlugOperator


class GeneratedVectorExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "vectorExtrude"

    grouping = GroupingField()
    solidsPerCharacter = grouping.solidsPerCharacter
    solidsPerWord = grouping.solidsPerWord
    solidsPerLine = grouping.solidsPerLine

    groupIds = GroupIdsField(default_value=(1.0, 1.0, 1.0, 0.0))
    capGroupId = groupIds.capGroupId
    bevelGroupId = groupIds.bevelGroupId
    extrudeGroupId = groupIds.extrudeGroupId
    charGroupId = groupIds.charGroupId

    outComponents = OutComponentsField()
    capComponents = outComponents.capComponents
    bevelComponents = outComponents.bevelComponents
    extrusionComponents = outComponents.extrusionComponents

    outputMesh = DataMeshField()

    enablePlanarCapUVs = BoolField(default_value=False)

    inputMesh = DataMeshField()

    extrudeDistance = FloatField(
        default_value=2.5, soft_min_value=0.1, soft_max_value=10.0
    )

    extrudeDivisions = LongField(
        default_value=4, min_value=1, soft_max_value=10
    )

    extrudeOffset = FloatField(
        default_value=0.30000001192092896,
        soft_min_value=0.01,
        soft_max_value=1.0,
    )

    bevelDistance = FloatField(
        default_value=0.30000001192092896,
        soft_min_value=0.01,
        soft_max_value=1.0,
    )

    bevelOffset = FloatField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=1.0
    )

    outerBevelDistance = FloatField(
        default_value=0.30000001192092896,
        soft_min_value=0.01,
        soft_max_value=1.0,
    )

    outerBevelDivisions = LongField(
        default_value=4, min_value=1, soft_max_value=10
    )

    bevelDivisions = LongField(default_value=4, min_value=1, soft_max_value=10)

    backBevelDistance = FloatField(
        default_value=0.30000001192092896,
        soft_min_value=0.01,
        soft_max_value=1.0,
    )

    backBevelOffset = FloatField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=1.0
    )

    backBevelDivisions = LongField(
        default_value=4, min_value=1, soft_max_value=10
    )

    frontBevelAdaptivity = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )

    inputComponents = TypedField()
    ics = inputComponents

    extrudeDistancePP = DataDoubleArrayField()

    extrudeDistanceScalePP = DataDoubleArrayField()

    enableExtrusion = BoolField(default_value=True)

    enableFrontBevel = BoolField(default_value=False)

    enableBackBevel = BoolField(default_value=False)

    enableOuterBevel = BoolField(default_value=False)

    offsetFrontBevelAsFraction = BoolField(default_value=True)

    offsetBackBevelAsFraction = BoolField(default_value=True)

    offsetExtrudeAsFraction = BoolField(default_value=True)

    keepFacesTogether = BoolField(default_value=True)

    deleteCaps = BoolField(default_value=False)

    rearBevelUsesFront = BoolField(default_value=False)

    vertsPerChar = DataDoubleArrayField()

    vertexGroupIds = TypedField()

    frontBevelCurve = FrontBevelCurveField(
        multi=True, default_value=(0.0, 0.0)
    )

    backBevelCurve = BackBevelCurveField(multi=True, default_value=(0.0, 0.0))

    extrudeCurve = ExtrudeCurveField(multi=True, default_value=(0.0, 0.0))

    outerBevelCurve = OuterBevelCurveField(
        multi=True, default_value=(0.0, 0.0)
    )

    bevelStyle = BevelStyleEnumField(default_value=1)

    mode = ModeEnumField(default_value=1)
    md = mode

    bevel = BevelEnumField(default_value=0)
    bv = bevel
