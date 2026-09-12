from __future__ import annotations

import json
import math
from dataclasses import replace

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    AnimCurveData,
    CurveKeyframeManager,
    KeyframeManager,
)
from test_keyframe_data import _assert_equivalent
from test_keyframe_set_equivalence import (
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _object(name):
    selection = om.MSelectionList()
    selection.add(name)
    return selection.getDependNode(0)


def _curve(cmds, curve_type="animCurveTL"):
    name = cmds.createNode(curve_type, name="explicitCurve")
    curve = oma.MFnAnimCurve(_object(name))
    curve.addKey(om.MTime(1, om.MTime.uiUnit()), 1.0)
    curve.addKey(om.MTime(5, om.MTime.uiUnit()), 5.0)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    return nodes.existing(name).keyframe, mod, curve


@pytest.mark.parametrize(
    "curve_type", ["animCurveTA", "animCurveTL", "animCurveTU"]
)
def test_explicit_units_queue_order_and_repeated_history(
    maya_cmds, monkeypatch, curve_type
):
    keyframe, mod, curve = _curve(maya_cmds, curve_type)
    before = keyframe.get_curve_data()
    assert isinstance(keyframe, CurveKeyframeManager)
    assert keyframe.has_anim_curve() and keyframe.key_count() == 2
    scale = 180 / math.pi if curve_type == "animCurveTA" else 1
    assert keyframe.values() == pytest.approx([scale, 5 * scale])

    def forbidden(*args, **kwargs):
        pytest.fail(
            "Explicit edits must not delegate value resolution to cmds."
        )

    monkeypatch.setattr(maya_cmds, "setKeyframe", forbidden)
    keyframe.set_keys([(3, 30), (7, 70), (3, 33)], out_tangent_type="linear")
    keyframe.set_key(55, 5)
    keyframe.insert_key(4, breakdown=True)
    keyframe.set_tangent(4, in_tangent_type="linear", out_tangent_type="flat")
    keyframe.delete_key(1)
    keyframe.delete_keys(7, 7)
    assert keyframe.get_curve_data() == before
    assert not mod.can_undo
    maya_cmds.currentUnit(angle="rad", linear="m")
    maya_cmds.flushUndo()
    mod.do_it_dg()
    assert keyframe.frames() == [3, 4, 5]
    assert keyframe.values()[::2] == pytest.approx([33, 55])
    assert keyframe.has_key(4)
    assert keyframe.get_key_data()[1].breakdown
    assert keyframe.get_key_data()[1].out_tangent_type == "flat"
    after = _curve_state(curve)
    assert maya_cmds.undoInfo(q=True, undoQueueEmpty=True)
    for _ in range(2):
        mod.undo_it()
        assert keyframe.frames() == [1, 5]
        assert keyframe.values() == pytest.approx([scale, 5 * scale])
        mod.redo_it()
        _assert_equivalent(_curve_state(curve), after)


@pytest.mark.parametrize(
    "curve_type", ["animCurveTA", "animCurveTL", "animCurveTU"]
)
def test_pending_creation_queries_do_not_flush_and_creation_undo_redo(
    maya_cmds, curve_type
):
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    node = getattr(nodes.create, curve_type)(name="pendingCurve")
    keyframe = node.keyframe
    with pytest.raises(RuntimeError, match="not available"):
        keyframe.get_curve_data()
    assert not maya_cmds.objExists("pendingCurve")
    keyframe.set_keys([(1, 2), (3, 4)])
    keyframe.set_weighted(True)
    mod.do_it_dg()
    assert keyframe.get_keys() == pytest.approx([(1, 2), (3, 4)])
    for _ in range(2):
        mod.undo_it()
        with pytest.raises(RuntimeError, match="not available"):
            keyframe.frames()
        assert not maya_cmds.objExists("pendingCurve")
        mod.redo_it()
        assert keyframe.get_keys() == pytest.approx([(1, 2), (3, 4)])
        assert keyframe.get_weighted() is True


@pytest.mark.parametrize(
    "attribute_type", ["doubleAngle", "doubleLinear", "double"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("boundaries", [False, True])
def test_explicit_snapshot_clip_and_json_share_plug_implementation(
    maya_cmds, attribute_type, weighted, boundaries
):
    plug, source = _existing_curve(maya_cmds, "source", attribute_type)
    source.setIsWeighted(weighted)
    expected = KeyframeManager(plug).get_curve_data(
        2, 8, include_boundaries=boundaries
    )
    keyframe = CurveKeyframeManager(source.object())
    maya_cmds.disconnectAttr(source.name() + ".output", plug.name())
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.connectAttr(source.name() + ".output", conversion + ".input")
    maya_cmds.connectAttr("time1.outTime", source.name() + ".input")
    before = _curve_state(source)
    nodes_before = set(maya_cmds.ls())
    maya_cmds.file(modified=False)
    data = keyframe.get_curve_data(2, 8, include_boundaries=boundaries)
    assert data == expected
    assert data.keys == tuple(
        keyframe.get_key_data(2, 8, include_boundaries=boundaries)
    )
    _assert_equivalent(_curve_state(source), before)
    assert set(maya_cmds.ls()) == nodes_before
    assert not maya_cmds.file(q=True, modified=True)
    data = AnimCurveData.from_dict(json.loads(json.dumps(data.to_dict())))
    samples = {
        frame: source.evaluate(om.MTime(frame, om.MTime.kFilm))
        for frame in (2, 2.5, 3.25, 4.75, 5, 5.5, 7, 8)
    }
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    target = getattr(nodes.create, data.curve_type)(name="restored")
    target.keyframe.set_curve_data(data)
    data.keys[0].value += 999
    maya_cmds.currentUnit(time="ntsc", updateAnimation=False)
    mod.do_it_dg()
    restored = oma.MFnAnimCurve(target.m_obj)
    if boundaries:
        for frame, value in samples.items():
            time = om.MTime(frame, om.MTime.kFilm)
            assert restored.evaluate(time) == pytest.approx(
                value, rel=2e-6, abs=2e-7
            )
    assert restored.isWeighted == weighted
    after = _curve_state(restored)
    for _ in range(2):
        mod.undo_it()
        assert not maya_cmds.objExists("restored")
        mod.redo_it()
        _assert_equivalent(_curve_state(restored), after)


@pytest.mark.parametrize("weighted", [False, True])
def test_partial_data_copies_inputs_and_preserves_weighted(
    maya_cmds, weighted
):
    keyframe, mod, curve = _curve(maya_cmds)
    curve.setIsWeighted(weighted)
    before = keyframe.get_curve_data()
    key = replace(before.keys[0], frame=3, value=8)
    keyframe.set_key_data([key])
    key.value = 999
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 1), (3, 8), (5, 5)]
    assert keyframe.get_weighted() == weighted
    after = keyframe.get_curve_data()
    for _ in range(2):
        mod.undo_it()
        assert keyframe.get_curve_data() == before
        mod.redo_it()
        assert keyframe.get_curve_data() == after
    keyframe.set_key_data([])
    keyframe.set_keys([])
    mod.do_it_dg()
    assert keyframe.get_curve_data() == after


@pytest.mark.parametrize("mode", ["rename", "reconnect"])
def test_node_identity_survives_rename_or_output_reconnection(maya_cmds, mode):
    keyframe, mod, curve = _curve(maya_cmds)
    original = curve.name()
    target = maya_cmds.createNode("transform")
    maya_cmds.connectAttr(original + ".output", target + ".tx")
    keyframe.set_key(80, 3)
    if mode == "rename":
        mod.dg_mod.renameNode(curve.object(), "renamedCurve")
    else:
        target_plug = om.MFnDependencyNode(_object(target)).findPlug(
            "tx", False
        )
        replacement = _object(maya_cmds.createNode("animCurveTL"))
        mod.dg_mod.disconnect(curve.findPlug("output", False), target_plug)
        mod.dg_mod.connect(
            oma.MFnAnimCurve(replacement).findPlug("output", False),
            target_plug,
        )
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 1), (3, 80), (5, 5)]
    if mode == "rename":
        assert curve.name() == "renamedCurve"
    else:
        assert oma.MFnAnimCurve(replacement).numKeys == 0
    mod.undo_it()
    assert keyframe.get_keys() == [(1, 1), (5, 5)]
    mod.redo_it()
    assert keyframe.get_keys() == [(1, 1), (3, 80), (5, 5)]


