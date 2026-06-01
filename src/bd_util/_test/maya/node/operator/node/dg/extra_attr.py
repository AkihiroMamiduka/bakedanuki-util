# coding: utf-8
"""
extra=True の Attr を使った自動 addAttr() 機能のテスト・デモ
"""

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.operator.node.dag.transform._core import Transform
from .......maya.node.operator.attr.at.double import DoubleAttr
from .......maya.node.operator.attr.dt.matrix import DataMatrixAttr

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class MyTransform(Transform):

    # extra=True: インスタンス生成時に自動 addAttr() される
    myWeight = DoubleAttr(extra=True)
    mw = myWeight

    myMatrix = DataMatrixAttr(extra=True)
    mm = myMatrix

    # extra=False (デフォルト): 通常のアトリビュート定義 (addAttr() されない)
    # ※ この例では transform の既存アトリビュートにアクセスする用途


def main():
    extra_attrs_class_access()
    auto_add_attr_on_init()
    no_auto_add_attr()
    manual_add_attr_via_plug()


def extra_attrs_class_access():
    test_str.title("1. extra=True: class access properties")
    logger.debug(
        "{}: {}".format(
            "MyTransform._extra_attributes",
            MyTransform._extra_attributes,
        )
    )
    for attr in MyTransform._extra_attributes:
        logger.debug("  attr: {}, extra: {}".format(attr, attr.extra))


def auto_add_attr_on_init():
    test_str.title("2. extra=True: instance access properties")

    node_name = "test_auto_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    # ノードを作成
    cmds.createNode("transform", name=node_name, skipSelect=True)

    # Node インスタンス生成 → extra=True の Attr が自動 addAttr() される
    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    node = MyTransform(dg_mod, dag_mod=dag_mod, name=node_name)

    logger.debug(
        "node.myWeight plug exists: {}".format(
            cmds.objExists(f"{node_name}.myWeight")
        )
    )
    logger.debug(
        "node.myMatrix plug exists: {}".format(
            cmds.objExists(f"{node_name}.myMatrix")
        )
    )

    # Plug 経由でアクセス
    logger.debug(
        "{}: {}".format(
            "node.myWeight.plug",
            node.myWeight.plug,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.myMatrix.plug",
            node.myMatrix.plug,
        )
    )


def no_auto_add_attr():
    test_str.title(
        "3. extra=True: auto_add_attr=False prevents auto addAttr()"
    )

    node_name = "test_no_auto_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)

    # auto_add_attr=False → addAttr() されない
    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    MyTransform(dg_mod, dag_mod=dag_mod, name=node_name, auto_add_attr=False)

    logger.debug(
        "node.myWeight plug exists (should be False): {}".format(
            cmds.objExists(f"{node_name}.myWeight")
        )
    )


def manual_add_attr_via_plug():
    test_str.title("4. extra=True: manual addAttr() via Plug")

    node_name = "test_manual_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)

    # auto_add_attr=False でインスタンス化
    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    node = MyTransform(
        dg_mod, dag_mod=dag_mod, name=node_name, auto_add_attr=False
    )

    # Plug 経由で任意タイミングに addAttr()
    logger.debug(
        "node.myWeight plug exists before add_attr(): {}".format(
            cmds.objExists(f"{node_name}.myWeight")
        )
    )
    node.myWeight.add_attr()
    logger.debug(
        "node.myWeight plug exists after manual add_attr(): {}".format(
            cmds.objExists(f"{node_name}.myWeight")
        )
    )

    logger.debug(
        "node.myMatrix plug exists before add_attr(): {}".format(
            cmds.objExists(f"{node_name}.myMatrix")
        )
    )
    node.myMatrix.add_attr()
    logger.debug(
        "node.myMatrix plug exists after manual add_attr(): {}".format(
            cmds.objExists(f"{node_name}.myMatrix")
        )
    )
