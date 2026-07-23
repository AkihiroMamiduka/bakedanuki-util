# coding: utf-8
from .._core import DG
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.unit_scalar.time import TimeField


class _GeneratedMute(DG):
    __slots__ = ()

    NODE_TYPE = "mute"

    input = GenericField()
    i = input

    hold = GenericField()
    h = hold

    holdTime = TimeField(default_value=0.0)
    ht = holdTime

    mute = BoolField(default_value=False)
    m = mute

    output = GenericField(writable=False)
    o = output
