# coding: utf-8

# maya
from maya import cmds

# self
from bd_util.maya.node.type import (
    is_dag_node_type,
    is_dg_node_type,
    is_shape_type,
    is_transform_type,
)


# get
def get_all_node_types():
    return cmds.allNodeTypes()


# specific_types
#       core
def get_specific_types_core(is_func):
    return [t for t in get_all_node_types() if is_func(t)]


#       dag_node
def get_dag_node_types():
    return get_specific_types_core(is_dag_node_type)


#           transform
def get_transform_types():
    return get_specific_types_core(is_transform_type)


#           shape
def get_shape_types():
    return get_specific_types_core(is_shape_type)


#       dg_node
def get_dg_node_types():
    return get_specific_types_core(is_dg_node_type)
