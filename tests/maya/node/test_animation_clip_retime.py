from __future__ import annotations

from dataclasses import replace

import pytest

import bd_util as bdu
from bd_util.maya.node.animation_clip import (
    LAYER_SETTINGS,
    AnimationClip,
    AnimationLayerData,
    ChannelAnimationData,
    LayerSettingData,
    NodeAnimationData,
)
from test_animation_clip_reverse import RATE, _clip, _curve, _key
from test_animation_clip_time import _layered_clip

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _frames(curve):
    return [key.frame for key in curve.keys]


def _settings(curve):
    return tuple(
        LayerSettingData(
            name,
            0.5 if name == "weight" else 0.0,
            curve if name == "weight" else None,
        )
        for name in LAYER_SETTINGS
    )


@pytest.mark.parametrize(
    "timing,bounds",
    [
        ({}, (10, 30)),
        (dict(offset_frames=-10.5), (-0.5, 19.5)),
        (dict(to_start_frame=100), (100, 120)),
        (dict(to_end_frame=100), (80, 100)),
        (dict(time_scale=2), (10, 50)),
        (dict(time_scale=0.5, offset_frames=15), (25, 35)),
        (dict(time_scale=2, to_start_frame=100), (100, 140)),
        (dict(duration_frames=30, to_end_frame=100), (70, 100)),
        (dict(to_start_frame=100, to_end_frame=140), (100, 140)),
    ],
)
def test_placement_uses_saved_range_and_returns_independent_clip(
    timing, bounds
):
    clip = _clip(
        (
            (
                "translate.translateX",
                _curve((_key(10, 2), _key(20, 6), _key(30, 10))),
            ),
        ),
        start=10,
        end=30,
        clipped=True,
        sample_by=0.5,
    )
    original = clip.to_json()

    result = clip.retimed(**timing)

    assert result is not clip
    assert (result.start_frame, result.end_frame) == pytest.approx(bounds)
    assert _frames(result.nodes[0].channels[0].curve) == pytest.approx(
        [bounds[0], sum(bounds) / 2, bounds[1]]
    )
    assert (
        result.seconds_per_frame,
        result.sample_by,
        result.clipped,
        result.schema_version,
    ) == (RATE, 0.5, True, 2)
    assert AnimationClip.from_json(result.to_json()) == result
    result.nodes[0].channels[0].curve.keys[0].value = 999
    assert clip.to_json() == original


def test_common_axis_preserves_all_channel_details_and_empty_curves():
    a = NodeAnimationData(
        "a",
        (
            ChannelAnimationData(
                "translate.translateX",
                None,
                _curve(
                    (
                        _key(10, 2),
                        _key(
                            20,
                            6,
                            in_xy=(3, 1),
                            out_xy=(4, -2),
                            tangents_locked=True,
                            weights_locked=True,
                            breakdown=True,
                        ),
                        _key(30, 10),
                    )
                ),
            ),
            ChannelAnimationData(
                "rotate.rotateX",
                None,
                _curve((_key(15, 30), _key(25, 60)), curve_type="animCurveTA"),
            ),
        ),
    )
    b = NodeAnimationData(
        "b",
        (
            ChannelAnimationData(
                "visibility",
                None,
                _curve(
                    (_key(18, 0, out_type="step"), _key(25, 1)),
                    curve_type="animCurveTU",
                    weighted=False,
                ),
            ),
            ChannelAnimationData("translate.translateY", None, _curve(())),
        ),
    )
    clip = AnimationClip(
        nodes=(a, b),
        layers=(),
        layer_mode="flatten",
        start_frame=10,
        end_frame=30,
        seconds_per_frame=RATE,
    )

    result = clip.retimed(time_scale=2, to_start_frame=100)

    assert (result.start_frame, result.end_frame) == pytest.approx((100, 140))
    for source_node, target_node in zip(clip.nodes, result.nodes):
        assert source_node.name == target_node.name
        for source_channel, target_channel in zip(
            source_node.channels, target_node.channels
        ):
            source_curve, target_curve = (
                source_channel.curve,
                target_channel.curve,
            )
            assert (source_channel.attribute, source_channel.layer) == (
                target_channel.attribute,
                target_channel.layer,
            )
            assert replace(source_curve, keys=()) == replace(
                target_curve, keys=()
            )
            assert _frames(target_curve) == pytest.approx(
                [100 + (key.frame - 10) * 2 for key in source_curve.keys]
            )
            for old, new in zip(source_curve.keys, target_curve.keys):
                assert new.in_tangent_xy == pytest.approx(
                    (old.in_tangent_xy[0] * 2, old.in_tangent_xy[1])
                )
                assert new.out_tangent_xy == pytest.approx(
                    (old.out_tangent_xy[0] * 2, old.out_tangent_xy[1])
                )
                assert (
                    replace(
                        new,
                        frame=old.frame,
                        in_tangent_xy=old.in_tangent_xy,
                        out_tangent_xy=old.out_tangent_xy,
                    )
                    == old
                )


