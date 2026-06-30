# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.edit_metadata import EditsField
from ...attr.define.std.at.typed import TypedField


class EditMetadata(DG):
    __slots__ = ()

    NODE_TYPE = "editMetadata"

    inData = TypedField()
    id = inData

    outData = TypedField()
    od = outData

    edits = EditsField(multi=True)
    e = edits
