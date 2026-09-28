from __future__ import annotations

from dataclasses import replace

import pytest
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.animation_clip import NodeAnimationData
from bd_util.maya.node.operator.attr import _keyframe_snapshot as snapshot

from test_animation_clip import _node, _values
from test_animation_clip_range import _assert_same_curve, _clip, _data, _state
from test_animation_clip_time import _keys, _layered_clip, _times

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


@pytest.fixture(autouse=True)
def units(maya_cmds):
    maya_cmds.currentUnit(time="film", angle="deg", linear="cm")
    yield
    maya_cmds.currentUnit(time="film", angle="deg", linear="cm")


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "bounds,expected",
    [
        ((None, None), [0, 20, 40]),
        ((10, 30), [10, 20, 30]),
        ((None, 30), [0, 20, 30]),
        ((10, None), [10, 20, 40]),
        ((20, 20), [20]),
        ((0, 40), [0, 20, 40]),
    ],
)
def test_trimmed_range_metadata_and_independent_copy(
    maya_cmds, layer_mode, bounds, expected
):
    _, clip = _clip(maya_cmds, layer_mode)
    original = clip.to_json()
    result = clip.trimmed(*bounds)

    assert result is not clip
    assert (result.start_frame, result.end_frame) == (
        0 if bounds[0] is None else bounds[0],
        40 if bounds[1] is None else bounds[1],
    )
    assert result.clipped == (bounds != (None, None))
    assert result.seconds_per_frame == clip.seconds_per_frame
    assert result.sample_by == clip.sample_by
    assert result.schema_version == clip.schema_version
    assert result.layer_mode == clip.layer_mode
    assert [
        key.frame for key in result.nodes[0].channels[0].curve.keys
    ] == expected
    assert bdu.AnimationClip.from_json(result.to_json()) == result
    if bounds == (None, None):
        assert result == clip

    result.nodes[0].channels[0].curve.keys[0].value = -999
    assert clip.to_json() == original


def test_unbounded_trim_preserves_existing_clipped_data(
    maya_cmds, monkeypatch
):
    _, clip = _clip(maya_cmds)
    clipped = clip.trimmed(10, 30)

    def fail(*args):
        raise AssertionError("unbounded trim must not crop")

    monkeypatch.setattr(snapshot, "clip_curve_data", fail)
    result = clipped.trimmed()
    assert result == clipped
    assert result is not clipped
    assert result.clipped
    result.nodes[0].channels[0].curve.keys[0].value = -999
    assert result != clipped


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("bounds", [(10, 30), (None, 30), (20, 20)])
def test_trimmed_restore_matches_direct_range_restore_with_history(
    maya_cmds, layer_mode, bounds
):
    cmds = maya_cmds
    source, clip = _clip(cmds, layer_mode)
    direct = _node(cmds, "direct", ())
    saved = _node(cmds, "saved", ())
    partial = bdu.AnimationClip.from_json(clip.trimmed(*bounds).to_json())
    cmds.delete(source)

    mod = bdu.ModifierManager()
    clip.restore(
        mod,
        targets=[direct],
        start_frame=bounds[0],
        end_frame=bounds[1],
        mode="replace_all",
    )
    partial.restore(mod, targets=[saved], mode="replace_all")
    assert not _times(cmds, direct + ".tx")
    assert not _times(cmds, saved + ".tx")
    mod.do_it_dg()

    expected = _data(direct)
    _assert_same_curve(_data(saved), expected)
    frames = [
        partial.start_frame
        + (partial.end_frame - partial.start_frame) * i / 40
        for i in range(41)
    ]
    assert _values(cmds, saved + ".tx", frames) == pytest.approx(
        _values(cmds, direct + ".tx", frames)
    )
    for _ in range(2):
        mod.undo_it()
        assert not _times(cmds, direct + ".tx")
        assert not _times(cmds, saved + ".tx")
        mod.redo_it()
        _assert_same_curve(_data(saved), expected)


