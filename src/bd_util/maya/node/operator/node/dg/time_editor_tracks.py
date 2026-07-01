# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time_editor_tracks import (
    CrossfadeField,
    TrackField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField


class TimeEditorTracks(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorTracks"

    track = TrackField(multi=True)
    t = track

    trackColorR = FloatField()
    tcr = trackColorR

    trackColorG = FloatField()
    tcg = trackColorG

    trackColorB = FloatField()
    tcb = trackColorB

    clip = MessageField()
    c = clip

    composition = MessageField()
    cmp = composition

    parentTime = TimeField()
    ptm = parentTime

    clipTime = TimeField(multi=True)
    ct = clipTime

    clipchanged = BoolField()
    clch = clipchanged

    state = TypedField()
    st = state

    muted = BoolField()
    m = muted

    crossfade = CrossfadeField(multi=True)
    cr = crossfade
