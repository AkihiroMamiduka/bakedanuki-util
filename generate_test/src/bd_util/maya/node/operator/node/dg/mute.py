# coding: utf-8
from ._core import DG
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar.time import TimeField


class Mute(DG):
    __slots__ = ()

    NODE_TYPE = "mute"

    input = GenericField()
    i = input

    hold = GenericField()
    h = hold

    holdTime = TimeField()
    ht = holdTime

    mute = BoolField()
    m = mute

    output = GenericField()
    o = output
