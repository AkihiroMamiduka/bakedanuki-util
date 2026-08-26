# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    src_p = nodes.create.transform(name="src_parent")
    src, _ = nodes.create.with_transform.locator(name="src", parent=src_p)

    dst_p = nodes.create.transform(name="dst_parent")
    dst_a, _ = nodes.create.with_transform.locator(name="dst_a", parent=dst_p)
    dst_b, _ = nodes.create.with_transform.locator(name="dst_b", parent=dst_p)

    for node in [src_p, src, dst_p]:
        node.translate.set(1, 2, 3)
        node.translate.set(
            random.random(),
            random.random(),
            random.random(),
        )
        node.rotate.set(
            random.randint(-360, 360),
            random.randint(-360, 360),
            random.randint(-360, 360),
        )
        node.scale.set(
            random.random(),
            random.random(),
            random.random(),
        )

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    # dst_a
    src_wm = src.wm[0].get()
    dst_pim = dst_a.pim[0].get()
    m = src_wm * dst_pim
    dst_a.translate.set(m.translate)
    dst_a.rotate.set(m.rotate)
    dst_a.scale.set(m.scale)
    dst_a.shear.set(m.shear)

    # dst_b
    m = src.get_local_matrix(dst_b)
    dst_b.translate.set(m.translate)
    dst_b.rotate.set(m.rotate)
    dst_b.scale.set(m.scale)
    dst_b.shear.set(m.shear)

    nodes.modifier_manager.do_it_dg()
