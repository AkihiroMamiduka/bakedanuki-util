# coding: utf-8
from __future__ import annotations

import importlib
import pkgutil


def test_all_generated_shape_modules_import():
    from bd_util.maya.node._maya_version import (
        _node_name_to_module_name,
        maya_major_version,
    )
    from bd_util.maya.node._node_version_registry import (
        NODE_TYPE_VERSION_RANGES,
    )
    from bd_util.maya.node.operator.node.dag import shape as shape_package
    from bd_util.maya.node.operator.node.dag.shape import (
        _generated as generated_package,
    )

    public_module_names = {
        module.name
        for module in pkgutil.iter_modules(shape_package.__path__)
        if not module.name.startswith("_")
    }
    generated_module_names = {
        module.name
        for module in pkgutil.iter_modules(generated_package.__path__)
        if not module.name.startswith("_")
    }

    maya_version = maya_major_version()
    future_module_names = {
        _node_name_to_module_name(node_type)
        for node_type, ranges in NODE_TYPE_VERSION_RANGES.items()
        if min(minimum for minimum, _ in ranges) > maya_version
    }
    available_public_module_names = public_module_names - future_module_names

    assert len(public_module_names) == 97
    assert generated_module_names == available_public_module_names | {"shape"}

    for module_name in sorted(available_public_module_names):
        importlib.import_module(f"{shape_package.__name__}.{module_name}")
        importlib.import_module(f"{generated_package.__name__}.{module_name}")
