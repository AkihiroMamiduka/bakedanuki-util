# coding: utf-8
"""複数scalar属性のChannel Box公開状態とlockを値と独立して編集する。"""

from __future__ import annotations

from collections.abc import Generator, Sequence
from contextlib import contextmanager, nullcontext
from dataclasses import dataclass
from typing import Literal, Protocol, TypeAlias

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import qt
from ...node.operator.node._core import NodeOperator
from ..callback import MayaCallbackRegistry
from ._float_edit import FloatEditUndo
from ._float_plug_endpoint import run_later
from .edit_session import MayaEditSession

ChannelDisplayState: TypeAlias = Literal["keyable", "channel_box", "hidden"]
_Operation: TypeAlias = Literal["display", "lock"]

__all__ = [
    "ChannelDisplayState",
    "MayaChannelStatePlug",
    "MayaChannelTargetState",
    "MayaChannelStateSnapshot",
    "MayaChannelStateBinding",
]


class MayaChannelStatePlug(Protocol):
    """具体的なPlugOperatorの型を失わず、必要な参照だけを受け取る。"""

    @property
    def node(self) -> NodeOperator:
        """対象plugを所有する既存nodeを返す。"""
        raise NotImplementedError

    @property
    def plug(self) -> om.MPlug:
        """状態を読み書きする実体を返す。"""
        raise NotImplementedError


@dataclass(frozen=True)
class MayaChannelTargetState:
    """一属性の表示・実効lockと、操作別の編集可否を保持する。"""

    plug_name: str
    is_available: bool
    display_state: ChannelDisplayState | None
    locked: bool | None
    parent_locked: bool
    display_reason: str | None
    lock_reason: str | None

    @property
    def can_set_display(self) -> bool:
        """値のlockや入力接続とは独立した表示変更可否を返す。"""
        return self.is_available and self.display_reason is None

    @property
    def can_set_locked(self) -> bool:
        """親を暗黙に解除せず対象自身のlockを変更できるか返す。"""
        return self.is_available and self.lock_reason is None


@dataclass(frozen=True)
class MayaChannelStateSnapshot:
    """先頭の代表状態と、利用可能な全対象の混在状態を保持する。"""

    display_state: ChannelDisplayState | None
    display_mixed: bool
    locked: bool | None
    lock_mixed: bool
    can_set_display: bool
    can_set_locked: bool
    target_count: int
    display_writable_count: int
    lock_writable_count: int
    targets: tuple[MayaChannelTargetState, ...]


@dataclass(frozen=True)
class _RawState:
    """非正規化状態も失わず復旧するため、Mayaの生フラグを保持する。"""

    keyable: bool
    channel_box: bool
    locked: bool

    @property
    def display(self) -> ChannelDisplayState:
        """両フラグがTrueの場合も、表示名はKeyableを優先する。"""
        if self.keyable:
            return "keyable"
        return "channel_box" if self.channel_box else "hidden"


