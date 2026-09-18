from __future__ import annotations

import math
from dataclasses import replace

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.animation_clip import NodeAnimationData
from bd_util.maya.node.operator.attr import _keyframe_snapshot as snapshot
from test_animation_clip import _node, _values
from test_animation_clip_time import _keys, _layered_clip, _times

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


@pytest.fixture(autouse=True)
def units(maya_cmds):
    maya_cmds.currentUnit(time="film", angle="deg", linear="cm")
    yield
    maya_cmds.currentUnit(time="film", angle="deg", linear="cm")


def _clip(cmds, mode="preserve"):
    source = _node(cmds, "source", ((0, 0), (20, 20), (40, 0)))
    return source, bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=mode, sample_by=20
    )


def _data(node, attr="tx"):
    return bdu.Nodes().existing(node)[attr].keyframe.get_curve_data()


def _state(cmds):
    return (
        sorted(cmds.ls()),
        cmds.file(query=True, modified=True),
        cmds.currentTime(query=True),
        cmds.ls(selection=True),
        cmds.undoInfo(query=True, undoName=True),
        cmds.undoInfo(query=True, redoName=True),
    )


def _assert_same_curve(actual, expected):
    assert replace(actual, keys=()) == replace(expected, keys=())
    assert len(actual.keys) == len(expected.keys)
    for a, b in zip(actual.keys, expected.keys):
        assert (
            replace(
                a,
                in_tangent_xy=b.in_tangent_xy,
                out_tangent_xy=b.out_tangent_xy,
            )
            == b
        )
        for left, right in (
            (a.in_tangent_xy, b.in_tangent_xy),
            (a.out_tangent_xy, b.out_tangent_xy),
        ):
            if actual.weighted:
                assert left == pytest.approx(right, abs=1e-12)
            else:
                assert math.atan2(left[1], left[0]) == pytest.approx(
                    math.atan2(right[1], right[0]), abs=1e-12
                )


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize("mode", ["merge", "replace_range", "replace_all"])
@pytest.mark.parametrize(
    "bounds,expected",
    [
        ((10, 30), [10, 20, 30]),
        ((None, 30), [0, 20, 30]),
        ((10, None), [10, 20, 40]),
        ((10.25, 12.5), [10.25, 12.5]),
        ((15, 15), [15]),
        ((20, 20), [20]),
        ((0, 40), [0, 20, 40]),
    ],
)
def test_range_modes_boundaries_and_history(
    maya_cmds, layer_mode, mode, bounds, expected
):
    cmds = maya_cmds
    source, clip = _clip(cmds, layer_mode)
    original = clip.to_json()
    target = _node(cmds, "target", ((-5, -10), (12, 500), (45, -20)))
    before = _data(target)
    mod = bdu.ModifierManager()
    assert (
        clip.restore(
            mod,
            targets=[target],
            start_frame=bounds[0],
            end_frame=bounds[1],
            mode=mode,
        )
        is None
    )
    assert _data(target) == before
    assert clip.to_json() == original
    mod.do_it_dg()
    actual = _times(cmds, target + ".tx")
    remaining = [] if mode == "replace_all" else [-5, 45]
    if mode == "merge" or (
        mode == "replace_range" and not expected[0] <= 12 <= expected[-1]
    ):
        remaining.append(12)
    assert actual == pytest.approx(sorted(set(expected + remaining)))
    assert _values(cmds, target + ".tx", expected) == pytest.approx(
        _values(cmds, source + ".tx", expected)
    )
    after = _data(target)
    frames = [-5 + i / 4 for i in range(201)]
    shape = _values(cmds, target + ".tx", frames)
    for _ in range(2):
        mod.undo_it()
        assert _data(target) == before
        mod.redo_it()
        _assert_same_curve(_data(target), after)
        assert _values(cmds, target + ".tx", frames) == pytest.approx(shape)
    assert clip.to_json() == original


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("tangent", tuple(snapshot._TANGENTS))
@pytest.mark.parametrize("attr", ["tx", "rx", "sx"])
def test_preserved_range_keeps_dense_shape_and_breakdowns(
    maya_cmds, weighted, tangent, attr
):
    cmds = maya_cmds
    source = _node(
        cmds,
        "source",
        ((0, 0), (10, 5), (20, -2), (30, 8), (40, 1)),
        attr=attr,
    )
    keyframe = bdu.Nodes().existing(source)[attr].keyframe
    curve = oma.MFnAnimCurve(keyframe.find_anim_curves()[0].m_obj)
    curve.setIsWeighted(weighted)
    for i in range(curve.numKeys):
        curve.setInTangentType(i, snapshot._TANGENTS[tangent])
        curve.setOutTangentType(i, snapshot._TANGENTS[tangent])
        curve.setIsBreakdown(i, i == 2)
    curve.setPreInfinityType(curve.kLinear)
    curve.setPostInfinityType(curve.kCycle)
    clip = bdu.AnimationClip.capture(
        [source], attributes=[attr], layer_mode="preserve"
    )
    before = clip.to_json()
    target = _node(cmds, "target", (), attr=attr)
    mod = bdu.ModifierManager()
    clip.restore(
        mod,
        targets=[target],
        start_frame=5.25,
        end_frame=34.75,
        mode="replace_all",
    )
    mod.do_it_dg()
    data = _data(target, attr)
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
    assert data.weighted == weighted
    assert (data.pre_infinity, data.post_infinity) == ("linear", "cycle")
    assert all(key.in_tangent_type == "fixed" for key in data.keys)
    assert all(
        key.out_tangent_type in ("fixed", "step", "stepnext")
        for key in data.keys
    )
    assert all(
        not key.tangents_locked and not key.weights_locked for key in data.keys
    )
    frames = [5.25 + 29.5 * i / 300 for i in range(301)]
    frames += [
        time + delta for time in (10, 20, 30) for delta in (-0.001, 0, 0.001)
    ]
    assert _values(cmds, target + "." + attr, frames) == pytest.approx(
        _values(cmds, source + "." + attr, frames), rel=2e-6, abs=2e-7
    )
    assert clip.to_json() == before


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "timing,expected",
    [
        ({}, (10, 30)),
        ({"offset_frames": -20.5}, (-10.5, 9.5)),
        ({"to_start_frame": 100}, (100, 120)),
        ({"to_end_frame": 100}, (80, 100)),
        ({"time_scale": 2}, (10, 50)),
        ({"time_scale": 2, "to_end_frame": 100}, (60, 100)),
        ({"duration_frames": 15, "to_start_frame": 100}, (100, 115)),
        ({"to_start_frame": 100, "to_end_frame": 140}, (100, 140)),
    ],
)
def test_crop_precedes_all_time_transforms(
    maya_cmds, layer_mode, timing, expected
):
    cmds = maya_cmds
    source, clip = _clip(cmds, layer_mode)
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], start_frame=10, end_frame=30, **timing)
    mod.do_it_dg()
    frames = [expected[0], sum(expected) / 2, expected[1]]
    assert _times(cmds, target + ".tx") == pytest.approx(frames)
    assert _values(cmds, target + ".tx", frames) == pytest.approx([10, 20, 10])


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_saved_source_units_destination_units_and_queued_copy(
    maya_cmds, layer_mode
):
    cmds = maya_cmds
    source, clip = _clip(cmds, layer_mode)
    targets = [_node(cmds, name, ()) for name in ("first", "second")]
    cmds.currentUnit(time="ntsc")
    mod = bdu.ModifierManager()
    clip.restore(
        mod,
        targets=[targets[0]],
        start_frame=10,
        end_frame=30,
        to_start_frame=90,
    )
    clip.restore(
        mod,
        targets=[targets[1]],
        start_frame=20,
        end_frame=30,
        to_start_frame=120,
    )
    cmds.delete(source)
    clip.nodes[0].channels[0].curve.keys[1].value = 999
    cmds.currentUnit(time="pal")
    mod.do_it_dg()
    assert _times(cmds, targets[0] + ".tx") == pytest.approx(
        [75, 75 + 10 * 25 / 24, 75 + 20 * 25 / 24]
    )
    assert _values(
        cmds, targets[0] + ".tx", _times(cmds, targets[0] + ".tx")
    ) == pytest.approx([10, 20, 10])
    assert _times(cmds, targets[1] + ".tx") == pytest.approx(
        [100, 100 + 10 * 25 / 24]
    )


