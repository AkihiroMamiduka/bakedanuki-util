# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.shape_editor_manager import BlendShapeDirectoryField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedShapeEditorManager(DG):
    __slots__ = ()

    NODE_TYPE = "shapeEditorManager"

    blendShapeDirectory = BlendShapeDirectoryField(multi=True)
    bsdt = blendShapeDirectory

    blendShapeParent = LongField(multi=True, default_value=0)
    bspr = blendShapeParent

    outBlendShapeVisibility = BoolField(multi=True, default_value=False, writable=False)
    obsv = outBlendShapeVisibility

    filterString = DataStringField()
    tpfs = filterString
