# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class XgmPalette(Transform):
    __slots__ = ()

    NODE_TYPE = "xgmPalette"

    xgBaseFile = DataStringField()
    xbf = xgBaseFile

    xgDeltaFiles = DataStringField()
    xdf = xgDeltaFiles

    xgExportAsDelta = BoolField(default_value=False)
    xed = xgExportAsDelta

    xgFileName = DataStringField()
    xfn = xgFileName
