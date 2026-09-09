# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    trsf = nodes.create.transform(name="test")
    for i in range(300):
        trsf.tx.keyframe.set(i, frame=i)
        trsf.rx.keyframe.set(i * 2, frame=i)
        trsf.sx.keyframe.set(i * i, frame=i)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
