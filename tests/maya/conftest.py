# coding: utf-8
from __future__ import annotations

import pytest


def pytest_configure(config):
    try:
        import maya.standalone
    except Exception:
        return

    try:
        maya.standalone.initialize(name="python")
    except Exception:
        pass


@pytest.fixture
def maya_cmds():
    return pytest.importorskip("maya.cmds")


@pytest.fixture
def maya_om():
    return pytest.importorskip("maya.api.OpenMaya")


@pytest.fixture
def new_scene(maya_cmds):
    maya_cmds.file(new=True, force=True)
    yield
    maya_cmds.file(new=True, force=True)


@pytest.fixture
def modifier_manager(new_scene, maya_cmds, maya_om):
    from bd_util.maya.node.modifier import ModifierManager

    return ModifierManager()


@pytest.fixture
def plus_minus_average_cls(maya_cmds, maya_om):
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    return PlusMinusAverage


@pytest.fixture
def plus_minus_average_node(modifier_manager, plus_minus_average_cls):
    node = plus_minus_average_cls.create(modifier_manager, name="test")
    modifier_manager.do_it_dg()
    return node


@pytest.fixture
def wt_add_matrix_cls(maya_cmds, maya_om):
    from bd_util.maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix

    return WtAddMatrix


@pytest.fixture
def wt_add_matrix_node(modifier_manager, wt_add_matrix_cls):
    node = wt_add_matrix_cls.create(modifier_manager, name="test")
    modifier_manager.do_it_dg()
    return node
