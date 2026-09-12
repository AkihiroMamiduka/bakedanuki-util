from __future__ import annotations

import json
from dataclasses import replace

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import AnimCurveData, KeyframeManager
from test_keyframe_set_equivalence import restore_animation_preferences
from test_keyframe_target import (
    EDITS,
    QUERIES,
    _object,
    _restrict,
    _state,
    _target,
)

pytestmark = pytest.mark.maya


def _manager(plug, mod):
    selection = om.MSelectionList()
    selection.add(plug)
    return KeyframeManager(selection.getPlug(0), modifier_manager=mod)


def _states(cmds):
    return {
        name: _state(oma.MFnAnimCurve(_object(name)))
        for name in cmds.ls(type="animCurve")
    }


def _standard(cmds, family):
    ctrl = cmds.createNode("transform", name="ctrl")
    driver = cmds.createNode("transform", name="driver")
    curves = {}
    for i, axis in enumerate("XYZ"):
        for frame in (1, 5):
            cmds.setKeyframe(
                ctrl + "." + family + axis, time=frame, value=frame + i
            )
            cmds.setKeyframe(
                driver + "." + family + axis, time=frame, value=10 * frame + i
            )
        curves[axis] = cmds.listConnections(
            ctrl + "." + family + axis, source=True, destination=False
        )[0]
    if family == "translate":
        cmds.pointConstraint(driver, ctrl)
    else:
        cmds.orientConstraint(driver, ctrl)
    blend = cmds.ls(type="pairBlend")[0]
    weight_plug = cmds.listConnections(
        blend + ".weight", source=True, destination=False, plugs=True
    )[0]
    cmds.setKeyframe(weight_plug, time=1, value=0.25)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(ctrl)
    keyframes = {
        axis: getattr(getattr(node, family), family + axis).keyframe
        for axis in "XYZ"
    }
    return node, keyframes, curves, blend, mod


@pytest.mark.parametrize("family", ["translate", "rotate"])
@pytest.mark.parametrize("axis", list("XYZ"))
def test_standard_pairblend_queries_choose_own_axis_and_ignore_other_animation(
    maya_cmds, family, axis
):
    node, keyframes, curves, blend, mod = _standard(maya_cmds, family)
    keyframe = keyframes[axis]
    curve = bdu.Nodes().existing(curves[axis]).keyframe
    assert maya_cmds.keyframe(keyframe.plug.name(), query=True, name=True) == [
        curves[axis]
    ]
    maya_cmds.selectKey(curves["X"], replace=True, time=(1, 1))
    for method, kwargs in QUERIES:
        assert getattr(keyframe, method)(**kwargs) == getattr(curve, method)(
            **kwargs
        )
    before = _states(maya_cmds)
    maya_cmds.file(modified=False)
    maya_cmds.flushUndo()
    current_time = maya_cmds.currentTime(query=True)
    selected = maya_cmds.ls(selection=True)
    assert (
        keyframe.get_curve_data(2, 4).keys == curve.get_curve_data(2, 4).keys
    )
    assert _states(maya_cmds) == before
    assert not maya_cmds.file(query=True, modified=True)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert maya_cmds.currentTime(query=True) == current_time
    assert maya_cmds.ls(selection=True) == selected
    assert not mod.can_undo


@pytest.mark.parametrize("family", ["translate", "rotate"])
@pytest.mark.parametrize("axis", list("XYZ"))
@pytest.mark.parametrize(
    "method", [m for m, _ in EDITS] + ["set_key_data", "set_curve_data"]
)
def test_channel_edits_touch_only_selected_curve_and_restore_connections(
    maya_cmds, family, axis, method
):
    node, keyframes, curves, blend, mod = _standard(maya_cmds, family)
    keyframe = keyframes[axis]
    selected = curves[axis]
    original = _states(maya_cmds)
    connections = maya_cmds.listConnections(
        blend, connections=True, plugs=True
    )
    if method.startswith("set_") and method.endswith("data"):
        data = keyframe.get_curve_data()
        data = replace(
            data,
            keys=tuple(replace(k, value=k.value + 20) for k in data.keys),
            weighted=True,
        )
        if method == "set_curve_data":
            keyframe.set_curve_data(
                AnimCurveData.from_dict(json.loads(json.dumps(data.to_dict())))
            )
        else:
            keyframe.set_key_data(data.keys)
    else:
        kwargs = dict(EDITS)[method]
        getattr(keyframe, method)(**kwargs)
    assert _states(maya_cmds) == original
    mod.do_it_dg()
    after = _states(maya_cmds)
    if method == "delete_anim_curve":
        assert selected not in after
        assert maya_cmds.objExists(blend) and maya_cmds.objExists(node.name)
        assert not keyframe.has_anim_curve()
    else:
        assert after[selected] != original[selected]
        assert (
            maya_cmds.listConnections(blend, connections=True, plugs=True)
            == connections
        )
        if method == "delete_keys":
            assert keyframe.has_anim_curve() and keyframe.key_count() == 0
            assert keyframe.get_curve_data().keys == ()
    assert {k: v for k, v in after.items() if k != selected} == {
        k: v for k, v in original.items() if k != selected
    }
    for _ in range(2):
        mod.undo_it()
        assert _states(maya_cmds) == original
        assert (
            maya_cmds.listConnections(blend, connections=True, plugs=True)
            == connections
        )
        mod.redo_it()
        assert _states(maya_cmds) == after


