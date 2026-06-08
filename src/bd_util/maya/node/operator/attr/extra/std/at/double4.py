# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...define.std.at.double4 import (
    Double4AttrOperator,
    Double4PlugOperator,
    Double4Field,
)

A = TypeVar("A", bound="Double4AttrOperator")

P = TypeVar("P", bound="Double4PlugOperator")


class ExtraDouble4Field(Double4Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double4AttrOperator)
    PLUG_CLS = cast(Type[P], Double4PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
