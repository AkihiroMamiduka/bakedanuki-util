# coding: utf-8
from ...._core import AttrOperator, PlugOperator, AttributeField


class FloatLinearPlugOperator(PlugOperator["FloatLinearAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMDistance()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMDistance(self.plug, value)

    def set_key_direct(self, value: float, frame: float):
        self._set_key_direct(value, frame)


class FloatLinearAttrOperator(AttrOperator[FloatLinearPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "floatLinear"


class FloatLinearField(
    AttributeField[FloatLinearAttrOperator, FloatLinearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatLinearAttrOperator
    PLUG_CLS = FloatLinearPlugOperator
