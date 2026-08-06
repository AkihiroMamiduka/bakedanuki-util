# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_multiply_multi import (
    InputQuatField,
    OutputQuatField,
)


class GeneratedBdQuatMultiplyMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_MultiplyMulti"

    inputQuat = InputQuatField(multi=True, default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat

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
