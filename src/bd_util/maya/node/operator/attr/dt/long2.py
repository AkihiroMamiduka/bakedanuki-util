# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataLong2Plug(DataTypePlug["DataLong2Attr"]):
    pass


class DataLong2Attr(DataTypeAttr[DataLong2Plug]):
    DATA_TYPE = "long2"
    PLUG_CLS = DataLong2Plug
