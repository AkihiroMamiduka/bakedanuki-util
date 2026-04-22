# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataInt32ArrayPlug(DataTypePlug["DataInt32ArrayAttr"]):
    pass


class DataInt32ArrayAttr(DataTypeAttr[DataInt32ArrayPlug]):
    DATA_TYPE = "int32Array"
    PLUG_CLS = DataInt32ArrayPlug
