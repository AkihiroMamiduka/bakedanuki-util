# coding: utf-8
"""接続済み属性の標準入力と、キー・一時値の失敗復旧を検証する。"""

from dataclasses import asdict

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui.binding._connected_plug_write import (
    inspect_connected_plug,
    prepare_connected_plug_write,
)


@pytest.fixture(autouse=True)
def scene(new_scene):
    """時刻・単位・Undo・Auto Keyを各試験で独立させる。"""
    auto = cmds.autoKeyframe(query=True, state=True)
    undo = cmds.undoInfo(query=True, state=True)
    cmds.autoKeyframe(state=False)
    cmds.undoInfo(state=True)
    cmds.currentUnit(angle="deg", linear="cm", time="film")
    yield
    cmds.autoKeyframe(state=auto)
    cmds.undoInfo(state=undo)


def target(kind, attribute="tx", keyed_layer=True):
    """時間・SDK・レイヤーの代表的な接続を生成する。"""
    node = cmds.createNode("transform")
    if attribute == "mode":
        cmds.addAttr(
            node,
            longName="mode",
            attributeType="enum",
            enumName="A:B:C",
            keyable=True,
        )
    path = node + "." + attribute
    driver = cmds.createNode("transform")
    discrete = attribute in ("v", "mode")
    if kind == "driven":
        for value in (0, 1 if discrete else 10):
            cmds.setAttr(driver + ".tx", value)
            cmds.setAttr(path, value)
            cmds.setDrivenKeyframe(path, currentDriver=driver + ".tx")
        cmds.setAttr(driver + ".tx", 0 if discrete else 3)
    else:
        for time, value in ((1, 0), (9, 1 if discrete else 8)):
            cmds.setKeyframe(path, time=time, value=value)
        if kind == "layer":
            layer = cmds.animLayer("editLayer", attribute=path)
            cmds.animLayer(layer, edit=True, selected=True, preferred=True)
            if keyed_layer:
                for time, value in ((1, 0), (9, 1 if discrete else 12)):
                    cmds.setKeyframe(
                        path, time=time, value=value, animLayer=layer
                    )
    cmds.currentTime(5)
    return om.MSelectionList().add(path).getPlug(0), driver


def keys(info):
    """対象経路のキー時刻と値を比較可能な形で読む。"""
    return tuple(
        (
            cmds.keyframe(
                om.MFnDependencyNode(node).name(), query=True, timeChange=True
            ),
            cmds.keyframe(
                om.MFnDependencyNode(node).name(), query=True, floatChange=True
            ),
            cmds.keyframe(
                om.MFnDependencyNode(node).name(), query=True, valueChange=True
            ),
        )
        for node in info.curves
    )


@pytest.mark.parametrize("kind", ["time", "driven", "layer"])
@pytest.mark.parametrize("auto", [False, True])
@pytest.mark.parametrize("attribute", ["tx", "rx", "sx", "v", "mode"])
def test_native_edit_restore_and_persistence(kind, auto, attribute):
    """Auto Key・SDK・型の違いに応じた標準入力と復旧を保証する。"""
    plug, driver = target(kind, attribute)
    info = inspect_connected_plug(plug)
    assert info.mode == kind
    before = cmds.getAttr(plug.name())
    before_keys = keys(info)
    cmds.autoKeyframe(state=auto)
    requested = 1 if attribute in ("v", "mode") else 42
    write = prepare_connected_plug_write(plug, requested)
    write.apply()
    assert cmds.getAttr(plug.name()) == pytest.approx(requested)
    if kind == "driven" or not auto:
        assert keys(info) == before_keys
    write.restore()
    assert cmds.autoKeyframe(query=True, state=True) == auto
    assert cmds.getAttr(plug.name()) == pytest.approx(before)
    assert keys(info) == before_keys
    cmds.currentTime(6)
    cmds.currentTime(5)
    if kind == "driven":
        cmds.setAttr(driver + ".tx", 4)
    assert keys(info) == before_keys


@pytest.mark.parametrize("auto", [False, True])
@pytest.mark.parametrize("undo", [False, True])
@pytest.mark.parametrize("keyed", [False, True])
def test_layer_static_input_and_temporary_value_restore(auto, undo, keyed):
    """カーブ未作成のレイヤー入力もUndo設定によらず元へ戻す。"""
    plug, _ = target("layer", keyed_layer=keyed)
    first = prepare_connected_plug_write(plug, 17)
    first.apply()
    cmds.autoKeyframe(state=auto)
    cmds.undoInfo(state=undo)
    write = prepare_connected_plug_write(plug, 42)
    original_nodes = cmds.ls(type="animCurve")
    write.apply()
    write.restore()
    assert cmds.getAttr(plug.name()) == pytest.approx(17)
    assert cmds.ls(type="animCurve") == original_nodes


