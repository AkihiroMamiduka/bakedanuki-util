# coding: utf-8
import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import (
    MayaFloatPlugBinding,
    MayaFloatPlugStore,
    resolve_float_plug,
)
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import FloatViewModel, qt


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def transform(new_scene):
    linear, angle = cmds.currentUnit(
        query=True, linear=True
    ), cmds.currentUnit(query=True, angle=True)
    cmds.currentUnit(linear="cm", angle="deg")
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield node
    cmds.currentUnit(linear=linear, angle=angle)
    flush()


@pytest.mark.parametrize(
    "attribute, value",
    [
        ("translateX", 123.456789123),
        ("rotateX", 450.123456789),
        ("scaleX", -2.123456789),
    ],
)
def test_scalar_initial_read_external_edits_and_undo(
    transform, attribute, value
):
    name = f"{transform.cmd_access_name}.{attribute}"
    cmds.setAttr(name, value)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    binding = MayaFloatPlugBinding(
        resolve_float_plug(transform.cmd_access_name, attribute)
    )
    try:
        assert binding.value == pytest.approx(value, rel=1e-14)
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        binding.set_value(-12.3456789123)
        assert cmds.getAttr(name) == pytest.approx(-12.3456789123, rel=1e-14)
        cmds.undo()
        flush()
        assert binding.value == pytest.approx(value, rel=1e-14)
        cmds.redo()
        flush()
        assert binding.value == pytest.approx(-12.3456789123, rel=1e-14)
        cmds.setAttr(name, 0.125)
        assert binding.value == pytest.approx(0.125)
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "attribute, value, scale, suffix",
    [
        ("tx", 100.0, 0.01, " m"),
        ("rx", 90.0, 0.017453292519943295, " rad"),
        ("sx", -2.0, 1.0, ""),
    ],
)
def test_ui_units_do_not_change_public_values(
    transform, attribute, value, scale, suffix
):
    plug = resolve_float_plug(transform.cmd_access_name, attribute)
    binding = MayaFloatPlugBinding(plug)
    try:
        binding.set_value(value)
        changes = []
        binding.changed.connect(changes.append)
        cmds.currentUnit(linear="m", angle="rad")
        assert binding.value == pytest.approx(value)
        assert changes == []
        presentation = binding.view_model.presentation
        assert presentation.scale == pytest.approx(scale)
        assert presentation.suffix == suffix
        binding.set_value(value * 2)
        assert cmds.getAttr(
            f"{transform.cmd_access_name}.{attribute}"
        ) == pytest.approx(value * 2 * scale)
        assert plug.get() == pytest.approx(value * 2)
    finally:
        binding.dispose()
        flush()


