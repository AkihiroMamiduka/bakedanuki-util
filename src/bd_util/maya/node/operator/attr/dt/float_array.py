# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataFloatArrayPlug(DataTypePlug["DataFloatArrayAttr"]):
    pass


class DataFloatArrayAttr(DataTypeAttr[DataFloatArrayPlug]):
    DATA_TYPE = "floatArray"
    PLUG_CLS = DataFloatArrayPlug
