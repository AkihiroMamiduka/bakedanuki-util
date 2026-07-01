# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.generic import GenericField
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class TrackPlugOperator(
    CompoundPlugOperator["TrackAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("index", "idx"),
        ("type", "typ"),
        ("trackName", "n"),
        ("trackMuted", "tm"),
        ("trackSolo", "ts"),
        ("trackGhost", "tgh"),
        ("trackSoloMute", "tsm"),
        ("trackHeight", "th"),
        ("useTrackColor", "utc"),
        ("trackColor", "tc"),
    )

    index = LongField()
    idx = index

    type = EnumField()
    typ = type

    trackName = DataStringField()
    n = trackName

    trackMuted = BoolField()
    tm = trackMuted

    trackSolo = BoolField()
    ts = trackSolo

    trackGhost = BoolField()
    tgh = trackGhost

    trackSoloMute = BoolField()
    tsm = trackSoloMute

    trackHeight = LongField()
    th = trackHeight

    useTrackColor = BoolField()
    utc = useTrackColor

    trackColor = Float3Field()
    tc = trackColor


class TrackAttrOperator(
    CompoundAttrOperator[TrackPlugOperator]
):
    __slots__ = ()

    index = LongField()
    idx = index

    type = EnumField()
    typ = type

    trackName = DataStringField()
    n = trackName

    trackMuted = BoolField()
    tm = trackMuted

    trackSolo = BoolField()
    ts = trackSolo

    trackGhost = BoolField()
    tgh = trackGhost

    trackSoloMute = BoolField()
    tsm = trackSoloMute

    trackHeight = LongField()
    th = trackHeight

    useTrackColor = BoolField()
    utc = useTrackColor

    trackColor = Float3Field()
    tc = trackColor


class TrackField(
    CompoundField[TrackAttrOperator, TrackPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrackAttrOperator
    PLUG_CLS = TrackPlugOperator


class CrossfadePlugOperator(
    CompoundPlugOperator["CrossfadeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("crossfadeClipId1", "cid1"),
        ("crossfadeClipId2", "cid2"),
        ("crossfadeMode", "cm"),
        ("crossfadeCurve", "cc"),
    )

    crossfadeClipId1 = MessageField()
    cid1 = crossfadeClipId1

    crossfadeClipId2 = MessageField()
    cid2 = crossfadeClipId2

    crossfadeMode = EnumField()
    cm = crossfadeMode

    crossfadeCurve = GenericField()
    cc = crossfadeCurve


class CrossfadeAttrOperator(
    CompoundAttrOperator[CrossfadePlugOperator]
):
    __slots__ = ()

    crossfadeClipId1 = MessageField()
    cid1 = crossfadeClipId1

    crossfadeClipId2 = MessageField()
    cid2 = crossfadeClipId2

    crossfadeMode = EnumField()
    cm = crossfadeMode

    crossfadeCurve = GenericField()
    cc = crossfadeCurve


class CrossfadeField(
    CompoundField[CrossfadeAttrOperator, CrossfadePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CrossfadeAttrOperator
    PLUG_CLS = CrossfadePlugOperator
