# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.type_extrude import (
    BackBevelCurveField,
    ExtrudeCurveField,
    FrontBevelCurveField,
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


class TypeExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "typeExtrude"

    inputMesh = DataMeshField()
    in_ = inputMesh

    outputMesh = DataMeshField()
    out = outputMesh

    mode = ModeEnumField()
    md = mode

    enableExtrusion = BoolField()
    enEx = enableExtrusion

    extrudeDivisions = LongField()
    exdv = extrudeDivisions

    extrudeDistance = FloatField()
    exds = extrudeDistance

    extrudeOffset = FloatField()
    exof = extrudeOffset

    extrudeCurve = ExtrudeCurveField(multi=True)
    exc = extrudeCurve

    deleteCaps = BoolField()
    dcs = deleteCaps

    gridSize = LongField()
    gs = gridSize

    bevelOffset = FloatField()
    bof = bevelOffset

    frontBevelCurve = FrontBevelCurveField(multi=True)
    fbc = frontBevelCurve

    bevelDivisions = LongField()
    bdv = bevelDivisions

    bevelDistance = FloatField()
    bds = bevelDistance

    capGroupId = LongField()
    cid = capGroupId

    bevelGroupId = LongField()
    bid = bevelGroupId

    extrudeGroupId = LongField()
    eid = extrudeGroupId

    defaultGroupId = LongField()
    did = defaultGroupId

    enableBackBevel = BoolField()
    ebb = enableBackBevel

    backBevelOffset = FloatField()
    bbof = backBevelOffset

    backBevelCurve = BackBevelCurveField(multi=True)
    bbc = backBevelCurve

    backBevelDivisions = LongField()
    bbdv = backBevelDivisions

    backBevelDistance = FloatField()
    bbds = backBevelDistance

    rearBevelUsesFront = BoolField()
    rbuf = rearBevelUsesFront

    enableCapShader = BoolField()
    ecs = enableCapShader

    enableBevelShader = BoolField()
    ebs = enableBevelShader

    enableExtrudeShader = BoolField()
    ees = enableExtrudeShader

    outComponents = OutComponentsField()
    capComponents = outComponents.capComponents
    bevelComponents = outComponents.bevelComponents
    extrusionComponents = outComponents.extrusionComponents

    charGroupId = LongField(multi=True)

    vertsPerChar = DataDoubleArrayField()

    offsetFrontBevelAsFraction = BoolField()

    offsetBackBevelAsFraction = BoolField()

    offsetExtrudeAsFraction = BoolField()

    enableFrontBevel = BoolField()

    enableOuterBevel = BoolField()

    outerBevelCurve = OuterBevelCurveField(multi=True)
    obc = outerBevelCurve

    outerBevelDistance = FloatField()

    outerBevelDivisions = LongField()

    bevelStyle = BevelStyleEnumField()

    vertexGroupIds = TypedField()
