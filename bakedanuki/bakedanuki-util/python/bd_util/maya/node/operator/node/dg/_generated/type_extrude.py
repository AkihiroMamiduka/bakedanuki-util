# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.type_extrude import (
    BackBevelCurveField,
    ExtrudeCurveField,
    FrontBevelCurveField,
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


class GeneratedTypeExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "typeExtrude"

    inputMesh = DataMeshField()
    in_ = inputMesh

    outputMesh = DataMeshField(writable=False)
    out = outputMesh

    mode = ModeEnumField(default_value=1)
    md = mode

    enableExtrusion = BoolField(default_value=True)
    enEx = enableExtrusion

    extrudeDivisions = LongField(
        default_value=4, min_value=1, soft_min_value=1, soft_max_value=10
    )
    exdv = extrudeDivisions

    extrudeDistance = FloatField(
        default_value=2.5, soft_min_value=0.1, soft_max_value=10.0
    )
    exds = extrudeDistance

    extrudeOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    exof = extrudeOffset

    extrudeCurve = ExtrudeCurveField(multi=True, default_value=(0.0, 0.0))
    exc = extrudeCurve

    deleteCaps = BoolField(default_value=False)
    dcs = deleteCaps

    gridSize = LongField(default_value=100)
    gs = gridSize

    bevelOffset = FloatField(
        default_value=0.25, soft_min_value=0.0, soft_max_value=1.0
    )
    bof = bevelOffset

    frontBevelCurve = FrontBevelCurveField(
        multi=True, default_value=(0.0, 0.0)
    )
    fbc = frontBevelCurve

    bevelDivisions = LongField(
        default_value=6, min_value=1, soft_min_value=1, soft_max_value=20
    )
    bdv = bevelDivisions

    bevelDistance = FloatField(
        default_value=0.3499999940395355,
        soft_min_value=-1.0,
        soft_max_value=1.0,
    )
    bds = bevelDistance

    capGroupId = LongField(default_value=-1)
    cid = capGroupId

    bevelGroupId = LongField(default_value=-1)
    bid = bevelGroupId

    extrudeGroupId = LongField(default_value=-1)
    eid = extrudeGroupId

    defaultGroupId = LongField(default_value=-1)
    did = defaultGroupId

    enableBackBevel = BoolField(default_value=False)
    ebb = enableBackBevel

    backBevelOffset = FloatField(
        default_value=0.25, soft_min_value=0.0, soft_max_value=1.0
    )
    bbof = backBevelOffset

    backBevelCurve = BackBevelCurveField(multi=True, default_value=(0.0, 0.0))
    bbc = backBevelCurve

    backBevelDivisions = LongField(
        default_value=6, min_value=1, soft_min_value=1, soft_max_value=20
    )
    bbdv = backBevelDivisions

    backBevelDistance = FloatField(
        default_value=0.3499999940395355,
        soft_min_value=-1.0,
        soft_max_value=1.0,
    )
    bbds = backBevelDistance

    rearBevelUsesFront = BoolField(default_value=False)
    rbuf = rearBevelUsesFront

    enableCapShader = BoolField(default_value=False)
    ecs = enableCapShader

    enableBevelShader = BoolField(default_value=False)
    ebs = enableBevelShader

    enableExtrudeShader = BoolField(default_value=False)
    ees = enableExtrudeShader

    outComponents = OutComponentsField()
    capComponents = outComponents.capComponents
    bevelComponents = outComponents.bevelComponents
    extrusionComponents = outComponents.extrusionComponents

    charGroupId = LongField(multi=True, default_value=0, readable=False)

    vertsPerChar = DataDoubleArrayField()

    offsetFrontBevelAsFraction = BoolField(default_value=True)

    offsetBackBevelAsFraction = BoolField(default_value=True)

    offsetExtrudeAsFraction = BoolField(default_value=True)

    enableFrontBevel = BoolField(default_value=False)

    enableOuterBevel = BoolField(default_value=False)

    outerBevelCurve = OuterBevelCurveField(
        multi=True, default_value=(0.0, 0.0)
    )
    obc = outerBevelCurve

    outerBevelDistance = FloatField(
        default_value=0.30000001192092896,
        soft_min_value=0.01,
        soft_max_value=1.0,
    )

    outerBevelDivisions = LongField(
        default_value=4, min_value=1, soft_max_value=10
    )

    bevelStyle = BevelStyleEnumField(default_value=1)

    vertexGroupIds = TypedField()
