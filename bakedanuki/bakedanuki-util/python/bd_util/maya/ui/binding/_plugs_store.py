# coding: utf-8
"""複数plugの監視と、事前検証・Undo・失敗復旧の共通境界。"""

from __future__ import annotations

from collections.abc import Callable, Generator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar, cast

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import FloatViewModel, qt
from ...node.operator.node._core import NodeOperator
from ..callback import MayaCallbackRegistry
from ._float_edit import FloatEditUndo
from ._float_plug_endpoint import run_later
from .plugs_state import MayaPlugTargetState

_ValueT = TypeVar("_ValueT", bool, float, int)


class PlugValueCodec(Protocol[_ValueT]):
    """公開値とMayaへの入力値を相互変換する内部契約。"""

    def read(self) -> _ValueT:
        """正本の公開値を取得する。"""
        raise NotImplementedError

    def to_ui(self, value: _ValueT) -> _ValueT:
        """入力を検証し、setAttrの現在単位へ変換する。"""
        raise NotImplementedError

    def validate(self, value: _ValueT) -> _ValueT:
        """新規入力の制限を検証し、現在単位へ変換する。"""
        raise NotImplementedError


@dataclass
class PlugTarget(Generic[_ValueT]):
    """一つの属性の実体、単位変換と削除後の無効状態を保持する。"""

    node: NodeOperator
    plug: om.MPlug
    codec: PlugValueCodec[_ValueT]
    removed: bool = False

    def __post_init__(self) -> None:
        """同名再作成に追従しない実体参照と監視対象を記録する。"""
        self.node_handle = om.MObjectHandle(self.plug.node())
        self.attribute_handle = om.MObjectHandle(self.plug.attribute())
        self.watched = [self.plug]
        while self.watched[-1].isChild:
            self.watched.append(self.watched[-1].parent())
        self.last_name = self.name()

    @property
    def is_available(self) -> bool:
        """削除後はUndoや同名再作成でも再接続しない。"""
        return (
            not self.removed
            and self.node_handle.isValid()
            and self.attribute_handle.isValid()
        )

    def name(self) -> str:
        """同名DAGも区別できる、現在の完全な属性名を取得する。"""
        # API検索用の先頭dotはcmds名へ含めず、完全pathで子を区別する
        path = self.plug.partialName(
            includeNodeName=False,
            useAlias=False,
            useFullAttributePath=True,
            useLongNames=True,
        )
        return f"{self.node.cmd_access_name}.{path}"

    def state(self) -> MayaPlugTargetState:
        """自身と祖先の状態から入力可否と説明を取得する。"""
        if not self.is_available:
            return MayaPlugTargetState(
                self.last_name,
                False,
                False,
                "ノードまたは属性が削除されました",
            )
        self.last_name = self.name()
        reason: str | None = None
        if any(plug.isLocked for plug in self.watched):
            reason = "ロックされています"
        elif any(plug.isDestination for plug in self.watched):
            reason = "入力接続があります（アニメーションを含む）"
        elif not om.MFnAttribute(self.plug.attribute()).writable:
            reason = "書き込み不可の属性です"
        elif self.plug.isFreeToChange(True, False) != om.MPlug.kFreeToChange:
            reason = "Mayaが値の変更を許可していません"
        return MayaPlugTargetState(
            self.last_name, True, reason is None, reason
        )


class PlugWrite(Protocol):
    """値型が異なる入力も同じ適用・復旧順序で処理する内部契約。"""

    def validate(self) -> None:
        """書込み直前の状態を再検証する。"""
        raise NotImplementedError

    def apply(self) -> None:
        """検証済みの一つの差分を適用する。"""
        raise NotImplementedError

    def restore(self) -> None:
        """差分が残っている場合だけ入力前の値を復旧する。"""
        raise NotImplementedError


