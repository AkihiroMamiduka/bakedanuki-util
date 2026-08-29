# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    src = nodes.create.joint(name="src")
    dst = nodes.create.joint(name="dst")

    src.tx.connect(dst.tx)
    src.ty.connect(dst.ty)
    src.tz.connect(dst.tz)
    src.r.connect(dst.r)
    src.s.connect(dst.s)
    src.v.connect(dst.v)
    src.jo.connect(dst.jo)
    src.ra.connect(dst.ra)

    src.tx.set_locked()
    src.ty.set_locked()
    src.tz.set_locked()
    src.r.set_locked()
    dst.s.set_locked()
    src.v.set_hidden()
    src.v.set_locked()
    src.jo.set_keyable()
    src.jo.set_locked()
    src.ra.set_channel_box()
    dst.jo.set_keyable()
    dst.jo.set_locked()
    dst.ra.set_channel_box()

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
