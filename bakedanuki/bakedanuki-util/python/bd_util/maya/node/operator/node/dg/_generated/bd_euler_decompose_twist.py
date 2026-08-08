# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_euler_decompose_twist import (
    AxisRotateField,
    InputRotateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class InputRotateOrderEnumPlugOperator(
    EnumPlugOperator["InputRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class InputRotateOrderEnumAttrOperator(
    EnumAttrOperator[InputRotateOrderEnumPlugOperator]
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


class InputRotateOrderEnumField(
    EnumField[
        InputRotateOrderEnumAttrOperator, InputRotateOrderEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputRotateOrderEnumAttrOperator
    PLUG_CLS = InputRotateOrderEnumPlugOperator


class AxisRotateOrderEnumPlugOperator(
    EnumPlugOperator["AxisRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class AxisRotateOrderEnumAttrOperator(
    EnumAttrOperator[AxisRotateOrderEnumPlugOperator]
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


class AxisRotateOrderEnumField(
    EnumField[AxisRotateOrderEnumAttrOperator, AxisRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisRotateOrderEnumAttrOperator
    PLUG_CLS = AxisRotateOrderEnumPlugOperator


class GeneratedBdEulerDecomposeTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdEuler_DecomposeTwist"

    inputRotate = InputRotateField(default_value=(0.0, 0.0, 0.0))
    ir = inputRotate
    inputRotateX = inputRotate.inputRotateX
    irx = inputRotateX
    inputRotateY = inputRotate.inputRotateY
    iry = inputRotateY
    inputRotateZ = inputRotate.inputRotateZ
    irz = inputRotateZ

    inputRotateOrder = InputRotateOrderEnumField(default_value=0)
    iro = inputRotateOrder

    axisRotate = AxisRotateField(default_value=(0.0, 0.0, 0.0))
    ar = axisRotate
    axisRotateX = axisRotate.axisRotateX
    arx = axisRotateX
    axisRotateY = axisRotate.axisRotateY
    ary = axisRotateY
    axisRotateZ = axisRotate.axisRotateZ
    arz = axisRotateZ

    axisRotateOrder = AxisRotateOrderEnumField(default_value=0)
    aro = axisRotateOrder

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist
