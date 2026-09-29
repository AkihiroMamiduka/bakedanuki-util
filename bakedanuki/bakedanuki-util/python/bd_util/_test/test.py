# coding:utf-8
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    src = nodes.create.joint(name="src")
    dst = nodes.create.joint(name="dst")

    src.t.set(0, 1, 2)
    src.r.set(3, 4, 5)
    src.s.set(6, 7, 8)
    src.v.set(False)
    src.side.set(2)
    src.type.set(src.type.OTHER)
    src.otherType.set("test")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    snap = bdu.AttrSnapshot.capture([src], include_hidden=True)
    path = r"D:/snap_shot.json"
    snap.save(path)
    load_snap = bdu.AttrSnapshot.load(path)
    load_snap.restore(nodes.modifier_manager, targets=[dst])

    nodes.modifier_manager.do_it_dg()
