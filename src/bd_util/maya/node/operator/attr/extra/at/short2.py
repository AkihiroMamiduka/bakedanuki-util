# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...std.at.short2 import (
    Short2AttrOperator,
    Short2PlugOperator,
    Short2Field,
)

A = TypeVar("A", bound="Short2AttrOperator")

P = TypeVar("P", bound="Short2PlugOperator")


class ExtraShort2Field(Short2Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short2AttrOperator)
    PLUG_CLS = cast(Type[P], Short2PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
