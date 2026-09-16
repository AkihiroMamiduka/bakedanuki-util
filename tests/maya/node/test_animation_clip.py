from __future__ import annotations

from dataclasses import replace

import pytest

import bd_util as bdu
from bd_util.maya.node.animation_clip import AnimationClip

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _node(cmds, name, keys=((1, 2), (5, 10)), attr="tx"):
    node = cmds.createNode("transform", name=name)
    for frame, value in keys:
        cmds.setKeyframe(
            node + "." + attr,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )
    return node


def _values(cmds, plug, frames=(1, 3, 5)):
    return [cmds.getAttr(plug, time=frame) for frame in frames]


def _layer(cmds, node, name="Upper", *, override=False, weight=1):
    layer = cmds.animLayer(name, override=override)
    cmds.animLayer(layer, edit=True, attribute=node + ".tx")
    for frame, value in ((1, 3), (5, 7)):
        cmds.setKeyframe(
            node + ".tx",
            animLayer=layer,
            time=frame,
            value=value,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    cmds.setAttr(layer + ".weight", weight)
    return layer


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("mode", ["merge", "replace_all", "replace_range"])
def test_roundtrip_and_history(maya_cmds, layer_mode, mode):
    cmds = maya_cmds
    source = _node(cmds, "source")
    target = _node(cmds, "target", ((-1, -4), (3, 100), (7, 20)))
    before = cmds.keyframe(target + ".tx", query=True, valueChange=True)
    clip = AnimationClip.capture(
        [source], attributes=["tx", "ty"], layer_mode=layer_mode
    )
    assert AnimationClip.from_json(clip.to_json()) == clip
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode=mode)
    assert (
        cmds.keyframe(target + ".tx", query=True, valueChange=True) == before
    )
    mod.do_it_dg()
    frames = cmds.keyframe(target + ".tx", query=True, timeChange=True)
    if mode == "replace_all":
        assert min(frames) == 1 and max(frames) == 5
    else:
        assert -1 in frames and 7 in frames
    if mode != "merge" or layer_mode == "flatten":
        assert _values(cmds, target + ".tx") == pytest.approx([2, 6, 10])
    assert _values(cmds, target + ".ty") == [0, 0, 0]
    after = cmds.keyframe(target + ".tx", query=True, valueChange=True)
    for _ in range(2):
        mod.undo_it()
        assert (
            cmds.keyframe(target + ".tx", query=True, valueChange=True)
            == before
        )
        mod.redo_it()
        assert (
            cmds.keyframe(target + ".tx", query=True, valueChange=True)
            == after
        )


def test_auto_attributes_and_explicit_nonkeyable(maya_cmds):
    cmds = maya_cmds
    node = _node(cmds, "source")
    cmds.addAttr(node, longName="shown", attributeType="double")
    cmds.setAttr(node + ".shown", channelBox=True)
    cmds.addAttr(node, longName="hiddenValue", attributeType="double")

    def names(**kwargs):
        return {
            ch.attribute
            for ch in AnimationClip.capture([node], **kwargs).nodes[0].channels
        }

    assert "shown" not in names()
    assert "shown" in names(include_channel_box=True)
    assert "hiddenValue" not in names(include_channel_box=True)
    assert names(attributes=["hiddenValue"], start_frame=1, end_frame=5) == {
        "hiddenValue"
    }
    assert names(attributes=["translate"]) == {
        "translate.translateX",
        "translate.translateY",
        "translate.translateZ",
    }


@pytest.mark.parametrize(
    "override,weight", [(False, 1), (False, 0.5), (True, 0.5)]
)
def test_flatten_resolves_existing_layers(maya_cmds, override, weight):
    cmds = maya_cmds
    source = _node(cmds, "source")
    target = _node(cmds, "target")
    layer = _layer(cmds, target, override=override, weight=weight)
    layer_curve = cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    before = cmds.keyframe(layer_curve, query=True, valueChange=True)
    clip = AnimationClip.capture([source], attributes=["tx"])
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_range")
    mod.do_it_dg()
    assert _values(cmds, target + ".tx") == pytest.approx([2, 6, 10])
    assert cmds.keyframe(layer_curve, query=True, valueChange=True) == before


