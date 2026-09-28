from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _members(cmds, layer):
    return set(cmds.animLayer(layer, query=True, attribute=True) or ())


def _setup(cmds):
    cmds.createNode("transform", name="ctrl")
    cmds.createNode("transform", name="other")
    cmds.addAttr("ctrl", longName="displayOnly", attributeType="double")
    cmds.setKeyframe("ctrl.tx", time=1, value=2)
    first = cmds.animLayer("First")
    for path in ("ctrl.tx", "ctrl.ty", "ctrl.displayOnly", "other.tx"):
        cmds.animLayer(first, edit=True, attribute=path)
    cmds.setKeyframe("ctrl.tx", animLayer=first, time=1, value=8)
    cmds.setKeyframe("ctrl.ty", animLayer=first, time=1, value=4)
    cmds.setKeyframe("other.tx", animLayer=first, time=1, value=6)
    second = cmds.animLayer("Second", attribute="ctrl.tx")
    cmds.setKeyframe("ctrl.tx", animLayer=second, time=1, value=12)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    ctrl = nodes.existing.transform("ctrl")
    other = nodes.existing.transform("other")
    return mod, nodes, ctrl, other, nodes.existing.animLayer(first)


@pytest.mark.parametrize("form", ["wrapper", "api", "name"])
def test_remove_all_registered_plugs_and_preserve_other_nodes_layers(
    maya_cmds, form
):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    target = {"wrapper": ctrl, "api": ctrl.m_obj, "name": "ctrl"}[form]
    maya_cmds.setAttr("ctrl.ty", keyable=False)
    assert not maya_cmds.getAttr("ctrl.displayOnly", keyable=True)
    before = set(maya_cmds.ls())
    first_curves = {
        maya_cmds.animLayer("First", query=True, findCurveForPlug=path)[0]
        for path in ("ctrl.tx", "ctrl.ty")
    }
    base_curve = maya_cmds.animLayer(
        maya_cmds.animLayer(query=True, root=True),
        query=True,
        findCurveForPlug="ctrl.tx",
    )[0]
    second_curve = maya_cmds.animLayer(
        "Second", query=True, findCurveForPlug="ctrl.tx"
    )[0]
    assert layer.remove_nodes([target]) is None
    assert set(maya_cmds.ls()) == before
    mod.do_it_dg()
    assert _members(maya_cmds, "First") == {"other.translateX"}
    assert not any(maya_cmds.objExists(curve) for curve in first_curves)
    assert maya_cmds.objExists(base_curve)
    assert maya_cmds.objExists(second_curve)
    assert other.tx.keyframe.anim_layer(layer).get_keys() == [(1, 6)]
    after = set(maya_cmds.ls())
    for _ in range(2):
        mod.undo_it()
        assert set(maya_cmds.ls()) == before
        assert len(_members(maya_cmds, "First")) == 4
        mod.redo_it()
        assert set(maya_cmds.ls()) == after
        assert _members(maya_cmds, "First") == {"other.translateX"}


def test_multiple_nodes_and_idempotent_requests(maya_cmds):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    layer.remove_nodes([ctrl, other, "ctrl"])
    mod.do_it_dg()
    assert not _members(maya_cmds, "First")
    assert maya_cmds.objExists("First")
    before = set(maya_cmds.ls())
    layer.remove_nodes([ctrl])
    layer.remove_nodes([])
    mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


def test_pending_registration_is_seen_at_execution(maya_cmds):
    maya_cmds.createNode("transform", name="ctrl")
    maya_cmds.createNode("transform", name="other")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    ctrl = nodes.existing.transform("ctrl")
    other = nodes.existing.transform("other")
    layer = nodes.create.animLayer(name="Correction")
    layer.add_nodes([ctrl])
    layer.add_plugs([other.tx])
    layer.remove_nodes([ctrl])
    mod.do_it_dg()
    assert _members(maya_cmds, "Correction") == {"other.translateX"}
    mod.undo_it()
    assert not maya_cmds.ls(type="animLayer")
    mod.redo_it()
    assert _members(maya_cmds, "Correction") == {"other.translateX"}


def test_pending_dg_node_is_removed_after_registration(maya_cmds):
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    pending = nodes.create.composeMatrix(name="pending")
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs([pending.inputTranslate.inputTranslateX])
    layer.remove_nodes([pending])
    mod.do_it_dg()
    assert not _members(maya_cmds, "Correction")
    mod.undo_it()
    assert not maya_cmds.objExists("pending")


def test_sparse_array_membership_is_removed_without_new_elements(maya_cmds):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    maya_cmds.addAttr(
        "ctrl", longName="samples", attributeType="double", multi=True
    )
    maya_cmds.setAttr("ctrl.samples[3]", 3)
    maya_cmds.setAttr("ctrl.samples[9]", 9)
    maya_cmds.animLayer("First", edit=True, attribute="ctrl.samples[3]")
    layer.remove_nodes([ctrl])
    mod.do_it_dg()
    assert _members(maya_cmds, "First") == {"other.translateX"}
    assert maya_cmds.getAttr("ctrl.samples", multiIndices=True) == [3, 9]


