# coding: utf-8
from __future__ import annotations

import pytest


def test_node_type_version_ranges():
    from bd_util.maya.node._maya_version import is_node_type_available

    assert is_node_type_available("absolute", 2025)
    assert not is_node_type_available("absoluteDL", 2025)
    assert is_node_type_available("absoluteDL", 2026)
    assert is_node_type_available("absoluteDL", 2027)
    assert is_node_type_available("addDoubleLinear", 2025)
    assert not is_node_type_available("addDoubleLinear", 2026)
    assert not is_node_type_available("shotLabel", 2026)
    assert is_node_type_available("shotLabel", 2027)
    assert not is_node_type_available("dgaDelta", 2025)
    assert is_node_type_available("dgaDelta", 2026)
    assert is_node_type_available("ufeLightArea", 2026)
    assert not is_node_type_available("UsdDefaultSettings", 2026)
    assert is_node_type_available("UsdDefaultSettings", 2027)
    assert is_node_type_available("bifrostClosureConverter", 2027)
    assert is_node_type_available("mayaUsdGeometryGizmoShape", 2025)
    assert not is_node_type_available("mayaUsdGeometryGizmoShape", 2026)


def test_generated_package_path_prefers_newest_compatible_overlay(
    tmp_path,
    monkeypatch,
):
    from bd_util.maya.node import _maya_version

    baseline_path = tmp_path / "_generated"
    maya_2026_path = tmp_path / "_generated_maya2026"
    maya_2027_path = tmp_path / "_generated_maya2027"
    baseline_path.mkdir()
    maya_2026_path.mkdir()
    maya_2027_path.mkdir()
    package_path = [str(baseline_path)]
    monkeypatch.setattr(_maya_version, "maya_major_version", lambda: 2027)

    _maya_version.configure_generated_package_path(
        package_path,
        str(baseline_path / "__init__.py"),
    )

    assert package_path == [
        str(maya_2027_path),
        str(maya_2026_path),
        str(baseline_path),
    ]


def test_generated_package_path_uses_baseline_in_maya_2025(
    tmp_path,
    monkeypatch,
):
    from bd_util.maya.node import _maya_version

    baseline_path = tmp_path / "_generated"
    (tmp_path / "_generated_maya2026").mkdir()
    baseline_path.mkdir()
    package_path = [str(baseline_path)]
    monkeypatch.setattr(_maya_version, "maya_major_version", lambda: 2025)

    _maya_version.configure_generated_package_path(
        package_path,
        str(baseline_path / "__init__.py"),
    )

    assert package_path == [str(baseline_path)]


def test_absolute_uses_the_running_maya_schema(new_scene):
    import bd_util as bdu
    from bd_util.maya.node._maya_version import maya_major_version
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.double import (
        DoubleAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.double_linear import (
        DoubleLinearAttrOperator,
    )

    absolute_cls = bdu.Nodes().types.Absolute
    expected_type = (
        DoubleLinearAttrOperator
        if maya_major_version() == 2025
        else DoubleAttrOperator
    )

    assert isinstance(absolute_cls.input, expected_type)
    assert isinstance(absolute_cls.output, expected_type)


def test_poly_smart_bevel_uses_the_maya_2027_schema(new_scene):
    import bd_util as bdu
    from bd_util.maya.node._maya_version import maya_major_version

    maya_version = maya_major_version()
    if maya_version == 2025:
        with pytest.raises(
            AttributeError,
            match="polySmartBevel.*unavailable in Maya 2025",
        ):
            _ = bdu.Nodes().types.PolySmartBevel
        return

    poly_smart_bevel_cls = bdu.Nodes().types.PolySmartBevel
    assert hasattr(poly_smart_bevel_cls, "cutbackRelaxation") == (
        maya_version >= 2027
    )
    assert hasattr(poly_smart_bevel_cls, "removeIsolatedArcs") == (
        maya_version >= 2027
    )


def test_version_only_node_creation_follows_the_running_maya(new_scene):
    import bd_util as bdu
    from bd_util.maya.node._maya_version import maya_major_version

    nodes = bdu.Nodes()
    maya_version = maya_major_version()

    if maya_version == 2025:
        old_node = nodes.create.addDoubleLinear(name="old_node")
        with pytest.raises(
            AttributeError,
            match="absoluteDL.*unavailable in Maya 2025",
        ):
            nodes.create.absoluteDL(name="new_node")

        nodes.modifier_manager.do_it_dg()
        assert old_node.exists()
        return

    new_node = nodes.create.absoluteDL(name="new_node")
    with pytest.raises(
        AttributeError,
        match=rf"addDoubleLinear.*unavailable in Maya {maya_version}",
    ):
        nodes.create.addDoubleLinear(name="old_node")

    nodes.modifier_manager.do_it_dg()
    assert new_node.exists()
