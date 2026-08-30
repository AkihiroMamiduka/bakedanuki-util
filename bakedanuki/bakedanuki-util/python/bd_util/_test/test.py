# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    src_space = nodes.create.transform(name="src_space")
    src, _ = nodes.create.with_transform.locator(name="src", parent=src_space)

    dst_space = nodes.create.transform(name="dst_space")
    dst, _ = nodes.create.with_transform.locator(name="dst", parent=dst_space)

    src_space.rotateOrder.set_keyable()
    src.rotateOrder.set_keyable()
    dst_space.rotateOrder.set_keyable()
    dst.rotateOrder.set_keyable()

    src_space.rotateOrder.set(random.randint(0, 5))
    src.rotateOrder.set(random.randint(0, 5))
    dst_space.rotateOrder.set(random.randint(0, 5))
    dst.rotateOrder.set(random.randint(0, 5))

    src_space.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    src.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    dst_space.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    q_src_space = src_space.m.get().quat
    q_src = src.m.get().quat
    inv_q_src_space = dst_space.m.get().quat.inverse()

    q = q_src * q_src_space * inv_q_src_space

    dst.r.set(q.to_euler(rotate_order=dst.rotateOrder.get()))

    nodes.modifier_manager.do_it_dg()
