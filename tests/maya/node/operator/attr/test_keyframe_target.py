from __future__ import annotations

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager
from test_keyframe_set_equivalence import (
    _assert_curve_state,
    _curve_state,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya

QUERIES = (
    ("has_anim_curve", {}),
    ("frames", {}),
    ("values", {}),
    ("key_count", {}),
    ("has_key", {"frame": 1}),
    ("get_keys", {}),
    ("get_key_data", {}),
    ("get_curve_data", {}),
    ("get_weighted", {}),
)
EDITS = (
    ("insert_key", {"frame": 3}),
    ("set_tangent", {"frame": 1, "out_tangent_type": "flat"}),
    ("delete_key", {"frame": 1}),
    ("delete_keys", {}),
    ("delete_anim_curve", {}),
    ("set_weighted", {"weighted": True}),
)


def _state(curve):
    if curve.isTimeInput:
        return _curve_state(curve)
    return tuple(
        (
            curve.input(i),
            curve.value(i),
            curve.getTangentXY(i, True),
            curve.getTangentXY(i, False),
        )
        for i in range(curve.numKeys)
    )


def _target(cmds):
    node = cmds.createNode("transform", name="target")
    for frame, value in ((1, 1), (5, 5)):
        cmds.setKeyframe(node + ".rx", time=frame, value=value)
    selection = om.MSelectionList()
    selection.add(node + ".rx")
    mod = bdu.ModifierManager()
    return KeyframeManager(selection.getPlug(0), modifier_manager=mod), mod


def _restrict(cmds, keyframe, kind):
    plug = keyframe.plug.name()
    curve = cmds.listConnections(plug, source=True, destination=False)[0]
    if kind == "shared":
        other = cmds.createNode("transform")
        cmds.connectAttr(curve + ".output", other + ".rx")
    elif kind == "time_input":
        cmds.connectAttr("time1.outTime", curve + ".input")
    elif kind == "quaternion":
        selection = om.MSelectionList()
        selection.add(curve)
        om.MFnDependencyNode(selection.getDependNode(0)).findPlug(
            "rotationInterpolation", False
        ).setInt(2)
    elif kind.startswith("layer"):
        layer = cmds.animLayer("Layer")
        if kind == "layer_member":
            cmds.animLayer(layer, edit=True, attribute=plug)
    else:
        cmds.disconnectAttr(curve + ".output", plug)
        if kind == "conversion":
            conversion = cmds.createNode("unitConversion")
            cmds.connectAttr(curve + ".output", conversion + ".input")
            cmds.connectAttr(conversion + ".output", plug)
        elif kind == "pair_blend":
            blend = cmds.createNode("pairBlend")
            cmds.connectAttr(curve + ".output", blend + ".inRotateX1")
            cmds.connectAttr(blend + ".outRotateX", plug)
        elif kind == "driven":
            driven = cmds.createNode("animCurveUA")
            cmds.setKeyframe(driven, float=1, value=10)
            cmds.connectAttr(driven + ".output", plug)
        else:
            drivers = [
                cmds.createNode("transform")
                for _ in range(2 if kind == "multiple_upstream" else 1)
            ]
            for driver in drivers:
                cmds.setKeyframe(driver + ".rx", time=1, value=20)
            cmds.orientConstraint(*drivers, plug.split(".")[0])


@pytest.mark.parametrize(
    "kind",
    [
        "conversion",
        "constraint",
        "multiple_upstream",
        "pair_blend",
        "shared",
        "time_input",
        "driven",
        "quaternion",
        "layer_unrelated",
        "layer_member",
    ],
)
@pytest.mark.parametrize("method,kwargs", QUERIES + EDITS)
def test_unsupported_graph_is_rejected_without_editing_upstream(
    maya_cmds, kind, method, kwargs
):
    keyframe, mod = _target(maya_cmds)
    # Edits must inspect the graph when executed, not when queued.
    editing = (method, kwargs) in EDITS
    if editing:
        getattr(keyframe, method)(**kwargs)
    _restrict(maya_cmds, keyframe, kind)
    nodes = set(maya_cmds.ls())
    curves = []
    for name in maya_cmds.ls(type="animCurve"):
        selection = om.MSelectionList()
        selection.add(name)
        curve = oma.MFnAnimCurve(selection.getDependNode(0))
        curves.append((curve, _state(curve)))
    history = (
        maya_cmds.undoInfo(q=True, undoName=True),
        maya_cmds.undoInfo(q=True, redoName=True),
    )
    with pytest.raises(RuntimeError):
        if editing:
            mod.do_it_dg()
        else:
            getattr(keyframe, method)(**kwargs)
    assert set(maya_cmds.ls()) == nodes
    for curve, before in curves:
        assert _state(curve) == before
    assert not mod.can_undo and not mod.can_redo
    assert (
        maya_cmds.undoInfo(q=True, undoName=True),
        maya_cmds.undoInfo(q=True, redoName=True),
    ) == history


@pytest.mark.parametrize("method,kwargs", EDITS)
@pytest.mark.parametrize("lock", ["plug", "node", "curve", "key"])
def test_direct_queries_allow_locks_but_edits_revalidate_at_execution(
    maya_cmds, method, kwargs, lock
):
    keyframe, mod = _target(maya_cmds)
    before = keyframe.get_curve_data()
    curve = keyframe.plug.sourceWithConversion().node()
    curve_name = om.MFnDependencyNode(curve).name()
    getattr(keyframe, method)(**kwargs)
    if lock == "node":
        maya_cmds.lockNode(keyframe.plug.name().split(".")[0], lock=True)
    elif lock == "curve":
        maya_cmds.lockNode(curve_name, lock=True)
    else:
        maya_cmds.setAttr(
            (
                keyframe.plug.name()
                if lock == "plug"
                else curve_name + ".ktv[0].kv"
            ),
            lock=True,
        )
    assert keyframe.get_curve_data() == before
    assert keyframe.frames() == [1, 5]
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == before
    assert not mod.can_undo


def test_simple_set_query_edit_share_curve_and_reconnect_is_resolved_late(
    maya_cmds,
):
    keyframe, mod = _target(maya_cmds)
    original = keyframe.plug.sourceWithConversion()
    before = keyframe.get_curve_data()
    selection = om.MSelectionList()
    selection.add(maya_cmds.createNode("animCurveTA"))
    replacement = oma.MFnAnimCurve(selection.getDependNode(0))
    replacement.addKey(om.MTime(1, om.MTime.uiUnit()), 0)
    replacement.addKey(om.MTime(5, om.MTime.uiUnit()), 1)
    replacement_before = _curve_state(replacement)
    mod.dg_mod.disconnect(original, keyframe.plug)
    mod.dg_mod.connect(replacement.findPlug("output", False), keyframe.plug)
    keyframe.set_key(90, frame=3)
    keyframe.set_tangent(3, out_tangent_type="linear")
    keyframe.delete_key(1)
    assert keyframe.get_curve_data() == before
    mod.do_it_dg()
    pairs = keyframe.get_keys()
    assert len(pairs) == 2
    assert pairs[0] == pytest.approx((3, 90))
    assert pairs[1] == pytest.approx((5, 180 / 3.141592653589793))
    assert (
        [key.frame for key in keyframe.get_key_data()]
        == keyframe.frames()
        == [3, 5]
    )
    after = keyframe.get_curve_data()
    for _ in range(2):
        mod.undo_it()
        assert keyframe.get_curve_data() == before
        _assert_curve_state(_curve_state(replacement), replacement_before)
        mod.redo_it()
        assert keyframe.get_curve_data() == after


def test_rejected_curve_edit_rolls_back_prior_work_in_same_batch(maya_cmds):
    keyframe, mod = _target(maya_cmds)
    original = keyframe.get_curve_data()
    keyframe.set_key(20, 2)
    other = maya_cmds.createNode("transform")
    destination = om.MSelectionList()
    destination.add(other + ".rx")
    mod.dg_mod.connect(
        keyframe.plug.sourceWithConversion(), destination.getPlug(0)
    )
    keyframe.delete_keys()
    with pytest.raises(RuntimeError, match="unshared"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == original
    assert not maya_cmds.listConnections(
        other + ".rx", source=True, destination=False
    )
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("method,kwargs", EDITS)
def test_referenced_curve_can_be_read_but_not_edited(
    maya_cmds, tmp_path, method, kwargs
):
    _target(maya_cmds)
    path = str(tmp_path / "keyframe_reference.ma")
    maya_cmds.file(rename=path)
    maya_cmds.file(save=True, type="mayaAscii")
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(path, reference=True, namespace="referenced")
    selection = om.MSelectionList()
    selection.add("referenced:target.rx")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(selection.getPlug(0), modifier_manager=mod)
    before = keyframe.get_curve_data()
    assert before is not None and keyframe.frames() == [1, 5]
    getattr(keyframe, method)(**kwargs)
    with pytest.raises(RuntimeError, match="referenced"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == before
    assert not mod.can_undo
