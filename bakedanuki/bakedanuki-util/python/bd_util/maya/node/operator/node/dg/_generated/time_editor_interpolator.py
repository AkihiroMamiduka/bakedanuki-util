# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.time_editor_interpolator import LayerAttributeField
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.typed import TypedField


class GeneratedTimeEditorInterpolator(DG):
    __slots__ = ()

    NODE_TYPE = "timeEditorInterpolator"

    parentCompound = TypedField(readable=False)
    pc = parentCompound

    parentCompoundState = TypedField(readable=False)
    pcs = parentCompoundState

    parentTracksState = TypedField(readable=False)
    pts = parentTracksState

    output = GenericField(multi=True)
    o = output

    outputRaw = GenericField(writable=False)
    or_ = outputRaw

    targetAttribute = MessageField(multi=True)
    ta = targetAttribute

    input = TypedField(multi=True)
    in_ = input

    layerAttribute = LayerAttributeField(multi=True)
    la = layerAttribute
