# coding: utf-8
import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaFloat3PlugBinding, resolve_float3_plug
from bd_util.maya.ui.binding import float3_plug as store_module
from bd_util.ui import qt


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def node(new_scene):
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    cmds.currentUnit(linear="cm", angle="deg")
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield node
    cmds.currentUnit(linear=units[0], angle=units[1])
    flush()


@pytest.mark.parametrize("attribute", ["translate", "rotate", "scale"])
@pytest.mark.parametrize("linear, angle", [("cm", "deg"), ("m", "rad")])
def test_bulk_values_units_notifications_and_single_undo(
    node, attribute, linear, angle
):
    cmds.currentUnit(linear=linear, angle=angle)
    plug = getattr(node, attribute)
    before = tuple(plug.get())
    binding = MayaFloat3PlugBinding(plug)
    events = []
    binding.changed.connect(events.append)
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        requested = (100.123456789, -240.25, 360.5)
        assert binding.set_value(requested)
        assert binding.value == pytest.approx(requested, rel=1e-14)
        assert tuple(plug.get()) == pytest.approx(requested, rel=1e-14)
        assert len(events) == 1
        expected_scale = (
            0.01
            if attribute == "translate" and linear == "m"
            else (
                om.MAngle(1, om.MAngle.kDegrees).asRadians()
                if attribute == "rotate" and angle == "rad"
                else 1
            )
        )
        assert binding.view_model.x.presentation.scale == pytest.approx(
            expected_scale
        )
        cmds.undo()
        flush()
        assert binding.value == pytest.approx(before)
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        cmds.redo()
        flush()
        assert binding.value == pytest.approx(requested, rel=1e-14)
        cmds.flushUndo()
        assert not binding.set_value(binding.value)
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    finally:
        binding.dispose()


@pytest.mark.parametrize("on_changed", ["plain", "replace", "dispose"])
def test_direct_store_write_syncs_and_handles_notification_reentry(
    node, on_changed
):
    baseline = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaFloat3PlugBinding(node.translate)
    store = binding.store
    events = []

    def changed(value):
        events.append(value)
        if value == (1, 2, 3):
            if on_changed == "replace":
                store.write((4, 5, 6))
            elif on_changed == "dispose":
                binding.dispose()

    binding.changed.connect(changed)
    try:
        actual = store.write((1, 2, 3))
        expected = (4, 5, 6) if on_changed == "replace" else (1, 2, 3)
        assert actual == expected
        assert tuple(node.translate.get()) == expected
        if on_changed == "dispose":
            assert binding.is_disposed
            assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == baseline
        else:
            assert binding.value == expected
            assert binding.view_model.z.value.value == expected[2]
            assert events[-1] == expected
    finally:
        binding.dispose()


def test_axis_edit_keeps_other_values_and_partial_lock_allows_other_axes(node):
    cmds.setAttr(
        node.cmd_access_name + ".translate",
        1,
        2.1234567890123,
        3.1234567890123,
        type="double3",
    )
    binding = MayaFloat3PlugBinding(node.translate)
    try:
        before = binding.value
        cmds.setAttr(node.cmd_access_name + ".ty", lock=True)
        assert binding.view_model.x.set_value_command.can_execute
        assert not binding.view_model.y.set_value_command.can_execute
        assert binding.view_model.z.set_value_command.can_execute
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value((7, 8, 9))
        assert binding.view_model.x.set_value_command.execute(10)
        assert binding.value == (10, before[1], before[2])
        cmds.setAttr(node.cmd_access_name + ".ty", lock=False)
        assert binding.view_model.set_value_command.can_execute
        cmds.setAttr(node.cmd_access_name + ".translate", lock=True)
        assert all(
            not axis.set_value_command.can_execute
            for axis in (
                binding.view_model.x,
                binding.view_model.y,
                binding.view_model.z,
            )
        )
    finally:
        binding.dispose()


