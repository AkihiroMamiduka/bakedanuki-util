# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_limit_bend_twist import (
    AxisQuatField,
    InputQuatField,
    MaxField,
    MinField,
    OutputField,
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


class BendLimitModeEnumPlugOperator(
    EnumPlugOperator["BendLimitModeEnumAttrOperator"]
):
    __slots__ = ()

    BOX = 0
    ELLIPSE = 1


class BendLimitModeEnumAttrOperator(
    EnumAttrOperator[BendLimitModeEnumPlugOperator]
):
    __slots__ = ()

    BOX = 0
    ELLIPSE = 1

    NAME_MAP = {
        BOX: "Box",
        ELLIPSE: "Ellipse",
    }


class BendLimitModeEnumField(
    EnumField[BendLimitModeEnumAttrOperator, BendLimitModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BendLimitModeEnumAttrOperator
    PLUG_CLS = BendLimitModeEnumPlugOperator


class GeneratedBdQuatLimitBendTwist(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_LimitBendTwist"

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

    bendLimitMode = BendLimitModeEnumField(default_value=0)
    blm = bendLimitMode

    min = MinField(default_value=(-180.0, -180.0, -180.0))
    mn = min
    minTwist = min.minTwist
    mntw = minTwist
    minBendH = min.minBendH
    mnbh = minBendH
    minBendV = min.minBendV
    mnbv = minBendV

    max = MaxField(default_value=(180.0, 180.0, 180.0))
    mx = max
    maxTwist = max.maxTwist
    mxtw = maxTwist
    maxBendH = max.maxBendH
    mxbh = maxBendH
    maxBendV = max.maxBendV
    mxbv = maxBendV

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputTwist = output.outputTwist
    otw = outputTwist
    outputBendH = output.outputBendH
    obh = outputBendH
    outputBendV = output.outputBendV
    obv = outputBendV

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
