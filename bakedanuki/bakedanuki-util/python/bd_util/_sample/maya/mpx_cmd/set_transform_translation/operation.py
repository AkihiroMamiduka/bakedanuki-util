# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from .....maya.node.nodes import Nodes
from .....maya.node.operator.node.dag.transform._core import Transform
from .....maya.value import DoubleLinear3


@dataclass(frozen=True, slots=True)
class SetTransformTranslationParams:
    """対象ノード名とローカル移動値を保持する。

    `node_name` は空文字列不可。
    """

    node_name: str
    translation: DoubleLinear3

    def __post_init__(self) -> None:
        if not self.node_name:
            raise ValueError("node_name must not be empty.")


@dataclass(frozen=True, slots=True)
class SetTransformTranslationResult:
    """更新したノード名と移動値を保持する。"""

    node_name: str
    translation: DoubleLinear3


def queue_set_transform_translation(
    nodes: Nodes,
    params: SetTransformTranslationParams,
) -> Transform:
    """ローカル移動値の変更を共有 `ModifierManager` に予約する。

    Args:
        nodes: 既存ノードの取得に使う `Nodes`。その `modifier_manager` に操作を積む。
        params: `node_name` と `translation` を保持する変更条件。

    Returns:
        対象の transform ノード。
    """
    transform = nodes.existing.transform(params.node_name)
    transform.set_translate(params.translation)
    return transform


def apply_set_transform_translation(
    nodes: Nodes,
    params: SetTransformTranslationParams,
) -> SetTransformTranslationResult:
    """ローカル移動値を設定し、変更があれば DG modifier を実行する。

    Args:
        nodes: 既存ノードの取得に使う `Nodes`。変更時はその `modifier_manager` を実行する。
        params: `node_name` と `translation` を保持する変更条件。

    Returns:
        対象ノード名と設定した移動値を保持する結果。
    """
    transform = queue_set_transform_translation(nodes, params)
    current_translation = transform.translate.get().as_tuple()
    if current_translation != params.translation.as_tuple():
        nodes.modifier_manager.do_it_dg()
    return SetTransformTranslationResult(
        node_name=transform.name,
        translation=params.translation,
    )
