# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    trsf = nodes.create.transform(name="test")
    values = [i for i in range(10000)]

    trsf.tx.keyframe.set_keys(values, frames=values)
    trsf.ty.keyframe.set_keys(values, frames=values)
    trsf.tz.keyframe.set_keys(values, frames=values)

    trsf.rx.keyframe.set_keys(values, frames=values)
    trsf.ry.keyframe.set_keys(values, frames=values)
    trsf.rz.keyframe.set_keys(values, frames=values)

    trsf.sx.keyframe.set_keys(values, frames=values)
    trsf.sy.keyframe.set_keys(values, frames=values)
    trsf.sz.keyframe.set_keys(values, frames=values)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
