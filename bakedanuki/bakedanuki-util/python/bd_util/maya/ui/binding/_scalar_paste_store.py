# coding: utf-8
"""表示用QObjectを対象ごとに作らない、値Paste専用の一時Store。"""

from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from typing import Generic, TypeAlias, TypeVar, cast

from ....ui import EnumDefinition
from ...node.inspection import ScalarAttributeKind
from ._enum_validation import EnumOperationSnapshot, enum_operation_validation
from ._int_plug_value import IntPlugValue
from ._plug_lifetime import LifetimeWrite, PlugLifetime as ScalarPasteLifetime
from ._plugs_store import (
    PlugTarget,
    PlugWrite,
    PlugWriteValidator,
    prepare_plug_values,
    validate_plug_write_target,
)
from ._plugs_value_transaction import PlugEditRequest
from .bool_plug_resolver import resolve_bool_plug
from .enum_definition import read_enum_definition
from .enum_plug_resolver import resolve_enum_plug
from .float_plug_resolver import resolve_float_plug
from .int_plug_resolver import resolve_int_plug
from .plugs_binding import (
    _BoolCodec,  # pyright: ignore[reportPrivateUsage]
    _EnumCodec,  # pyright: ignore[reportPrivateUsage]
    _FloatCodec,  # pyright: ignore[reportPrivateUsage]
    _StringCodec,  # pyright: ignore[reportPrivateUsage]
    prepare_string_values,
)
from .plugs_state import MayaPlugTargetState
from .string_plug_resolver import resolve_string_plug

_ValueT = TypeVar("_ValueT", bool, float, int, str)


class ScalarPasteStore(Generic[_ValueT]):
    """対象一件の拒否単位を維持し、UIを作らず共通書込みへ接続する。"""

    def __init__(
        self,
        target: PlugTarget[_ValueT],
        value: _ValueT,
        lifetime: ScalarPasteLifetime,
    ) -> None:
        """値と実体を保持し、初期読取り中の削除から監視する。"""
        self.target = target
        self.value = value
        self._write_depth = 0
        self._enum_codec = (
            target.codec if isinstance(target.codec, _EnumCodec) else None
        )
        self._enum_snapshot: EnumOperationSnapshot | None = None
        lifetime.add(target)
        self.refresh()

    @property
    def state(self) -> MayaPlugTargetState:
        """Paste候補の採否に使う現在の状態を返す。"""
        return self.target.state()

    def require_available(self) -> None:
        """Undoに保持されていても、一度削除された対象は利用しない。"""
        if not self.target.is_available:
            raise RuntimeError("入力中に対象属性の状態が変わりました")

    def refresh(self) -> None:
        """従来の初期読取りと同期時の値・metadata検証をUIなしで行う。"""
        state = self.target.state()
        if not state.is_available:
            return
        self.target.codec.read()
        if isinstance(self.target.codec, _FloatCodec):
            _ = self.target.codec.value.presentation
        elif isinstance(self.target.codec, IntPlugValue):
            _ = self.target.codec.presentation
        if self._enum_codec is not None:
            _ = self._enum_codec.value.definition

    def prepare(self) -> list[PlugWrite]:
        """採用済みの一対象は現在も編集可能か確認し、共通の差分を作る。"""
        if self._write_depth:
            raise RuntimeError("一括書き込み中に別の入力は開始できません")
        if not self.state.is_writable:
            raise RuntimeError("代表のMaya属性は編集できません")
        if isinstance(self.value, str):
            plan = prepare_string_values(
                cast(PlugWriteValidator[str], self),
                (cast(PlugTarget[str], self.target),),
                self.value,
            )
        else:
            plan = prepare_plug_values(self, (self.target,), (self.value,))
        return [LifetimeWrite(write, self.require_available) for write in plan]

    @contextmanager
    def write_guard(self) -> Generator[None, None, None]:
        """書込み開始前の拒否と再入防止を対象ごとに維持する。"""
        if self._write_depth:
            raise RuntimeError("一括書き込み中に別の入力は開始できません")
        if not self.state.is_writable:
            raise RuntimeError("代表のMaya属性は編集できません")
        self._write_depth += 1
        try:
            yield
        finally:
            self._write_depth -= 1

    def validate_write_target(
        self, target: PlugTarget[_ValueT], requested: _ValueT
    ) -> None:
        """状態を再確認し、同じ対象のenum定義と値は直後の共通検証へ委ねる。"""
        validate_plug_write_target(self.target, target)

    def _enum_definitions(self) -> tuple[EnumDefinition, ...]:
        """文字列が同じ場合も含め、現在のenum定義を新しく解析する。"""
        if self._enum_codec is None:
            raise RuntimeError("enum属性ではありません")
        return (self._enum_codec.value.read_definition(refresh=True),)

    @contextmanager
    def operation_validation(self) -> Generator[None, None, None]:
        """通常のenum一括入力と同じ開始・終了時の定義確認を使う。"""
        if self._enum_codec is None:
            raise RuntimeError("enum属性ではありません")
        with enum_operation_validation(
            (self.target,), (self._enum_codec,), self._enum_definitions
        ) as snapshot:
            self._enum_snapshot = snapshot
            try:
                yield
            finally:
                self._enum_snapshot = None

    def validate_operation_definition(self) -> None:
        """同値で未書込みの対象も開始時のenum定義と照合する。"""
        if self._enum_snapshot is None:
            raise RuntimeError("enumの操作単位の検証は開始されていません")
        self._enum_snapshot.validate((self.target,), self._enum_definitions)

    def _notify_failure(self, _message: str) -> None:
        """画面を持たないため、失敗は公開APIからの例外だけで通知する。"""
        return None

    def request(self) -> PlugEditRequest:
        """全要求の事前検証・単一Undo・逆順復旧へ接続する。"""
        return PlugEditRequest(
            self,
            (self.target.plug,),
            self.prepare,
            self.write_guard,
            self.refresh,
            self._notify_failure,
            (
                self.operation_validation
                if self._enum_codec is not None
                else None
            ),
            (
                self.validate_operation_definition
                if self._enum_codec is not None
                else None
            ),
            self.require_available,
        )


