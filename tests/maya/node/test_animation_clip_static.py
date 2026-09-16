from __future__ import annotations

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _keys(cmds, plug, values=((1, 2), (5, 10)), **kwargs):
    for frame, value in values:
        cmds.setKeyframe(
            plug,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
            **kwargs,
        )


def _names(clip):
    return {
        channel.attribute for node in clip.nodes for channel in node.channels
    }


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("include_static", [False, True])
def test_static_collection_and_restore_leave_excluded_attributes_alone(
    maya_cmds, layer_mode, include_static
):
    cmds = maya_cmds
    source = cmds.createNode("transform")
    target = cmds.createNode("transform")
    _keys(cmds, source + ".tx")
    cmds.setAttr(source + ".ty", 7)
    _keys(cmds, target + ".ty", ((-10, 20), (10, 30)))
    for node in (source, target):
        cmds.addAttr(node, longName="shown", attributeType="double")
        cmds.setAttr(node + ".shown", 9, channelBox=True)
    clip = bdu.AnimationClip.capture(
        [source],
        layer_mode=layer_mode,
        include_channel_box=True,
        include_static=include_static,
    )
    if include_static:
        assert {"translate.translateY", "shown"} <= _names(clip)
    else:
        assert _names(clip) == {"translate.translateX"}
    assert bdu.AnimationClip.from_json(clip.to_json()) == clip
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    if include_static:
        assert cmds.getAttr(target + ".ty", time=3) == 7
        assert cmds.keyframe(target + ".shown", query=True, keyframeCount=True)
    else:
        assert cmds.keyframe(target + ".ty", query=True, timeChange=True) == [
            -10,
            10,
        ]
        assert cmds.keyframe(target + ".ty", query=True, valueChange=True) == [
            20,
            30,
        ]
        assert not cmds.keyframe(
            target + ".shown", query=True, keyframeCount=True
        )
    mod.undo_it()
    assert cmds.keyframe(target + ".ty", query=True, valueChange=True) == [
        20,
        30,
    ]
    mod.redo_it()
    assert cmds.getAttr(target + ".tx", time=3) == pytest.approx(6)


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_explicit_attributes_and_compounds_still_filter_static(
    maya_cmds, layer_mode
):
    cmds = maya_cmds
    source = cmds.createNode("transform")
    _keys(cmds, source + ".tx")
    cmds.addAttr(source, longName="hidden", attributeType="double")
    _keys(cmds, source + ".hidden")
    clip = bdu.AnimationClip.capture(
        [source], attributes=["translate", "hidden"], layer_mode=layer_mode
    )
    assert _names(clip) == {"translate.translateX", "hidden"}


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_all_static_is_an_error_unless_opted_in(maya_cmds, layer_mode):
    source = maya_cmds.createNode("transform")
    with pytest.raises(ValueError, match="include_static=True"):
        bdu.AnimationClip.capture(
            [source], start_frame=1, end_frame=5, layer_mode=layer_mode
        )
    clip = bdu.AnimationClip.capture(
        [source],
        start_frame=1,
        end_frame=5,
        layer_mode=layer_mode,
        include_static=True,
    )
    assert "translate.translateX" in _names(clip)


@pytest.mark.parametrize("value", [1, None, "yes"])
def test_include_static_requires_bool(maya_cmds, value):
    source = maya_cmds.createNode("transform")
    with pytest.raises(TypeError, match="include_static must be a bool"):
        bdu.AnimationClip.capture([source], include_static=value)


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("key_values", [((1, 7),), ((-10, 7), (10, 7))])
def test_constant_keys_are_kept_and_empty_curves_are_excluded(
    maya_cmds, layer_mode, key_values
):
    cmds = maya_cmds
    source = cmds.createNode("transform")
    _keys(cmds, source + ".tx", key_values)
    empty = cmds.createNode("animCurveTL")
    cmds.connectAttr(empty + ".output", source + ".ty")
    cmds.connectAttr("time1.outTime", empty + ".input")
    clip = bdu.AnimationClip.capture(
        [source], start_frame=2, end_frame=4, layer_mode=layer_mode
    )
    assert _names(clip) == {"translate.translateX"}
    assert {k.value for k in clip.nodes[0].channels[0].curve.keys} == {7}


