"""保存済みノードを名前やノード参照から選ぶ。"""

from __future__ import annotations

from collections.abc import Iterable

from maya.api import OpenMaya as om

from .animation_clip import literal_name
from .operator.node._core import NodeOperator


def _leaf_name(name: str) -> str:
    return name.rsplit("|", 1)[-1]


def _selector_names(
    value: NodeOperator | om.MObject | str, *, kind: str
) -> tuple[str, ...]:
    """既存ノードや名前付き作成待ちノードから保存名候補を得る。"""
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
        raise ValueError(f"The {kind} node selector is no longer available.")
    if handle.isValid():
        name = om.MFnDependencyNode(node).name()
        return (
            (om.MFnDagNode(node).fullPathName(), name)
            if node.hasFn(om.MFn.kDagNode)
            else (name,)
        )
    if om.MFnDependencyNode(node).name():
        raise ValueError(f"The {kind} node selector is no longer available.")
    if operator is None:
        raise ValueError(
            "A pending MObject has no requested name; pass its NodeOperator "
            "or a saved node name."
        )
    if not operator._was_pending_creation:
        raise ValueError(f"The {kind} node selector is no longer available.")
    name = operator._requested_name_hint
    if name is None:
        raise ValueError(
            "A pending NodeOperator must have an explicit name to select a "
            f"saved {kind} node."
        )
    return (literal_name(name),)


def _resolve_name(
    saved_names: tuple[str, ...], selector: str, *, kind: str
) -> str:
    """保存名または DAG の末尾名から一意のノード名を選ぶ。"""
    matches = (
        [name for name in saved_names if name == selector]
        if "|" in selector
        else [name for name in saved_names if _leaf_name(name) == selector]
    )
    if not matches:
        raise ValueError(f"Unknown {kind} node: {selector}.")
    if len(matches) > 1:
        candidates = ", ".join(matches)
        raise ValueError(
            f"Ambiguous {kind} node: {selector}. Use one of: {candidates}."
        )
    return matches[0]


def select_saved_node_names(
    saved_names: Iterable[str],
    *,
    nodes: Iterable[NodeOperator | om.MObject | str],
    kind: str,
) -> tuple[str, ...]:
    """保存済みノード名を `nodes` の指定順に解決する。"""
    if isinstance(nodes, (str, NodeOperator, om.MObject)):
        raise TypeError("nodes must be an iterable of node selectors.")
    values = tuple(nodes)
    if not values:
        raise ValueError("nodes must not be empty.")
    names = tuple(saved_names)
    selected: list[str] = []
    seen: set[str] = set()
    for value in values:
        selectors = _selector_names(value, kind=kind)
        name = next(
            (selector for selector in selectors[:-1] if selector in names),
            None,
        )
        if name is None:
            name = _resolve_name(names, selectors[-1], kind=kind)
        if name in seen:
            raise ValueError(f"Duplicate {kind} node: {name}.")
        seen.add(name)
        selected.append(name)
    return tuple(selected)
