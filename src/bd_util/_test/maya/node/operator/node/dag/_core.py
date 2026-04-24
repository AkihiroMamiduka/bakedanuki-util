# coding: utf-8
"""
DAG クラスの long_name プロパティのテスト・デモ
"""
import maya.cmds as cmds

from ....... import logger as u_logger
from .......maya.node.operator.node.dag._core import DAG

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    long_name_root()
    long_name_under_group()


def long_name_root():
    logger.debug("===========================================================")
    logger.debug("--- long_name: ルート直下のノード ---")

    node_name = "test_dag_root"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)
    node = DAG(node_name)

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
    logger.debug("===========================================================")
    logger.debug("--- long_name: グループ配下のノード ---")

    group_name = "test_dag_group"
    child_name = "test_dag_child"

    for n in [child_name, group_name]:
        if cmds.objExists(n):
            cmds.delete(n)

    grp = cmds.createNode("transform", name=group_name, skipSelect=True)
    child = cmds.createNode(
        "transform", name=child_name, parent=grp, skipSelect=True
    )
    node = DAG(child)

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
