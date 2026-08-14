# coding: utf-8
from __future__ import annotations

import pytest

pytestmark = pytest.mark.maya


def test_class_attribute_access(wt_add_matrix_cls):
    node_cls = wt_add_matrix_cls

    assert node_cls.NODE_TYPE == "wtAddMatrix"

    assert node_cls.matrixSum.long_name == "matrixSum"
    assert node_cls.o.long_name == "matrixSum"
    assert node_cls.o.short_name == "o"

    assert node_cls.wtMatrix.long_name == "wtMatrix"
    assert node_cls.i.long_name == "wtMatrix"
    assert node_cls.i.short_name == "i"

    assert node_cls.wtMatrix.matrixIn.long_name == "matrixIn"
    assert node_cls.wtMatrix.matrixIn.short_name == "m"
    assert node_cls.i.m.long_name == "matrixIn"
    assert node_cls.i.m.short_name == "m"

    assert node_cls.wtMatrix.weightIn.long_name == "weightIn"
    assert node_cls.wtMatrix.weightIn.short_name == "w"
    assert node_cls.i.w.long_name == "weightIn"
    assert node_cls.i.w.short_name == "w"


def test_create_node(wt_add_matrix_node, maya_cmds):
    node = wt_add_matrix_node

    assert node.name == "test"
    assert str(node) == "test"
    assert node.exists()
    assert maya_cmds.nodeType(node.name) == "wtAddMatrix"


def test_plug_cache_and_short_name_aliases(wt_add_matrix_node):
    node = wt_add_matrix_node

    assert node.matrixSum is node.matrixSum
    assert node.o is node.matrixSum

    assert node.wtMatrix is node.wtMatrix
    assert node.i is node.wtMatrix

    assert node.wtMatrix.matrixIn is node.wtMatrix.matrixIn
    assert node.wtMatrix.matrixIn is node.i.m
    assert node.wtMatrix.weightIn is node.wtMatrix.weightIn
    assert node.wtMatrix.weightIn is node.i.w

    assert node.wtMatrix[0] is node.wtMatrix[0]
    assert node.i[0] is node.wtMatrix[0]
    assert node.wtMatrix[0].matrixIn is node.wtMatrix[0].matrixIn
    assert node.wtMatrix[0].matrixIn is node.i[0].m
    assert node.wtMatrix[0].weightIn is node.wtMatrix[0].weightIn
    assert node.wtMatrix[0].weightIn is node.i[0].w


def test_get_set_short_name_aliases(modifier_manager, wt_add_matrix_node):
    node = wt_add_matrix_node

    node.wtMatrix[0].weightIn.set(100.0)
    modifier_manager.do_it_dg()
    assert node.wtMatrix[0].weightIn.get() == pytest.approx(100.0)
    assert node.i[0].w.get() == pytest.approx(100.0)

    node.i[0].w.set(200.0)
    modifier_manager.do_it_dg()
    assert node.wtMatrix[0].weightIn.get() == pytest.approx(200.0)
    assert node.i[0].w.get() == pytest.approx(200.0)


def test_next_index_connects_to_sequential_elements(
    modifier_manager,
    wt_add_matrix_cls,
):
    dst = wt_add_matrix_cls.create(modifier_manager, name="dst")
    sources = []

    for i in range(5):
        src = wt_add_matrix_cls.create(modifier_manager, name=f"src_{i}")
        sources.append(src)
        src.matrixSum.connect(dst.wtMatrix[next].matrixIn)

    modifier_manager.do_it_dg()

    for i, src in enumerate(sources):
        assert dst.wtMatrix[i].matrixIn.src_plug == f"{src.name}.matrixSum"

    assert dst.wtMatrix[5].matrixIn.src_plug is None


def test_refresh_next_index_rescans_existing_elements(
    modifier_manager,
    wt_add_matrix_cls,
    maya_cmds,
):
    dst = wt_add_matrix_cls.create(modifier_manager, name="dst")

    for i in range(3):
        src = wt_add_matrix_cls.create(modifier_manager, name=f"src_{i}")
        src.matrixSum.connect(dst.wtMatrix[next].matrixIn)

    modifier_manager.do_it_dg()

    maya_cmds.createNode("wtAddMatrix", name="src_external", skipSelect=True)
    maya_cmds.connectAttr(
        "src_external.matrixSum",
        "dst.wtMatrix[5].matrixIn",
    )

    dst.wtMatrix.refresh_next_index()
    extra_src = wt_add_matrix_cls.create(modifier_manager, name="src_extra")
    extra_src.matrixSum.connect(dst.wtMatrix[next].matrixIn)
    modifier_manager.do_it_dg()

    assert dst.wtMatrix[0].matrixIn.src_plug == "src_0.matrixSum"
    assert dst.wtMatrix[1].matrixIn.src_plug == "src_1.matrixSum"
    assert dst.wtMatrix[2].matrixIn.src_plug == "src_2.matrixSum"
    assert dst.wtMatrix[5].matrixIn.src_plug == "src_external.matrixSum"
    assert dst.wtMatrix[6].matrixIn.src_plug == "src_extra.matrixSum"
