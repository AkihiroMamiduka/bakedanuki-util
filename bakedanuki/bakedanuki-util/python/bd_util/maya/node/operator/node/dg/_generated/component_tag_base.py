# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.component_tag_base import ComponentTagsField
from ....attr.define.std.at.generic import GenericField


class _GeneratedComponentTagBase(DG):
    __slots__ = ()

    NODE_TYPE = "componentTagBase"

    inputGeometry = GenericField()
    ig = inputGeometry

    outputGeometry = GenericField(writable=False)
    og = outputGeometry

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags
