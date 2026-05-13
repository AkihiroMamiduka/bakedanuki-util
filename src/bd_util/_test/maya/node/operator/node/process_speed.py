# conding: utf-8

# maya
from maya import cmds
from pymel import core as pm

# self
from ...... import logger as u_logger
from ..... import str as test_str
from ......_dev.timer import timer
from ......maya.node.operator.node.dg.plus_minus_average import (
    PlusMinusAverage,
)
from ......maya import scene as u_scene

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    u_scene.new_scene()
    # create
    test_str.title("処理速度計測(create)")
    create_cmds()
    create_pm()
    create_node_operator()
    # create_connect
    test_str.title("処理速度計測(create_connect)")
    create_connect_cmds()
    create_connect_pm()
    create_connect_node_operator()


# create
@timer
def create_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    for _ in range(100000):
        cmds.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_pm():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    for _ in range(100000):
        pm.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    for _ in range(100000):
        PlusMinusAverage.create()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


# create_connect
@timer
def create_connect_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    parent_node = None
    for _ in range(100000):
        # ノードを作成
        node = cmds.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        if parent_node is not None:
            cmds.connectAttr(
                f"{parent_node}.output3Dx",
                f"{node}.input3D[0].input3Dx",
            )
        # parent を置き換え
        parent_node = node

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_pm():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    parent_node = None
    for _ in range(100000):
        # ノードを作成
        node = pm.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        if parent_node is not None:
            parent_node.output3Dx >> node.input3D[0].input3Dx
        # parent を置き換え
        parent_node = node

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    parent_node = None
    for _ in range(100000):
        # ノードを作成
        node = PlusMinusAverage.create()
        # ノードを接続
        if parent_node is not None:
            parent_node.output3Dx > node.input3D[0].input3Dx
        # parent を置き換え
        parent_node = node

    # 新規シーンを開く
    cmds.file(new=True, force=True)
