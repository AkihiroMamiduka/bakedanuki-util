# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time_editor import AttributesField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class TimeEditor(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditor"

    composition = MessageField(multi=True)
    cmp = composition

    activeComposition = LongField()
    ac = activeComposition

    attributes = AttributesField(multi=True)
    ats = attributes

    nextClipId = LongField()
    ncid = nextClipId

    mute = BoolField()
    mt = mute
