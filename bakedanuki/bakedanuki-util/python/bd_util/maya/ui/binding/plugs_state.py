# coding: utf-8
"""複数属性の入力対象と除外理由を表す公開値型。"""

from dataclasses import dataclass

from .plug_input_state import MayaPlugInputState

__all__ = ["MayaPlugTargetState"]


@dataclass(frozen=True)
class MayaPlugTargetState:
    """順序付き入力対象の編集可否、入力接続と実効ロック状態。"""

    name: str
    is_available: bool
    is_writable: bool
    reason: str | None
    input_state: MayaPlugInputState | None = None
    is_locked: bool | None = None
