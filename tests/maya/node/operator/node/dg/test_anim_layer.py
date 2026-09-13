from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _members(cmds, layer):
    return set(cmds.animLayer(layer, query=True, attribute=True) or ())


def _setup(cmds):
    name = cmds.createNode("transform", name="ctrl")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    return mod, nodes, nodes.existing.transform(name)


@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("existing_root", [False, True])
def test_create_register_and_key_in_one_batch(
    maya_cmds, override, existing_root
):
    mod, nodes, ctrl = _setup(maya_cmds)
    if existing_root:
        maya_cmds.animLayer("Unrelated")
        root = maya_cmds.rename(
            maya_cmds.animLayer(q=True, root=True), "RenamedBase"
        )
    else:
        root = "BaseAnimation"
    before = set(maya_cmds.ls())
    layer = nodes.create.animLayer(name="Correction", override=override)
    layer.weight.set(0.5)
    layer.add_plugs([ctrl.translate])
    keyframe = ctrl.ty.keyframe.anim_layer(layer)
    keyframe.set_key(12, frame=3)
    assert set(maya_cmds.ls()) == before
    with pytest.raises(RuntimeError, match="not available"):
        keyframe.get_keys()
    mod.do_it_dg()
    assert maya_cmds.animLayer("Correction", q=True, parent=True) == root
    assert maya_cmds.getAttr(root + ".override") is True
    assert maya_cmds.getAttr("Correction.override") is override
    assert maya_cmds.getAttr("Correction.weight") == 0.5
    assert _members(maya_cmds, "Correction") == {
        "ctrl.translate" + axis for axis in "XYZ"
    }
    expected = keyframe.get_curve_data()
    assert expected is not None
    maya_cmds.currentTime(3)
    assert maya_cmds.getAttr("ctrl.ty") == pytest.approx(12)
    after = set(maya_cmds.ls())
    for _ in range(2):
        mod.undo_it()
        assert set(maya_cmds.ls()) == before
        mod.redo_it()
        assert set(maya_cmds.ls()) == after
        assert keyframe.get_curve_data() == expected
        maya_cmds.currentTime(3)
        assert maya_cmds.getAttr("ctrl.ty") == pytest.approx(12)


@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("channel", ["translateY", "rotateZ", "scaleX"])
def test_created_layer_matches_native_values(maya_cmds, override, channel):
    mod, nodes, ctrl = _setup(maya_cmds)
    control = maya_cmds.createNode("transform", name="control")
    for name in ("ctrl", control):
        maya_cmds.setKeyframe(name + "." + channel, time=1, value=4)
    layer = nodes.create.animLayer(name="Correction", override=override)
    layer.weight.set(0.75)
    layer.add_plugs(["ctrl." + channel])
    keyframe = getattr(ctrl, channel).keyframe.anim_layer(layer)
    keyframe.set_key(16, frame=1)
    mod.do_it_dg()
    native = maya_cmds.animLayer("Native", override=override)
    maya_cmds.setAttr(native + ".weight", 0.75)
    maya_cmds.animLayer(native, edit=True, attribute=control + "." + channel)
    maya_cmds.setKeyframe(
        control + "." + channel, animLayer=native, time=1, value=16
    )
    expected = getattr(
        nodes.existing.transform(control), channel
    ).keyframe.anim_layer(native)
    assert keyframe.get_keys() == pytest.approx(expected.get_keys())
    assert maya_cmds.animLayer(
        "Correction", q=True, override=True
    ) == maya_cmds.animLayer(native, q=True, override=True)


def test_multiple_layers_share_root_and_preserve_selection(maya_cmds):
    mod, nodes, ctrl = _setup(maya_cmds)
    unrelated = maya_cmds.animLayer("Unrelated")
    maya_cmds.animLayer(unrelated, edit=True, selected=True, preferred=True)
    maya_cmds.select("ctrl")
    selected = maya_cmds.ls(selection=True, long=True)
    first = nodes.create.animLayer(name="First")
    second = nodes.create.animLayer(name="Second")
    first.add_nodes([ctrl])
    second.add_plugs([ctrl.tx])
    mod.do_it_dg()
    root = maya_cmds.animLayer(q=True, root=True)
    assert set(maya_cmds.animLayer(root, q=True, children=True)) == {
        unrelated,
        "First",
        "Second",
    }
    assert maya_cmds.ls(selection=True, long=True) == selected
    assert maya_cmds.animLayer(unrelated, q=True, selected=True)
    assert maya_cmds.animLayer(unrelated, q=True, preferred=True)


