# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.time_editor_tracks import (
    CrossfadeField,
    TrackField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField


class GeneratedTimeEditorTracks(DG):
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

    parentTime = TimeField(default_value=0.0, readable=False)
    ptm = parentTime

    clipTime = TimeField(multi=True, default_value=0.0, writable=False)
    ct = clipTime

    clipchanged = BoolField(default_value=False)
    clch = clipchanged

    state = TypedField(writable=False)
    st = state

    muted = BoolField(default_value=False)
    m = muted

    crossfade = CrossfadeField(multi=True)
    cr = crossfade
