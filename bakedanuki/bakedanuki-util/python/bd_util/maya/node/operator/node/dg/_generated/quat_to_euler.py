# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.quat_to_euler import (
    InputQuatField,
    OutputRotateField,
)
from ....attr.define.std.at.scalar.enum import (
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


class GeneratedQuatToEuler(DG):
    __slots__ = ()

    NODE_TYPE = "quatToEuler"

    inputQuat = InputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW

    inputRotateOrder = InputRotateOrderEnumField(default_value=0)
    iro = inputRotateOrder

    outputRotate = OutputRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    ort = outputRotate
    outputRotateX = outputRotate.outputRotateX
    orx = outputRotateX
    outputRotateY = outputRotate.outputRotateY
    ory = outputRotateY
    outputRotateZ = outputRotate.outputRotateZ
    orz = outputRotateZ
