# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ....define.std.at.double2 import (
    Double2AttrOperator,
    Double2PlugOperator,
    Double2Field,
)

A = TypeVar("A", bound="Double2AttrOperator")

P = TypeVar("P", bound="Double2PlugOperator")


class ExtraDouble2Field(Double2Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double2AttrOperator)
    PLUG_CLS = cast(Type[P], Double2PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
