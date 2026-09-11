# coding: utf-8
from __future__ import annotations

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager

pytestmark = pytest.mark.maya


@pytest.fixture(autouse=True)
def restore_units(new_scene, maya_cmds):
    units = {
        flag: maya_cmds.currentUnit(query=True, **{flag: True})
        for flag in ("linear", "angle", "time")
    }
    maya_cmds.currentUnit(linear="cm", angle="deg", time="film")
    yield
    maya_cmds.currentUnit(**units)


def _keyframe(mod, node_name, attribute="translateX"):
    return getattr(
        bdu.Nodes(modifier_manager=mod).existing(node_name), attribute
    ).keyframe


def _scene_state(maya_cmds, plug_name):
    curves = {}
    for curve in sorted(maya_cmds.ls(type="animCurve")):
        curves[curve] = (
            maya_cmds.keyframe(curve, query=True, timeChange=True),
            maya_cmds.keyframe(curve, query=True, valueChange=True),
            maya_cmds.keyTangent(curve, query=True, inTangentType=True),
            maya_cmds.keyTangent(curve, query=True, outTangentType=True),
        )
    return (
        curves,
        maya_cmds.listConnections(
            plug_name, source=True, destination=False, plugs=True
        ),
    )


def _record_commands(monkeypatch, maya_cmds, *, fail_at=None):
    original = maya_cmds.setKeyframe
    calls = []

    def set_keyframe(*args, **kwargs):
        calls.append((args, kwargs))
        if len(calls) == fail_at:
            raise RuntimeError("intentional remaining key command failure")
        return original(*args, **kwargs)

    monkeypatch.setattr(maya_cmds, "setKeyframe", set_keyframe)
    return calls


def _record_api_edits(monkeypatch, *, fail_at=None):
    edits = []

    class RecordedAnimCurve(oma.MFnAnimCurve):
        def addKey(self, time, *args, **kwargs):
            index = super().addKey(time, *args, **kwargs)
            edits.append((id(self), time.asUnits(om.MTime.uiUnit())))
            if len(edits) == fail_at:
                raise RuntimeError("intentional failure during batch API edit")
            return index

    monkeypatch.setattr(oma, "MFnAnimCurve", RecordedAnimCurve)
    return edits


def _record_routes(monkeypatch, *, fail_at=None):
    original = KeyframeManager._api_set_curve
    routes = []

    def route(self, in_type):
        routes.append(self.plug.name())
        if len(routes) == fail_at:
            raise RuntimeError(
                "intentional remaining batch preparation failure"
            )
        return original(self, in_type)

    monkeypatch.setattr(KeyframeManager, "_api_set_curve", route)
    return routes


@pytest.mark.parametrize("existing_curve", [False, True])
def test_batch_reuses_routing_and_function_set_in_input_order(
    maya_cmds, monkeypatch, existing_curve
):
    name = maya_cmds.createNode("transform", name="batchRoutingTarget")
    if existing_curve:
        maya_cmds.setKeyframe(name + ".translateX", time=1, value=10)
    before = _scene_state(maya_cmds, name + ".translateX")
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    commands = _record_commands(monkeypatch, maya_cmds)
    routes = _record_routes(monkeypatch)
    edits = _record_api_edits(monkeypatch)
    frames = [5, 2, 5, 4]
    values = [50, 20, 55, 40]

    assert keyframe.set_keys(values, frames=frames) is None
    assert commands == routes == edits == []
    assert _scene_state(maya_cmds, name + ".translateX") == before
    mod.do_it_dg()

    assert len(commands) == (0 if existing_curve else 1)
    assert len(routes) == (1 if existing_curve else 2)
    assert [frame for _, frame in edits] == (
        frames if existing_curve else frames[1:]
    )
    assert len({identity for identity, _ in edits}) == 1
    assert keyframe.frames() == ([1.0] if existing_curve else []) + [
        2.0,
        4.0,
        5.0,
    ]
    assert keyframe.values() == ([10.0] if existing_curve else []) + [
        20.0,
        40.0,
        55.0,
    ]
    after = _scene_state(maya_cmds, name + ".translateX")
    counts = (len(commands), len(routes), len(edits))
    for _ in range(3):
        mod.undo_it()
        assert _scene_state(maya_cmds, name + ".translateX") == before
        mod.redo_it()
        assert _scene_state(maya_cmds, name + ".translateX") == after
        assert (len(commands), len(routes), len(edits)) == counts


