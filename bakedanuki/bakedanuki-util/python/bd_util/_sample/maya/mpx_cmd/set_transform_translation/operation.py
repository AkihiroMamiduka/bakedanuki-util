# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from .....maya.node.nodes import Nodes
from .....maya.node.operator.node.dag.transform._core import Transform
from .....maya.value import DoubleLinear3


@dataclass(frozen=True, slots=True)
class SetTransformTranslationParams:
    node_name: str
    translation: DoubleLinear3

    def __post_init__(self) -> None:
        if not self.node_name:
            raise ValueError("node_name must not be empty.")


@dataclass(frozen=True, slots=True)
class SetTransformTranslationResult:
    node_name: str
    translation: DoubleLinear3


def queue_set_transform_translation(
    nodes: Nodes,
    params: SetTransformTranslationParams,
) -> Transform:
    """Queue a local translation edit into the caller's ModifierManager."""
    transform = nodes.existing.transform(params.node_name)
    transform.set_translate(params.translation)
    return transform