def test_compound_changes_lock_connections_and_dirty_refresh(transform):
    binding = MayaFloatPlugBinding(transform.translate.translateX)
    name = transform.cmd_access_name
    source = cmds.createNode("transform")
    try:
        cmds.setAttr(name + ".translate", 1, 2, 3, type="double3")
        flush()
        assert binding.value == 1.0
        cmds.setAttr(name + ".translate", lock=True)
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value(99.0)
        cmds.setAttr(name + ".translate", lock=False)
        assert binding.view_model.set_value_command.can_execute
        cmds.connectAttr(source + ".translate", name + ".translate")
        flush()
        assert not binding.store.plug_operator.plug.isDestination
        assert not binding.view_model.set_value_command.can_execute
        for value in [10.0, 20.0, -30.0]:
            cmds.setAttr(source + ".tx", value)
            flush()
            assert binding.value == value
        cmds.disconnectAttr(source + ".translate", name + ".translate")
        flush()
        assert binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_float_storage_adopts_actual_precision(transform):
    name = transform.cmd_access_name
    cmds.addAttr(name, longName="floatValue", attributeType="float")
    binding = MayaFloatPlugBinding(resolve_float_plug(name, "floatValue"))
    try:
        assert binding.set_value(0.1)
        assert binding.value == 0.10000000149011612
        cmds.flushUndo()
        assert not binding.set_value(0.1)
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "attribute_type", ["double", "doubleLinear", "doubleAngle"]
)
def test_hard_limits_use_public_units_and_ignore_soft_limits(
    transform, attribute_type
):
    name = transform.cmd_access_name
    cmds.addAttr(
        name,
        longName="limited",
        attributeType=attribute_type,
        minValue=-2,
        maxValue=4,
        softMinValue=-1,
        softMaxValue=1,
    )
    binding = MayaFloatPlugBinding(resolve_float_plug(name, "limited"))
    try:
        factor = (
            om.MAngle(1, om.MAngle.kRadians).asDegrees()
            if attribute_type == "doubleAngle"
            else 1
        )
        assert binding.view_model.presentation.minimum == pytest.approx(
            -2 * factor
        )
        assert binding.view_model.presentation.maximum == pytest.approx(
            4 * factor
        )
        cmds.currentUnit(linear="m", angle="rad")
        assert binding.view_model.presentation.maximum == pytest.approx(
            4 * factor
        )
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "attribute",
    [
        "translate",
        "visibility",
        "rotateOrder",
        "matrix",
        "missing",
        "translate.translateX",
    ],
)
def test_resolver_rejects_non_scalar_or_non_float_attributes(
    transform, attribute
):
    with pytest.raises((TypeError, ValueError, AttributeError)):
        resolve_float_plug(transform.cmd_access_name, attribute)


def test_array_element_and_child_of_array_are_rejected(transform):
    name = transform.cmd_access_name
    cmds.addAttr(name, longName="values", attributeType="double", multi=True)
    cmds.setAttr(name + ".values[0]", 2)
    with pytest.raises(TypeError):
        resolve_float_plug(name, "values")
    with pytest.raises(ValueError):
        resolve_float_plug(name, "values[0]")


@pytest.mark.parametrize("target", ["node", "attribute"])
def test_removal_stops_callbacks_and_never_retargets_recreated_attribute(
    transform, target
):
    name = transform.cmd_access_name
    cmds.addAttr(name, longName="scalar", attributeType="double")
    binding = MayaFloatPlugBinding(resolve_float_plug(name, "scalar"))
    try:
        if target == "node":
            cmds.delete(name)
        else:
            cmds.deleteAttr(name + ".scalar")
        flush()
        assert not binding.store.is_available
        assert binding.store.is_disposed
        assert not binding.view_model.set_value_command.can_execute
        if target == "attribute":
            cmds.addAttr(
                name, longName="scalar", attributeType="double", defaultValue=8
            )
            assert not binding.set_value(2)
            assert cmds.getAttr(name + ".scalar") == 8
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("failure", ["callbacks", "read", "argument"])
def test_construction_failure_releases_node_and_unit_callbacks(
    transform, monkeypatch, failure
):
    before = tuple(om.MMessage.nodeCallbacks(transform.m_obj))
    owner = qt.QObject()
    original = MayaFloatPlugStore._register_callbacks
    registries = []

    def fail_register(self):
        original(self)
        registries.extend(
            child
            for child in self.parent().children()
            if isinstance(child, MayaCallbackRegistry)
        )
        raise ValueError("failed")

    def fail_read(self):
        raise ValueError("failed")

    if failure == "callbacks":
        monkeypatch.setattr(
            MayaFloatPlugStore, "_register_callbacks", fail_register
        )
    elif failure == "read":
        monkeypatch.setattr(MayaFloatPlugStore, "read", fail_read)
    try:
        with pytest.raises((ValueError, TypeError)):
            MayaFloatPlugBinding(
                (
                    object()
                    if failure == "argument"
                    else transform.rotate.rotateX
                ),
                parent=owner,
            )
        assert tuple(om.MMessage.nodeCallbacks(transform.m_obj)) == before
        assert all(not registry.callback_ids for registry in registries)
        flush()
        assert not owner.children()
    finally:
        owner.deleteLater()
        flush()


