# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...std.at.float3 import (
    Float3AttrOperator,
    Float3PlugOperator,
    Float3Field,
)

A = TypeVar("A", bound="Float3AttrOperator")

P = TypeVar("P", bound="Float3PlugOperator")


class ExtraFloat3Field(Float3Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float3AttrOperator)
    PLUG_CLS = cast(Type[P], Float3PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
