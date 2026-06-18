# coding: utf-8

# self
from ...std.at.base.numeric_compound_base import (
    NumericBasePlugOperator,
    NumericBaseAttrOperator,
    NumericBaseField,
)
from ...std.at.double import DoubleField


class Double3PlugOperator(NumericBasePlugOperator["Double3AttrOperator"]):
    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asDouble()

    # set
    def _set_child_value(self, child_plug, value: float):
        self._node._dg_mod.newPlugValueDouble(child_plug, value)


class Double3AttrOperator(NumericBaseAttrOperator[Double3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double3"


class Double3Field(NumericBaseField[Double3AttrOperator, Double3PlugOperator]):
    __slots__ = ()

    ATTR_CLS = Double3AttrOperator
    PLUG_CLS = Double3PlugOperator
