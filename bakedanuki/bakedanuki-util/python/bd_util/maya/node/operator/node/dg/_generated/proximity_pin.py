# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


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


class CoordModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EDGE = 0
    UV = 1


class CoordModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EDGE = 0
    UV = 1

    NAME_MAP = {
        EDGE: "Edge",
        UV: "UV",
    }


class CoordModeEnumField(
    EnumField[CoordModeEnumAttrOperator, CoordModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordModeEnumAttrOperator
    PLUG_CLS = CoordModeEnumPlugOperator


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
    NONE = 6


class TangentAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5
    NONE = 6

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
        MINUS_X: "-X",
        MINUS_Y: "-Y",
        MINUS_Z: "-Z",
        NONE: "None",
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


class _GeneratedProximityPin(DG):
    __slots__ = ()

    NODE_TYPE = "proximityPin"

    deformedGeometry = TypedField()
    curgeom = deformedGeometry

    originalGeometry = TypedField()
    orggeom = originalGeometry

    normalOverride = NormalOverrideEnumField(default_value=0)
    novr = normalOverride

    railCurve = TypedField()
    rlcrv = railCurve

    originalRailCurve = TypedField()
    orlcrv = originalRailCurve

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=3.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    inputMatrix = MatrixField(multi=True)
    imat = inputMatrix

    coordMode = CoordModeEnumField(default_value=0)
    crdm = coordMode

    offsetTranslation = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ostr = offsetTranslation

    offsetOrientation = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    osor = offsetOrientation

    uvSetName = DataStringField()
    msn = uvSetName

    normalAxis = NormalAxisEnumField(default_value=0)
    nrm = normalAxis

    tangentAxis = TangentAxisEnumField(default_value=2)
    tng = tangentAxis

    relativeSpaceMode = RelativeSpaceModeEnumField(default_value=0)
    rsmd = relativeSpaceMode

    relativeSpaceMatrix = MatrixField()
    rsmat = relativeSpaceMatrix

    outputMatrix = MatrixField(multi=True, writable=False)
    omat = outputMatrix
