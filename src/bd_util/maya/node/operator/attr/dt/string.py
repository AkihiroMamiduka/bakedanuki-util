# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataStringPlug(DataTypePlug["DataStringAttr"]):
    pass


class DataStringAttr(DataTypeAttr[DataStringPlug]):
    DATA_TYPE = "string"
    PLUG_CLS = DataStringPlug
