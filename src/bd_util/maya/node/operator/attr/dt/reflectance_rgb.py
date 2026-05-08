# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataReflectanceRGBPlug(DataTypePlug["DataReflectanceRGBAttr"]):
    pass


class DataReflectanceRGBAttr(DataTypeAttr[DataReflectanceRGBPlug]):
    DATA_TYPE = "reflectanceRGB"
    PLUG_CLS = DataReflectanceRGBPlug
