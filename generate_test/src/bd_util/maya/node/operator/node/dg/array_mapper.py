# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.array_mapper import ComputeNodeColorField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class ArrayMapper(DG):
    __slots__ = ()

    NODE_TYPE = "arrayMapper"

    computeNode = MessageField()
    cn = computeNode

    uCoordPP = DataDoubleArrayField()
    upp = uCoordPP

    vCoordPP = DataDoubleArrayField()
    vpp = vCoordPP

    minValue = DoubleField()
    min = minValue

    maxValue = DoubleField()
    max = maxValue

    computeNodeColor = ComputeNodeColorField()
    cnc = computeNodeColor
    computeNodeColorR = computeNodeColor.computeNodeColorR
    cncr = computeNodeColorR
    computeNodeColorG = computeNodeColor.computeNodeColorG
    cncg = computeNodeColorG
    computeNodeColorB = computeNodeColor.computeNodeColorB
    cncb = computeNodeColorB

    time = TimeField()
    tim = time

    outColorPP = DataVectorArrayField()
    ocpp = outColorPP

    outValuePP = DataDoubleArrayField()
    ovpp = outValuePP
