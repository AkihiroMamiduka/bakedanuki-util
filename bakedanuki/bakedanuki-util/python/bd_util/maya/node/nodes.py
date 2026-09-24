# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Literal

from maya.api import OpenMaya as om

from .creator import NodeCreator
from .existing_node import ExistingNode
from .modifier import ModifierManager
from .node_types import NodeTypes
from .operator.node._core import NodeOperator
from .operator.node._keyframes import NodesKeyframeManager


class _ExistingNodeAccessor:
    """共有 ModifierManager を使って既存ノードを包む。"""

    __slots__ = (
        "__dict__",
        "_modifier_manager",
    )

    def __init__(self, modifier_manager: ModifierManager):
        self._modifier_manager = modifier_manager

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    def __call__(
        self,
        node: str | om.MObject,
        auto_add_attr: bool = False,
    ) -> NodeOperator:
        """既存ノードを型に対応した NodeOperator として取得する。

        Args:
            node: ノード名または MObject。
            auto_add_attr: 不足している extra attribute を追加するか。
                既存ノードを変更しないよう、既定値は False。

        Returns:
            ノード型に対応した NodeOperator。
        """
        return ExistingNode(
            node,
            modifier_manager=self._modifier_manager,
            auto_add_attr=auto_add_attr,
        )

    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        existing_node_accessor: Callable[..., NodeOperator] = getattr(
            ExistingNode,
            node_name,
        )

        def _wrap(
            node: str | om.MObject,
            auto_add_attr: bool = False,
        ) -> NodeOperator:
            return existing_node_accessor(
                node,
                modifier_manager=self._modifier_manager,
                auto_add_attr=auto_add_attr,
            )

        _wrap.__name__ = node_name
        _wrap.__qualname__ = f"{type(self).__name__}.{node_name}"
        _wrap.__doc__ = existing_node_accessor.__doc__
        return_type = existing_node_accessor.__annotations__.get("return")
        if return_type is not None:
            _wrap.__annotations__["return"] = return_type
        setattr(self, node_name, _wrap)
        return _wrap


class Nodes:
    """ノードの作成・取得と共通の ModifierManager をまとめる入口。"""

    __slots__ = (
        "_modifier_manager",
        "_create",
        "_existing",
        "_keyframes",
        "_types",
    )

    def __init__(
        self,
        modifier_manager: ModifierManager | None = None,
        *,
        typing_maya_version: Literal["2025", "2026", "2027"] | None = None,
    ):
        """ノード操作の入口を初期化する。

        Args:
            modifier_manager: 操作を予約する先。省略時は新規作成する。
            typing_maya_version: IDE の補完対象にする Maya バージョン。
                実行時のノード定義は現在の Maya に従う。
        """
        # 型補完だけに使う引数。実行時の定義は読み込んだ Maya の版に従う。
        del typing_maya_version
        if modifier_manager is None:
            modifier_manager = ModifierManager()

        self._modifier_manager = modifier_manager
        self._create = NodeCreator(modifier_manager=modifier_manager)
        self._existing = _ExistingNodeAccessor(
            modifier_manager=modifier_manager,
        )
        self._keyframes = NodesKeyframeManager(modifier_manager)
        self._types = NodeTypes()

    @property
    def modifier_manager(self) -> ModifierManager:
        """作成・取得したノードと共有する ModifierManager。"""
        return self._modifier_manager

    @property
    def create(self) -> NodeCreator:
        """作成を予約するノード型別アクセサ。"""
        return self._create

    @property
    def existing(self) -> _ExistingNodeAccessor:
        """既存ノードを包むノード型別アクセサ。"""
        return self._existing

    @property
    def keyframes(self) -> NodesKeyframeManager:
        """複数ノードのキーフレーム操作を予約する入口。"""
        return self._keyframes

    @property
    def types(self) -> NodeTypes:
        """ノード型の参照・解決を行うアクセサ。"""
        return self._types
