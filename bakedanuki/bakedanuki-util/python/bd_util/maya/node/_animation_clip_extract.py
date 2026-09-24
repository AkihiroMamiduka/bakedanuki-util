"""AnimationClipから保存nodeを名前selectorで抽出する。"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import replace

from maya.api import OpenMaya as om

from .animation_clip import AnimationClip, NodeAnimationData, literal_name
from .operator.node._core import NodeOperator


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


def _selector_names(
    value: NodeOperator | om.MObject | str,
) -> tuple[str, ...]:
    if isinstance(value, str):
        return (literal_name(value),)
    operator = value if isinstance(value, NodeOperator) else None
    if operator is not None:
        node = operator.m_obj
    elif isinstance(value, om.MObject):
        node = value
    else:
        raise TypeError("Expected a NodeOperator, MObject or saved node name.")
    if not node.hasFn(om.MFn.kDependencyNode):
        raise TypeError("Expected a dependency node selector.")
    handle = om.MObjectHandle(node)
    if not handle.isAlive():
        raise ValueError("The clip node selector is no longer available.")
    if handle.isValid():
        name = om.MFnDependencyNode(node).name()
        return (
            (om.MFnDagNode(node).fullPathName(), name)
            if node.hasFn(om.MFn.kDagNode)
            else (name,)
        )
    if om.MFnDependencyNode(node).name():
        raise ValueError("The clip node selector is no longer available.")
    if operator is None:
        raise ValueError(
            "A pending MObject has no requested name; pass its NodeOperator "
            "or a saved node name."
        )
    if not operator._was_pending_creation:
        raise ValueError("The clip node selector is no longer available.")
    name = operator._requested_name_hint
    if name is None:
        raise ValueError(
            "A pending NodeOperator must have an explicit name to select a "
            "saved clip node."
        )
    return (literal_name(name),)


def _resolve_selector(
    data: AnimationClip,
    value: NodeOperator | om.MObject | str,
) -> NodeAnimationData:
    selectors = _selector_names(value)
    for selector in selectors[:-1]:
        matches = [node for node in data.nodes if node.name == selector]
        if matches:
            return matches[0]
    return _resolve_node(data, selectors[-1])


def extract(
    data: AnimationClip,
    *,
    nodes: Iterable[NodeOperator | om.MObject | str],
) -> AnimationClip:
    """指定した保存nodeだけを持つ独立clipを返す。"""
    if isinstance(nodes, (str, NodeOperator, om.MObject)):
        raise TypeError("nodes must be an iterable of node selectors.")
    values = tuple(nodes)
    if not values:
        raise ValueError("nodes must not be empty.")

    # 除外対象を含む元データ全体を再検証し、変更可能なKeyDataも独立させる。
    data = replace(data)
    selected: list[NodeAnimationData] = []
    selected_names: set[str] = set()
    for value in values:
        node = _resolve_selector(data, value)
        if node.name in selected_names:
            raise ValueError(f"Duplicate clip node: {node.name}.")
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
