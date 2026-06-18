# conding: utf-8

# maya
from maya import cmds
from maya.api import OpenMaya as om

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
    #   one
    test_str.title("処理速度計測(create-one)")
    create_one_cmds()
    create_one_pm()
    create_one_om()
    create_one_node_operator()
    #   many
    test_str.title("処理速度計測(create-many)")
    create_many_cmds()
    create_many_pm()
    create_many_om_individual()
    create_many_om_all_together()
    create_many_node_operator()
    # create_connect
    test_str.title("処理速度計測(create_connect)")
    create_connect_cmds()
    create_connect_pm()
    create_connect_om_individual()
    create_connect_om_all_together()
    create_connect_node_operator()


# create
@timer
def create_one_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_one_pm():
    from pymel import core as pm

    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_one_om():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    mod.createNode("plusMinusAverage")
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_one_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    PlusMinusAverage.create(mod)
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_cmds():
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
def create_many_pm():
    from pymel import core as pm

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
def create_many_om_individual():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    for _ in range(100000):
        mod.createNode("plusMinusAverage")
        mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_om_all_together():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    for _ in range(100000):
        mod.createNode("plusMinusAverage")
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    for _ in range(100000):
        PlusMinusAverage.create(mod)
    mod.doIt()

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
    from pymel import core as pm

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
def create_connect_om_individual():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    parent_m_obj = None
    for _ in range(100000):
        # ノードを作成
        m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        if parent_m_obj is not None:
            src = om.MPlug(
                om.MObject(parent_m_obj),
                om.MFnDependencyNode(parent_m_obj).attribute("output3Dx"),
            )
            array_plug = om.MPlug(
                m_obj, om.MFnDependencyNode(m_obj).attribute("input3D")
            )
            dst = array_plug.elementByLogicalIndex(0).child(0)
            mod.connect(src, dst)
        mod.doIt()
        # parent を置き換え
        parent_m_obj = m_obj

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_om_all_together():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    parent_m_obj = None
    for _ in range(100000):
        # ノードを作成
        m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        if parent_m_obj is not None:
            src = om.MPlug(
                om.MObject(parent_m_obj),
                om.MFnDependencyNode(parent_m_obj).attribute("output3Dx"),
            )
            array_plug = om.MPlug(
                m_obj, om.MFnDependencyNode(m_obj).attribute("input3D")
            )
            dst = array_plug.elementByLogicalIndex(0).child(0)
            mod.connect(src, dst)
        # parent を置き換え
        parent_m_obj = m_obj
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    parent_node = None
    for _ in range(100000):
        # ノードを作成
        node = PlusMinusAverage.create(mod)
        # ノードを接続
        if parent_node is not None:
            parent_node.output3Dx > node.input3D[0].input3Dx
        # parent を置き換え
        parent_node = node
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)
