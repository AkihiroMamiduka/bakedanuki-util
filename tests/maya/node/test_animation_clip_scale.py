from __future__ import annotations

import math
from dataclasses import replace

import pytest

import bd_util as bdu
from bd_util.maya.node._animation_clip_capture import capture_settings
from test_animation_clip_time import _layered_clip

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


def _node(cmds, name="source", keys=((10, 2), (20, 6), (30, 10))):
    node = cmds.createNode("transform", name=name)
    _keys(cmds, node + ".tx", keys)
    return node


def _times(cmds, plug):
    return cmds.keyframe(plug, query=True, timeChange=True) or []


def _values(cmds, plug, frames):
    return [cmds.getAttr(plug, time=t) for t in frames]


def _curve(node, attr="tx"):
    return getattr(
        bdu.Nodes().existing.transform(node), attr
    ).keyframe.get_curve_data()


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "timing,bounds",
    [
        (dict(time_scale=2), (10, 50)),
        (dict(time_scale=0.5), (10, 20)),
        (dict(time_scale=2, offset_frames=15), (25, 65)),
        (dict(time_scale=2, to_start_frame=100), (100, 140)),
        (dict(time_scale=2, to_end_frame=100), (60, 100)),
        (dict(duration_frames=30), (10, 40)),
        (dict(duration_frames=30, offset_frames=15), (25, 55)),
        (dict(duration_frames=30, to_start_frame=100), (100, 130)),
        (dict(duration_frames=30, to_end_frame=100), (70, 100)),
        (dict(to_start_frame=100, to_end_frame=140), (100, 140)),
        (dict(to_start_frame=-0.5, to_end_frame=4.5), (-0.5, 4.5)),
        (dict(time_scale=1), (10, 30)),
        (dict(duration_frames=20), (10, 30)),
        (dict(to_start_frame=10, to_end_frame=30), (10, 30)),
    ],
)
def test_scale_placement_and_identity(maya_cmds, layer_mode, timing, bounds):
    cmds = maya_cmds
    source = _node(cmds)
    target = _node(cmds, "target", ())
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    original = clip.to_json()
    mod = bdu.ModifierManager()
    assert clip.restore(mod, targets=[target], **timing) is None
    assert not _times(cmds, target + ".tx")
    mod.do_it_dg()
    times = _times(cmds, target + ".tx")
    assert (min(times), max(times)) == pytest.approx(bounds)
    assert len(times) == len(clip.nodes[0].channels[0].curve.keys)
    assert _values(
        cmds, target + ".tx", (bounds[0], sum(bounds) / 2, bounds[1])
    ) == pytest.approx([2, 6, 10])
    assert clip.to_json() == original
    assert _times(cmds, source + ".tx") == [10, 20, 30]
    for _ in range(2):
        mod.undo_it()
        assert not _times(cmds, target + ".tx")
        mod.redo_it()
        assert _times(cmds, target + ".tx") == times


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("mode", ["merge", "replace_all", "replace_range"])
@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=2, to_start_frame=100),
        dict(duration_frames=40, to_end_frame=140),
        dict(to_start_frame=100, to_end_frame=140),
    ],
)
def test_scaled_replacement_bounds_and_collisions(
    maya_cmds, layer_mode, mode, timing
):
    cmds = maya_cmds
    source = _node(cmds)
    target = _node(
        cmds,
        "target",
        ((5, -5), (100, -100), (107, 777), (140, 888), (150, 9)),
    )
    before = _curve(target)
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode=mode, **timing)
    mod.do_it_dg()
    times = _times(cmds, target + ".tx")
    assert (5 in times) == (mode != "replace_all")
    assert (150 in times) == (mode != "replace_all")
    assert (107 in times) == (mode == "merge")
    assert _values(cmds, target + ".tx", (100, 120, 140)) == pytest.approx(
        [2, 6, 10]
    )
    after = _curve(target)
    mod.undo_it()
    assert _curve(target) == before
    mod.redo_it()
    assert _curve(target) == after


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("attr", ["tx", "rx", "sy"])
@pytest.mark.parametrize(
    "tangent",
    [
        "fixed",
        "auto",
        "clamped",
        "flat",
        "linear",
        "plateau",
        "spline",
        "step",
        "stepnext",
        "fast",
        "slow",
        "autocustom",
        "autoease",
        "automix",
    ],
)
@pytest.mark.parametrize("scale", [0.25, 2])
def test_scaled_curve_shape_and_metadata(
    maya_cmds, weighted, attr, tangent, scale
):
    cmds = maya_cmds
    source = _node(cmds, keys=())
    plug = source + "." + attr
    _keys(cmds, plug, ((10, 0), (14, 3), (25, 1), (30, 5)))
    cmds.keyTangent(plug, edit=True, weightedTangents=weighted)
    cmds.keyTangent(
        plug,
        edit=True,
        lock=False,
        inTangentType="linear" if tangent == "step" else tangent,
        outTangentType=tangent,
    )
    if tangent == "fixed":
        cmds.keyTangent(plug, edit=True, inAngle=21, outAngle=-30)
    cmds.keyTangent(plug, edit=True, time=(14, 14), lock=True)
    if weighted:
        cmds.keyTangent(plug, edit=True, time=(25, 25), weightLock=True)
    cmds.keyframe(plug, edit=True, time=(25, 25), breakdown=True)
    cmds.setInfinity(plug, preInfinite="linear", postInfinite="cycle")
    clip = bdu.AnimationClip.capture(
        [source], attributes=[attr], layer_mode="preserve"
    )
    saved = clip.nodes[0].channels[0].curve
    samples = [8 + i / 4 for i in range(109)]
    expected = _values(cmds, plug, samples)
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(
        mod,
        targets=[target],
        time_scale=scale,
        to_start_frame=100,
        mode="replace_all",
    )
    mod.do_it_dg()
    if tangent in ("fast", "slow"):
        # Maya recomputes these legacy slopes even when every key is scaled.
        cmds.scaleKey(plug, timeScale=scale, timePivot=10)
        cmds.keyframe(plug, edit=True, relative=True, timeChange=90)
        # Native scaleKey can round the cycle seam; endpoint keys are checked below.
        samples = [t for t in samples if t != saved.keys[-1].frame]
        expected = _values(
            cmds, plug, [100 + (t - 10) * scale for t in samples]
        )
    assert _values(
        cmds, target + "." + attr, [100 + (t - 10) * scale for t in samples]
    ) == pytest.approx(expected, abs=2e-6)
    actual = _curve(target, attr)
    assert replace(actual, keys=()) == replace(saved, keys=())
    for a, b in zip(actual.keys, saved.keys):
        assert a.frame == pytest.approx(100 + (b.frame - 10) * scale)
        assert a.value == pytest.approx(b.value)
        assert (
            replace(
                a,
                frame=b.frame,
                value=b.value,
                in_tangent_xy=b.in_tangent_xy,
                out_tangent_xy=b.out_tangent_xy,
            )
            == b
        )
        if tangent == "fixed":
            for xy, old in (
                (a.in_tangent_xy, b.in_tangent_xy),
                (a.out_tangent_xy, b.out_tangent_xy),
            ):
                wanted = (old[0] * scale, old[1])
                assert math.atan2(xy[1], xy[0]) == pytest.approx(
                    math.atan2(wanted[1], wanted[0]), abs=1e-7
                )
                if weighted:
                    assert xy == pytest.approx(wanted, rel=1e-6, abs=1e-7)


