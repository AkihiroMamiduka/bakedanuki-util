# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from ._validation import require_float, require_suffix

FloatUnitKind: TypeAlias = Literal["number", "distance", "angle"]


def require_unit_kind(value: object) -> FloatUnitKind:
    """表示文字列から推測せず、明示された公開値の単位種別を検証する。"""
    if value == "number":
        return "number"
    if value == "distance":
        return "distance"
    if value == "angle":
        return "angle"
    raise ValueError("unit_kindにはnumber・distance・angleを指定してください")


@dataclass(frozen=True)
class FloatPresentation:
    """公開値から表示値への倍率・単位表記・正本のhard limit。

    表示桁数と操作時の刻み幅は各Viewが決める。

    Attributes:
        scale: 公開値から表示値への倍率。正の有限値を指定する。
        suffix: 表示値に付ける単位文字列。
        minimum: 公開単位の下限。`None`なら制限しない。
        maximum: 公開単位の上限。`None`なら制限しない。
        unit_kind: 公開値の単位種別。距離はcm、角度はdegree。

    Raises:
        TypeError: 数値またはsuffixの型が不正な場合。
        ValueError: 倍率や単位種別、上下限の指定が不正な場合。
    """

    scale: float = 1.0
    suffix: str = ""
    minimum: float | None = None
    maximum: float | None = None
    unit_kind: FloatUnitKind = "number"

    def __post_init__(self) -> None:
        scale = require_float(self.scale, "scale")
        if scale <= 0:
            raise ValueError("scaleには正の値を指定してください")
        require_suffix(self.suffix)
        require_unit_kind(self.unit_kind)
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
        """公開値に`scale`を掛けて表示単位へ変換する。

        Args:
            value: 公開単位の有限値。

        Returns:
            表示単位の有限値。

        Raises:
            TypeError: 数値以外を指定した場合。
            ValueError: 入力または変換後の値が有限でない場合。
        """
        return require_float(
            require_float(value) * self.scale, "display value"
        )

    def from_display(self, value: float) -> float:
        """表示値を`scale`で割って公開単位へ変換する。

        Args:
            value: 表示単位の有限値。

        Returns:
            公開単位の有限値。

        Raises:
            TypeError: 数値以外を指定した場合。
            ValueError: 入力または変換後の値が有限でない場合。
        """
        return require_float(require_float(value) / self.scale)


def require_presentation(value: object) -> FloatPresentation:
    """表示情報が ``FloatPresentation`` であることを検証する。

    Args:
        value: 検証する値。

    Returns:
        検証済みの表示情報。

    Raises:
        TypeError: 値が ``FloatPresentation`` でない場合。
    """
    if not isinstance(value, FloatPresentation):
        raise TypeError("presentationにはFloatPresentationを指定してください")
    return value
