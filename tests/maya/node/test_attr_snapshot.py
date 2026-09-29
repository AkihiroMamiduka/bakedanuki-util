from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def test_capture_json_restore_and_undo(maya_cmds, tmp_path):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 4.25)
    cmds.setAttr(source + ".rx", 30)
    cmds.addAttr(source, longName="count", attributeType="long", keyable=True)
    cmds.addAttr(source, longName="label", dataType="string", keyable=True)
    cmds.setAttr(source + ".count", 7)
    cmds.setAttr(source + ".label", "日本語", type="string")
    snapshot = bdu.AttrSnapshot.capture(
        [source], attributes=["tx", "rx", "count", "label"]
    )
    loaded = bdu.AttrSnapshot.load(snapshot.save(tmp_path / "値.json"))
    assert loaded == snapshot
    assert bdu.AttrSnapshot.from_json(snapshot.to_json()) == snapshot
    cmds.delete(source)
    target = cmds.createNode("transform", name="target")
    cmds.addAttr(target, longName="count", attributeType="long", keyable=True)
    cmds.addAttr(target, longName="label", dataType="string", keyable=True)
    mod = bdu.ModifierManager()
    report = loaded.restore(mod, targets=[target])
    assert not report.complete
    mod.do_it_dg()
    assert report.complete and report.applied_count == 4 and not report.skipped
    assert cmds.getAttr(target + ".tx") == pytest.approx(4.25)
    assert cmds.getAttr(target + ".rx") == pytest.approx(30)
    assert cmds.getAttr(target + ".count") == 7
    assert cmds.getAttr(target + ".label") == "日本語"
    mod.undo_it()
    assert cmds.getAttr(target + ".tx") == 0
    assert cmds.getAttr(target + ".count") == 0
    mod.redo_it()
    assert cmds.getAttr(target + ".tx") == pytest.approx(4.25)


def test_capture_display_options_and_explicit_hidden(maya_cmds):
    cmds = maya_cmds
    node = cmds.createNode("transform", name="source")
    cmds.addAttr(node, longName="box", attributeType="double")
    cmds.setAttr(node + ".box", channelBox=True)
    cmds.addAttr(node, longName="invisible", attributeType="double")
    default = bdu.AttrSnapshot.capture([node])
    names = {item.attribute for item in default.nodes[0].attributes}
    assert "translate.translateX" in names or "translateX" in names
    assert "box" in names
    assert "invisible" not in names
    without_box = bdu.AttrSnapshot.capture([node], include_channel_box=False)
    assert "box" not in {
        item.attribute for item in without_box.nodes[0].attributes
    }
    with_hidden = bdu.AttrSnapshot.capture([node], include_hidden=True)
    assert "invisible" in {
        item.attribute for item in with_hidden.nodes[0].attributes
    }
    explicit = bdu.AttrSnapshot.capture([node], attributes=["invisible"])
    assert [item.attribute for item in explicit.nodes[0].attributes] == [
        "invisible"
    ]


def test_connected_skip_and_strict_preflight(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 3)
    cmds.setAttr(source + ".ty", 6)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx", "ty"])
    target = cmds.createNode("transform", name="target")
    driver = cmds.createNode("transform", name="driver")
    cmds.connectAttr(driver + ".tx", target + ".tx")
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target])
    mod.do_it_dg()
    assert report.applied_count == 1
    assert [(item.attribute, item.reason) for item in report.skipped] == [
        ("translate.translateX", "non-animation input connection")
    ] or [(item.attribute, item.reason) for item in report.skipped] == [
        ("translateX", "non-animation input connection")
    ]
    assert cmds.getAttr(target + ".ty") == pytest.approx(6)
    assert cmds.isConnected(driver + ".tx", target + ".tx")
    cmds.setAttr(target + ".ty", 0)
    strict = bdu.ModifierManager()
    snapshot.restore(strict, targets=[target], strict=True)
    with pytest.raises(RuntimeError, match="non-animation input connection"):
        strict.do_it_dg()
    assert cmds.getAttr(target + ".ty") == 0