@pytest.mark.parametrize("parent_connection", [False, True])
def test_parent_or_child_connection_and_upstream_evaluation(
    node, parent_connection
):
    source = cmds.createNode("transform")
    cmds.setAttr(source + ".translate", 1, 2, 3, type="double3")
    target = ".translate" if parent_connection else ".ty"
    binding = MayaFloat3PlugBinding(node.translate)
    try:
        cmds.connectAttr(source + target, node.cmd_access_name + target)
        flush()
        assert not binding.view_model.set_value_command.can_execute
        assert binding.view_model.x.set_value_command.can_execute == (
            not parent_connection
        )
        assert not binding.view_model.y.set_value_command.can_execute
        cmds.setAttr(source + ".ty", 123.456789)
        flush()
        assert binding.value[1] == 123.456789
        cmds.disconnectAttr(source + target, node.cmd_access_name + target)
        flush()
        assert binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()


def test_bulk_validation_prevents_partial_writes_and_preserves_undo(node):
    name = node.cmd_access_name
    cmds.addAttr(name, ln="triple", at="double3")
    for axis in "XYZ":
        cmds.addAttr(
            name,
            ln="triple" + axis,
            at="double",
            p="triple",
            minValue=0,
            maxValue=10,
        )
    binding = MayaFloat3PlugBinding(resolve_float3_plug(name, "triple"))
    try:
        binding.set_value((1, 2, 3))
        cmds.flushUndo()
        for value in (
            (4, -1, 6),
            (4, 11, 6),
            (4, float("nan"), 6),
            (4, float("inf"), 6),
        ):
            with pytest.raises(ValueError):
                binding.set_value(value)
            assert binding.value == (1, 2, 3)
            assert cmds.getAttr(name + ".triple")[0] == (1, 2, 3)
            assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    finally:
        binding.dispose()


def test_float3_quantization_overflow_and_no_op(node):
    name = node.cmd_access_name
    cmds.addAttr(name, ln="triple", at="float3")
    for axis in "XYZ":
        cmds.addAttr(name, ln="triple" + axis, at="float", p="triple")
    binding = MayaFloat3PlugBinding(resolve_float3_plug(name, "triple"))
    try:
        binding.set_value((0.1, 0.2, 0.3))
        assert binding.value == cmds.getAttr(name + ".triple")[0]
        cmds.flushUndo()
        assert not binding.set_value((0.1, 0.2, 0.3))
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        before = binding.value
        for value in ((1, 1e100, 2), (1, 1e-100, 2)):
            with pytest.raises(ValueError):
                binding.set_value(value)
            assert binding.value == before
            assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    finally:
        binding.dispose()


def test_node_removal_stops_every_callback_without_resurrection(node):
    baseline = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaFloat3PlugBinding(node.translate)
    stores = binding.store.components
    assert len(om.MMessage.nodeCallbacks(node.m_obj)) > len(baseline)
    cmds.delete(node.cmd_access_name)
    flush()
    assert binding.store.is_disposed
    assert all(store.is_disposed for store in stores)
    assert not binding.view_model.set_value_command.can_execute
    cmds.undo()
    flush()
    assert not binding.store.is_available
    binding.dispose()


def test_attribute_removal_and_owner_destruction_release_callbacks(node):
    name = node.cmd_access_name
    cmds.addAttr(name, ln="triple", at="double3")
    for axis in "XYZ":
        cmds.addAttr(name, ln="triple" + axis, at="double", p="triple")
    baseline = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QObject()
    binding = MayaFloat3PlugBinding(
        resolve_float3_plug(name, "triple"), parent=owner
    )
    cmds.deleteAttr(name + ".triple")
    flush()
    assert binding.store.is_disposed
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == baseline
    other = MayaFloat3PlugBinding(node.translate, parent=owner)
    stores = other.store.components
    owner.deleteLater()
    flush()
    assert all(store.is_disposed for store in stores)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == baseline