def test_generic_creator_and_name_collision(maya_cmds):
    mod, nodes, ctrl = _setup(maya_cmds)
    maya_cmds.createNode("network", name="BaseAnimation")
    first = nodes.create.create("animLayer", name="First")
    second = nodes.create.animLayer(name="Second")
    second.add_plugs([ctrl.tx])
    mod.do_it_dg()
    root = maya_cmds.animLayer(q=True, root=True)
    assert root != "BaseAnimation"
    assert (
        maya_cmds.animLayer(first.fn_node.name(), q=True, parent=True) == root
    )
    assert maya_cmds.animLayer("Second", q=True, parent=True) == root


@pytest.mark.parametrize("kind", ["wrapper", "api", "name"])
def test_membership_accepts_plug_and_node_forms(maya_cmds, kind):
    mod, nodes, ctrl = _setup(maya_cmds)
    layer = nodes.create.animLayer(name="Correction")
    plug = {"wrapper": ctrl.tx, "api": ctrl.tx.plug, "name": "ctrl.tx"}[kind]
    node = {"wrapper": ctrl, "api": ctrl.m_obj, "name": "ctrl"}[kind]
    layer.add_plugs([plug])
    layer.add_nodes([node])
    mod.do_it_dg()
    assert _members(maya_cmds, "Correction") == {
        "ctrl." + attr
        for attr in (
            "translateX",
            "translateY",
            "translateZ",
            "rotateX",
            "rotateY",
            "rotateZ",
            "scaleX",
            "scaleY",
            "scaleZ",
            "visibility",
        )
    }


@pytest.mark.parametrize("explicit_element", [False, True])
def test_compounds_sparse_arrays_and_nonkeyable_plugs(
    maya_cmds, explicit_element
):
    mod, nodes, ctrl = _setup(maya_cmds)
    maya_cmds.addAttr(
        "ctrl", longName="samples", attributeType="double", multi=True
    )
    maya_cmds.setAttr("ctrl.samples[3]", 3)
    maya_cmds.setAttr("ctrl.samples[9]", 9)
    maya_cmds.addAttr("ctrl", longName="displayOnly", attributeType="double")
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs(
        [
            ctrl.translate,
            "ctrl.displayOnly",
            "ctrl.samples[3]" if explicit_element else "ctrl.samples",
        ]
    )
    mod.do_it_dg()
    assert _members(maya_cmds, "Correction") == {
        "ctrl.translateX",
        "ctrl.translateY",
        "ctrl.translateZ",
        "ctrl.displayOnly",
        "ctrl.samples[3]",
    } | (set() if explicit_element else {"ctrl.samples[9]"})
    assert maya_cmds.getAttr("ctrl.samples", multiIndices=True) == [3, 9]
    assert not maya_cmds.getAttr("ctrl.displayOnly", keyable=True)


