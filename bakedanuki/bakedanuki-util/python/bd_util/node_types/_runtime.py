# coding: utf-8
"""公開ノード型の遅延参照を共有する。"""

from ..maya.node.node_types import NodeTypes
from ..maya.node.operator.node._core import NodeOperator

_node_types = NodeTypes()


def __getattr__(class_name: str) -> type[NodeOperator]:
    """クラス名から現在の Maya に対応する実クラスを返す。"""
    return getattr(_node_types, class_name)


def resolve(node_type: object) -> type[NodeOperator]:
    """Maya ノード型名から対応する `NodeOperator` クラスを返す。

    Args:
        node_type: Maya ノード型名。文字列以外は `TypeError`。

    Raises:
        TypeError: `node_type` が文字列でない場合。
        AttributeError: 対応するノード型がない場合。
    """
    return _node_types.resolve(node_type)


def available_class_names() -> tuple[str, ...]:
    """現在の Maya で参照できるノードクラス名を返す。"""
    return _node_types.available_class_names()


def __dir__() -> list[str]:
    """現在の Maya で参照できるノードクラス名を返す。"""
    return list(available_class_names())