def test_layer_and_root_settings_outside_range_use_common_seconds_axis():
    channel = _curve((_key(10, 2), _key(30, 8)))
    layer_curve = _curve((_key(0, 0.25), _key(40, 0.75)))
    root_curve = _curve(
        (_key(0, 0.1), _key(60, 0.9)), rate=1 / 30, curve_type="animCurveTL"
    )
    clip = AnimationClip(
        nodes=(
            NodeAnimationData(
                "source",
                (
                    ChannelAnimationData(
                        "translate.translateX", "Upper", channel
                    ),
                ),
            ),
        ),
        layers=(AnimationLayerData("Upper", None, _settings(layer_curve)),),
        root_settings=_settings(root_curve),
        layer_mode="preserve",
        start_frame=10,
        end_frame=30,
        seconds_per_frame=RATE,
    )

    result = clip.retimed(time_scale=2, to_start_frame=100)
    layer = result.layers[0].settings[4].curve
    root = result.root_settings[4].curve

    assert _frames(result.nodes[0].channels[0].curve) == pytest.approx(
        [100, 140]
    )
    assert layer is not None and _frames(layer) == pytest.approx([80, 160])
    assert root is not None and _frames(root) == pytest.approx([100, 220])
    assert root.seconds_per_frame == 1 / 30
    assert [key.value for key in root.keys] == [0.1, 0.9]
    assert result.layers[0].settings[0] == clip.layers[0].settings[0]
    assert clip.layers[0].settings[4].curve == layer_curve


def test_retimed_uses_saved_frames_independently_of_maya_ui_unit(maya_cmds):
    cmds = maya_cmds
    cmds.currentUnit(time="film")
    try:
        clip = _clip(
            (("translate.translateX", _curve((_key(10, 2), _key(30, 8)))),),
            start=10,
            end=30,
        )
        cmds.currentUnit(time="ntsc")
        result = clip.retimed(duration_frames=48, to_start_frame=24)
        assert (result.start_frame, result.end_frame) == pytest.approx(
            (24, 72)
        )
        assert _frames(result.nodes[0].channels[0].curve) == pytest.approx(
            [24, 72]
        )

        target = cmds.createNode("transform", name="target")
        mod = bdu.ModifierManager()
        result.restore(mod, targets=[target], mode="replace_all")
        assert not cmds.keyframe(
            target + ".tx", query=True, keyframeCount=True
        )
        mod.do_it_dg()
        assert cmds.keyframe(
            target + ".tx", query=True, timeChange=True
        ) == pytest.approx([30, 90])
        mod.undo_it()
        assert not cmds.keyframe(
            target + ".tx", query=True, keyframeCount=True
        )
        mod.redo_it()
        assert cmds.keyframe(
            target + ".tx", query=True, timeChange=True
        ) == pytest.approx([30, 90])
    finally:
        cmds.currentUnit(time="film")


def test_retimed_layered_clip_restores_composite_and_settings(maya_cmds):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(cmds, weighted=True)
    source_frames = [10 + index * 0.5 for index in range(41)]
    expected = [
        cmds.getAttr(source + ".tx", time=frame) for frame in source_frames
    ]
    weights = {
        layer: [
            cmds.getAttr(layer + ".weight", time=frame)
            for frame in source_frames
        ]
        for layer in layers
    }
    result = clip.retimed(time_scale=2, to_start_frame=100)
    cmds.file(new=True, force=True)
    target = cmds.createNode("transform", name="target")
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    target_frames = [100 + index for index in range(41)]
    assert [
        cmds.getAttr(target + ".tx", time=frame) for frame in target_frames
    ] == pytest.approx(expected, abs=2e-6)
    for layer in layers:
        assert [
            cmds.getAttr(layer + ".weight", time=frame)
            for frame in target_frames
        ] == pytest.approx(weights[layer], abs=2e-6)


