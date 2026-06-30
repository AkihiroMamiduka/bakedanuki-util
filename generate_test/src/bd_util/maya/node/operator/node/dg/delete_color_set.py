# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class DeleteColorSet(DG):
    __slots__ = ()

    NODE_TYPE = "deleteColorSet"

    inputGeometry = TypedField()
    ig = inputGeometry

    outputGeometry = TypedField()
    og = outputGeometry

    colorSetName = DataStringField()
    cols = colorSetName
