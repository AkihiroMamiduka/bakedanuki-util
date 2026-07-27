# coding: utf-8
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generic, Self, TypeVar

Scalar = TypeVar("Scalar", int, float, covariant=True)


class ScalarCompoundValue(Sequence[Scalar], Generic[Scalar], ABC):
    __slots__ = ()

    @classmethod
    @abstractmethod
    def from_values(cls, values: Sequence[int | float]) -> Self:
        pass

    @abstractmethod
    def as_tuple(self) -> tuple[Scalar, ...]:
        pass
