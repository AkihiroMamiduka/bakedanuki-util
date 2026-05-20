# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataSpectrumRGBPlug(DataTypePlug["DataSpectrumRGBAttr"]):
    __slots__ = ()


class DataSpectrumRGBAttr(DataTypeAttr[DataSpectrumRGBPlug]):
    __slots__ = ()

    DATA_TYPE = "spectrumRGB"
    PLUG_CLS = DataSpectrumRGBPlug