def test_reentrant_value_change_and_disposal(node):
    baseline = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaFloat3PlugBinding(node.translate)

    def replace(values):
        if values == (1, 2, 3):
            binding.set_value((4, 5, 6))

    binding.changed.connect(replace)
    binding.set_value((1, 2, 3))
    assert binding.value == (4, 5, 6)
    assert tuple(
        axis.value.value
        for axis in (
            binding.view_model.x,
            binding.view_model.y,
            binding.view_model.z,
        )
    ) == (4, 5, 6)
    binding.changed.connect(lambda _value: binding.dispose())
    binding.set_value((7, 8, 9))
    assert binding.is_disposed
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == baseline


def test_command_failure_keeps_actual_values_and_callback_cleanup(
    node, monkeypatch
):
    binding = MayaFloat3PlugBinding(node.translate)
    try:
        binding.set_value((1, 2, 3))

        def fail(*args, **kwargs):
            raise RuntimeError("write failed")

        monkeypatch.setattr(store_module.cmds, "setAttr", fail)
        with pytest.raises(RuntimeError, match="write failed"):
            binding.set_value((4, 5, 6))
        assert binding.value == (1, 2, 3)
        assert binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()


def test_constructor_failure_releases_partially_created_stores(
    node, monkeypatch
):
    baseline = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    original = store_module.resolve_float_plug

    def resolve(name, attribute):
        if attribute == "translateY":
            raise RuntimeError("failed on second axis")
        return original(name, attribute)

    monkeypatch.setattr(store_module, "resolve_float_plug", resolve)
    with pytest.raises(RuntimeError, match="second axis"):
        MayaFloat3PlugBinding(node.translate)
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == baseline


@pytest.mark.parametrize(
    "attribute",
    [
        "tx",
        "visibility",
        "rotateQuaternion",
        "matrix",
        "translate.translateX",
        "translate[0]",
    ],
)
def test_invalid_targets_are_rejected(node, attribute):
    with pytest.raises((TypeError, ValueError)):
        resolve_float3_plug(node.cmd_access_name, attribute)


def test_short_names_rename_and_duplicate_dag_names(node):
    other_parent = cmds.createNode("transform")
    child_a = cmds.createNode(
        "transform", name="same", parent=node.cmd_access_name
    )
    child_b = cmds.createNode("transform", name="same", parent=other_parent)
    child_a = cmds.listRelatives(
        node.cmd_access_name, children=True, fullPath=True
    )[0]
    child_b = cmds.listRelatives(other_parent, children=True, fullPath=True)[0]
    binding = MayaFloat3PlugBinding(resolve_float3_plug(child_a, "t"))
    try:
        cmds.rename(child_a, "renamed")
        binding.set_value((1, 2, 3))
        assert binding.value == (1, 2, 3)
        assert cmds.getAttr(child_b + ".translate")[0] == (0, 0, 0)
    finally:
        binding.dispose()


@pytest.mark.parametrize("kind", ["array", "compound", "mixed"])
def test_unsupported_compound_schemas_are_rejected(node, kind):
    name = node.cmd_access_name
    if kind == "compound":
        cmds.addAttr(name, ln="triple", at="compound", numberOfChildren=3)
    else:
        cmds.addAttr(name, ln="triple", at="double3", multi=(kind == "array"))
    for axis in "XYZ":
        child_type = (
            "doubleAngle" if kind == "mixed" and axis == "Y" else "double"
        )
        cmds.addAttr(name, ln="triple" + axis, at=child_type, p="triple")
    with pytest.raises(TypeError):
        resolve_float3_plug(name, "triple")


def test_unit_changes_do_not_emit_value_changes(node):
    binding = MayaFloat3PlugBinding(node.rotate)
    events = []
    try:
        binding.set_value((450, -90, 12.3456789))
        before = binding.value
        binding.changed.connect(events.append)
        cmds.currentUnit(angle="rad")
        assert binding.value == before
        assert events == []
        assert all(
            axis.presentation.suffix == " rad"
            for axis in (
                binding.view_model.x,
                binding.view_model.y,
                binding.view_model.z,
            )
        )
    finally:
        binding.dispose()
