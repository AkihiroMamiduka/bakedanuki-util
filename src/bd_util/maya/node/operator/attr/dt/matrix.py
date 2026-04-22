# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataMatrixPlug(DataTypePlug["DataMatrixAttr"]):
    pass


class DataMatrixAttr(DataTypeAttr[DataMatrixPlug]):
    DATA_TYPE = "matrix"
    PLUG_CLS = DataMatrixPlug