def test_current_driver_is_resolved_at_execution_and_redo_keeps_recorded_target(
    maya_cmds,
):
    ctrl = maya_cmds.createNode("transform")
    blend = maya_cmds.createNode("pairBlend")
    maya_cmds.connectAttr(blend + ".outTranslateY", ctrl + ".ty")
    mod = bdu.ModifierManager()
    keyframe = _manager(ctrl + ".ty", mod)
    for i in (1, 2):
        curve = maya_cmds.createNode("animCurveTL", name="curve" + str(i))
        maya_cmds.connectAttr(
            curve + ".output", blend + ".inTranslateY" + str(i)
        )
        maya_cmds.setKeyframe(curve, time=1, value=i)
    before = _states(maya_cmds)
    keyframe.set_weighted(True)
    maya_cmds.setAttr(blend + ".currentDriver", 2)
    assert keyframe.get_keys() == [(1, 2)]
    mod.do_it_dg()
    after = _states(maya_cmds)
    assert after["curve1"] == before["curve1"]
    assert after["curve2"] != before["curve2"]
    mod.undo_it()
    maya_cmds.setAttr(blend + ".currentDriver", 1)
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_blendweighted_uses_logical_input_order_and_does_not_follow_driven_key(
    maya_cmds,
):
    ctrl = maya_cmds.createNode("transform")
    blend = maya_cmds.createNode("blendWeighted")
    maya_cmds.connectAttr(blend + ".output", ctrl + ".sx")
    for index, kind, name in (
        (100, "animCurveTU", "alphabeticallyFirst"),
        (2, "animCurveTU", "selected"),
        (1, "animCurveUU", "driven"),
    ):
        curve = maya_cmds.createNode(kind, name=name)
        maya_cmds.connectAttr(curve + ".output", f"{blend}.input[{index}]")
        if kind == "animCurveTU":
            maya_cmds.setKeyframe(curve, time=1, value=index)
    driver = maya_cmds.createNode("animCurveTU", name="driverOfDriven")
    maya_cmds.connectAttr(driver + ".output", "driven.input")
    weight = maya_cmds.createNode("animCurveTU", name="weight")
    maya_cmds.connectAttr(weight + ".output", blend + ".weight[2]")
    keyframe = _manager(ctrl + ".sx", bdu.ModifierManager())
    assert keyframe.get_keys() == [(1, 2)]
    assert keyframe._get_anim_curve_fn().name() == "selected"


@pytest.mark.parametrize("kind", ["constraint", "driven", "pair_blend"])
@pytest.mark.parametrize("method", ["set_key_data", "set_curve_data"])
def test_restore_without_channel_curve_preserves_existing_connection(
    maya_cmds, kind, method
):
    keyframe, mod = _target(maya_cmds)
    data = keyframe.get_curve_data()
    _restrict(maya_cmds, keyframe, kind)
    if kind == "pair_blend":
        maya_cmds.disconnectAttr(
            "target_rotateX.output",
            maya_cmds.ls(type="pairBlend")[0] + ".inRotateX1",
        )
    before = _states(maya_cmds)
    source = keyframe.plug.sourceWithConversion().name()
    getattr(keyframe, method)(
        data if method == "set_curve_data" else data.keys
    )
    with pytest.raises(RuntimeError, match="connected plug"):
        mod.do_it_dg()
    assert keyframe.plug.sourceWithConversion().name() == source
    assert _states(maya_cmds) == before and not mod.can_undo


def test_channel_changes_and_native_key_creation_rollback_together(maya_cmds):
    node, keyframes, curves, blend, mod = _standard(maya_cmds, "translate")
    before = _states(maya_cmds)
    keyframes["Y"].set_key(20, 3)
    keyframes["Y"].set_tangent(3, out_tangent_type="linear")
    keyframes["Z"].delete_key(1)
    keyframes["X"].set_weighted(True)
    empty = maya_cmds.createNode("transform")
    _manager(empty + ".tx", mod).insert_key(1)
    with pytest.raises(RuntimeError, match="no channel"):
        mod.do_it_dg()
    assert _states(maya_cmds) == before
    assert not mod.can_undo and not mod.can_redo


def test_unknown_utility_requires_explicit_curve_instead_of_guessing_an_axis(
    maya_cmds,
):
    keyframe, mod = _target(maya_cmds)
    curve = keyframe.plug.sourceWithConversion().name()
    maya_cmds.disconnectAttr(curve, keyframe.plug.name())
    utility = maya_cmds.createNode("multiplyDivide")
    maya_cmds.connectAttr(curve, utility + ".input1X")
    maya_cmds.connectAttr(utility + ".outputX", keyframe.plug.name())
    with pytest.raises(RuntimeError, match="Cannot resolve the channel"):
        keyframe.get_keys()


