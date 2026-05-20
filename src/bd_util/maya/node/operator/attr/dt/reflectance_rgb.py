# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataReflectanceRGBPlug(DataTypePlug["DataReflectanceRGBAttr"]):
    __slots__ = ()


class DataReflectanceRGBAttr(DataTypeAttr[DataReflectanceRGBPlug]):
    __slots__ = ()

    DATA_TYPE = "reflectanceRGB"
    PLUG_CLS = DataReflectanceRGBPlug
