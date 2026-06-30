# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.uv_pin import (
    CoordinateField,
    OutputTranslateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class NormalOverrideEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    RAIL_CURVE = 1


class NormalOverrideEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    RAIL_CURVE = 1

    NAME_MAP = {
        AUTO: "Auto",
        RAIL_CURVE: "Rail Curve",
    }


class NormalOverrideEnumField(
    EnumField[NormalOverrideEnumAttrOperator, NormalOverrideEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalOverrideEnumAttrOperator
    PLUG_CLS = NormalOverrideEnumPlugOperator


class NormalAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5


class NormalAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
        MINUS_X: "-X",
        MINUS_Y: "-Y",
        MINUS_Z: "-Z",
    }


class NormalAxisEnumField(
    EnumField[NormalAxisEnumAttrOperator, NormalAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAxisEnumAttrOperator
    PLUG_CLS = NormalAxisEnumPlugOperator


class TangentAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5


class TangentAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
        MINUS_X: "-X",
        MINUS_Y: "-Y",
        MINUS_Z: "-Z",
    }


class TangentAxisEnumField(
    EnumField[TangentAxisEnumAttrOperator, TangentAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentAxisEnumAttrOperator
    PLUG_CLS = TangentAxisEnumPlugOperator


class RelativeSpaceModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    CUSTOM = 2


class RelativeSpaceModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    CUSTOM = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
        CUSTOM: "Custom",
    }


class RelativeSpaceModeEnumField(
    EnumField[RelativeSpaceModeEnumAttrOperator, RelativeSpaceModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelativeSpaceModeEnumAttrOperator
    PLUG_CLS = RelativeSpaceModeEnumPlugOperator


class UvPin(DG):
    __slots__ = ()

    NODE_TYPE = "uvPin"

    deformedGeometry = TypedField()
    curgeom = deformedGeometry

    originalGeometry = TypedField()
    orggeom = originalGeometry

    normalOverride = NormalOverrideEnumField()
    novr = normalOverride

    railCurve = TypedField()
    rlcrv = railCurve

    coordinate = CoordinateField(multi=True)
    coord = coordinate

    uvSetName = DataStringField()
    msn = uvSetName

    normalAxis = NormalAxisEnumField()
    nrm = normalAxis

    tangentAxis = TangentAxisEnumField()
    tng = tangentAxis

    normalizedIsoParms = BoolField()
    nrmip = normalizedIsoParms

    relativeSpaceMode = RelativeSpaceModeEnumField()
    rsmd = relativeSpaceMode

    relativeSpaceMatrix = MatrixField()
    rsmat = relativeSpaceMatrix

    outputTranslate = OutputTranslateField(multi=True)
    ot = outputTranslate

    outputMatrix = MatrixField(multi=True)
    omat = outputMatrix
