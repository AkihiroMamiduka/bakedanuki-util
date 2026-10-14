# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from ._validation import require_int


@dataclass(frozen=True)
class IntPresentation:
    """整数の正本に適用する入力下限と上限。

    境界を省略した側は符号付き32-bit整数の全域を使用する。
    """

    minimum: int | None = None
    maximum: int | None = None

    def __post_init__(self) -> None:
        """境界値の型と大小関係を検証する。"""
        if self.minimum is not None:
            require_int(self.minimum, "minimum")
        if self.maximum is not None:
            require_int(self.maximum, "maximum")
        if (
            self.minimum is not None
            and self.maximum is not None
            and self.minimum > self.maximum
        ):
            raise ValueError("minimumはmaximum以下にしてください")


def require_presentation(value: object) -> IntPresentation:
    """整数の表示情報だけを受け付ける。"""
    if not isinstance(value, IntPresentation):
        raise TypeError("presentationにはIntPresentationを指定してください")
    return value