def test_unresolvable_layer_rolls_back_other_nodes(maya_cmds):
    cmds = maya_cmds
    src = _node(cmds, "src")
    src2 = _node(cmds, "src2")
    dst = _node(cmds, "dst", ((1, -2), (5, -8)))
    dst2 = _node(cmds, "dst2")
    _layer(cmds, dst2, override=True)
    before = cmds.keyframe(dst + ".tx", query=True, valueChange=True)
    clip = AnimationClip.capture([src, src2], attributes=["tx"])
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[dst, dst2], mode="replace_all")
    with pytest.raises(RuntimeError, match="Cannot resolve clip value"):
        mod.do_it_dg()
    assert cmds.keyframe(dst + ".tx", query=True, valueChange=True) == before
    assert not mod.can_undo


def test_preserve_layers_recreate_and_undo(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source")
    layer = _layer(cmds, source, weight=0.5)
    cmds.setKeyframe(layer + ".weight", time=1, value=0.5)
    cmds.setKeyframe(layer + ".weight", time=5, value=0.75)
    expected = _values(cmds, source + ".tx")
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    cmds.file(new=True, force=True)
    target = _node(cmds, "source", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, target + ".tx") == pytest.approx(expected)
    assert cmds.objExists("Upper")
    mod.undo_it()
    assert not cmds.objExists("Upper")
    assert not cmds.objExists("BaseAnimation")
    mod.redo_it()
    assert _values(cmds, target + ".tx") == pytest.approx(expected)


def test_layer_conflict_requires_explicit_setting_replacement(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source")
    layer = _layer(cmds, source, weight=0.5)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    cmds.setAttr(layer + ".weight", 0.25)
    mod = bdu.ModifierManager()
    clip.restore(mod)
    with pytest.raises(ValueError, match="settings differ"):
        mod.do_it_dg()
    assert cmds.getAttr(layer + ".weight") == 0.25
    clip.restore(mod, restore_layer_settings=True)
    mod.do_it_dg()
    assert cmds.getAttr(layer + ".weight") == 0.5
    mod.undo_it()
    assert cmds.getAttr(layer + ".weight") == 0.25


def test_namespace_mapping_and_ordered_targets(maya_cmds):
    cmds = maya_cmds
    cmds.namespace(add="old")
    cmds.namespace(add="new")
    a = _node(cmds, "old:a")
    b = _node(cmds, "old:b", ((1, 20), (5, 40)))
    ta = _node(cmds, "new:a", ())
    tb = _node(cmds, "new:b", ())
    clip = AnimationClip.capture([b, a], attributes=["tx"])
    mod = bdu.ModifierManager()
    clip.restore(mod, namespace="new")
    mod.do_it_dg()
    assert _values(cmds, ta + ".tx") == pytest.approx([2, 6, 10])
    assert _values(cmds, tb + ".tx") == pytest.approx([20, 30, 40])
    mod.undo_it()
    clip.restore(mod, targets=[ta, tb])
    mod.do_it_dg()
    assert _values(cmds, ta + ".tx") == pytest.approx([20, 30, 40])


def test_static_range_and_subframes(maya_cmds):
    cmds = maya_cmds
    node = _node(cmds, "source", ())
    cmds.setAttr(node + ".tx", 7)
    with pytest.raises(ValueError, match="Explicit start_frame"):
        AnimationClip.capture([node], attributes=["tx"])
    clip = AnimationClip.capture(
        [node],
        attributes=["tx"],
        start_frame=-1.5,
        end_frame=0.3,
        sample_by=0.5,
    )
    assert [
        key.frame for key in clip.nodes[0].channels[0].curve.keys
    ] == pytest.approx([-1.5, -1, -0.5, 0, 0.3])
    assert {key.value for key in clip.nodes[0].channels[0].curve.keys} == {7}


def test_capture_leaves_pending_edits_and_scene_state(maya_cmds):
    cmds = maya_cmds
    node = _node(cmds, "source")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    nodes.existing.transform(node).tx.keyframe.set_key(999, 3)
    cmds.currentTime(17)
    cmds.select(node)
    cmds.flushUndo()
    cmds.file(modified=False)
    clip = AnimationClip.capture([node], attributes=["tx"])
    assert clip.nodes[0].channels[0].curve.keys[2].value == pytest.approx(6)
    assert cmds.currentTime(query=True) == 17
    assert cmds.ls(selection=True) == [node]
    assert not cmds.file(query=True, modified=True)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert not mod.can_undo


def test_json_validation_and_booking_copy(maya_cmds):
    node = _node(maya_cmds, "source")
    clip = AnimationClip.capture([node], attributes=["tx"])
    bad = clip.to_dict()
    bad["schema_version"] = 1
    with pytest.raises(ValueError, match="schema_version"):
        AnimationClip.from_dict(bad)
    target = _node(maya_cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target])
    clip.nodes[0].channels[0].curve.keys[0].value = 200
    mod.do_it_dg()
    assert maya_cmds.getAttr(target + ".tx", time=1) == pytest.approx(2)


@pytest.mark.parametrize("mutation", ["lock", "delete", "type"])
def test_preflight_does_not_partially_restore(maya_cmds, mutation):
    cmds = maya_cmds
    source = _node(cmds, "source")
    a = _node(cmds, "a")
    b = _node(cmds, "b")
    clip = AnimationClip.capture([source, a], attributes=["tx"])
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[a, b])
    if mutation == "lock":
        cmds.setAttr(b + ".tx", lock=True)
    elif mutation == "delete":
        cmds.delete(b)
        _node(cmds, "b")
    else:
        cmds.lockNode(b, lock=True)
    before = cmds.keyframe(a + ".tx", query=True, valueChange=True)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert cmds.keyframe(a + ".tx", query=True, valueChange=True) == before


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "attr", ["tx", "rx", "sx", "visibility", "rotateOrder"]
)
def test_channel_units_and_discrete_types(maya_cmds, layer_mode, attr):
    cmds = maya_cmds
    source = _node(cmds, "source", ((1, 0), (5, 1)), attr=attr)
    clip = AnimationClip.capture(
        [source], attributes=[attr], layer_mode=layer_mode
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, target + "." + attr) == pytest.approx(
        _values(cmds, source + "." + attr)
    )


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_cross_fps_and_ui_units(maya_cmds, layer_mode):
    cmds = maya_cmds
    cmds.currentUnit(time="film", linear="m", angle="rad")
    try:
        source = _node(cmds, "source", ((-12, 1), (24, 2)))
        clip = AnimationClip.capture(
            [source], attributes=["tx"], layer_mode=layer_mode
        )
        target = _node(cmds, "target", ())
        mod = bdu.ModifierManager()
        clip.restore(mod, targets=[target], mode="replace_all")
        cmds.currentUnit(time="ntsc", linear="mm", angle="deg")
        mod.do_it_dg()
        assert cmds.keyframe(target + ".tx", query=True, timeChange=True)[
            :: len(clip.nodes[0].channels[0].curve.keys) - 1
        ] == pytest.approx([-15, 30])
        assert _values(cmds, target + ".tx", (-15, 30)) == pytest.approx(
            [1000, 2000]
        )
    finally:
        cmds.currentUnit(time="film", linear="cm", angle="deg")


