# coding: utf-8
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from typing import Generic, Literal, Self, TypeVar, cast, overload

from .scalar_compound_value import ScalarCompoundValue

Scalar = TypeVar("Scalar", int, float)


@dataclass(frozen=True, slots=True)
class Scalar2(ScalarCompoundValue[Scalar], Generic[Scalar]):
    x: Scalar
    y: Scalar

    @classmethod
    def from_values(cls, values: Sequence[int | float]) -> Self:
        if len(values) != 2:
            raise ValueError(f"{cls.__name__} requires 2 values")
        return cls(cast(Scalar, values[0]), cast(Scalar, values[1]))

    @overload
    def __getitem__(self, index: int) -> Scalar:
        pass

    @overload
    def __getitem__(self, index: slice) -> tuple[Scalar, ...]:
        pass

    def __getitem__(
        self,
        index: int | slice,
    ) -> Scalar | tuple[Scalar, ...]:
        return self.as_tuple()[index]

    def __iter__(self) -> Iterator[Scalar]:
        return iter(self.as_tuple())

    def __len__(self) -> Literal[2]:
        return 2

    def as_tuple(self) -> tuple[Scalar, Scalar]:
        return self.x, self.y