@pytest.mark.parametrize("clipped", [False, True])
@pytest.mark.parametrize("weighted", [False, True])
def test_root_and_layer_settings_crop_transform_and_reuse(
    maya_cmds, clipped, weighted
):
    cmds = maya_cmds
    source, clip, layers = _layered_clip(
        cmds, clipped=clipped, weighted=weighted
    )
    original = clip.to_json()
    source_frames = [17.5, 20, 22.5]
    expected = _values(cmds, source + ".tx", source_frames)
    weights = {
        name: _values(cmds, name + ".weight", source_frames) for name in layers
    }
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(
        mod,
        targets=[target],
        start_frame=17.5,
        end_frame=22.5,
        mode="replace_range",
    )
    mod.do_it_dg()
    for name in layers:
        assert _times(cmds, name + ".weight") == [10, 30]
    assert _values(cmds, target + ".tx", source_frames) == pytest.approx(
        expected
    )
    mod.undo_it()
    clip.restore(
        mod,
        targets=[target],
        start_frame=17.5,
        end_frame=22.5,
        to_start_frame=100,
        to_end_frame=120,
    )
    with pytest.raises(ValueError, match="settings differ"):
        mod.do_it_dg()
    clip.restore(
        mod,
        targets=[target],
        start_frame=17.5,
        end_frame=22.5,
        to_start_frame=100,
        to_end_frame=120,
        restore_layer_settings=True,
    )
    mod.do_it_dg()
    for name in layers:
        assert _times(cmds, name + ".weight") == [100, 120]
        assert _values(
            cmds, name + ".weight", [100, 110, 120]
        ) == pytest.approx(weights[name])
    assert _values(cmds, target + ".tx", [100, 110, 120]) == pytest.approx(
        expected
    )
    clip.restore(
        mod,
        targets=[target],
        start_frame=17.5,
        end_frame=22.5,
        to_start_frame=100,
        to_end_frame=120,
    )
    mod.do_it_dg()
    assert clip.to_json() == original


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
        ({"start_frame": 1e30}, ValueError),
        (
            {"start_frame": 20, "end_frame": 20, "duration_frames": 10},
            ValueError,
        ),
        (
            {
                "start_frame": 20,
                "end_frame": 20,
                "to_start_frame": 0,
                "to_end_frame": 10,
            },
            ValueError,
        ),
        ({"start_frame": 1e-20, "end_frame": 2e-20}, ValueError),
    ],
)
def test_invalid_range_does_not_book_edits(maya_cmds, kwargs, error):
    cmds = maya_cmds
    _, clip = _clip(cmds)
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    cmds.file(modified=False)
    before = _state(cmds)
    with pytest.raises(error):
        clip.restore(mod, targets=[target], **kwargs)
    assert _state(cmds) == before
    mod.do_it_dg()
    assert not _times(cmds, target + ".tx")


