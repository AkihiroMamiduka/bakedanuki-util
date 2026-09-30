# coding:utf-8
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes(namespace=":test")

    top = nodes.create.transform(name="top", namespace=":top_ns")

    parent = top
    for num in range(10):
        for i in range(num):
            if i % 2:
                parent = nodes.create.transform(
                    name=f"trsf_{num}_{i}",
                    parent=parent,
                )
            else:
                parent = nodes.create.joint(
                    name=f"j_{num}_{i}",
                    parent=parent,
                )

    nodes.modifier_manager.do_it_dag()

    joints = top.descendants(filter_type=bdu.node_types.Joint)
    for j in joints:
        j.t.set(0, 1, 2)
        j.r.set(3, 4, 5)
        j.s.set(6, 7, 8)
        j.v.set(False)
        j.side.set(2)
        j.type.set(j.type.OTHER)
        j.otherType.set("test")

    nodes.move_to_namespace(joints, namespace=":jjj")

    nodes.modifier_manager.do_it_dg()
