# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataDoubleArrayPlug(DataTypePlug["DataDoubleArrayAttr"]):
    pass


class DataDoubleArrayAttr(DataTypeAttr[DataDoubleArrayPlug]):
    DATA_TYPE = "doubleArray"
    PLUG_CLS = DataDoubleArrayPlug
