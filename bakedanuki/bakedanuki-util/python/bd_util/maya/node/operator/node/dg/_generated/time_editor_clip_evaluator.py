# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.time_editor_clip_evaluator import (
    AttributeField,
    LayerAttributeField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.typed import TypedField


class GeneratedTimeEditorClipEvaluator(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorClipEvaluator"

    parentContainerState = TypedField(readable=False)
    pcs = parentContainerState

    attribute = AttributeField(multi=True)
    a = attribute

    output = GenericField()
    o = output

    rosterItems = MessageField(multi=True, readable=False)
    tas = rosterItems

    layerAttribute = LayerAttributeField(multi=True)
    la = layerAttribute