def test_global_anchor_and_snapshot(maya_cmds):
    cmds = maya_cmds
    a = _node(cmds, "a")
    b = _node(cmds, "b", ((15, 3), (25, 8)))
    _keys(cmds, b + ".ty", ((18, 7),))
    clip = bdu.AnimationClip.capture([a, b], layer_mode="preserve")
    original = clip.to_json()
    targets = [
        _node(cmds, name, ())
        for name in ("firstA", "firstB", "secondA", "secondB")
    ]
    mod = bdu.ModifierManager()
    clip.restore(
        mod, targets=targets[:2], to_start_frame=100, to_end_frame=140
    )
    clip.restore(mod, targets=targets[2:], time_scale=0.5, to_start_frame=-5)
    assert clip.to_json() == original
    clip.nodes[1].channels[0].curve.keys[0].value = 999
    mod.do_it_dg()
    assert _times(cmds, targets[0] + ".tx") == [100, 120, 140]
    assert _times(cmds, targets[1] + ".tx") == [110, 130]
    assert _times(cmds, targets[1] + ".ty") == [116]
    assert _times(cmds, targets[3] + ".tx") == [-2.5, 2.5]
    assert _values(cmds, targets[1] + ".tx", (110, 130)) == pytest.approx(
        [3, 8]
    )


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=2, to_start_frame=90),
        dict(duration_frames=60, to_start_frame=90),
        dict(to_start_frame=90, to_end_frame=150),
    ],
)
def test_scale_units_are_fixed_at_booking(maya_cmds, layer_mode, timing):
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
        assert (min(times), max(times)) == pytest.approx([75, 125])
        assert _values(cmds, target + ".tx", (75, 125)) == pytest.approx(
            [2, 10]
        )
        mod.undo_it()
        assert not _times(cmds, target + ".tx")
        mod.redo_it()
        assert _times(cmds, target + ".tx") == times
    finally:
        cmds.currentUnit(time="film")


