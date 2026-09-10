# coding: utf-8
from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


@pytest.fixture(autouse=True)
def restore_units(maya_cmds):
    units = {
        flag: maya_cmds.currentUnit(query=True, **{flag: True})
        for flag in ("linear", "angle", "time")
    }
    maya_cmds.currentUnit(linear="cm", angle="deg", time="film")
    yield
    maya_cmds.currentUnit(**units)


@pytest.fixture
def set_keyframe_calls(maya_cmds, monkeypatch):
    original = maya_cmds.setKeyframe
    calls = []

    def set_keyframe(*args, **kwargs):
        calls.append((args, kwargs))
        return original(*args, **kwargs)

    monkeypatch.setattr(maya_cmds, "setKeyframe", set_keyframe)
    return calls


def _keyframe(modifier, node_name, attribute="translateX"):
    node = bdu.Nodes(modifier_manager=modifier).existing(node_name)
    return getattr(node, attribute).keyframe


def _curve_state(maya_cmds, curve_name):
    return (
        maya_cmds.keyframe(curve_name, query=True, timeChange=True),
        maya_cmds.keyframe(curve_name, query=True, valueChange=True),
        maya_cmds.keyTangent(curve_name, query=True, inTangentType=True),
        maya_cmds.keyTangent(curve_name, query=True, outTangentType=True),
    )


def _source_curve(maya_cmds, plug_name):
    return maya_cmds.listConnections(
        plug_name, source=True, destination=False, type="animCurve"
    )[0]


@pytest.mark.parametrize("existing_curve", [False, True])
def test_set_routes_new_curve_to_cmds_then_uses_api_for_later_keys(
    new_scene,
    maya_cmds,
    set_keyframe_calls,
    existing_curve,
):
    name = maya_cmds.createNode("transform", name="backendTarget")
    if existing_curve:
        maya_cmds.setKeyframe(name + ".translateX", time=1, value=1)
    set_keyframe_calls.clear()
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    maya_cmds.flushUndo()

    keyframe.set(1, 1)
    keyframe.set(2, 2)
    keyframe.set(3, 2)
    assert set_keyframe_calls == []
    assert keyframe.frames() == ([1.0] if existing_curve else [])
    mod.do_it_dg()

    expected_calls = 0 if existing_curve else 1
    assert len(set_keyframe_calls) == expected_calls
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    for _ in range(3):
        assert keyframe.frames() == [1.0, 2.0]
        assert keyframe.values() == [1.0, 3.0]
        mod.undo_it()
        assert keyframe.frames() == ([1.0] if existing_curve else [])
        assert keyframe.values() == ([1.0] if existing_curve else [])
        assert len(maya_cmds.ls(type="animCurve")) == int(existing_curve)
        mod.redo_it()
        assert len(set_keyframe_calls) == expected_calls


def test_set_resolves_direct_curve_after_queued_reconnection(
    new_scene,
    maya_cmds,
    maya_om,
    set_keyframe_calls,
):
    name = maya_cmds.createNode("transform", name="reconnectedBackendTarget")
    maya_cmds.setKeyframe(name + ".translateX", time=1, value=1)
    first_curve = _source_curve(maya_cmds, name + ".translateX")
    second_curve = maya_cmds.createNode(
        "animCurveTL", name="secondBackendCurve"
    )
    maya_cmds.setKeyframe(second_curve, time=3, value=3)
    before_first = _curve_state(maya_cmds, first_curve)
    before_second = _curve_state(maya_cmds, second_curve)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    selection = maya_om.MSelectionList()
    selection.add(second_curve + ".output")
    second_output = selection.getPlug(0)
    first_output = keyframe.plug.sourceWithConversion()
    set_keyframe_calls.clear()

    keyframe.set(2, 2)
    mod.dg_mod.disconnect(first_output, keyframe.plug)
    mod.dg_mod.connect(second_output, keyframe.plug)
    keyframe.set(4, 4)
    mod.do_it_dg()
    assert set_keyframe_calls == []
    final_first = _curve_state(maya_cmds, first_curve)
    final_second = _curve_state(maya_cmds, second_curve)
    assert final_first[:2] == ([1.0, 2.0], [1.0, 2.0])
    assert final_second[:2] == ([3.0, 4.0], [3.0, 4.0])

    for _ in range(2):
        assert _source_curve(maya_cmds, keyframe.plug.name()) == second_curve
        assert _curve_state(maya_cmds, first_curve) == final_first
        assert _curve_state(maya_cmds, second_curve) == final_second
        mod.undo_it()
        assert _source_curve(maya_cmds, keyframe.plug.name()) == first_curve
        assert _curve_state(maya_cmds, first_curve) == before_first
        assert _curve_state(maya_cmds, second_curve) == before_second
        mod.redo_it()
        assert set_keyframe_calls == []