class _ChannelTarget:
    """同名再作成へ再接続せず、対象と祖先の実体を監視する。"""

    def __init__(self, operator: MayaChannelStatePlug) -> None:
        """配列配下と非scalarを拒否し、実体と祖先を記録する。"""
        self.node = operator.node
        self.plug = operator.plug
        attribute = self.plug.attribute()
        if self.plug.isCompound or not any(
            attribute.hasFn(kind)
            for kind in (
                om.MFn.kNumericAttribute,
                om.MFn.kUnitAttribute,
                om.MFn.kEnumAttribute,
            )
        ):
            raise TypeError("単一のnumeric・unit・enum属性を指定してください")
        watched = [self.plug]
        while True:
            ancestor = watched[-1]
            if ancestor.isArray or ancestor.isElement:
                raise TypeError("配列配下の属性には対応していません")
            if not ancestor.isChild:
                break
            watched.append(ancestor.parent())
        self.watched = tuple(watched)
        self.node_handle = om.MObjectHandle(self.plug.node())
        self.attribute_handle = om.MObjectHandle(attribute)
        self.removed = False
        self.last_name = self.name()

    @property
    def is_available(self) -> bool:
        """削除された対象はUndo後も再利用しない。"""
        return (
            not self.removed
            and self.node_handle.isValid()
            and self.attribute_handle.isValid()
        )

    def name(self) -> str:
        """改名と同名DAGに対応した現在の正式plug名を取得する。"""
        path = self.plug.partialName(
            includeNodeName=False,
            useAlias=False,
            useFullAttributePath=True,
            useLongNames=True,
        )
        return f"{self.node.cmd_access_name}.{path}"

    def raw(self) -> _RawState:
        """書込みと正規化を行わず現在の生フラグを取得する。"""
        return _RawState(
            bool(self.plug.isKeyable),
            bool(self.plug.isChannelBox),
            bool(self.plug.isLocked),
        )

    def state(self) -> MayaChannelTargetState:
        """表示とlockの変更可否を独立して判定する。"""
        if not self.is_available:
            reason = "ノードまたは属性が削除されました"
            return MayaChannelTargetState(
                self.last_name, False, None, None, False, reason, reason
            )
        self.last_name = self.name()
        raw = self.raw()
        display_reason = None
        if raw.keyable and raw.channel_box:
            # 属性定義由来の両TrueはsetAttrのUndoで元へ戻せない
            display_reason = (
                "KeyableとChannelBoxが同時に有効な属性は"
                "Undoで復元できないため表示状態を変更できません"
            )
        parent_locked = any(plug.isLocked for plug in self.watched[1:])
        lock_reason = None
        if parent_locked:
            lock_reason = "親の属性がロックされています"
        elif om.MFnDependencyNode(self.plug.node()).isLocked:
            lock_reason = "ノードがロックされています"
        return MayaChannelTargetState(
            self.last_name,
            True,
            raw.display,
            raw.locked,
            parent_locked,
            display_reason,
            lock_reason,
        )


