# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.grease_pencil_sequence import (
    ColorField,
    FrameField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField


class GeneratedGreasePencilSequence(DG):
    __slots__ = ()

    NODE_TYPE = "greasePencilSequence"

    timeInput = TimeField(default_value=0.0)
    ti = timeInput

    blendLen = TimeField(default_value=2.5, min_value=0.0, max_value=120.0)
    bl = blendLen

    preGhost = BoolField(default_value=True)
    peg = preGhost

    preFrames = LongField(default_value=1, min_value=0, max_value=10)
    prf = preFrames

    postGhost = BoolField(default_value=True)
    pog = postGhost

    postFrames = LongField(default_value=1, min_value=0, max_value=10)
    pof = postFrames

    alphaMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    amp = alphaMultiplier

    color = ColorField(
        default_value=(
            0.5609999895095825,
            0.7570000290870667,
            0.8119999766349792,
        )
    )
    col = color
    colorR = color.colorR
    clr = colorR
    colorG = color.colorG
    clg = colorG
    colorB = color.colorB
    clb = colorB

    activeFrameIndex = LongField(default_value=0)
    afi = activeFrameIndex

    frame = FrameField(multi=True)
    k = frame