@pytest.mark.parametrize(
    "driver_kind",
    ["connection", "math", "constraint", "expression", "time", "driven_key"],
)
def test_flatten_keeps_upstream_animation_without_direct_keys(
    maya_cmds, driver_kind
):
    cmds = maya_cmds
    driver = cmds.createNode("transform", name="driver")
    source = cmds.createNode("transform", name="clipSource")
    _keys(cmds, driver + ".tx")
    if driver_kind == "connection":
        cmds.connectAttr(driver + ".tx", source + ".tx")
    elif driver_kind == "math":
        math = cmds.createNode("multiplyDivide")
        cmds.connectAttr(driver + ".tx", math + ".input1X")
        cmds.setAttr(math + ".input2X", 3)
        cmds.connectAttr(math + ".outputX", source + ".tx")
    elif driver_kind == "constraint":
        cmds.pointConstraint(driver, source)
    elif driver_kind == "expression":
        cmds.expression(
            string=source + ".tx = frame * 2;", alwaysEvaluate=True
        )
    elif driver_kind == "time":
        cmds.connectAttr("time1.outTime", source + ".tx")
        # Initialize Maya's automatic time conversion in the normal context.
        cmds.getAttr(source + ".tx")
    else:
        for value in (2, 10):
            cmds.setDrivenKeyframe(
                source + ".tx",
                currentDriver=driver + ".tx",
                driverValue=value,
                value=value * 2,
                inTangentType="linear",
                outTangentType="linear",
            )
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], start_frame=1, end_frame=5
    )
    expected = [cmds.getAttr(source + ".tx", time=t) for t in (1, 3, 5)]
    assert _names(clip) == {"translate.translateX"}
    target = cmds.createNode("transform")
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target])
    mod.do_it_dg()
    assert [
        cmds.getAttr(target + ".tx", time=t) for t in (1, 3, 5)
    ] == pytest.approx(expected)


def test_static_connection_does_not_inherit_sibling_animation(maya_cmds):
    cmds = maya_cmds
    driver = cmds.createNode("transform")
    source = cmds.createNode("transform")
    _keys(cmds, driver + ".tx")
    cmds.connectAttr(driver + ".ty", source + ".tx")
    with pytest.raises(ValueError, match="No animated attributes"):
        bdu.AnimationClip.capture([source], start_frame=1, end_frame=5)


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_static_nodes_keep_positional_mapping_and_pending_keys_are_not_executed(
    maya_cmds, layer_mode
):
    cmds = maya_cmds
    sources = [cmds.createNode("transform") for _ in range(3)]
    _keys(cmds, sources[0] + ".tx")
    _keys(cmds, sources[2] + ".tx", ((1, 20), (5, 40)))
    pending = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=pending)
    nodes.existing.transform(sources[1]).tx.keyframe.set_key(99, frame=3)
    cmds.currentTime(17)
    cmds.select(sources[1])
    cmds.flushUndo()
    cmds.file(modified=False)
    clip = bdu.AnimationClip.capture(sources, layer_mode=layer_mode)
    assert len(clip.nodes) == 3
    assert not clip.nodes[1].channels
    assert not cmds.keyframe(sources[1], query=True, keyframeCount=True)
    assert cmds.currentTime(query=True) == 17
    assert cmds.ls(selection=True) == [sources[1]]
    assert not cmds.file(query=True, modified=True)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    targets = [cmds.createNode("transform") for _ in range(3)]
    cmds.setAttr(targets[1] + ".tx", 123)
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=targets)
    mod.do_it_dg()
    assert [
        cmds.getAttr(node + ".tx", time=3) for node in targets
    ] == pytest.approx([6, 123, 30])