@dataclass(frozen=True)
class _PreparedPlugWrite(Generic[_ValueT]):
    """事前検証した入力と公開単位の復旧値を保持する。"""

    store: PlugsStore[_ValueT]
    target: PlugTarget[_ValueT]
    before: _ValueT
    value: _ValueT
    requested: _ValueT

    def validate(self) -> None:
        """状態・範囲・単位が変わっていないことを確認する。"""
        self.store.validate_write_target(self.target, self.requested)
        if self.target.codec.validate(self.value) != self.requested:
            raise RuntimeError("入力中に対象属性の単位が変わりました")

    def apply(self) -> None:
        """事前検証した現在単位の値をMayaへ書き込む。"""
        set_attr = cast(Callable[[str, _ValueT], None], cmds.setAttr)
        set_attr(self.target.name(), self.requested)

    def restore(self) -> None:
        """公開単位の復旧値を現在単位へ変換して元に戻す。"""
        before = self.target.codec.to_ui(self.before)
        if self.target.codec.to_ui(self.target.codec.read()) != before:
            set_attr = cast(Callable[[str, _ValueT], None], cmds.setAttr)
            set_attr(self.target.name(), before)


@contextmanager
def plugs_undo_chunk() -> Generator[None, None, None]:
    """値入力を一操作へまとめ、MayaのUndo設定を変えずに閉じる。"""
    enabled = bool(cmds.undoInfo(query=True, state=True))
    if enabled:
        cmds.undoInfo(openChunk=True, chunkName="EditAttributes")
    try:
        yield
    finally:
        if enabled:
            cmds.undoInfo(closeChunk=True)


def execute_plug_writes(plan: Sequence[PlugWrite]) -> None:
    """入力元や値型をまたぐ全差分を適用し、途中失敗では逆順に復旧する。"""
    applied: list[PlugWrite] = []
    try:
        for write in plan:
            write.validate()
            applied.append(write)
            write.apply()
    except Exception as error:
        failures: list[Exception] = [error]
        for write in reversed(applied):
            try:
                write.restore()
            except Exception as restore_error:
                failures.append(restore_error)
        if len(failures) > 1:
            raise ExceptionGroup("属性の入力と復旧に失敗しました", failures)
        raise


