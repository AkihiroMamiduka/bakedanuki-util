# coding: utf-8
from .._core import DG
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField


class _GeneratedGroupParts(DG):
    __slots__ = ()

    NODE_TYPE = "groupParts"

    inputGeometry = GenericField()
    ig = inputGeometry

    inputComponents = TypedField()
    ic = inputComponents

    inputRemoveComponent = TypedField()
    irc = inputRemoveComponent

    outputGeometry = GenericField(writable=False)
    og = outputGeometry

    groupId = LongField(default_value=-1)
    gi = groupId