def test_deleted_node_is_not_replaced_by_same_name_and_failed_batch_rolls_back(
    maya_cmds,
):
    keyframe, mod, curve = _curve(maya_cmds)
    name = curve.name()
    other_name = maya_cmds.createNode("animCurveTL", name="other")
    other = (
        bdu.Nodes(modifier_manager=mod)
        .existing.animCurveTL(other_name)
        .keyframe
    )
    other.set_key(12, 1)
    keyframe.set_key(20, 2)
    maya_cmds.delete(name)
    replacement = maya_cmds.createNode("animCurveTL", name=name)
    with pytest.raises(RuntimeError, match="not available"):
        keyframe.get_keys()
    with pytest.raises(RuntimeError, match="not available"):
        mod.do_it_dg()
    assert other.get_keys() == []
    assert oma.MFnAnimCurve(_object(replacement)).numKeys == 0
    assert not mod.can_undo and not mod.can_redo


def test_shared_curve_and_time_driver_edit_delete_restore_all_connections(
    maya_cmds,
):
    keyframe, mod, curve = _curve(maya_cmds)
    name = curve.name()
    targets = [maya_cmds.createNode("transform") for _ in range(2)]
    for target in targets:
        maya_cmds.connectAttr(name + ".output", target + ".tx")
    maya_cmds.connectAttr("time1.outTime", name + ".input")
    owner = maya_cmds.createNode("network")
    maya_cmds.addAttr(owner, longName="curve", attributeType="message")
    maya_cmds.connectAttr(name + ".message", owner + ".curve")
    keyframe.set_key(9, 3)
    mod.do_it_dg()
    for target in targets:
        assert maya_cmds.getAttr(target + ".tx", time=3) == 9
    maya_cmds.setAttr(targets[0] + ".tx", lock=True)
    keyframe.set_key(10, 3)
    mod.do_it_dg()
    assert keyframe.get_keys()[1] == (3, 10)
    maya_cmds.setAttr(targets[0] + ".tx", lock=False)
    mod.clear()
    before = keyframe.get_curve_data()
    keyframe.delete_anim_curve()
    mod.do_it_dg()
    for _ in range(2):
        assert not maya_cmds.objExists(name)
        assert all(maya_cmds.objExists(n) for n in targets + ["time1", owner])
        with pytest.raises(RuntimeError, match="not available"):
            keyframe.get_curve_data()
        mod.undo_it()
        assert keyframe.get_curve_data() == before
        assert maya_cmds.isConnected("time1.outTime", name + ".input")
        assert maya_cmds.isConnected(name + ".message", owner + ".curve")
        for target in targets:
            assert maya_cmds.isConnected(name + ".output", target + ".tx")
        mod.redo_it()


