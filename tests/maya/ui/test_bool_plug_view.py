# coding: utf-8
from __future__ import annotations

import gc
from dataclasses import dataclass

import pytest

from bd_util import Nodes
from bd_util.maya.ui import MayaBoolPlugStore, MayaBoolPlugView
from bd_util.ui import BoolViewModel, PythonBoolAttributeStore, qt


@dataclass
class _BoolData:
    """Maya Viewより優先するPython側のtest data。"""

    visible: bool


class _NormalizingBoolData:
    """書き込み要求をFalseへ正規化するtest data。"""

    def __init__(self) -> None:
        """Falseを初期値として保持する。"""
        self._visible = False

    @property
    def visible(self) -> bool:
        """確定済みの値を返す。"""
        return self._visible

    @visible.setter
    def visible(self, _value: bool) -> None:
        """すべての要求をFalseへ正規化する。"""
        self._visible = False


class _FailingBoolStore:
    """書き込み前後の例外を再現するtest Store。"""

    def __init__(self, *, update_before_error: bool) -> None:
        """例外前に値を確定するか指定して初期化する。"""
        self.value = False
        self.update_before_error = update_before_error
        self.error = RuntimeError("Store write failed")

    @property
    def is_available(self) -> bool:
        """test中は常に利用可能。"""
        return True

    @property
    def is_writable(self) -> bool:
        """書き込み処理へ到達させるためTrueを返す。"""
        return True

    def read(self) -> bool:
        """確定済みの値を返す。"""
        return self.value

    def write(self, value: bool) -> bool:
        """指定条件で値を確定してから例外を送出する。"""
        if self.update_before_error:
            self.value = value
        raise self.error


@dataclass
class _ViewContext:
    """Maya bool plug View testで共有するobject。"""

    node_name: str
    data: _BoolData
    store: PythonBoolAttributeStore[_BoolData]
    view_model: BoolViewModel
    view: MayaBoolPlugView
    owner: qt.QObject


@pytest.fixture
def bool_plug_view(new_scene, maya_cmds) -> _ViewContext:
    """Python Storeとtransform.visibilityを接続した一式を返す。"""
    node_name = maya_cmds.createNode("transform", name="boolPlugViewTest")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    data = _BoolData(False)
    store = PythonBoolAttributeStore(data, "visible")
    view_model = BoolViewModel(parent=owner)
    view_model.attach_store(store)
    view = MayaBoolPlugView(view_model, node.visibility, owner)
    context = _ViewContext(
        node_name=node_name,
        data=data,
        store=store,
        view_model=view_model,
        view=view,
        owner=owner,
    )
    yield context
    view.dispose()


