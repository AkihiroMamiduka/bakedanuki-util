# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    j_root = nodes.create.joint(name="root")
    j_0 = nodes.create.joint(name="j_0", parent=j_root)
    j_1 = nodes.create.joint(name="j_1", parent=j_0)
    j_2 = nodes.create.joint(name="j_2", parent=j_1)
    j_3 = nodes.create.joint(name="j_3", parent=j_2)
    j_4 = nodes.create.joint(name="j_4", parent=j_3)

    loc, _ = nodes.create.with_transform.locator(name="loc")

    loc.t.set(0, 10, 0)

    j_root.set_translate(
        abs(random.random()), abs(random.random()), abs(random.random())
    )
    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    j_0.set_translate(
        abs(random.random()), abs(random.random()), abs(random.random())
    )
    nodes.modifier_manager.do_it_dg()

    j_1.set_translate(
        abs(random.random()), abs(random.random()), abs(random.random())
    )
    nodes.modifier_manager.do_it_dg()

    j_2.set_translate(
        abs(random.random()), abs(random.random()), abs(random.random())
    )
    nodes.modifier_manager.do_it_dg()

    j_3.set_translate(
        abs(random.random()), abs(random.random()), abs(random.random())
    )
    nodes.modifier_manager.do_it_dg()

    j_4.set_translate(
        abs(random.random()), abs(random.random()), abs(random.random())
    )
    nodes.modifier_manager.do_it_dg()

    joints = [j_0, j_1, j_2, j_3, j_4]
    up_axis = (0, 1, 0)
    for j in joints:
        j.aim_child_to_joint_orient(
            up_axis=up_axis,
            up_target=loc,
        )
        j.jo.set_keyable()
        j.ra.set_keyable()
        nodes.modifier_manager.do_it_dg()
