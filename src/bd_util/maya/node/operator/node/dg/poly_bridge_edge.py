# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_bridge_edge import TaperCurveField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class CurveTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    BLEND = 1
    CURVE = 2


class CurveTypeEnumAttrOperator(EnumAttrOperator):
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


class DirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    CUSTOM = 1


class DirectionEnumAttrOperator(EnumAttrOperator):
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


class SourceDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLUS = 0
    MINUS = 1


class SourceDirectionEnumAttrOperator(EnumAttrOperator):
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


class TargetDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLUS = 0
    MINUS = 1


class TargetDirectionEnumAttrOperator(EnumAttrOperator):
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


class PolyBridgeEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polyBridgeEdge"

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

    inputProfile = DataNurbsCurveField()
    ipc = inputProfile

    twist = DoubleAngleField()
    twt = twist

    taper = DoubleField()
    tp = taper

    taperCurve = TaperCurveField(multi=True)
    c = taperCurve

    divisions = LongField()
    dv = divisions

    startVert1 = LongField()
    sv1 = startVert1

    startVert2 = LongField()
    sv2 = startVert2

    bridgeOffset = LongField()
    bo = bridgeOffset

    curveType = CurveTypeEnumField()
    ctp = curveType

    smoothingAngle = DoubleAngleField()
    sma = smoothingAngle

    reverse = BoolField()
    rev = reverse

    direction = DirectionEnumField()
    d = direction

    sourceDirection = SourceDirectionEnumField()
    sd = sourceDirection

    targetDirection = TargetDirectionEnumField()
    td = targetDirection
