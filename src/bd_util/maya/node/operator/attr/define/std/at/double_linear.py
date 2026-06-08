# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class DoubleLinearPlugOperator(PlugOperator["DoubleLinearAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMDistance().asCentimeters()

    # set
    def set(self, value: float):
        value = om.MDistance(value, om.MDistance.kCentimeters)
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)


class DoubleLinearAttrOperator(AttrOperator[DoubleLinearPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "doubleLinear"


class DoubleLinearField(
    AttributeField[DoubleLinearAttrOperator, DoubleLinearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DoubleLinearAttrOperator
    PLUG_CLS = DoubleLinearPlugOperator
