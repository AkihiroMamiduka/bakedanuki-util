# coding: utf-8
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
