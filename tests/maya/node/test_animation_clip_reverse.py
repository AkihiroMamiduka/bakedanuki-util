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
from bd_util.maya.node.operator.attr import AnimCurveData, KeyData
from test_animation_clip_time import _layered_clip

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]

RATE = 1 / 24


def _key(
    frame,
    value,
    *,
    in_type="fixed",
    out_type="fixed",
    in_xy=(1.0, -0.5),
    out_xy=(2.0, 0.75),
    tangents_locked=False,
    weights_locked=False,
    breakdown=False,
):
    return KeyData(
        frame=frame,
        value=value,
        in_tangent_type=in_type,
        out_tangent_type=out_type,
        in_tangent_xy=in_xy,
        out_tangent_xy=out_xy,
        tangents_locked=tangents_locked,
        weights_locked=weights_locked,
        breakdown=breakdown,
    )


def _curve(
    keys,
    *,
    rate=RATE,
    curve_type="animCurveTL",
    weighted=True,
    pre="linear",
    post="cycleRelative",
):
    return AnimCurveData(
        curve_type=curve_type,
        seconds_per_frame=rate,
        weighted=weighted,
        pre_infinity=pre,
        post_infinity=post,
        keys=tuple(keys),
    )


def _clip(curves, *, start=-2.5, end=4.5, **kwargs):
    return AnimationClip(
        nodes=(
            NodeAnimationData(
                "source",
                tuple(
                    ChannelAnimationData(attribute, None, curve)
                    for attribute, curve in curves
                ),
            ),
        ),
        layers=(),
        layer_mode="flatten",
        start_frame=start,
        end_frame=end,
        seconds_per_frame=RATE,
        **kwargs,
    )


def _set_keys(cmds, plug, values, *, tangent="fixed", weighted=False):
    initial_tangent = "linear" if tangent == "fixed" else tangent
    for frame, value in values:
        cmds.setKeyframe(
            plug,
            time=frame,
            value=value,
            inTangentType=initial_tangent,
            outTangentType=initial_tangent,
        )
    cmds.keyTangent(plug, edit=True, weightedTangents=weighted)
    if tangent == "fixed":
        options = dict(
            inTangentType="fixed",
            outTangentType="fixed",
            inAngle=-25,
            outAngle=35,
            lock=False,
        )
        if weighted:
            options.update(inWeight=1.25, outWeight=2.5, weightLock=False)
        cmds.keyTangent(plug, edit=True, time=(17, 17), **options)


def _values(cmds, plug, frames):
    return [cmds.getAttr(plug, time=frame) for frame in frames]


def test_reversed_returns_independent_schema_2_data_and_is_involutive(
    tmp_path,
):
    keys = (
        _key(
            -2.5,
            2,
            in_type="linear",
            out_type="fixed",
            tangents_locked=True,
        ),
        _key(
            1.25,
            7,
            in_type="fixed",
            out_type="spline",
            in_xy=(3, 1),
            out_xy=(4, -2),
            weights_locked=True,
            breakdown=True,
        ),
        _key(
            4.5,
            -3,
            in_type="flat",
            out_type="linear",
            in_xy=(5, 3),
            out_xy=(6, -4),
        ),
    )
    clip = _clip(
        (("translate.translateX", _curve(keys)),),
        clipped=True,
        sample_by=0.5,
    )
    original = clip.to_json()

    result = clip.reversed()
    curve = result.nodes[0].channels[0].curve
    assert result is not clip
    assert result.schema_version == 2
    assert (
        result.start_frame,
        result.end_frame,
        result.seconds_per_frame,
        result.sample_by,
        result.clipped,
        result.layer_mode,
    ) == (-2.5, 4.5, RATE, 0.5, True, "flatten")
    assert [key.frame for key in curve.keys] == [-2.5, 0.75, 4.5]
    assert [key.value for key in curve.keys] == [-3, 7, 2]
    assert (curve.pre_infinity, curve.post_infinity) == (
        "cycleRelative",
        "linear",
    )
    assert curve.keys[0].in_tangent_type == "linear"
    assert curve.keys[0].in_tangent_xy == (6, 4)
    assert curve.keys[-1].out_tangent_type == "linear"
    assert curve.keys[-1].out_tangent_xy == (1, 0.5)
    assert curve.keys[1].breakdown
    assert curve.keys[1].weights_locked
    assert clip.to_json() == original
    assert result.reversed() == clip
    assert AnimationClip.load(result.save(tmp_path / "reverse.json")) == result

    result.nodes[0].channels[0].curve.keys[0].value = 999
    assert clip.to_json() == original


