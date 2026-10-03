# coding: utf-8
from __future__ import annotations

from typing import cast

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import StringViewModel, qt
from ....ui.binding.string._connection import (
    connect_queued_qt_signal,
    disconnect_qt_connection,
)
from ....ui.binding.string._validation import require_string
from ...node.operator.node._core import NodeOperator
from ..callback import MayaCallbackRegistry


class MayaNodeNameStore(qt.QObject):
    """固定した一つのMayaノード名を文字列の正本として扱う。

    値は名前空間込みのノード名で、DAGの親パスを含まない。
    通常の改名とUndo / Redoは監視し、名前空間自体の改名やロック変更は
    `refresh()`で再取得する。対象削除後はUndoでも自動再接続しない。
    """

    def __init__(
        self,
        view_model: StringViewModel,
        node: NodeOperator,
        owner: qt.QObject,
        *,
        rename_shapes: bool = True,
    ) -> None:
        """既存ノードの実体を保持し、書込みなしで監視を始める。

        Args:
            view_model: このStoreを接続する専用のViewModel。
            node: 作成処理を実行済みの既存ノード。
            owner: StoreとMaya callbackの寿命を所有するQObject。
            rename_shapes: Maya標準のShape名追従を有効にするか。
        """
        if not isinstance(cast(object, node), NodeOperator):
            raise TypeError("nodeにはNodeOperatorを指定してください")
        if type(rename_shapes) is not bool:
            raise TypeError("rename_shapesにはboolを指定してください")
        if view_model.is_disposed:
            raise RuntimeError("StringViewModelは終了しています")
        super().__init__(owner)
        self._node_operator = node
        self._node_handle = om.MObjectHandle(node.m_obj)
        self._rename_shapes = rename_shapes
        self._view_model: StringViewModel | None = view_model
        self._is_disposed = False
        self._write_depth = 0
        self._refresh_scheduled = False
        self._refresh_timer = qt.QtCore.QTimer(self)
        self._refresh_timer.setSingleShot(True)
        self._refresh_timer.timeout.connect(self._refresh_later)
        self._registry = MayaCallbackRegistry(
            self, on_maya_exiting=self.dispose
        )
        self._disposed_connection = view_model.disposed.connect(self.dispose)
        self._destroyed_connection = connect_queued_qt_signal(
            view_model.destroyed, self.dispose
        )
        try:
            # 作成予約中や削除済みの実体を既存ノードとして接続しない
            selection = om.MSelectionList()
            selection.add(self._cmds_node_name())
            if selection.getDependNode(0) != self._node_handle.object():
                raise ValueError("シーン上の既存ノードを指定してください")
            self._register_callbacks()
        except Exception:
            self.dispose()
            self.deleteLater()
            raise

    @property
    def node_operator(self) -> NodeOperator:
        """接続対象を包む元のNodeOperatorを返す。"""
        return self._node_operator

    @property
    def is_disposed(self) -> bool:
        """監視終了またはQtの所有者破棄済みならTrueを返す。"""
        return (
            self._is_disposed
            or not qt.isValid(self)
            or self._registry.is_disposed
        )

    @property
    def is_available(self) -> bool:
        """接続したノードの実体を現在も読み取れるか返す。"""
        return not self.is_disposed and self._node_handle.isValid()

    @property
    def is_writable(self) -> bool:
        """参照、ノードロック、名前ロックを現在の状態で判定する。"""
        if not self.is_available:
            return False
        try:
            node = self._fn_node()
            if node.isLocked or node.isFromReferencedFile:
                return False
            locked = cast(
                list[bool],
                cmds.lockNode(
                    self._cmds_node_name(), query=True, lockName=True
                ),
            )
            return not locked[0]
        except RuntimeError:
            return False

    def read(self) -> str:
        """名前空間の相対表示設定に依存しない確定名を返す。"""
        return self._fn_node().absoluteName().removeprefix(":")

    def write(self, value: str) -> str:
        """名前空間を保って改名し、Mayaが採番した実名を返す。

        一回の実変更をMaya標準Undoへ載せる。現在と同じ名前空間を含む
        入力も受け付けるが、別の名前空間への移動やDAGパスは拒否する。

        Raises:
            ValueError: 空の名前、DAGパス、制御文字、名前空間の変更。
            RuntimeError: 対象が利用できないかMayaが改名を拒否した場合。
        """
        requested = self._resolve_requested_name(require_string(value))
        if not self.is_writable:
            raise RuntimeError("対象ノードの名前は変更できません")
        if requested.removeprefix(":") == self.read():
            return self.read()

        # 自身の改名通知は、コマンド終了後の実値読込みへまとめる
        self._write_depth += 1
        try:
            cmds.rename(
                self._cmds_node_name(),
                requested,
                ignoreShape=not self._rename_shapes,
            )
            actual = self.read()
        finally:
            self._write_depth -= 1
        self.refresh()
        return self.read() if self.is_available else actual

    def refresh(self) -> bool:
        """実名と編集可否を再読込みし、確定値の変更有無を返す。"""
        view_model = self._view_model
        if (
            view_model is None
            or not qt.isValid(view_model)
            or view_model.is_disposed
        ):
            self.dispose()
            return False
        if view_model.store is not self:
            return False
        return view_model.refresh_from_store(self)

    def dispose(self, *_args: object) -> None:
        """コールバックを直ちに解除し、以降の改名を停止する。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        self._refresh_scheduled = False
        if qt.isValid(self._refresh_timer):
            self._refresh_timer.stop()
        disconnect_qt_connection(self._disposed_connection)
        disconnect_qt_connection(self._destroyed_connection)
        self._registry.dispose()
        view_model = self._view_model
        self._view_model = None
        if (
            view_model is not None
            and qt.isValid(view_model)
            and view_model.store is self
        ):
            view_model.store_became_unavailable(self)

    def _validate_attached_view_model(
        self, view_model: StringViewModel
    ) -> None:
        """構築時に指定した専用ViewModelへの接続だけを許可する。"""
        if view_model is not self._view_model:
            raise ValueError("別のStringViewModelへStoreを接続できません")

    def _fn_node(self) -> om.MFnDependencyNode:
        """保存した実体の生存を検証して関数セットを返す。"""
        if not self.is_available:
            raise RuntimeError("対象のMayaノードは利用できません")
        return om.MFnDependencyNode(self._node_handle.object())

    def _cmds_node_name(self) -> str:
        """現在の親階層から一意なコマンド対象名を組み立てる。"""
        node = self._fn_node()
        if not node.object().hasFn(om.MFn.kDagNode):
            return node.absoluteName()
        path = om.MDagPath.getAPathTo(node.object())
        names: list[str] = []
        while path.length():
            names.append(om.MFnDependencyNode(path.node()).absoluteName())
            path.pop()
        return "|" + "|".join(reversed(names))

    def _resolve_requested_name(self, value: str) -> str:
        """入力を現在の名前空間内の絶対名へ解決する。"""
        if (
            not value.strip()
            or "|" in value
            or any(ord(c) < 32 or ord(c) == 127 for c in value)
        ):
            raise ValueError("空の名前、DAGパス、制御文字は指定できません")
        namespace = self.read().rpartition(":")[0]
        local_name = value
        if ":" in value:
            supplied_namespace, _, local_name = value.removeprefix(
                ":"
            ).rpartition(":")
            if supplied_namespace != namespace:
                raise ValueError("名前空間の移動は別の操作で行ってください")
        if not local_name.strip():
            raise ValueError("空のノード名は指定できません")
        return f":{namespace}:{local_name}" if namespace else f":{local_name}"

    def _register_callbacks(self) -> None:
        """対象の改名と削除、およびUndo / Redoを監視する。"""
        node = self._node_handle.object()
        self._registry.register(
            int(
                om.MNodeMessage.addNameChangedCallback(
                    node, self._schedule_refresh
                )
            )
        )
        self._registry.register(
            int(om.MNodeMessage.addNodePreRemovalCallback(node, self.dispose))
        )
        for event in ("Undo", "Redo"):
            self._registry.register(
                int(
                    om.MEventMessage.addEventCallback(
                        event, self._schedule_refresh
                    )
                )
            )

    def _schedule_refresh(self, *_args: object) -> None:
        """同じイベントループの通知を一回の読込みへまとめる。"""
        if self.is_disposed or self._write_depth or self._refresh_scheduled:
            return
        self._refresh_scheduled = True
        self._refresh_timer.start(0)

    def _refresh_later(self) -> None:
        """終了後の遅延通知を無視して、現在の実名を公開する。"""
        if self.is_disposed:
            return
        self._refresh_scheduled = False
        self.refresh()