class MayaChannelStateBinding(qt.QObject):
    """複数属性の公開状態とlockを、明示操作だけで一括変更する。"""

    state_changed = qt.Signal()
    edit_failed = qt.Signal(str)

    def __init__(
        self,
        plugs: Sequence[MayaChannelStatePlug],
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """先頭を代表にし、値やフラグを書き戻さず監視を開始する。"""
        targets = tuple(_ChannelTarget(plug) for plug in plugs)
        if not targets:
            raise ValueError("plugsには一つ以上の属性を指定してください")
        for index, target in enumerate(targets):
            if any(target.plug == prior.plug for prior in targets[:index]):
                raise ValueError("同じ属性を複数回指定できません")
        super().__init__(parent)
        self._targets = targets
        self._disposed = False
        self._writing = False
        self._refreshing = False
        self._refresh_pending = False
        self._refresh_scheduled = False
        self._state = self._read_state()
        self._registry = MayaCallbackRegistry(
            self, on_maya_exiting=self.dispose
        )
        self.destroyed.connect(self._on_destroyed)
        try:
            self._register_callbacks()
        except Exception:
            self.dispose()
            raise

    @property
    def state(self) -> MayaChannelStateSnapshot:
        """最後に同期したimmutableな表示状態を返す。"""
        return self._state

    @property
    def is_disposed(self) -> bool:
        """手動終了とQt owner破棄の両方を確認する。"""
        return self._disposed or not qt.isValid(self)

    def _read_state(self) -> MayaChannelStateSnapshot:
        """代表値と操作別の対象数を、全対象の状態から集約する。"""
        states = tuple(target.state() for target in self._targets)
        first = states[0]
        available = tuple(state for state in states if state.is_available)
        return MayaChannelStateSnapshot(
            display_state=first.display_state,
            display_mixed=len({state.display_state for state in available})
            > 1,
            locked=first.locked,
            lock_mixed=len({state.locked for state in available}) > 1,
            can_set_display=first.can_set_display,
            can_set_locked=first.can_set_locked,
            target_count=len(states),
            display_writable_count=sum(s.can_set_display for s in states),
            lock_writable_count=sum(s.can_set_locked for s in states),
            targets=states,
        )

    def refresh(self) -> bool:
        """値を書かず同期し、通知中の再読取り要求をまとめる。"""
        if self.is_disposed:
            return False
        if self._writing or self._refreshing:
            self._refresh_pending = True
            return False
        changed = False
        self._refreshing = True
        try:
            while True:
                self._refresh_pending = False
                state = self._read_state()
                if state != self._state:
                    self._state = state
                    changed = True
                    self.state_changed.emit()
                if self.is_disposed or not self._refresh_pending:
                    break
        finally:
            self._refreshing = False
        return changed

    def set_display_state(
        self,
        state: ChannelDisplayState,
        *,
        edit_session: MayaEditSession | None = None,
    ) -> bool:
        """公開状態の差分を、単独または共有セッションのUndoで適用する。"""
        if state not in ("keyable", "channel_box", "hidden"):
            raise ValueError("stateにはkeyable/channel_box/hiddenを指定します")
        return self._request("display", state, edit_session)

    def set_locked(self, locked: bool) -> bool:
        """親lockを変更せず、対象自身のlock差分だけを一括適用する。"""
        if type(locked) is not bool:
            raise TypeError("lockedにはboolを指定してください")
        return self._request("lock", locked)

    def _request(
        self,
        operation: _Operation,
        value: ChannelDisplayState | bool,
        edit_session: MayaEditSession | None = None,
    ) -> bool:
        """対象と差分を先に確認し、失敗時は変更済みフラグを復旧する。"""
        if self.is_disposed:
            raise RuntimeError("終了済みのBindingには入力できません")
        if self._writing:
            raise RuntimeError("状態変更中に別の入力は開始できません")
        self.refresh()
        if not self._can_edit(self._state.targets[0], operation):
            return False
        plan: list[tuple[_ChannelTarget, _RawState, _RawState]] = []
        for target in self._targets:
            if not self._can_edit(target.state(), operation):
                continue
            before = target.raw()
            requested = (
                _RawState(
                    value == "keyable", value == "channel_box", before.locked
                )
                if operation == "display"
                else _RawState(
                    before.keyable, before.channel_box, value is True
                )
            )
            if before != requested:
                plan.append((target, before, requested))
        if not plan:
            return False

        # 他の値ドラッグと状態変更を別のUndo操作として閉じる
        FloatEditUndo.finish_active()
        self._writing = True
        try:
            with (
                edit_session.write()
                if edit_session is not None
                else nullcontext()
            ), self._undo_chunk():
                self._execute(plan, operation)
        except Exception as error:
            self._writing = False
            self.refresh()
            if not self.is_disposed:
                self.edit_failed.emit(str(error))
            raise
        finally:
            self._writing = False
        self.refresh()
        return True

    @staticmethod
    def _can_edit(
        state: MayaChannelTargetState, operation: _Operation
    ) -> bool:
        """操作対象となるフラグに対応した編集可否を返す。"""
        return (
            state.can_set_display
            if operation == "display"
            else state.can_set_locked
        )

    @contextmanager
    def _undo_chunk(self) -> Generator[None, None, None]:
        """MayaのUndo設定を維持し、開いたchunkを必ず閉じる。"""
        enabled = bool(cmds.undoInfo(query=True, state=True))
        if enabled:
            cmds.undoInfo(openChunk=True, chunkName="EditChannelStates")
        try:
            yield
        finally:
            if enabled:
                cmds.undoInfo(closeChunk=True)

    def _execute(
        self,
        plan: list[tuple[_ChannelTarget, _RawState, _RawState]],
        operation: _Operation,
    ) -> None:
        """書込み直前にも状態を検査し、途中失敗では逆順に復旧する。"""
        applied: list[tuple[_ChannelTarget, _RawState]] = []
        try:
            for target, before, requested in plan:
                if self.is_disposed or not self._can_edit(
                    target.state(), operation
                ):
                    raise RuntimeError("入力中に対象属性の状態が変わりました")
                applied.append((target, before))
                self._write(target, requested, operation)
                if target.raw() != requested:
                    raise RuntimeError(
                        f"Mayaが状態変更を拒否しました: {target.name()}"
                    )
        except Exception as error:
            failures: list[Exception] = [error]
            for target, before in reversed(applied):
                try:
                    if target.raw() != before:
                        self._write(target, before, operation)
                except Exception as restore_error:
                    failures.append(restore_error)
            if len(failures) > 1:
                raise ExceptionGroup(
                    "属性状態の変更と復旧に失敗しました", failures
                )
            raise

    @staticmethod
    def _write(
        target: _ChannelTarget, raw: _RawState, operation: _Operation
    ) -> None:
        """値を変更せず、Maya標準Undoへ対象フラグだけを記録する。"""
        if operation == "display":
            # 両flagの同時指定はMayaのUndoでchannelBoxを失うため分ける
            if raw.keyable:
                if bool(target.plug.isChannelBox) != raw.channel_box:
                    cmds.setAttr(target.name(), channelBox=raw.channel_box)
                if not target.plug.isKeyable:
                    cmds.setAttr(target.name(), keyable=True)
            else:
                if target.plug.isKeyable:
                    cmds.setAttr(target.name(), keyable=False)
                if bool(target.plug.isChannelBox) != raw.channel_box:
                    cmds.setAttr(target.name(), channelBox=raw.channel_box)
        else:
            cmds.setAttr(target.name(), lock=raw.locked)

    def _register_callbacks(self) -> None:
        """対象nodeだけを監視し、UndoとRedoの同期も登録する。"""
        visited: set[int] = set()
        for target in self._targets:
            identity = target.node_handle.hashCode()
            if identity in visited:
                continue
            visited.add(identity)
            node = target.plug.node()
            self._registry.register(
                int(
                    om.MNodeMessage.addAttributeChangedCallback(
                        node, self._on_attribute_changed
                    )
                )
            )
            self._registry.register(
                int(
                    om.MNodeMessage.addNodePreRemovalCallback(
                        node, self._on_node_removed
                    )
                )
            )
            self._registry.register(
                int(
                    om.MNodeMessage.addNameChangedCallback(
                        node, self._schedule_refresh
                    )
                )
            )
        for event in ("Undo", "Redo"):
            self._registry.register(
                int(
                    om.MEventMessage.addEventCallback(
                        event, self._schedule_refresh
                    )
                )
            )

    def _on_attribute_changed(
        self, message: int, plug: om.MPlug, _other: om.MPlug, _data: object
    ) -> None:
        """channelBox単独変更も含め、対象と祖先の通知だけを処理する。"""
        matched = False
        for target in self._targets:
            if target.removed:
                continue
            if any(plug == watched for watched in target.watched):
                matched = True
                if message & om.MNodeMessage.kAttributeRemoved:
                    target.removed = True
        if matched and not self._writing:
            self.refresh()

    def _on_node_removed(self, node: om.MObject, *_args: object) -> None:
        """削除予定の対象を無効化し、同名の再作成へ接続しない。"""
        for target in self._targets:
            if (
                target.node_handle.isValid()
                and target.node_handle.object() == node
            ):
                target.removed = True
        if not self._writing:
            self.refresh()

    def _schedule_refresh(self, *_args: object) -> None:
        """同じevent loop内のUndo等の通知を一回の読取りにまとめる。"""
        if self.is_disposed or self._writing or self._refresh_scheduled:
            return
        self._refresh_scheduled = True
        run_later(self._refresh_later)

    def _refresh_later(self) -> None:
        """予約後に終了したBindingへの読取りを停止する。"""
        self._refresh_scheduled = False
        self.refresh()

    def dispose(self) -> None:
        """全callbackを即座に解除し、遅延入力と同期を停止する。"""
        if self._disposed:
            return
        self._disposed = True
        self._refresh_scheduled = False
        self._registry.dispose()

    def _on_destroyed(self, *_args: object) -> None:
        """QObject破棄時は表示へ通知せず監視だけを終了する。"""
        self.dispose()
