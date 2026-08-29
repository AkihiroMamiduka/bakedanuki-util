# coding: utf-8
from typing import Any, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ....._channel_state import ChannelBoxStateMixin
from ....._core import AttrOperator, PlugOperator, AttributeField
from .....keyframe import KeyframeManager

A = TypeVar("A", bound="ScalarBaseAttrOperator[Any]")

P = TypeVar("P", bound="ScalarBasePlugOperator[Any]")


class ScalarBasePlugOperator(ChannelBoxStateMixin, PlugOperator[A]):
    __slots__ = ()

    def _channel_box_state_plugs(self) -> tuple[om.MPlug, ...]:
        self._require_indexed_channel_box_target()
        return (self.plug,)

    @property
    def keyframe(self) -> KeyframeManager:
        return self._get_keyframe_manager()


class ScalarBaseAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "abc"


class ScalarBaseField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ScalarBaseAttrOperator)
    PLUG_CLS = cast(Type[P], ScalarBasePlugOperator)
