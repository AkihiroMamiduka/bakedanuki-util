# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.snapshot import LocalPositionField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.point_array import DataPointArrayField


class UpdateEnumPlugOperator(EnumPlugOperator["UpdateEnumAttrOperator"]):
    __slots__ = ()

    DEMAND = 0
    ALWAYS = 1
    ANIMCURVE = 2


class UpdateEnumAttrOperator(EnumAttrOperator[UpdateEnumPlugOperator]):
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


class GeneratedSnapshot(DG):
    __slots__ = ()

    NODE_TYPE = "snapshot"

    startTime = TimeField(default_value=0.0)
    s = startTime

    endTime = TimeField(default_value=0.0)
    e = endTime

    increment = TimeField(default_value=2.5, min_value=0.01)
    b = increment

    inputGeom = TypedField()
    in_ = inputGeom

    outputGeom = TypedField(multi=True, writable=False)
    out = outputGeom

    inputMatrix = DataMatrixField()
    im = inputMatrix

    localPosition = LocalPositionField(default_value=(0.0, 0.0, 0.0))
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

    animCurveChanged = MessageField(writable=False)
    acc = animCurveChanged

    update = UpdateEnumField(default_value=1, writable=False)
    up = update

    snapshotObject = MessageField()
    so = snapshotObject