@pytest.mark.parametrize("attr", ["tx", "rx"])
def test_preserve_trimmed_keeps_shape_and_key_details(maya_cmds, attr):
    cmds = maya_cmds
    source = _node(
        cmds,
        "source",
        ((0, 0), (10, 5), (20, -2), (30, 8), (40, 1)),
        attr=attr,
    )
    curve = oma.MFnAnimCurve(
        bdu.Nodes().existing(source)[attr].keyframe.find_anim_curves()[0].m_obj
    )
    curve.setIsWeighted(True)
    curve.setIsBreakdown(2, True)
    curve.setPreInfinityType(curve.kLinear)
    curve.setPostInfinityType(curve.kCycle)
    clip = bdu.AnimationClip.capture(
        [source], attributes=[attr], layer_mode="preserve"
    )
    original = clip.to_json()

    result = clip.trimmed(5.25, 34.75)
    data = result.nodes[0].channels[0].curve
    assert data.curve_type == (
        "animCurveTA" if attr == "rx" else "animCurveTL"
    )
    assert data.weighted
    assert (data.pre_infinity, data.post_infinity) == ("linear", "cycle")
    assert [key.frame for key in data.keys] == pytest.approx(
        [5.25, 10, 20, 30, 34.75]
    )
    assert [key.breakdown for key in data.keys] == [
        False,
        False,
        True,
        False,
        False,
    ]
    assert all(key.in_tangent_type == "fixed" for key in data.keys)

    target = _node(cmds, "target", (), attr=attr)
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    frames = [5.25 + 29.5 * i / 100 for i in range(101)]
    assert _values(cmds, target + "." + attr, frames) == pytest.approx(
        _values(cmds, source + "." + attr, frames), rel=2e-6, abs=2e-7
    )
    assert clip.to_json() == original


def test_discrete_channel_and_empty_structure(maya_cmds):
    cmds = maya_cmds
    source = _node(
        cmds, "source", ((0, 0), (20, 1), (40, 0)), attr="visibility"
    )
    cmds.keyTangent(source + ".visibility", edit=True, outTangentType="step")
    clip = bdu.AnimationClip.capture(
        [source], attributes=["visibility"], sample_by=20
    )
    node = clip.nodes[0]
    empty = replace(
        node.channels[0],
        attribute="translateY",
        curve=replace(
            node.channels[0].curve, curve_type="animCurveTL", keys=()
        ),
    )
    clip = replace(
        clip,
        nodes=(
            NodeAnimationData("empty", ()),
            replace(node, channels=(node.channels[0], empty)),
        ),
    )
    result = clip.trimmed(10.25, 29.75)
    assert [node.name for node in result.nodes] == ["empty", source]
    assert result.nodes[0].channels == ()
    assert result.nodes[1].channels[1].curve.keys == ()
    discrete = result.nodes[1].channels[0].curve
    assert discrete.curve_type == "animCurveTU"
    assert [key.frame for key in discrete.keys] == pytest.approx(
        [10.25, 20, 29.75]
    )
    assert discrete.keys[0].out_tangent_type == "step"

    target = _node(cmds, "target", ())
    cmds.createNode("transform", name="empty")
    mod = bdu.ModifierManager()
    result.restore(mod, targets=["empty", target], mode="replace_all")
    mod.do_it_dg()
    frames = [10.25 + 19.5 * i / 100 for i in range(101)]
    assert _values(cmds, target + ".visibility", frames) == _values(
        cmds, source + ".visibility", frames
    )


def test_layer_and_root_settings_are_trimmed_and_json_roundtrip(maya_cmds):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(cmds, weighted=True)
    frames = [12.5, 20, 27.5]
    values = _values(cmds, source + ".tx", frames)
    weights = {
        layer: _values(cmds, layer + ".weight", frames) for layer in layers
    }
    original = clip.to_json()
    result = clip.trimmed(12.5, 27.5)
    result = bdu.AnimationClip.from_json(result.to_json())
    assert result.clipped
    assert [(layer.name, layer.parent) for layer in result.layers] == [
        (layer.name, layer.parent) for layer in clip.layers
    ]
    for settings in (
        result.root_settings,
        *(layer.settings for layer in result.layers),
    ):
        curve = next(item.curve for item in settings if item.name == "weight")
        assert curve is not None
        assert curve.weighted
        assert [key.frame for key in curve.keys] == pytest.approx([12.5, 27.5])
    assert clip.to_json() == original

    cmds.file(new=True, force=True)
    _node(cmds, source, ())
    mod = bdu.ModifierManager()
    result.restore(mod, restore_layer_settings=True)
    mod.do_it_dg()
    assert _values(cmds, source + ".tx", frames) == pytest.approx(values)
    for layer in layers:
        assert _values(cmds, layer + ".weight", frames) == pytest.approx(
            weights[layer]
        )
    mod.undo_it()
    assert not cmds.ls(type="animLayer")
    mod.redo_it()
    assert _values(cmds, source + ".tx", frames) == pytest.approx(values)


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"start_frame": -1}, ValueError),
        ({"end_frame": 41}, ValueError),
        ({"start_frame": 30, "end_frame": 10}, ValueError),
        ({"start_frame": True}, TypeError),
        ({"end_frame": "30"}, TypeError),
        ({"start_frame": float("nan")}, ValueError),
        ({"end_frame": float("inf")}, ValueError),
        ({"start_frame": 1e-20, "end_frame": 2e-20}, ValueError),
    ],
)
def test_invalid_trim_does_not_change_clip_or_scene(maya_cmds, kwargs, error):
    _, clip = _clip(maya_cmds)
    original = clip.to_json()
    maya_cmds.file(modified=False)
    scene = _state(maya_cmds)
    with pytest.raises(error):
        clip.trimmed(**kwargs)
    assert clip.to_json() == original
    assert _state(maya_cmds) == scene


