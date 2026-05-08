# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataPointArrayPlug(DataTypePlug["DataPointArrayAttr"]):
    pass


class DataPointArrayAttr(DataTypeAttr[DataPointArrayPlug]):
    DATA_TYPE = "pointArray"
    PLUG_CLS = DataPointArrayPlug