@pytest.mark.parametrize(
    "timing,error",
    [
        (dict(time_scale=0), ValueError),
        (dict(time_scale=-1), ValueError),
        (dict(time_scale=float("nan")), ValueError),
        (dict(time_scale=float("inf")), ValueError),
        (dict(time_scale=True), TypeError),
        (dict(time_scale="2"), TypeError),
        (dict(duration_frames=0), ValueError),
        (dict(duration_frames=-1), ValueError),
        (dict(duration_frames=float("nan")), ValueError),
        (dict(duration_frames=float("inf")), ValueError),
        (dict(duration_frames=True), TypeError),
        (dict(duration_frames="30"), TypeError),
        (dict(time_scale=1, duration_frames=20), ValueError),
        (dict(to_start_frame=100, to_end_frame=100), ValueError),
        (dict(to_start_frame=100, to_end_frame=90), ValueError),
        (dict(to_start_frame=100, to_end_frame=140, time_scale=2), ValueError),
        (
            dict(to_start_frame=100, to_end_frame=140, duration_frames=40),
            ValueError,
        ),
        (
            dict(to_start_frame=100, to_end_frame=140, offset_frames=0),
            ValueError,
        ),
        (dict(to_start_frame=100, to_end_frame=float("inf")), ValueError),
        (dict(to_start_frame=True, to_end_frame=140), TypeError),
        (dict(time_scale=1e100), ValueError),
        (dict(time_scale=1e-100, to_start_frame=100), ValueError),
    ],
)
def test_invalid_scaling_is_rejected_before_booking(maya_cmds, timing, error):
    cmds = maya_cmds
    source = _node(cmds)
    target = _node(cmds, "target", ())
    clip = bdu.AnimationClip.capture([source], attributes=["tx"])
    original = clip.to_json()
    before = set(cmds.ls())
    mod = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=mod).existing.transform(target).ty.set(42)
    with pytest.raises(error):
        clip.restore(mod, targets=[target], **timing)
    mod.do_it_dg()
    assert not _times(cmds, target + ".tx")
    assert cmds.getAttr(target + ".ty") == 42
    assert set(cmds.ls()) == before
    assert clip.to_json() == original


