from __future__ import annotations

from dataclasses import replace

import pytest

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _keys(cmds, plug, values=((10, 2), (20, 6), (30, 10)), **kwargs):
    for frame, value in values:
        cmds.setKeyframe(
            plug,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
            **kwargs,
        )


def _node(cmds, name="clipSource", keys=((10, 2), (20, 6), (30, 10))):
    node = cmds.createNode("transform", name=name)
    _keys(cmds, node + ".tx", keys)
    return node


def _times(cmds, plug):
    return cmds.keyframe(plug, query=True, timeChange=True) or []


def _values(cmds, plug, frames):
    return [cmds.getAttr(plug, time=t) for t in frames]


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("mode", ["merge", "replace_range", "replace_all"])
@pytest.mark.parametrize(
    "timing",
    [dict(offset_frames=90), dict(to_start_frame=100), dict(to_end_frame=120)],
)
def test_shifted_restore_modes_and_history(
    maya_cmds, layer_mode, mode, timing
):
    cmds = maya_cmds
    source = _node(cmds)
    target = _node(
        cmds, "target", ((5, -5), (10, -10), (107, 777), (120, 888), (130, 9))
    )
    before = (
        bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
    )
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    saved = clip.to_json()
    mod = bdu.ModifierManager()
    assert clip.restore(mod, targets=[target], mode=mode, **timing) is None
    assert (
        bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
        == before
    )
    assert clip.to_json() == saved
    mod.do_it_dg()
    after = bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
    assert _values(cmds, target + ".tx", (100, 110, 120)) == pytest.approx(
        [2, 6, 10]
    )
    times = _times(cmds, target + ".tx")
    if mode == "replace_all":
        assert min(times) == 100 and max(times) == 120
    else:
        assert {5, 10, 130} <= set(times)
    if layer_mode == "preserve":
        assert (107 in times) == (mode == "merge")
    assert _times(cmds, source + ".tx") == [10, 20, 30]
    for _ in range(2):
        mod.undo_it()
        assert (
            bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
            == before
        )
        mod.redo_it()
        assert (
            bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
            == after
        )
    assert clip.to_json() == saved


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "timing",
    [
        {},
        dict(offset_frames=0),
        dict(to_start_frame=10),
        dict(to_end_frame=30),
    ],
)
def test_zero_shift_still_restores(maya_cmds, layer_mode, timing):
    source = _node(maya_cmds)
    target = _node(maya_cmds, "target", ())
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], **timing)
    mod.do_it_dg()
    assert _values(maya_cmds, target + ".tx", (10, 20, 30)) == pytest.approx(
        [2, 6, 10]
    )


