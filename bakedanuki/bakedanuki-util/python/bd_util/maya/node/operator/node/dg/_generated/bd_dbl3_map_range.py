# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_map_range import (
    InputField,
    OutputField,
    SourceMaximumField,
    SourceMinimumField,
    TargetMaximumField,
    TargetMinimumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField


class GeneratedBdDbl3MapRange(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_MapRange"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    sourceMinimum = SourceMinimumField(default_value=(0.0, 0.0, 0.0))
    smin = sourceMinimum
    sourceMinimumX = sourceMinimum.sourceMinimumX
    sminx = sourceMinimumX
    sourceMinimumY = sourceMinimum.sourceMinimumY
    sminy = sourceMinimumY
    sourceMinimumZ = sourceMinimum.sourceMinimumZ
    sminz = sourceMinimumZ

    sourceMaximum = SourceMaximumField(default_value=(1.0, 1.0, 1.0))
    smax = sourceMaximum
    sourceMaximumX = sourceMaximum.sourceMaximumX
    smaxx = sourceMaximumX
    sourceMaximumY = sourceMaximum.sourceMaximumY
    smaxy = sourceMaximumY
    sourceMaximumZ = sourceMaximum.sourceMaximumZ
    smaxz = sourceMaximumZ

    targetMinimum = TargetMinimumField(default_value=(0.0, 0.0, 0.0))
    tmin = targetMinimum
    targetMinimumX = targetMinimum.targetMinimumX
    tminx = targetMinimumX
    targetMinimumY = targetMinimum.targetMinimumY
    tminy = targetMinimumY
    targetMinimumZ = targetMinimum.targetMinimumZ
    tminz = targetMinimumZ

    targetMaximum = TargetMaximumField(default_value=(1.0, 1.0, 1.0))
    tmax = targetMaximum
    targetMaximumX = targetMaximum.targetMaximumX
    tmaxx = targetMaximumX
    targetMaximumY = targetMaximum.targetMaximumY
    tmaxy = targetMaximumY
    targetMaximumZ = targetMaximum.targetMaximumZ
    tmaxz = targetMaximumZ

    clamp = BoolField(default_value=True)
    c = clamp

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