@pytest.mark.parametrize(
    "timing,valid",
    [
        (dict(time_scale=2, to_end_frame=-0.25), True),
        (dict(duration_frames=10), False),
        (dict(to_start_frame=100, to_end_frame=140), False),
    ],
)
def test_single_time_clip_scaling(maya_cmds, timing, valid):
    source = _node(maya_cmds, keys=((10, 7),))
    target = _node(maya_cmds, "target", ())
    clip = bdu.AnimationClip.capture([source], attributes=["tx"])
    mod = bdu.ModifierManager()
    if valid:
        clip.restore(mod, targets=[target], **timing)
        mod.do_it_dg()
        assert _times(maya_cmds, target + ".tx") == [-0.25]
        assert _values(maya_cmds, target + ".tx", (-0.25,)) == [7]
    else:
        with pytest.raises(ValueError, match="single-time"):
            clip.restore(mod, targets=[target], **timing)
        mod.do_it_dg()
        assert not _times(maya_cmds, target + ".tx")


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("clipped", [False, True])
@pytest.mark.parametrize("existing", [False, True])
def test_scaled_layer_and_root_settings(
    maya_cmds, weighted, clipped, existing
):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(
        cmds, clipped=clipped, weighted=weighted
    )
    frames = [
        clip.start_frame + (clip.end_frame - clip.start_frame) * i / 16
        for i in range(17)
    ]
    expected = _values(cmds, source + ".tx", frames)
    weights = {
        layer: _values(cmds, layer + ".weight", frames) for layer in layers
    }
    original = clip.to_json()
    if not existing:
        cmds.file(new=True, force=True)
    target = _node(cmds, "target", ())
    before = set(cmds.ls())
    mod = bdu.ModifierManager()
    timing = dict(to_start_frame=100, to_end_frame=140)
    if existing:
        clip.restore(mod, targets=[target], **timing)
        with pytest.raises(ValueError, match="settings differ"):
            mod.do_it_dg()
        assert not _times(cmds, target + ".tx")
    clip.restore(
        mod, targets=[target], restore_layer_settings=existing, **timing
    )
    mod.do_it_dg()
    times = [100 + i * 2.5 for i in range(17)]
    assert _values(cmds, target + ".tx", times) == pytest.approx(
        expected, abs=2e-6
    )
    for layer in layers:
        assert _times(cmds, layer + ".weight") == [100, 140]
        assert _values(cmds, layer + ".weight", times) == pytest.approx(
            weights[layer], abs=2e-6
        )
    clip.restore(mod, targets=[target], **timing)
    mod.do_it_dg()
    assert clip.to_json() == original
    mod.undo_it()
    assert set(cmds.ls()) == before
    if existing:
        for layer in layers:
            assert _times(cmds, layer + ".weight") == [10, 30]
    mod.redo_it()
    assert _values(cmds, target + ".tx", times) == pytest.approx(
        expected, abs=2e-6
    )


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_clipped_boundaries_define_scale(maya_cmds, layer_mode):
    cmds = maya_cmds
    source = _node(cmds, keys=((0, 0), (40, 40)))
    clip = bdu.AnimationClip.capture(
        [source],
        attributes=["tx"],
        start_frame=10,
        end_frame=30,
        layer_mode=layer_mode,
    )
    mod = bdu.ModifierManager()
    clip.restore(
        mod, to_start_frame=100, to_end_frame=110, mode="replace_range"
    )
    mod.do_it_dg()
    assert _values(cmds, source + ".tx", (100, 105, 110)) == pytest.approx(
        [10, 20, 30]
    )
    assert {0, 40, 100, 110} <= set(_times(cmds, source + ".tx"))


@pytest.mark.parametrize("fail", [False, True])
def test_scaling_after_queued_creation_and_later_failure(maya_cmds, fail):
    cmds = maya_cmds
    source = cmds.createNode("multiplyDivide")
    _keys(cmds, source + ".input1X")
    clip = bdu.AnimationClip.capture([source], attributes=["input1X"])
    mod = bdu.ModifierManager()
    target = bdu.Nodes(modifier_manager=mod).create.multiplyDivide(
        name="pendingTarget"
    )
    clip.restore(mod, targets=[target], to_start_frame=100, to_end_frame=140)
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
            cmds, "pendingTarget.input1X", (100, 120, 140)
        ) == pytest.approx([2, 6, 10])
        mod.undo_it()
        assert not cmds.objExists("pendingTarget")
        mod.redo_it()
        assert _values(
            cmds, "pendingTarget.input1X", (100, 120, 140)
        ) == pytest.approx([2, 6, 10])