def test_set_switches_back_to_cmds_after_queued_curve_deletion(
    new_scene,
    maya_cmds,
    set_keyframe_calls,
):
    name = maya_cmds.createNode("transform", name="recreatedBackendTarget")
    maya_cmds.setKeyframe(name + ".translateX", time=1, value=1)
    first_curve = _source_curve(maya_cmds, name + ".translateX")
    first_uuid = maya_cmds.ls(first_curve, uuid=True)
    before = _curve_state(maya_cmds, first_curve)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    set_keyframe_calls.clear()

    keyframe.set(2, 2)
    keyframe.delete_anim_curve()
    keyframe.set(30, 3)
    keyframe.set(40, 4)
    mod.do_it_dg()
    assert len(set_keyframe_calls) == 1
    recreated_curve = _source_curve(maya_cmds, keyframe.plug.name())
    recreated_uuid = maya_cmds.ls(recreated_curve, uuid=True)
    assert recreated_uuid != first_uuid

    for _ in range(3):
        assert keyframe.frames() == [3.0, 4.0]
        assert keyframe.values() == [30.0, 40.0]
        assert len(maya_cmds.ls(type="animCurve")) == 1
        assert maya_cmds.ls(recreated_curve, uuid=True) == recreated_uuid
        mod.undo_it()
        assert _curve_state(maya_cmds, first_curve) == before
        assert maya_cmds.ls(first_curve, uuid=True) == first_uuid
        assert len(maya_cmds.ls(type="animCurve")) == 1
        mod.redo_it()
        assert len(set_keyframe_calls) == 1


@pytest.mark.parametrize("existing_curve", [False, True])
def test_partial_api_set_failure_restores_cmds_and_api_edits_in_the_flush(
    new_scene,
    maya_cmds,
    monkeypatch,
    set_keyframe_calls,
    existing_curve,
):
    from maya.api import OpenMayaAnim as oma

    name = maya_cmds.createNode("transform", name="failingBackendTarget")
    if existing_curve:
        maya_cmds.setKeyframe(name + ".translateX", time=1, value=10)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    previous = mod.dg_mod.createNode("network")
    mod.dg_mod.renameNode(previous, "previousBackendFlush")
    mod.do_it_dg()
    edits = []
    fail_at = 2 if existing_curve else 1

    class FailingAnimCurve(oma.MFnAnimCurve):
        def addKey(self, *args, **kwargs):
            index = super().addKey(*args, **kwargs)
            edits.append(index)
            if len(edits) == fail_at:
                raise RuntimeError("intentional failure after API key edit")
            return index

    monkeypatch.setattr(oma, "MFnAnimCurve", FailingAnimCurve)
    set_keyframe_calls.clear()
    keyframe.set(20, 2)
    keyframe.set(30, 3)
    with pytest.raises(
        RuntimeError, match="intentional failure after API key edit"
    ):
        mod.do_it_dg()

    assert len(edits) == fail_at
    assert len(set_keyframe_calls) == (0 if existing_curve else 1)
    assert keyframe.frames() == ([1.0] if existing_curve else [])
    assert keyframe.values() == ([10.0] if existing_curve else [])
    assert len(maya_cmds.ls(type="animCurve")) == int(existing_curve)
    assert maya_cmds.objExists("previousBackendFlush")
    assert mod.can_undo
    assert not mod.can_redo
    mod.do_it_dg()
    mod.undo_it()
    assert not maya_cmds.objExists("previousBackendFlush")
    mod.redo_it()
    assert maya_cmds.objExists("previousBackendFlush")
    assert len(edits) == fail_at
    assert keyframe.values() == ([10.0] if existing_curve else [])


