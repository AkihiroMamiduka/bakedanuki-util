# coding: utf-8

from ....maya.node.creator._core import NodeCreator


def create_node():
    """transform と joint の作成・値設定を予約して DAG、DG の順に実行する。"""
    creator = NodeCreator()

    # 2 つのノード作成と属性の初期値を同じ `ModifierManager` に積む。
    trsf = creator.transform(name="sample_trsf")
    trsf.translate.set(1, 2, 3)
    trsf.rotateX.set(30)
    trsf.rotateY.set(60)
    trsf.rotateZ.set(90)

    joint = creator.joint(name="sample_joint")
    joint.jointOrient.set(10, 20, 30)

    # ノード作成を確定してから属性値を適用する。
    creator.modifier_manager.do_it_dag()
    creator.modifier_manager.do_it_dg()