@pytest.mark.parametrize("unresolvable", [False, True])
def test_scaling_flatten_resolves_destination_layers_and_rolls_back(
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
        ((10, 1000), (100, 3), (140, 7)),
        animLayer=layer,
        noResolve=True,
    )
    if not unresolvable:
        _keys(cmds, layer + ".weight", ((100, 0.25), (140, 0.75)))
    mod = bdu.ModifierManager()
    for target in (a, b):
        clip.restore(
            mod, targets=[target], to_start_frame=100, to_end_frame=140
        )
    if unresolvable:
        with pytest.raises(RuntimeError, match="Cannot resolve clip value"):
            mod.do_it_dg()
        assert not _times(cmds, a + ".tx")
    else:
        mod.do_it_dg()
        assert _values(cmds, b + ".tx", (100, 120, 140)) == pytest.approx(
            [2, 6, 10]
        )
    data = (
        bdu.Nodes()
        .existing.transform(b)
        .tx.keyframe.anim_layer(layer)
        .get_curve_data()
    )
    assert [key.frame for key in data.keys] == [10, 100, 140]
    assert [key.value for key in data.keys] == [1000, 3, 7]


@pytest.mark.parametrize("tangent", ["fast", "slow"])
@pytest.mark.parametrize("weighted", [False, True])
def test_legacy_layer_tangents_reuse_native_recomputed_settings(
    maya_cmds, tangent, weighted
):
    cmds = maya_cmds
    source, _, layers = _layered_clip(cmds, weighted=weighted)
    for layer in layers:
        cmds.keyTangent(
            layer + ".weight",
            edit=True,
            inTangentType=tangent,
            outTangentType=tangent,
        )
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    timing = dict(time_scale=2, to_start_frame=100)
    clip.restore(mod, targets=[target], restore_layer_settings=True, **timing)
    mod.do_it_dg()
    clip.restore(mod, targets=[target], **timing)
    mod.do_it_dg()
    cmds.keyTangent(
        layers[0] + ".weight", edit=True, time=(100, 100), outAngle=45
    )
    clip.restore(mod, targets=[target], **timing)
    with pytest.raises(ValueError, match="settings differ"):
        mod.do_it_dg()


def test_adjacent_keys_cannot_collapse_at_distant_destination(maya_cmds):
    source = _node(maya_cmds, keys=((10, 2), (10.000001, 6), (30, 10)))
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    assert len(clip.nodes[0].channels[0].curve.keys) == 3
    original = _curve(source)
    mod = bdu.ModifierManager()
    with pytest.raises(ValueError, match="coincide|increasing"):
        clip.restore(mod, time_scale=2, to_start_frame=1e12)
    mod.do_it_dg()
    assert _curve(source) == original


def test_layer_keys_outside_clip_and_different_setting_units(maya_cmds):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(cmds)
    for layer in layers:
        _keys(cmds, layer + ".weight", ((0, 0.25), (40, 1)))
    clip = replace(
        clip,
        layers=tuple(
            replace(layer, settings=capture_settings(layer.name, None, None))
            for layer in clip.layers
        ),
        root_settings=capture_settings(layers[0], None, None),
    )
    assert (clip.start_frame, clip.end_frame) == (10, 30)
    settings = []
    for item in clip.root_settings:
        if item.curve is not None:
            curve = item.curve
            item = replace(
                item,
                curve=replace(
                    curve,
                    seconds_per_frame=1 / 30,
                    keys=tuple(
                        replace(key, frame=key.frame * 30 / 24)
                        for key in curve.keys
                    ),
                ),
            )
        settings.append(item)
    clip = replace(clip, root_settings=tuple(settings))
    weights = {
        layer: _values(cmds, layer + ".weight", (0, 10, 30, 40))
        for layer in layers
    }
    cmds.file(new=True, force=True)
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], to_start_frame=100, to_end_frame=140)
    mod.do_it_dg()
    for layer in layers:
        assert _times(cmds, layer + ".weight") == [80, 100, 140, 160]
        assert _values(
            cmds, layer + ".weight", (80, 100, 140, 160)
        ) == pytest.approx(weights[layer])
