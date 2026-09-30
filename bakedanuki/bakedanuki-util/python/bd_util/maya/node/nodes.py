# coding: utf-8
from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Literal, Self

from maya.api import OpenMaya as om

from ._creation_name import resolve_namespace
from .creator import NodeCreator
from .existing_node import ExistingNode
from .modifier import ModifierManager
from .operator.node._core import NodeOperator
from .operator.node._keyframes import NodesKeyframeManager


class _ExistingNodeAccessor:
    """共有 `ModifierManager` を使って既存ノードを包む。"""

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
        """既存ノードを型に対応した `NodeOperator` として取得する。

        Args:
            node: ノード名または `MObject`。
            auto_add_attr: 不足している extra attribute を追加するか。
                既存ノードを変更しないよう、既定値は False。

        Returns:
            ノード型に対応した `NodeOperator`。
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


def _node_for_namespace_move(
    value: object,
    modifier_manager: ModifierManager,
) -> NodeOperator:
    """ノード指定を現在の操作履歴へ結び付ける。"""
    if isinstance(value, NodeOperator):
        if value.modifier_manager is not modifier_manager:
            raise ValueError(
                "NodeOperator must use this Nodes modifier_manager."
            )
        node = value
    else:
        if isinstance(value, str):
            if not value or any(char in value for char in ".*?[]"):
                raise ValueError("Expected one node name.")
            selection = om.MSelectionList()
            try:
                selection.add(value)
            except RuntimeError as exc:
                raise ValueError(f"Node not found: {value}") from exc
            if selection.length() != 1:
                raise ValueError("Expected one node name.")
            m_obj = selection.getDependNode(0)
        elif isinstance(value, om.MObject):
            m_obj = value
        else:
            raise TypeError("Expected a NodeOperator, MObject or node name.")

        handle = om.MObjectHandle(m_obj)
        if not handle.isAlive() or not handle.isValid():
            raise ValueError("An MObject target must be an existing node.")
        if not m_obj.hasFn(om.MFn.kDependencyNode):
            raise TypeError("Expected a dependency node.")
        node = NodeOperator(modifier_manager, m_obj=m_obj, auto_add_attr=False)

    if not om.MObjectHandle(node.m_obj).isAlive():
        raise ValueError("The node is no longer available.")
    if not node._name_for_edit():  # pyright: ignore[reportPrivateUsage]
        raise ValueError(
            "A pending node must have a name to move its namespace."
        )
    return node


class Nodes:
    """ノードの作成・取得と共通の `ModifierManager` をまとめる入口。"""

    __slots__ = (
        "_modifier_manager",
        "_create",
        "_existing",
        "_keyframes",
    )

    def __init__(
        self,
        modifier_manager: ModifierManager | None = None,
        *,
        namespace: str | None = None,
        typing_maya_version: Literal["2025", "2026", "2027"] | None = None,
    ):
        """ノード操作の入口を初期化する。

        Args:
            modifier_manager: 操作を予約する先。省略時は新規作成する。
            namespace: 作成時の既定 namespace。`None` は既定値なし。
                相対指定はこの呼び出し時のカレント namespace を基準にする。
            typing_maya_version: IDE の補完対象にする Maya バージョン。
                実行時のノード定義は現在の Maya に従う。
        """
        # `typing_maya_version` は型補完だけに使う。実行時は読み込んだ Maya の版に従う。
        del typing_maya_version
        if modifier_manager is None:
            modifier_manager = ModifierManager()

        self._modifier_manager = modifier_manager
        self._create = NodeCreator(
            modifier_manager=modifier_manager, namespace=namespace
        )
        self._existing = _ExistingNodeAccessor(
            modifier_manager=modifier_manager,
        )
        self._keyframes = NodesKeyframeManager(modifier_manager)

    @property
    def modifier_manager(self) -> ModifierManager:
        """作成・取得したノードと共有する `ModifierManager`。"""
        return self._modifier_manager

    @property
    def namespace(self) -> str | None:
        """以後のノード作成に使う絶対 namespace。`None` は既定値なし。"""
        return self._create.namespace

    def set_namespace(self, namespace: str | None) -> Self:
        """以後の `nodes.create` だけに適用する既定 namespace を設定する。

        予約済みノードと既存ノードは変更しない。namespace 自体はノード作成の
        `do_it_dg()` / `do_it_dag()` 時に必要なら作成する。

        Args:
            namespace: 先頭の `:` はルート起点。空文字列と `":"` はルート。
                `None` は既定値を解除する。

        Returns:
            この `Nodes`。

        Raises:
            TypeError: `namespace` が文字列でも `None` でもない場合。
            ValueError: `namespace` が不正な場合。
        """
        self._create.set_namespace(namespace)
        return self

    def move_to_namespace(
        self,
        targets: Iterable[NodeOperator | om.MObject | str],
        *,
        namespace: str,
    ) -> None:
        """複数ノードの namespace 変更を共有 DG バッチに予約する。

        `namespace` は予約時のカレント namespace を基準に解決する。移動先が
        未作成なら `do_it_dg()` 時に作成し、同じ履歴で Undo / Redo する。
        作成待ちの DAG ノードは `do_it_dag()` 後に `do_it_dg()` を実行する。
        移動先で名前が衝突すると Maya がローカル名に連番を付ける。

        Args:
            targets: 対象ノードの iterable。作成待ちノードは、この `Nodes` と
                同じ `ModifierManager` を持つ、名前付きの `NodeOperator` で指定する。
            namespace: 移動先。先頭の `:` はルート起点。`""` と `":"` はルート。

        Raises:
            TypeError: `targets` が iterable でないか、対象または `namespace` の型が不正な場合。
            ValueError: 対象が空・重複・不正、別の `ModifierManager` に属する、
                または `namespace` が不正な場合。
        """
        resolved_namespace = resolve_namespace(namespace)
        if isinstance(targets, (str, NodeOperator, om.MObject)):
            raise TypeError("targets must be an iterable of nodes.")
        try:
            values = tuple(targets)
        except TypeError as exc:
            raise TypeError("targets must be an iterable of nodes.") from exc
        if not values:
            raise ValueError("targets must contain at least one node.")

        nodes: list[NodeOperator] = []
        seen: set[om.MObjectHandle] = set()
        for value in values:
            node = _node_for_namespace_move(value, self._modifier_manager)
            handle = om.MObjectHandle(node.m_obj)
            if handle in seen:
                raise ValueError("Duplicate namespace move node.")
            seen.add(handle)
            nodes.append(node)

        for node in nodes:
            node.move_to_namespace(resolved_namespace)

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
