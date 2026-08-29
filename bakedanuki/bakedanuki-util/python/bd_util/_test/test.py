# coding:utf-8
import random

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    before = nodes.create.joint(name="before")
    after = nodes.create.joint(name="after")

    axis = (
        random.randint(-360, 360),
        random.randint(-360, 360),
        random.randint(-360, 360),
    )
    before.r.set(axis)
    after.r.set(axis)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    after.remap_axes_to_rotate(x="-y", y="+z")

    nodes.modifier_manager.do_it_dg()
