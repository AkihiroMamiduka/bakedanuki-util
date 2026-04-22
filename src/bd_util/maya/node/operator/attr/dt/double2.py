# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataDouble2Plug(DataTypePlug["DataDouble2Attr"]):
    pass


class DataDouble2Attr(DataTypeAttr[DataDouble2Plug]):
    DATA_TYPE = "double2"
    PLUG_CLS = DataDouble2Plug