def test_failed_cmds_fallback_restores_prior_api_edit_and_new_curve(
    new_scene,
    maya_cmds,
    set_keyframe_calls,
):
    name = maya_cmds.createNode("transform", name="fallbackFailureTarget")
    maya_cmds.setKeyframe(name + ".translateX", time=1, value=1)
    maya_cmds.setAttr(name + ".translateZ", lock=True)
    curve = _source_curve(maya_cmds, name + ".translateX")
    initial = _curve_state(maya_cmds, curve)
    mod = bdu.ModifierManager()
    x_keys = _keyframe(mod, name)
    y_keys = _keyframe(mod, name, "translateY")
    z_keys = _keyframe(mod, name, "translateZ")
    set_keyframe_calls.clear()

    x_keys.set(2, 2)
    y_keys.set(3, 3)
    z_keys.set(4, 4)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()

    assert len(set_keyframe_calls) == 2
    assert _curve_state(maya_cmds, curve) == initial
    assert not y_keys.has_anim_curve()
    assert not z_keys.has_anim_curve()
    assert maya_cmds.ls(type="animCurve") == [curve]
    assert not mod.can_undo
    assert not mod.can_redo


def test_conversion_node_uses_cmds_instead_of_treating_source_as_direct_curve(
    new_scene,
    maya_cmds,
    maya_om,
    set_keyframe_calls,
):
    def create_target(name):
        node = maya_cmds.createNode("transform", name=name)
        curve = maya_cmds.createNode("animCurveTU", name=name + "Curve")
        conversion = maya_cmds.createNode("unitConversion")
        maya_cmds.setKeyframe(curve, time=1, value=1)
        maya_cmds.connectAttr(curve + ".output", conversion + ".input")
        maya_cmds.connectAttr(conversion + ".output", node + ".scaleX")
        maya_cmds.setAttr(conversion + ".conversionFactor", 3)
        return node, curve

    expected_node, expected_curve = create_target("cmdsConversionTarget")
    node, curve = create_target("backendConversionTarget")
    maya_cmds.setKeyframe(expected_node + ".scaleX", time=2, value=12)
    expected = _curve_state(maya_cmds, expected_curve)
    before = _curve_state(maya_cmds, curve)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, node, "scaleX")
    assert keyframe.plug.source().node().hasFn(maya_om.MFn.kAnimCurve)
    assert (
        not keyframe.plug.sourceWithConversion()
        .node()
        .hasFn(maya_om.MFn.kAnimCurve)
    )
    set_keyframe_calls.clear()

    keyframe.set(12, 2)
    mod.do_it_dg()
    assert len(set_keyframe_calls) == 1
    assert _curve_state(maya_cmds, curve) == expected
    for _ in range(2):
        assert maya_cmds.getAttr(node + ".scaleX", time=2) == pytest.approx(
            maya_cmds.getAttr(expected_node + ".scaleX", time=2)
        )
        mod.undo_it()
        assert _curve_state(maya_cmds, curve) == before
        mod.redo_it()
        assert _curve_state(maya_cmds, curve) == expected
        assert len(set_keyframe_calls) == 1


