# coding: utf-8
"""複数属性の入力対象と除外理由を表す公開値型。"""

from dataclasses import dataclass

__all__ = ["MayaPlugTargetState"]


@dataclass(frozen=True)
class MayaPlugTargetState:
    """順序付き入力対象の現在名、利用可否、書込み可否と理由。"""

    name: str
    is_available: bool
    is_writable: bool
    reason: str | None
