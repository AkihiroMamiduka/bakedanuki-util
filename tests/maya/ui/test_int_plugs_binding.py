# coding: utf-8
import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaIntPlugBinding,
    MayaIntPlugsBinding,
    resolve_int_plug,
)
from bd_util.ui import qt


def flush():
    """Maya callback後のQtイベントを処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


@pytest.fixture
def integer_nodes(new_scene):
    """各整数型とcompound子を持つ二つのノードを作る。"""
    nodes = tuple(cmds.createNode("transform") for _ in range(2))
    for node in nodes:
        cmds.addAttr(node, longName="byteValue", attributeType="byte")
        cmds.addAttr(node, longName="shortValue", attributeType="short")
        cmds.addAttr(node, longName="longValue", attributeType="long")
        cmds.addAttr(
            node,
            longName="limitedValue",
            attributeType="long",
            minValue=-5,
            maxValue=5,
        )
        cmds.addAttr(
            node,
            longName="intGroup",
            attributeType="compound",
            numberOfChildren=1,
        )
        cmds.addAttr(
            node,
            longName="childValue",
            attributeType="short",
            parent="intGroup",
        )
    yield nodes
    flush()


@pytest.mark.parametrize(
    "attribute, value, expected_range",
    [
        ("byteValue", 255, (0, 255)),
        ("shortValue", -(2**15), (-(2**15), 2**15 - 1)),
        ("longValue", 2**31 - 1, (-(2**31), 2**31 - 1)),
        ("intGroup.childValue", 32767, (-(2**15), 2**15 - 1)),
    ],
)
def test_resolve_read_and_write_integer_types(
    integer_nodes, attribute, value, expected_range
):
    """型付きPlugの実値とMaya bindingの範囲を確認する。"""
    node = integer_nodes[0]
    name = f"{node}.{attribute}"
    cmds.setAttr(name, value)
    plug = resolve_int_plug(node, attribute)
    assert plug.get() == value
    binding = MayaIntPlugBinding(plug)
    try:
        assert binding.value == value
        presentation = binding.view_model.presentation
        assert (presentation.minimum, presentation.maximum) == expected_range
        assert not binding.set_value(value)
        next_value = 128 if attribute == "byteValue" else 1
        assert binding.set_value(next_value)
        assert cmds.getAttr(name) == binding.value == next_value
        cmds.setAttr(name, 2)
        flush()
        assert binding.value == 2
    finally:
        binding.dispose()
        flush()


def test_single_binding_hard_limits_and_undo(integer_nodes):
    """入力前のhard limit検証とUndo後の再同期を確認する。"""
    node = integer_nodes[0]
    name = node + ".limitedValue"
    cmds.setAttr(name, 2)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    binding = MayaIntPlugBinding(resolve_int_plug(node, "limitedValue"))
    try:
        assert binding.value == 2
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        assert (
            binding.view_model.presentation.minimum,
            binding.view_model.presentation.maximum,
        ) == (-5, 5)
        with pytest.raises(ValueError):
            binding.set_value(6)
        assert cmds.getAttr(name) == 2
        assert binding.set_value(-5)
        assert cmds.getAttr(name) == -5
        cmds.undo()
        flush()
        assert binding.value == cmds.getAttr(name) == 2
        cmds.redo()
        flush()
        assert binding.value == cmds.getAttr(name) == -5
    finally:
        binding.dispose()
        flush()


def test_multiple_types_validate_all_targets_before_write(integer_nodes):
    """混在値と型ごとの範囲を維持し、一括書込みを原子的に行う。"""
    first, second = integer_nodes
    cmds.setAttr(first + ".longValue", 3)
    cmds.setAttr(second + ".byteValue", 4)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    binding = MayaIntPlugsBinding(
        (
            resolve_int_plug(first, "longValue"),
            resolve_int_plug(second, "byteValue"),
        )
    )
    try:
        assert binding.value == 3
        assert binding.is_mixed
        assert binding.target_count == binding.writable_count == 2
        with pytest.raises(ValueError):
            binding.set_value(-1)
        assert (
            cmds.getAttr(first + ".longValue"),
            cmds.getAttr(second + ".byteValue"),
        ) == (
            3,
            4,
        )
        assert binding.set_value(200)
        assert not binding.is_mixed
        assert (
            cmds.getAttr(first + ".longValue"),
            cmds.getAttr(second + ".byteValue"),
        ) == (
            200,
            200,
        )
        cmds.undo()
        flush()
        assert binding.value == 3
        assert binding.is_mixed
        assert binding.apply_representative_value()
        assert cmds.getAttr(second + ".byteValue") == 3
    finally:
        binding.dispose()
        flush()


def test_invalid_types_and_array_are_rejected(integer_nodes):
    """bool・enum・float・配列・compound親を整数対象から除外する。"""
    node = integer_nodes[0]
    cmds.addAttr(node, longName="arrayValue", attributeType="long", multi=True)
    for attribute in ("visibility", "rotateOrder", "scaleX", "intGroup"):
        with pytest.raises(TypeError):
            resolve_int_plug(node, attribute)
    with pytest.raises(ValueError):
        resolve_int_plug(node, "arrayValue[0]")


def test_lock_connection_and_deletion_stop_input(integer_nodes):
    """属性状態を監視し、接続中と削除後の編集を止める。"""
    target, source = integer_nodes
    name = target + ".longValue"
    binding = MayaIntPlugBinding(resolve_int_plug(target, "longValue"))
    try:
        assert binding.view_model.set_value_command.can_execute
        cmds.setAttr(name, lock=True)
        flush()
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value(7)
        cmds.setAttr(name, lock=False)
        flush()
        assert binding.view_model.set_value_command.can_execute
        cmds.connectAttr(source + ".longValue", name)
        flush()
        assert not binding.view_model.set_value_command.can_execute
        cmds.setAttr(source + ".longValue", 9)
        flush()
        assert binding.value == 9
        assert not binding.set_value(10)
        cmds.disconnectAttr(source + ".longValue", name)
        flush()
        assert binding.view_model.set_value_command.can_execute
        cmds.delete(target)
        flush()
        assert not binding.store.is_available
        assert not binding.set_value(11)
    finally:
        binding.dispose()
        flush()
