# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.rotate_vector import (
    InputField,
    OutputField,
    RotateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


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


class RotateVector(DG):
    __slots__ = ()

    NODE_TYPE = "rotateVector"

    input = InputField()
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    rotate = RotateField()
    r = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    rotateOrder = RotateOrderEnumField()
    ro = rotateOrder

    output = OutputField()
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
