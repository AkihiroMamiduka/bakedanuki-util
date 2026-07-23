# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.dt.string import DataStringField


class TrackInfoPlugOperator(
    CompoundPlugOperator["TrackInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("title", "t"),
    )

    title = DataStringField()
    t = title


class TrackInfoAttrOperator(
    CompoundAttrOperator[TrackInfoPlugOperator]
):
    __slots__ = ()

    title = DataStringField()
    t = title


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
    )

    audioTitle = DataStringField()
    at = audioTitle


class AudioTrackInfoAttrOperator(
    CompoundAttrOperator[AudioTrackInfoPlugOperator]
):
    __slots__ = ()

    audioTitle = DataStringField()
    at = audioTitle


class AudioTrackInfoField(
    CompoundField[AudioTrackInfoAttrOperator, AudioTrackInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AudioTrackInfoAttrOperator
    PLUG_CLS = AudioTrackInfoPlugOperator
