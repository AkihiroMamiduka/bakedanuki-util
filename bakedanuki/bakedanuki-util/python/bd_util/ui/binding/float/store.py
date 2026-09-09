# coding: utf-8
from typing import Protocol

from .presentation import FloatPresentation


class FloatValueStore(Protocol):
    """単一の浮動小数点値の正本への読み書きと表示情報。"""

    @property
    def is_available(self) -> bool:
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        raise NotImplementedError

    @property
    def presentation(self) -> FloatPresentation:
        raise NotImplementedError

    def read(self) -> float:
        """丸めていない公開単位の実値を返す。"""
        raise NotImplementedError

    def write(self, value: float) -> float:
        """公開単位の要求を書き込み、確定後の実値を返す。"""
        raise NotImplementedError
