# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.quat_negate import (
    InputQuatField,
    OutputQuatField,
)


class GeneratedQuatNegate(DG):
    __slots__ = ()

    NODE_TYPE = "quatNegate"

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

    outputQuat = OutputQuatField(
        default_value=(0.0, 0.0, 0.0, 0.0), writable=False
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
