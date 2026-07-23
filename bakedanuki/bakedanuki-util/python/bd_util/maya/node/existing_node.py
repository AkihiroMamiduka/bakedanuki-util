# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from maya.api import OpenMaya as om

from .creator import NodeCreator
from .modifier import ModifierManager
from .operator.node._core import NodeOperator


class _ExistingNodeMeta(type):
    _accessor_cache: dict[str, Callable[..., NodeOperator]] = {}

    def __getattr__(cls, node_name: str) -> Callable[..., NodeOperator]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        cached = cls._accessor_cache.get(node_name)
        if cached is not None:
            return cached

        node_cls = _get_node_cls(node_name, ModifierManager())

        def _wrap(
            node: str | om.MObject,
            modifier_manager: ModifierManager | None = None,
            auto_add_attr: bool = False,
        ) -> NodeOperator:
            return _wrap_existing_node(
                node,
                modifier_manager=modifier_manager,
                auto_add_attr=auto_add_attr,
                expected_node_cls=node_cls,
            )

        _wrap.__name__ = node_name
        _wrap.__qualname__ = f"{cls.__name__}.{node_name}"
        _wrap.__doc__ = (
            f"Wrap an existing {node_cls.NODE_TYPE} node as "
            f"{node_cls.__name__}."
        )
        _wrap.__annotations__["return"] = node_cls
        cls._accessor_cache[node_name] = _wrap
        return _wrap


class ExistingNode(metaclass=_ExistingNodeMeta):
    def __new__(
        cls,
        node: str | om.MObject,
        modifier_manager: ModifierManager | None = None,
        auto_add_attr: bool = False,
    ) -> NodeOperator:
        return _wrap_existing_node(
            node,
            modifier_manager=modifier_manager,
            auto_add_attr=auto_add_attr,
        )


def _wrap_existing_node(
    node: str | om.MObject,
    modifier_manager: ModifierManager | None = None,
    auto_add_attr: bool = False,
    expected_node_cls: type[NodeOperator] | None = None,
) -> NodeOperator:
    m_obj = _to_m_object(node)
    node_type = _get_node_type(m_obj)

    if modifier_manager is None:
        modifier_manager = ModifierManager()

    if expected_node_cls is None:
        node_cls = _get_node_cls(node_type, modifier_manager)
    else:
        node_cls = expected_node_cls
        if node_type != node_cls.NODE_TYPE:
            node_name = om.MFnDependencyNode(m_obj).name()
            raise TypeError(
                "Node type mismatch for {!r}: expected {!r}, got {!r}".format(
                    node_name,
                    node_cls.NODE_TYPE,
                    node_type,
                )
            )

    return node_cls(
        modifier_manager,
        m_obj=m_obj,
        auto_add_attr=auto_add_attr,
    )


def _to_m_object(node: str | om.MObject) -> om.MObject:
    if isinstance(node, om.MObject):
        return node
    if isinstance(node, str):
        selection = om.MSelectionList()
        try:
            selection.add(node)
        except RuntimeError as e:
            raise ValueError(f"Node not found: {node}") from e
        return selection.getDependNode(0)
    raise TypeError(f"node must be str or MObject: {type(node)}")


def _get_node_type(m_obj: om.MObject) -> str:
    return om.MFnDependencyNode(m_obj).typeName


def _get_node_cls(
    node_type: str,
    modifier_manager: ModifierManager,
) -> type[NodeOperator]:
    try:
        return NodeCreator(modifier_manager=modifier_manager).node_class(
            node_type
        )
    except AttributeError as e:
        raise AttributeError(f"Unsupported node type: {node_type}") from e