@pytest.mark.parametrize(
    "change",
    ["time", "units", "auto", "key", "value", "lock", "connection", "layer"],
)
def test_prepared_input_rejects_context_changes(change):
    """事前検証後の関連状態変更には一切書き込まない。"""
    plug, _ = target("layer")
    write = prepare_connected_plug_write(plug, 42)
    if change == "time":
        cmds.currentTime(6)
    elif change == "units":
        cmds.currentUnit(linear="m")
    elif change == "auto":
        cmds.autoKeyframe(state=True)
    elif change == "key":
        cmds.setKeyframe(plug.name(), time=1, value=50)
    elif change == "value":
        cmds.setAttr(plug.name(), 50)
    elif change == "lock":
        cmds.setAttr(plug.name(), lock=True)
    elif change == "connection":
        other = cmds.createNode("transform")
        cmds.connectAttr(other + ".tx", plug.name(), force=True)
    else:
        cmds.animLayer("editLayer", edit=True, lock=True)
    with pytest.raises(RuntimeError):
        write.apply()


@pytest.mark.parametrize(
    "kind",
    [
        "constraint",
        "pairBlend",
        "unitConversion",
        "mute",
        "expression",
        "direct",
        "fake_layer",
        "shared",
        "timewarp",
    ],
)
def test_unsupported_paths_remain_read_only(kind):
    """初回対応外の演算・合成・拘束経路を値入力へ含めない。"""
    plug, driver = target("time")
    if kind == "constraint":
        cmds.pointConstraint(driver, om.MFnDependencyNode(plug.node()).name())
    elif kind == "mute":
        cmds.mute(plug.name())
    elif kind == "shared":
        cmds.connectAttr(plug.sourceWithConversion().name(), driver + ".tx")
    elif kind == "timewarp":
        cmds.setAttr("time1.enableTimewarp", True)
    elif kind == "expression":
        cmds.delete(
            om.MFnDependencyNode(plug.sourceWithConversion().node()).name()
        )
        cmds.expression(string=plug.name() + " = " + driver + ".translateX;")
    elif kind == "direct":
        cmds.connectAttr(driver + ".tx", plug.name(), force=True)
    else:
        node_type = "animBlendNodeAdditiveDL" if kind == "fake_layer" else kind
        node = cmds.createNode(node_type)
        output = ".outTranslateX" if kind == "pairBlend" else ".output"
        cmds.connectAttr(node + output, plug.name(), force=True)
    with pytest.raises(RuntimeError):
        inspect_connected_plug(plug)


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("existing", [False, True])
def test_restore_keeps_tangents_and_breakdown(weighted, existing):
    """Auto Keyによる既存・新規キー編集の接線情報を失敗時に戻す。"""
    plug, _ = target("time")
    curve = om.MFnDependencyNode(plug.sourceWithConversion().node()).name()
    cmds.keyTangent(curve, edit=True, weightedTangents=weighted)
    cmds.keyTangent(curve, edit=True, lock=False)
    cmds.keyTangent(curve, edit=True, inAngle=12, outAngle=-25)
    if weighted:
        cmds.keyTangent(curve, edit=True, weightLock=False)
        cmds.keyTangent(curve, edit=True, inWeight=0.8, outWeight=1.5)
        cmds.keyTangent(curve, edit=True, weightLock=True)
    cmds.keyframe(curve, edit=True, breakdown=True)
    cmds.currentTime(1 if existing else 5)
    cmds.autoKeyframe(state=True)
    write = prepare_connected_plug_write(plug, 42)
    write.apply()
    write.restore()
    for state in write.curves:
        actual = state.capture(state.handle.object())
        assert len(state.keys) == len(actual.keys)
        for before, after in zip(state.keys, actual.keys):
            assert asdict(after) == pytest.approx(asdict(before))


