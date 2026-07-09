# coding: utf-8

from ....maya.node.creater._core import NodeCreater


def create_node():
    # creater を作成
    creater = NodeCreater()

    # transform ノードを作成
    trsf = creater.transform(name="sample_trsf")
    trsf.translate.set(1, 2, 3)
    trsf.rotateX.set(30)
    trsf.rotateY.set(60)
    trsf.rotateZ.set(90)

    # joint ノードを作成
    joint = creater.joint(name="sample_joint")
    joint.jointOrient.set(10, 20, 30)

    creater.modifier_manager.do_it_dag()
    creater.modifier_manager.do_it_dg()
