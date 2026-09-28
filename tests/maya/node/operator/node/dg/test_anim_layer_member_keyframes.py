from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _times(cmds, curve):
    return [
        round(frame, 6)
        for frame in cmds.keyframe(curve, query=True, timeChange=True) or ()
    ]


def _layer_curve(cmds, layer, plug):
    return cmds.animLayer(layer, query=True, findCurveForPlug=plug)[0]


def test_direct_members_only_leave_base_other_layer_and_weight_untouched(
    maya_cmds,
):
    for name in ("ctrl", "other"):
        maya_cmds.createNode("transform", name=name)
    maya_cmds.setKeyframe("ctrl.tx", time=0, value=0)
    maya_cmds.setKeyframe("ctrl.tx", time=1.4, value=4)
    first = maya_cmds.animLayer("First")
    for plug in ("ctrl.tx", "other.ty"):
        maya_cmds.animLayer(first, edit=True, attribute=plug)
    maya_cmds.setKeyframe(
        "ctrl.tx", animLayer=first, time=1.4, value=10, noResolve=True
    )
    maya_cmds.setKeyframe(
        "other.ty", animLayer=first, time=3.6, value=20, noResolve=True
    )
    second = maya_cmds.animLayer("Second", attribute="ctrl.tx")
    maya_cmds.setKeyframe(
        "ctrl.tx", animLayer=second, time=2.4, value=30, noResolve=True
    )
    maya_cmds.setKeyframe(first + ".weight", time=2.3, value=0.5)

    first_curves = [
        _layer_curve(maya_cmds, first, plug)
        for plug in ("ctrl.tx", "other.ty")
    ]
    base_curve = _layer_curve(
        maya_cmds, maya_cmds.animLayer(query=True, root=True), "ctrl.tx"
    )
    second_curve = _layer_curve(maya_cmds, second, "ctrl.tx")
    weight_curve = maya_cmds.listConnections(
        first + ".weight", source=True, destination=False, type="animCurve"
    )[0]
    untouched = {
        curve: _times(maya_cmds, curve)
        for curve in (base_curve, second_curve, weight_curve)
    }
    original = [_times(maya_cmds, curve) for curve in first_curves]

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    layer = nodes.existing.animLayer(first)
    assert layer.member_keyframes.snap_subframe_keys() is None
    assert [_times(maya_cmds, curve) for curve in first_curves] == original
    mod.do_it_dg()

    assert 1 in _times(maya_cmds, first_curves[0])
    assert 1.4 not in _times(maya_cmds, first_curves[0])
    assert 4 in _times(maya_cmds, first_curves[1])
    assert 3.6 not in _times(maya_cmds, first_curves[1])
    assert {
        curve: _times(maya_cmds, curve) for curve in untouched
    } == untouched

    for _ in range(2):
        mod.undo_it()
        assert [_times(maya_cmds, curve) for curve in first_curves] == original
        mod.redo_it()
        assert 1.4 not in _times(maya_cmds, first_curves[0])
        assert 3.6 not in _times(maya_cmds, first_curves[1])


def test_membership_and_curves_are_discovered_at_execution(maya_cmds):
    maya_cmds.createNode("transform", name="ctrl")
    name = maya_cmds.animLayer("Correction")
    mod = bdu.ModifierManager()
    layer = bdu.Nodes(modifier_manager=mod).existing.animLayer(name)
    layer.member_keyframes.snap_subframe_keys()

    maya_cmds.animLayer(name, edit=True, attribute="ctrl.tx")
    maya_cmds.setKeyframe(
        "ctrl.tx", animLayer=name, time=2.3, value=5, noResolve=True
    )
    curve = _layer_curve(maya_cmds, name, "ctrl.tx")
    mod.do_it_dg()
    assert 2 in _times(maya_cmds, curve)
    assert 2.3 not in _times(maya_cmds, curve)


def test_earlier_queued_layer_creation_and_key_are_included(maya_cmds):
    maya_cmds.createNode("transform", name="ctrl")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    ctrl = nodes.existing.transform("ctrl")
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs([ctrl.tx])
    ctrl.tx.keyframe.anim_layer(layer).set_key(5, frame=2.3)
    layer.member_keyframes.snap_subframe_keys()
    mod.do_it_dg()

    curve = _layer_curve(maya_cmds, "Correction", "ctrl.tx")
    assert 2 in _times(maya_cmds, curve)
    assert 2.3 not in _times(maya_cmds, curve)
    mod.undo_it()
    assert not maya_cmds.objExists("Correction")


def test_child_layer_curves_are_not_included(maya_cmds):
    maya_cmds.createNode("transform", name="ctrl")
    parent = maya_cmds.animLayer("Parent", attribute="ctrl.tx")
    child = maya_cmds.animLayer("Child", attribute="ctrl.ty")
    maya_cmds.animLayer(child, edit=True, parent=parent)
    maya_cmds.setKeyframe(
        "ctrl.tx", animLayer=parent, time=1.4, value=4, noResolve=True
    )
    maya_cmds.setKeyframe(
        "ctrl.ty", animLayer=child, time=2.3, value=5, noResolve=True
    )
    parent_curve = _layer_curve(maya_cmds, parent, "ctrl.tx")
    child_curve = _layer_curve(maya_cmds, child, "ctrl.ty")

    mod = bdu.ModifierManager()
    layer = bdu.Nodes(modifier_manager=mod).existing.animLayer(parent)
    layer.member_keyframes.snap_subframe_keys()
    mod.do_it_dg()
    assert 1.4 not in _times(maya_cmds, parent_curve)
    assert 2.3 in _times(maya_cmds, child_curve)


def test_root_layer_is_rejected(maya_cmds):
    maya_cmds.animLayer("Correction")
    root_name = maya_cmds.animLayer(query=True, root=True)
    mod = bdu.ModifierManager()
    layer = bdu.Nodes(modifier_manager=mod).existing.animLayer(root_name)
    layer.member_keyframes.snap_subframe_keys()
    with pytest.raises(RuntimeError, match="base"):
        mod.do_it_dg()
    assert not mod.can_undo and not mod.can_redo
