# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...define.std.at.float2 import (
    Float2AttrOperator,
    Float2PlugOperator,
    Float2Field,
)

A = TypeVar("A", bound="Float2AttrOperator")

P = TypeVar("P", bound="Float2PlugOperator")


class ExtraFloat2Field(Float2Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float2AttrOperator)
    PLUG_CLS = cast(Type[P], Float2PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