@pytest.mark.parametrize("method,kwargs", EDITS)
def test_conversion_edits_preserve_node_and_factor_animation(
    maya_cmds, method, kwargs
):
    keyframe, mod = _target(maya_cmds)
    selected = keyframe._get_anim_curve_fn().name()
    _restrict(maya_cmds, keyframe, "conversion")
    conversion = maya_cmds.listConnections(
        keyframe.plug.name(),
        source=True,
        destination=False,
        skipConversionNodes=False,
    )[0]
    maya_cmds.setAttr(conversion + ".conversionFactor", 2)
    factor_curve = maya_cmds.createNode("animCurveTU", name="factorCurve")
    maya_cmds.connectAttr(
        factor_curve + ".output", conversion + ".conversionFactor"
    )
    maya_cmds.setKeyframe(factor_curve, time=1, value=2)
    before = _states(maya_cmds)
    assert keyframe.get_keys() == [(1, 1), (5, 5)]
    assert maya_cmds.getAttr(keyframe.plug.name(), time=1) == pytest.approx(2)
    getattr(keyframe, method)(**kwargs)
    mod.do_it_dg()
    after = _states(maya_cmds)
    assert maya_cmds.objExists(conversion)
    assert {k: v for k, v in after.items() if k != selected} == {
        k: v for k, v in before.items() if k != selected
    }
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_nested_blends_query_pending_connections_and_native_set_share_channel(
    maya_cmds,
):
    node, keyframes, curves, blend, mod = _standard(maya_cmds, "translate")
    keyframe = keyframes["Y"]
    nested = maya_cmds.createNode("pairBlend")
    keyframe.set_key(12, 3)
    # Queue a new intermediate pairBlend before the following edits execute.
    source = keyframe.plug.sourceWithConversion()
    fn = om.MFnDependencyNode(_object(nested))
    mod.dg_mod.disconnect(source, keyframe.plug)
    mod.dg_mod.connect(source, fn.findPlug("inTranslateY1", False))
    mod.dg_mod.connect(fn.findPlug("outTranslateY", False), keyframe.plug)
    keyframe.set_tangent(3, out_tangent_type="linear")
    before = _states(maya_cmds)
    assert keyframe.get_keys() == [(1, 2), (5, 6)]
    assert keyframe.plug.sourceWithConversion().node() != fn.object()
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 2), (3, 12), (5, 6)]
    assert keyframe.plug.sourceWithConversion().node() == fn.object()
    after = _states(maya_cmds)
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_empty_first_curve_stays_selected_and_can_be_restored(maya_cmds):
    node, keyframes, curves, blend, mod = _standard(maya_cmds, "translate")
    keyframe = keyframes["Y"]
    data = keyframe.get_curve_data()
    keyframe.delete_keys()
    mod.do_it_dg()
    assert (
        maya_cmds.keyframe(keyframe.plug.name(), query=True, name=True) is None
    )
    assert keyframe.has_anim_curve()
    assert keyframe.get_curve_data().keys == ()
    keyframe.set_curve_data(data)
    mod.do_it_dg()
    assert keyframe.get_curve_data() == data


@pytest.mark.parametrize("channel", ["translateY", "rotateZ"])
def test_native_set_then_query_and_edit_use_pairblend_current_driver(
    maya_cmds, channel
):
    family = "translate" if channel.startswith("translate") else "rotate"
    curve_type = "animCurveTL" if family == "translate" else "animCurveTA"
    target = maya_cmds.createNode("transform")
    blend = maya_cmds.createNode("pairBlend")
    output = "out" + channel[0].upper() + channel[1:]
    input_name = "in" + channel[0].upper() + channel[1:]
    maya_cmds.connectAttr(blend + "." + output, target + "." + channel)
    for index in (1, 2):
        curve = maya_cmds.createNode(curve_type, name="curve" + str(index))
        maya_cmds.connectAttr(
            curve + ".output", blend + "." + input_name + str(index)
        )
        maya_cmds.setKeyframe(curve, time=1, value=index)
    maya_cmds.setAttr(blend + ".currentDriver", 2)
    mod = bdu.ModifierManager()
    keyframe = _manager(target + "." + channel, mod)
    before = _states(maya_cmds)
    keyframe.set_key(20, 3)
    keyframe.delete_key(1)
    mod.do_it_dg()
    assert keyframe.get_keys() == [(3, 20)]
    assert _states(maya_cmds)["curve1"] == before["curve1"]
    mod.undo_it()
    assert _states(maya_cmds) == before


def test_pending_root_query_does_not_execute_node_creation(maya_cmds):
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.transform(name="pending")
    with pytest.raises(RuntimeError, match="not available"):
        node.translate.translateY.keyframe.get_keys()
    assert not maya_cmds.objExists("pending")
