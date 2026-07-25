# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.clip_library import (
    CharacterdataField,
    ClipEvalListField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedClipLibrary(DG):
    __slots__ = ()

    NODE_TYPE = "clipLibrary"

    clipEvalList = ClipEvalListField(multi=True)
    cel = clipEvalList

    clipFunction = TypedField(writable=False)
    cf = clipFunction

    characterdata = CharacterdataField(multi=True)
    cd = characterdata

    activeClip = LongField(default_value=-1)
    act = activeClip

    clipName = DataStringField(multi=True)
    cn = clipName

    start = TimeField(multi=True, default_value=0.0)
    st = start

    duration = TimeField(multi=True, default_value=0.0)
    du = duration

    sourceClip = MessageField(multi=True)
    sc = sourceClip

    clip = MessageField(multi=True)
    cl = clip
