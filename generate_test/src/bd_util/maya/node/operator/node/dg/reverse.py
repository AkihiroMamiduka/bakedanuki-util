# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.reverse import (
    InputField,
    OutputField,
)


class Reverse(DG):
    __slots__ = ()

    NODE_TYPE = "reverse"

    input = InputField()
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    output = OutputField()
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
