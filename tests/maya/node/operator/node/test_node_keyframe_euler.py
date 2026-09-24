from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing.transform(name)


def _rotation_keys(cmds, node, samples, *, layer=None):
    for frame, values in samples:
        for axis, value in zip("XYZ", values):
            arguments = {
                "time": frame,
                "value": value,
                "inTangentType": "linear",
                "outTangentType": "linear",
            }
            if layer is not None:
                arguments.update(animLayer=layer, noResolve=True)
            cmds.setKeyframe(node + ".rotate" + axis, **arguments)


def _values(cmds, node, axis, *, layer=None):
    plug = node + ".rotate" + axis
    if layer is not None:
        plug = cmds.animLayer(layer, query=True, findCurveForPlug=plug)[0]
    return tuple(cmds.keyframe(plug, query=True, valueChange=True) or [])


def _curve(cmds, node, axis):
    name = cmds.listConnections(
        node + ".rotate" + axis,
        source=True,
        destination=False,
        type="animCurve",
    )[0]
    return oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))


def _quaternion(values, order):
    return om.MEulerRotation(
        *(math.radians(value) for value in values), order
    ).asQuaternion()


def _same_rotation(first, second):
    dot = (
        first.x * second.x
        + first.y * second.y
        + first.z * second.z
        + first.w * second.w
    )
    return abs(dot) == pytest.approx(1.0, abs=1e-10)


@pytest.mark.parametrize("order", range(6))
def test_node_euler_filter_uses_rotate_order_and_preserves_pose(
    maya_cmds, order
):
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.setAttr(target + ".rotateOrder", order)
    samples = (
        (1, (10.0, 20.0, 30.0)),
        (2, (380.0, 385.0, 390.0)),
        (3, (-330.0, -325.0, -320.0)),
    )
    _rotation_keys(maya_cmds, target, samples)
    before_rotations = tuple(
        _quaternion(values, order) for _, values in samples
    )
    manager = bdu.ModifierManager()

    assert _node(target, manager).keyframes.euler_filter() is None
    manager.do_it_dg()

    result = tuple(
        zip(
            _values(maya_cmds, target, "X"),
            _values(maya_cmds, target, "Y"),
            _values(maya_cmds, target, "Z"),
        )
    )
    expected = (
        (10.0, 20.0, 30.0),
        (20.0, 25.0, 30.0),
        (30.0, 35.0, 40.0),
    )
    for values, expected_values in zip(result, expected):
        assert values == pytest.approx(expected_values)
    for before, values in zip(before_rotations, result):
        assert _same_rotation(before, _quaternion(values, order))

    for _ in range(2):
        manager.undo_it()
        assert _values(maya_cmds, target, "X") == pytest.approx(
            tuple(values[0] for _, values in samples)
        )
        manager.redo_it()
        assert _values(maya_cmds, target, "X") == pytest.approx(
            (10.0, 20.0, 30.0)
        )


