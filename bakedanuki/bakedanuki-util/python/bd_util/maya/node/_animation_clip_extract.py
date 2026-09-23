"""AnimationClipから保存nodeを抽出する。sceneは参照しない。"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import replace

from .animation_clip import AnimationClip, NodeAnimationData, literal_name


def _leaf_name(name: str) -> str:
    return name.rsplit("|", 1)[-1]


def _resolve_node(data: AnimationClip, selector: str) -> NodeAnimationData:
    matches = (
        [node for node in data.nodes if node.name == selector]
        if "|" in selector
        else [node for node in data.nodes if _leaf_name(node.name) == selector]
    )
    if not matches:
        raise ValueError(f"Unknown clip node: {selector}.")
    if len(matches) > 1:
        candidates = ", ".join(node.name for node in matches)
        raise ValueError(
            f"Ambiguous clip node: {selector}. Use one of: {candidates}."
        )
    return matches[0]


def extract(data: AnimationClip, *, nodes: Iterable[str]) -> AnimationClip:
    """指定した保存nodeだけを持つ独立clipを返す。"""
    if isinstance(nodes, str):
        raise TypeError("nodes must be an iterable of node names.")
    selectors = tuple(literal_name(node) for node in nodes)
    if not selectors:
        raise ValueError("nodes must not be empty.")

    # 除外対象を含む元データ全体を再検証し、変更可能なKeyDataも独立させる。
    data = replace(data)
    selected: list[NodeAnimationData] = []
    selected_names: set[str] = set()
    for selector in selectors:
        node = _resolve_node(data, selector)
        if node.name in selected_names:
            raise ValueError(f"Duplicate clip node: {selector}.")
        selected_names.add(node.name)
        selected.append(node)
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