@pytest.mark.parametrize(
    "animated_part", ["base", "layer", "weight", "parent_weight"]
)
def test_preserve_keeps_static_contributions_required_by_animation(
    maya_cmds, animated_part
):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="clipSource")
    cmds.setAttr(source + ".tx", 5)
    layer = cmds.animLayer("Upper")
    cmds.animLayer(layer, edit=True, attribute=source + ".tx")
    if animated_part == "layer":
        _keys(cmds, source + ".tx", animLayer=layer, noResolve=True)
    else:
        raw = cmds.animLayer(layer, query=True, layeredPlug=source + ".tx")
        cmds.setAttr(raw, 7)
        if animated_part == "base":
            root = cmds.animLayer(query=True, root=True)
            _keys(cmds, source + ".tx", animLayer=root, noResolve=True)
        else:
            weight_layer = layer
            if animated_part == "parent_weight":
                weight_layer = cmds.animLayer("Parent")
                cmds.animLayer(layer, edit=True, parent=weight_layer)
            _keys(cmds, weight_layer + ".weight", ((1, 0.25), (5, 0.75)))
    unrelated = cmds.animLayer("Unrelated")
    cmds.animLayer(unrelated, edit=True, attribute=source + ".ty")
    clip = bdu.AnimationClip.capture([source], layer_mode="preserve")
    assert _names(clip) == {"translate.translateX"}
    assert {ch.layer for ch in clip.nodes[0].channels} == {None, layer}
    assert unrelated not in {item.name for item in clip.layers}
    expected = [cmds.getAttr(source + ".tx", time=t) for t in (1, 3, 5)]
    cmds.file(new=True, force=True)
    target = cmds.createNode("transform", name="clipSource")
    mod = bdu.ModifierManager()
    clip.restore(mod)
    mod.do_it_dg()
    assert [
        cmds.getAttr(target + ".tx", time=t) for t in (1, 3, 5)
    ] == pytest.approx(expected)
    assert not cmds.keyframe(target + ".ty", query=True, keyframeCount=True)


def test_preserve_subset_does_not_inherit_unselected_layer_keys(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform")
    _keys(cmds, source + ".tx")
    layer = cmds.animLayer("StaticLayer")
    cmds.animLayer(layer, edit=True, attribute=source + ".tx")
    with pytest.raises(ValueError, match="include_static=True"):
        bdu.AnimationClip.capture(
            [source],
            layer_mode="preserve",
            layers=[layer],
            start_frame=1,
            end_frame=5,
        )
    clip = bdu.AnimationClip.capture(
        [source],
        layer_mode="preserve",
        layers=[layer],
        start_frame=1,
        end_frame=5,
        include_static=True,
    )
    assert {ch.layer for ch in clip.nodes[0].channels} == {layer}


@pytest.mark.parametrize("animated_layer", ["base", "upper"])
@pytest.mark.parametrize("accumulation", [0, 1])
def test_preserve_keeps_coupled_rotation_axes(
    maya_cmds, animated_layer, accumulation
):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="clipSource")
    cmds.setAttr(source + ".rotate", 30, 20, 40)
    layer = cmds.animLayer("Upper")
    cmds.animLayer(layer, edit=True, attribute=source + ".rotate")
    cmds.setAttr(layer + ".rotationAccumulationMode", accumulation)
    root = cmds.animLayer(query=True, root=True)
    chosen = root if animated_layer == "base" else layer
    _keys(
        cmds,
        source + ".ry",
        ((1, 10), (5, 90)),
        animLayer=chosen,
        noResolve=True,
    )
    clip = bdu.AnimationClip.capture([source], layer_mode="preserve")
    assert _names(clip) == {
        "rotate.rotateX",
        "rotate.rotateY",
        "rotate.rotateZ",
    }
    expected = [
        cmds.getAttr(source + "." + attr, time=t)
        for t in (1, 3, 5)
        for attr in ("rx", "ry", "rz")
    ]
    subset = bdu.AnimationClip.capture(
        [source], layer_mode="preserve", layers=[chosen]
    )
    assert _names(subset) == _names(clip)
    assert {ch.layer for ch in subset.nodes[0].channels} == {
        None if chosen == root else layer
    }
    cmds.file(new=True, force=True)
    target = cmds.createNode("transform", name="clipSource")
    mod = bdu.ModifierManager()
    clip.restore(mod)
    mod.do_it_dg()
    assert [
        cmds.getAttr(target + "." + attr, time=t)
        for t in (1, 3, 5)
        for attr in ("rx", "ry", "rz")
    ] == pytest.approx(expected)
