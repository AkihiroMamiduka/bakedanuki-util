# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ....define.std.at.long2 import (
    Long2AttrOperator,
    Long2PlugOperator,
    Long2Field,
)

A = TypeVar("A", bound="Long2AttrOperator")

P = TypeVar("P", bound="Long2PlugOperator")


class ExtraLong2Field(Long2Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long2AttrOperator)
    PLUG_CLS = cast(Type[P], Long2PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
