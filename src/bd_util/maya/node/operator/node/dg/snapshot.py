# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.snapshot import LocalPositionField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.point_array import DataPointArrayField


class UpdateEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEMAND = 0
    ALWAYS = 1
    ANIMCURVE = 2


class UpdateEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEMAND = 0
    ALWAYS = 1
    ANIMCURVE = 2

    NAME_MAP = {
        DEMAND: "demand",
        ALWAYS: "always",
        ANIMCURVE: "animCurve",
    }


class UpdateEnumField(
    EnumField[UpdateEnumAttrOperator, UpdateEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpdateEnumAttrOperator
    PLUG_CLS = UpdateEnumPlugOperator


class Snapshot(DG):
    __slots__ = ()

    NODE_TYPE = "snapshot"

    startTime = TimeField()
    s = startTime

    endTime = TimeField()
    e = endTime

    increment = TimeField()
    b = increment

    inputGeom = TypedField()
    in_ = inputGeom

    outputGeom = TypedField(multi=True)
    out = outputGeom

    inputMatrix = DataMatrixField()
    im = inputMatrix

    localPosition = LocalPositionField()
    lp = localPosition
    localPositionX = localPosition.localPositionX
    lpx = localPositionX
    localPositionY = localPosition.localPositionY
    lpy = localPositionY
    localPositionZ = localPosition.localPositionZ
    lpz = localPositionZ

    points = DataPointArrayField()
    pts = points

    frames = TypedField()
    f = frames

    animCurveChanged = MessageField()
    acc = animCurveChanged

    update = UpdateEnumField()
    up = update

    snapshotObject = MessageField()
    so = snapshotObject
