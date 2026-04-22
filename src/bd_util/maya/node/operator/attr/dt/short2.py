# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataShort2Plug(DataTypePlug["DataShort2Attr"]):
    pass


class DataShort2Attr(DataTypeAttr[DataShort2Plug]):
    DATA_TYPE = "short2"
    PLUG_CLS = DataShort2Plug
