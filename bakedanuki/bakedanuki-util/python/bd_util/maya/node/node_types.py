# coding: utf-8
from __future__ import annotations

from ._node_class_resolver import resolve_node_class
from ._node_type_registry import NODE_TYPE_BY_CLASS_NAME
from .operator.node._core import NodeOperator
from .operator.node.dag._core import DAG
from .operator.node.dag.shape._core import Shape
from .operator.node.dag.transform.base_geometry_var_group import (
    BaseGeometryVarGroup,
)

_BASE_NODE_CLASSES: dict[str, type[NodeOperator]] = {
    node_cls.__name__: node_cls
    for node_cls in (
        NodeOperator,
        DAG,
        Shape,
        BaseGeometryVarGroup,
    )
}
_NODE_CLASS_NAMES = tuple(
    sorted(set(_BASE_NODE_CLASSES) | set(NODE_TYPE_BY_CLASS_NAME))
)


class NodeTypes:
    __slots__ = ("_cache",)

    def __init__(self) -> None:
        self._cache: dict[str, type[NodeOperator]] = dict(_BASE_NODE_CLASSES)

    def resolve(self, node_type: object) -> type[NodeOperator]:
        """Maya node type名に対応するNodeOperatorクラスを返す。"""
        if not isinstance(node_type, str):
            raise TypeError(f"node_type must be str: {type(node_type)}")

        node_cls = resolve_node_class(node_type)
        if node_cls.NODE_TYPE != node_type:
            raise AttributeError(f"Unsupported node type: {node_type}")
        return node_cls

    def available_class_names(self) -> tuple[str, ...]:
        return _NODE_CLASS_NAMES

    def __getattr__(self, class_name: str) -> type[NodeOperator]:
        if class_name.startswith("_"):
            raise AttributeError(class_name)

        cached = self._cache.get(class_name)
        if cached is not None:
            return cached

        node_type = NODE_TYPE_BY_CLASS_NAME.get(class_name)
        if node_type is None:
            raise AttributeError(
                f"Unsupported NodeOperator class: {class_name}"
            )

        node_cls = resolve_node_class(node_type)
        if node_cls.__name__ != class_name:
            raise RuntimeError(
                "NodeOperator class registry mismatch: "
                f"expected {class_name}, got {node_cls.__name__}"
            )

        self._cache[class_name] = node_cls
        return node_cls

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | set(_NODE_CLASS_NAMES))
