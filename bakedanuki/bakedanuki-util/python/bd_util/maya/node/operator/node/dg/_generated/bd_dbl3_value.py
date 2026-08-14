# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_value import ValueField


class GeneratedBdDbl3Value(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_Value"

    value = ValueField(default_value=(0.0, 0.0, 0.0))
    v = value
    valueX = value.valueX
    vx = valueX
    valueY = value.valueY
    vy = valueY
    valueZ = value.valueZ
    vz = valueZ
