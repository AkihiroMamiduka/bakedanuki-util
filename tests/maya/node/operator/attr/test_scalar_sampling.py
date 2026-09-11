# coding: utf-8
from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr
from bd_util.maya.node.operator.node.dag.transform._core import Transform

pytestmark = [
    pytest.mark.maya,
    pytest.mark.filterwarnings("error::DeprecationWarning"),
]


class SamplingTransform(Transform):
    __slots__ = ()

    number = AddAttr.at.double()
    single = AddAttr.at.float()
    integer = AddAttr.at.long()
    short_value = AddAttr.at.short()
    byte_value = AddAttr.at.byte()
    char_value = AddAttr.at.char()
    float_angle = AddAttr.at.float_angle(default_value=0.0)
    float_linear = AddAttr.at.float_linear(default_value=0.0)
    duration = AddAttr.at.time(default_value=0.0)
    multi_number = AddAttr.at.double(multi=True)


@pytest.fixture(autouse=True)
def restore_sampling_state(new_scene, maya_cmds):
    units = {
        name: maya_cmds.currentUnit(query=True, **{name: True})
        for name in ("linear", "angle", "time")
    }
    maya_cmds.currentUnit(linear="cm", angle="deg", time="film")
    try:
        yield
    finally:
        maya_cmds.currentUnit(**units)


@pytest.fixture
def sampling_node(modifier_manager):
    node = SamplingTransform.create(modifier_manager, name="samplingTarget")
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()
    modifier_manager.clear()
    return node


def _keys(maya_cmds, plug, end_value=10.0):
    for frame, value in ((1.0, 0.0), (11.0, end_value)):
        maya_cmds.setKeyframe(
            plug.plug.name(),
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )


def _assert_samples(actual, expected):
    assert len(actual) == len(expected)
    for pair, expected_pair in zip(actual, expected):
        assert isinstance(pair, tuple)
        assert all(type(value) is float for value in pair)
        assert pair == pytest.approx(expected_pair, abs=1e-6)


def _replace_reader(monkeypatch, operator, read):
    original = operator.plug

    class ReadProbe:
        def __getattr__(self, name):
            return getattr(original, name)

        def asDouble(self):
            return read(original)

    monkeypatch.setattr(operator, "_m_plug", ReadProbe())


@pytest.mark.parametrize("changed_units", [False, True])
@pytest.mark.parametrize(
    "attribute,end_value,middle_value",
    [
        ("number", 10.0, 5.0),
        ("single", 10.0, 5.0),
        ("integer", 8.0, 4.0),
        ("short_value", 8.0, 4.0),
        ("byte_value", 8.0, 4.0),
        ("char_value", 8.0, 4.0),
        ("translateX", 10.0, 5.0),
        ("rotateX", 90.0, 45.0),
        ("float_linear", 10.0, 5.0),
        ("float_angle", 90.0, 45.0),
        ("duration", 24.0, 12.0),
        ("visibility", 1.0, 0.0),
        ("rotateOrder", 2.0, 0.0),
    ],
)
def test_sample_values_preserves_input_order_and_public_units(
    sampling_node, maya_cmds, attribute, end_value, middle_value, changed_units
):
    plug = getattr(sampling_node, attribute)
    _keys(maya_cmds, plug, end_value)
    if changed_units:
        maya_cmds.currentUnit(linear="m", angle="rad", time="ntsc")
    scale = 1.25 if changed_units else 1.0
    value_scale = scale if attribute == "duration" else 1.0
    maya_cmds.currentTime(3.0 * scale)
    current_value = plug.get()
    frames = [11.0 * scale, 1.0 * scale, 6.0 * scale, 11.0 * scale]

    samples = plug.sample_values(frames=iter(frames))

    _assert_samples(
        samples,
        list(
            zip(
                frames,
                [
                    end_value * value_scale,
                    0.0,
                    middle_value * value_scale,
                    end_value * value_scale,
                ],
            )
        ),
    )
    assert maya_cmds.currentTime(query=True) == 3.0 * scale
    assert om.MDGContext.current().isNormal()
    if isinstance(current_value, str):
        assert plug.get() == current_value
    else:
        assert plug.get() == pytest.approx(current_value)