@pytest.mark.parametrize("kind", ["time", "driven", "layer"])
@pytest.mark.parametrize("auto", [False, True])
def test_native_undo_redo_and_failed_chunk_history(kind, auto):
    """成功と失敗の値入力が通常Undo chunkの履歴を壊さない。"""
    plug, _ = target(kind)
    cmds.autoKeyframe(state=auto)
    info = inspect_connected_plug(plug)
    before = cmds.getAttr(plug.name())
    before_keys = keys(info)
    cmds.flushUndo()
    cmds.undoInfo(openChunk=True, chunkName="ConnectedPlugInput")
    write = prepare_connected_plug_write(plug, 42)
    write.apply()
    cmds.undoInfo(closeChunk=True)
    after_keys = keys(info)
    cmds.undo()
    assert cmds.getAttr(plug.name()) == pytest.approx(before)
    assert keys(info) == before_keys
    cmds.redo()
    assert cmds.getAttr(plug.name()) == pytest.approx(42)
    assert keys(info) == after_keys
    cmds.undo()
    cmds.flushUndo()
    cmds.undoInfo(openChunk=True, chunkName="ConnectedPlugFailedInput")
    write = prepare_connected_plug_write(plug, 42)
    write.apply()
    write.restore()
    cmds.undoInfo(closeChunk=True)
    cmds.undo()
    assert keys(info) == before_keys
    assert cmds.getAttr(plug.name()) == pytest.approx(before)
    cmds.redo()
    assert keys(info) == before_keys
    assert cmds.getAttr(plug.name()) == pytest.approx(before)


@pytest.mark.parametrize(
    "state", ["locked", "all_locked", "zero", "muted", "override"]
)
@pytest.mark.parametrize("auto", [False, True])
def test_layer_standard_target_and_output_states(state, auto):
    """レイヤーのlock fallbackや出力抑制をMaya標準へ委ねて復旧する。"""
    plug, _ = target("layer")
    if state in ("locked", "all_locked"):
        cmds.animLayer("editLayer", edit=True, lock=True)
    if state == "all_locked":
        cmds.animLayer("BaseAnimation", edit=True, lock=True)
    elif state == "zero":
        cmds.setAttr("editLayer.weight", 0)
    elif state == "muted":
        cmds.animLayer("editLayer", edit=True, mute=True)
    elif state == "override":
        cmds.animLayer("editLayer", edit=True, override=True)
    cmds.autoKeyframe(state=auto)
    write = prepare_connected_plug_write(plug, 42)
    before = cmds.getAttr(plug.name())
    write.apply()
    write.restore()
    assert cmds.getAttr(plug.name()) == pytest.approx(before)
    assert all(item.matches() for item in write.curves)


def test_whole_rotation_layer_supports_each_axis():
    """三軸まとめてレイヤー登録した回転も軸単位で入力できる。"""
    node = cmds.createNode("transform")
    cmds.setKeyframe(node + ".rotate", time=1, value=0)
    layer = cmds.animLayer("rotationLayer", attribute=node + ".rotate")
    cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    cmds.setKeyframe(node + ".rotate", time=1, value=10, animLayer=layer)
    for axis in "XYZ":
        plug = om.MSelectionList().add(node + ".rotate" + axis).getPlug(0)
        write = prepare_connected_plug_write(plug, 42)
        write.apply()
        assert cmds.getAttr(plug.name()) == pytest.approx(42)
        write.restore()


@pytest.mark.parametrize(
    "selected", ["BaseAnimation", "keyedLayer", "emptyLayer"]
)
def test_layer_missing_curve_restores_original_topology(selected):
    """キーのない対象レイヤーへの入力でも元の接続と実入力を復旧する。"""
    node = cmds.createNode("transform")
    path = node + ".tx"
    cmds.setAttr(path, 3)
    layer = cmds.animLayer("keyedLayer", attribute=path)
    cmds.setKeyframe(path, time=1, value=5, animLayer=layer)
    cmds.animLayer("emptyLayer", attribute=path)
    for name in ("BaseAnimation", "keyedLayer", "emptyLayer"):
        cmds.animLayer(
            name,
            edit=True,
            selected=name == selected,
            preferred=name == selected,
        )
    cmds.currentTime(5)
    cmds.autoKeyframe(state=True)
    plug = om.MSelectionList().add(path).getPlug(0)
    write = prepare_connected_plug_write(plug, 42)
    names = cmds.ls(type="animCurve")
    before = cmds.getAttr(path)
    write.apply()
    write.restore()
    assert cmds.ls(type="animCurve") == names
    assert cmds.getAttr(path) == pytest.approx(before)
    assert all(state.matches() for state in write.curves)
