from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _members(cmds, layer):
    return set(cmds.animLayer(layer, query=True, attribute=True) or ())


def _setup(cmds):
    cmds.createNode("transform", name="ctrl")
    cmds.setKeyframe("ctrl.tx", time=1, value=2)
    first = cmds.animLayer("First", attribute=["ctrl.tx", "ctrl.ty"])
    cmds.setKeyframe("ctrl.tx", animLayer=first, time=1, value=8)
    cmds.setKeyframe("ctrl.ty", animLayer=first, time=1, value=4)
    second = cmds.animLayer("Second", attribute="ctrl.tx")
    cmds.setKeyframe("ctrl.tx", animLayer=second, time=1, value=12)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    return (
        mod,
        nodes,
        nodes.existing.transform("ctrl"),
        nodes.existing.animLayer(first),
    )


@pytest.mark.parametrize("form", ["wrapper", "api", "name"])
def test_remove_preserves_other_layers_and_undo_redo(maya_cmds, form):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
    target = {"wrapper": ctrl.tx, "api": ctrl.tx.plug, "name": "ctrl.tx"}[form]
    before = set(maya_cmds.ls())
    first_curve = maya_cmds.animLayer(
        "First", query=True, findCurveForPlug="ctrl.tx"
    )[0]
    base_curve = maya_cmds.animLayer(
        maya_cmds.animLayer(query=True, root=True),
        query=True,
        findCurveForPlug="ctrl.tx",
    )[0]
    second_curve = maya_cmds.animLayer(
        "Second", query=True, findCurveForPlug="ctrl.tx"
    )[0]
    assert layer.remove_plugs([target]) is None
    assert set(maya_cmds.ls()) == before
    mod.do_it_dg()
    assert _members(maya_cmds, "First") == {"ctrl.translateY"}
    assert not maya_cmds.objExists(first_curve)
    assert maya_cmds.objExists(base_curve)
    assert maya_cmds.objExists(second_curve)
    assert ctrl.ty.keyframe.anim_layer(layer).get_keys()
    after = set(maya_cmds.ls())
    for _ in range(2):
        mod.undo_it()
        assert set(maya_cmds.ls()) == before
        assert _members(maya_cmds, "First") == {
            "ctrl.translateX",
            "ctrl.translateY",
        }
        mod.redo_it()
        assert set(maya_cmds.ls()) == after
        assert _members(maya_cmds, "First") == {"ctrl.translateY"}


def test_compound_array_duplicates_and_unregistered_are_noop(maya_cmds):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
    maya_cmds.addAttr(
        "ctrl", longName="samples", attributeType="double", multi=True
    )
    maya_cmds.setAttr("ctrl.samples[3]", 3)
    maya_cmds.setAttr("ctrl.samples[9]", 9)
    maya_cmds.animLayer("First", edit=True, attribute="ctrl.samples[3]")
    layer.remove_plugs([ctrl.translate, "ctrl.tx", "ctrl.samples", "ctrl.tz"])
    mod.do_it_dg()
    assert not _members(maya_cmds, "First")
    assert maya_cmds.getAttr("ctrl.samples", multiIndices=True) == [3, 9]
    before = set(maya_cmds.ls())
    layer.remove_plugs([ctrl.tz])
    layer.remove_plugs([])
    mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


def test_add_then_remove_in_one_batch(maya_cmds):
    maya_cmds.createNode("transform", name="ctrl")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    ctrl = nodes.existing.transform("ctrl")
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs([ctrl.tx, ctrl.ty])
    layer.remove_plugs([ctrl.tx])
    mod.do_it_dg()
    assert _members(maya_cmds, "Correction") == {"ctrl.translateY"}
    mod.undo_it()
    assert not maya_cmds.ls(type="animLayer")
    mod.redo_it()
    assert _members(maya_cmds, "Correction") == {"ctrl.translateY"}


def test_captures_identity_and_tracks_renames(maya_cmds):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
    targets = ["ctrl.tx"]
    layer.remove_plugs(targets)
    targets.append("ctrl.ty")
    maya_cmds.rename("ctrl", "renamed")
    maya_cmds.rename("First", "RenamedLayer")
    mod.do_it_dg()
    assert _members(maya_cmds, "RenamedLayer") == {"renamed.translateY"}


