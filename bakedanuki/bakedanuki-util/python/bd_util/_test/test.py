# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    src_aim, _ = nodes.create.with_transform.locator(name="src_aim")
    src_up, _ = nodes.create.with_transform.locator(name="src_up")
    dst_space = nodes.create.transform(name="dst_space")
    dst = nodes.create.joint(name="dst", parent=dst_space)
    dst_child = nodes.create.joint(name="dst_child", parent=dst)

    loc, _ = nodes.create.with_transform.locator(name="loc")

    dst.jo.set_keyable()
    dst.ra.set_keyable()

    src_aim.t.set(random.random(), random.random(), random.random())
    src_up.t.set(random.random(), random.random(), random.random())

    dst_space.t.set(random.random(), random.random(), random.random())
    dst_space.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    loc.set_translate(1, 1, 1, space="world")
    dst_child.set_translate(1, 1, 1, space="world")
    dst_child.set_rotate(0, 0, 0, space="world")

    nodes.modifier_manager.do_it_dg()

    dst.aim_to_joint_orient(
        src_aim,
        aim_axis=(0, 0, 1),
        up_target=src_up,
        up_axis=(1, 0, 0),
        compensate_children=True,
        compensate_child_translate=True,
    )

    nodes.modifier_manager.do_it_dg()