def test_common_clip_anchor_preserves_node_and_channel_offsets(maya_cmds):
    cmds = maya_cmds
    a = _node(cmds, "a", ((10, 2), (30, 10)))
    b = _node(cmds, "b", ((15, 3), (25, 8)))
    _keys(cmds, b + ".ty", ((18, 7),))
    clip = bdu.AnimationClip.capture([a, b], layer_mode="preserve")
    targets = [_node(cmds, name, ()) for name in ("dstA", "dstB")]
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=targets, to_start_frame=100)
    mod.do_it_dg()
    assert _times(cmds, targets[0] + ".tx") == [100, 120]
    assert _times(cmds, targets[1] + ".tx") == [105, 115]
    assert _times(cmds, targets[1] + ".ty") == [108]


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_clipped_boundaries_negative_subframes_and_repeat_booking(
    maya_cmds, layer_mode
):
    cmds = maya_cmds
    source = _node(cmds, keys=((0, 0), (40, 40)))
    clip = bdu.AnimationClip.capture(
        [source],
        attributes=["tx"],
        start_frame=10,
        end_frame=30,
        layer_mode=layer_mode,
    )
    saved = clip.to_json()
    targets = [_node(cmds, name, ()) for name in ("first", "second")]
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[targets[0]], to_start_frame=-10.5)
    clip.restore(mod, targets=[targets[1]], to_end_frame=100.25)
    assert clip.to_json() == saved
    clip.nodes[0].channels[0].curve.keys[0].value = 999
    mod.do_it_dg()
    assert _values(cmds, targets[0] + ".tx", (-10.5, 9.5)) == pytest.approx(
        [10, 30]
    )
    assert _values(cmds, targets[1] + ".tx", (80.25, 100.25)) == pytest.approx(
        [10, 30]
    )


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "timing,expected",
    [
        (dict(offset_frames=15), (37.5, 62.5)),
        (dict(to_start_frame=90), (75, 100)),
        (dict(to_end_frame=90), (50, 75)),
    ],
)
def test_time_units_are_captured_at_booking(
    maya_cmds, layer_mode, timing, expected
):
    cmds = maya_cmds
    cmds.currentUnit(time="film")
    try:
        source = _node(cmds, keys=((24, 2), (48, 10)))
        clip = bdu.AnimationClip.capture(
            [source], attributes=["tx"], layer_mode=layer_mode
        )
        target = _node(cmds, "target", ())
        cmds.currentUnit(time="ntsc")
        mod = bdu.ModifierManager()
        clip.restore(mod, targets=[target], **timing)
        cmds.currentUnit(time="pal")
        mod.do_it_dg()
        times = _times(cmds, target + ".tx")
        assert (min(times), max(times)) == pytest.approx(expected)
        assert _values(cmds, target + ".tx", expected) == pytest.approx(
            [2, 10]
        )
        mod.undo_it()
        assert not _times(cmds, target + ".tx")
        mod.redo_it()
        assert _values(cmds, target + ".tx", expected) == pytest.approx(
            [2, 10]
        )
    finally:
        cmds.currentUnit(time="film")


@pytest.mark.parametrize(
    "timing,error",
    [
        (dict(offset_frames=0, to_start_frame=10), ValueError),
        (dict(to_start_frame=0, to_end_frame=20), ValueError),
        (dict(offset_frames=1, to_end_frame=20), ValueError),
        (dict(offset_frames=float("nan")), ValueError),
        (dict(to_start_frame=float("inf")), ValueError),
        (dict(to_end_frame=-float("inf")), ValueError),
        (dict(offset_frames=True), TypeError),
        (dict(to_start_frame="100"), TypeError),
        (dict(to_end_frame=object()), TypeError),
        (dict(offset_frames=1e100), ValueError),
        (dict(to_start_frame=1e100), ValueError),
    ],
)
def test_invalid_timing_does_not_queue_any_restore(maya_cmds, timing, error):
    cmds = maya_cmds
    source = _node(cmds)
    target = _node(cmds, "target", ())
    clip = bdu.AnimationClip.capture([source], attributes=["tx"])
    before = set(cmds.ls())
    mod = bdu.ModifierManager()
    with pytest.raises(error):
        clip.restore(mod, targets=[target], **timing)
    mod.do_it_dg()
    assert not _times(cmds, target + ".tx")
    assert set(cmds.ls()) == before


@pytest.mark.parametrize("weighted", [False, True])
def test_shift_keeps_detailed_key_metadata(maya_cmds, weighted):
    cmds = maya_cmds
    source = _node(cmds)
    cmds.keyTangent(source + ".tx", edit=True, weightedTangents=weighted)
    cmds.keyTangent(
        source + ".tx",
        edit=True,
        time=(20, 20),
        inTangentType="fixed",
        outTangentType="fixed",
        inAngle=25,
        outAngle=-15,
        lock=False,
    )
    cmds.keyframe(source + ".tx", edit=True, time=(20, 20), breakdown=True)
    cmds.setInfinity(
        source + ".tx", preInfinite="linear", postInfinite="cycle"
    )
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    original = clip.nodes[0].channels[0].curve
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], offset_frames=90, mode="replace_all")
    mod.do_it_dg()
    result = (
        bdu.Nodes().existing.transform(target).tx.keyframe.get_curve_data()
    )
    assert replace(result, keys=()) == replace(original, keys=())
    for actual, saved in zip(result.keys, original.keys):
        assert actual.frame == pytest.approx(saved.frame + 90)
        assert actual.in_tangent_xy == pytest.approx(saved.in_tangent_xy)
        assert actual.out_tangent_xy == pytest.approx(saved.out_tangent_xy)
        assert (
            replace(
                actual,
                frame=saved.frame,
                in_tangent_xy=saved.in_tangent_xy,
                out_tangent_xy=saved.out_tangent_xy,
            )
            == saved
        )


