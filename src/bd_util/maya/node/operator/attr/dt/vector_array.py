# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataVectorArrayPlug(DataTypePlug["DataVectorArrayAttr"]):
    pass


class DataVectorArrayAttr(DataTypeAttr[DataVectorArrayPlug]):
    DATA_TYPE = "vectorArray"
    PLUG_CLS = DataVectorArrayPlug
