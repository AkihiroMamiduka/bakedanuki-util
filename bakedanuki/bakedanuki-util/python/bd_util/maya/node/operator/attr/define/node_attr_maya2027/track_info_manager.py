# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.short import ShortField
from ..std.dt.string import DataStringField


class TrackInfoPlugOperator(CompoundPlugOperator["TrackInfoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("title", "t"),
        ("trackState", "ts"),
    )

    title = DataStringField()
    t = title

    trackState = ShortField(default_value=0, min_value=0)
    ts = trackState


class TrackInfoAttrOperator(CompoundAttrOperator[TrackInfoPlugOperator]):
    __slots__ = ()

    title = DataStringField()
    t = title

    trackState = ShortField(default_value=0, min_value=0)
    ts = trackState


class TrackInfoField(
    CompoundField[TrackInfoAttrOperator, TrackInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrackInfoAttrOperator
    PLUG_CLS = TrackInfoPlugOperator


class AudioTrackInfoPlugOperator(
    CompoundPlugOperator["AudioTrackInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("audioTitle", "at"),
        ("audioTrackState", "ats"),
    )

    audioTitle = DataStringField()
    at = audioTitle

    audioTrackState = ShortField(default_value=0, min_value=0)
    ats = audioTrackState


class AudioTrackInfoAttrOperator(
    CompoundAttrOperator[AudioTrackInfoPlugOperator]
):
    __slots__ = ()

    audioTitle = DataStringField()
    at = audioTitle

    audioTrackState = ShortField(default_value=0, min_value=0)
    ats = audioTrackState


class AudioTrackInfoField(
    CompoundField[AudioTrackInfoAttrOperator, AudioTrackInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AudioTrackInfoAttrOperator
    PLUG_CLS = AudioTrackInfoPlugOperator
