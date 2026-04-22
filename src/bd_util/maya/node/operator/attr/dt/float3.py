# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataFloat3Plug(DataTypePlug["DataFloat3Attr"]):
    pass


class DataFloat3Attr(DataTypeAttr[DataFloat3Plug]):
    DATA_TYPE = "float3"
    PLUG_CLS = DataFloat3Plug
