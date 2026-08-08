# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_euler_value import ValueField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class RotateOrderEnumPlugOperator(
    EnumPlugOperator["RotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(
    EnumAttrOperator[RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class GeneratedBdEulerValue(DG):
    __slots__ = ()

    NODE_TYPE = "bdEuler_Value"

    value = ValueField(default_value=(0.0, 0.0, 0.0))
    v = value
    valueX = value.valueX
    vx = valueX
    valueY = value.valueY
    vy = valueY
    valueZ = value.valueZ
    vz = valueZ

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder
