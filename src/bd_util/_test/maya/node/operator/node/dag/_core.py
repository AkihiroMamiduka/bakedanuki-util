# coding: utf-8
"""
DAG クラスの long_name プロパティのテスト・デモ
"""
import maya.cmds as cmds

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.operator.node.dag._core import DAG
from .......maya.node.operator.node.dag.transform._core import Transform

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    long_name_root()
    long_name_under_group()


def long_name_root():
    test_str.title("long_name_root")

    node_name = "test_dag_root"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    node = Transform.create(node_name)

    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.long_name",
            node.long_name,
        )
    )
    # 期待値: "|test_dag_root"


def long_name_under_group():
    test_str.title("long_name_under_group")

    group_name = "test_dag_group"
    child_name = "test_dag_child"

    for n in [child_name, group_name]:
        if cmds.objExists(n):
            cmds.delete(n)

    grp = Transform.create(group_name)
    child = Transform.create(child_name)
    cmds.parent(child.name, grp.name)
    node = DAG(child.name)

    logger.debug(
        "{}: {}".format(
            "node.name",
            node.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.long_name",
            node.long_name,
        )
    )
    # 期待値: "|test_dag_group|test_dag_child"