def test_preserve_reuses_animated_layer_without_settings_override(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source")
    layer = _layer(cmds, source)
    cmds.setKeyframe(layer + ".weight", time=1, value=0.25)
    cmds.setKeyframe(layer + ".weight", time=5, value=0.75)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, target + ".tx") == pytest.approx(
        _values(cmds, source + ".tx")
    )


@pytest.mark.parametrize(
    "setting,value", [("weight", 0.5), ("mute", True), ("solo", True)]
)
def test_root_layer_settings_roundtrip(maya_cmds, setting, value):
    cmds = maya_cmds
    source = _node(cmds, "source")
    _layer(cmds, source)
    root = cmds.animLayer(query=True, root=True)
    cmds.setAttr(root + "." + setting, value)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    expected = _values(cmds, source + ".tx")
    cmds.file(new=True, force=True)
    target = _node(cmds, "source", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, target + ".tx") == pytest.approx(expected)
    mod.undo_it()
    assert not cmds.ls(type="animLayer")
    mod.redo_it()
    assert _values(cmds, target + ".tx") == pytest.approx(expected)


def test_subset_layers_capture_ancestors_without_their_channels(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source", ((-10, 2), (100, 4)))
    parent = cmds.animLayer("Parent")
    child = _layer(cmds, source, "Child")
    cmds.animLayer(child, edit=True, parent=parent)
    other = _layer(cmds, source, "Other")
    cmds.setKeyframe(source + ".tx", time=200, value=4, animLayer=other)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve", layers=[child]
    )
    assert [layer.name for layer in clip.layers] == [parent, child]
    assert clip.layers[1].parent == parent
    assert {ch.layer for ch in clip.nodes[0].channels} == {child}
    assert (clip.start_frame, clip.end_frame) == (1, 5)
    cmds.file(new=True, force=True)
    target = _node(cmds, "source", ())
    mod = bdu.ModifierManager()
    clip.restore(mod)
    mod.do_it_dg()
    assert cmds.animLayer("Child", query=True, parent=True) == "Parent"
    assert "Other" not in cmds.ls(type="animLayer")


