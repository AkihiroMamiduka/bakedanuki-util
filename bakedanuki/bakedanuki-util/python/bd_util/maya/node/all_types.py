# coding: utf-8
from collections.abc import Callable

# maya
from maya import cmds

# self
from .type import (
    is_dag_node_type,
    is_dg_node_type,
    is_shape_type,
    is_transform_type,
)


def get_all_node_types() -> list[str]:
    """現在の Maya が認識する全ノード型名を返す。"""
    return cmds.allNodeTypes()


def get_specific_types_core(is_func: Callable[[str], bool]) -> list[str]:
    """判定関数に合うノード型名を返す。

    Args:
        is_func: 各ノード型名を受け取り、対象なら True を返す関数。

    Returns:
        条件に合うノード型名のリスト。
    """
    return [t for t in get_all_node_types() if is_func(t)]


def get_dag_node_types() -> list[str]:
    """DAG ノード型名を返す。"""
    return get_specific_types_core(is_dag_node_type)


def get_transform_types() -> list[str]:
    """Transform ノード型名を返す。"""
    return get_specific_types_core(is_transform_type)


def get_shape_types() -> list[str]:
    """Shape ノード型名を返す。"""
    return get_specific_types_core(is_shape_type)


def get_dg_node_types() -> list[str]:
    """DAG に属さない DG ノード型名を返す。"""
    return get_specific_types_core(is_dg_node_type)