@pytest.mark.parametrize("during_change", [False, True])
def test_dispose_and_owner_destruction_release_callbacks(
    transform, during_change
):
    before = tuple(om.MMessage.nodeCallbacks(transform.m_obj))
    owner = qt.QObject()
    binding = MayaFloatPlugBinding(transform.rotate.rotateX, parent=owner)
    vm = binding.view_model
    if during_change:
        binding.changed.connect(binding.dispose)
        binding.set_value(30.0)
        assert not vm.set_value_command.can_execute
    else:
        owner.deleteLater()
        flush()
    assert binding.is_disposed
    assert tuple(om.MMessage.nodeCallbacks(transform.m_obj)) == before
    if qt.isValid(owner):
        owner.deleteLater()
    flush()


def test_direct_store_write_reentrant_command_keeps_latest_actual_value(
    transform,
):
    binding = MayaFloatPlugBinding(transform.scale.scaleX)

    def replace(value):
        if value == 2:
            binding.set_value(3)

    binding.changed.connect(replace)
    try:
        assert binding.store.write(2) == 3
        assert binding.value == transform.scale.scaleX.get() == 3
    finally:
        binding.dispose()
        flush()


@pytest.mark.parametrize("value", [1e40, -1e40, 1e-50])
def test_float_unrepresentable_input_does_not_modify_scene(transform, value):
    name = transform.cmd_access_name
    cmds.addAttr(
        name, longName="floatValue", attributeType="float", defaultValue=1
    )
    binding = MayaFloatPlugBinding(resolve_float_plug(name, "floatValue"))
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        with pytest.raises(ValueError):
            binding.set_value(value)
        assert binding.value == cmds.getAttr(name + ".floatValue") == 1.0
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
        flush()


def test_animation_dirty_updates_value_while_input_remains_disabled(transform):
    name = transform.cmd_access_name
    cmds.setKeyframe(name, attribute="translateX", time=1, value=0)
    cmds.setKeyframe(name, attribute="translateX", time=10, value=100)
    binding = MayaFloatPlugBinding(transform.translate.translateX)
    try:
        for frame in [1, 5, 10, 2]:
            cmds.currentTime(frame)
            flush()
            assert binding.value == pytest.approx(cmds.getAttr(name + ".tx"))
            assert not binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_rename_and_duplicate_dag_names_keep_correct_target(transform):
    name = transform.cmd_access_name
    binding = MayaFloatPlugBinding(transform.translate.translateX)
    try:
        renamed = cmds.rename(name, "renamedFloatTarget")
        parent = cmds.createNode("transform")
        duplicate = cmds.createNode(
            "transform", name="renamedFloatTarget", parent=parent
        )
        binding.set_value(75)
        assert cmds.getAttr("|" + renamed + ".tx") == 75
        assert cmds.getAttr(duplicate + ".tx") == 0
    finally:
        binding.dispose()
        flush()


def test_unit_notification_reentrant_input_uses_latest_value(transform):
    binding = MayaFloatPlugBinding(transform.translate.translateX)
    binding.view_model.presentation_changed.connect(
        lambda _: binding.set_value(250)
    )
    try:
        cmds.currentUnit(linear="m")
        assert binding.value == transform.translate.translateX.get() == 250
    finally:
        binding.dispose()
        flush()


def test_store_requires_its_original_view_model(transform):
    owner = qt.QObject()
    first, second = FloatViewModel(parent=owner), FloatViewModel(parent=owner)
    store = MayaFloatPlugStore(first, transform.scale.scaleX, owner)
    try:
        with pytest.raises(ValueError, match="構築時に指定"):
            second.attach_store(store)
        first.attach_store(store)
        assert first.value.value == 1.0
    finally:
        store.dispose()
        owner.deleteLater()
        flush()