ScalarPasteStoreType: TypeAlias = (
    ScalarPasteStore[bool]
    | ScalarPasteStore[int]
    | ScalarPasteStore[float]
    | ScalarPasteStore[str]
)


def create_scalar_paste_store(
    node_name: str,
    path: str,
    kind: ScalarAttributeKind,
    value: bool | int | float | str,
    definition: EnumDefinition | None,
    *,
    key_animated: bool,
    edit_connected: bool,
    lifetime: ScalarPasteLifetime,
) -> ScalarPasteStoreType:
    """型付きの既存codecを使い、候補一件の一時Storeを初期検証する。"""
    if kind == "bool":
        plug = resolve_bool_plug(node_name, path)
        return ScalarPasteStore(
            PlugTarget(
                plug.node,
                plug.plug,
                _BoolCodec(plug),
                key_animated=key_animated,
                edit_connected=edit_connected,
            ),
            cast(bool, value),
            lifetime,
        )
    if kind in ("byte", "short", "long"):
        plug = resolve_int_plug(node_name, path)
        return ScalarPasteStore(
            PlugTarget(
                plug.node,
                plug.plug,
                IntPlugValue(plug),
                key_animated=key_animated,
                edit_connected=edit_connected,
            ),
            cast(int, value),
            lifetime,
        )
    if kind == "enum":
        plug = resolve_enum_plug(node_name, path)
        if definition is None or not definition.matches(
            read_enum_definition(plug)
        ):
            raise ValueError("enum定義（整数値と項目名）が異なります")
        if definition.item_for_value(cast(int, value)) is None:
            raise ValueError("コピー元のenum値が定義されていません")
        return ScalarPasteStore(
            PlugTarget(
                plug.node,
                plug.plug,
                _EnumCodec(plug),
                key_animated=key_animated,
                edit_connected=edit_connected,
            ),
            cast(int, value),
            lifetime,
        )
    if kind == "string":
        plug = resolve_string_plug(node_name, path)
        return ScalarPasteStore(
            PlugTarget(plug.node, plug.plug, _StringCodec(plug)),
            cast(str, value),
            lifetime,
        )
    plug = resolve_float_plug(node_name, path)
    return ScalarPasteStore(
        PlugTarget(
            plug.node,
            plug.plug,
            _FloatCodec(plug),
            key_animated=key_animated,
            edit_connected=edit_connected,
        ),
        cast(float, value),
        lifetime,
    )
