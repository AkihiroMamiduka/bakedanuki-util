from __future__ import annotations

from dataclasses import replace

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr import _keyframe_snapshot as snapshot
from test_keyframe_channel import _states
from test_keyframe_data import _assert_equivalent
from test_keyframe_set_equivalence import (
    _assert_curve_state,
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya
CHANNELS = ("translateY", "rotateZ", "scaleX")
DESTINATIONS = ("base", "base_explicit", "additive", "override")


def _source(cmds, channel):
    name = cmds.createNode("transform", name="source")
    for frame, value in ((-10, 2), (10, 6)):
        cmds.setKeyframe(
            name + "." + channel,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )
    keyframe = getattr(bdu.Nodes().existing.transform(name), channel).keyframe
    curve = snapshot.resolve_curve(keyframe._target)
    curve.setIsWeighted(False)
    return keyframe.get_curve_data(), _curve_state(curve)


def _destination(cmds, channel="translateY", destination="base"):
    name = cmds.createNode("transform", name="destination")
    additive = cmds.animLayer("Additive")
    override = cmds.animLayer("Override", override=True)
    for layer in (additive, override):
        cmds.animLayer(layer, edit=True, attribute=name + "." + channel[:-1])
    base = cmds.animLayer(query=True, root=True)
    selected = {
        "base": base,
        "base_explicit": base,
        "additive": additive,
        "override": override,
    }[destination]
    cmds.animLayer(override, edit=True, selected=True, preferred=True)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(name)
    keyframe = getattr(node, channel).keyframe
    if destination != "base":
        keyframe = keyframe.anim_layer(selected)
    return keyframe, mod, selected


def _scene(cmds):
    nodes = sorted(cmds.ls(long=True))
    connections = {
        name: sorted(
            cmds.listConnections(name, connections=True, plugs=True) or []
        )
        for name in nodes
    }
    layers = {
        name: (
            sorted(cmds.animLayer(name, query=True, attribute=True) or []),
            tuple(
                cmds.getAttr(name + "." + attr)
                for attr in (
                    "weight",
                    "mute",
                    "solo",
                    "lock",
                    "selected",
                    "preferred",
                    "override",
                )
            ),
        )
        for name in cmds.ls(type="animLayer")
    }
    return nodes, connections, _states(cmds), layers


def _write(keyframe, data, method):
    if method == "keys":
        keyframe.set_key_data(
            data.keys, seconds_per_frame=data.seconds_per_frame
        )
    else:
        keyframe.set_curve_data(data)


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("destination", DESTINATIONS)
@pytest.mark.parametrize("method", ["curve", "keys", "empty_curve"])
def test_layer_restore_creates_only_its_curve_without_a_seed_key(
    maya_cmds, channel, destination, method
):
    data, source_state = _source(maya_cmds, channel)
    keyframe, mod, _ = _destination(maya_cmds, channel, destination)
    if method == "empty_curve":
        data = replace(
            data,
            keys=(),
            weighted=True,
            pre_infinity="linear",
            post_infinity="cycle",
        )
    maya_cmds.keyTangent(g=True, weightedTangents=True)
    maya_cmds.select("destination")
    maya_cmds.flushUndo()
    maya_cmds.file(modified=False)
    before = _scene(maya_cmds)
    selection = maya_cmds.ls(selection=True)
    current_time = maya_cmds.currentTime(query=True)

    _write(keyframe, data, method)
    assert keyframe.get_curve_data() is None
    assert _scene(maya_cmds) == before
    assert not maya_cmds.file(query=True, modified=True)
    mod.do_it_dg()
    restored = snapshot.resolve_curve(keyframe._target)
    assert keyframe.frames() == ([] if method == "empty_curve" else [-10, 10])
    assert not keyframe.has_key(0)
    if method == "empty_curve":
        assert keyframe.get_curve_data() == data
    else:
        _assert_curve_state(_curve_state(restored), source_state)
    after = _scene(maya_cmds)
    assert len(after[2]) == len(before[2]) + 1
    assert {
        name: state
        for name, state in after[2].items()
        if name != restored.name()
    } == before[2]
    assert after[3] == before[3]
    assert maya_cmds.ls(selection=True) == selection
    assert maya_cmds.currentTime(query=True) == current_time
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    for _ in range(2):
        mod.undo_it()
        assert _scene(maya_cmds) == before
        mod.redo_it()
        assert _scene(maya_cmds) == after


@pytest.mark.parametrize("destination", DESTINATIONS)
@pytest.mark.parametrize("condition", ["zero_weight", "muted"])
@pytest.mark.parametrize("method", ["curve", "keys"])
def test_layer_restore_writes_raw_values_with_inactive_layers(
    maya_cmds, destination, condition, method
):
    data, source_state = _source(maya_cmds, "translateY")
    keyframe, mod, layer = _destination(maya_cmds, destination=destination)
    maya_cmds.setAttr(
        layer + (".weight" if condition == "zero_weight" else ".mute"),
        0 if condition == "zero_weight" else True,
    )
    _write(keyframe, data, method)
    mod.do_it_dg()
    _assert_curve_state(
        _curve_state(snapshot.resolve_curve(keyframe._target)), source_state
    )


@pytest.mark.parametrize("destination", DESTINATIONS)
@pytest.mark.parametrize(
    "channel,attribute_type",
    [
        ("translateY", "doubleLinear"),
        ("rotateZ", "doubleAngle"),
        ("scaleX", "double"),
    ],
)
def test_weighted_layer_restore_preserves_shape_after_pending_unit_changes(
    maya_cmds, destination, channel, attribute_type
):
    plug, source = _existing_curve(maya_cmds, "source", attribute_type)
    source.setIsWeighted(True)
    expected = _curve_state(source)
    times = tuple(
        om.MTime(seconds, om.MTime.kSeconds)
        for seconds in (-0.1, 0.03, 0.13, 0.24, 0.37, 0.6)
    )
    samples = [source.evaluate(time) for time in times]
    data = KeyframeManager(plug).get_curve_data()
    keyframe, mod, _ = _destination(maya_cmds, channel, destination)
    keyframe.set_curve_data(data)
    maya_cmds.currentUnit(
        angle="rad", linear="m", time="ntsc", updateAnimation=False
    )
    mod.do_it_dg()
    restored = snapshot.resolve_curve(keyframe._target)
    _assert_equivalent(_curve_state(restored), expected)
    for time, value in zip(times, samples):
        assert restored.evaluate(time) == pytest.approx(
            value, rel=2e-6, abs=2e-7
        )


@pytest.mark.parametrize("method", ["curve", "keys"])
@pytest.mark.parametrize("explicit", [False, True])
@pytest.mark.parametrize("registration", ["nodes", "plugs"])
def test_restore_follows_pending_layer_creation_registration_and_rename(
    maya_cmds, method, explicit, registration
):
    data, _ = _source(maya_cmds, "translateY")
    name = maya_cmds.createNode("transform", name="destination")
    before = _scene(maya_cmds)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    dest = nodes.existing.transform(name)
    layer = nodes.create.animLayer(name="PendingLayer")
    if registration == "nodes":
        layer.add_nodes([dest])
    else:
        layer.add_plugs([dest.ty])
    mod.dg_mod.renameNode(layer.m_obj, "RenamedLayer")
    mod.dg_mod.renameNode(dest.m_obj, "renamedDestination")
    keyframe = (
        dest.ty.keyframe.anim_layer(layer) if explicit else dest.ty.keyframe
    )
    _write(keyframe, data, method)
    assert _scene(maya_cmds) == before
    mod.do_it_dg()
    assert keyframe.frames() == [-10, 10]
    assert keyframe.values() == pytest.approx([2, 6])
    after = _scene(maya_cmds)
    for _ in range(2):
        mod.undo_it()
        assert _scene(maya_cmds) == before
        mod.redo_it()
        assert _scene(maya_cmds) == after


@pytest.mark.parametrize("channel", CHANNELS)
@pytest.mark.parametrize("method", ["curve", "keys"])
def test_existing_user_keys_follow_replace_or_merge_contract(
    maya_cmds, channel, method
):
    data, _ = _source(maya_cmds, channel)
    keyframe, mod, _ = _destination(maya_cmds, channel)
    keyframe.set_key(99, frame=0)
    _write(keyframe, data, method)
    mod.do_it_dg()
    assert keyframe.frames() == (
        [-10, 0, 10] if method == "keys" else [-10, 10]
    )
    if method == "keys":
        assert keyframe.get_keys(0, 0) == [(0, 99)]


@pytest.mark.parametrize("destination", DESTINATIONS)
def test_empty_key_data_does_not_create_a_curve(maya_cmds, destination):
    keyframe, mod, _ = _destination(maya_cmds, destination=destination)
    before = _scene(maya_cmds)
    keyframe.set_key_data([])
    mod.do_it_dg()
    assert keyframe.get_curve_data() is None
    assert _scene(maya_cmds) == before


@pytest.mark.parametrize("destination", ["base", "additive"])
@pytest.mark.parametrize("method", ["curve", "keys"])
@pytest.mark.parametrize("failure", ["restore", "later"])
def test_failed_restore_removes_created_curve_and_partial_data(
    maya_cmds, monkeypatch, destination, method, failure
):
    data, _ = _source(maya_cmds, "translateY")
    keyframe, mod, _ = _destination(maya_cmds, destination=destination)
    before = _scene(maya_cmds)

    def fail(*args):
        raise RuntimeError("intentional restore failure")

    if failure == "restore":
        original = snapshot._restore_key_data

        def restore_then_fail(*args):
            original(*args)
            fail()

        monkeypatch.setattr(snapshot, "_restore_key_data", restore_then_fail)
    _write(keyframe, data, method)
    if failure == "later":
        mod.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="intentional restore failure"):
        mod.do_it_dg()
    assert _scene(maya_cmds) == before
    assert keyframe.get_curve_data() is None
    assert not mod.can_undo


