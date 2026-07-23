# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.track_info_manager import (
    AudioTrackInfoField,
    TrackInfoField,
)


class _GeneratedTrackInfoManager(DG):
    __slots__ = ()

    NODE_TYPE = "trackInfoManager"

    trackInfo = TrackInfoField(multi=True)
    ti = trackInfo

    audioTrackInfo = AudioTrackInfoField(multi=True)
    ati = audioTrackInfo
