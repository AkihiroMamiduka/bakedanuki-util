# coding: utf-8
"""同期的なscalar属性の解決中だけ、同じnodeの操作オブジェクトを共有する。"""

from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass

from maya.api import OpenMaya as om

from ..._identity import ObjectIdentityIndex
from ...node import Nodes
from ...node.operator.node._core import NodeOperator

__all__ = ["shared_scalar_plug_nodes"]


@dataclass(frozen=True)
class _ResolvedNode:
    """wrapper作成時のDAG経路を保持し、後続の解決先だけを更新可能にする。"""

    operator: NodeOperator
    path: om.MDagPath | None


class _ScalarPlugNodes:
    """名前の鮮度を維持し、構築範囲内だけnode実体ごとのwrapperを保持する。"""

    def __init__(self) -> None:
        """解決が必要になるまでNodesの生成を遅らせる。"""
        self._bd_nodes: Nodes | None = None
        self._identities = ObjectIdentityIndex()
        self._nodes: dict[int, _ResolvedNode] = {}
        self._closed = False

    def resolve(self, node_name: str) -> NodeOperator:
        """毎回名前を解決し、実体やDAG経路が変わったwrapperは再利用しない。"""
        if self._closed:
            raise RuntimeError(
                "終了したscalar属性の解決範囲は再利用できません"
            )
        selection = om.MSelectionList()
        try:
            selection.add(node_name)
        except RuntimeError as error:
            raise ValueError(f"Node not found: {node_name}") from error
        m_obj = selection.getDependNode(0)
        identity = self._identities.index(m_obj)
        previous = self._nodes.get(identity)
        path = (
            om.MDagPath.getAPathTo(m_obj)
            if m_obj.hasFn(om.MFn.kDagNode)
            else None
        )
        if previous is not None and (
            path is None
            or (
                previous.path is not None
                and previous.path.isValid()
                and previous.path == path
            )
        ):
            return previous.operator

        # 古い行が持つwrapperを書き換えず、以後の解決先だけを置き換える
        if self._bd_nodes is None:
            self._bd_nodes = Nodes()
        operator = self._bd_nodes.existing(m_obj)
        self._nodes[identity] = _ResolvedNode(operator, path)
        return operator

    def close(self) -> None:
        """例外時も解決済み実体を解放し、別の操作へ持ち越さない。"""
        self._closed = True
        self._nodes.clear()
        self._identities = ObjectIdentityIndex()
        self._bd_nodes = None


_CURRENT_NODES: ContextVar[_ScalarPlugNodes | None] = ContextVar(
    "scalar_plug_nodes", default=None
)


@contextmanager
def shared_scalar_plug_nodes() -> Generator[None, None, None]:
    """範囲内のscalar resolverで同じnodeの操作オブジェクトを共有する。

    `resolve_bool_plug()`、`resolve_float_plug()`、`resolve_int_plug()`、
    `resolve_enum_plug()`、`resolve_string_plug()`の同期的な対象構築に使う。
    node実体ごとに`NodeOperator`を共有し、範囲内の`modifier_manager`も共通にする。
    属性の正式path・型と、名前・実体・DAG経路は毎回照合し、入れ子の範囲は独立する。
    範囲を抜けると索引を解放し、返却済みのplugはそのまま使用できる。
    値の書込み、監視、検証、Undoの境界は変更しない。
    """
    nodes = _ScalarPlugNodes()
    token = _CURRENT_NODES.set(nodes)
    try:
        yield
    finally:
        _CURRENT_NODES.reset(token)
        nodes.close()


def resolve_scalar_node(node_name: str) -> NodeOperator:
    """明示範囲の外では従来どおり独立したnodeを返す。"""
    nodes = _CURRENT_NODES.get()
    return (
        Nodes().existing(node_name)
        if nodes is None
        else nodes.resolve(node_name)
    )
