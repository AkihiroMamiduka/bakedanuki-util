# coding: utf-8
"""接続属性への貼り付けとMaya標準Auto Keyの契約を検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaNodeValueSnapshot,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
    apply_scalar_value_transfer_to_paths,
    apply_scalar_value_to_paths,
)


@pytest.fixture
def scene(new_scene):
    """Auto KeyとUndoを固定し、各検証後に利用前の設定へ戻す。"""
    auto_key = cmds.autoKeyframe(query=True, state=True)
    undo_enabled = cmds.undoInfo(query=True, state=True)
    linear_unit = cmds.currentUnit(query=True, linear=True)
    cmds.autoKeyframe(state=False)
    cmds.undoInfo(state=True)
    cmds.currentUnit(linear="cm")
    yield
    cmds.autoKeyframe(state=auto_key)
    cmds.undoInfo(state=undo_enabled)
    cmds.currentUnit(linear=linear_unit)


def _node(name):
    """単位変換のない公開数値属性を持つtransformを作る。"""
    node = cmds.createNode("transform", name=name)
    cmds.addAttr(node, longName="amount", attributeType="double", keyable=True)
    return node


def _animate(plug, *, layer=None):
    """開始と終了にキーを作り、現在時刻にはキーがない状態にする。"""
    options = {"animLayer": layer} if layer else {}
    for time, value in ((1, 2.0), (10, 8.0)):
        cmds.setKeyframe(plug, time=time, value=value, **options)
    if layer:
        return cmds.animLayer(layer, query=True, findCurveForPlug=plug)
    return cmds.listConnections(plug, source=True, destination=False)[0]


def _transfer(path="amount", kind="number", value=42.0):
    """貼り付け先の接続状態に依存しない単一値の搬送データを作る。"""
    return MayaScalarValueTransfer(
        (MayaNodeValueSnapshot((MayaScalarValueSnapshot(path, kind, value),)),)
    )


def _paste(api, nodes, transfer, paths=("amount",), **options):
    """三つの公開貼り付けAPIを同じ検証条件で呼び出す。"""
    if api == "same_paths":
        return apply_scalar_value_transfer(nodes, transfer, **options)
    if api == "selected_paths":
        return apply_scalar_value_transfer_to_paths(
            nodes, paths, transfer, **options
        )
    return apply_scalar_value_to_paths(nodes, paths, transfer, **options)


@pytest.mark.parametrize("api", ["same_paths", "selected_paths", "one_value"])
@pytest.mark.parametrize("auto_key", [False, True])
def test_paste_shares_native_edit_and_undo_across_connection_kinds(
    scene, api, auto_key
):
    """通常値・時間キー・SDK・Layerをまとめて入力し、一回でUndoする。"""
    static, animated, driven, layered = (
        _node(name) for name in ("static", "animated", "driven", "layered")
    )
    driver = cmds.createNode("transform", name="driver")
    animated_curve = _animate(animated + ".amount")
    for driver_value, value in ((0, 2), (10, 8)):
        cmds.setDrivenKeyframe(
            driven + ".amount",
            currentDriver=driver + ".tx",
            driverValue=driver_value,
            value=value,
        )
    driven_curve = cmds.listConnections(
        driven + ".amount", source=True, destination=False
    )[0]
    layer = cmds.animLayer("pasteLayer", attribute=layered + ".amount")
    layer_curve = _animate(layered + ".amount", layer=layer)
    cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    cmds.currentTime(5)
    nodes = (static, animated, driven, layered)
    before = [cmds.getAttr(node + ".amount") for node in nodes]
    curves = (animated_curve, driven_curve, layer_curve)
    curve_values = [
        cmds.keyframe(curve, query=True, valueChange=True) for curve in curves
    ]
    cmds.autoKeyframe(state=auto_key)
    cmds.flushUndo()

    result = _paste(api, nodes, _transfer(), edit_connected=True)

    assert result.changed
    assert result.eligible_count == 4
    assert result.excluded == ()
    assert [cmds.getAttr(node + ".amount") for node in nodes] == [42] * 4
    assert not cmds.listConnections(
        static + ".amount", source=True, destination=False
    )
    assert cmds.keyframe(driven_curve, query=True, valueChange=True) == (
        curve_values[1]
    )
    for curve in (animated_curve, layer_curve):
        assert cmds.keyframe(curve, query=True, keyframeCount=True) == (
            3 if auto_key else 2
        )
        assert cmds.keyframe(
            curve, query=True, time=(5, 5), valueChange=True
        ) == ([42.0] if auto_key else None)

    cmds.undo()
    assert [cmds.getAttr(node + ".amount") for node in nodes] == pytest.approx(
        before
    )
    assert [
        cmds.keyframe(curve, query=True, valueChange=True) for curve in curves
    ] == curve_values
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize("api", ["same_paths", "selected_paths", "one_value"])
def test_paste_excludes_constraint_and_unsupported_inputs(scene, api):
    """constraint・一般接続・変換接続を維持し、通常値だけ貼り付ける。"""
    nodes = [cmds.createNode("transform") for _ in range(5)]
    driver, static, constrained, connected, converted = nodes
    cmds.pointConstraint(driver, constrained)
    cmds.connectAttr(driver + ".tx", connected + ".tx")
    conversion = cmds.createNode("unitConversion")
    cmds.connectAttr(driver + ".tx", conversion + ".input")
    cmds.connectAttr(conversion + ".output", converted + ".tx")
    targets = (static, constrained, connected, converted)
    sources = {
        node: cmds.connectionInfo(node + ".tx", sourceFromDestination=True)
        for node in targets[1:]
    }
    cmds.flushUndo()

    result = _paste(
        api,
        targets,
        _transfer("translate.translateX", "distance"),
        paths=("translate.translateX",),
        edit_connected=True,
    )

    assert result.changed
    assert result.eligible_count == 1
    assert len(result.excluded) == 3
    assert cmds.getAttr(static + ".tx") == 42
    for node, source in sources.items():
        assert any(node in exclusion for exclusion in result.excluded)
        assert cmds.getAttr(node + ".tx") == 0
        assert (
            cmds.connectionInfo(node + ".tx", sourceFromDestination=True)
            == source
        )
    cmds.undo()
    assert cmds.getAttr(static + ".tx") == 0
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize("api", ["same_paths", "selected_paths", "one_value"])
@pytest.mark.parametrize("paths", [("caption",), (), ("absent",)])
def test_conflicting_policies_raise_before_string_or_empty_path_paste(
    scene, api, paths
):
    """数値Bindingを作らない経路でも入力方針の矛盾を明示拒否する。"""
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="caption", dataType="string")
    cmds.setAttr(node + ".caption", "before", type="string")
    cmds.flushUndo()

    with pytest.raises(ValueError, match="key_animated.*edit_connected"):
        _paste(
            api,
            (node,),
            _transfer("caption", "string", "after"),
            paths=paths,
            key_animated=True,
            edit_connected=True,
        )

    assert cmds.getAttr(node + ".caption") == "before"
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
