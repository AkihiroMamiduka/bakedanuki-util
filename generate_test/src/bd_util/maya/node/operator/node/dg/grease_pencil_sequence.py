# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.grease_pencil_sequence import (
    ColorField,
    FrameField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField


class GreasePencilSequence(DG):
    __slots__ = ()

    NODE_TYPE = "greasePencilSequence"

    timeInput = TimeField()
    ti = timeInput

    blendLen = TimeField()
    bl = blendLen

    preGhost = BoolField()
    peg = preGhost

    preFrames = LongField()
    prf = preFrames

    postGhost = BoolField()
    pog = postGhost

    postFrames = LongField()
    pof = postFrames

    alphaMultiplier = FloatField()
    amp = alphaMultiplier

    color = ColorField()
    col = color
    colorR = color.colorR
    clr = colorR
    colorG = color.colorG
    clg = colorG
    colorB = color.colorB
    clb = colorB

    activeFrameIndex = LongField()
    afi = activeFrameIndex

    frame = FrameField(multi=True)
    k = frame