@pytest.mark.parametrize("dirty", [False, True])
@pytest.mark.parametrize(
    "stage", [None, "restore", "boundary", "capture", "second_channel"]
)
def test_booking_and_failure_preserve_scene_and_pending_edits(
    maya_cmds, monkeypatch, dirty, stage
):
    cmds = maya_cmds
    source, clip = _clip(cmds)
    clip = replace(
        clip, nodes=(clip.nodes[0], replace(clip.nodes[0], name="otherSource"))
    )
    before = clip.to_json()
    cmds.delete(source)
    targets = [_node(cmds, name, ()) for name in ("target", "second")]
    cmds.setAttr(targets[0] + ".ty", 5)
    cmds.undo()
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    nodes.create.multiplyDivide(name="pending")
    nodes.existing(targets[0]).ty.set(9)
    calls = 0
    handles = []
    name = {
        "restore": "_restore_working_data",
        "boundary": "_complete_boundaries",
        "capture": "_capture_working_data",
    }.get(stage, "_capture_working_data")
    original = getattr(snapshot, name)

    def injected(work, *args, **kwargs):
        nonlocal calls
        calls += 1
        handles.append(om.MObjectHandle(work.object()))
        result = original(work, *args, **kwargs)
        if stage is not None and (stage != "second_channel" or calls == 2):
            raise RuntimeError("crop failure")
        return result

    monkeypatch.setattr(snapshot, name, injected)
    cmds.file(modified=dirty)
    scene = _state(cmds)
    if stage is None:
        clip.restore(mod, targets=targets, start_frame=10, end_frame=30)
    else:
        with pytest.raises(RuntimeError, match="crop failure"):
            clip.restore(mod, targets=targets, start_frame=10, end_frame=30)
    assert _state(cmds) == scene
    assert handles and all(not handle.isAlive() for handle in handles)
    assert clip.to_json() == before
    assert not cmds.objExists("pending")
    mod.do_it_dg()
    assert cmds.objExists("pending")
    assert cmds.getAttr(targets[0] + ".ty") == 9
    assert bool(_times(cmds, targets[0] + ".tx")) == (stage is None)


