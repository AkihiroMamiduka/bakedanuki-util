# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.unit_scalar.time import TimeField


class Sequencer(DG):
    __slots__ = ()

    NODE_TYPE = "sequencer"

    minFrame = TimeField(default_value=0.01)
    mnf = minFrame

    maxFrame = TimeField(default_value=0.1)
    mxf = maxFrame

    shots = MessageField(multi=True, readable=False)
    shts = shots

    audio = MessageField(multi=True)
    aud = audio
