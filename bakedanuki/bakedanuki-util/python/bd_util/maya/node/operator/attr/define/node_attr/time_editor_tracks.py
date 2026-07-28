# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class TypeEnumPlugOperator(EnumPlugOperator["TypeEnumAttrOperator"]):
    __slots__ = ()

    ANIMATION_TRACK = 0
    AUDIO_TRACK = 1


class TypeEnumAttrOperator(EnumAttrOperator[TypeEnumPlugOperator]):
    __slots__ = ()

    ANIMATION_TRACK = 0
    AUDIO_TRACK = 1

    NAME_MAP = {
        ANIMATION_TRACK: "Animation Track",
        AUDIO_TRACK: "Audio Track",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class CrossfadeModeEnumPlugOperator(EnumPlugOperator["CrossfadeModeEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 0
    STEP = 1
    HOLD_LEFT = 2
    HOLD_RIGHT = 3
    CUSTOM = 4


class CrossfadeModeEnumAttrOperator(EnumAttrOperator[CrossfadeModeEnumPlugOperator]):
    __slots__ = ()

    LINEAR = 0
    STEP = 1
    HOLD_LEFT = 2
    HOLD_RIGHT = 3
    CUSTOM = 4

    NAME_MAP = {
        LINEAR: "Linear",
        STEP: "Step",
        HOLD_LEFT: "Hold Left",
        HOLD_RIGHT: "Hold Right",
        CUSTOM: "Custom",
    }


class CrossfadeModeEnumField(
    EnumField[CrossfadeModeEnumAttrOperator, CrossfadeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CrossfadeModeEnumAttrOperator
    PLUG_CLS = CrossfadeModeEnumPlugOperator


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

    index = LongField(default_value=0)
    idx = index

    type = TypeEnumField(default_value=0)
    typ = type

    trackName = DataStringField()
    n = trackName

    trackMuted = BoolField(default_value=False)
    tm = trackMuted

    trackSolo = BoolField(default_value=False)
    ts = trackSolo

    trackGhost = BoolField(default_value=False)
    tgh = trackGhost

    trackSoloMute = BoolField(default_value=False)
    tsm = trackSoloMute

    trackHeight = LongField(default_value=32)
    th = trackHeight

    useTrackColor = BoolField(default_value=False)
    utc = useTrackColor

    trackColor = Float3Field(default_value=(0.21960000693798065, 0.21960000693798065, 0.21960000693798065))
    tc = trackColor


class TrackAttrOperator(
    CompoundAttrOperator[TrackPlugOperator]
):
    __slots__ = ()

    index = LongField(default_value=0)
    idx = index

    type = TypeEnumField(default_value=0)
    typ = type

    trackName = DataStringField()
    n = trackName

    trackMuted = BoolField(default_value=False)
    tm = trackMuted

    trackSolo = BoolField(default_value=False)
    ts = trackSolo

    trackGhost = BoolField(default_value=False)
    tgh = trackGhost

    trackSoloMute = BoolField(default_value=False)
    tsm = trackSoloMute

    trackHeight = LongField(default_value=32)
    th = trackHeight

    useTrackColor = BoolField(default_value=False)
    utc = useTrackColor

    trackColor = Float3Field(default_value=(0.21960000693798065, 0.21960000693798065, 0.21960000693798065))
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

    crossfadeClipId1 = MessageField(readable=False)
    cid1 = crossfadeClipId1

    crossfadeClipId2 = MessageField(readable=False)
    cid2 = crossfadeClipId2

    crossfadeMode = CrossfadeModeEnumField(default_value=0)
    cm = crossfadeMode

    crossfadeCurve = GenericField()
    cc = crossfadeCurve


class CrossfadeAttrOperator(
    CompoundAttrOperator[CrossfadePlugOperator]
):
    __slots__ = ()

    crossfadeClipId1 = MessageField(readable=False)
    cid1 = crossfadeClipId1

    crossfadeClipId2 = MessageField(readable=False)
    cid2 = crossfadeClipId2

    crossfadeMode = CrossfadeModeEnumField(default_value=0)
    cm = crossfadeMode

    crossfadeCurve = GenericField()
    cc = crossfadeCurve


class CrossfadeField(
    CompoundField[CrossfadeAttrOperator, CrossfadePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CrossfadeAttrOperator
    PLUG_CLS = CrossfadePlugOperator