@pytest.mark.parametrize("destination", ["base", "additive"])
@pytest.mark.parametrize(
    "restriction", ["layer_lock", "node_lock", "plug_lock"]
)
@pytest.mark.parametrize("method", ["curve", "keys"])
def test_missing_curve_restore_rechecks_locks_at_execution(
    maya_cmds, destination, restriction, method
):
    data, _ = _source(maya_cmds, "translateY")
    keyframe, mod, layer = _destination(maya_cmds, destination=destination)
    _write(keyframe, data, method)
    if restriction == "layer_lock":
        maya_cmds.animLayer(layer, edit=True, lock=True)
    elif restriction == "node_lock":
        maya_cmds.lockNode("destination", lock=True)
    else:
        maya_cmds.setAttr(keyframe.plug.name(), lock=True)
    before = _scene(maya_cmds)
    with pytest.raises(RuntimeError, match="lock"):
        mod.do_it_dg()
    assert _scene(maya_cmds) == before


@pytest.mark.parametrize("method", ["curve", "keys"])
def test_restore_does_not_register_nonmember_plugs(maya_cmds, method):
    data, _ = _source(maya_cmds, "translateY")
    layer = maya_cmds.animLayer("EmptyLayer")
    name = maya_cmds.createNode("transform", name="destination")
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod)
        .existing.transform(name)
        .ty.keyframe.anim_layer(layer)
    )
    before = _scene(maya_cmds)
    _write(keyframe, data, method)
    with pytest.raises(RuntimeError, match="not a member"):
        mod.do_it_dg()
    assert _scene(maya_cmds) == before


