# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from .....maya.node.nodes import Nodes
from .....maya.node.operator.node.dag.transform._core import Transform


@dataclass(frozen=True, slots=True)
class CreateTransformsParams:
    prefix: str = "bduSample"
    count: int = 2

    def __post_init__(self) -> None:
        if not self.prefix:
            raise ValueError("prefix must not be empty.")
        if self.count < 1:
            raise ValueError("count must be greater than zero.")


@dataclass(frozen=True, slots=True)
class CreateTransformsResult:
    node_names: tuple[str, ...]


def queue_create_transforms(
    nodes: Nodes,
    params: CreateTransformsParams,
) -> tuple[Transform, ...]:
    """Queue reusable scene edits into the caller's ModifierManager."""
    return tuple(
        nodes.create.transform(name=f"{params.prefix}{index + 1}")
        for index in range(params.count)
    )
