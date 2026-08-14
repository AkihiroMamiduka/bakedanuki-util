# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_compose_bend_twist import (
    AxisQuatField,
    InputField,
    OutputQuatField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


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


class GeneratedBdQuatComposeBendTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_ComposeBendTwist"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputTwist = input.inputTwist
    itw = inputTwist
    inputBendH = input.inputBendH
    ibh = inputBendH
    inputBendV = input.inputBendV
    ibv = inputBendV

    axisQuat = AxisQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    aq = axisQuat
    axisQuatX = axisQuat.axisQuatX
    aqx = axisQuatX
    axisQuatY = axisQuat.axisQuatY
    aqy = axisQuatY
    axisQuatZ = axisQuat.axisQuatZ
    aqz = axisQuatZ
    axisQuatW = axisQuat.axisQuatW
    aqw = axisQuatW

    order = OrderEnumField(default_value=0)
    ord = order

    outputQuat = OutputQuatField(
        default_value=(0.0, 0.0, 0.0, 1.0), writable=False
    )
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW
