# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class CopyColorSet(DG):
    __slots__ = ()

    NODE_TYPE = "copyColorSet"

    inputGeometry = TypedField()
    ig = inputGeometry

    outputGeometry = TypedField()
    og = outputGeometry

    srcColorSetName = DataStringField()
    src = srcColorSetName

    dstColorName = DataStringField()
    dst = dstColorName