def test_empty_and_single_key_curves_are_kept():
    clip = _clip(
        (
            ("translate.translateX", _curve((_key(1, 8),))),
            ("translate.translateY", _curve(())),
        ),
        start=-2,
        end=6,
    )
    result = clip.reversed()
    assert [key.frame for key in result.nodes[0].channels[0].curve.keys] == [3]
    assert not result.nodes[0].channels[1].curve.keys
    assert result.reversed() == clip

    one_time = _clip(
        (("translate.translateX", _curve((_key(10, 8),))),),
        start=10,
        end=10,
    )
    assert one_time.reversed().reversed() == one_time
    assert one_time.reversed().nodes[0].channels[0].curve.keys[0].frame == 10


@pytest.mark.parametrize("attr", ["tx", "rx", "sx"])
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("tangent", ["fixed", "linear", "auto"])
def test_continuous_curve_evaluation_is_mirrored(
    maya_cmds, attr, weighted, tangent
):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    target = cmds.createNode("transform", name="target")
    _set_keys(
        cmds,
        source + "." + attr,
        ((10, 2), (17, 9), (30, -4)),
        tangent=tangent,
        weighted=weighted,
    )
    clip = AnimationClip.capture(
        [source], attributes=[attr], layer_mode="preserve"
    )
    original = clip.to_json()
    result = clip.reversed()
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()

    frames = [10 + index * 0.25 for index in range(81)]
    assert _values(cmds, target + "." + attr, frames) == pytest.approx(
        _values(cmds, source + "." + attr, [40 - frame for frame in frames]),
        rel=2e-5,
        abs=2e-5,
    )
    assert clip.to_json() == original
    after = bdu.Nodes().existing.transform(target)
    after_curve = getattr(after, attr).keyframe.get_curve_data()
    mod.undo_it()
    assert not cmds.keyframe(
        target + "." + attr, query=True, keyframeCount=True
    )
    mod.redo_it()
    assert getattr(after, attr).keyframe.get_curve_data() == after_curve


