# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataDouble3Plug(DataTypePlug["DataDouble3Attr"]):
    pass


class DataDouble3Attr(DataTypeAttr[DataDouble3Plug]):
    DATA_TYPE = "double3"
    PLUG_CLS = DataDouble3Plug