def test_existing_key_uses_root_and_requested_layer(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 8)
    cmds.setAttr(source + ".ty", 9)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx", "ty"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    cmds.setKeyframe(target + ".tx", time=10, value=0)
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], frame=5)
    mod.do_it_dg()
    assert report.applied_count == 2
    assert cmds.getAttr(target + ".tx", time=5) == pytest.approx(8)
    assert cmds.getAttr(target + ".ty") == pytest.approx(9)
    assert cmds.keyframe(
        target + ".tx", query=True, time=(5, 5), valueChange=True
    ) == pytest.approx([8])
    mod.undo_it()
    assert cmds.getAttr(target + ".tx", time=5) == pytest.approx(0)
    assert cmds.getAttr(target + ".ty") == pytest.approx(0)
    mod.redo_it()
    assert cmds.getAttr(target + ".tx", time=5) == pytest.approx(8)

    cmds.keyframe(target + ".tx", edit=True, time=(5, 5), valueChange=0)
    assert cmds.getAttr(target + ".tx", time=5) == pytest.approx(0)
    layer = cmds.animLayer("PoseLayer")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    cmds.setKeyframe(target + ".tx", time=5, value=0, animLayer=layer)
    mod2 = bdu.ModifierManager()
    report2 = snapshot.restore(
        mod2, targets=[target], frame=5, anim_layer=layer
    )
    mod2.do_it_dg()
    cmds.currentTime(5)
    assert report2.applied_count == 2
    assert cmds.getAttr(target + ".tx") == pytest.approx(8)
    assert cmds.getAttr(target + ".ty") == pytest.approx(9)


def test_invalid_schema(maya_cmds, tmp_path):
    source = maya_cmds.createNode("transform")
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    data = snapshot.to_dict()
    data["schema_version"] = 2
    with pytest.raises(ValueError):
        bdu.AttrSnapshot.from_dict(data)
    data = snapshot.to_dict()
    data["nodes"][0]["attributes"][0]["value"] = float("nan")
    with pytest.raises(ValueError):
        bdu.AttrSnapshot.from_dict(data)


def test_scalar_types_and_existing_array_elements(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("network", name="source")
    cmds.addAttr(source, longName="enabled", attributeType="bool")
    cmds.addAttr(
        source, longName="mode", attributeType="enum", enumName="off:on"
    )
    cmds.addAttr(source, longName="gain", attributeType="float")
    cmds.addAttr(
        source, longName="weights", attributeType="double", multi=True
    )
    cmds.setAttr(source + ".enabled", True)
    cmds.setAttr(source + ".mode", 1)
    cmds.setAttr(source + ".gain", 2.5)
    cmds.setAttr(source + ".weights[2]", 3.5)
    snapshot = bdu.AttrSnapshot.capture(
        [source], attributes=["enabled", "mode", "gain", "weights"]
    )
    assert "weights[2]" in {
        item.attribute for item in snapshot.nodes[0].attributes
    }
    target = cmds.createNode("network", name="target")
    cmds.addAttr(target, longName="enabled", attributeType="bool")
    cmds.addAttr(
        target, longName="mode", attributeType="enum", enumName="off:on"
    )
    cmds.addAttr(target, longName="gain", attributeType="float")
    cmds.addAttr(
        target, longName="weights", attributeType="double", multi=True
    )
    cmds.setAttr(target + ".weights[2]", 0)
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target])
    mod.do_it_dg()
    assert report.applied_count == 4
    assert cmds.getAttr(target + ".enabled") is True
    assert cmds.getAttr(target + ".mode") == 1
    assert cmds.getAttr(target + ".gain") == pytest.approx(2.5)
    assert cmds.getAttr(target + ".weights[2]") == pytest.approx(3.5)


def test_layer_unmembership_skips_key_but_sets_static(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 5)
    cmds.setAttr(source + ".tz", 7)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx", "tz"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    layer = cmds.animLayer("OtherLayer")
    cmds.animLayer(layer, edit=True, attribute=target + ".ty")
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], anim_layer=layer, frame=1)
    mod.do_it_dg()
    assert report.applied_count == 1
    assert (
        report.skipped[0].reason
        == "attribute is not a member of animation layer"
    )
    assert cmds.getAttr(target + ".tx") == pytest.approx(0)
    assert cmds.getAttr(target + ".tz") == pytest.approx(7)


