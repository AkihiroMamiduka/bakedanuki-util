# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

import pytest

from bd_util import Nodes
from bd_util.maya.ui import MayaBoolPlugStore, MayaBoolPlugView
from bd_util.maya.ui.binding.bool_plug import (
    MayaBoolPlugStore as ModuleMayaBoolPlugStore,
)
from bd_util.maya.ui.binding.bool_plug import (
    MayaBoolPlugView as ModuleMayaBoolPlugView,
)
from bd_util.maya.ui.callback import dispose_owned_callbacks
from bd_util.ui import BoolViewModel, qt


@dataclass
class _BindingContext:
    """実Maya binding testで共有するobject。"""

    node_name: str
    view_model: BoolViewModel
    store: MayaBoolPlugStore
    owner: qt.QObject


@pytest.fixture
def bool_binding(new_scene, maya_cmds) -> _BindingContext:
    """transform.visibilityへ接続したViewModel一式を提供する。"""
    node_name = maya_cmds.createNode("transform", name="boolBindingTest")
    nodes = Nodes()
    node = nodes.existing.transform(node_name)
    owner = qt.QObject()
    view_model = BoolViewModel(False, owner)
    store = MayaBoolPlugStore(
        view_model,
        node.visibility,
        owner,
    )
    view_model.attach_store(store)
    context = _BindingContext(
        node_name=node_name,
        view_model=view_model,
        store=store,
        owner=owner,
    )
    yield context
    store.dispose()


def _process_events() -> None:
    """dirty callbackが予約したQt処理を実行する。"""
    qt.QtCore.QCoreApplication.processEvents()


def test_role_module_and_facade_share_class_definitions() -> None:
    assert ModuleMayaBoolPlugStore is MayaBoolPlugStore
    assert ModuleMayaBoolPlugView is MayaBoolPlugView


def test_store_uses_maya_value_as_initial_state(bool_binding) -> None:
    # transform.visibilityの既定値Trueを正本として初期同期する。
    assert bool_binding.store.is_available
    assert bool_binding.store.is_writable
    assert bool_binding.view_model.value.value is True
    assert bool_binding.view_model.set_value_command.can_execute


def test_store_attachment_is_explicit(new_scene, maya_cmds) -> None:
    # Store構築だけではViewModelの正本を暗黙に変更しない。
    node_name = maya_cmds.createNode("transform", name="explicitStoreTest")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    view_model = BoolViewModel(False, owner)
    store = MayaBoolPlugStore(view_model, node.visibility, owner)
    try:
        assert view_model.store is None
        assert view_model.value.value is False

        view_model.attach_store(store)
        assert view_model.store is store
        assert view_model.value.value is True
    finally:
        store.dispose()


def test_store_rejects_a_different_view_model(new_scene, maya_cmds) -> None:
    # callback先と正本のattach先が分裂する誤接続を拒否する。
    node_name = maya_cmds.createNode("transform", name="storeIdentityTest")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    callback_view_model = BoolViewModel(False, owner)
    other_view_model = BoolViewModel(False, owner)
    store = MayaBoolPlugStore(
        callback_view_model,
        node.visibility,
        owner,
    )
    try:
        with pytest.raises(ValueError, match="構築時に指定"):
            other_view_model.attach_store(store)
        assert callback_view_model.store is None
        assert other_view_model.store is None
    finally:
        store.dispose()


def test_store_preserves_runtime_argument_validation(
    new_scene,
    maya_cmds,
) -> None:
    # 型注釈を迂回するPython呼び出し用にruntime検証も維持する。
    node_name = maya_cmds.createNode("transform", name="argumentTest")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    view_model = BoolViewModel(False, owner)

    with pytest.raises(TypeError, match="view_model"):
        MayaBoolPlugStore(
            object(),  # pyright: ignore[reportArgumentType]
            node.visibility,
            owner,
        )
    with pytest.raises(TypeError, match="owner"):
        MayaBoolPlugStore(
            view_model,
            node.visibility,
            object(),  # pyright: ignore[reportArgumentType]
        )
    with pytest.raises(TypeError, match="plug"):
        MayaBoolPlugStore(
            view_model,
            object(),  # pyright: ignore[reportArgumentType]
            owner,
        )

    store = MayaBoolPlugStore(view_model, node.visibility, owner)
    try:
        with pytest.raises(TypeError, match="value"):
            store.write(1)  # pyright: ignore[reportArgumentType]
    finally:
        store.dispose()