def test_add_nodes_matches_native_own_keyable_attributes(maya_cmds):
    mod, nodes, ctrl = _setup(maya_cmds)
    maya_cmds.createNode("transform", name="child", parent="ctrl")
    maya_cmds.createNode("mesh", name="shape", parent="ctrl")
    for name, kind in (
        ("dynamic", "double"),
        ("toggle", "bool"),
        ("count", "long"),
    ):
        maya_cmds.addAttr(
            "ctrl", longName=name, attributeType=kind, keyable=True
        )
    maya_cmds.addAttr(
        "ctrl",
        longName="mode",
        attributeType="enum",
        enumName="a:b",
        keyable=True,
    )
    maya_cmds.addAttr("ctrl", longName="displayOnly", attributeType="double")
    maya_cmds.setAttr("ctrl.displayOnly", channelBox=True)
    maya_cmds.addAttr(
        "ctrl",
        longName="samples",
        attributeType="double",
        multi=True,
        keyable=True,
    )
    maya_cmds.setAttr("ctrl.samples[9]", 3)
    maya_cmds.setAttr("ctrl.ty", lock=True)
    maya_cmds.setKeyframe("ctrl.tx", time=1, value=7)
    original = ctrl.tx.keyframe.get_curve_data()
    layer = nodes.create.animLayer(name="Correction")
    layer.add_nodes([ctrl])
    mod.do_it_dg()
    actual = _members(maya_cmds, "Correction")
    assert {
        "ctrl.dynamic",
        "ctrl.mode",
        "ctrl.toggle",
        "ctrl.count",
        "ctrl.samples[9]",
    } <= actual
    assert "ctrl.translateY" not in actual
    assert "ctrl.displayOnly" not in actual
    assert all(plug.startswith("ctrl.") for plug in actual)
    assert ctrl.tx.keyframe.get_curve_data() == original
    maya_cmds.select("ctrl")
    native = maya_cmds.animLayer("Native", addSelectedObjects=True)
    assert actual == _members(maya_cmds, native)


def test_duplicates_and_empty_arrays_do_not_change_graph(maya_cmds):
    mod, nodes, ctrl = _setup(maya_cmds)
    maya_cmds.addAttr(
        "ctrl", longName="samples", attributeType="double", multi=True
    )
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs([ctrl.tx, "ctrl.translateX", "|ctrl.tx", "ctrl.samples"])
    mod.do_it_dg()
    before = set(maya_cmds.ls())
    layer.add_plugs([ctrl.tx])
    layer.add_plugs([])
    layer.add_nodes([])
    mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert _members(maya_cmds, "Correction") == {"ctrl.translateX"}
    assert maya_cmds.getAttr("ctrl.samples", multiIndices=True) is None


def test_membership_captures_identity_and_copies_inputs(maya_cmds):
    mod, nodes, ctrl = _setup(maya_cmds)
    name = maya_cmds.animLayer("Correction")
    layer = nodes.existing.animLayer(name)
    targets = ["ctrl.tx"]
    layer.add_plugs(targets)
    targets.append("ctrl.ty")
    maya_cmds.rename("ctrl", "renamed")
    maya_cmds.rename(name, "RenamedLayer")
    mod.do_it_dg()
    assert _members(maya_cmds, "RenamedLayer") == {"renamed.translateX"}
    ctrl.tx.keyframe.anim_layer(layer).set_key(5, frame=1)
    mod.do_it_dg()
    assert ctrl.tx.keyframe.anim_layer(layer).get_keys() == [(1, 5)]


@pytest.mark.parametrize("method", ["add_plugs", "add_nodes"])
def test_deleted_target_is_not_replaced_by_same_name(maya_cmds, method):
    mod, nodes, ctrl = _setup(maya_cmds)
    layer = nodes.create.animLayer(name="Correction")
    getattr(layer, method)(["ctrl.tx" if method == "add_plugs" else "ctrl"])
    maya_cmds.delete("ctrl")
    maya_cmds.createNode("transform", name="ctrl")
    with pytest.raises(RuntimeError, match="not available"):
        mod.do_it_dg()
    assert not maya_cmds.ls(type="animLayer")


@pytest.mark.parametrize("plug", ["message", "matrix", "translate"])
def test_invalid_explicit_membership_rolls_back_creation(maya_cmds, plug):
    mod, nodes, ctrl = _setup(maya_cmds)
    if plug == "translate":
        maya_cmds.setAttr("ctrl.ty", lock=True)
    before = set(maya_cmds.ls())
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs(["ctrl." + plug])
    with pytest.raises((RuntimeError, TypeError)):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("target", ["layer", "node", "base"])