EDITS = [
    ("set_key", (20, 3)),
    ("set_keys", ([(3, 20)],)),
    ("insert_key", (3,)),
    ("set_tangent", (1, "linear")),
    ("delete_key", (1,)),
    ("delete_keys", ()),
    ("delete_anim_curve", ()),
    ("set_weighted", (True,)),
    ("set_key_data", ()),
    ("set_curve_data", ()),
]


def _queue_edit(keyframe, method, args):
    if method == "set_key_data":
        args = (keyframe.get_key_data(),)
    elif method == "set_curve_data":
        args = (keyframe.get_curve_data(),)
    getattr(keyframe, method)(*args)


@pytest.mark.parametrize("method,args", EDITS)
@pytest.mark.parametrize("lock", ["node", "output", "key", "input"])
def test_explicit_write_rechecks_locks_but_queries_allow_them(
    maya_cmds, method, args, lock
):
    keyframe, mod, curve = _curve(maya_cmds)
    before = keyframe.get_curve_data()
    _queue_edit(keyframe, method, args)
    if lock == "node":
        maya_cmds.lockNode(curve.name(), lock=True)
    else:
        attribute = "ktv[0].kv" if lock == "key" else lock
        maya_cmds.setAttr(curve.name() + "." + attribute, lock=True)
    assert keyframe.get_curve_data() == before
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == before
    assert not mod.can_undo


