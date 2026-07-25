# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.array_mapper import ComputeNodeColorField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class _GeneratedArrayMapper(DG):
    __slots__ = ()

    NODE_TYPE = "arrayMapper"

    computeNode = MessageField(readable=False)
    cn = computeNode

    uCoordPP = DataDoubleArrayField()
    upp = uCoordPP

    vCoordPP = DataDoubleArrayField()
    vpp = vCoordPP

    minValue = DoubleField(default_value=0.0)
    min = minValue

    maxValue = DoubleField(default_value=1.0)
    max = maxValue

    computeNodeColor = ComputeNodeColorField(default_value=(0.0, 0.0, 0.0))
    cnc = computeNodeColor
    computeNodeColorR = computeNodeColor.computeNodeColorR
    cncr = computeNodeColorR
    computeNodeColorG = computeNodeColor.computeNodeColorG
    cncg = computeNodeColorG
    computeNodeColorB = computeNodeColor.computeNodeColorB
    cncb = computeNodeColorB

    time = TimeField(default_value=0.0)
    tim = time

    outColorPP = DataVectorArrayField(writable=False)
    ocpp = outColorPP

    outValuePP = DataDoubleArrayField(writable=False)
    ovpp = outValuePP
