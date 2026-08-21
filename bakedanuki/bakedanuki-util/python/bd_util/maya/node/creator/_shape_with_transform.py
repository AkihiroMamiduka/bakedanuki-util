# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from ..modifier import ModifierManager
from ..operator.node._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator
from ..operator.node.dag._core import DAG
from ..operator.node.dag.shape._core import Shape
from ..operator.node.dag.transform._core import Transform
from ._shape_types import CREATABLE_SHAPE_NODE_TYPES


class ShapeWithTransformCreator:
    __slots__ = (
        "__dict__",
        "_modifier_manager",
        "_node_class_resolver",
    )

    def __init__(
        self,
        modifier_manager: ModifierManager,
        node_class_resolver: Callable[[str], type[NodeOperator]],
    ) -> None:
        self._modifier_manager = modifier_manager
        self._node_class_resolver = node_class_resolver

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    def create(
        self,
        node_name: str,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        shape_name: str | None = None,
        parent: DAG | None = None,
    ) -> tuple[Transform, Shape]:
        node_cls = self._shape_node_class(node_name)
        return self._create(
            node_cls,
            name=name,
            auto_add_attr=auto_add_attr,
            shape_name=shape_name,
            parent=parent,
        )

    def available_node_names(self) -> tuple[str, ...]:
        return tuple(sorted(CREATABLE_SHAPE_NODE_TYPES))

    def __getattr__(
        self,
        node_name: str,
    ) -> Callable[..., tuple[Transform, Shape]]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        node_cls = self._shape_node_class(node_name)

        def _create_shape_with_transform(
            name: str | None = None,
            auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
            *,
            shape_name: str | None = None,
            parent: DAG | None = None,
        ) -> tuple[Transform, Shape]:
            return self._create(
                node_cls,
                name=name,
                auto_add_attr=auto_add_attr,
                shape_name=shape_name,
                parent=parent,
            )

        create_func: Callable[..., tuple[Transform, Shape]] = (
            _create_shape_with_transform
        )
        create_func.__name__ = node_name
        create_func.__qualname__ = f"{type(self).__name__}.{node_name}"
        create_func.__doc__ = (
            f"Create Transform and {node_cls.__name__} together."
        )
        setattr(self, node_name, create_func)
        return create_func

    def __dir__(self) -> list[str]:
        return sorted(
            set(super().__dir__()) | set(self.available_node_names())
        )

    def _shape_node_class(self, node_name: str) -> type[Shape]:
        node_cls = self._node_class_resolver(node_name)
        if not issubclass(node_cls, Shape):
            raise AttributeError(f"Unsupported shape node type: {node_name}")
        return node_cls

    def _create(
        self,
        node_cls: type[Shape],
        name: str | None,
        auto_add_attr: bool,
        shape_name: str | None,
        parent: DAG | None,
    ) -> tuple[Transform, Shape]:
        transform = Transform.create(
            self._modifier_manager,
            name=name,
            auto_add_attr=auto_add_attr,
            parent=parent,
        )
        if shape_name is None and name is not None:
            shape_name = f"{name}Shape"
        shape = node_cls.create(
            self._modifier_manager,
            name=shape_name,
            auto_add_attr=auto_add_attr,
            parent=transform,
        )
        return transform, shape
