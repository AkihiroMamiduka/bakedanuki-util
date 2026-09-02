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


def apply_create_transforms(
    nodes: Nodes,
    params: CreateTransformsParams,
) -> CreateTransformsResult:
    """Create transforms and execute the operation's DAG boundary."""
    transforms = queue_create_transforms(nodes, params)
    nodes.modifier_manager.do_it_dag()
    return CreateTransformsResult(
        node_names=tuple(transform.name for transform in transforms)
    )