def test_retimed_discrete_attribute_keeps_step_values_on_restore(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    target = cmds.createNode("transform", name="target")
    cmds.setKeyframe(source + ".visibility", time=10, value=0)
    cmds.setKeyframe(source + ".visibility", time=30, value=1)
    clip = bdu.AnimationClip.capture(
        [source], attributes=["visibility"], layer_mode="preserve"
    )
    result = clip.retimed(time_scale=2, to_start_frame=100)
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    assert [
        cmds.getAttr(target + ".visibility", time=frame)
        for frame in (100, 120, 139, 140)
    ] == [0, 0, 0, 1]


@pytest.mark.parametrize(
    "timing,error",
    [
        (dict(time_scale=0), ValueError),
        (dict(time_scale=-1), ValueError),
        (dict(time_scale=float("nan")), ValueError),
        (dict(time_scale=True), TypeError),
        (dict(duration_frames=0), ValueError),
        (dict(duration_frames="30"), TypeError),
        (dict(time_scale=2, duration_frames=30), ValueError),
        (dict(offset_frames=1, to_start_frame=100), ValueError),
        (dict(offset_frames=1, to_end_frame=100), ValueError),
        (dict(to_start_frame=100, to_end_frame=100), ValueError),
        (dict(to_start_frame=100, to_end_frame=90), ValueError),
        (dict(to_start_frame=100, to_end_frame=140, time_scale=2), ValueError),
        (
            dict(to_start_frame=100, to_end_frame=140, duration_frames=40),
            ValueError,
        ),
        (dict(to_start_frame=1e100), ValueError),
        (dict(time_scale=1e-100), ValueError),
    ],
)
def test_invalid_retime_does_not_change_source(timing, error):
    clip = _clip(
        (("translate.translateX", _curve((_key(10, 2), _key(30, 8)))),),
        start=10,
        end=30,
    )
    original = clip.to_json()
    with pytest.raises(error):
        clip.retimed(**timing)
    assert clip.to_json() == original


def test_single_time_and_empty_clips():
    clip = _clip(
        (("translate.translateX", _curve((_key(10, 7),))),), start=10, end=10
    )
    result = clip.retimed(time_scale=2, to_end_frame=-0.25)
    assert (result.start_frame, result.end_frame) == pytest.approx(
        (-0.25, -0.25)
    )
    assert _frames(result.nodes[0].channels[0].curve) == pytest.approx([-0.25])
    with pytest.raises(ValueError, match="single-time"):
        clip.retimed(duration_frames=10)
    with pytest.raises(ValueError, match="single-time"):
        clip.retimed(to_start_frame=10, to_end_frame=20)

    empty = AnimationClip(
        nodes=(),
        layers=(),
        layer_mode="flatten",
        start_frame=10,
        end_frame=30,
        seconds_per_frame=RATE,
    )
    shifted = empty.retimed(time_scale=2, to_end_frame=100)
    assert (shifted.start_frame, shifted.end_frame) == pytest.approx((60, 100))
    assert not shifted.nodes


def test_precision_collision_is_rejected_without_partial_result():
    clip = _clip(
        (
            (
                "translate.translateX",
                _curve((_key(10, 2), _key(10.000001, 6), _key(30, 8))),
            ),
        ),
        start=10,
        end=30,
    )
    original = clip.to_json()
    with pytest.raises(ValueError, match="coincide"):
        clip.retimed(time_scale=2, to_start_frame=1e12)
    assert clip.to_json() == original


def test_retimed_revalidates_mutated_keys_without_touching_scene(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    for frame, value in ((10, 2), (30, 8)):
        cmds.setKeyframe(source + ".tx", time=frame, value=value)
    clip = bdu.AnimationClip.capture([source], attributes=["tx"])
    pending = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=pending).create.transform(name="pending")
    cmds.currentTime(17)
    cmds.select(source)
    cmds.file(modified=False)

    clip.nodes[0].channels[0].curve.keys[0].value = float("nan")
    with pytest.raises(ValueError):
        clip.retimed(time_scale=2)

    assert not cmds.objExists("pending")
    assert cmds.currentTime(query=True) == 17
    assert cmds.ls(selection=True) == [source]
    assert not cmds.file(query=True, modified=True)
    assert not pending.can_undo


def test_retimed_restore_joins_rollback(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    target = cmds.createNode("transform", name="target")
    for frame, value in ((10, 2), (20, 6), (30, 10)):
        cmds.setKeyframe(source + ".tx", time=frame, value=value)
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    result = clip.retimed(time_scale=2, to_start_frame=100)
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")

    def reject(modifier):
        raise RuntimeError("later failure")

    mod.queue_dg_modifier(reject)
    with pytest.raises(RuntimeError, match="later failure"):
        mod.do_it_dg()
    assert not cmds.keyframe(target + ".tx", query=True, keyframeCount=True)
    assert cmds.keyframe(source + ".tx", query=True, timeChange=True) == [
        10,
        20,
        30,
    ]
