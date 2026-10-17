# coding: utf-8
"""表示用Bindingと一時Storeで共有する一括入力の検証・Undo・復旧境界。"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from contextlib import AbstractContextManager, ExitStack
from dataclasses import dataclass
from typing import Literal

from maya.api import OpenMaya as om

from ..._identity import PlugIdentitySet
from ._enum_validation import require_enum_validation
from ._float_edit import FloatEditUndo
from ._plugs_store import PlugWrite, execute_plug_writes, plugs_undo_chunk
from .edit_session import MayaEditSession


@dataclass(frozen=True)
class PlugEditRequest:
    """値型を保った準備処理と、表示の有無に依存しない一括入力契約。"""

    store_identity: object
    target_plugs: tuple[om.MPlug, ...]
    prepare: Callable[[], list[PlugWrite]]
    write_guard: Callable[[], AbstractContextManager[None]]
    refresh: Callable[[], object]
    notify_failure: Callable[[str], None]
    enum_context: Callable[[], AbstractContextManager[None]] | None = None
    validate_enum: Callable[[], None] | None = None
    validate_after: Callable[[], None] | None = None


def apply_edit_requests(
    requests: Sequence[PlugEditRequest],
    *,
    edit_session: MayaEditSession | None = None,
    enum_validation: Literal["per_write", "operation"] = "per_write",
) -> bool:
    """全要求を検証し、差分と終了検証を同じUndo・復旧範囲で実行する。"""
    enum_validation = require_enum_validation(enum_validation)
    requests = tuple(requests)
    if not requests:
        return False

    # 無変更の対象も含めて重複を拒否し、要求順で結果が変わらないようにする
    seen_plugs = PlugIdentitySet()
    seen_stores: set[int] = set()
    for request in requests:
        identity = id(request.store_identity)
        if identity in seen_stores:
            raise ValueError("同じBindingを複数回指定できません")
        seen_stores.add(identity)
        for plug in request.target_plugs:
            if not seen_plugs.add(plug):
                raise ValueError("同じ属性を複数の入力へ指定できません")

    def validate_after() -> None:
        """未書込み要求も含めた消失と、操作単位のenum定義を照合する。"""
        for request in requests:
            if request.validate_after is not None:
                request.validate_after()
            if (
                enum_validation == "operation"
                and request.validate_enum is not None
            ):
                request.validate_enum()

    needs_final_validation = enum_validation == "operation" or any(
        request.validate_after is not None for request in requests
    )

    try:
        with ExitStack() as validation_stack:
            if enum_validation == "operation":
                for request in requests:
                    if request.enum_context is not None:
                        validation_stack.enter_context(request.enum_context())

            # 全要求の準備が成功してから一括書込みへ進む
            plan = [
                write for request in requests for write in request.prepare()
            ]
            if plan:
                FloatEditUndo.finish_active()
                with ExitStack() as stack:
                    if edit_session is not None:
                        stack.enter_context(edit_session.write())
                    for request in requests:
                        stack.enter_context(request.write_guard())
                    stack.enter_context(plugs_undo_chunk())
                    execute_plug_writes(
                        plan,
                        validate_after=(
                            validate_after if needs_final_validation else None
                        ),
                    )
            elif needs_final_validation:
                validate_after()
    except Exception as error:
        failures: list[Exception] = [error]
        for request in requests:
            try:
                request.refresh()
            except Exception as refresh_error:
                failures.append(refresh_error)
        reported = (
            error
            if len(failures) == 1
            else ExceptionGroup("属性の入力と状態同期に失敗しました", failures)
        )
        for request in requests:
            request.notify_failure(str(reported))
        if reported is not error:
            raise reported from error
        raise

    # 全書込み後にまとめて同期し、途中状態を別の要求へ通知しない
    for request in requests:
        request.refresh()
    return bool(plan)
