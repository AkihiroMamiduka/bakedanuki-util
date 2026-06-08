# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ....define.std.at.long3 import (
    Long3AttrOperator,
    Long3PlugOperator,
    Long3Field,
)

A = TypeVar("A", bound="Long3AttrOperator")

P = TypeVar("P", bound="Long3PlugOperator")


class ExtraLong3Field(Long3Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long3AttrOperator)
    PLUG_CLS = cast(Type[P], Long3PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