def test_cyclic_infinity_outside_key_range_is_rejected(maya_cmds):
    cmds = maya_cmds
    source, _ = _clip(cmds)
    _keys(cmds, source + ".ty", ((10, 2), (30, 6)))
    cmds.setInfinity(source + ".ty", preInfinite="cycle", postInfinite="cycle")
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx", "ty"], layer_mode="preserve"
    )
    original = clip.to_json()
    cmds.file(modified=False)
    scene = _state(cmds)
    with pytest.raises(RuntimeError, match="cyclic infinity"):
        clip.trimmed(0, 40)
    assert clip.to_json() == original
    assert _state(cmds) == scene


def test_negative_subframe_and_mutated_input_validation(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source", ((-5, -5), (0, 0), (5, 5)))
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    result = clip.trimmed(-2.75, 3.25)
    assert (result.start_frame, result.end_frame) == (-2.75, 3.25)
    assert [
        key.frame for key in result.nodes[0].channels[0].curve.keys
    ] == pytest.approx([-2.75, 0, 3.25])
    assert [
        key.value for key in result.nodes[0].channels[0].curve.keys
    ] == pytest.approx([-2.75, 0, 3.25])

    clip.nodes[0].channels[0].curve.keys[0].value = float("nan")
    cmds.file(modified=False)
    scene = _state(cmds)
    with pytest.raises(ValueError):
        clip.trimmed()
    assert _state(cmds) == scene


def test_saved_time_unit_chaining_and_pending_edits(maya_cmds):
    cmds = maya_cmds
    source = _node(cmds, "source", ((0, 0), (20, 10), (40, 40)))
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=mod).existing(target).ty.set(9)
    cmds.currentUnit(time="ntsc")
    before = _state(cmds)
    shifted = clip.trimmed(10, 30).retimed(time_scale=2, to_start_frame=100)
    result = shifted.reversed()
    assert (result.start_frame, result.end_frame) == pytest.approx((100, 140))
    assert result.clipped
    assert [
        key.frame for key in result.nodes[0].channels[0].curve.keys
    ] == pytest.approx([100, 120, 140])
    assert _state(cmds) == before
    assert cmds.getAttr(target + ".ty") == 0
    result.restore(mod, targets=[target], mode="replace_all")
    assert not _times(cmds, target + ".tx")
    mod.do_it_dg()
    assert cmds.getAttr(target + ".ty") == 9
    assert _values(
        cmds, target + ".tx", [100 * 30 / 24, 120 * 30 / 24, 140 * 30 / 24]
    ) == pytest.approx([25, 10, 5])


def test_trimmed_restore_late_failure_rolls_back(maya_cmds):
    cmds = maya_cmds
    _, clip = _clip(cmds)
    target = _node(cmds, "target", ((0, -1), (40, -1)))
    before = _data(target)
    partial = clip.trimmed(10, 30)
    mod = bdu.ModifierManager()
    partial.restore(mod, targets=[target], mode="replace_all")

    def reject(modifier):
        raise RuntimeError("later failure")

    mod.queue_dg_modifier(reject)
    with pytest.raises(RuntimeError, match="later failure"):
        mod.do_it_dg()
    assert _data(target) == before

    partial.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    after = _data(target)
    mod.undo_it()
    assert _data(target) == before
    mod.redo_it()
    _assert_same_curve(_data(target), after)