def test_step_and_stepnext_are_reversed_by_interval(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    target = cmds.createNode("transform", name="target")
    _set_keys(cmds, source + ".tx", ((10, 1), (20, 5), (30, 9)))
    cmds.keyTangent(
        source + ".tx", edit=True, time=(10, 10), outTangentType="step"
    )
    cmds.keyTangent(
        source + ".tx",
        edit=True,
        time=(20, 20),
        outTangentType="stepnext",
    )
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    result = clip.reversed()
    curve = result.nodes[0].channels[0].curve
    assert [key.out_tangent_type for key in curve.keys[:-1]] == [
        "step",
        "stepnext",
    ]
    assert result.reversed() == clip

    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    frames = [10, 10.001, 15, 19.999, 20, 20.001, 25, 29.999, 30]
    assert _values(cmds, target + ".tx", frames) == pytest.approx(
        _values(cmds, source + ".tx", [40 - frame for frame in frames])
    )


def test_input_only_step_type_does_not_create_a_step_interval():
    curve = _curve(
        (
            _key(10, 1, out_type="linear"),
            _key(20, 5, in_type="stepnext", out_type="linear"),
            _key(30, 9, in_type="linear"),
        )
    )
    clip = _clip((("translate.translateX", curve),), start=10, end=30)
    result = clip.reversed()
    assert (
        result.nodes[0].channels[0].curve.keys[0].out_tangent_type == "linear"
    )
    assert result.reversed() == clip


@pytest.mark.parametrize(
    "pre,post",
    [
        ("constant", "linear"),
        ("linear", "cycle"),
        ("cycle", "cycleRelative"),
        ("cycleRelative", "oscillate"),
        ("oscillate", "constant"),
    ],
)
def test_infinity_evaluation_is_mirrored(maya_cmds, pre, post):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    target = cmds.createNode("transform", name="target")
    _set_keys(
        cmds, source + ".tx", ((10, 2), (20, 8), (30, 5)), tangent="linear"
    )
    cmds.setInfinity(source + ".tx", preInfinite=pre, postInfinite=post)
    clip = AnimationClip.capture(
        [source], attributes=["tx"], layer_mode="preserve"
    )
    result = clip.reversed()
    curve = result.nodes[0].channels[0].curve
    assert (curve.pre_infinity, curve.post_infinity) == (post, pre)
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    frames = [-20, -5, 0, 5, 10, 20, 30, 35, 40, 45, 60]
    assert _values(cmds, target + ".tx", frames) == pytest.approx(
        _values(cmds, source + ".tx", [40 - frame for frame in frames]),
        rel=2e-6,
        abs=2e-6,
    )


def _settings(curve=None):
    return tuple(
        LayerSettingData(
            name,
            0.5 if name == "weight" else 0.0,
            curve if name == "weight" else None,
        )
        for name in LAYER_SETTINGS
    )


def test_layer_and_root_settings_use_common_seconds_axis_with_external_keys():
    channel = _curve((_key(10, 2), _key(30, 8)))
    layer_curve = _curve((_key(0, 0.25), _key(40, 0.75)))
    root_curve = _curve(
        (_key(0, 0.1), _key(60, 0.9)),
        rate=1 / 30,
        curve_type="animCurveTU",
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
    result = clip.reversed()
    layer = next(item for item in result.layers[0].settings if item.curve)
    root = next(item for item in result.root_settings if item.curve)
    assert [key.frame for key in layer.curve.keys] == pytest.approx([0, 40])
    assert [key.value for key in layer.curve.keys] == [0.75, 0.25]
    assert [key.frame for key in root.curve.keys] == pytest.approx([-10, 50])
    assert [key.value for key in root.curve.keys] == [0.9, 0.1]
    twice = result.reversed()
    assert [
        key.frame for key in twice.root_settings[4].curve.keys
    ] == pytest.approx([0, 60])
    assert twice.nodes == clip.nodes
    assert twice.layers == clip.layers


@pytest.mark.parametrize("weighted", [False, True])
def test_reversed_layered_clip_restores_mirrored_composite_and_settings(
    maya_cmds, weighted
):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(cmds, weighted=weighted)
    frames = [10 + index * 0.5 for index in range(41)]
    mirrored = [40 - frame for frame in frames]
    expected = _values(cmds, source + ".tx", mirrored)
    expected_weights = {
        layer: _values(cmds, layer + ".weight", mirrored) for layer in layers
    }
    result = clip.reversed()

    cmds.file(new=True, force=True)
    target = cmds.createNode("transform", name="target")
    mod = bdu.ModifierManager()
    result.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    assert _values(cmds, target + ".tx", frames) == pytest.approx(
        expected, abs=2e-6
    )
    for layer in layers:
        assert _values(cmds, layer + ".weight", frames) == pytest.approx(
            expected_weights[layer], abs=2e-6
        )
    mod.undo_it()
    assert not cmds.keyframe(target + ".tx", query=True, keyframeCount=True)
    assert not cmds.ls(type="animLayer")
    mod.redo_it()
    assert _values(cmds, target + ".tx", frames) == pytest.approx(
        expected, abs=2e-6
    )


@pytest.mark.parametrize(
    "field,value",
    [
        ("frame", float("nan")),
        ("out_tangent_type", "invalid"),
        ("in_tangent_xy", (-1, 0)),
    ],
)
def test_reversed_revalidates_mutated_keys_without_changing_scene(
    maya_cmds, field, value
):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    _set_keys(cmds, source + ".tx", ((10, 1), (30, 9)))
    clip = AnimationClip.capture([source], attributes=["tx"])
    setattr(clip.nodes[0].channels[0].curve.keys[0], field, value)
    pending = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=pending).create.transform(name="pending")
    cmds.currentTime(17)
    cmds.select(source)
    cmds.file(modified=False)
    with pytest.raises((TypeError, ValueError)):
        clip.reversed()
    assert not cmds.objExists("pending")
    assert cmds.currentTime(query=True) == 17
    assert cmds.ls(selection=True) == [source]
    assert not cmds.file(query=True, modified=True)
    assert not pending.can_undo


def test_reversed_restore_participates_in_rollback(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("transform", name="source")
    target = cmds.createNode("transform", name="target")
    _set_keys(cmds, source + ".tx", ((10, 1), (30, 9)))
    clip = AnimationClip.capture([source], attributes=["tx"]).reversed()
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")

    def reject(modifier):
        raise RuntimeError("later failure")

    mod.queue_dg_modifier(reject)
    with pytest.raises(RuntimeError, match="later failure"):
        mod.do_it_dg()
    assert not cmds.keyframe(target + ".tx", query=True, keyframeCount=True)
