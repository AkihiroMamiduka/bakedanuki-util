# coding: utf-8

# maya
from maya import cmds

TYPE_DAG_NODE = "dagNode"
TYPE_TRANSFORM_NODE = "transform"
TYPE_SHAPE_NODE = "shape"


def is_type_core(node_type: str, inheritance_type: str) -> bool:
    inheritance = cmds.nodeType(node_type, inherited=True, isTypeName=True)
    return inheritance_type in inheritance


# dag_node
def is_dag_node_type(node_type: str) -> bool:
    return is_type_core(node_type, TYPE_DAG_NODE)


#   transform
def is_transform_type(node_type: str) -> bool:
    return is_type_core(node_type, TYPE_TRANSFORM_NODE)


#   shape
def is_shape_type(node_type: str) -> bool:
    return is_type_core(node_type, TYPE_SHAPE_NODE)


# dg_node
def is_dg_node_type(node_type: str) -> bool:
    return not is_type_core(node_type, TYPE_DAG_NODE)
