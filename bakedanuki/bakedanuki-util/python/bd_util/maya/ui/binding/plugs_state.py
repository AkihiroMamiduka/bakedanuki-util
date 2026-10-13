# coding: utf-8
"""複数属性の入力対象と除外理由を表す公開値型。"""

from dataclasses import dataclass

from .plug_input_state import MayaPlugInputState

__all__ = ["MayaPlugTargetState"]


@dataclass(frozen=True)
class MayaPlugTargetState:
    """順序付き入力対象の編集可否、入力接続と実効ロック状態。

    `edit_description` は接続編集の方針と現在のキー設定先の説明です。
    未接続、未対応、または接続編集を有効にしていない場合は `None` です。
    """

    name: str
    is_available: bool
    is_writable: bool
    reason: str | None
    input_state: MayaPlugInputState | None = None
    is_locked: bool | None = None
    edit_description: str | None = None
