# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_quat_value import ValueField


class GeneratedBdQuatValue(DG):
    __slots__ = ()

    NODE_TYPE = "bdQuat_Value"

    value = ValueField(default_value=(0.0, 0.0, 0.0, 1.0))
    v = value
    valueX = value.valueX
    vx = valueX
    valueY = value.valueY
    vy = valueY
    valueZ = value.valueZ
    vz = valueZ
    valueW = value.valueW
    vw = valueW
