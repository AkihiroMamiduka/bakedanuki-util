# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.quat_normalize import (
    InputQuatField,
    OutputQuatField,
)


class QuatNormalize(DG):
    __slots__ = ()

    NODE_TYPE = "quatNormalize"

    inputQuat = InputQuatField()
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW

    outputQuat = OutputQuatField()
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW
