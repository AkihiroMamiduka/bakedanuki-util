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
    # dst, _ = nodes.create.with_transform.locator(name="dst", parent=dst_space)
    dst = nodes.create.joint(name="dst", parent=dst_space)

    dst.jo.set_keyable()
    dst.ra.set_keyable()

    src_space.t.set(random.random(), random.random(), random.random())
    src_space.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    src.t.set(random.random(), random.random(), random.random())
    src.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    dst_space.t.set(random.random(), random.random(), random.random())
    dst_space.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    dst.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )
    dst.jo.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    m = src.wm[0].get()

    dst.set_translate(m.translate, space="world")
    dst.set_rotate_axis(m.rotate, space="world")

    nodes.modifier_manager.do_it_dg()