@pytest.mark.parametrize(
    "lock",
    ["node", "output", "keyTimeValue", "ktv[0].kv", "ktl[0]"],
)
def test_locked_destination_curve_skips_only_its_attribute(maya_cmds, lock):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 8)
    cmds.setAttr(source + ".ty", 9)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["ty", "tx"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    curve = cmds.listConnections(
        target + ".tx", source=True, destination=False
    )[0]
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], frame=5)
    if lock == "node":
        cmds.lockNode(curve, lock=True)
    else:
        cmds.setAttr(curve + "." + lock, lock=True)
    mod.do_it_dg()
    assert report.complete and report.applied_count == 1
    assert [(item.attribute, item.reason) for item in report.skipped] == [
        (snapshot.nodes[0].attributes[1].attribute, "locked animation curve")
    ]
    assert cmds.getAttr(target + ".ty") == pytest.approx(9)
    assert cmds.keyframe(curve, query=True, time=(5, 5)) is None
    mod.undo_it()
    assert cmds.getAttr(target + ".ty") == pytest.approx(0)
    mod.redo_it()
    assert cmds.getAttr(target + ".ty") == pytest.approx(9)


def test_locked_destination_curve_strict_fails_before_writing(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 8)
    cmds.setAttr(source + ".ty", 9)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["ty", "tx"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    curve = cmds.listConnections(
        target + ".tx", source=True, destination=False
    )[0]
    cmds.setAttr(curve + ".ktv[0].kv", lock=True)
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], strict=True)
    with pytest.raises(RuntimeError, match="locked animation curve"):
        mod.do_it_dg()
    assert not report.complete
    assert cmds.getAttr(target + ".ty") == pytest.approx(0)
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 1
    assert not mod.can_undo


@pytest.mark.parametrize("target_layer", ["root", "PoseLayer"])
def test_other_layer_curve_lock_does_not_block_restore(
    maya_cmds, target_layer
):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 5)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    layer = cmds.animLayer("PoseLayer")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    cmds.setKeyframe(target + ".tx", time=1, value=0, animLayer=layer)
    root = cmds.animLayer(query=True, root=True)
    protected_layer = layer if target_layer == "root" else root
    protected_curve = cmds.animLayer(
        protected_layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    cmds.setAttr(protected_curve + ".ktv", lock=True)
    kwargs = {} if target_layer == "root" else {"anim_layer": layer}
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], frame=5, **kwargs)
    mod.do_it_dg()
    destination_layer = root if target_layer == "root" else layer
    destination_curve = cmds.animLayer(
        destination_layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    assert report.complete and report.applied_count == 1 and not report.skipped
    assert cmds.keyframe(
        destination_curve, query=True, time=(5, 5), valueChange=True
    ) == pytest.approx([5])


@pytest.mark.parametrize("layered", [False, True])
def test_unrelated_curve_attribute_lock_does_not_block_restore(
    maya_cmds, layered
):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 5)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    layer = None
    if layered:
        layer = cmds.animLayer("PoseLayer")
        cmds.animLayer(layer, edit=True, attribute=target + ".tx")
        cmds.setKeyframe(target + ".tx", time=1, value=0, animLayer=layer)
    curve = (
        cmds.animLayer(layer, query=True, findCurveForPlug=target + ".tx")[0]
        if layer is not None
        else cmds.listConnections(
            target + ".tx", source=True, destination=False
        )[0]
    )
    cmds.addAttr(curve, longName="guard", attributeType="double")
    cmds.setAttr(curve + ".guard", lock=True)
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], frame=5, anim_layer=layer)
    mod.do_it_dg()
    assert report.complete and report.applied_count == 1 and not report.skipped
    assert cmds.keyframe(
        curve, query=True, time=(5, 5), valueChange=True
    ) == pytest.approx([5])


