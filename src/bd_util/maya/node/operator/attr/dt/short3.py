# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataShort3Plug(DataTypePlug["DataShort3Attr"]):
    pass


class DataShort3Attr(DataTypeAttr[DataShort3Plug]):
    DATA_TYPE = "short3"
    PLUG_CLS = DataShort3Plug