@pytest.mark.parametrize("kind", ["bool", "conversion", "shared", "layer"])
def test_batch_fallback_runs_each_key_as_cmds_and_restores_scene(
    maya_cmds, monkeypatch, kind
):
    name = maya_cmds.createNode("transform", name="batchFallbackTarget")
    attribute = "visibility" if kind == "bool" else "translateX"
    plug_name = name + "." + attribute
    if kind == "conversion":
        curve = maya_cmds.createNode("animCurveTU")
        conversion = maya_cmds.createNode("unitConversion")
        maya_cmds.setKeyframe(curve, time=1, value=1)
        maya_cmds.connectAttr(curve + ".output", conversion + ".input")
        maya_cmds.connectAttr(conversion + ".output", plug_name)
        maya_cmds.setAttr(conversion + ".conversionFactor", 3)
    else:
        maya_cmds.setKeyframe(plug_name, time=1, value=1)
    if kind == "shared":
        other = maya_cmds.createNode("transform", name="batchSharedTarget")
        output = maya_cmds.listConnections(
            plug_name, source=True, destination=False, plugs=True
        )[0]
        maya_cmds.connectAttr(output, other + ".translateX")
    elif kind == "layer":
        layer = maya_cmds.animLayer("BatchLayer")
        maya_cmds.animLayer(layer, edit=True, attribute=plug_name)
        maya_cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    before = _scene_state(maya_cmds, plug_name)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name, attribute)
    commands = _record_commands(monkeypatch, maya_cmds)
    routes = _record_routes(monkeypatch)
    edits = _record_api_edits(monkeypatch)

    keyframe.set_keys([0, 1, 0, 1], frames=[3, 1, 3, 4])
    mod.do_it_dg()

    assert [kwargs["time"] for _, kwargs in commands] == [3.0, 1.0, 3.0, 4.0]
    assert len(routes) == 2
    assert edits == []
    after = _scene_state(maya_cmds, plug_name)
    assert after != before
    for _ in range(2):
        mod.undo_it()
        assert _scene_state(maya_cmds, plug_name) == before
        mod.redo_it()
        assert _scene_state(maya_cmds, plug_name) == after
        assert len(commands) == 4
        assert len(routes) == 2
        assert edits == []


@pytest.mark.parametrize("existing_curve", [False, True])
def test_batch_api_failure_restores_bootstrap_and_all_partial_key_edits(
    maya_cmds, monkeypatch, existing_curve
):
    name = maya_cmds.createNode("transform", name="batchApiFailureTarget")
    if existing_curve:
        maya_cmds.setKeyframe(name + ".translateX", time=1, value=10)
    before = _scene_state(maya_cmds, name + ".translateX")
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    previous = mod.dg_mod.createNode("network")
    mod.dg_mod.renameNode(previous, "previousBatchFlush")
    mod.do_it_dg()
    current = mod.dg_mod.createNode("network")
    mod.dg_mod.renameNode(current, "failedBatchFlush")
    commands = _record_commands(monkeypatch, maya_cmds)
    edits = _record_api_edits(monkeypatch, fail_at=3)

    keyframe.set_keys([50, 20, 55, 40, 60], frames=[5, 2, 5, 4, 6])
    with pytest.raises(
        RuntimeError, match="intentional failure during batch API edit"
    ):
        mod.do_it_dg()

    assert len(edits) == 3
    assert len(commands) == (0 if existing_curve else 1)
    assert _scene_state(maya_cmds, name + ".translateX") == before
    assert not maya_cmds.objExists("failedBatchFlush")
    assert maya_cmds.objExists("previousBatchFlush")
    assert mod.can_undo
    assert not mod.can_redo
    mod.do_it_dg()
    mod.undo_it()
    assert not maya_cmds.objExists("previousBatchFlush")
    mod.redo_it()
    assert maya_cmds.objExists("previousBatchFlush")
    assert _scene_state(maya_cmds, name + ".translateX") == before
    assert len(edits) == 3


def test_batch_recheck_failure_restores_the_successful_first_cmds_key(
    maya_cmds, monkeypatch
):
    name = maya_cmds.createNode(
        "transform", name="batchPreparationFailureTarget"
    )
    before = _scene_state(maya_cmds, name + ".translateX")
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name)
    commands = _record_commands(monkeypatch, maya_cmds)
    routes = _record_routes(monkeypatch, fail_at=2)
    edits = _record_api_edits(monkeypatch)

    keyframe.set_keys([10, 20, 30], frames=[1, 2, 3])
    with pytest.raises(
        RuntimeError, match="intentional remaining batch preparation failure"
    ):
        mod.do_it_dg()

    assert len(commands) == 1
    assert len(routes) == 2
    assert edits == []
    assert _scene_state(maya_cmds, name + ".translateX") == before
    assert not mod.can_undo
    assert not mod.can_redo
    mod.do_it_dg()
    assert len(commands) == 1
    assert _scene_state(maya_cmds, name + ".translateX") == before


@pytest.mark.parametrize("existing_curve", [False, True])
def test_batch_later_cmds_failure_restores_previous_commands(
    maya_cmds, monkeypatch, existing_curve
):
    name = maya_cmds.createNode("transform", name="batchCmdsFailureTarget")
    plug_name = name + ".visibility"
    if existing_curve:
        maya_cmds.setKeyframe(plug_name, time=1, value=1)
    before = _scene_state(maya_cmds, plug_name)
    mod = bdu.ModifierManager()
    keyframe = _keyframe(mod, name, "visibility")
    commands = _record_commands(monkeypatch, maya_cmds, fail_at=3)
    edits = _record_api_edits(monkeypatch)

    keyframe.set_keys([0, 1, 0, 1], frames=[1, 2, 1, 4])
    with pytest.raises(RuntimeError):
        mod.do_it_dg()

    assert len(commands) == 3
    assert edits == []
    assert _scene_state(maya_cmds, plug_name) == before
    assert not mod.can_undo
    assert not mod.can_redo
    mod.do_it_dg()
    assert len(commands) == 3
    assert _scene_state(maya_cmds, plug_name) == before
