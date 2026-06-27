# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    NumericCompoundBasePlugOperator,
    NumericCompoundBaseAttrOperator,
    NumericCompoundBaseField,
)
from .....std.at.numeric_scalar_range.float import FloatField


class Float3PlugOperator(
    NumericCompoundBasePlugOperator["Float3AttrOperator"]
):
    __slots__ = ()

    CHILD_M_ATTR_TYPE: int = om.MFnNumericData.kFloat

    x = FloatField()
    y = FloatField()
    z = FloatField()

    # get
    def _get_child_value(self, child_plug) -> float:
        return child_plug.asFloat()

    # set
    def _set_child_value(self, child_plug, value: float):
        self._node._dg_mod.newPlugValueFloat(child_plug, value)


class Float3AttrOperator(NumericCompoundBaseAttrOperator[Float3PlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "float3"


class Float3Field(
    NumericCompoundBaseField[Float3AttrOperator, Float3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Float3AttrOperator
    PLUG_CLS = Float3PlugOperator
