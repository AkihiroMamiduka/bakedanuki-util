# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from ._validation import require_float, require_suffix


@dataclass(frozen=True)
class FloatPresentation:
    """公開値から表示値への倍率・単位表記・正本のhard limit。

    minimum/maximumは公開値の単位。Noneはその側の制限なしを表す。
    decimalsや操作時の刻み幅は各Viewが選ぶ。
    """

    scale: float = 1.0
    suffix: str = ""
    minimum: float | None = None
    maximum: float | None = None

    def __post_init__(self) -> None:
        scale = require_float(self.scale, "scale")
        if scale <= 0:
            raise ValueError("scaleには正の値を指定してください")
        require_suffix(self.suffix)
        for name, value in (
            ("minimum", self.minimum),
            ("maximum", self.maximum),
        ):
            if value is not None:
                require_float(value, name)
        if self.minimum is not None and self.maximum is not None:
            if self.minimum > self.maximum:
                raise ValueError("minimumはmaximum以下にしてください")

    def to_display(self, value: float) -> float:
        """公開値を表示単位へ変換する。"""
        return require_float(
            require_float(value) * self.scale, "display value"
        )

    def from_display(self, value: float) -> float:
        """表示単位の入力を公開値へ変換する。"""
        return require_float(require_float(value) / self.scale)


def require_presentation(value: object) -> FloatPresentation:
    if not isinstance(value, FloatPresentation):
        raise TypeError("presentationにはFloatPresentationを指定してください")
    return value
