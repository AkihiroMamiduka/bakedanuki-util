# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from .creater import NodeCreater
from .modifier import ModifierManager
from .operator.node._core import NodeOperator
from .operator.node.dag.transform._core import Transform
from .operator.node.dag.transform.joint import Joint


class BDNode:
    def __new__(
        cls,
        node: str | om.MObject,
        modifier_manager: ModifierManager | None = None,
        auto_add_attr: bool = False,
    ) -> NodeOperator:
        modifier_manager = modifier_manager or ModifierManager()
        m_obj = _to_m_object(node)
        node_type = _get_node_type(m_obj)
        node_cls = _get_node_cls(node_type, modifier_manager)
        return node_cls(
            modifier_manager,
            m_obj=m_obj,
            auto_add_attr=auto_add_attr,
        )


def _to_m_object(node: str | om.MObject) -> om.MObject:
    if isinstance(node, om.MObject):
        return node
    if isinstance(node, str):
        selection = om.MSelectionList()
        try:
            selection.add(node)
        except RuntimeError as e:
            raise ValueError(f"Node not found: {node}") from e
        return selection.getDependNode(0)
    raise TypeError(f"node must be str or MObject: {type(node)}")


def _get_node_type(m_obj: om.MObject) -> str:
    return om.MFnDependencyNode(m_obj).typeName


def _get_node_cls(
    node_type: str,
    modifier_manager: ModifierManager,
) -> type[NodeOperator]:
    dag_node_cls_map: dict[str, type[NodeOperator]] = {
        "transform": Transform,
        "joint": Joint,
    }
    if node_type in dag_node_cls_map:
        return dag_node_cls_map[node_type]

    try:
        return NodeCreater(modifier_manager=modifier_manager).node_class(
            node_type
        )
    except AttributeError as e:
        raise AttributeError(f"Unsupported node type: {node_type}") from e
