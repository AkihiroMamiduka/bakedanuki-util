# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.time_editor_anim_source import AnimationField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar.time import TimeField


class TimeEditorAnimSource(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorAnimSource"

    animation = AnimationField(multi=True)
    an = animation

    start = TimeField()
    s = start

    duration = TimeField()
    d = duration

    initialClipStart = TimeField()
    ics = initialClipStart

    initialClipDuration = TimeField()
    icd = initialClipDuration

    initialClipAbsoluteDuration = TimeField()
    iad = initialClipAbsoluteDuration

    rosters = MessageField()
    rs = rosters

    blendShapeSource = BoolField()
    bs = blendShapeSource
