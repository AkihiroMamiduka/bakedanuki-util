# coding: utf-8
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generic, Self, TypeVar

Scalar = TypeVar("Scalar", int, float, covariant=True)


class ScalarCompoundValue(Sequence[Scalar], Generic[Scalar], ABC):
    """数値成分をシーケンスとして扱うための抽象基底。"""

    __slots__ = ()

    @classmethod
    @abstractmethod
    def from_values(cls, values: Sequence[int | float]) -> Self:
        """成分値の並びからインスタンスを作る。

        Args:
            values: サブクラスが定める個数の成分値。

        Returns:
            作成したインスタンス。
        """
        pass

    @abstractmethod
    def as_tuple(self) -> tuple[Scalar, ...]:
        """成分値を定義順にタプルで返す。"""
        pass
