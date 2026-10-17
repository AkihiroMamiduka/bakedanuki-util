# coding: utf-8
"""異なる属性群への明示入力を事前検証し、一つのUndoで適用する。"""

from __future__ import annotations

from collections.abc import Sequence
from contextlib import ExitStack
from dataclasses import dataclass
from typing import Literal, TypeAlias

from ..._identity import PlugIdentitySet

from ._enum_validation import require_enum_validation
from ._float_edit import FloatEditUndo
from ._plugs_store import PlugWrite, execute_plug_writes, plugs_undo_chunk
from .edit_session import MayaEditSession
from .plugs_binding import (
    MayaBoolPlugsBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
    MayaIntPlugsBinding,
    MayaStringPlugsBinding,
)

__all__ = [
    "MayaBoolValueEdit",
    "MayaFloatValueEdit",
    "MayaIntValueEdit",
    "MayaIntOffsetEdit",
    "MayaFloatOffsetEdit",
    "MayaFloatRoundEdit",
    "MayaEnumValueEdit",
    "MayaStringValueEdit",
    "MayaPlugsValueEdit",
    "apply_plugs_values",
]


def _require_binding(value: object, expected: type[object]) -> None:
    """動的呼出しから受け取ったBindingの型を確認する。"""
    if not isinstance(value, expected):
        raise TypeError(f"bindingには{expected.__name__}を指定します")


@dataclass(frozen=True)
class MayaBoolValueEdit:
    """一つのbool属性群へ適用する入力を保持する。

    Attributes:
        binding: 編集先のbool Binding。
        value: 設定する真偽値。
    """

    binding: MayaBoolPlugsBinding
    value: bool

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaBoolPlugsBinding)


@dataclass(frozen=True)
class MayaFloatValueEdit:
    """一つの数値属性群へ適用する入力を保持する。

    Attributes:
        binding: 編集先のfloat Binding。
        value: Bindingの公開単位で設定する値。
    """

    binding: MayaFloatPlugsBinding
    value: float

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaFloatPlugsBinding)


@dataclass(frozen=True)
class MayaIntValueEdit:
    """一つの整数属性群へ適用する未変換の整数値を保持する。"""

    binding: MayaIntPlugsBinding
    value: int

    def __post_init__(self) -> None:
        """Bindingの型を確認し、値は一括実行前に検証する。"""
        _require_binding(self.binding, MayaIntPlugsBinding)


@dataclass(frozen=True)
class MayaIntOffsetEdit:
    """整数属性群の各現在値へ同じ整数差分を加える。"""

    binding: MayaIntPlugsBinding
    offset: int

    def __post_init__(self) -> None:
        """Bindingの型を確認し、差分は一括実行前に検証する。"""
        _require_binding(self.binding, MayaIntPlugsBinding)


@dataclass(frozen=True)
class MayaFloatOffsetEdit:
    """数値属性群の各現在値へ同じ増減量を加える。

    Attributes:
        binding: 編集先のfloat Binding。
        offset: Bindingの公開単位で加算する値。
    """

    binding: MayaFloatPlugsBinding
    offset: float

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaFloatPlugsBinding)


@dataclass(frozen=True)
class MayaFloatRoundEdit:
    """各数値属性の現在値を表示単位で個別に四捨五入する。

    Attributes:
        binding: 編集先のfloat Binding。
        decimals: 残す小数桁数。0は整数へ丸める。
    """

    binding: MayaFloatPlugsBinding
    decimals: int

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaFloatPlugsBinding)


@dataclass(frozen=True)
class MayaEnumValueEdit:
    """一つのenum属性群へ適用する整数値を保持する。

    Attributes:
        binding: 編集先のenum Binding。
        value: 設定する選択肢の整数値。
    """

    binding: MayaEnumPlugsBinding
    value: int

    def __post_init__(self) -> None:
        """値の検証は実行前にまとめ、Bindingの型を先に確認する。"""
        _require_binding(self.binding, MayaEnumPlugsBinding)


@dataclass(frozen=True)
class MayaStringValueEdit:
    """一つのstring属性群へ適用する文字列を保持する。"""

    binding: MayaStringPlugsBinding
    value: str

    def __post_init__(self) -> None:
        """Bindingの型を確認し、値は一括実行前に検証する。"""
        _require_binding(self.binding, MayaStringPlugsBinding)


MayaPlugsValueEdit: TypeAlias = (
    MayaBoolValueEdit
    | MayaIntValueEdit
    | MayaIntOffsetEdit
    | MayaFloatValueEdit
    | MayaFloatOffsetEdit
    | MayaFloatRoundEdit
    | MayaEnumValueEdit
    | MayaStringValueEdit
)


def _require_edit(value: object) -> MayaPlugsValueEdit:
    """動的呼出しも対応する値入力だけに限定する。"""
    if not isinstance(
        value,
        (
            MayaBoolValueEdit,
            MayaIntValueEdit,
            MayaIntOffsetEdit,
            MayaFloatValueEdit,
            MayaFloatOffsetEdit,
            MayaFloatRoundEdit,
            MayaEnumValueEdit,
            MayaStringValueEdit,
        ),
    ):
        raise TypeError("editsにはMayaの属性値入力を指定してください")
    return value