def test_command_writes_with_maya_undo_and_redo(
    bool_binding,
    maya_cmds,
) -> None:
    # UI/Python共通Commandよりvisibilityを変更する。
    maya_cmds.undoInfo(state=True)
    maya_cmds.flushUndo()
    events: list[bool] = []
    bool_binding.view_model.value.changed.connect(events.append)
    assert bool_binding.view_model.set_value_command.execute(False)
    assert not maya_cmds.getAttr(f"{bool_binding.node_name}.visibility")
    assert events == [False]

    # Maya標準undo/redoのcallbackも同じデータへ同期する。
    maya_cmds.undo()
    assert bool_binding.view_model.value.value is True
    maya_cmds.redo()
    assert bool_binding.view_model.value.value is False
    assert events == [False, True, False]


def test_external_maya_change_updates_data_without_write_back(
    bool_binding,
    maya_cmds,
) -> None:
    # Store外部からのMaya操作をcallbackで同期する。
    maya_cmds.setAttr(f"{bool_binding.node_name}.visibility", False)
    assert bool_binding.view_model.value.value is False

    # unrelatedなattribute変更ではboolデータを変更しない。
    events: list[bool] = []
    bool_binding.view_model.value.changed.connect(events.append)
    maya_cmds.setAttr(f"{bool_binding.node_name}.translateX", 10.0)
    assert bool_binding.view_model.value.value is False
    assert events == []


def test_lock_state_updates_command_availability(
    bool_binding,
    maya_cmds,
) -> None:
    # visibilityのlock変更をcallbackでCommand状態へ反映する。
    maya_cmds.setAttr(
        f"{bool_binding.node_name}.visibility",
        lock=True,
    )
    assert not bool_binding.store.is_writable
    assert not bool_binding.view_model.set_value_command.can_execute

    maya_cmds.setAttr(
        f"{bool_binding.node_name}.visibility",
        lock=False,
    )
    assert bool_binding.store.is_writable
    assert bool_binding.view_model.set_value_command.can_execute


def test_incoming_connection_disables_command_and_dirty_updates_value(
    bool_binding,
    maya_cmds,
) -> None:
    # 別transformのvisibilityを同期対象へ接続する。
    source = maya_cmds.createNode("transform", name="boolBindingSource")
    maya_cmds.connectAttr(
        f"{source}.visibility",
        f"{bool_binding.node_name}.visibility",
    )
    assert not bool_binding.store.is_writable
    assert not bool_binding.view_model.set_value_command.can_execute

    # 上流値の評価変更はdirty callback経由で次のevent loopに同期する。
    maya_cmds.setAttr(f"{source}.visibility", False)
    _process_events()
    assert bool_binding.view_model.value.value is False


def test_node_rename_keeps_store_connected(
    bool_binding,
    maya_cmds,
) -> None:
    # callbackはnode名ではなくMObjectを追跡する。
    renamed = maya_cmds.rename(bool_binding.node_name, "renamedBindingTest")
    maya_cmds.setAttr(f"{renamed}.visibility", False)
    assert bool_binding.view_model.value.value is False
    assert bool_binding.store.plug_operator.plug.name().endswith(".visibility")

    # Command書き込みもrename後の完全パスを動的に解決する。
    assert bool_binding.view_model.set_value_command.execute(True)
    assert maya_cmds.getAttr(f"{renamed}.visibility")


def test_command_targets_duplicate_dag_name_by_full_path(
    new_scene,
    maya_cmds,
) -> None:
    # 異なる親の下へ同じshort nameのtransformを作成する。
    first_parent = maya_cmds.createNode("transform", name="firstParent")
    second_parent = maya_cmds.createNode("transform", name="secondParent")
    maya_cmds.createNode(
        "transform",
        name="duplicate",
        parent=first_parent,
    )
    maya_cmds.createNode(
        "transform",
        name="duplicate",
        parent=second_parent,
    )
    first_path = "|firstParent|duplicate"
    second_path = "|secondParent|duplicate"

    # 後者だけへbindingし、曖昧なshort plug名を使わず書き込む。
    owner = qt.QObject()
    view_model = BoolViewModel(False, owner)
    node = Nodes().existing.transform(second_path)
    store = MayaBoolPlugStore(
        view_model,
        node.visibility,
        owner,
    )
    view_model.attach_store(store)
    try:
        assert view_model.set_value_command.execute(False)
        assert maya_cmds.getAttr(f"{first_path}.visibility")
        assert not maya_cmds.getAttr(f"{second_path}.visibility")
    finally:
        store.dispose()


