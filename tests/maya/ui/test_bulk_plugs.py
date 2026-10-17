# coding: utf-8
"""監視しない一時Bindingと、実体索引・限定属性取得を検証する。"""

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya import _identity
from bd_util.maya.node.inspection import inspect_scalar_attributes
from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaFloatPlugsBinding,
    MayaIntPlugsBinding,
    MayaEnumPlugsBinding,
    MayaStringPlugsBinding,
    resolve_bool_plug,
    resolve_float_plug,
    resolve_int_plug,
    resolve_enum_plug,
    resolve_string_plug,
)
from bd_util.ui import qt


@pytest.mark.parametrize("kind", ["bool", "double", "long", "enum", "string"])
def test_unmonitored_binding_validates_current_targets(new_scene, kind):
    """監視を作らず、外部変更は明示同期し、入力時に後続のlockを検証する。"""
    factories = {
        "bool": (MayaBoolPlugsBinding, resolve_bool_plug, True),
        "double": (MayaFloatPlugsBinding, resolve_float_plug, 2.5),
        "long": (MayaIntPlugsBinding, resolve_int_plug, 2),
        "enum": (MayaEnumPlugsBinding, resolve_enum_plug, 1),
        "string": (MayaStringPlugsBinding, resolve_string_plug, "updated"),
    }
    nodes = [cmds.createNode("network") for _ in range(2)]
    for node in nodes:
        if kind == "string":
            cmds.addAttr(node, longName="value", dataType="string")
        else:
            options = {"enumName": "A:B"} if kind == "enum" else {}
            cmds.addAttr(node, longName="value", attributeType=kind, **options)
    factory, resolver, value = factories[kind]
    binding = factory([resolver(n, "value") for n in nodes], monitor=False)
    try:
        assert binding.store._registry is None
        assert not binding.store._input_lock_timer.isActive()
        initial = binding.value
        if kind == "string":
            cmds.setAttr(nodes[0] + ".value", value, type="string")
        else:
            cmds.setAttr(nodes[0] + ".value", value)
        qt.QApplication.processEvents()
        assert binding.value == initial
        binding.refresh()
        assert binding.value == value
        cmds.setAttr(nodes[1] + ".value", lock=True)
        cmds.flushUndo()
        assert not binding.set_value(value)
        assert binding.writable_count == 1
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
        binding.deleteLater()
    with pytest.raises(TypeError, match="monitor"):
        factory([resolver(nodes[0], "value")], monitor=1)


def test_path_inspection_and_identity_hash_collisions(new_scene, monkeypatch):
    """hash衝突でも実体を区別し、同じplugだけを重複として除外する。"""
    nodes = [cmds.createNode("transform") for _ in range(2)]

    def same_hash(node):
        """異なる実体が同じhashを返す条件を作る。"""
        return 1

    monkeypatch.setattr(_identity, "_object_hash", same_hash)
    objects = _identity.ObjectIdentityIndex()
    plugs = _identity.PlugIdentitySet()
    for index, name in enumerate(nodes):
        selection = om.MSelectionList()
        selection.add(name + ".translateX")
        plug = selection.getPlug(0)
        assert objects.index(plug.node()) == index
        assert objects.index(plug.node()) == index
        assert plugs.add(plug)
        assert not plugs.add(plug)
    infos = inspect_scalar_attributes(
        nodes[0],
        paths=(
            "tx",
            "translate.translateX",
            "missing",
            "translate",
            "visibility",
        ),
    )
    assert [a.path for a in infos] == ["translate.translateX", "visibility"]
