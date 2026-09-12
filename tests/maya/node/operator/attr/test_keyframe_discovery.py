from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _keyframe(name, mod=None):
    selection = om.MSelectionList()
    selection.add(name)
    return KeyframeManager(selection.getPlug(0), modifier_manager=mod)


def _names(keyframe, **kwargs):
    return tuple(curve.name for curve in keyframe.find_anim_curves(**kwargs))


def _connect_curve(cmds, destination, name, curve_type="animCurveTU"):
    curve = cmds.createNode(curve_type, name=name)
    cmds.connectAttr(curve + ".output", destination)
    return curve


@pytest.mark.parametrize(
    "suffix", ["TA", "TL", "TT", "TU", "UA", "UL", "UT", "UU"]
)
def test_all_curve_types_are_discoverable_with_concrete_wrappers(
    maya_cmds, suffix
):
    node = maya_cmds.createNode("transform")
    curve_type = "animCurve" + suffix
    name = _connect_curve(maya_cmds, node + ".tx", "candidate", curve_type)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    keyframe = nodes.existing.transform(node).translate.translateX.keyframe
    candidates = keyframe.find_anim_curves()
    assert isinstance(candidates, tuple) and len(candidates) == 1
    curve = candidates[0]
    assert curve.name == name and curve.NODE_TYPE == curve_type
    assert isinstance(curve, getattr(nodes.types, "AnimCurve" + suffix))
    assert curve.modifier_manager is mod
    assert _names(keyframe, filter_type=type(curve)) == (name,)
    assert _names(_keyframe(name + ".output")) == (name,)


def test_blend_candidates_sort_deduplicate_and_filter_after_stopping(
    maya_cmds,
):
    blend = maya_cmds.createNode("blendWeighted")
    a = _connect_curve(maya_cmds, blend + ".input[0]", "zCurve")
    maya_cmds.connectAttr(a + ".output", blend + ".input[1]")
    b = _connect_curve(
        maya_cmds, blend + ".input[2]", "aDriven", "animCurveUU"
    )
    _connect_curve(maya_cmds, b + ".input", "hiddenDriver")
    weight = _connect_curve(maya_cmds, blend + ".weight[0]", "mWeight")
    keyframe = _keyframe(blend + ".output")
    assert _names(keyframe) == (b, weight, a)
    nodes = bdu.Nodes()
    assert _names(keyframe, filter_type=nodes.types.AnimCurveTU) == (weight, a)
    assert _names(keyframe, filter_type=nodes.types.AnimCurveTL) == ()


def test_declared_dependencies_can_include_other_axes_but_not_unrelated_nodes(
    maya_cmds,
):
    multiply = maya_cmds.createNode("multiplyDivide")
    x = _connect_curve(maya_cmds, multiply + ".input1X", "axisX")
    y = _connect_curve(maya_cmds, multiply + ".input1Y", "axisY")
    unrelated = maya_cmds.createNode("transform")
    _connect_curve(maya_cmds, unrelated + ".tx", "unrelated")
    assert _names(_keyframe(multiply + ".outputX")) == (x, y)


def test_layer_curves_and_weight_are_candidates_even_when_muted_and_locked(
    maya_cmds,
):
    node = maya_cmds.createNode("transform")
    plug = node + ".tx"
    maya_cmds.setKeyframe(plug, time=1, value=2)
    layer = maya_cmds.animLayer("layer", attribute=plug)
    maya_cmds.setKeyframe(plug, time=1, value=3, animLayer=layer)
    maya_cmds.setKeyframe(layer + ".weight", time=1, value=0.5)
    keyframe = _keyframe(plug)
    expected = set(maya_cmds.ls(type="animCurve"))
    assert len(expected) == 3
    assert set(_names(keyframe)) == expected
    maya_cmds.animLayer(layer, edit=True, mute=True, lock=True)
    assert set(_names(keyframe)) == expected
    assert keyframe.get_keys() == [(1.0, 2.0)]


def test_constraint_and_world_space_dependencies(maya_cmds):
    driver = maya_cmds.createNode("transform", name="driver")
    target = maya_cmds.createNode("transform", name="target")
    curve = _connect_curve(maya_cmds, driver + ".tx", "motion", "animCurveTL")
    maya_cmds.pointConstraint(driver, target)
    assert _names(_keyframe(target + ".tx")) == (curve,)
    decompose = maya_cmds.createNode("decomposeMatrix")
    maya_cmds.connectAttr(
        driver + ".worldMatrix[0]", decompose + ".inputMatrix"
    )
    assert _names(_keyframe(decompose + ".outputTranslateX")) == (curve,)


def test_message_links_do_not_add_curve_candidates(maya_cmds):
    target = maya_cmds.createNode("transform")
    curve = maya_cmds.createNode("animCurveTU")
    maya_cmds.addAttr(target, longName="owner", attributeType="message")
    maya_cmds.connectAttr(curve + ".message", target + ".owner")
    assert _names(_keyframe(target + ".tx")) == ()
    with pytest.raises(TypeError, match="scalar"):
        _names(_keyframe(target + ".owner"))


