# coding: utf-8
"""
DAG クラスの long_name プロパティのテスト・デモ
"""

import maya.cmds as cmds

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.nodes import Nodes
from .......maya.node.modifier import ModifierManager
from .......maya.node.operator.node.dag.transform._core import Transform

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    # long_name_root()
    # long_name_under_group()
    operate_transform()
    get_local_matrix()


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

    nodes = Nodes()

    grp = nodes.create.transform(name=group_name)
    child = nodes.create.transform(name=child_name, parent=grp)

    logger.debug(
        "{}: {}".format(
            "child.name",
            child.name,
        )
    )
    child.name
    logger.debug(
        "{}: {}".format(
            "child.long_name",
            child.long_name,
        )
    )
    # 期待値: "|test_dag_group|test_dag_child"


def operate_transform():
    test_str.title("operate_transform")

    modifier_manager = ModifierManager()

    name = "test_transform"
    node = Transform.create(modifier_manager, name=name)

    node.translate.set(10.0, 20.0, 30.0)
    node.rotate.set(10.0, 20.0, 30.0)
    node.scale.set(10.0, 20.0, 30.0)

    logger.debug(f"translate: {node.translate.get()}")
    logger.debug(f"rotate: {node.rotate.get()}")
    logger.debug(f"scale: {node.scale.get()}")

    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()

    logger.debug("---- after modifier_manager.do_it_dag()/do_it_dg()")
    logger.debug(f"translate: {node.translate.get()}")
    logger.debug(f"rotate: {node.rotate.get()}")
    logger.debug(f"scale: {node.scale.get()}")


def get_local_matrix():
    test_str.title("get_local_matrix")

    nodes = Nodes()

    # 作成
    src_parent = nodes.create.transform(name="src_parent")
    src = nodes.create.transform(name="src", parent=src_parent)
    dst_parent = nodes.create.transform(name="dst_parent")
    dst = nodes.create.transform(name="dst", parent=dst_parent)

    # 値をセット
    #   src_parent
    src_parent.translate.set(10.0, 20.0, 30.0)
    src_parent.rotate.set(30, 60, 90)
    src_parent.scale.set(2, 3, 4)
    #   src
    src.translate.set(10.0, 20.0, 30.0)
    src.rotate.set(-90, -60, -30)
    src.scale.set(0.6, 0.5, 0.4)
    #   dst_parent
    dst_parent.translate.set(-6, -7, -8)
    dst_parent.rotate.set(45, 90, 135)
    dst_parent.scale.set(8, 7, 6)

    # mod
    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    # local 行列を取得
    local_m = src.get_local_matrix(dst)
    dst.translate.set(local_m.translate)
    dst.rotate.set(local_m.rotate)
    dst.scale.set(local_m.scale)
    dst.shear.set(local_m.shear)

    # mod
    nodes.modifier_manager.do_it_dg()
