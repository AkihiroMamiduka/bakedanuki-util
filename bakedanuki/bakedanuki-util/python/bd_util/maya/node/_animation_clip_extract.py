"""`AnimationClip` から名前やノード参照で保存ノードを抽出する。"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import replace

from maya.api import OpenMaya as om

from ._saved_node_selector import select_saved_node_names
from .animation_clip import AnimationClip, NodeAnimationData
from .operator.node._core import NodeOperator


def extract(
    data: AnimationClip,
    *,
    nodes: Iterable[NodeOperator | om.MObject | str],
) -> AnimationClip:
    """指定した保存ノードだけを持つ独立した clip を返す。

    Args:
        data: 抽出元の clip。
        nodes: 保存名、既存ノード、または名前付き作成待ちノード。

    Returns:
        指定順に並ぶノードと必要な親レイヤーだけを持つ clip。

    Raises:
        ValueError: 対象が空、重複、見つからない、または名前が曖昧な場合。
    """
    # 除外対象を含む元データ全体を再検証し、変更可能な `KeyData` も独立させる。
    data = replace(data)
    selected_names = select_saved_node_names(
        (node.name for node in data.nodes), nodes=nodes, kind="clip"
    )
    by_name: dict[str, NodeAnimationData] = {
        node.name: node for node in data.nodes
    }
    selected = tuple(by_name[name] for name in selected_names)
    if not any(node.channels for node in selected):
        raise ValueError("The selected clip nodes contain no channels.")

    required_layers = {
        channel.layer
        for node in selected
        for channel in node.channels
        if channel.layer is not None
    }
    parents = {layer.name: layer.parent for layer in data.layers}
    for name in tuple(required_layers):
        parent = parents[name]
        while parent is not None:
            required_layers.add(parent)
            parent = parents[parent]

    return replace(
        data,
        nodes=tuple(selected),
        layers=tuple(
            layer for layer in data.layers if layer.name in required_layers
        ),
    )