@pytest.mark.parametrize("lock", ["node", "ktv[0].kv"])
def test_locked_selected_layer_curve_skips_only_its_attribute(maya_cmds, lock):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 5)
    cmds.setAttr(source + ".ty", 7)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx", "ty"])
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(target + ".tx", time=1, value=0)
    layer = cmds.animLayer("PoseLayer")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    cmds.setKeyframe(target + ".tx", time=1, value=0, animLayer=layer)
    curve = cmds.animLayer(layer, query=True, findCurveForPlug=target + ".tx")[
        0
    ]
    if lock == "node":
        cmds.lockNode(curve, lock=True)
    else:
        cmds.setAttr(curve + "." + lock, lock=True)
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], frame=5, anim_layer=layer)
    mod.do_it_dg()
    assert report.complete and report.applied_count == 1
    assert [(item.attribute, item.reason) for item in report.skipped] == [
        (snapshot.nodes[0].attributes[0].attribute, "locked animation curve")
    ]
    assert cmds.getAttr(target + ".ty") == pytest.approx(7)
    assert cmds.keyframe(curve, query=True, time=(5, 5)) is None


def test_referenced_destination_curve_skips_only_its_attribute(
    maya_cmds, tmp_path
):
    cmds = maya_cmds
    curve = cmds.createNode("animCurveTL", name="referencedCurve")
    cmds.setKeyframe(curve, time=1, value=0)
    cmds.select(curve)
    curve_file = tmp_path / "curve.ma"
    cmds.file(
        str(curve_file),
        force=True,
        options="v=0;",
        type="mayaAscii",
        exportSelected=True,
    )
    cmds.delete(curve)
    cmds.file(str(curve_file), reference=True, namespace="ref")
    source = cmds.createNode("transform", name="source")
    cmds.setAttr(source + ".tx", 5)
    cmds.setAttr(source + ".ty", 7)
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx", "ty"])
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr("ref:referencedCurve.output", target + ".tx")
    mod = bdu.ModifierManager()
    report = snapshot.restore(mod, targets=[target], frame=5)
    mod.do_it_dg()
    assert report.complete and report.applied_count == 1
    assert [(item.attribute, item.reason) for item in report.skipped] == [
        (
            snapshot.nodes[0].attributes[0].attribute,
            "referenced animation curve",
        )
    ]
    assert cmds.getAttr(target + ".ty") == pytest.approx(7)
    assert (
        cmds.keyframe("ref:referencedCurve", query=True, time=(5, 5)) is None
    )


def test_extract_round_trip_and_restore_in_requested_order(
    maya_cmds, tmp_path
):
    cmds = maya_cmds
    originals = []
    for name, tx, rx in (("a", 1, 10), ("b", 2, 20), ("c", 3, 30)):
        node = cmds.createNode("transform", name=name)
        cmds.setAttr(node + ".tx", tx)
        cmds.setAttr(node + ".rx", rx)
        originals.append(node)
    snapshot = bdu.AttrSnapshot.capture(originals, attributes=["tx", "rx"])
    loaded = bdu.AttrSnapshot.load(snapshot.save(tmp_path / "all.json"))
    cmds.delete(originals)

    part = loaded.extract(nodes=["c", "a"])
    assert part is not loaded
    assert [node.name for node in part.nodes] == ["c", "a"]
    assert [node.name for node in loaded.nodes] == ["a", "b", "c"]
    assert part.nodes[0].attributes == loaded.nodes[2].attributes
    assert part.nodes[1].attributes == loaded.nodes[0].attributes
    assert part.schema_version == loaded.schema_version
    assert bdu.AttrSnapshot.load(part.save(tmp_path / "part.json")) == part

    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    mod = bdu.ModifierManager()
    report = part.restore(mod, targets=[first, second])
    mod.do_it_dg()
    assert report.complete and report.applied_count == 4 and not report.skipped
    assert cmds.getAttr(first + ".tx") == pytest.approx(3)
    assert cmds.getAttr(first + ".rx") == pytest.approx(30)
    assert cmds.getAttr(second + ".tx") == pytest.approx(1)
    assert cmds.getAttr(second + ".rx") == pytest.approx(10)
    mod.undo_it()
    assert cmds.getAttr(first + ".tx") == pytest.approx(0)
    assert cmds.getAttr(second + ".rx") == pytest.approx(0)


