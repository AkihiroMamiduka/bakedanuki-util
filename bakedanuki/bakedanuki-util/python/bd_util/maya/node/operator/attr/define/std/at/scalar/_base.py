# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ....._core import AttrOperator, PlugOperator, AttributeField
from .....keyframe import KeyframeManager

A = TypeVar("A", bound="ScalarBaseAttrOperator")

P = TypeVar("P", bound="ScalarBasePlugOperator")


class ScalarBasePlugOperator(PlugOperator[A]):
    __slots__ = ()

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
