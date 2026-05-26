# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttr, DataTypePlug


class DataStringPlug(DataTypePlug["DataStringAttr"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        return self.plug.asString()

    # set
    def set(self, value: str):
        self._node._dg_mod.newPlugValueString(self.plug, value)


class DataStringAttr(DataTypeAttr[DataStringPlug]):
    __slots__ = ()

    DATA_TYPE = "string"
    PLUG_CLS = DataStringPlug

    # add
    def add_attr(self, node_name: str):
        fn_node = super().add_attr(node_name)
        if fn_node is None:
            return

        fn_attr = om.MFnTypedAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            om.MFnData.kString,
        )
        fn_node.addAttribute(attr_obj)
