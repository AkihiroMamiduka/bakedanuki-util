# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.time_editor_anim_source import AnimationField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.unit_scalar.time import TimeField


class _GeneratedTimeEditorAnimSource(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorAnimSource"

    animation = AnimationField(multi=True)
    an = animation

    start = TimeField(default_value=0.0)
    s = start

    duration = TimeField(default_value=0.0)
    d = duration

    initialClipStart = TimeField(default_value=0.0)
    ics = initialClipStart

    initialClipDuration = TimeField(default_value=0.0)
    icd = initialClipDuration

    initialClipAbsoluteDuration = TimeField(default_value=0.0)
    iad = initialClipAbsoluteDuration

    rosters = MessageField()
    rs = rosters

    blendShapeSource = BoolField(default_value=False, writable=False)
    bs = blendShapeSource
