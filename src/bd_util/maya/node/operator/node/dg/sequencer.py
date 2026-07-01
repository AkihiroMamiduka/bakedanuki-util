# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.unit_scalar.time import TimeField


class Sequencer(DG):
    __slots__ = ()

    NODE_TYPE = "sequencer"

    minFrame = TimeField()
    mnf = minFrame

    maxFrame = TimeField()
    mxf = maxFrame

    shots = MessageField(multi=True)
    shts = shots

    audio = MessageField(multi=True)
    aud = audio
