# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAdskPrepareRenderGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "adskPrepareRenderGlobals"

    repName = DataStringField()
    rna = repName

    repLabel = DataStringField()
    rla = repLabel

    repType = DataStringField()
    rty = repType

    useRegExp = BoolField(default_value=False)
    urx = useRegExp
