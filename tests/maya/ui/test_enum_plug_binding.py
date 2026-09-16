# coding: utf-8
import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaEnumPlugBinding, resolve_enum_plug
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import EnumDefinition, qt


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def enum_node(new_scene):
    node = cmds.createNode("transform")
    cmds.addAttr(
        node,
        longName="mode",
        shortName="md",
        attributeType="enum",
        enumName="Negative=-2:Off=0:Preview=5:Final=10",
        keyable=True,
    )
    cmds.setAttr(node + ".mode", 5)
    yield node
    flush()


def test_initial_value_external_changes_undo_redo_and_sparse_validation(
    enum_node,
):
    binding = MayaEnumPlugBinding(resolve_enum_plug(enum_node, "md"))
    values = []
    binding.changed.connect(values.append)
    try:
        assert binding.value == 5
        assert binding.definition == EnumDefinition.from_mapping(
            {-2: "Negative", 0: "Off", 5: "Preview", 10: "Final"}
        )
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        binding.set_value(-2)
        assert cmds.getAttr(enum_node + ".mode") == -2
        cmds.undo()
        flush()
        assert binding.value == 5
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert binding.value == -2
        cmds.setAttr(enum_node + ".mode", 1)
        flush()
        assert binding.value == 1
        assert not binding.is_value_defined
        with pytest.raises(ValueError):
            binding.set_value(1)
        with pytest.raises(ValueError):
            binding.store.write(3)
        assert cmds.getAttr(enum_node + ".mode") == 1
        assert values == [-2, 5, -2, 1]
        binding.store.write(10)
        assert binding.value == 10
    finally:
        binding.dispose()
        flush()


def test_runtime_definition_rename_remove_current_and_undo(enum_node):
    binding = MayaEnumPlugBinding(resolve_enum_plug(enum_node, "mode"))
    values = []
    definitions = []
    binding.changed.connect(values.append)
    binding.definition_changed.connect(definitions.append)
    try:
        cmds.addAttr(
            enum_node + ".mode", edit=True, enumName="Off=0:Renamed=5:Final=10"
        )
        flush()
        assert binding.definition.item_for_value(5).name == "Renamed"
        assert values == []
        cmds.addAttr(enum_node + ".mode", edit=True, enumName="Off=0:Final=10")
        flush()
        assert binding.value == 5
        assert not binding.is_value_defined
        assert len(definitions) == 2
        cmds.undo()
        flush()
        assert binding.is_value_defined
        assert binding.definition.item_for_value(5).name == "Renamed"
        cmds.redo()
        flush()
        assert not binding.is_value_defined
    finally:
        binding.dispose()
        flush()


def test_builtin_enum_and_runtime_names_override_generated_metadata(new_scene):
    node = Nodes().existing.transform(cmds.createNode("transform"))
    binding = MayaEnumPlugBinding(node.rotateOrder)
    try:
        assert [item.name for item in binding.definition.items] == [
            "xyz",
            "yzx",
            "zxy",
            "xzy",
            "yxz",
            "zyx",
        ]
        assert binding.set_value(node.rotateOrder.ZYX)
        assert node.rotateOrder.get() == 5
    finally:
        binding.dispose()
        flush()