@pytest.mark.parametrize("deleted", ["node", "layer", "attribute"])
def test_deleted_identity_is_not_replaced(maya_cmds, deleted):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
    layer.remove_plugs([ctrl.tx])
    if deleted == "node":
        maya_cmds.delete("ctrl")
        maya_cmds.createNode("transform", name="ctrl")
    elif deleted == "layer":
        maya_cmds.delete("First")
        maya_cmds.animLayer("First", attribute="ctrl.tx")
    else:
        maya_cmds.addAttr("ctrl", longName="value", attributeType="double")
        maya_cmds.animLayer("First", edit=True, attribute="ctrl.value")
        layer.remove_plugs(["ctrl.value"])
        maya_cmds.deleteAttr("ctrl.value")
        maya_cmds.addAttr("ctrl", longName="value", attributeType="double")
    before = set(maya_cmds.ls())
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


def test_referenced_target_is_rejected_before_removal(maya_cmds, tmp_path):
    maya_cmds.createNode("transform", name="ctrl")
    path = str(tmp_path / "reference.ma")
    maya_cmds.file(rename=path)
    maya_cmds.file(save=True, type="mayaAscii")
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(path, reference=True, namespace="ref")
    maya_cmds.createNode("transform", name="local")
    layer_name = maya_cmds.animLayer("First")
    maya_cmds.animLayer(layer_name, edit=True, attribute="local.tx")
    maya_cmds.animLayer(layer_name, edit=True, attribute="ref:ctrl.tx")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    layer = nodes.existing.animLayer(layer_name)
    layer.remove_plugs(["local.tx", "ref:ctrl.tx"])
    before = set(maya_cmds.ls())
    with pytest.raises(RuntimeError, match="referenced"):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert _members(maya_cmds, layer_name) == {
        "local.translateX",
        "ref:ctrl.translateX",
    }


def test_invalid_arguments_and_root_are_rejected(maya_cmds):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
    for value in (ctrl.tx, ctrl.tx.plug, "ctrl.tx", [ctrl], [1]):
        with pytest.raises(TypeError):
            layer.remove_plugs(value)
    root = nodes.existing.animLayer(maya_cmds.animLayer(query=True, root=True))
    root.remove_plugs([ctrl.tx])
    with pytest.raises(RuntimeError, match="base"):
        mod.do_it_dg()


@pytest.mark.parametrize(
    "locked",
    ["layer", "node", "plug", "curve", "curve_output", "blend_output"],
)
def test_readonly_targets_are_rejected_before_any_removal(maya_cmds, locked):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
    if locked == "layer":
        maya_cmds.animLayer("First", edit=True, lock=True)
    elif locked == "node":
        maya_cmds.lockNode("ctrl", lock=True)
    elif locked == "plug":
        maya_cmds.setAttr("ctrl.ty", lock=True)
    elif locked == "curve":
        curve = maya_cmds.animLayer(
            "First", query=True, findCurveForPlug="ctrl.ty"
        )[0]
        maya_cmds.lockNode(curve, lock=True)
    elif locked == "curve_output":
        curve = maya_cmds.animLayer(
            "First", query=True, findCurveForPlug="ctrl.ty"
        )[0]
        maya_cmds.setAttr(curve + ".output", lock=True)
    else:
        source = maya_cmds.listConnections(
            "ctrl.ty", source=True, destination=False, plugs=True
        )[0]
        maya_cmds.setAttr(source, lock=True)
    before = set(maya_cmds.ls())
    layer.remove_plugs([ctrl.tx, ctrl.ty])
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert _members(maya_cmds, "First") == {
        "ctrl.translateX",
        "ctrl.translateY",
    }
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("mode", ["raise", "skip", "late"])
def test_native_failure_and_late_failure_roll_back(
    maya_cmds, monkeypatch, mode
):
    mod, nodes, ctrl, layer = _setup(maya_cmds)
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
    layer.remove_plugs([ctrl.tx, ctrl.ty])
    if mode == "late":

        def fail(modifier):
            raise RuntimeError("intentional late failure")

        mod.queue_dg_modifier(fail)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert _members(maya_cmds, "First") == {
        "ctrl.translateX",
        "ctrl.translateY",
    }
    assert not mod.can_undo and not mod.can_redo
