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

    targets = [src, dst]
    snap = bdu.AttrSnapshot.capture(targets, include_hidden=True)

    src.t.set(0, 0, 0)
    src.r.set(0, 0, 0)
    src.s.set(1, 1, 1)
    src.v.set(True)
    src.side.set(0)
    src.type.set(src.type.NONE)
    src.otherType.set("jaw")

    dst.t.set(0, 0, 0)
    dst.r.set(0, 0, 0)
    dst.s.set(1, 1, 1)
    dst.v.set(True)
    dst.side.set(0)
    dst.type.set(src.type.NONE)
    dst.otherType.set("jaw")

    extract_snap = snap.extract(nodes=[dst])
    extract_snap.restore(nodes.modifier_manager)

    nodes.modifier_manager.do_it_dg()
