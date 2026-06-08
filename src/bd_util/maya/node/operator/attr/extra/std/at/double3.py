# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...define.std.at.double3 import (
    Double3AttrOperator,
    Double3PlugOperator,
    Double3Field,
)

A = TypeVar("A", bound="Double3AttrOperator")

P = TypeVar("P", bound="Double3PlugOperator")


class ExtraDouble3Field(Double3Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double3AttrOperator)
    PLUG_CLS = cast(Type[P], Double3PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
