# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.euler_to_quat import (
    InputRotateField,
    OutputQuatField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class InputRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class InputRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class InputRotateOrderEnumField(
    EnumField[InputRotateOrderEnumAttrOperator, InputRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputRotateOrderEnumAttrOperator
    PLUG_CLS = InputRotateOrderEnumPlugOperator


class _GeneratedEulerToQuat(DG):
    __slots__ = ()

    NODE_TYPE = "eulerToQuat"

    inputRotate = InputRotateField(default_value=(0.0, 0.0, 0.0))
    irt = inputRotate
    inputRotateX = inputRotate.inputRotateX
    irx = inputRotateX
    inputRotateY = inputRotate.inputRotateY
    iry = inputRotateY
    inputRotateZ = inputRotate.inputRotateZ
    irz = inputRotateZ

    inputRotateOrder = InputRotateOrderEnumField(default_value=0)
    ro = inputRotateOrder

    outputQuat = OutputQuatField(default_value=(0.0, 0.0, 0.0, 0.0), writable=False)
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW
