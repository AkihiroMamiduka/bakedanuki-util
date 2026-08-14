# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_decompose_bend_twist import (
    AxisQuatField,
    InputQuatField,
    OutputField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


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


class GeneratedBdQuatDecomposeBendTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_DecomposeBendTwist"

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
