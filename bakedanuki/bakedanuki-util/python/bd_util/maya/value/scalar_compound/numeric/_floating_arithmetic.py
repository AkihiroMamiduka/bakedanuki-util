# coding: utf-8
from collections.abc import Sequence
from typing import cast, Self

from ..scalar_compound_value import ScalarCompoundValue


class FloatingNumericArithmeticMixin:
    """浮動小数点numeric compound用のimmutableな基本演算。"""

    __slots__ = ()

    def __add__(self, other: Self, /) -> Self:
        if type(other) is not type(self):
            return cast(Self, NotImplemented)
        return self._from_arithmetic_values(
            tuple(
                float(left + right)
                for left, right in zip(
                    self._arithmetic_values(),
                    cast(Sequence[float], other),
                )
            )
        )

    def __sub__(self, other: Self, /) -> Self:
        if type(other) is not type(self):
            return cast(Self, NotImplemented)
        return self._from_arithmetic_values(
            tuple(
                float(left - right)
                for left, right in zip(
                    self._arithmetic_values(),
                    cast(Sequence[float], other),
                )
            )
        )

    def __mul__(self, other: int | float, /) -> Self:
        scalar = self._arithmetic_scalar(other)
        if scalar is None:
            return cast(Self, NotImplemented)
        return self._from_arithmetic_values(
            tuple(float(value * scalar) for value in self._arithmetic_values())
        )

    def __rmul__(self, other: int | float, /) -> Self:
        return self * other

    def __truediv__(self, other: int | float, /) -> Self:
        scalar = self._arithmetic_scalar(other)
        if scalar is None:
            return cast(Self, NotImplemented)
        return self._from_arithmetic_values(
            tuple(float(value / scalar) for value in self._arithmetic_values())
        )

    def __neg__(self) -> Self:
        return self._from_arithmetic_values(
            tuple(float(-value) for value in self._arithmetic_values())
        )

    def _arithmetic_values(self) -> ScalarCompoundValue[float]:
        return cast(ScalarCompoundValue[float], self)

    def _from_arithmetic_values(
        self,
        values: Sequence[int | float],
    ) -> Self:
        value_type = cast(type[ScalarCompoundValue[float]], type(self))
        return cast(Self, value_type.from_values(values))

    @staticmethod
    def _arithmetic_scalar(value: object) -> float | None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return None
        return float(value)
