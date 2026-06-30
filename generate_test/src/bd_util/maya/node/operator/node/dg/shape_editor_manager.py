# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shape_editor_manager import BlendShapeDirectoryField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class ShapeEditorManager(DG):
    __slots__ = ()

    NODE_TYPE = "shapeEditorManager"

    blendShapeDirectory = BlendShapeDirectoryField(multi=True)
    bsdt = blendShapeDirectory

    blendShapeParent = LongField(multi=True)
    bspr = blendShapeParent

    outBlendShapeVisibility = BoolField(multi=True)
    obsv = outBlendShapeVisibility

    filterString = DataStringField()
    tpfs = filterString