def test_lock_connection_rename_and_deletion(enum_node):
    binding = MayaEnumPlugBinding(resolve_enum_plug(enum_node, "mode"))
    try:
        cmds.setAttr(enum_node + ".mode", lock=True)
        assert not binding.view_model.set_value_command.can_execute
        cmds.setAttr(enum_node + ".mode", lock=False)
        assert binding.view_model.set_value_command.can_execute
        source = cmds.createNode("network")
        cmds.addAttr(
            source,
            longName="mode",
            attributeType="enum",
            enumName="Off=0:Preview=5:Final=10",
        )
        cmds.connectAttr(source + ".mode", enum_node + ".mode")
        assert not binding.view_model.set_value_command.can_execute
        cmds.setAttr(source + ".mode", 10)
        flush()
        assert binding.value == 10
        cmds.disconnectAttr(source + ".mode", enum_node + ".mode")
        assert binding.view_model.set_value_command.can_execute
        renamed = cmds.rename(enum_node, "renamedEnumTarget")
        binding.set_value(-2)
        assert cmds.getAttr(renamed + ".mode") == -2
        cmds.deleteAttr(renamed + ".mode")
        flush()
        assert binding.store.is_disposed
        assert not binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_compound_child_parent_lock_and_duplicate_dag_paths(new_scene):
    parent_a = cmds.createNode("transform", name="parentA")
    parent_b = cmds.createNode("transform", name="parentB")
    for parent in (parent_a, parent_b):
        child = cmds.createNode("transform", name="same", parent=parent)
        path = "|" + parent + "|same"
        cmds.addAttr(
            path,
            longName="settings",
            attributeType="compound",
            numberOfChildren=1,
        )
        cmds.addAttr(
            path,
            longName="mode",
            attributeType="enum",
            enumName="Off:On",
            parent="settings",
        )
    path = "|parentB|same"
    binding = MayaEnumPlugBinding(resolve_enum_plug(path, "settings.mode"))
    try:
        binding.set_value(1)
        assert cmds.getAttr(path + ".mode") == 1
        assert cmds.getAttr("|parentA|same.mode") == 0
        cmds.setAttr(path + ".settings", lock=True)
        assert not binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_resolver_rejects_other_types_and_array_ancestors(enum_node):
    with pytest.raises(TypeError):
        resolve_enum_plug(enum_node, "visibility")
    with pytest.raises(TypeError):
        resolve_enum_plug(enum_node, "translateX")
    cmds.addAttr(
        enum_node,
        longName="modes",
        attributeType="enum",
        enumName="Off:On",
        multi=True,
    )
    with pytest.raises(TypeError):
        resolve_enum_plug(enum_node, "modes")
    with pytest.raises(ValueError):
        resolve_enum_plug(enum_node, "modes[0]")


@pytest.mark.parametrize(
    "ending", ["dispose", "owner", "node", "registry", "view_model"]
)
def test_callbacks_are_released_on_all_endings(enum_node, ending):
    owner = qt.QObject()
    binding = MayaEnumPlugBinding(
        resolve_enum_plug(enum_node, "mode"), parent=owner
    )
    store = binding.store
    registry = binding.findChildren(MayaCallbackRegistry)[0]
    assert len(registry.callback_ids) == 3
    if ending == "dispose":
        binding.dispose()
    elif ending == "owner":
        owner.deleteLater()
    elif ending == "node":
        cmds.delete(enum_node)
    elif ending == "registry":
        registry.dispose()
    else:
        binding.view_model.dispose()
    flush()
    assert registry.is_disposed
    assert registry.callback_ids == ()
    assert store.is_disposed
    if qt.isValid(owner):
        owner.deleteLater()
    flush()


def test_reentrant_write_and_dispose_do_not_publish_stale_values(enum_node):
    binding = MayaEnumPlugBinding(resolve_enum_plug(enum_node, "mode"))
    binding.changed.connect(
        lambda value: binding.set_value(0) if value == 10 else None
    )
    try:
        binding.set_value(10)
        assert binding.value == cmds.getAttr(enum_node + ".mode") == 0
        vm = binding.view_model
        binding.changed.connect(lambda _value: binding.dispose())
        binding.set_value(5)
        assert not vm.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_api_enum_names_with_equals_and_short_boundaries(new_scene):
    node = cmds.createNode("network")
    selection = om.MSelectionList()
    selection.add(node)
    fn_node = om.MFnDependencyNode(selection.getDependNode(0))
    attribute = om.MFnEnumAttribute()
    obj = attribute.create("mode", "md")
    for name, value in (
        ("Negative", -32768),
        ("A=5", 0),
        ("A", 5),
        ("==", 10),
        ("Last", 32767),
    ):
        attribute.addField(name, value)
    fn_node.addAttribute(obj)
    binding = MayaEnumPlugBinding(resolve_enum_plug(node, "mode"))
    try:
        assert binding.definition.item_for_value(0).name == "A=5"
        assert binding.definition.item_for_value(5).name == "A"
        assert binding.definition.item_for_value(10).name == "=="
        binding.set_value(-32768)
        assert binding.value == -32768
        binding.set_value(32767)
        assert binding.value == 32767
    finally:
        binding.dispose()
        flush()
