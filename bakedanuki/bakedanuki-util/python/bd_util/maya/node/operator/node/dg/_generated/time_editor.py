# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.time_editor import AttributesField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedTimeEditor(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditor"

    composition = MessageField(multi=True, writable=False)
    cmp = composition

    activeComposition = LongField(default_value=-1)
    ac = activeComposition

    attributes = AttributesField(multi=True)
    ats = attributes

    nextClipId = LongField(default_value=1, min_value=1)
    ncid = nextClipId

    mute = BoolField(default_value=False)
    mt = mute
