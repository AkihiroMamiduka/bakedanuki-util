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