def test_existing_readonly_or_base_layer_is_rejected(maya_cmds, target):
    mod, nodes, ctrl = _setup(maya_cmds)
    name = maya_cmds.animLayer("Correction")
    if target == "layer":
        maya_cmds.animLayer(name, edit=True, lock=True)
    elif target == "node":
        maya_cmds.lockNode("ctrl", lock=True)
    else:
        name = maya_cmds.animLayer(q=True, root=True)
    layer = nodes.existing.animLayer(name)
    layer.add_plugs([ctrl.tx])
    before = set(maya_cmds.ls())
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


def test_node_enumeration_observes_earlier_queued_changes(maya_cmds):
    mod, nodes, ctrl = _setup(maya_cmds)
    layer = nodes.create.animLayer(name="Correction")
    mod.dg_mod.pythonCommandToExecute(
        lambda: maya_cmds.setAttr("ctrl.tx", keyable=False)
    )
    mod.dg_mod.pythonCommandToExecute(
        lambda: maya_cmds.setAttr("ctrl.ty", lock=True)
    )
    mod.dg_mod.pythonCommandToExecute(
        lambda: maya_cmds.addAttr(
            "ctrl", longName="late", attributeType="double", keyable=True
        )
    )
    layer.add_nodes([ctrl])
    mod.do_it_dg()
    members = _members(maya_cmds, "Correction")
    assert (
        "ctrl.translateX" not in members and "ctrl.translateY" not in members
    )
    assert "ctrl.late" in members
    mod.undo_it()
    assert maya_cmds.getAttr("ctrl.tx", keyable=True)
    assert not maya_cmds.getAttr("ctrl.ty", lock=True)
    assert not maya_cmds.objExists("ctrl.late")


def test_pending_dg_node_membership(maya_cmds):
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    ctrl = nodes.create.composeMatrix(name="pending")
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs([ctrl.inputTranslate])
    keyframe = ctrl.inputTranslate.inputTranslateX.keyframe.anim_layer(layer)
    keyframe.set_key(8, frame=1)
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1, 8)]
    mod.undo_it()
    assert not maya_cmds.objExists("pending")
    assert not maya_cmds.ls(type="animLayer")


@pytest.mark.parametrize("method", ["add_plugs", "add_nodes"])
def test_pending_dynamic_attribute_membership(maya_cmds, maya_om, method):
    mod, nodes, ctrl = _setup(maya_cmds)
    attribute = maya_om.MFnNumericAttribute().create(
        "pending", "pnd", maya_om.MFnNumericData.kDouble, 0.0
    )
    maya_om.MFnAttribute(attribute).keyable = True
    mod.dg_mod.addAttribute(ctrl.m_obj, attribute)
    layer = nodes.create.animLayer(name="Correction")
    getattr(layer, method)(
        [maya_om.MPlug(ctrl.m_obj, attribute)]
        if method == "add_plugs"
        else [ctrl]
    )
    mod.do_it_dg()
    assert "ctrl.pending" in _members(maya_cmds, "Correction")
    mod.undo_it()
    assert not maya_cmds.objExists("ctrl.pending")
    mod.redo_it()
    assert "ctrl.pending" in _members(maya_cmds, "Correction")


@pytest.mark.parametrize("kind", ["byte", "char"])
def test_unsupported_numeric_attributes_are_skipped_only_for_add_nodes(
    maya_cmds, kind
):
    mod, nodes, ctrl = _setup(maya_cmds)
    maya_cmds.addAttr(
        "ctrl", longName="unsupported", attributeType=kind, keyable=True
    )
    layer = nodes.create.animLayer(name="Correction")
    layer.add_nodes([ctrl])
    mod.do_it_dg()
    assert "ctrl.unsupported" not in _members(maya_cmds, "Correction")
    before = set(maya_cmds.ls())
    layer.add_plugs(["ctrl.unsupported"])
    with pytest.raises(TypeError, match="Unsupported"):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


