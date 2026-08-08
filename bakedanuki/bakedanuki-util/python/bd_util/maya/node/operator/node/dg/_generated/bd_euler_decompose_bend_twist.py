# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_euler_decompose_bend_twist import (
    AxisRotateField,
    InputRotateField,
    OutputField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


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


class GeneratedBdEulerDecomposeBendTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdEuler_DecomposeBendTwist"

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

    order = OrderEnumField(default_value=0)
    ord = order

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputTwist = output.outputTwist
    otw = outputTwist
    outputBendH = output.outputBendH
    obh = outputBendH
    outputBendV = output.outputBendV
    obv = outputBendV

    bendRatio = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0, writable=False
    )
    br = bendRatio
