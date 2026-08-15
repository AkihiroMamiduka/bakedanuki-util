# coding: utf-8
from __future__ import annotations

from typing import Self

from .....modifier import ModifierManager
from ..._core import DEFAULT_VALUE_AUTO_ADD_ATTR
from .._core import DAG
from ._generated.shape import GeneratedShape


class Shape(GeneratedShape):
    __slots__ = ()

    NODE_TYPE = "shape"

    @classmethod
    def create(
        cls,
        modifier_manager: ModifierManager,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: DAG | None = None,
    ) -> Self:
        if cls is Shape:
            raise TypeError("Shape is an abstract NodeOperator base class")
        if parent is None:
            raise TypeError("parent is required for shape nodes")
        return super().create(
            modifier_manager,
            name=name,
            auto_add_attr=auto_add_attr,
            parent=parent,
        )