def test_locked_base_layer_blocks_set_on_an_unrelated_direct_curve(
    new_scene,
    maya_cmds,
    maya_om,
    set_keyframe_calls,
):
    name = maya_cmds.createNode("transform", name="unrelatedLayerTarget")
    maya_cmds.setKeyframe(name + ".translateX", time=1, value=1)
    other = maya_cmds.createNode("transform", name="layerMember")
    layer = maya_cmds.animLayer("UnrelatedLayer")
    maya_cmds.animLayer(layer, edit=True, attribute=other + ".translateX")
    base_layer = maya_cmds.animLayer(query=True, root=True)
    maya_cmds.animLayer(base_layer, edit=True, lock=True)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    assert (
        keyframe.plug.sourceWithConversion()
        .node()
        .hasFn(maya_om.MFn.kAnimCurve)
    )
    curve = _source_curve(maya_cmds, keyframe.plug.name())
    before = _curve_state(maya_cmds, curve)
    set_keyframe_calls.clear()

    keyframe.set(12, 2)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()

    assert len(set_keyframe_calls) == 1
    assert _curve_state(maya_cmds, curve) == before
    assert not mod.can_undo
    assert not mod.can_redo


def test_animation_layer_member_fallback_matches_cmds_value_resolution(
    new_scene,
    maya_cmds,
    set_keyframe_calls,
):
    expected_node = maya_cmds.createNode("transform", name="cmdsLayerTarget")
    name = maya_cmds.createNode("transform", name="backendLayerTarget")
    for node_name in (expected_node, name):
        maya_cmds.setKeyframe(node_name + ".translateX", time=1, value=1)
    layer = maya_cmds.animLayer("BackendComparisonLayer")
    for node_name in (expected_node, name):
        maya_cmds.animLayer(
            layer, edit=True, attribute=node_name + ".translateX"
        )
    maya_cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    expected_plug = expected_node + ".translateX"
    plug_name = name + ".translateX"
    maya_cmds.setKeyframe(expected_plug, time=2, value=12)
    expected_curve = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=expected_plug
    )[0]
    expected_state = _curve_state(maya_cmds, expected_curve)
    before_layer_curve = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=plug_name
    )
    before_curves = sorted(maya_cmds.ls(type="animCurve"))
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    set_keyframe_calls.clear()

    keyframe.set(12, 2)
    mod.do_it_dg()
    assert len(set_keyframe_calls) == 1
    actual_curve = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=plug_name
    )[0]
    assert expected_state[1] == [11.0]
    for _ in range(2):
        assert _curve_state(maya_cmds, actual_curve) == expected_state
        maya_cmds.currentTime(0)
        maya_cmds.currentTime(2)
        assert maya_cmds.getAttr(plug_name) == pytest.approx(
            maya_cmds.getAttr(expected_plug)
        )
        mod.undo_it()
        assert (
            maya_cmds.animLayer(layer, query=True, findCurveForPlug=plug_name)
            == before_layer_curve
        )
        assert sorted(maya_cmds.ls(type="animCurve")) == before_curves
        mod.redo_it()
        assert len(set_keyframe_calls) == 1


@pytest.mark.parametrize(
    "connection", ["shared_output", "explicit_time_input"]
)
def test_connected_curve_uses_conservative_cmds_fallback(
    new_scene,
    maya_cmds,
    set_keyframe_calls,
    connection,
):
    name = maya_cmds.createNode("transform", name="connectedBackendTarget")
    maya_cmds.setKeyframe(name + ".translateX", time=1, value=1)
    curve = _source_curve(maya_cmds, name + ".translateX")
    if connection == "shared_output":
        other = maya_cmds.createNode("transform", name="sharedBackendTarget")
        maya_cmds.connectAttr(curve + ".output", other + ".translateX")
    else:
        maya_cmds.connectAttr("time1.outTime", curve + ".input")
    before = _curve_state(maya_cmds, curve)
    before_connections = maya_cmds.listConnections(
        curve, connections=True, plugs=True
    )
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    set_keyframe_calls.clear()

    keyframe.set(2, 2)
    mod.do_it_dg()
    assert len(set_keyframe_calls) == 1
    after = _curve_state(maya_cmds, curve)
    assert after[:2] == ([1.0, 2.0], [1.0, 2.0])
    for _ in range(2):
        assert _curve_state(maya_cmds, curve) == after
        mod.undo_it()
        assert _curve_state(maya_cmds, curve) == before
        assert (
            maya_cmds.listConnections(curve, connections=True, plugs=True)
            == before_connections
        )
        mod.redo_it()
        assert len(set_keyframe_calls) == 1