def test_empty_nodes_and_channels_keep_mapping(maya_cmds):
    cmds = maya_cmds
    _, clip = _clip(cmds)
    node = clip.nodes[0]
    empty_channel = replace(
        node.channels[0],
        attribute="translateY",
        curve=replace(node.channels[0].curve, keys=()),
    )
    clip = replace(
        clip,
        nodes=(
            NodeAnimationData("empty", ()),
            replace(node, channels=(*node.channels, empty_channel)),
        ),
    )
    targets = [_node(cmds, name, ()) for name in ("emptyTarget", "target")]
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=targets, start_frame=10, end_frame=30)
    mod.do_it_dg()
    assert not _times(cmds, targets[0] + ".tx")
    assert _times(cmds, targets[1] + ".tx") == [10, 20, 30]
    assert not _times(cmds, targets[1] + ".ty")


@pytest.mark.parametrize("bounds", [(10.25, 29.75), (20, 20), (19.5, 20.5)])
def test_flatten_step_boundaries_keep_discrete_values(maya_cmds, bounds):
    cmds = maya_cmds
    source = _node(
        cmds, "source", ((0, 0), (20, 1), (40, 0)), attr="visibility"
    )
    cmds.keyTangent(source + ".visibility", edit=True, outTangentType="step")
    clip = bdu.AnimationClip.capture(
        [source], attributes=["visibility"], sample_by=20
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(
        mod, targets=[target], start_frame=bounds[0], end_frame=bounds[1]
    )
    mod.do_it_dg()
    frames = [
        bounds[0] + (bounds[1] - bounds[0]) * i / 200 for i in range(201)
    ]
    assert _values(cmds, target + ".visibility", frames) == _values(
        cmds, source + ".visibility", frames
    )


@pytest.mark.parametrize(
    "infinity", ["constant", "linear", "cycle", "cycleRelative", "oscillate"]
)
@pytest.mark.parametrize("bounds", [(0, 5), (35, 40), (0, 40)])
def test_short_channels_use_infinity_with_existing_clip_limits(
    maya_cmds, infinity, bounds
):
    cmds = maya_cmds
    source, _ = _clip(cmds)
    _keys(cmds, source + ".ty", ((10, 2), (30, 6)))
    cmds.setInfinity(
        source + ".ty", preInfinite=infinity, postInfinite=infinity
    )
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx", "ty"], layer_mode="preserve"
    )
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    if infinity not in ("constant", "linear"):
        with pytest.raises(RuntimeError, match="cyclic infinity"):
            clip.restore(
                mod,
                targets=[target],
                start_frame=bounds[0],
                end_frame=bounds[1],
            )
        mod.do_it_dg()
        assert not _times(cmds, target + ".tx")
        return
    clip.restore(
        mod, targets=[target], start_frame=bounds[0], end_frame=bounds[1]
    )
    mod.do_it_dg()
    frames = [
        bounds[0] + (bounds[1] - bounds[0]) * i / 100 for i in range(101)
    ]
    assert _values(cmds, target + ".ty", frames) == pytest.approx(
        _values(cmds, source + ".ty", frames)
    )


