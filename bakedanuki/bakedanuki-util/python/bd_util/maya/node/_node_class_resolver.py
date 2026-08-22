# coding: utf-8
from __future__ import annotations

import importlib
import keyword
import re
from collections.abc import Iterator
from importlib import resources

from .operator.node._core import NodeOperator

DG_NODE_PACKAGE = "bd_util.maya.node.operator.node.dg"
DAG_NODE_PACKAGE = "bd_util.maya.node.operator.node.dag"
DAG_TRANSFORM_NODE_PACKAGE = "bd_util.maya.node.operator.node.dag.transform"
DAG_SHAPE_NODE_PACKAGE = "bd_util.maya.node.operator.node.dag.shape"
NODE_CLASS_PACKAGES = (
    DG_NODE_PACKAGE,
    DAG_NODE_PACKAGE,
    DAG_TRANSFORM_NODE_PACKAGE,
    DAG_SHAPE_NODE_PACKAGE,
)
CREATOR_PACKAGES = (
    DG_NODE_PACKAGE,
    DAG_TRANSFORM_NODE_PACKAGE,
    DAG_SHAPE_NODE_PACKAGE,
)

_VALID_MODULE_NAME_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _camel_to_snake(name: str) -> str:
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", name)
    return name.lower().lstrip("_")


def _node_module_name(package_name: str, module_name: str) -> str:
    if package_name.endswith(".transform") and module_name == "transform":
        return "_core"
    if package_name.endswith(".shape") and module_name == "shape":
        return "_core"
    return module_name


def _iter_node_module_paths(
    packages: tuple[str, ...],
    module_name: str,
) -> Iterator[str]:
    for package_name in packages:
        node_module_name = _node_module_name(package_name, module_name)
        package_files = resources.files(package_name)
        if not package_files.joinpath(f"{node_module_name}.py").is_file():
            continue
        yield f"{package_name}.{node_module_name}"


def _normalize_node_name(node_name: object) -> str:
    if not isinstance(node_name, str):
        raise TypeError(f"node_name must be str: {type(node_name)}")

    module_name = _camel_to_snake(node_name)
    if module_name.endswith("_") and keyword.iskeyword(module_name[:-1]):
        module_name = module_name[:-1]

    if not _VALID_MODULE_NAME_PATTERN.fullmatch(module_name):
        raise AttributeError(f"Unsupported node type: {node_name}")
    return module_name


class _NodeClassResolver:
    __slots__ = ("_node_cls_cache",)

    def __init__(self) -> None:
        self._node_cls_cache: dict[
            tuple[tuple[str, ...], str], type[NodeOperator]
        ] = {}

    def resolve(
        self,
        node_name: str,
        packages: tuple[str, ...] = NODE_CLASS_PACKAGES,
    ) -> type[NodeOperator]:
        module_name = _normalize_node_name(node_name)
        cache_key = (packages, module_name)

        cached = self._node_cls_cache.get(cache_key)
        if cached is not None:
            return cached

        module = None
        module_path: str | None = None
        for module_path in _iter_node_module_paths(packages, module_name):
            try:
                module = importlib.import_module(module_path)
            except ModuleNotFoundError as e:
                if e.name == module_path:
                    continue
                raise
            break

        if module is None or module_path is None:
            raise AttributeError(f"Unsupported node type: {node_name}")

        node_classes = [
            obj
            for obj in vars(module).values()
            if isinstance(obj, type)
            and obj.__module__ == module.__name__
            and issubclass(obj, NodeOperator)
            and obj is not NodeOperator
            and getattr(obj, "NODE_TYPE", None) is not None
        ]
        if not node_classes:
            raise AttributeError(
                f"NodeOperator class not found: {module_path}"
            )
        if len(node_classes) > 1:
            class_names = ", ".join(cls.__name__ for cls in node_classes)
            raise RuntimeError(
                "{} {}: {}".format(
                    "Multiple NodeOperator classes found in",
                    module_path,
                    class_names,
                )
            )

        node_cls = node_classes[0]
        self._node_cls_cache[cache_key] = node_cls
        return node_cls


_NODE_CLASS_RESOLVER = _NodeClassResolver()


def resolve_node_class(
    node_name: str,
    packages: tuple[str, ...] = NODE_CLASS_PACKAGES,
) -> type[NodeOperator]:
    return _NODE_CLASS_RESOLVER.resolve(node_name, packages)
