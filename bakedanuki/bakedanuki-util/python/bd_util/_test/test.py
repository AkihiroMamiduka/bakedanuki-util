# coding:utf-8
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    joints: list[bdu.node_types.Joint] = []
    for i in range(10):
        joints.append(nodes.create.joint(name=f"j_{i}"))

    for j in joints:
        j.t.set(0, 1, 2)
        j.r.set(3, 4, 5)
        j.s.set(6, 7, 8)
        j.v.set(False)
        j.side.set(2)
        j.type.set(j.type.OTHER)
        j.otherType.set("test")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