@pytest.mark.parametrize("rate", [1 / 24, 1 / 29.97, 0.123456789])
@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_reduced_json_clip_and_arbitrary_time_units(
    maya_cmds, rate, layer_mode
):
    cmds = maya_cmds
    source = _node(cmds, "source", [(-5 + i, float(i)) for i in range(11)])
    clip = bdu.AnimationClip.capture(
        [source], attributes=["tx"], layer_mode=layer_mode
    ).reduce_keys(tolerance=0)
    node = clip.nodes[0]
    channel = node.channels[0]
    clip = replace(
        clip,
        seconds_per_frame=rate,
        nodes=(
            replace(
                node,
                channels=(
                    replace(
                        channel,
                        curve=replace(channel.curve, seconds_per_frame=rate),
                    ),
                ),
            ),
        ),
    )
    clip = bdu.AnimationClip.from_json(clip.to_json())
    before = clip.to_json()
    cmds.delete(source)
    target = _node(cmds, "target", ())
    mod = bdu.ModifierManager()
    clip.restore(
        mod,
        targets=[target],
        start_frame=-2.75,
        end_frame=3.25,
        to_start_frame=-10.5,
        duration_frames=20,
    )
    mod.do_it_dg()
    assert _times(cmds, target + ".tx") == pytest.approx([-10.5, 9.5])
    assert _values(cmds, target + ".tx", [-10.5, -0.5, 9.5]) == pytest.approx(
        [2.25, 5.25, 8.25]
    )
    assert clip.to_json() == before


@pytest.mark.parametrize("layer_mode", ["flatten", "preserve"])
def test_range_restore_after_pending_creation_and_late_rollback(
    maya_cmds, layer_mode
):
    cmds = maya_cmds
    source = cmds.createNode("multiplyDivide")
    _keys(cmds, source + ".input1X", ((0, 0), (40, 40)))
    clip = bdu.AnimationClip.capture(
        [source], attributes=["input1X"], layer_mode=layer_mode, sample_by=40
    )
    mod = bdu.ModifierManager()
    pending = bdu.Nodes(modifier_manager=mod).create.multiplyDivide(
        name="pending"
    )
    clip.restore(mod, targets=[pending], start_frame=10, end_frame=30)
    assert not cmds.objExists("pending")
    mod.do_it_dg()
    assert _times(cmds, "pending.input1X") == [10, 30]
    target = _node(cmds, "target", ((0, 123), (40, 123)))
    _, clip = _clip(cmds, layer_mode)
    before = _data(target)
    clip.restore(
        mod,
        targets=[target],
        start_frame=10,
        end_frame=30,
        mode="replace_range",
    )

    def fail(modifier):
        raise RuntimeError("later failure")

    mod.queue_dg_modifier(fail)
    with pytest.raises(RuntimeError, match="later failure"):
        mod.do_it_dg()
    assert _data(target) == before
    assert _times(cmds, "pending.input1X") == [10, 30]


def test_unbounded_restore_bypasses_clipping(maya_cmds, monkeypatch):
    cmds = maya_cmds
    _, clip = _clip(cmds)
    target = _node(cmds, "target", ())

    def fail(*args):
        raise AssertionError("unbounded restore must not crop")

    monkeypatch.setattr(snapshot, "clip_curve_data", fail)
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], start_frame=None, end_frame=None)
    mod.do_it_dg()
    assert _times(cmds, target + ".tx") == [0, 20, 40]