def _layered_clip(cmds, *, clipped=False, weighted=False):
    source = _node(cmds)
    root = cmds.animLayer("Parent")
    layer = cmds.animLayer("Upper")
    cmds.animLayer(layer, edit=True, parent=root, attribute=source + ".tx")
    _keys(
        cmds,
        source + ".tx",
        ((10, 3), (30, 7)),
        animLayer=layer,
        noResolve=True,
    )
    _keys(cmds, layer + ".weight", ((10, 0.25), (30, 0.75)))
    _keys(cmds, root + ".weight", ((10, 0.5), (30, 1)))
    base = cmds.animLayer(query=True, root=True)
    _keys(cmds, base + ".weight", ((10, 0.75), (30, 1)))
    if weighted:
        for name in (base, root, layer):
            cmds.keyTangent(name + ".weight", edit=True, weightedTangents=True)
    bounds = dict(start_frame=15, end_frame=25) if clipped else {}
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve", **bounds
    )
    return source, clip, (base, root, layer)


@pytest.mark.parametrize("clipped", [False, True])
def test_layer_and_root_settings_shift_with_channels(maya_cmds, clipped):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(cmds, clipped=clipped)
    frames = (
        clip.start_frame,
        (clip.start_frame + clip.end_frame) / 2,
        clip.end_frame,
    )
    expected = _values(cmds, source + ".tx", frames)
    weights = {
        layer: _values(cmds, layer + ".weight", frames) for layer in layers
    }
    original = clip.to_json()
    cmds.file(new=True, force=True)
    target = _node(cmds, keys=())
    mod = bdu.ModifierManager()
    clip.restore(mod, offset_frames=90)
    mod.do_it_dg()
    shifted = [frame + 90 for frame in frames]
    assert _values(cmds, target + ".tx", shifted) == pytest.approx(expected)
    for layer in layers:
        assert _times(cmds, layer + ".weight") == pytest.approx(
            [shifted[0], shifted[-1]]
        )
        assert _values(cmds, layer + ".weight", shifted) == pytest.approx(
            weights[layer]
        )
    assert clip.to_json() == original
    mod.undo_it()
    assert not cmds.ls(type="animLayer")
    mod.redo_it()
    assert _values(cmds, target + ".tx", shifted) == pytest.approx(expected)


@pytest.mark.parametrize("clipped", [False, True])
@pytest.mark.parametrize("weighted", [False, True])
def test_existing_layer_settings_are_compared_at_shifted_times(
    maya_cmds, clipped, weighted
):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(
        cmds, clipped=clipped, weighted=weighted
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], offset_frames=90)
    with pytest.raises(ValueError, match="settings differ"):
        mod.do_it_dg()
    assert not _times(cmds, target + ".tx")
    for layer in layers:
        assert _times(cmds, layer + ".weight") == [10, 30]
    clip.restore(
        mod, targets=[target], offset_frames=90, restore_layer_settings=True
    )
    mod.do_it_dg()
    start, end = clip.start_frame + 90, clip.end_frame + 90
    for layer in layers:
        assert _times(cmds, layer + ".weight") == pytest.approx([start, end])
    # A second restore reuses matching shifted settings without an override.
    clip.restore(mod, targets=[target], offset_frames=90)
    mod.do_it_dg()


