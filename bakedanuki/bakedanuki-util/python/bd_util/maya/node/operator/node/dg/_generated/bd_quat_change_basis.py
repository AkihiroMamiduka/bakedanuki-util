# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_change_basis import (
    AxisQuatField,
    InputQuatField,
    OutputQuatField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class DirectionEnumPlugOperator(EnumPlugOperator["DirectionEnumAttrOperator"]):
    __slots__ = ()

    APPLYAXIS = 0
    REMOVEAXIS = 1


class DirectionEnumAttrOperator(EnumAttrOperator[DirectionEnumPlugOperator]):
    __slots__ = ()

    APPLYAXIS = 0
    REMOVEAXIS = 1

    NAME_MAP = {
        APPLYAXIS: "ApplyAxis",
        REMOVEAXIS: "RemoveAxis",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class GeneratedBdQuatChangeBasis(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_ChangeBasis"

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

    direction = DirectionEnumField(default_value=0)
    dir = direction

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
