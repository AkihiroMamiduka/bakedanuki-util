# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_bridge_edge import TaperCurveField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class CurveTypeEnumPlugOperator(EnumPlugOperator["CurveTypeEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 0
    BLEND = 1
    CURVE = 2


class CurveTypeEnumAttrOperator(EnumAttrOperator[CurveTypeEnumPlugOperator]):
    __slots__ = ()

    LINEAR = 0
    BLEND = 1
    CURVE = 2

    NAME_MAP = {
        LINEAR: "Linear",
        BLEND: "Blend",
        CURVE: "Curve",
    }


class CurveTypeEnumField(
    EnumField[CurveTypeEnumAttrOperator, CurveTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveTypeEnumAttrOperator
    PLUG_CLS = CurveTypeEnumPlugOperator


class DirectionEnumPlugOperator(EnumPlugOperator["DirectionEnumAttrOperator"]):
    __slots__ = ()

    AUTO = 0
    CUSTOM = 1


class DirectionEnumAttrOperator(EnumAttrOperator[DirectionEnumPlugOperator]):
    __slots__ = ()

    AUTO = 0
    CUSTOM = 1

    NAME_MAP = {
        AUTO: "Auto",
        CUSTOM: "Custom",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class SourceDirectionEnumPlugOperator(
    EnumPlugOperator["SourceDirectionEnumAttrOperator"]
):
    __slots__ = ()

    PLUS = 0
    MINUS = 1


class SourceDirectionEnumAttrOperator(
    EnumAttrOperator[SourceDirectionEnumPlugOperator]
):
    __slots__ = ()

    PLUS = 0
    MINUS = 1

    NAME_MAP = {
        PLUS: "+",
        MINUS: "-",
    }


class SourceDirectionEnumField(
    EnumField[SourceDirectionEnumAttrOperator, SourceDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SourceDirectionEnumAttrOperator
    PLUG_CLS = SourceDirectionEnumPlugOperator


class TargetDirectionEnumPlugOperator(
    EnumPlugOperator["TargetDirectionEnumAttrOperator"]
):
    __slots__ = ()

    PLUS = 0
    MINUS = 1


class TargetDirectionEnumAttrOperator(
    EnumAttrOperator[TargetDirectionEnumPlugOperator]
):
    __slots__ = ()

    PLUS = 0
    MINUS = 1

    NAME_MAP = {
        PLUS: "+",
        MINUS: "-",
    }


class TargetDirectionEnumField(
    EnumField[TargetDirectionEnumAttrOperator, TargetDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetDirectionEnumAttrOperator
    PLUG_CLS = TargetDirectionEnumPlugOperator


class GeneratedPolyBridgeEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polyBridgeEdge"

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

    inputProfile = DataNurbsCurveField()
    ipc = inputProfile

    twist = DoubleAngleField(
        default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0
    )
    twt = twist

    taper = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=15.0
    )
    tp = taper

    taperCurve = TaperCurveField(multi=True, default_value=(0.0, 0.0, 0.0))
    c = taperCurve

    divisions = LongField(default_value=1, min_value=0)
    dv = divisions

    startVert1 = LongField(default_value=-1)
    sv1 = startVert1

    startVert2 = LongField(default_value=-1)
    sv2 = startVert2

    bridgeOffset = LongField(default_value=0, min_value=0)
    bo = bridgeOffset

    curveType = CurveTypeEnumField(default_value=0)
    ctp = curveType

    smoothingAngle = DoubleAngleField(
        default_value=29.999999999999996,
        soft_min_value=0.0,
        soft_max_value=180.0,
    )
    sma = smoothingAngle

    reverse = BoolField(default_value=False)
    rev = reverse

    direction = DirectionEnumField(default_value=0)
    d = direction

    sourceDirection = SourceDirectionEnumField(default_value=0)
    sd = sourceDirection

    targetDirection = TargetDirectionEnumField(default_value=0)
    td = targetDirection
