# coding: utf-8
"""表示生成を省く検証でも、現在の入力条件と途中失敗の復旧を維持する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import MayaFloatPlugsBinding, resolve_float_plug
from bd_util.maya.ui.binding import _plugs_store


@pytest.mark.parametrize("track_input_state", [False, True])
@pytest.mark.parametrize("locked_target", ["secondary", "parent", "reference"])
def test_prepared_write_rechecks_current_locks(
    new_scene, track_input_state, locked_target
):
    """準備後の自身・祖先・代表のlockを拒否し、全対象を未変更で保つ。"""
    nodes = [cmds.createNode("transform") for _ in range(2)]
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "tx") for node in nodes],
        monitor=False,
        monitor_lifetime=True,
        track_input_state=track_input_state,
    )
    locked = {
        "secondary": nodes[1] + ".tx",
        "parent": nodes[1] + ".translate",
        "reference": nodes[0] + ".tx",
    }[locked_target]
    try:
        plan = binding.store.prepare_write(2.0)
        cmds.setAttr(locked, lock=True)
        with pytest.raises(RuntimeError):
            binding.store._execute_write(plan)
        assert [cmds.getAttr(node + ".tx") for node in nodes] == [0, 0]
    finally:
        cmds.setAttr(locked, lock=False)
        binding.dispose()
        binding.deleteLater()


@pytest.mark.parametrize("change", ["lock", "connection", "range"])
def test_unmonitored_write_rechecks_later_target_and_restores(
    new_scene, monkeypatch, change
):
    """先行書込みによる後続の制約変更を検出し、適用済みの値を復旧する。"""
    nodes = [cmds.createNode("transform") for _ in range(2)]
    source = cmds.createNode("transform")
    for node in nodes:
        cmds.addAttr(
            node,
            longName="value",
            attributeType="double",
            minValue=0,
            maxValue=10,
        )
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "value") for node in nodes],
        monitor=False,
        monitor_lifetime=True,
        edit_connected=True,
    )
    original = cmds.setAttr
    first = cmds.ls(nodes[0], long=True)[0] + ".value"
    changed = []

    def write(name, *args, **kwargs):
        """最初の書込み後に一度だけ後続対象の入力条件を変える。"""
        original(name, *args, **kwargs)
        if name != first or changed:
            return
        changed.append(True)
        if change == "lock":
            original(nodes[1] + ".value", lock=True)
        elif change == "connection":
            cmds.connectAttr(source + ".tx", nodes[1] + ".value")
        else:
            cmds.addAttr(nodes[1] + ".value", edit=True, maxValue=1)

    monkeypatch.setattr(cmds, "setAttr", write)
    try:
        with pytest.raises((RuntimeError, ValueError)):
            binding.set_value(2.0)
        assert changed
        assert [cmds.getAttr(node + ".value") for node in nodes] == [0, 0]
        assert binding.value == 0
    finally:
        monkeypatch.setattr(cmds, "setAttr", original)
        if change == "lock":
            original(nodes[1] + ".value", lock=False)
        binding.dispose()
        binding.deleteLater()


def test_unconnected_validation_does_not_generate_display_names(
    new_scene, monkeypatch
):
    """表示用の名前生成を省き、同じ対象への再検証でも最新のlockを確認する。"""
    node = cmds.createNode("transform")
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "tx")], monitor=False
    )
    target = binding.store._targets[0]

    def unexpected_name(self):
        """検証だけで表示用の完全名を作る回帰を検出する。"""
        raise AssertionError("書込み可否の検証で表示名を生成しています")

    try:
        with monkeypatch.context() as patch:
            patch.setattr(_plugs_store.PlugTarget, "name", unexpected_name)
            _plugs_store.validate_plug_write_target(target, target)
            cmds.setAttr(node + ".translate", lock=True)
            with pytest.raises(RuntimeError):
                _plugs_store.validate_plug_write_target(target, target)
    finally:
        cmds.setAttr(node + ".translate", lock=False)
        binding.dispose()
        binding.deleteLater()
