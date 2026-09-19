# coding: utf-8
"""異なる属性群への明示入力を事前検証し、一つのUndoで適用する。"""

from __future__ import annotations

from collections.abc import Sequence
from contextlib import ExitStack
from dataclasses import dataclass
from typing import TypeAlias

from maya.api import OpenMaya as om

from ._float_edit import FloatEditUndo
from ._plugs_store import PlugWrite, execute_plug_writes, plugs_undo_chunk
from .edit_session import MayaEditSession
from .plugs_binding import (
    MayaBoolPlugsBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
)

__all__ = [
    "MayaBoolValueEdit",
    "MayaFloatValueEdit",
    "MayaFloatOffsetEdit",
    "MayaEnumValueEdit",
    "MayaPlugsValueEdit",
    "apply_plugs_values",
]


def _require_binding(value: object, expected: type[object]) -> None:
    """動的呼出しから受け取ったBindingの型を確認する。"""
    if not isinstance(value, expected):
        raise TypeError(f"bindingには{expected.__name__}を指定します")


@dataclass(frozen=True)
class MayaBoolValueEdit:
    """一つのbool属性群へ明示入力する値を保持する。"""

    binding: MayaBoolPlugsBinding
    value: bool

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaBoolPlugsBinding)


@dataclass(frozen=True)
class MayaFloatValueEdit:
    """一つの数値属性群へ入力するcm・degree・単位なしの値を保持する。"""

    binding: MayaFloatPlugsBinding
    value: float

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaFloatPlugsBinding)


@dataclass(frozen=True)
class MayaFloatOffsetEdit:
    """数値属性群の各現在値へ、公開単位の同じ増減量を加える。"""

    binding: MayaFloatPlugsBinding
    offset: float

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaFloatPlugsBinding)


@dataclass(frozen=True)
class MayaEnumValueEdit:
    """一つのenum属性群へ明示入力する整数値を保持する。"""

    binding: MayaEnumPlugsBinding
    value: int

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaEnumPlugsBinding)


MayaPlugsValueEdit: TypeAlias = (
    MayaBoolValueEdit
    | MayaFloatValueEdit
    | MayaFloatOffsetEdit
    | MayaEnumValueEdit
)


def _require_edit(value: object) -> MayaPlugsValueEdit:
    """動的呼出しも対応する値入力だけに限定する。"""
    if not isinstance(
        value,
        (
            MayaBoolValueEdit,
            MayaFloatValueEdit,
            MayaFloatOffsetEdit,
            MayaEnumValueEdit,
        ),
    ):
        raise TypeError("editsにはMayaの属性値入力を指定してください")
    return value


def _prepare_edit(edit: MayaPlugsValueEdit) -> list[PlugWrite]:
    """入力の型対応を保持したまま、既存Storeの事前検証を共用する。"""
    if isinstance(edit, MayaBoolValueEdit):
        return edit.binding.store.prepare_write(edit.value)
    if isinstance(edit, MayaFloatValueEdit):
        return edit.binding.store.prepare_write(edit.value)
    if isinstance(edit, MayaFloatOffsetEdit):
        return edit.binding.store.prepare_offset(edit.offset)
    return edit.binding.store.prepare_write(edit.value)


def apply_plugs_values(
    edits: Sequence[MayaPlugsValueEdit],
    *,
    edit_session: MayaEditSession | None = None,
) -> bool:
    """全要求を事前検証し、差分を一回のUndoで適用する。

    各値はBindingの公開単位で渡す。空入力・全対象が同値ならFalseを返す。
    代表属性が編集不可の場合と、Binding間で対象が重複する場合は全体を拒否する。
    編集不可の後続属性は既存Bindingと同じく除外し、途中失敗は全変更を復旧する。
    """
    requests = tuple(_require_edit(edit) for edit in edits)
    if not requests:
        return False

    # 無変更の対象も含めて重複を拒否し、適用順による値の上書きを防ぐ
    stores = tuple(edit.binding.store for edit in requests)
    seen_plugs: list[om.MPlug] = []
    for index, store in enumerate(stores):
        if any(store is previous for previous in stores[:index]):
            raise ValueError("同じBindingを複数回指定できません")
        for plug in store.target_plugs:
            if any(plug == previous for previous in seen_plugs):
                raise ValueError("同じ属性を複数の入力へ指定できません")
            seen_plugs.append(plug)

    try:
        # 全行の検証が済むまで、値とUndo履歴を変更しない
        plan = [write for edit in requests for write in _prepare_edit(edit)]
        if plan:
            FloatEditUndo.finish_active()
            with ExitStack() as stack:
                if edit_session is not None:
                    stack.enter_context(edit_session.write())
                for store in stores:
                    stack.enter_context(store.write_guard())
                stack.enter_context(plugs_undo_chunk())
                execute_plug_writes(plan)
    except Exception as error:
        for store in stores:
            store.refresh()
            if not store.is_disposed:
                store.edit_failed.emit(str(error))
        raise

    # 全対象を確定してから同期し、途中状態を他の行へ伝播しない
    for store in stores:
        store.refresh()
    return bool(plan)