def test_query_has_no_scene_history_or_pending_modifier_side_effects(
    maya_cmds,
):
    target = maya_cmds.createNode("transform")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    node = nodes.existing.transform(target)
    curve = nodes.create.animCurveTL(name="pendingCurve")
    curve.output.connect(node.translate.translateX)
    curve.keyframe.set_key(2, 1)
    maya_cmds.select(target)
    maya_cmds.currentTime(17)
    maya_cmds.flushUndo()
    maya_cmds.file(modified=False)
    before = (
        maya_cmds.ls(),
        maya_cmds.ls(selection=True),
        maya_cmds.currentTime(query=True),
    )
    assert node.translate.translateX.keyframe.find_anim_curves() == ()
    assert not mod.can_undo
    assert not maya_cmds.objExists("pendingCurve")
    assert not maya_cmds.file(query=True, modified=True)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert before == (
        maya_cmds.ls(),
        maya_cmds.ls(selection=True),
        maya_cmds.currentTime(query=True),
    )
    mod.do_it_dg()
    (candidate,) = node.translate.translateX.keyframe.find_anim_curves()
    assert candidate.m_obj == curve.m_obj and candidate.modifier_manager is mod
    assert candidate.keyframe.get_keys() == [(1, 2)]
    mod.undo_it()
    assert node.translate.translateX.keyframe.find_anim_curves() == ()
    mod.redo_it()
    assert _names(node.translate.translateX.keyframe) == (curve.name,)


def test_selected_candidate_keeps_identity_and_edits_share_undo(maya_cmds):
    blend = maya_cmds.createNode("blendWeighted")
    a = _connect_curve(maya_cmds, blend + ".input[0]", "first")
    b = _connect_curve(maya_cmds, blend + ".input[1]", "second")
    mod = bdu.ModifierManager()
    keyframe = _keyframe(blend + ".output", mod)
    selected, other = keyframe.find_anim_curves()
    maya_cmds.rename(a, "renamed")
    maya_cmds.disconnectAttr("renamed.output", blend + ".input[0]")
    assert _names(keyframe) == (b,)
    selected.keyframe.set_keys([(1, 4), (5, 8)])
    mod.do_it_dg()
    assert selected.name == "renamed"
    assert selected.keyframe.get_keys() == [(1, 4), (5, 8)]
    assert other.keyframe.get_keys() == []
    mod.undo_it()
    assert selected.keyframe.get_keys() == []
    mod.redo_it()
    assert selected.keyframe.get_keys() == [(1, 4), (5, 8)]


@pytest.mark.parametrize("attribute", ["translate", "worldMatrix", "message"])
def test_unsupported_root_plugs_raise(maya_cmds, attribute):
    node = maya_cmds.createNode("transform")
    with pytest.raises(TypeError, match="scalar"):
        _names(_keyframe(node + "." + attribute))


@pytest.mark.parametrize(
    "filter_type", ["animCurveTL", 1, object, bdu.Nodes().types.Transform]
)
def test_invalid_filter_rejected_without_needing_a_candidate(
    maya_cmds, filter_type
):
    node = maya_cmds.createNode("transform")
    with pytest.raises(TypeError, match="filter_type"):
        _names(_keyframe(node + ".tx"), filter_type=filter_type)


def test_pending_or_deleted_root_is_an_error(maya_cmds):
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    curve = nodes.create.animCurveTL(name="pending")
    keyframe = curve.output.keyframe
    with pytest.raises(RuntimeError, match="not available"):
        keyframe.find_anim_curves()
    mod.do_it_dg()
    maya_cmds.delete(curve.name)
    with pytest.raises(RuntimeError, match="not available"):
        keyframe.find_anim_curves()


def test_discovery_without_manager_shares_one_new_manager(maya_cmds):
    blend = maya_cmds.createNode("blendWeighted")
    _connect_curve(maya_cmds, blend + ".input[0]", "a")
    _connect_curve(maya_cmds, blend + ".input[1]", "b")
    a, b = _keyframe(blend + ".output").find_anim_curves()
    assert a.modifier_manager is b.modifier_manager
    assert not a.modifier_manager.can_undo


def test_sparse_arrays_are_distinct_and_query_does_not_create_elements(
    maya_cmds,
):
    blend = maya_cmds.createNode("blendWeighted")
    first = _connect_curve(maya_cmds, blend + ".input[2]", "first")
    last = _connect_curve(maya_cmds, blend + ".input[100]", "last")
    keyframe = _keyframe(blend + ".output")
    inputs = maya_cmds.getAttr(blend + ".input", multiIndices=True)
    weights = maya_cmds.getAttr(blend + ".weight", multiIndices=True)
    maya_cmds.file(modified=False)
    maya_cmds.flushUndo()
    assert _names(keyframe) == (first, last)
    assert maya_cmds.getAttr(blend + ".input", multiIndices=True) == inputs
    assert maya_cmds.getAttr(blend + ".weight", multiIndices=True) == weights
    assert not maya_cmds.file(query=True, modified=True)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_discovery_does_not_require_an_editable_curve(maya_cmds):
    target = maya_cmds.createNode("transform")
    name = _connect_curve(
        maya_cmds, target + ".rx", "lockedCurve", "animCurveTA"
    )
    selection = om.MSelectionList()
    selection.add(name)
    om.MFnDependencyNode(selection.getDependNode(0)).findPlug(
        "rotationInterpolation", False
    ).setInt(2)
    maya_cmds.lockNode(name, lock=True)
    maya_cmds.setAttr(target + ".rx", lock=True)
    (candidate,) = _keyframe(target + ".rx").find_anim_curves()
    assert candidate.name == name
    with pytest.raises(RuntimeError, match="independent scalar"):
        candidate.keyframe.get_keys()


def test_time_driver_is_not_discovered_past_a_curve_output(maya_cmds):
    target = maya_cmds.createNode("transform")
    name = _connect_curve(maya_cmds, target + ".tx", "motion", "animCurveTL")
    driver = _connect_curve(
        maya_cmds, name + ".input", "timeDriver", "animCurveTT"
    )
    assert _names(_keyframe(target + ".tx")) == (name,)
    assert _names(_keyframe(name + ".input")) == (driver,)
