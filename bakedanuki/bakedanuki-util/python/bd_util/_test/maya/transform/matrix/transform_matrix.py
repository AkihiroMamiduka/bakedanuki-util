# coding: utf-8

# maya
from maya import cmds

# self
from .....maya.transform.matrix.transform_matrix import TransformMatrix
from .....maya.node.nodes import Nodes


def main():
    test_transform_matrix()


def test_transform_matrix():
    nodes = Nodes()
    src = nodes.create.transform(name="src")
    dst_parent = nodes.create.transform(name="dst_parent")
    dst = nodes.create.transform(name="dst")

    # transform をセット
    #   src
    src.translate.set(10.0, 20.0, 30.0)
    src.rotate.set(-90, -60, -30)
    src.scale.set(4, 3, 2)
    #   dst_parent
    dst_parent.translate.set(3.0, 4.0, 5.0)
    dst_parent.rotate.set(30, 60, 90)
    dst_parent.scale.set(2, 3, 4)

    # mod
    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    # parent (DagNodeOperator に parent メソッドをまだ実装できていないので、cmds で parent する)
    cmds.parent(dst.name, dst_parent.name)

    # local 値を取得
    src_wm = TransformMatrix(src.wm[0].plug)
    dst_parent_wim = TransformMatrix(dst_parent.wim[0].plug)

    local_m = src_wm * dst_parent_wim

    # dst にセット
    dst.translate.set(local_m.translate)
    dst.rotate.set(local_m.rotate)
    dst.scale.set(local_m.scale)

    # mod
    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
