# coding: utf-8

from ....maya.node.creator._core import NodeCreator


def create_node():
    # creator を作成
    creator = NodeCreator()

    # transform ノードを作成
    trsf = creator.transform(name="sample_trsf")
    trsf.translate.set(1, 2, 3)
    trsf.rotateX.set(30)
    trsf.rotateY.set(60)
    trsf.rotateZ.set(90)

    # joint ノードを作成
    joint = creator.joint(name="sample_joint")
    joint.jointOrient.set(10, 20, 30)

    creator.modifier_manager.do_it_dag()
    creator.modifier_manager.do_it_dg()