@pytest.mark.parametrize("method,args", EDITS)
def test_explicit_reference_is_readable_but_not_editable(
    maya_cmds, tmp_path, method, args
):
    _curve(maya_cmds)
    path = str(tmp_path / "curve_reference.ma")
    maya_cmds.file(rename=path)
    maya_cmds.file(save=True, type="mayaAscii")
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(path, reference=True, namespace="ref")
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod)
        .existing.animCurveTL("ref:explicitCurve")
        .keyframe
    )
    before = keyframe.get_curve_data()
    _queue_edit(keyframe, method, args)
    with pytest.raises(RuntimeError, match="referenced"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == before


@pytest.mark.parametrize("kind", ["quaternion", "driven_attribute"])
def test_unsupported_curve_state_is_rechecked_at_execution(maya_cmds, kind):
    keyframe, mod, curve = _curve(maya_cmds, "animCurveTA")
    before = _curve_state(curve)
    keyframe.set_key(20, 3)
    if kind == "quaternion":
        curve.findPlug("rotationInterpolation", False).setInt(3)
    else:
        source = maya_cmds.createNode("multiplyDivide")
        maya_cmds.connectAttr(
            source + ".outputX", curve.name() + ".keyTanInX[0]"
        )
    with pytest.raises(RuntimeError):
        keyframe.get_curve_data()
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert curve.numKeys == len(before["keys"])
    assert not mod.can_undo


@pytest.mark.parametrize(
    "curve_type",
    [
        "animCurveUA",
        "animCurveUL",
        "animCurveUU",
        "animCurveUT",
        "animCurveTT",
        "transform",
    ],
)
def test_explicit_unsupported_node_types(maya_cmds, curve_type):
    name = maya_cmds.createNode(curve_type)
    with pytest.raises((TypeError, RuntimeError)):
        CurveKeyframeManager(_object(name))


def test_explicit_validation_and_missing_modifier_do_not_edit(maya_cmds):
    keyframe, mod, curve = _curve(maya_cmds)
    before = keyframe.get_curve_data()
    with pytest.raises(TypeError):
        CurveKeyframeManager(curve.name())
    with pytest.raises(TypeError):
        CurveKeyframeManager(om.MObject.kNullObj)
    with pytest.raises(RuntimeError, match="ModifierManager"):
        CurveKeyframeManager(curve.object()).set_key(1, 1)
    for call in (
        lambda: keyframe.set_keys([(3, 20), (4, float("nan"))]),
        lambda: keyframe.set_key(1, float("inf")),
        lambda: keyframe.set_key(1, 2, in_tangent_type="step"),
        lambda: keyframe.set_curve_data(
            replace(before, curve_type="animCurveTA")
        ),
        lambda: keyframe.get_keys(5, 1),
        lambda: keyframe.get_key_data(1, 5, include_boundaries=1),
    ):
        with pytest.raises((ValueError, TypeError)):
            call()
    assert not mod.can_undo
    mod.do_it_dg()
    assert keyframe.get_curve_data() == before


@pytest.mark.parametrize("lock", ["plug", "node"])
def test_delete_preflights_all_destinations_before_disconnecting(
    maya_cmds, lock
):
    keyframe, mod, curve = _curve(maya_cmds)
    name = curve.name()
    targets = [maya_cmds.createNode("transform") for _ in range(2)]
    for target in targets:
        maya_cmds.connectAttr(name + ".output", target + ".tx")
    before = keyframe.get_curve_data()
    keyframe.set_key(20, 3)
    keyframe.delete_anim_curve()
    if lock == "plug":
        maya_cmds.setAttr(targets[1] + ".tx", lock=True)
    else:
        maya_cmds.lockNode(targets[1], lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == before
    for target in targets:
        assert maya_cmds.isConnected(name + ".output", target + ".tx")
    assert not mod.can_undo


@pytest.mark.parametrize(
    "curve_type", ["animCurveTA", "animCurveTL", "animCurveTU"]
)
def test_explicit_set_captures_input_time_unit(maya_cmds, curve_type):
    mod = bdu.ModifierManager()
    node = getattr(bdu.Nodes(modifier_manager=mod).create, curve_type)(
        name="queued"
    )
    keyframe = node.keyframe
    keyframe.set_keys([(12, 30), (24, 60)])
    maya_cmds.currentUnit(
        time="ntsc", angle="rad", linear="m", updateAnimation=False
    )
    mod.do_it_dg()
    for frame_value, expected in zip(
        keyframe.get_keys(), [(15, 30), (30, 60)]
    ):
        assert frame_value == pytest.approx(expected)


@pytest.mark.parametrize("locked", [False, True])
def test_explicit_layer_curve_edits_raw_value_and_respects_curve_locks(
    maya_cmds, locked
):
    target = maya_cmds.createNode("transform")
    maya_cmds.setKeyframe(target + ".tx", time=1, value=1)
    layer = maya_cmds.animLayer("Layer")
    maya_cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    maya_cmds.setKeyframe(target + ".tx", animLayer=layer, time=1, value=12)
    names = maya_cmds.animLayer(layer, q=True, animCurves=True)
    assert len(names) == 1
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing.animCurveTL(names[0]).keyframe
    )
    assert keyframe.get_keys() == [(1, 11)]
    before = keyframe.get_curve_data()
    keyframe.set_key(20, 1)
    if locked:
        maya_cmds.animLayer(layer, edit=True, lock=True)
        with pytest.raises(RuntimeError, match="locked"):
            mod.do_it_dg()
        assert keyframe.get_curve_data() == before
        return
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 20)]
    assert maya_cmds.getAttr(target + ".tx", time=1) == 21
    for _ in range(2):
        mod.undo_it()
        assert keyframe.get_curve_data() == before
        assert maya_cmds.getAttr(target + ".tx", time=1) == 12
        mod.redo_it()
        assert maya_cmds.getAttr(target + ".tx", time=1) == 21