@pytest.mark.parametrize(
    "constraint", ["pointConstraint", "parentConstraint", "orientConstraint"]
)
def test_sample_values_evaluates_constraint_result(
    sampling_node, maya_cmds, constraint
):
    driver_name = maya_cmds.createNode("transform", name="samplingDriver")
    driver = bdu.Nodes().existing(driver_name)
    attribute = "rotateY" if constraint == "orientConstraint" else "translateX"
    target_plug = getattr(sampling_node, attribute)
    maya_cmds.setAttr(target_plug.plug.name(), 5.0)
    getattr(maya_cmds, constraint)(
        driver_name, sampling_node.name, maintainOffset=True
    )
    _keys(maya_cmds, getattr(driver, attribute), 10.0)
    maya_cmds.currentTime(3.0)
    current_value = target_plug.get()

    samples = target_plug.sample_values(frames=[11, 1, 6])

    _assert_samples(samples, [(11.0, 15.0), (1.0, 5.0), (6.0, 10.0)])
    assert target_plug.keyframe.get_keys() == [(1.0, 0.0), (11.0, 10.0)]
    assert target_plug.get() == pytest.approx(current_value)
    assert maya_cmds.currentTime(query=True) == 3.0


def test_sample_values_evaluates_conversion_and_computed_output(
    sampling_node, maya_cmds
):
    _keys(maya_cmds, sampling_node.rotateX, 90.0)
    multiply = maya_cmds.createNode("multiplyDivide")
    maya_cmds.connectAttr(
        sampling_node.rotateX.plug.name(), multiply + ".input1X"
    )
    maya_cmds.setAttr(multiply + ".input2X", 3.0)
    output = bdu.Nodes().existing(multiply).outputX
    frames = [11.0, 1.0, 6.0]
    actual = output.sample_values(frames=frames)
    expected = [
        (f, maya_cmds.getAttr(output.plug.name(), time=f)) for f in frames
    ]
    _assert_samples(actual, expected)


def test_sample_values_evaluates_animation_layer_blend(
    sampling_node, maya_cmds
):
    plug = sampling_node.translateX
    _keys(maya_cmds, plug, 10.0)
    layer = maya_cmds.animLayer("samplingLayer", override=True)
    maya_cmds.animLayer(layer, edit=True, attribute=plug.plug.name())
    for frame, value in ((1.0, 20.0), (11.0, 40.0)):
        maya_cmds.setKeyframe(
            plug.plug.name(),
            animLayer=layer,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )
    maya_cmds.setAttr(layer + ".weight", 0.5)
    frames = [1.0, 6.0, 11.0]
    actual = plug.sample_values(frames=frames)
    expected = [
        (f, maya_cmds.getAttr(plug.plug.name(), time=f)) for f in frames
    ]
    _assert_samples(actual, expected)
    assert actual[-1][1] != 10.0


def test_sample_values_snapshots_before_constraint_removal_and_rekey(
    sampling_node, maya_cmds
):
    mod = sampling_node.modifier_manager
    driver_name = maya_cmds.createNode("transform")
    driver = bdu.Nodes().existing(driver_name)
    maya_cmds.setAttr(sampling_node.translateX.plug.name(), 5.0)
    constraint = maya_cmds.pointConstraint(
        driver_name, sampling_node.name, maintainOffset=True
    )[0]
    _keys(maya_cmds, driver.translateX)
    samples = sampling_node.translateX.sample_values(frames=range(1, 12))
    selection = om.MSelectionList()
    selection.add(constraint)
    mod.dg_mod.deleteNode(selection.getDependNode(0))
    sampling_node.translateX.keyframe.set_keys(
        samples, in_tangent_type="linear", out_tangent_type="linear"
    )
    mod.do_it_dg()
    for _ in range(2):
        _assert_samples(sampling_node.translateX.keyframe.get_keys(), samples)
        assert not maya_cmds.objExists(constraint)
        mod.undo_it()
        assert maya_cmds.objExists(constraint)
        _assert_samples(
            sampling_node.translateX.sample_values(frames=range(1, 12)),
            samples,
        )
        mod.redo_it()


