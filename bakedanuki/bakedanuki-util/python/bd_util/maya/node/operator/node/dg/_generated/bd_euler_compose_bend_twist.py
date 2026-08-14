# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_euler_compose_bend_twist import (
    AxisRotateField,
    InputField,
    OutputRotateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


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


class OrderEnumPlugOperator(EnumPlugOperator["OrderEnumAttrOperator"]):
    __slots__ = ()

    TWISTBEND = 0
    BENDTWIST = 1


class OrderEnumAttrOperator(EnumAttrOperator[OrderEnumPlugOperator]):
    __slots__ = ()

    TWISTBEND = 0
    BENDTWIST = 1

    NAME_MAP = {
        TWISTBEND: "TwistBend",
        BENDTWIST: "BendTwist",
    }


class OrderEnumField(EnumField[OrderEnumAttrOperator, OrderEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OrderEnumAttrOperator
    PLUG_CLS = OrderEnumPlugOperator


class OutputRotateOrderEnumPlugOperator(
    EnumPlugOperator["OutputRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class OutputRotateOrderEnumAttrOperator(
    EnumAttrOperator[OutputRotateOrderEnumPlugOperator]
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


class OutputRotateOrderEnumField(
    EnumField[
        OutputRotateOrderEnumAttrOperator, OutputRotateOrderEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateOrderEnumAttrOperator
    PLUG_CLS = OutputRotateOrderEnumPlugOperator


class GeneratedBdEulerComposeBendTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdEuler_ComposeBendTwist"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputTwist = input.inputTwist
    itw = inputTwist
    inputBendH = input.inputBendH
    ibh = inputBendH
    inputBendV = input.inputBendV
    ibv = inputBendV

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

    order = OrderEnumField(default_value=0)
    ord = order

    outputRotateOrder = OutputRotateOrderEnumField(default_value=0)
    oro = outputRotateOrder

    outputRotate = OutputRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ort = outputRotate
    outputRotateX = outputRotate.outputRotateX
    orx = outputRotateX
    outputRotateY = outputRotate.outputRotateY
    ory = outputRotateY
    outputRotateZ = outputRotate.outputRotateZ
    orz = outputRotateZ
