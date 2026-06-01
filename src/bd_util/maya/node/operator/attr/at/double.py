# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .._core import AttrOperator, PlugOperator


class DoublePlugOperator(PlugOperator["DoubleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asDouble()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueDouble(self.plug, value)


class DoubleAttrOperator(AttrOperator[DoublePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double"
    PLUG_CLS = DoublePlugOperator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # デフォルト値
        self._default_value = kwargs.get("default_value", 0.0)

    # add
    def add_attr(self, node_name: str):
        fn_node = super().add_attr(node_name)
        if fn_node is None:
            return

        fn_attr = om.MFnNumericAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            om.MFnNumericData.kDouble,
            self._default_value,
        )
        fn_node.addAttribute(attr_obj)

        if self._min_value is not None:
            fn_attr.setMin(self._min_value)
        if self._max_value is not None:
            fn_attr.setMax(self._max_value)

        if self._min_value is not None:
            fn_attr.setSoftMin(self._min_value)
        if self._max_value is not None:
            fn_attr.setSoftMax(self._max_value)