def _prepare_edit(edit: MayaPlugsValueEdit) -> list[PlugWrite]:
    """入力の型対応を保持したまま、既存Storeの事前検証を共用する。"""
    if isinstance(edit, MayaBoolValueEdit):
        return edit.binding.store.prepare_write(edit.value)
    if isinstance(edit, MayaIntValueEdit):
        return edit.binding.store.prepare_write(edit.value)
    if isinstance(edit, MayaIntOffsetEdit):
        return edit.binding.store.prepare_offset(edit.offset)
    if isinstance(edit, MayaFloatValueEdit):
        return edit.binding.store.prepare_write(edit.value)
    if isinstance(edit, MayaFloatOffsetEdit):
        return edit.binding.store.prepare_offset(edit.offset)
    if isinstance(edit, MayaFloatRoundEdit):
        return edit.binding.store.prepare_round(edit.decimals)
    if isinstance(edit, MayaEnumValueEdit):
        return edit.binding.store.prepare_write(edit.value)
    return edit.binding.store.prepare_write(edit.value)


def apply_plugs_values(
    edits: Sequence[MayaPlugsValueEdit],
    *,
    edit_session: MayaEditSession | None = None,
    enum_validation: Literal["per_write", "operation"] = "per_write",
) -> bool:
    """全要求を事前検証し、差分を一回のUndoで適用する。

    代表属性が編集不可なら要求を拒否し、編集不可の後続属性は除外する。
    適用途中に失敗した場合は変更を復旧し、各Storeを再同期する。

    Args:
        edits: 適用する編集要求。数値は各Bindingの公開単位で指定する。
        edit_session: Mayaへの書き込み中に使う編集セッション。
        enum_validation: `per_write`は各書込み前に全enum定義を照合する。
            `operation`は開始時の定義を固定し、直前に基準と書込み先、終了時に
            全要求の対象を再確認する。異常検出が遅れる場合があり、外部処理の
            副作用と定義変更自体は復旧しない。復旧不能時はエラーを通知する。

    Returns:
        差分を適用した場合は`True`。空入力・全対象が同値なら`False`。

    Raises:
        TypeError: 対応していない編集要求を渡した場合。
        ValueError: 同じBindingまたは属性を複数回指定した場合。
            または`enum_validation`が不正な場合。

    """
    enum_validation = require_enum_validation(enum_validation)
    requests = tuple(_require_edit(edit) for edit in edits)
    if not requests:
        return False

    # 無変更の対象も含めて重複を拒否し、適用順で結果が変わらないようにする。
    stores = tuple(edit.binding.store for edit in requests)
    seen_plugs = PlugIdentitySet()
    seen_stores: set[int] = set()
    for store in stores:
        if id(store) in seen_stores:
            raise ValueError("同じBindingを複数回指定できません")
        seen_stores.add(id(store))
        for plug in store.target_plugs:
            if not seen_plugs.add(plug):
                raise ValueError("同じ属性を複数の入力へ指定できません")

    enum_stores = tuple(
        edit.binding.store
        for edit in requests
        if isinstance(edit, MayaEnumValueEdit)
    )

    def validate_definitions() -> None:
        """差分のない行も含め、操作開始時のenum定義と照合する。"""
        for enum_store in enum_stores:
            enum_store.validate_operation_definition()

    try:
        with ExitStack() as validation_stack:
            if enum_validation == "operation":
                for enum_store in enum_stores:
                    validation_stack.enter_context(
                        enum_store.operation_validation()
                    )

            # 全要求を準備できてから単一のUndo chunk内で書き込む
            plan = [
                write for edit in requests for write in _prepare_edit(edit)
            ]
            if plan:
                FloatEditUndo.finish_active()
                with ExitStack() as stack:
                    if edit_session is not None:
                        stack.enter_context(edit_session.write())
                    for store in stores:
                        stack.enter_context(store.write_guard())
                    stack.enter_context(plugs_undo_chunk())
                    execute_plug_writes(
                        plan,
                        validate_after=(
                            validate_definitions
                            if enum_validation == "operation"
                            else None
                        ),
                    )
            elif enum_validation == "operation":
                validate_definitions()
    except Exception as error:
        failures: list[Exception] = [error]
        for store in stores:
            try:
                store.refresh()
            except Exception as refresh_error:
                failures.append(refresh_error)
        reported = (
            error
            if len(failures) == 1
            else ExceptionGroup("属性の入力と状態同期に失敗しました", failures)
        )
        for store in stores:
            if not store.is_disposed:
                store.edit_failed.emit(str(reported))
        if reported is not error:
            raise reported from error
        raise

    # 書き込み完了後にまとめて同期し、途中状態を別の行へ通知しない。
    for store in stores:
        store.refresh()
    return bool(plan)
