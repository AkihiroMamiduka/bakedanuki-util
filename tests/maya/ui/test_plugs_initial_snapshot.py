# coding: utf-8
"""Maya属性群の初回同期だけで読取りを再利用する境界を検証する。"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Literal, cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
    MayaIntPlugsBinding,
    MayaStringPlugsBinding,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
    resolve_int_plug,
    resolve_string_plug,
)
from bd_util.maya.ui.binding import plugs_binding
from bd_util.maya.ui.binding._int_plug_value import IntPlugValue
from bd_util.maya.ui.binding._plugs_store import PlugTarget
from bd_util.maya.ui.binding.plugs_state import MayaPlugTargetState
from bd_util.ui import FloatViewModel, qt

Kind = Literal["float", "int", "bool", "enum", "string"]
Binding = (
    MayaFloatPlugsBinding
    | MayaIntPlugsBinding
    | MayaBoolPlugsBinding
    | MayaEnumPlugsBinding
    | MayaStringPlugsBinding
)


def _flush() -> None:
    """予約同期とQtの遅延破棄を処理する。"""
    for _ in range(3):
        qt.QApplication.processEvents()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


@pytest.fixture
def scene(new_scene: None) -> Iterator[tuple[list[str], qt.QObject]]:
    """独立した二対象と、確実に破棄するBinding所有者を用意する。"""
    del new_scene
    nodes = [cmds.createNode("transform") for _ in range(2)]
    owner = qt.QObject()
    yield nodes, owner
    if qt.isValid(owner):
        owner.deleteLater()
    _flush()


def _add_values(nodes: list[str], kind: Kind) -> None:
    """状態比較しやすい同名のscalar属性を作る。"""
    for node in nodes:
        if kind == "string":
            cmds.addAttr(node, longName="sample", dataType="string")
        elif kind == "enum":
            cmds.addAttr(
                node,
                longName="sample",
                attributeType="enum",
                enumName="First:Second:Third",
            )
        else:
            cmds.addAttr(
                node,
                longName="sample",
                attributeType={
                    "float": "double",
                    "int": "long",
                    "bool": "bool",
                }[kind],
            )


def _binding(
    nodes: list[str], owner: qt.QObject, kind: Kind, *, monitor: bool = True
) -> Binding:
    """属性種別に合う公開Bindingを作る。"""
    if kind == "float":
        return MayaFloatPlugsBinding(
            [resolve_float_plug(node, "sample") for node in nodes],
            parent=owner,
            monitor=monitor,
        )
    if kind == "int":
        return MayaIntPlugsBinding(
            [resolve_int_plug(node, "sample") for node in nodes],
            parent=owner,
            monitor=monitor,
        )
    if kind == "bool":
        return MayaBoolPlugsBinding(
            [resolve_bool_plug(node, "sample") for node in nodes],
            parent=owner,
            monitor=monitor,
        )
    if kind == "enum":
        return MayaEnumPlugsBinding(
            [resolve_enum_plug(node, "sample") for node in nodes],
            parent=owner,
            monitor=monitor,
        )
    return MayaStringPlugsBinding(
        [resolve_string_plug(node, "sample") for node in nodes],
        parent=owner,
        monitor=monitor,
    )


def _record_reads(
    kind: Kind, monkeypatch: pytest.MonkeyPatch
) -> tuple[list[bool], list[bool]]:
    """内部codecと状態解析の呼出しだけを数え、実処理を維持する。"""
    codec_type = (
        IntPlugValue
        if kind == "int"
        else getattr(plugs_binding, f"_{kind.capitalize()}Codec")
    )
    original = cast(Callable[[object], object], getattr(codec_type, "read"))
    state = PlugTarget[float].state
    reads: list[bool] = []
    states: list[bool] = []

    def read(codec: object) -> object:
        """正本への追加読取りを記録する。"""
        reads.append(True)
        return original(codec)

    def read_state(target: PlugTarget[float]) -> MayaPlugTargetState:
        """Maya状態への追加解析を記録する。"""
        states.append(True)
        return state(target)

    monkeypatch.setattr(codec_type, "read", read)
    monkeypatch.setattr(PlugTarget, "state", read_state)
    return reads, states


@pytest.mark.parametrize("kind", ["float", "int", "bool", "enum", "string"])
def test_initial_snapshot_is_consumed_once_and_refresh_stays_live(
    scene: tuple[list[str], qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    kind: Kind,
) -> None:
    """初回の一組だけを再利用し、通常refreshは再読取りする。"""
    nodes, owner = scene
    _add_values(nodes, kind)
    reads, states = _record_reads(kind, monkeypatch)
    binding = _binding(nodes, owner, kind)
    # intの初期範囲通知後だけは正本を再確認する
    expected = 3 if kind == "int" else 2
    assert len(reads) == expected
    assert len(states) == expected
    assert not binding.is_mixed
    assert all(state.is_available for state in binding.target_states)
    reads.clear()
    states.clear()
    binding.refresh()
    assert len(reads) >= 3
    assert len(states) >= 3
    take = cast(
        Callable[[], object], getattr(binding.store, "_take_initial_snapshot")
    )
    assert take() is None


def test_unmonitored_store_keeps_initial_live_reads(
    scene: tuple[list[str], qt.QObject], monkeypatch: pytest.MonkeyPatch
) -> None:
    """監視なしの一時Storeでは通常の初期再検証を省略しない。"""
    nodes, owner = scene
    _add_values(nodes, "float")
    reads, states = _record_reads("float", monkeypatch)
    binding = _binding(nodes, owner, "float", monitor=False)
    assert len(reads) == 3
    assert len(states) == 3
    assert binding.value == 0.0


@pytest.mark.parametrize("change", ["value", "lock", "delete"])
def test_later_target_evaluation_invalidates_entire_initial_state(
    scene: tuple[list[str], qt.QObject],
    monkeypatch: pytest.MonkeyPatch,
    change: Literal["value", "lock", "delete"],
) -> None:
    """後続の評価が先行対象を変えた場合は、混在と状態も全対象で読み直す。"""
    nodes, owner = scene
    _add_values(nodes, "float")
    original = cast(
        Callable[[object], float],
        getattr(plugs_binding, "_FloatCodec").read,
    )
    count = 0

    def read(codec: object) -> float:
        """二対象目の評価から、一対象目の値または実体を変更する。"""
        nonlocal count
        count += 1
        value = original(codec)
        if count == 2:
            if change == "value":
                cast(Callable[[str, float], None], cmds.setAttr)(
                    nodes[0] + ".sample", 8.0
                )
            elif change == "lock":
                cmds.setAttr(nodes[0] + ".sample", lock=True)
            else:
                cmds.deleteAttr(nodes[0] + ".sample")
        return value

    monkeypatch.setattr(getattr(plugs_binding, "_FloatCodec"), "read", read)
    binding = _binding(nodes, owner, "float")
    assert count > 2
    if change == "value":
        assert binding.value == 8.0
        assert binding.is_mixed
        assert binding.target_states[0].is_writable
    elif change == "lock":
        assert not binding.target_states[0].is_writable
        assert binding.target_states[0].is_locked
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.is_mixed
    else:
        assert not binding.target_states[0].is_available
        assert not binding.view_model.set_value_command.can_execute
        cmds.undo()
        _flush()
        assert not binding.target_states[0].is_available


@pytest.mark.parametrize("change", ["value", "delete", "dispose"])
def test_float_initial_presentation_signal_rechecks_live_source(
    scene: tuple[list[str], qt.QObject],
    change: Literal["value", "delete", "dispose"],
) -> None:
    """初期表示の通知先が正本を変えた後へsnapshot値を持ち越さない。"""
    nodes, owner = scene
    _add_values(nodes, "float")
    for node in nodes:
        cmds.addAttr(node + ".sample", edit=True, minValue=0.0)
    models: list[FloatViewModel] = []

    class BindingWithObserver(MayaFloatPlugsBinding):
        """Viewの接続前から表示通知を受ける利用者を再現する。"""

        def _create_view_model(self) -> FloatViewModel:
            """初期接続中の外部slotを登録する。"""
            view_model = super()._create_view_model()
            models.append(view_model)

            def changed(_presentation: object) -> None:
                """表示情報の通知中に正本かViewModelの寿命を変更する。"""
                if change == "value":
                    cast(Callable[[str, float], None], cmds.setAttr)(
                        nodes[0] + ".sample", 6.0
                    )
                elif change == "delete":
                    cmds.deleteAttr(nodes[0] + ".sample")
                else:
                    view_model.dispose()

            view_model.presentation_changed.connect(changed)
            return view_model

    binding = BindingWithObserver(
        [resolve_float_plug(node, "sample") for node in nodes], parent=owner
    )
    if change == "value":
        assert binding.value == 6.0
        assert binding.is_mixed
    elif change == "delete":
        assert not binding.target_states[0].is_available
        assert not binding.view_model.set_value_command.can_execute
    else:
        assert binding.is_disposed
        assert models[0].is_disposed
        assert not models[0].set_value_command.can_execute


def test_binding_constructed_during_undo_uses_live_initialization(
    scene: tuple[list[str], qt.QObject], monkeypatch: pytest.MonkeyPatch
) -> None:
    """Undo途中に作られたBindingはsnapshotを採用せず通常接続する。"""
    nodes, owner = scene
    _add_values(nodes, "float")
    cast(Callable[[str, float], None], cmds.setAttr)(nodes[0] + ".sample", 4.0)
    bindings: list[Binding] = []
    constructing: list[bool] = []

    def changed(*_args: object) -> None:
        """Undoによる属性通知の処理中に新しいBindingを生成する。"""
        if om.MGlobal.isUndoing() and not bindings and not constructing:
            constructing.append(True)
            bindings.append(_binding(nodes, owner, "float"))

    def unexpected(_store: object) -> None:
        """Undo途中で初期snapshotを取得した場合は失敗させる。"""
        raise AssertionError("Undo途中にsnapshotを取得しました")

    monkeypatch.setattr(
        getattr(plugs_binding, "_FloatPlugsStore"),
        "_prepare_initial_snapshot",
        unexpected,
    )
    plug = resolve_float_plug(nodes[0], "sample")
    callback = om.MNodeMessage.addAttributeChangedCallback(
        plug.plug.node(), changed
    )
    try:
        cmds.undo()
    finally:
        om.MMessage.removeCallback(callback)
    _flush()
    assert len(bindings) == 1
    assert bindings[0].value == 0.0
    assert not bindings[0].is_mixed


def test_float_snapshot_keeps_existing_reentrant_confirmation_payload(
    scene: tuple[list[str], qt.QObject],
) -> None:
    """値変更通知から再入しても、各refreshが取得した値を確認通知する。"""
    nodes, owner = scene
    _add_values(nodes, "float")
    cast(Callable[[str, float], None], cmds.setAttr)(nodes[0] + ".sample", 4.0)
    confirmations: list[float] = []

    class BindingWithObserver(MayaFloatPlugsBinding):
        """初回の値通知から外部変更を起こす利用者を再現する。"""

        def _create_view_model(self) -> FloatViewModel:
            """値通知と確認通知へ構築前から接続する。"""
            view_model = super()._create_view_model()

            def changed(value: float) -> None:
                """初回値の通知だけを契機に、正本を別の値へ変える。"""
                if value == 4.0:
                    cast(Callable[[str, float], None], cmds.setAttr)(
                        nodes[0] + ".sample", 9.0
                    )

            view_model.value.changed.connect(changed)
            view_model.store_refreshed.connect(confirmations.append)
            return view_model

    binding = BindingWithObserver(
        [resolve_float_plug(node, "sample") for node in nodes], parent=owner
    )
    assert binding.value == 9.0
    assert confirmations == [9.0, 4.0]
    assert binding.is_mixed


def test_float_presentation_adapter_uses_live_initialization(
    scene: tuple[list[str], qt.QObject], monkeypatch: pytest.MonkeyPatch
) -> None:
    """任意の表示変換を持つViewModelでは初回snapshotを省略する。"""
    nodes, owner = scene
    _add_values(nodes, "float")
    reads, states = _record_reads("float", monkeypatch)

    class BindingWithAdapter(MayaFloatPlugsBinding):
        """Store以外の利用者コードを初期表示の経路へ追加する。"""

        def _create_view_model(self) -> FloatViewModel:
            """初回接続前から表示adapterを設定する。"""
            view_model = super()._create_view_model()
            view_model.set_presentation_adapter(lambda value: value)
            return view_model

    binding = BindingWithAdapter(
        [resolve_float_plug(node, "sample") for node in nodes], parent=owner
    )
    assert binding.value == 0.0
    assert len(reads) == 3
    assert len(states) == 3
