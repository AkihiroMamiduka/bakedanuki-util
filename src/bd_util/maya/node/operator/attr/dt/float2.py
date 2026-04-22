# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataFloat2Plug(DataTypePlug["DataFloat2Attr"]):
    pass


class DataFloat2Attr(DataTypeAttr[DataFloat2Plug]):
    DATA_TYPE = "float2"
    PLUG_CLS = DataFloat2Plug
