# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.set_range import (
    MaxField,
    MinField,
    OldMaxField,
    OldMinField,
    OutValueField,
    ValueField,
)


class GeneratedSetRange(DG):
    __slots__ = ()

    NODE_TYPE = "setRange"

    value = ValueField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(5.0, 5.0, 5.0),
    )
    v = value
    valueX = value.valueX
    vx = valueX
    valueY = value.valueY
    vy = valueY
    valueZ = value.valueZ
    vz = valueZ

    min = MinField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    n = min
    minX = min.minX
    nx = minX
    minY = min.minY
    ny = minY
    minZ = min.minZ
    nz = minZ

    max = MaxField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    m = max
    maxX = max.maxX
    mx = maxX
    maxY = max.maxY
    my = maxY
    maxZ = max.maxZ
    mz = maxZ

    oldMin = OldMinField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    on = oldMin
    oldMinX = oldMin.oldMinX
    onx = oldMinX
    oldMinY = oldMin.oldMinY
    ony = oldMinY
    oldMinZ = oldMin.oldMinZ
    onz = oldMinZ

    oldMax = OldMaxField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    om = oldMax
    oldMaxX = oldMax.oldMaxX
    omx = oldMaxX
    oldMaxY = oldMax.oldMaxY
    omy = oldMaxY
    oldMaxZ = oldMax.oldMaxZ
    omz = oldMaxZ

    outValue = OutValueField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = outValue
    outValueX = outValue.outValueX
    ox = outValueX
    outValueY = outValue.outValueY
    oy = outValueY
    outValueZ = outValue.outValueZ
    oz = outValueZ
