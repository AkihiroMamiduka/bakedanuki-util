# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.rotate_helper import (
    ForwardField,
    RotateField,
    UpField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField


class RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(EnumAttrOperator):
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


class RotateHelper(DG):
    __slots__ = ()

    NODE_TYPE = "rotateHelper"

    up = UpField(default_value=(0.0, 1.0, 0.0))
    u = up
    upX = up.upX
    ux = upX
    upY = up.upY
    uy = upY
    upZ = up.upZ
    uz = upZ

    forward = ForwardField(default_value=(0.0, 0.0, 1.0))
    f = forward
    forwardX = forward.forwardX
    fx = forwardX
    forwardY = forward.forwardY
    fy = forwardY
    forwardZ = forward.forwardZ
    fz = forwardZ

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    r = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder

    rotateMatrix = MatrixField()
    rm = rotateMatrix
