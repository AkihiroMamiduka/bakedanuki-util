# coding: utf-8
from __future__ import annotations

import importlib
import pkgutil


def test_all_generated_shape_modules_import():
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

    assert len(public_module_names) == 81
    assert generated_module_names == public_module_names | {"shape"}

    for module_name in sorted(public_module_names):
        importlib.import_module(f"{shape_package.__name__}.{module_name}")
        importlib.import_module(f"{generated_package.__name__}.{module_name}")
