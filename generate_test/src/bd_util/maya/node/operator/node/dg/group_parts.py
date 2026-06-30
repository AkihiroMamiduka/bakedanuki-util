# coding: utf-8
from ._core import DG
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class GroupParts(DG):
    __slots__ = ()

    NODE_TYPE = "groupParts"

    inputGeometry = GenericField()
    ig = inputGeometry

    inputComponents = TypedField()
    ic = inputComponents

    inputRemoveComponent = TypedField()
    irc = inputRemoveComponent

    outputGeometry = GenericField()
    og = outputGeometry

    groupId = LongField()
    gi = groupId
