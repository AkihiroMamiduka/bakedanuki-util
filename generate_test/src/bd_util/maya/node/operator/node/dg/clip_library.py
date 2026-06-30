# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.clip_library import (
    CharacterdataField,
    ClipEvalListField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class ClipLibrary(DG):
    __slots__ = ()

    NODE_TYPE = "clipLibrary"

    clipEvalList = ClipEvalListField(multi=True)
    cel = clipEvalList

    clipFunction = TypedField()
    cf = clipFunction

    characterdata = CharacterdataField(multi=True)
    cd = characterdata

    activeClip = LongField()
    act = activeClip

    clipName = DataStringField(multi=True)
    cn = clipName

    start = TimeField(multi=True)
    st = start

    duration = TimeField(multi=True)
    du = duration

    sourceClip = MessageField(multi=True)
    sc = sourceClip

    clip = MessageField(multi=True)
    cl = clip
