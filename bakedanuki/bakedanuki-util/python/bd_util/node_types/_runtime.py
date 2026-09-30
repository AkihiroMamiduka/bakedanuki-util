# coding: utf-8
"""公開ノード型の遅延参照を共有する。"""

from ..maya.node.node_types import NodeTypes
from ..maya.node.operator.node._core import NodeOperator

_node_types = NodeTypes()


def __getattr__(class_name: str) -> type[NodeOperator]:
    """クラス名から現在の Maya に対応する実クラスを返す。"""
    return getattr(_node_types, class_name)


def __dir__() -> list[str]:
    """現在の Maya で参照できるノードクラス名を返す。"""
    return sorted(_node_types.available_class_names())
