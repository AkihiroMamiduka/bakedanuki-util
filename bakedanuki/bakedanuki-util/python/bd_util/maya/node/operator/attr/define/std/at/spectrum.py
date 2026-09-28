# coding: utf-8
from typing import Any, TypeVar, Type, cast

from ...custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)

A = TypeVar("A", bound="Float3CompoundBaseAttrOperator[Any]")

P = TypeVar("P", bound="Float3CompoundBasePlugOperator[Any]")


class SpectrumPlugOperator(
    Float3CompoundBasePlugOperator["SpectrumAttrOperator"]
):
    """Maya の `spectrum` 属性の RGB 成分を操作する。"""

    __slots__ = ()
    _SUFFIXES = ("r", "g", "b")


class SpectrumAttrOperator(
    Float3CompoundBaseAttrOperator[SpectrumPlugOperator]
):
    """Maya の `spectrum` 属性定義を表す。"""

    __slots__ = ()

    ATTR_TYPE = "spectrum"


class SpectrumField(Float3CompoundBaseField[A, P]):
    """ノードクラスに `spectrum` 属性を定義する。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], SpectrumAttrOperator)
    PLUG_CLS = cast(Type[P], SpectrumPlugOperator)