@pytest.mark.parametrize("deleted", ["layer", "attribute"])
def test_deleted_membership_identity_is_not_reused(maya_cmds, deleted):
    mod, nodes, ctrl = _setup(maya_cmds)
    maya_cmds.addAttr("ctrl", longName="value", attributeType="double")
    name = maya_cmds.animLayer("Correction")
    layer = nodes.existing.animLayer(name)
    layer.add_plugs(["ctrl.value"])
    if deleted == "layer":
        maya_cmds.delete(name)
        maya_cmds.animLayer(name)
    else:
        maya_cmds.deleteAttr("ctrl.value")
        maya_cmds.addAttr("ctrl", longName="value", attributeType="double")
    with pytest.raises(RuntimeError, match="not available"):
        mod.do_it_dg()
    assert not _members(maya_cmds, name)


@pytest.mark.parametrize("method", ["add_plugs", "add_nodes"])
def test_referenced_nodes_reject_membership(maya_cmds, tmp_path, method):
    maya_cmds.createNode("transform", name="ctrl")
    path = str(tmp_path / "reference.ma")
    maya_cmds.file(rename=path)
    maya_cmds.file(save=True, type="mayaAscii")
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(path, reference=True, namespace="ref")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    layer = nodes.create.animLayer(name="Correction")
    getattr(layer, method)(
        ["ref:ctrl.tx" if method == "add_plugs" else "ref:ctrl"]
    )
    before = set(maya_cmds.ls())
    with pytest.raises(RuntimeError, match="referenced"):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before


def test_duplicate_dag_names_register_only_the_specified_node(maya_cmds):
    for parent in ("first", "second"):
        maya_cmds.createNode("transform", name=parent)
        maya_cmds.createNode("transform", name="ctrl", parent=parent)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    layer = nodes.create.animLayer(name="Correction")
    layer.add_plugs(["|first|ctrl.tx"])
    mod.do_it_dg()
    assert maya_cmds.listConnections("|first|ctrl.tx", source=True)
    assert not maya_cmds.listConnections("|second|ctrl.tx", source=True)


@pytest.mark.parametrize("mode", ["raise", "skip", "late"])
@pytest.mark.parametrize("existing_layer", [False, True])
def test_native_failure_or_skipped_registration_rolls_back(
    maya_cmds, monkeypatch, mode, existing_layer
):
    mod, nodes, ctrl = _setup(maya_cmds)
    if existing_layer:
        name = maya_cmds.animLayer("Correction", attribute="ctrl.tz")
        layer = nodes.existing.animLayer(name)
    else:
        layer = nodes.create.animLayer(name="Correction")
    before = set(maya_cmds.ls())
    native = maya_cmds.animLayer

    def anim_layer(*args, **kwargs):
        if kwargs.get("edit") and kwargs.get("attribute", "").endswith(
            "translateY"
        ):
            if mode == "raise":
                raise RuntimeError("intentional registration failure")
            if mode == "skip":
                return None
        return native(*args, **kwargs)

    monkeypatch.setattr(maya_cmds, "animLayer", anim_layer)
    layer.add_plugs([ctrl.tx, ctrl.ty])
    if mode == "late":

        def fail(modifier):
            raise RuntimeError("intentional late failure")

        mod.queue_dg_modifier(fail)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == before
    if existing_layer:
        assert _members(maya_cmds, "Correction") == {"ctrl.translateZ"}
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize(
    "kwargs",
    [{"override": 1}, {"name": ""}, {"name": "bad.name"}, {"name": "*"}],
)
def test_invalid_create_arguments_do_not_queue_work(maya_cmds, kwargs):
    mod, nodes, ctrl = _setup(maya_cmds)
    with pytest.raises((TypeError, ValueError)):
        nodes.create.animLayer(**kwargs)
    mod.do_it_dg()
    assert not maya_cmds.ls(type="animLayer")


@pytest.mark.parametrize(
    "method, value",
    [
        ("add_plugs", "ctrl.tx"),
        ("add_nodes", "ctrl"),
        ("add_plugs", [1]),
        ("add_nodes", [1]),
    ],
)
def test_invalid_membership_arguments(maya_cmds, method, value):
    mod, nodes, ctrl = _setup(maya_cmds)
    name = maya_cmds.animLayer("Correction")
    layer = nodes.existing.animLayer(name)
    with pytest.raises(TypeError):
        getattr(layer, method)(value)
    mod.do_it_dg()
    assert not _members(maya_cmds, name)
