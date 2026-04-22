# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataSpectrumRGBPlug(DataTypePlug["DataSpectrumRGBAttr"]):
    pass


class DataSpectrumRGBAttr(DataTypeAttr[DataSpectrumRGBPlug]):
    DATA_TYPE = "spectrumRGB"
    PLUG_CLS = DataSpectrumRGBPlug
