# coding: utf-8
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from typing import Generic, Literal, Self, TypeVar, cast, overload

from .scalar_compound_value import ScalarCompoundValue

Scalar = TypeVar("Scalar", int, float)


@dataclass(frozen=True, slots=True)
class Scalar4(ScalarCompoundValue[Scalar], Generic[Scalar]):
    """4 成分の不変な数値を保持する。"""

    x: Scalar
    y: Scalar
    z: Scalar
    w: Scalar

    @classmethod
    def from_values(cls, values: Sequence[int | float]) -> Self:
        """4 個の値からインスタンスを作る。

        Args:
            values: x, y, z, w の順に並ぶ値。

        Returns:
            作成したインスタンス。

        Raises:
            ValueError: 値の個数が 4 個でない場合。
        """
        if len(values) != 4:
            raise ValueError(f"{cls.__name__} requires 4 values")
        return cls(
            cast(Scalar, values[0]),
            cast(Scalar, values[1]),
            cast(Scalar, values[2]),
            cast(Scalar, values[3]),
        )

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

    def __len__(self) -> Literal[4]:
        return 4

    def as_tuple(self) -> tuple[Scalar, Scalar, Scalar, Scalar]:
        """x, y, z, w を順番どおりにタプルで返す。"""
        return self.x, self.y, self.z, self.w