@pytest.mark.parametrize("method", ["curve", "keys"])
@pytest.mark.parametrize(
    "layers", ["none", "unrelated", "explicit", "member", "explicit_member"]
)
@pytest.mark.parametrize(
    "connection", ["constraint", "driven_key", "pair_blend", "blend_weighted"]
)
def test_restore_does_not_create_through_other_connections(
    maya_cmds, method, layers, connection
):
    data, _ = _source(maya_cmds, "translateY")
    name = maya_cmds.createNode("transform", name="destination")
    driver = maya_cmds.createNode("transform", name="driver")
    if connection == "constraint":
        maya_cmds.pointConstraint(driver, name)
    elif connection == "driven_key":
        maya_cmds.setDrivenKeyframe(
            name + ".ty", currentDriver=driver + ".tx", driverValue=0, value=2
        )
    elif connection == "pair_blend":
        blend = maya_cmds.createNode("pairBlend")
        maya_cmds.connectAttr(blend + ".outTranslateY", name + ".ty")
    else:
        blend = maya_cmds.createNode("blendWeighted")
        maya_cmds.setAttr(blend + ".input[0]", 2)
        maya_cmds.connectAttr(blend + ".output", name + ".ty")
    if layers != "none":
        layer = maya_cmds.animLayer("Layer")
        if "member" in layers:
            maya_cmds.animLayer(layer, edit=True, attribute=name + ".ty")
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing.transform(name).ty.keyframe
    )
    if layers.startswith("explicit"):
        keyframe = keyframe.anim_layer(
            maya_cmds.animLayer(query=True, root=True)
        )
    before = _scene(maya_cmds)
    _write(keyframe, data, method)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _scene(maya_cmds) == before
    assert not mod.can_undo


@pytest.mark.parametrize("method", ["curve", "keys"])
@pytest.mark.parametrize("destination", ["base", "additive"])
def test_restore_rejects_a_locked_layer_input(maya_cmds, method, destination):
    data, _ = _source(maya_cmds, "translateY")
    keyframe, mod, _ = _destination(maya_cmds, destination=destination)
    layer_input = maya_cmds.animLayer(
        "Additive", query=True, layeredPlug=keyframe.plug.name()
    )
    if destination == "base":
        layer_input = layer_input.replace(".inputB", ".inputA")
    maya_cmds.setAttr(layer_input, lock=True)
    before = _scene(maya_cmds)
    _write(keyframe, data, method)
    with pytest.raises(RuntimeError, match="lock"):
        mod.do_it_dg()
    assert _scene(maya_cmds) == before


@pytest.mark.parametrize("method", ["curve", "keys"])
def test_restore_rejects_other_drivers_on_the_named_layer_input(
    maya_cmds, method
):
    data, _ = _source(maya_cmds, "translateY")
    keyframe, mod, layer = _destination(maya_cmds, destination="additive")
    layer_input = maya_cmds.animLayer(
        layer, query=True, layeredPlug=keyframe.plug.name()
    )
    blend = maya_cmds.createNode("pairBlend")
    maya_cmds.connectAttr(blend + ".outTranslateY", layer_input)
    before = _scene(maya_cmds)
    _write(keyframe, data, method)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert _scene(maya_cmds) == before
