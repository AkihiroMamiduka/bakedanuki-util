# coding: utf-8

# maya
from maya import cmds

TYPE_DAG_NODE = "dagNode"
TYPE_TRANSFORM_NODE = "transform"
TYPE_SHAPE_NODE = "shape"


def is_type_core(node_type: str, inheritance_type: str) -> bool:
    """ノード型が指定した Maya の型を継承するか。

    Args:
        node_type: 調べる Maya ノード型名。
        inheritance_type: 継承先として調べる型名。
    """
    inheritance = cmds.nodeType(node_type, inherited=True, isTypeName=True)
    return inheritance_type in inheritance


def is_dag_node_type(node_type: str) -> bool:
    """指定した型が DAG ノードか。"""
    return is_type_core(node_type, TYPE_DAG_NODE)


def is_transform_type(node_type: str) -> bool:
    """指定した型が Transform ノードか。"""
    return is_type_core(node_type, TYPE_TRANSFORM_NODE)


def is_shape_type(node_type: str) -> bool:
    """指定した型が Shape ノードか。"""
    return is_type_core(node_type, TYPE_SHAPE_NODE)


def is_dg_node_type(node_type: str) -> bool:
    """指定した型が DAG に属さない DG ノードか。"""
    return not is_type_core(node_type, TYPE_DAG_NODE)