def test_node_removal_disables_binding(bool_binding, maya_cmds) -> None:
    # node削除前callbackで読み書き不可へ移行する。
    maya_cmds.delete(bool_binding.node_name)
    assert bool_binding.store.is_disposed
    assert not bool_binding.store.is_available
    assert not bool_binding.view_model.set_value_command.can_execute
    assert not bool_binding.view_model.set_value_command.execute(False)


def test_dispose_stops_external_updates(bool_binding, maya_cmds) -> None:
    # Storeを明示破棄して現在のデータ値を固定する。
    bool_binding.store.dispose()
    assert bool_binding.store.is_disposed
    assert not bool_binding.view_model.set_value_command.can_execute

    maya_cmds.setAttr(f"{bool_binding.node_name}.visibility", False)
    assert bool_binding.view_model.value.value is True


def test_controller_style_callback_disposal_stops_store_immediately(
    bool_binding,
    maya_cmds,
) -> None:
    # WindowControllerがDeferredDelete前にregistryだけを解除する経路を再現する。
    assert dispose_owned_callbacks(bool_binding.owner) == 1
    assert bool_binding.store.is_disposed
    assert not bool_binding.store.is_available
    assert not bool_binding.view_model.set_value_command.can_execute

    # callback解除後に書き込みだけが残る半端な状態へ移行しない。
    assert not bool_binding.view_model.set_value_command.execute(False)
    maya_cmds.setAttr(f"{bool_binding.node_name}.visibility", False)
    assert bool_binding.view_model.value.value is True


def test_changed_slot_disposal_does_not_reenable_command(
    bool_binding,
    maya_cmds,
) -> None:
    # data通知の同期slotからStoreを破棄するreentrant経路を再現する。
    bool_binding.view_model.value.changed.connect(
        lambda _value: bool_binding.store.dispose()
    )
    maya_cmds.setAttr(f"{bool_binding.node_name}.visibility", False)

    # refresh開始時の古いwritable状態でCommandを再度有効にしない。
    assert bool_binding.store.is_disposed
    assert not bool_binding.view_model.set_value_command.can_execute


def test_owner_destruction_stops_store_with_external_view_model(
    new_scene,
    maya_cmds,
) -> None:
    # ViewModelより先に独立ownerが破棄される構成を用意する。
    node_name = maya_cmds.createNode("transform", name="ownerLifetimeTest")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    view_model = BoolViewModel(False)
    store = MayaBoolPlugStore(
        view_model,
        node.visibility,
        owner,
    )
    view_model.attach_store(store)

    owner.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        owner,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt.QtCore.QCoreApplication.processEvents()

    assert store.is_disposed
    assert not store.is_available
    assert not view_model.set_value_command.can_execute
    maya_cmds.setAttr(f"{node_name}.visibility", False)
    assert view_model.value.value is True


def test_view_model_destruction_disposes_store_safely(
    bool_binding,
    maya_cmds,
) -> None:
    # ownerを残したままViewModelのC++ objectだけを先に破棄する。
    view_model = bool_binding.view_model
    view_model.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        view_model,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt.QtCore.QCoreApplication.processEvents()

    assert not qt.isValid(view_model)
    assert bool_binding.store.is_disposed
    assert not bool_binding.store.is_available
    with pytest.raises(RuntimeError, match="ViewModelは破棄"):
        _ = bool_binding.store.view_model

    # 後続のMaya変更と二重disposeでdeleted QObjectへアクセスしない。
    maya_cmds.setAttr(f"{bool_binding.node_name}.visibility", False)
    bool_binding.store.dispose()


def test_store_qobject_destruction_stops_callbacks(
    bool_binding,
    maya_cmds,
) -> None:
    # disposeを直接呼ばずStoreのC++ objectを破棄する。
    store = bool_binding.store
    store.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        store,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    qt.QtCore.QCoreApplication.processEvents()

    # registryとViewModelの両方が破棄通知へ追従する。
    assert not qt.isValid(store)
    assert store.is_disposed
    assert not bool_binding.view_model.set_value_command.can_execute
    maya_cmds.setAttr(f"{bool_binding.node_name}.visibility", False)
    assert bool_binding.view_model.value.value is True
