# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)

A = TypeVar("A", bound="CompoundAttrOperator")

P = TypeVar("P", bound="CompoundPlugOperator")


class ExtraCompoundField(CompoundField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], CompoundAttrOperator)
    PLUG_CLS = cast(Type[P], CompoundPlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
