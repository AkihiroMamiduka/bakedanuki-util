# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataStringArrayPlug(DataTypePlug["DataStringArrayAttr"]):
    pass


class DataStringArrayAttr(DataTypeAttr[DataStringArrayPlug]):
    DATA_TYPE = "stringArray"
    PLUG_CLS = DataStringArrayPlug
