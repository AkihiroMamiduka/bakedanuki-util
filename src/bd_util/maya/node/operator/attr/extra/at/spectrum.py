# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...std.at.spectrum import (
    SpectrumAttrOperator,
    SpectrumPlugOperator,
    SpectrumField,
)

A = TypeVar("A", bound="SpectrumAttrOperator")

P = TypeVar("P", bound="SpectrumPlugOperator")


class ExtraSpectrumField(SpectrumField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], SpectrumAttrOperator)
    PLUG_CLS = cast(Type[P], SpectrumPlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
