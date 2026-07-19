# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from maya.api import OpenMaya as om

from .creator import NodeCreator
from .existing_node import ExistingNode
from .modifier import ModifierManager
from .operator.node._core import NodeOperator


class _ExistingNodeAccessor:
    __slots__ = (
        "_modifier_manager",
        "_accessor_cache",
    )

    def __init__(self, modifier_manager: ModifierManager):
        self._modifier_manager = modifier_manager
        self._accessor_cache: dict[str, Callable[..., NodeOperator]] = {}

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    def __call__(
        self,
        node: str | om.MObject,
        auto_add_attr: bool = False,
    ) -> NodeOperator:
        return ExistingNode(
            node,
            modifier_manager=self._modifier_manager,
            auto_add_attr=auto_add_attr,
        )

    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        cached = self._accessor_cache.get(node_name)
        if cached is not None:
            return cached

        existing_node_accessor: Callable[..., NodeOperator] = getattr(
            ExistingNode,
            node_name,
        )

        def _wrap(
            node: str | om.MObject,
            auto_add_attr: bool = False,
        ) -> NodeOperator:
            return existing_node_accessor(
                node,
                modifier_manager=self._modifier_manager,
                auto_add_attr=auto_add_attr,
            )

        _wrap.__name__ = node_name
        _wrap.__qualname__ = f"{type(self).__name__}.{node_name}"
        _wrap.__doc__ = existing_node_accessor.__doc__
        return_type = existing_node_accessor.__annotations__.get("return")
        if return_type is not None:
            _wrap.__annotations__["return"] = return_type
        self._accessor_cache[node_name] = _wrap
        return _wrap


class Nodes:
    __slots__ = (
        "_modifier_manager",
        "_create",
        "_existing",
    )

    def __init__(self, modifier_manager: ModifierManager | None = None):
        if modifier_manager is None:
            modifier_manager = ModifierManager()

        self._modifier_manager = modifier_manager
        self._create = NodeCreator(modifier_manager=modifier_manager)
        self._existing = _ExistingNodeAccessor(
            modifier_manager=modifier_manager,
        )

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    @property
    def create(self) -> NodeCreator:
        return self._create

    @property
    def existing(self) -> _ExistingNodeAccessor:
        return self._existing
