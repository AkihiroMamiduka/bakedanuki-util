# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    src, _ = nodes.create.with_transform.locator(name="src")
    dst, _ = nodes.create.with_transform.locator(name="dst")

    src.t.set(random.random(), random.random(), random.random())
    src.r.set(
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
        random.randint(-360, 360) + random.random(),
    )
    src.s.set(random.random(), random.random(), random.random())

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    m = bdu.TransformMatrix(
        translate=src.t.get(),
        rotate=src.r.get(),
        rotate_order="xyz",
        scale=src.s.get(),
    )
    dst.opm.set(m)

    nodes.modifier_manager.do_it_dg()