def test_captures_inputs_and_tracks_node_and_layer_renames(maya_cmds):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    targets = ["ctrl"]
    layer.remove_nodes(targets)
    targets.append("other")
    maya_cmds.rename("ctrl", "renamed")
    maya_cmds.rename("First", "RenamedLayer")
    mod.do_it_dg()
    assert _members(maya_cmds, "RenamedLayer") == {"other.translateX"}


def test_node_identity_excludes_same_named_dag_and_children(
    maya_cmds, maya_om
):
    for parent in ("first", "second"):
        maya_cmds.createNode("transform", name=parent)
        maya_cmds.createNode("transform", name="ctrl", parent=parent)
    maya_cmds.createNode("transform", name="child", parent="|first|ctrl")
    layer_name = maya_cmds.animLayer("Correction")
    for path in ("|first|ctrl.tx", "|second|ctrl.tx", "|first|ctrl|child.tx"):
        maya_cmds.animLayer(layer_name, edit=True, attribute=path)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    layer = nodes.existing.animLayer(layer_name)
    layer.remove_nodes(["|first|ctrl"])
    mod.do_it_dg()
    remaining = set()
    for member in _members(maya_cmds, layer_name):
        selection = maya_om.MSelectionList()
        selection.add(member)
        remaining.add(maya_om.MObjectHandle(selection.getPlug(0).node()))
    assert remaining == {
        maya_om.MObjectHandle(nodes.existing.transform("|second|ctrl").m_obj),
        maya_om.MObjectHandle(
            nodes.existing.transform("|first|ctrl|child").m_obj
        ),
    }


@pytest.mark.parametrize("deleted", ["node", "layer"])
def test_deleted_identity_is_not_replaced_by_same_name(maya_cmds, deleted):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    layer.remove_nodes([ctrl])
    if deleted == "node":
        maya_cmds.delete("ctrl")
        maya_cmds.createNode("transform", name="ctrl")
    else:
        maya_cmds.delete("First")
        maya_cmds.animLayer("First", attribute="other.tx")
    before = set(maya_cmds.ls())
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


@pytest.mark.parametrize("locked", ["layer", "node", "plug", "curve"])
def test_readonly_later_node_aborts_entire_batch(maya_cmds, locked):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    if locked == "layer":
        maya_cmds.animLayer("First", edit=True, lock=True)
    elif locked == "node":
        maya_cmds.lockNode("other", lock=True)
    elif locked == "plug":
        maya_cmds.setAttr("other.tx", lock=True)
    else:
        curve = maya_cmds.animLayer(
            "First", query=True, findCurveForPlug="other.tx"
        )[0]
        maya_cmds.lockNode(curve, lock=True)
    before = set(maya_cmds.ls())
    layer.remove_nodes([ctrl, other])
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert len(_members(maya_cmds, "First")) == 4
    assert not mod.can_undo and not mod.can_redo


def test_referenced_node_aborts_entire_batch(maya_cmds, tmp_path):
    maya_cmds.createNode("transform", name="refCtrl")
    path = str(tmp_path / "reference.ma")
    maya_cmds.file(rename=path)
    maya_cmds.file(save=True, type="mayaAscii")
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(path, reference=True, namespace="ref")
    maya_cmds.createNode("transform", name="local")
    layer_name = maya_cmds.animLayer("Correction")
    maya_cmds.animLayer(layer_name, edit=True, attribute="local.tx")
    maya_cmds.animLayer(layer_name, edit=True, attribute="ref:refCtrl.tx")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    layer = nodes.existing.animLayer(layer_name)
    layer.remove_nodes(["local", "ref:refCtrl"])
    before = set(maya_cmds.ls())
    with pytest.raises(RuntimeError, match="referenced"):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert len(_members(maya_cmds, layer_name)) == 2


@pytest.mark.parametrize("mode", ["raise", "skip", "late"])
def test_native_failure_and_late_failure_roll_back(
    maya_cmds, monkeypatch, mode
):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    before = set(maya_cmds.ls())
    native = maya_cmds.animLayer

    def anim_layer(*args, **kwargs):
        if kwargs.get("edit") and kwargs.get("removeAttribute", "").endswith(
            "translateY"
        ):
            if mode == "raise":
                raise RuntimeError("intentional removal failure")
            if mode == "skip":
                return None
        return native(*args, **kwargs)

    monkeypatch.setattr(maya_cmds, "animLayer", anim_layer)
    layer.remove_nodes([ctrl, other])
    if mode == "late":

        def fail(modifier):
            raise RuntimeError("intentional late failure")

        mod.queue_dg_modifier(fail)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert len(_members(maya_cmds, "First")) == 4
    assert not mod.can_undo and not mod.can_redo


def test_invalid_arguments_and_root_are_rejected(maya_cmds):
    mod, nodes, ctrl, other, layer = _setup(maya_cmds)
    for value in (ctrl, ctrl.m_obj, "ctrl", [ctrl.tx], [1]):
        with pytest.raises(TypeError):
            layer.remove_nodes(value)
    root = nodes.existing.animLayer(maya_cmds.animLayer(query=True, root=True))
    root.remove_nodes([ctrl])
    with pytest.raises(RuntimeError, match="base"):
        mod.do_it_dg()
