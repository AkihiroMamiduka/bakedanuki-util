# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_l3_map_range import (
    DstMaxField,
    DstMinField,
    InputField,
    OutputField,
    SrcMaxField,
    SrcMinField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField


class GeneratedBdDblL3MapRange(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL3_MapRange"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    srcMin = SrcMinField(default_value=(0.0, 0.0, 0.0))
    smin = srcMin
    srcMinX = srcMin.srcMinX
    sminx = srcMinX
    srcMinY = srcMin.srcMinY
    sminy = srcMinY
    srcMinZ = srcMin.srcMinZ
    sminz = srcMinZ

    srcMax = SrcMaxField(default_value=(1.0, 1.0, 1.0))
    smax = srcMax
    srcMaxX = srcMax.srcMaxX
    smaxx = srcMaxX
    srcMaxY = srcMax.srcMaxY
    smaxy = srcMaxY
    srcMaxZ = srcMax.srcMaxZ
    smaxz = srcMaxZ

    dstMin = DstMinField(default_value=(0.0, 0.0, 0.0))
    dmin = dstMin
    dstMinX = dstMin.dstMinX
    dminx = dstMinX
    dstMinY = dstMin.dstMinY
    dminy = dstMinY
    dstMinZ = dstMin.dstMinZ
    dminz = dstMinZ

    dstMax = DstMaxField(default_value=(1.0, 1.0, 1.0))
    dmax = dstMax
    dstMaxX = dstMax.dstMaxX
    dmaxx = dstMaxX
    dstMaxY = dstMax.dstMaxY
    dmaxy = dstMaxY
    dstMaxZ = dstMax.dstMaxZ
    dmaxz = dstMaxZ

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