def test_layer_order_conflict_and_explicit_reordering(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source")
    a = _layer(cmds, source, "A")
    b = _layer(cmds, source, "B", override=True, weight=0.5)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    root = cmds.animLayer(query=True, root=True)
    cmds.animLayer(b, edit=True, moveLayerBefore=a)
    mod = bdu.ModifierManager()
    clip.restore(mod)
    with pytest.raises(ValueError, match="order differs"):
        mod.do_it_dg()
    clip.restore(mod, restore_layer_settings=True)
    mod.do_it_dg()
    assert cmds.animLayer(root, query=True, children=True) == [a, b]
    mod.undo_it()
    assert cmds.animLayer(root, query=True, children=True) == [b, a]


def test_new_layers_and_keys_rollback_on_late_failure(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source")
    _layer(cmds, source)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    cmds.file(new=True, force=True)
    target = _node(cmds, "source", ())
    mod = bdu.ModifierManager()
    clip.restore(mod)

    def fail(modifier):
        raise RuntimeError("later failure")

    mod.queue_dg_modifier(fail)
    before = set(cmds.ls())
    with pytest.raises(RuntimeError, match="later failure"):
        mod.do_it_dg()
    assert set(cmds.ls()) == before
    assert not cmds.keyframe(target + ".tx", query=True, timeChange=True)


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_restore_after_pending_node_creation_and_rename(maya_cmds, layer_mode):
    source = _node(maya_cmds, "source")
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    target = nodes.create.multiplyDivide(name="target")
    # Reuse a compatible scalar destination through the editable clip data.
    channel = clip.nodes[0].channels[0]
    unitless = replace(channel.curve, curve_type="animCurveTU")
    clip = replace(
        clip,
        nodes=(
            replace(
                clip.nodes[0],
                channels=(
                    replace(channel, attribute="input1X", curve=unitless),
                ),
            ),
        ),
    )
    clip.restore(mod, targets=[target])
    mod.do_it_dg()
    assert _values(maya_cmds, "target.input1X") == pytest.approx([2, 6, 10])


def test_no_implicit_sample_reduction_or_tangent_rewriting(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source", ((1, 0), (3, 10), (5, 2)))
    cmds.keyTangent(source + ".tx", edit=True, weightedTangents=True)
    cmds.keyTangent(
        source + ".tx",
        time=(3, 3),
        edit=True,
        inTangentType="fixed",
        outTangentType="fixed",
        inAngle=20,
        outAngle=-30,
        lock=False,
    )
    cmds.keyframe(source + ".tx", time=(3, 3), edit=True, breakdown=True)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    original = clip.nodes[0].channels[0].curve
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    copied = (
        AnimationClip.capture(
            [target], attributes=["tx"], layer_mode="preserve"
        )
        .nodes[0]
        .channels[0]
        .curve
    )
    assert copied.weighted == original.weighted
    assert len(copied.keys) == len(original.keys)
    for actual, saved in zip(copied.keys, original.keys):
        assert actual.in_tangent_xy == pytest.approx(saved.in_tangent_xy)
        assert actual.out_tangent_xy == pytest.approx(saved.out_tangent_xy)
        assert (
            replace(
                actual,
                in_tangent_xy=saved.in_tangent_xy,
                out_tangent_xy=saved.out_tangent_xy,
            )
            == saved
        )
    flat = AnimationClip.capture([source], attributes=["tx"])
    assert len(flat.nodes[0].channels[0].curve.keys) == 5


@pytest.mark.parametrize(
    "bad",
    [
        dict(mode="bad"),
        dict(namespace="foo", targets=[]),
        dict(targets=[]),
        dict(tolerance=-1),
    ],
)
def test_bad_restore_arguments_are_rejected_before_queueing(maya_cmds, bad):
    source = _node(maya_cmds, "source")
    clip = AnimationClip.capture([source], attributes=["tx"])
    mod = bdu.ModifierManager()
    with pytest.raises((ValueError, TypeError)):
        clip.restore(mod, **bad)
    assert not mod.can_undo


def test_clip_range_is_used_for_partial_replacement(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source", ((0, 0), (30, 30)))
    clip = AnimationClip.capture(
        [source],
        attributes=["tx"],
        start_frame=10,
        end_frame=20,
        layer_mode="preserve",
    )
    target = _node(
        cmds, "target", ((5, 50), (10, 100), (15, 150), (20, 200), (25, 250))
    )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_range")
    mod.do_it_dg()
    assert cmds.keyframe(target + ".tx", query=True, timeChange=True) == [
        5,
        10,
        20,
        25,
    ]
    assert _values(cmds, target + ".tx", (5, 10, 15, 20, 25)) == pytest.approx(
        [50, 10, 15, 20, 250]
    )


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_full_replace_restores_curve_settings(maya_cmds, layer_mode):
    cmds = maya_cmds
    source = _node(cmds, "source")
    target = _node(cmds, "target")
    cmds.setInfinity(target + ".tx", preInfinite="cycle", postInfinite="cycle")
    cmds.keyTangent(target + ".tx", edit=True, weightedTangents=True)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    curve = bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
    assert not curve.weighted
    assert curve.pre_infinity == curve.post_infinity == "constant"


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_explicit_nonkeyable_and_sparse_array_restore(maya_cmds, layer_mode):
    cmds = maya_cmds
    source, target = [_node(cmds, name, ()) for name in ("source", "target")]
    for node in (source, target):
        cmds.addAttr(
            node, longName="values", attributeType="double", multi=True
        )
        cmds.setAttr(node + ".values[3]", 2)
        cmds.setAttr(node + ".values[11]", 4)
    clip = AnimationClip.capture(
        [source],
        attributes=["values"],
        start_frame=1,
        end_frame=5,
        layer_mode=layer_mode,
    )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target])
    mod.do_it_dg()
    assert cmds.getAttr(target + ".values[3]", time=3) == 2
    assert cmds.getAttr(target + ".values[11]", time=3) == 4
    assert cmds.getAttr(target + ".values", multiIndices=True) == [3, 11]


def test_cycle_weight_can_be_saved_without_range_clipping(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source", ((1, 2), (20, 5)))
    layer = _layer(cmds, source)
    cmds.setKeyframe(layer + ".weight", time=1, value=0.25)
    cmds.setKeyframe(layer + ".weight", time=5, value=0.5)
    cmds.setInfinity(layer + ".weight", postInfinite="cycle")
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    assert not clip.clipped
    weight = next(
        item for item in clip.layers[0].settings if item.name == "weight"
    )
    assert weight.curve.post_infinity == "cycle"
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, target + ".tx", (1, 7, 13, 20)) == pytest.approx(
        _values(cmds, source + ".tx", (1, 7, 13, 20))
    )


@pytest.mark.parametrize(
    "setting,value",
    [
        ("override", True),
        ("passthrough", False),
        ("rotationAccumulationMode", 1),
        ("scaleAccumulationMode", 0),
    ],
)
def test_layer_setting_overwrite_and_history(maya_cmds, setting, value):
    cmds = maya_cmds
    source = _node(cmds, "source")
    layer = _layer(cmds, source)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    cmds.setAttr(layer + "." + setting, value)
    mod = bdu.ModifierManager()
    clip.restore(mod, restore_layer_settings=True)
    mod.do_it_dg()
    saved = next(
        item.value for item in clip.layers[0].settings if item.name == setting
    )
    assert cmds.getAttr(layer + "." + setting) == saved
    mod.undo_it()
    assert cmds.getAttr(layer + "." + setting) == value


def test_layer_settings_namespace_and_source_ui_are_preserved(maya_cmds):
    cmds = maya_cmds
    cmds.namespace(add="src")
    cmds.namespace(add="dst")
    source = _node(cmds, "src:ctrl")
    target = _node(cmds, "dst:ctrl", ())
    layer = _layer(cmds, source, "src:Correction")
    cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    cmds.currentTime(19)
    cmds.select(source)
    cmds.flushUndo()
    cmds.file(modified=False)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    assert cmds.currentTime(query=True) == 19
    assert cmds.ls(selection=True) == [source]
    assert cmds.animLayer(layer, query=True, selected=True)
    assert cmds.animLayer(layer, query=True, preferred=True)
    assert not cmds.file(query=True, modified=True)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    mod = bdu.ModifierManager()
    clip.restore(mod, namespace="dst", mode="replace_all")
    mod.do_it_dg()
    assert cmds.objExists("dst:Correction")
    assert _values(cmds, target + ".tx") == pytest.approx(
        _values(cmds, source + ".tx")
    )