class PlugsStore(qt.QObject, Generic[_ValueT]):
    """先頭を代表値として読み、入力時だけ編集可能な対象へ一括適用する。"""

    state_changed = qt.Signal()
    edit_failed = qt.Signal(str)

    def __init__(
        self,
        targets: Sequence[PlugTarget[_ValueT]],
        owner: qt.QObject,
        *,
        float_view_model: FloatViewModel | None = None,
    ) -> None:
        """対象を重複排除せず検証し、書込みなしで監視を開始する。"""
        if not targets:
            raise ValueError("plugsには一つ以上の属性を指定してください")
        for index, target in enumerate(targets):
            if any(target.plug == prior.plug for prior in targets[:index]):
                raise ValueError("同じ属性を複数回指定できません")
        super().__init__(owner)
        self._targets = tuple(targets)
        self._disposed = False
        self._write_depth = 0
        self._refreshing = False
        self._refresh_pending = False
        self._refresh_scheduled = False
        self._states: tuple[MayaPlugTargetState, ...] = ()
        self._values: tuple[_ValueT | None, ...] = ()
        self._float_view_model = float_view_model
        self._edit_undo = (
            None
            if float_view_model is None
            else FloatEditUndo(float_view_model)
        )
        self._registry = MayaCallbackRegistry(
            self, on_maya_exiting=self.dispose
        )
        self.destroyed.connect(self._on_destroyed)
        try:
            self._register_callbacks()
            self._read_state()
        except Exception:
            self.dispose()
            raise

    @property
    def is_available(self) -> bool:
        """代表属性が存在する間だけ読取りを許可する。"""
        return not self.is_disposed and self._targets[0].is_available

    @property
    def is_disposed(self) -> bool:
        """監視終了とQt破棄の両方を確認する。"""
        return self._disposed or not qt.isValid(self)

    @property
    def is_writable(self) -> bool:
        """代表属性が書込み可能な場合だけ一括入力を許可する。"""
        return self.is_available and self._targets[0].state().is_writable

    @property
    def target_count(self) -> int:
        """構築時の対象数を返す。削除された対象も含む。"""
        return len(self._targets)

    @property
    def writable_count(self) -> int:
        """現在個別に書込みできる対象数を返す。"""
        return sum(state.is_writable for state in self._states)

    @property
    def target_states(self) -> tuple[MayaPlugTargetState, ...]:
        """最後に同期した対象順の状態と理由を返す。"""
        return self._states

    @property
    def target_plugs(self) -> tuple[om.MPlug, ...]:
        """複数入力間の重複を検証するため、対象実体を返す。"""
        return tuple(target.plug for target in self._targets)

    @property
    def is_mixed(self) -> bool:
        """利用可能な対象に代表値と異なる実値があるか返す。"""
        return bool(self._values) and any(
            value is not None and value != self._values[0]
            for value in self._values[1:]
        )

    def read(self) -> _ValueT:
        """代表属性の実値を読み、他の属性へ書き戻さない。"""
        if not self.is_available:
            raise RuntimeError("代表のMaya属性は利用できません")
        return self._targets[0].codec.read()

    def write(self, value: _ValueT) -> _ValueT:
        """一括入力後に代表属性の確定値を返す。"""
        self.request_value(value)
        return self.read()

    def request_value(self, value: _ValueT) -> bool:
        """全入力を先に検証し、差分だけをUndo可能な一操作として適用する。"""
        if self._write_depth:
            raise RuntimeError("一括書き込み中に別の入力は開始できません")
        if not self.is_writable:
            self.refresh()
            return False
        try:
            plan = self.prepare_write(value)
            if not plan:
                self.refresh()
                return False
            self._execute_write(plan)
        except Exception as error:
            self.refresh()
            if not self.is_disposed:
                self.edit_failed.emit(str(error))
            raise
        self.refresh()
        return True

    def prepare_write(self, value: _ValueT) -> list[PlugWrite]:
        """編集可能な全対象を検証してから、変更対象と復旧値を返す。"""
        if self._write_depth:
            raise RuntimeError("一括書き込み中に別の入力は開始できません")
        if not self.is_writable:
            raise RuntimeError("代表のMaya属性は編集できません")
        plan: list[PlugWrite] = []
        for target in self._targets:
            if not target.state().is_writable:
                continue
            try:
                requested = target.codec.validate(value)
            except ValueError as error:
                raise ValueError(f"{target.name()}: {error}") from error
            before = target.codec.read()
            if target.codec.to_ui(before) != requested:
                plan.append(
                    _PreparedPlugWrite(self, target, before, value, requested)
                )
        return plan

    @contextmanager
    def write_guard(self) -> Generator[None, None, None]:
        """書込み中の再入力とcallbackからの表示同期をまとめて抑止する。"""
        if self._write_depth:
            raise RuntimeError("一括書き込み中に別の入力は開始できません")
        if not self.is_writable:
            raise RuntimeError("代表のMaya属性は編集できません")
        self._write_depth += 1
        try:
            yield
        finally:
            self._write_depth -= 1

    def _execute_write(self, plan: Sequence[PlugWrite]) -> None:
        """途中失敗では変更済み対象を同じchunk内で元へ戻す。"""
        view_model = self._float_view_model
        if view_model is None or not view_model.is_editing:
            FloatEditUndo.finish_active()
        with self.write_guard():
            if self._edit_undo is None:
                with plugs_undo_chunk():
                    execute_plug_writes(plan)
            else:
                with self._edit_undo.write(), plugs_undo_chunk():
                    execute_plug_writes(plan)

    def validate_write_target(
        self, target: PlugTarget[_ValueT], requested: _ValueT
    ) -> None:
        """書込み直前に対象の利用可否を再確認する。"""
        if (
            not self.is_available
            or not self._targets[0].state().is_writable
            or not target.state().is_writable
        ):
            raise RuntimeError("入力中に対象属性の状態が変わりました")

    def _read_state(self) -> bool:
        """状態と全実値を読み、混在だけが変わった場合も検出する。"""
        states = tuple(target.state() for target in self._targets)
        values = tuple(
            target.codec.read() if state.is_available else None
            for target, state in zip(self._targets, states)
        )
        changed = states != self._states or values != self._values
        self._states = states
        self._values = values
        return changed

    def refresh(self) -> bool:
        """表示だけを同期し、再入した通知は次の読取りへまとめる。"""
        if self.is_disposed:
            return False
        if self._write_depth or self._refreshing:
            self._refresh_pending = True
            return False
        changed = False
        self._refreshing = True
        try:
            while True:
                self._refresh_pending = False
                state_changed = self._read_state()
                changed = self._refresh_view_model() or changed
                if self.is_disposed:
                    break
                if state_changed:
                    self.state_changed.emit()
                if self.is_disposed or not self._refresh_pending:
                    break
        finally:
            self._refreshing = False
        return changed

    def _refresh_view_model(self) -> bool:
        """具象Storeで対応するViewModelへ正本を通知する。"""
        raise NotImplementedError

    def _schedule_refresh(self, *_args: object) -> None:
        """関連するdirty・単位・Undo通知を一回の再読取りへまとめる。"""
        if self.is_disposed or self._refresh_scheduled or self._write_depth:
            return
        self._refresh_scheduled = True
        run_later(self._refresh_later)

    def _refresh_later(self) -> None:
        """予約後に終了したStoreへアクセスせず再読取りする。"""
        self._refresh_scheduled = False
        self.refresh()

    def _register_callbacks(self) -> None:
        """監視nodeごとの対象をcallbackへ渡し、別nodeの走査を省く。"""
        groups: list[tuple[om.MObject, list[PlugTarget[_ValueT]]]] = []
        for target in self._targets:
            node = target.plug.node()
            for registered_node, targets in groups:
                if node == registered_node:
                    targets.append(target)
                    break
            else:
                groups.append((node, [target]))

        # 実体でまとめた対象だけを保持し、改名やhash値の衝突に依存しない
        for node, targets in groups:
            node_targets = tuple(targets)
            self._registry.register(
                int(
                    om.MNodeMessage.addAttributeChangedCallback(
                        node, self._on_attribute_changed, node_targets
                    )
                )
            )
            self._registry.register(
                int(
                    om.MNodeMessage.addNodeDirtyPlugCallback(
                        node, self._on_plug_dirty, node_targets
                    )
                )
            )
            self._registry.register(
                int(
                    om.MNodeMessage.addNodePreRemovalCallback(
                        node, self._on_node_removed, node_targets
                    )
                )
            )
        for event in (
            "linearUnitChanged",
            "angularUnitChanged",
            "Undo",
            "Redo",
        ):
            self._registry.register(
                int(
                    om.MEventMessage.addEventCallback(
                        event, self._schedule_refresh
                    )
                )
            )

    def _on_attribute_changed(
        self,
        message: int,
        plug: om.MPlug,
        _other_plug: om.MPlug,
        client_data: object,
    ) -> None:
        """変更nodeの対象と祖先だけを照合し、値・状態・削除を同期する。"""
        if self.is_disposed:
            return
        matched = False
        for target in cast(tuple[PlugTarget[_ValueT], ...], client_data):
            if not target.is_available:
                continue
            if any(plug == watched for watched in target.watched):
                matched = True
                if message & om.MNodeMessage.kAttributeRemoved:
                    target.removed = True
        if matched and not self._write_depth:
            self.refresh()

    def _on_plug_dirty(
        self, _node: om.MObject, plug: om.MPlug, client_data: object
    ) -> None:
        """対象または祖先がdirtyになった場合だけ、評価後の再読取りを予約する。"""
        if self.is_disposed or self._refresh_scheduled or self._write_depth:
            return
        for target in cast(tuple[PlugTarget[_ValueT], ...], client_data):
            if target.is_available and any(
                plug == watched for watched in target.watched
            ):
                self._schedule_refresh()
                return

    def _on_node_removed(self, _node: om.MObject, client_data: object) -> None:
        """削除予定nodeの属性を恒久的に無効化する。"""
        if self.is_disposed:
            return
        for target in cast(tuple[PlugTarget[_ValueT], ...], client_data):
            target.removed = True
        if not self._write_depth:
            self.refresh()

    def dispose(self) -> None:
        """callbackと開いているUndoを即座に解除する。"""
        if self._disposed:
            return
        self._disposed = True
        self._refresh_scheduled = False
        if self._edit_undo is not None:
            self._edit_undo.dispose()
        self._registry.dispose()

    def _on_destroyed(self, *_args: object) -> None:
        """QObject破棄中は兄弟Viewへ通知せず外部状態だけを解放する。"""
        self.dispose()