def test_node_euler_filter_uses_inclusive_range_without_boundary_keys(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    samples = (
        (1, (10.0, 20.0, 30.0)),
        (2, (370.0, 380.0, 390.0)),
        (3, (20.0, 30.0, 40.0)),
        (4, (30.0, 40.0, 50.0)),
    )
    _rotation_keys(maya_cmds, target, samples)
    maya_cmds.setKeyframe(
        target + ".rotateY",
        time=0,
        value=5,
        inTangentType="linear",
        outTangentType="linear",
    )
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter(2, 3)
    manager.do_it_dg()

    assert tuple(
        maya_cmds.keyframe(target + ".rotateX", query=True, timeChange=True)
    ) == (1.0, 2.0, 3.0, 4.0)
    assert _values(maya_cmds, target, "X") == pytest.approx(
        (10.0, 370.0, 380.0, 30.0)
    )
    assert _values(maya_cmds, target, "Y") == pytest.approx(
        (5.0, 20.0, 380.0, 390.0, 40.0)
    )

    manager.undo_it()
    maya_cmds.cutKey(target + ".rotateY", time=(0, 0))
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter(None, 3)
    manager.do_it_dg()
    assert _values(maya_cmds, target, "X") == pytest.approx(
        (10.0, 10.0, 20.0, 30.0)
    )

    manager.undo_it()
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter(2, None)
    manager.do_it_dg()
    assert _values(maya_cmds, target, "X") == pytest.approx(
        (10.0, 370.0, 380.0, 390.0)
    )


def test_node_euler_filter_preserves_key_metadata(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    samples = ((1, (0.0, 10.0, 20.0)), (2, (370.0, 380.0, 390.0)))
    _rotation_keys(maya_cmds, target, samples)
    snapshots = []
    for axis in "XYZ":
        curve = _curve(maya_cmds, target, axis)
        curve.setIsWeighted(True)
        curve.setIsBreakdown(1, True)
        curve.setTangentsLocked(1, False)
        curve.setWeightsLocked(1, True)
        curve.setInTangentType(1, oma.MFnAnimCurve.kTangentFixed)
        curve.setOutTangentType(1, oma.MFnAnimCurve.kTangentFixed)
        curve.setTangent(1, 0.03, 0.2, True, convertUnits=False)
        curve.setTangent(1, 0.09, -0.1, False, convertUnits=False)
        curve.setPreInfinityType(oma.MFnAnimCurve.kCycle)
        curve.setPostInfinityType(oma.MFnAnimCurve.kOscillate)
        snapshots.append(
            (
                tuple(
                    curve.input(index).value for index in range(curve.numKeys)
                ),
                tuple(
                    curve.inTangentType(index)
                    for index in range(curve.numKeys)
                ),
                tuple(
                    curve.outTangentType(index)
                    for index in range(curve.numKeys)
                ),
                tuple(
                    curve.isBreakdown(index) for index in range(curve.numKeys)
                ),
                tuple(
                    curve.tangentsLocked(index)
                    for index in range(curve.numKeys)
                ),
                tuple(
                    curve.weightsLocked(index)
                    for index in range(curve.numKeys)
                ),
                curve.isWeighted,
                curve.preInfinityType,
                curve.postInfinityType,
                tuple(
                    component
                    for incoming in (True, False)
                    for component in curve.getTangentXY(1, incoming)
                ),
            )
        )
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter()
    manager.do_it_dg()

    for curve, expected in zip(
        (_curve(maya_cmds, target, axis) for axis in "XYZ"), snapshots
    ):
        actual = (
            tuple(curve.input(index).value for index in range(curve.numKeys)),
            tuple(
                curve.inTangentType(index) for index in range(curve.numKeys)
            ),
            tuple(
                curve.outTangentType(index) for index in range(curve.numKeys)
            ),
            tuple(curve.isBreakdown(index) for index in range(curve.numKeys)),
            tuple(
                curve.tangentsLocked(index) for index in range(curve.numKeys)
            ),
            tuple(
                curve.weightsLocked(index) for index in range(curve.numKeys)
            ),
            curve.isWeighted,
            curve.preInfinityType,
            curve.postInfinityType,
            tuple(
                component
                for incoming in (True, False)
                for component in curve.getTangentXY(1, incoming)
            ),
        )
        assert actual[:-1] == expected[:-1]
        assert actual[-1] == pytest.approx(expected[-1])


def test_node_euler_filter_requires_complete_synchronized_curves(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter()
    manager.do_it_dg()

    for frame, value in ((1, 0), (2, 360)):
        maya_cmds.setKeyframe(target + ".rotateX", time=frame, value=value)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter(10, 20)
    manager.do_it_dg()
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter()
    with pytest.raises(RuntimeError, match="rotateX, rotateY and rotateZ"):
        manager.do_it_dg()

    _rotation_keys(
        maya_cmds,
        target,
        ((1, (0, 0, 0)), (2, (360, 360, 360))),
    )
    maya_cmds.setKeyframe(target + ".rotateZ", time=1.5, value=10)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter()
    with pytest.raises(RuntimeError, match="synchronized"):
        manager.do_it_dg()

    independent = maya_cmds.createNode("transform", name="independent")
    _rotation_keys(
        maya_cmds,
        independent,
        ((1, (0, 0, 0)), (2, (360, 360, 360))),
    )
    _curve(maya_cmds, independent, "X").findPlug(
        "rotationInterpolation", False
    ).setInt(3)
    manager = bdu.ModifierManager()
    _node(independent, manager).keyframes.euler_filter()
    with pytest.raises(RuntimeError, match="independent scalar"):
        manager.do_it_dg()


def test_nodes_euler_filter_prevalidates_all_nodes_and_rotate_order(
    maya_cmds,
):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    samples = ((1, (0, 0, 0)), (2, (370, 380, 390)))
    _rotation_keys(maya_cmds, first, samples)
    _rotation_keys(maya_cmds, second, samples)
    second_curve = maya_cmds.listConnections(
        second + ".rotateX", source=True, destination=False
    )[0]
    maya_cmds.lockNode(second_curve, lock=True)
    first_before = _values(maya_cmds, first, "X")
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.euler_filter([first, second])
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert _values(maya_cmds, first, "X") == first_before
    assert not manager.can_undo

    maya_cmds.lockNode(second_curve, lock=False)
    maya_cmds.setKeyframe(second + ".rotateOrder", time=1, value=0)
    manager = bdu.ModifierManager()
    _node(second, manager).keyframes.euler_filter()
    with pytest.raises(RuntimeError, match="static rotateOrder"):
        manager.do_it_dg()


def test_node_euler_filter_supports_explicit_layer(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    base_samples = ((1, (1, 2, 3)), (2, (361, 362, 363)))
    _rotation_keys(maya_cmds, target, base_samples)
    base_curves = tuple(
        maya_cmds.listConnections(
            target + ".rotate" + axis,
            source=True,
            destination=False,
            type="animCurve",
        )[0]
        for axis in "XYZ"
    )
    base_before = tuple(
        tuple(maya_cmds.keyframe(curve, query=True, valueChange=True))
        for curve in base_curves
    )
    layer = maya_cmds.animLayer("Correction")
    maya_cmds.animLayer(layer, edit=True, attribute=target + ".rotate")
    layer_samples = ((1, (10, 20, 30)), (2, (380, 390, 400)))
    _rotation_keys(maya_cmds, target, layer_samples, layer=layer)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).euler_filter()
    manager.do_it_dg()

    assert (
        tuple(
            tuple(maya_cmds.keyframe(curve, query=True, valueChange=True))
            for curve in base_curves
        )
        == base_before
    )
    assert _values(maya_cmds, target, "X", layer=layer) == pytest.approx(
        (10.0, 20.0)
    )
    assert _values(maya_cmds, target, "Y", layer=layer) == pytest.approx(
        (20.0, 30.0)
    )
    assert _values(maya_cmds, target, "Z", layer=layer) == pytest.approx(
        (30.0, 40.0)
    )

    maya_cmds.animLayer(layer, edit=True, preferred=True)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.euler_filter()
    manager.do_it_dg()
    base_result = tuple(
        tuple(maya_cmds.keyframe(curve, query=True, valueChange=True))
        for curve in base_curves
    )
    for values, expected in zip(
        base_result, ((1.0, 1.0), (2.0, 2.0), (3.0, 3.0))
    ):
        assert values == pytest.approx(expected)
    assert _values(maya_cmds, target, "X", layer=layer) == pytest.approx(
        (10.0, 20.0)
    )


def test_node_euler_filter_follows_queued_curve_creation_and_rolls_back(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    for plug, values in zip(
        (node.rx, node.ry, node.rz),
        ((0, 370), (10, 380), (20, 390)),
    ):
        plug.keyframe.set_keys([(1, values[0]), (2, values[1])])
    node.keyframes.euler_filter()
    manager.do_it_dg()
    assert _values(maya_cmds, target, "X") == pytest.approx((0.0, 10.0))

    manager = bdu.ModifierManager()
    for axis, value in zip("XYZ", (370, 380, 390)):
        maya_cmds.setKeyframe(target + ".rotate" + axis, time=2, value=value)
    _node(target, manager).keyframes.euler_filter()

    def fail(_change):
        raise RuntimeError("later failure")

    manager.queue_anim_curve_change(fail)
    before = _values(maya_cmds, target, "X")
    with pytest.raises(RuntimeError, match="later failure"):
        manager.do_it_dg()
    assert _values(maya_cmds, target, "X") == before
    assert not manager.can_undo


def test_euler_filter_rejects_invalid_ranges_nodes_and_node_types(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    network = maya_cmds.createNode("network", name="network")
    joint = maya_cmds.createNode("joint", name="joint")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    with pytest.raises(ValueError, match="start_frame"):
        node.keyframes.euler_filter(2, 1)

    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(ValueError, match="at least one"):
        nodes.keyframes.euler_filter([])
    with pytest.raises(TypeError, match="iterable"):
        nodes.keyframes.euler_filter(target)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.euler_filter([target, node])
    nodes.keyframes.euler_filter([joint])
    manager.do_it_dg()

    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.euler_filter([network])
    with pytest.raises(TypeError, match="transform or joint"):
        manager.do_it_dg()