def test_explicit_curve_does_not_reject_unrelated_layer(maya_cmds):
    keyframe, mod, curve = _curve(maya_cmds)
    layer = maya_cmds.animLayer("UnrelatedLayer")
    maya_cmds.animLayer(layer, edit=True, lock=True)
    keyframe.set_key(20, 3)
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 1), (3, 20), (5, 5)]


@pytest.mark.parametrize("lock_base", [False, True])
def test_base_curve_uses_base_layer_lock_not_other_layer_lock(
    maya_cmds, lock_base
):
    target = maya_cmds.createNode("transform")
    maya_cmds.setKeyframe(target + ".tx", time=1, value=1)
    name = maya_cmds.listConnections(target + ".tx", type="animCurve")[0]
    layer = maya_cmds.animLayer("Layer")
    maya_cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    base = maya_cmds.animLayer(q=True, root=True)
    maya_cmds.animLayer(base if lock_base else layer, edit=True, lock=True)
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing.animCurveTL(name).keyframe
    )
    before = keyframe.get_curve_data()
    keyframe.set_key(9, 1)
    if lock_base:
        with pytest.raises(RuntimeError, match="locked animation layer"):
            mod.do_it_dg()
        assert keyframe.get_curve_data() == before
    else:
        mod.do_it_dg()
        assert keyframe.get_keys() == [(1, 9)]


def test_explicit_frame_is_curve_input_time_not_scene_time(maya_cmds):
    keyframe, mod, curve = _curve(maya_cmds)
    driver = maya_cmds.createNode("network")
    maya_cmds.addAttr(driver, longName="curveTime", attributeType="time")
    maya_cmds.setAttr(driver + ".curveTime", 20)
    maya_cmds.connectAttr(driver + ".curveTime", curve.name() + ".input")
    target = maya_cmds.createNode("transform")
    maya_cmds.connectAttr(curve.name() + ".output", target + ".tx")
    keyframe.set_key(22, frame=20)
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 1), (5, 5), (20, 22)]
    assert maya_cmds.getAttr(target + ".tx", time=10) == 22
    assert keyframe.get_key_data(20, 20)[0].value == 22


@pytest.mark.parametrize("weighted", [False, True])
def test_full_restore_and_empty_curve_keep_node_and_connections(
    maya_cmds, weighted
):
    keyframe, mod, curve = _curve(maya_cmds)
    curve.setIsWeighted(weighted)
    target = maya_cmds.createNode("transform")
    maya_cmds.connectAttr(curve.name() + ".output", target + ".tx")
    data = replace(
        keyframe.get_curve_data(), weighted=weighted, pre_infinity="cycle"
    )
    empty = replace(data, keys=())
    keyframe.set_curve_data(empty)
    mod.do_it_dg()
    assert keyframe.has_anim_curve() and keyframe.get_curve_data() == empty
    assert (
        keyframe.get_keys()
        == keyframe.values()
        == keyframe.get_key_data()
        == []
    )
    assert maya_cmds.isConnected(curve.name() + ".output", target + ".tx")
    mod.clear()
    keyframe.set_curve_data(data)
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 1), (5, 5)]
    assert keyframe.get_weighted() == weighted
    after = keyframe.get_curve_data()
    assert after.pre_infinity == "cycle"
    for _ in range(2):
        mod.undo_it()
        assert keyframe.get_curve_data() == empty
        mod.redo_it()
        assert keyframe.get_curve_data() == after
    keyframe.delete_keys()
    mod.do_it_dg()
    assert keyframe.get_curve_data() == empty
    assert maya_cmds.objExists(curve.name())
