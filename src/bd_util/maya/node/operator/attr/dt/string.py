# coding: utf-8
from __future__ import annotations

# maya
from maya import cmds

# self
from ._core import DataTypeAttr, DataTypePlug


class DataStringPlug(DataTypePlug["DataStringAttr"]):
    def set(self, value: str):
        cmds.setAttr(self.plug, value, type="string")


class DataStringAttr(DataTypeAttr[DataStringPlug]):
    DATA_TYPE = "string"
    PLUG_CLS = DataStringPlug
