# coding: utf-8
"""表示用QObjectを対象ごとに作らない、値Paste専用の一時Store。"""

from __future__ import annotations

from collections.abc import Callable, Generator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generic, Protocol, TypeAlias, TypeVar, cast

from maya.api import OpenMaya as om

from ....ui import EnumDefinition, qt
from ..._identity import ObjectIdentityIndex
from ...node.inspection import ScalarAttributeKind
from ..callback import MayaCallbackRegistry
from ._enum_validation import EnumOperationSnapshot, enum_operation_validation
from ._int_plug_value import IntPlugValue
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


class _LifetimeTarget(Protocol):
    """値型に依存せず、操作中の削除履歴だけを保持する対象。"""

    plug: om.MPlug
    watched: list[om.MPlug]
    removed: bool


class ScalarPasteLifetime:
    """一回のPasteだけnode単位で削除を監視し、同名再作成へ追従しない。"""

    def __init__(self) -> None:
        """対象数と独立したQt ownerと、衝突を実体で区別する索引を作る。"""
        self._owner = qt.QObject()
        self._registry = MayaCallbackRegistry(self._owner)
        self._indices = ObjectIdentityIndex()
        self._targets: dict[int, list[_LifetimeTarget]] = {}

    def add(self, target: _LifetimeTarget) -> None:
        """初期読取り前に対象を記録し、同じnodeの監視を重複登録しない。"""
        identity = self._indices.index(target.plug.node())
        targets = self._targets.setdefault(identity, [])
        first = not targets
        targets.append(target)
        if first:
            self._registry.register(
                int(
                    om.MNodeMessage.addAttributeChangedCallback(
                        target.plug.node(), self._on_attribute_changed
                    )
                )
            )
            self._registry.register(
                int(
                    om.MNodeMessage.addNodePreRemovalCallback(
                        target.plug.node(), self._on_node_removed
                    )
                )
            )

    def _on_attribute_changed(
        self, message: int, plug: om.MPlug, _other: om.MPlug, _data: object
    ) -> None:
        """通常の値通知は処理せず、対象または祖先の削除だけを記録する。"""
        if not message & om.MNodeMessage.kAttributeRemoved:
            return
        identity = self._indices.index(plug.node())
        for target in self._targets.get(identity, ()):
            if not target.removed and any(
                plug == watched for watched in target.watched
            ):
                target.removed = True

    def _on_node_removed(self, node: om.MObject, *_args: object) -> None:
        """削除前の同じnodeに属する全対象を恒久的に無効化する。"""
        identity = self._indices.index(node)
        for target in self._targets.get(identity, ()):
            target.removed = True

    def close(self) -> None:
        """成功・失敗を問わず全監視を解除し、Qt ownerの破棄を予約する。"""
        try:
            self._registry.dispose()
        finally:
            self._owner.deleteLater()


@dataclass
class _LifetimeWrite:
    """削除済みMPlugへ触れず、共通の差分適用・復旧処理を呼ぶ。"""

    original: PlugWrite
    require_available: Callable[[], None]
    attempted: bool = False

    def validate(self) -> None:
        """生存確認後に従来の事前検証を実行する。"""
        self.require_available()
        self.original.validate()

    def apply(self) -> None:
        """各書込みの直前にも削除履歴を確認する。"""
        self.require_available()
        self.attempted = True
        self.original.apply()

    def restore(self) -> None:
        """復旧不能な削除対象を明示的に拒否し、別実体へ書き戻さない。"""
        if not self.attempted:
            return
        self.require_available()
        self.original.restore()


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
        return [
            _LifetimeWrite(write, self.require_available) for write in plan
        ]

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
        """後続も独立した代表として扱い、途中のlock変更は全体を拒否する。"""
        validate_plug_write_target(self.target, target)
        if self._enum_codec is not None:
            expected = self._enum_codec.operation_definition
            if expected is not None and not expected.matches(
                self._enum_codec.value.read_definition(refresh=True)
            ):
                raise ValueError("入力中に代表のenum定義が変わりました")
            self._enum_codec.validate(cast(int, requested))

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