def _process_events() -> None:
    """遅延されたMaya入力を確定する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def test_store_value_wins_during_initial_sync(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # Maya既定値Trueではなく、Python StoreのFalseを初期表示する。
    assert bool_plug_view.view.is_available
    assert bool_plug_view.view.is_writable
    assert bool_plug_view.view.is_synchronized
    assert bool_plug_view.view.last_sync_error is None
    assert not maya_cmds.getAttr(f"{bool_plug_view.node_name}.visibility")
    assert bool_plug_view.data.visible is False


def test_view_requires_store_and_preserves_runtime_validation(
    new_scene,
    maya_cmds,
) -> None:
    # Maya Viewは値の正本を暗黙には作成しない。
    node_name = maya_cmds.createNode("transform", name="viewArgumentTest")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    view_model = BoolViewModel()
    with pytest.raises(RuntimeError, match="Storeを接続"):
        MayaBoolPlugView(view_model, node.visibility, owner)

    data = _BoolData(True)
    view_model.attach_store(PythonBoolAttributeStore(data, "visible"))
    with pytest.raises(TypeError, match="view_model"):
        MayaBoolPlugView(
            object(),  # pyright: ignore[reportArgumentType]
            node.visibility,
            owner,
        )
    with pytest.raises(TypeError, match="owner"):
        MayaBoolPlugView(
            view_model,
            node.visibility,
            object(),  # pyright: ignore[reportArgumentType]
        )
    with pytest.raises(TypeError, match="plug"):
        MayaBoolPlugView(
            view_model,
            object(),  # pyright: ignore[reportArgumentType]
            owner,
        )


def test_view_rejects_maya_plug_store_as_its_source(
    new_scene,
    maya_cmds,
) -> None:
    # 2つのMaya setAttrを1 Commandへぶら下げるundo不整合を防ぐ。
    store_node_name = maya_cmds.createNode(
        "transform",
        name="mayaStoreSource",
    )
    view_node_name = maya_cmds.createNode(
        "transform",
        name="mayaStoreView",
    )
    nodes = Nodes()
    owner = qt.QObject()
    view_model = BoolViewModel(parent=owner)
    maya_store = MayaBoolPlugStore(
        view_model,
        nodes.existing.transform(store_node_name).visibility,
        owner,
    )
    view_model.attach_store(maya_store)
    try:
        with pytest.raises(RuntimeError, match="Python側を正本"):
            MayaBoolPlugView(
                view_model,
                nodes.existing.transform(view_node_name).visibility,
                owner,
            )
    finally:
        maya_store.dispose()


def test_failed_initial_sync_releases_view_slot(new_scene, maya_cmds) -> None:
    # 初期描画に失敗してもcallbackと1 View制約の登録を残さない。
    node_name = maya_cmds.createNode("transform", name="failedInitialView")
    plug_name = f"{node_name}.visibility"
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    data = _BoolData(False)
    view_model = BoolViewModel(parent=owner)
    view_model.attach_store(PythonBoolAttributeStore(data, "visible"))

    maya_cmds.setAttr(plug_name, lock=True)
    with pytest.raises(RuntimeError, match="書き込めません"):
        MayaBoolPlugView(view_model, node.visibility, owner)

    maya_cmds.setAttr(plug_name, lock=False)
    view = MayaBoolPlugView(view_model, node.visibility, owner)
    try:
        assert view.is_synchronized
        assert not maya_cmds.getAttr(plug_name)
    finally:
        view.dispose()


def test_python_command_and_direct_store_refresh_update_maya_view(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # Python入力はStoreで確定後、Maya Viewへ描画する。
    assert bool_plug_view.view_model.set_value_command.execute(True)
    assert bool_plug_view.data.visible is True
    assert maya_cmds.getAttr(f"{bool_plug_view.node_name}.visibility")

    # dataclassを直接編集した場合も明示refresh後にViewへ反映する。
    bool_plug_view.data.visible = False
    assert bool_plug_view.view_model.refresh_from_store(bool_plug_view.store)
    assert not maya_cmds.getAttr(f"{bool_plug_view.node_name}.visibility")
    assert bool_plug_view.view.is_synchronized


def test_external_maya_change_updates_python_store(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # Maya側の入力も遅延callbackから共通Commandへ入る。
    maya_cmds.setAttr(f"{bool_plug_view.node_name}.visibility", True)
    assert bool_plug_view.data.visible is False
    assert not bool_plug_view.view.is_synchronized
    _process_events()

    assert bool_plug_view.data.visible is True
    assert bool_plug_view.view_model.value.value is True
    assert bool_plug_view.view.is_synchronized
    assert bool_plug_view.view.last_sync_error is None


def test_same_store_command_wins_over_queued_maya_input(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    plug_name = f"{bool_plug_view.node_name}.visibility"
    maya_cmds.setAttr(plug_name, True)
    assert not bool_plug_view.view.is_synchronized

    # Storeと同値でも、後から実行したCommandを操作順どおり優先する。
    assert not bool_plug_view.view_model.set_value_command.execute(False)
    assert not maya_cmds.getAttr(plug_name)
    _process_events()
    assert bool_plug_view.data.visible is False
    assert not maya_cmds.getAttr(plug_name)
    assert bool_plug_view.view.is_synchronized


def test_same_store_refresh_wins_over_queued_maya_input(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    plug_name = f"{bool_plug_view.node_name}.visibility"
    maya_cmds.setAttr(plug_name, True)
    assert not bool_plug_view.view.is_synchronized

    # 同値でも後から明示refreshしたStore値を操作順どおり優先する。
    assert not bool_plug_view.view_model.refresh_from_store(
        bool_plug_view.store
    )
    assert not maya_cmds.getAttr(plug_name)
    _process_events()
    assert bool_plug_view.data.visible is False
    assert not maya_cmds.getAttr(plug_name)
    assert bool_plug_view.view.is_synchronized


def test_maya_undo_redo_updates_store_without_echo_write(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # StoreからMayaへ行う1回の描画だけをundo履歴へ積む。
    maya_cmds.undoInfo(state=True)
    maya_cmds.flushUndo()
    assert bool_plug_view.view_model.set_value_command.execute(True)
    assert bool_plug_view.data.visible is True

    maya_cmds.undo()
    _process_events()
    assert bool_plug_view.data.visible is False
    assert bool_plug_view.view_model.value.value is False

    # callback echoがsetAttrしなければredo履歴を維持できる。
    maya_cmds.redo()
    _process_events()
    assert bool_plug_view.data.visible is True
    assert bool_plug_view.view_model.value.value is True
    assert bool_plug_view.view.is_synchronized


def test_locked_view_keeps_store_authoritative_and_syncs_after_unlock(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    plug_name = f"{bool_plug_view.node_name}.visibility"
    errors: list[object] = []
    bool_plug_view.view.sync_failed.connect(errors.append)
    maya_cmds.setAttr(plug_name, lock=True)
    _process_events()

    # Viewが書き込めなくてもStoreのCommandは有効なままにする。
    assert bool_plug_view.view_model.set_value_command.execute(True)
    assert bool_plug_view.data.visible is True
    assert not maya_cmds.getAttr(plug_name)
    assert bool_plug_view.view_model.set_value_command.can_execute
    assert not bool_plug_view.view.is_synchronized
    assert errors

    # 再び書き込み可能になった時、最新Store値をMayaへpushする。
    maya_cmds.setAttr(plug_name, lock=False)
    _process_events()
    assert maya_cmds.getAttr(plug_name)
    assert bool_plug_view.data.visible is True
    assert bool_plug_view.view.is_synchronized


def test_incoming_connection_does_not_replace_store_value(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    source = maya_cmds.createNode("transform", name="boolPlugViewSource")
    plug_name = f"{bool_plug_view.node_name}.visibility"
    maya_cmds.connectAttr(f"{source}.visibility", plug_name)
    maya_cmds.setAttr(f"{source}.visibility", True)
    _process_events()

    # driven値は入力として採用せず、Python Storeを維持する。
    assert maya_cmds.getAttr(plug_name)
    assert bool_plug_view.data.visible is False
    assert bool_plug_view.view_model.set_value_command.can_execute
    assert not bool_plug_view.view.is_synchronized

    maya_cmds.disconnectAttr(f"{source}.visibility", plug_name)
    _process_events()
    assert not maya_cmds.getAttr(plug_name)
    assert bool_plug_view.data.visible is False
    assert bool_plug_view.view.is_synchronized


def test_short_lived_incoming_connection_keeps_store_authoritative(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # connectとdisconnectが同じQt tick内でも接続値をStoreへ採用しない。
    source = maya_cmds.createNode("transform", name="shortLivedSource")
    plug_name = f"{bool_plug_view.node_name}.visibility"
    maya_cmds.connectAttr(f"{source}.visibility", plug_name)
    maya_cmds.disconnectAttr(f"{source}.visibility", plug_name)
    assert maya_cmds.getAttr(plug_name)

    _process_events()
    assert bool_plug_view.data.visible is False
    assert not maya_cmds.getAttr(plug_name)
    assert bool_plug_view.view.is_synchronized


def test_locked_equal_value_can_create_synchronized_view(
    new_scene,
    maya_cmds,
) -> None:
    # 現在値が既に一致するViewはlock中でも初期描画を必要としない。
    node_name = maya_cmds.createNode("transform", name="lockedEqualView")
    plug_name = f"{node_name}.visibility"
    maya_cmds.setAttr(plug_name, lock=True)
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    data = _BoolData(True)
    view_model = BoolViewModel(parent=owner)
    view_model.attach_store(PythonBoolAttributeStore(data, "visible"))
    view = MayaBoolPlugView(view_model, node.visibility, owner)
    try:
        assert not view.is_writable
        assert view.is_synchronized
        assert view.last_sync_error is None
    finally:
        view.dispose()


def test_rejected_maya_input_reports_desync_until_explicit_retry(
    new_scene,
    maya_cmds,
) -> None:
    node_name = maya_cmds.createNode("transform", name="normalizedView")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    data = _NormalizingBoolData()
    store = PythonBoolAttributeStore(data, "visible")
    view_model = BoolViewModel(parent=owner)
    view_model.attach_store(store)
    view = MayaBoolPlugView(view_model, node.visibility, owner)
    errors: list[object] = []
    view.sync_failed.connect(errors.append)
    try:
        maya_cmds.setAttr(f"{node_name}.visibility", True)
        _process_events()

        # Storeをrollbackせず、Maya側の不一致を明示状態として残す。
        assert data.visible is False
        assert view_model.value.value is False
        assert not view.is_synchronized
        assert isinstance(view.last_sync_error, RuntimeError)
        assert errors
        assert maya_cmds.getAttr(f"{node_name}.visibility")

        assert view.sync_from_view_model()
        assert not maya_cmds.getAttr(f"{node_name}.visibility")
        assert view.is_synchronized
        assert view.last_sync_error is None
    finally:
        view.dispose()


@pytest.mark.parametrize("update_before_error", [False, True])
def test_store_write_error_from_maya_input_is_contained(
    new_scene,
    maya_cmds,
    update_before_error: bool,
) -> None:
    # Maya callback境界からStore例外を漏らさず、Storeの確定値を維持する。
    node_name = maya_cmds.createNode("transform", name="failingStoreView")
    plug_name = f"{node_name}.visibility"
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    store = _FailingBoolStore(update_before_error=update_before_error)
    view_model = BoolViewModel(parent=owner)
    view_model.attach_store(store)
    view = MayaBoolPlugView(view_model, node.visibility, owner)
    errors: list[object] = []
    view.sync_failed.connect(errors.append)
    try:
        maya_cmds.setAttr(plug_name, True)
        _process_events()

        assert view.last_sync_error is store.error
        assert errors[-1] is store.error
        assert not view.is_synchronized
        assert store.value is update_before_error
        assert view_model.value.value is update_before_error
        assert maya_cmds.getAttr(plug_name)

        changed = view.sync_from_view_model()
        assert changed is (not update_before_error)
        assert maya_cmds.getAttr(plug_name) is update_before_error
        assert view.is_synchronized
        assert view.last_sync_error is None
    finally:
        view.dispose()


def test_view_disposal_and_node_removal_do_not_disable_store_command(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # Viewの終了は正本であるPython Storeの利用可否と無関係。
    bool_plug_view.view.dispose()
    assert bool_plug_view.view.is_disposed
    assert bool_plug_view.view_model.set_value_command.can_execute
    assert bool_plug_view.view_model.set_value_command.execute(True)
    assert bool_plug_view.data.visible is True

    # node削除後も同じStoreとCommandを継続利用できる。
    second_name = maya_cmds.createNode("transform", name="removedView")
    second_node = Nodes().existing.transform(second_name)
    second_view = MayaBoolPlugView(
        bool_plug_view.view_model,
        second_node.visibility,
        bool_plug_view.owner,
    )
    maya_cmds.delete(second_name)
    assert second_view.is_disposed
    assert not second_view.is_available
    assert bool_plug_view.view_model.set_value_command.can_execute
    assert bool_plug_view.view_model.set_value_command.execute(False)
    assert bool_plug_view.data.visible is False
    second_view.dispose()


def test_dispose_cancels_queued_maya_input(
    bool_plug_view: _ViewContext,
    maya_cmds,
) -> None:
    # callbackを予約済みでもdispose後はStoreへ入力しない。
    maya_cmds.setAttr(
        f"{bool_plug_view.node_name}.visibility",
        True,
    )
    assert not bool_plug_view.view.is_synchronized
    bool_plug_view.view.dispose()
    _process_events()

    assert bool_plug_view.data.visible is False
    assert bool_plug_view.view_model.set_value_command.can_execute


def test_owner_destruction_disposes_view_but_keeps_store_usable(
    new_scene,
    maya_cmds,
) -> None:
    # View ownerと正本のlifecycleを分離する。
    node_name = maya_cmds.createNode("transform", name="viewOwnerLifetime")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()
    data = _BoolData(False)
    view_model = BoolViewModel()
    view_model.attach_store(PythonBoolAttributeStore(data, "visible"))
    view = MayaBoolPlugView(view_model, node.visibility, owner)

    owner.deleteLater()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        owner,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    _process_events()

    assert view.is_disposed
    assert view_model.set_value_command.can_execute
    assert view_model.set_value_command.execute(True)
    assert data.visible is True


def test_view_keeps_temporary_view_model_alive(
    new_scene,
    maya_cmds,
) -> None:
    # factoryがViewだけを返してもVMとPython Storeを存続させる。
    node_name = maya_cmds.createNode("transform", name="temporaryViewModel")
    node = Nodes().existing.transform(node_name)
    owner = qt.QObject()

    def create_view() -> tuple[MayaBoolPlugView, _BoolData]:
        data = _BoolData(False)
        view_model = BoolViewModel()
        view_model.attach_store(PythonBoolAttributeStore(data, "visible"))
        return MayaBoolPlugView(view_model, node.visibility, owner), data

    view, data = create_view()
    gc.collect()
    try:
        assert not view.is_disposed
        assert view.view_model.set_value_command.execute(True)
        assert data.visible is True
        assert maya_cmds.getAttr(f"{node_name}.visibility")
    finally:
        view.dispose()


def test_view_model_accepts_only_one_maya_bool_plug_view(
    bool_plug_view: _ViewContext,
) -> None:
    # 複数plugへの個別setAttrがundo履歴を壊さないようv1では1つに限定する。
    with pytest.raises(RuntimeError, match="複数のMayaBoolPlugView"):
        MayaBoolPlugView(
            bool_plug_view.view_model,
            bool_plug_view.view.plug_operator,
            bool_plug_view.owner,
        )

    # 既存Viewを明示破棄した後は新しいViewへ交換できる。
    bool_plug_view.view.dispose()
    replacement = MayaBoolPlugView(
        bool_plug_view.view_model,
        bool_plug_view.view.plug_operator,
        bool_plug_view.owner,
    )
    replacement.dispose()