def test_extract_resolves_dag_names_and_live_selectors(maya_cmds):
    cmds = maya_cmds
    left_group = cmds.createNode("transform", name="left")
    right_group = cmds.createNode("transform", name="right")
    cmds.createNode("transform", name="ctrl", parent=left_group)
    cmds.createNode("transform", name="ctrl", parent=right_group)
    left = cmds.listRelatives(left_group, children=True, fullPath=True)[0]
    right = cmds.listRelatives(right_group, children=True, fullPath=True)[0]
    snapshot = bdu.AttrSnapshot.capture([left, right], attributes=["tx"])
    assert [node.name for node in snapshot.nodes] == [left, right]
    with pytest.raises(ValueError, match="Ambiguous snapshot node"):
        snapshot.extract(nodes=["ctrl"])
    selected = snapshot.extract(nodes=[right, left])
    assert [node.name for node in selected.nodes] == [right, left]
    nodes = bdu.Nodes()
    selected = snapshot.extract(
        nodes=[nodes.existing(left), nodes.existing(right).m_obj]
    )
    assert [node.name for node in selected.nodes] == [left, right]
    with pytest.raises(ValueError, match="Duplicate snapshot node"):
        snapshot.extract(nodes=[left, nodes.existing(left)])


def test_extract_keeps_namespace_in_short_name(maya_cmds):
    cmds = maya_cmds
    cmds.namespace(add="character")
    source = cmds.createNode("transform", name="character:ctrl")
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    assert snapshot.extract(nodes=["character:ctrl"]).nodes[0].name == (
        "character:ctrl"
    )
    with pytest.raises(ValueError, match="Unknown snapshot node"):
        snapshot.extract(nodes=["ctrl"])
    cmds.namespace(set=":")


def test_extract_rejects_invalid_and_empty_selections(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    saved_name = snapshot.nodes[0].name
    with pytest.raises(TypeError, match="iterable"):
        snapshot.extract(nodes="source")
    with pytest.raises(TypeError, match="iterable"):
        snapshot.extract(nodes=bdu.Nodes().existing(source))
    with pytest.raises(ValueError, match="must not be empty"):
        snapshot.extract(nodes=[])
    with pytest.raises(ValueError, match="Unknown snapshot node"):
        snapshot.extract(nodes=["missing"])
    with pytest.raises(ValueError, match="Duplicate snapshot node"):
        snapshot.extract(nodes=[saved_name, saved_name])

    data = snapshot.to_dict()
    data["nodes"] = ({"name": "empty", "attributes": []}, *data["nodes"])
    with_empty = bdu.AttrSnapshot.from_dict(data)
    with pytest.raises(ValueError, match="contain no attributes"):
        with_empty.extract(nodes=["empty"])
    selected = with_empty.extract(nodes=["empty", saved_name])
    assert [node.name for node in selected.nodes] == ["empty", saved_name]
    assert selected.nodes[0].attributes == ()


def test_extract_named_pending_operator_does_not_run_modifier(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="pendingTarget")
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    cmds.delete(source)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    pending = nodes.create.transform(name="pendingTarget")
    selected = snapshot.extract(nodes=[pending])
    assert [node.name for node in selected.nodes] == ["pendingTarget"]
    assert not cmds.objExists("pendingTarget")
    assert not mod.can_undo
    with pytest.raises(ValueError, match="pending MObject"):
        snapshot.extract(nodes=[pending.m_obj])
    with pytest.raises(ValueError, match="explicit name"):
        snapshot.extract(nodes=[nodes.create.transform()])


def test_extract_rejects_deleted_node_selector(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    snapshot = bdu.AttrSnapshot.capture([source], attributes=["tx"])
    operator = bdu.Nodes().existing(source)
    cmds.delete(source)
    with pytest.raises(ValueError, match="no longer available"):
        snapshot.extract(nodes=[operator])