def test_sample_values_does_not_flush_pending_values_or_change_history(
    sampling_node, maya_cmds
):
    mod = sampling_node.modifier_manager
    plug = sampling_node.number
    maya_cmds.setAttr(plug.plug.name(), 3.0)
    maya_cmds.flushUndo()
    plug.set(9.0)
    pending = mod.dg_mod
    samples = plug.sample_values(frames=[-1, 0.5, 20])
    assert samples == [(-1.0, 3.0), (0.5, 3.0), (20.0, 3.0)]
    assert mod.dg_mod is pending
    assert not mod.can_undo
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    mod.do_it_dg()
    assert plug.get() == 9.0
    assert samples[-1] == (20.0, 3.0)
    mod.undo_it()
    assert plug.get() == 3.0


@pytest.mark.parametrize(
    "frames,error",
    [
        (None, TypeError),
        (1.0, TypeError),
        ("12", TypeError),
        (b"12", TypeError),
        ([1.0, float("nan")], ValueError),
        ([1.0, float("inf")], ValueError),
        ([1.0, float("-inf")], ValueError),
        ([1.0, object()], TypeError),
    ],
)
def test_invalid_frames_are_rejected_before_evaluation(
    sampling_node, monkeypatch, frames, error
):
    def unexpected_read(*args):
        raise AssertionError("Input must be validated before reading values")

    _replace_reader(monkeypatch, sampling_node.number, unexpected_read)
    with pytest.raises(error):
        sampling_node.number.sample_values(frames=frames)
    assert om.MDGContext.current().isNormal()


def test_generator_failure_does_not_start_evaluation(
    sampling_node, monkeypatch
):
    def frames():
        yield 1.0
        raise RuntimeError("generation failed")

    def unexpected_read(*args):
        raise AssertionError("Input must be captured before reading values")

    _replace_reader(monkeypatch, sampling_node.number, unexpected_read)
    with pytest.raises(RuntimeError, match="generation failed"):
        sampling_node.number.sample_values(frames=frames())


def test_sample_values_captures_entry_time_unit_before_consuming_generator(
    sampling_node, maya_cmds
):
    _keys(maya_cmds, sampling_node.duration, 24.0)

    def frames():
        yield 1.0
        maya_cmds.currentUnit(time="ntsc")
        yield 6.0
        yield 11.0

    _assert_samples(
        sampling_node.duration.sample_values(frames=frames()),
        [(1, 0), (6, 12), (11, 24)],
    )


@pytest.mark.parametrize("failure", [False, True])
def test_sample_values_restores_outer_context_even_on_failure(
    sampling_node, maya_cmds, monkeypatch, failure
):
    _keys(maya_cmds, sampling_node.number)
    maya_cmds.currentTime(3.0)
    read = om.MPlug.asDouble
    if failure:

        def fail_at_second_frame(plug):
            current = om.MDGContext.current()
            if (
                not current.isNormal()
                and current.getTime().asUnits(om.MTime.uiUnit()) == 6.0
            ):
                raise RuntimeError("sample failed")
            return read(plug)

        _replace_reader(
            monkeypatch, sampling_node.number, fail_at_second_frame
        )
    outer = om.MDGContext(om.MTime(8.0, om.MTime.uiUnit()))
    previous = outer.makeCurrent()
    try:
        if failure:
            with pytest.raises(RuntimeError, match="sample failed"):
                sampling_node.number.sample_values(frames=[1, 6, 11])
        else:
            _assert_samples(
                sampling_node.number.sample_values(frames=[1, 6, 11]),
                [(1, 0), (6, 5), (11, 10)],
            )
        assert om.MDGContext.current().getTime() == outer.getTime()
        assert sampling_node.number.get() == pytest.approx(7.0)
    finally:
        previous.makeCurrent()
    assert om.MDGContext.current().isNormal()
    assert maya_cmds.currentTime(query=True) == 3.0
    assert sampling_node.number.get() == pytest.approx(2.0)


def test_empty_frames_do_not_evaluate_and_array_requires_index(
    sampling_node, monkeypatch
):
    def unexpected_read(*args):
        raise AssertionError("Empty input must not evaluate")

    with monkeypatch.context() as patch:
        _replace_reader(patch, sampling_node.number, unexpected_read)
        assert sampling_node.number.sample_values(frames=[]) == []
        with pytest.raises(TypeError, match="scalar"):
            sampling_node.multi_number.sample_values(frames=[])
    sampling_node.multi_number[3].set(5.0)
    sampling_node.modifier_manager.do_it_dg()
    assert sampling_node.multi_number[3].sample_values(frames=[1, 2]) == [
        (1.0, 5.0),
        (2.0, 5.0),
    ]
