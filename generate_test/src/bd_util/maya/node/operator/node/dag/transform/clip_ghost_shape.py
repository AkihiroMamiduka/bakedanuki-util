# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.clip_ghost_shape import ColorField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField


class ClipGhostShape(Transform):
    __slots__ = ()

    NODE_TYPE = "clipGhostShape"

    clipGhostData = TypedField()
    cgd = clipGhostData

    clipData = TypedField(writable=False)
    cd = clipData

    showStartPose = BoolField(default_value=True)
    ssp = showStartPose

    showEndPose = BoolField(default_value=True)
    sep = showEndPose

    showIntermediatePoses = BoolField(default_value=True)
    sip = showIntermediatePoses

    showClipPath = BoolField(default_value=True)
    scp = showClipPath

    intermediatePoses = LongField(default_value=0, min_value=0)
    ip = intermediatePoses

    clipDirectionScale = DoubleField(default_value=1.4, min_value=0.0)
    cds = clipDirectionScale

    color = ColorField(default_value=(0.06700000166893005, 0.0860000029206276, 0.3799999952316284))
    col = color
    colorR = color.colorR
    colr = colorR
    colorG = color.colorG
    colg = colorG
    colorB = color.colorB
    colb = colorB

    trackMuted = BoolField(default_value=False)
    tm = trackMuted

    clipEnabled = BoolField(default_value=True)
    ce = clipEnabled
