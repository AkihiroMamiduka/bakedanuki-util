# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataLong3Plug(DataTypePlug["DataLong3Attr"]):
    pass


class DataLong3Attr(DataTypeAttr[DataLong3Plug]):
    DATA_TYPE = "long3"
    PLUG_CLS = DataLong3Plug