@pytest.mark.parametrize("weighted", [False, True])
def test_shifted_setting_comparison_still_detects_tangent_changes(
    maya_cmds, weighted
):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(cmds, clipped=True, weighted=weighted)
    mod = bdu.ModifierManager()
    clip.restore(mod, offset_frames=90, restore_layer_settings=True)
    mod.do_it_dg()
    options = (
        dict(outWeight=2, weightLock=False) if weighted else dict(outAngle=45)
    )
    cmds.keyTangent(
        layers[0] + ".weight",
        edit=True,
        time=(105, 105),
        lock=False,
        outTangentType="fixed",
        **options,
    )
    clip.restore(mod, offset_frames=90)
    with pytest.raises(ValueError, match="settings differ"):
        mod.do_it_dg()


@pytest.mark.parametrize("fail", [False, True])
def test_shift_after_queued_creation_and_later_failure(maya_cmds, fail):
    cmds = maya_cmds
    source = cmds.createNode("multiplyDivide")
    _keys(cmds, source + ".input1X")
    clip = bdu.AnimationClip.capture([source], attributes=["input1X"])
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    target = nodes.create.multiplyDivide(name="pendingTarget")
    clip.restore(mod, targets=[target], to_start_frame=100)
    assert not cmds.objExists("pendingTarget")
    if fail:

        def reject(modifier):
            raise RuntimeError("later failure")

        mod.queue_dg_modifier(reject)
        with pytest.raises(RuntimeError, match="later failure"):
            mod.do_it_dg()
        assert not cmds.objExists("pendingTarget")
    else:
        mod.do_it_dg()
        assert _values(
            cmds, "pendingTarget.input1X", (100, 110, 120)
        ) == pytest.approx([2, 6, 10])
        mod.undo_it()
        assert not cmds.objExists("pendingTarget")
        mod.redo_it()
        assert _values(
            cmds, "pendingTarget.input1X", (100, 110, 120)
        ) == pytest.approx([2, 6, 10])


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_single_time_clip_can_align_its_end(maya_cmds, layer_mode):
    source = _node(maya_cmds, keys=((10, 7),))
    target = _node(maya_cmds, "target", ())
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], to_end_frame=-0.25)
    mod.do_it_dg()
    assert _times(maya_cmds, target + ".tx") == [-0.25]
    assert _values(maya_cmds, target + ".tx", (-0.25,)) == [7]


@pytest.mark.parametrize("unresolvable", [False, True])
def test_flatten_resolves_destination_time_layers_and_rolls_back(
    maya_cmds, unresolvable
):
    cmds = maya_cmds
    source = _node(cmds)
    clip = bdu.AnimationClip.capture([source], attributes=["tx"])
    a = _node(cmds, "first", ())
    b = _node(cmds, "second", ())
    layer = cmds.animLayer("Upper", override=unresolvable)
    cmds.animLayer(layer, edit=True, attribute=b + ".tx")
    _keys(
        cmds,
        b + ".tx",
        ((10, 1000), (100, 3), (120, 7)),
        animLayer=layer,
        noResolve=True,
    )
    if not unresolvable:
        _keys(cmds, layer + ".weight", ((100, 0.25), (120, 0.75)))
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[a], to_start_frame=100)
    clip.restore(mod, targets=[b], to_start_frame=100)
    if unresolvable:
        with pytest.raises(RuntimeError, match="Cannot resolve clip value"):
            mod.do_it_dg()
        assert not _times(cmds, a + ".tx")
    else:
        mod.do_it_dg()
        assert _values(cmds, b + ".tx", (100, 110, 120)) == pytest.approx(
            [2, 6, 10]
        )
    data = (
        bdu.Nodes()
        .existing.transform(b)
        .tx.keyframe.anim_layer(layer)
        .get_curve_data()
    )
    assert [key.frame for key in data.keys] == [10, 100, 120]
    assert [key.value for key in data.keys] == [1000, 3, 7]
