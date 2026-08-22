# coding: utf-8
from __future__ import annotations

import pytest


def test_node_types_exposes_base_and_concrete_classes(new_scene):
    import bd_util
    from bd_util.maya.node.operator.node._core import NodeOperator
    from bd_util.maya.node.operator.node.dag._core import DAG
    from bd_util.maya.node.operator.node.dag.shape._core import Shape
    from bd_util.maya.node.operator.node.dag.shape.locator import Locator
    from bd_util.maya.node.operator.node.dag.shape.sphere_locator import (
        SphereLocator,
    )
    from bd_util.maya.node.operator.node.dag.transform._core import Transform
    from bd_util.maya.node.operator.node.dag.transform.base_geometry_var_group import (
        BaseGeometryVarGroup,
    )
    from bd_util.maya.node.operator.node.dag.transform.ik_handle import (
        IkHandle,
    )
    from bd_util.maya.node.operator.node.dag.unknown_dag import UnknownDag

    node_types = bd_util.Nodes().types

    assert node_types.NodeOperator is NodeOperator
    assert node_types.DAG is DAG
    assert node_types.Transform is Transform
    assert node_types.Shape is Shape
    assert node_types.BaseGeometryVarGroup is BaseGeometryVarGroup
    assert node_types.Locator is Locator
    assert node_types.SphereLocator is SphereLocator
    assert node_types.IkHandle is IkHandle
    assert node_types.UnknownDag is UnknownDag


def test_node_types_resolves_exact_maya_node_type_names(new_scene):
    import bd_util
    from bd_util.maya.node.operator.node.dag.shape.locator import Locator
    from bd_util.maya.node.operator.node.dg.mash_audio import MASHAudio

    node_types = bd_util.Nodes().types

    assert node_types.resolve("locator") is Locator
    assert node_types.resolve("MASH_Audio") is MASHAudio
    assert node_types.resolve("and") is node_types.And
    assert node_types.And.__name__ == "And"

    with pytest.raises(AttributeError, match="Unsupported node type"):
        node_types.resolve("Locator")
    with pytest.raises(AttributeError, match="Unsupported node type"):
        node_types.resolve("plus_minus_average")
    with pytest.raises(TypeError, match="node_type must be str"):
        node_types.resolve(1)  # type: ignore[arg-type]


def test_node_types_has_completion_names_and_caches_classes(new_scene):
    import bd_util

    node_types = bd_util.Nodes().types
    class_names = node_types.available_class_names()

    assert len(class_names) == 1258
    assert class_names == tuple(sorted(class_names))
    assert {
        "NodeOperator",
        "DAG",
        "Transform",
        "Shape",
        "BaseGeometryVarGroup",
        "Locator",
        "IkHandle",
        "UnknownDag",
        "SphereLocator",
    }.issubset(class_names)
    assert set(class_names).issubset(dir(node_types))
    assert node_types.Locator is node_types.Locator


def test_node_types_rejects_unknown_or_non_class_attribute(new_scene):
    import bd_util

    node_types = bd_util.Nodes().types

    with pytest.raises(AttributeError, match="Unsupported NodeOperator class"):
        _ = node_types.NotExistingNode
    with pytest.raises(AttributeError, match="Unsupported NodeOperator class"):
        _ = node_types.locator
    with pytest.raises(AttributeError):
        node_types.Locator = node_types.Transform  # type: ignore[misc]
