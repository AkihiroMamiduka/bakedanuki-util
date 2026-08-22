# coding:utf-8

from maya import cmds

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    transform_0 = nodes.create.transform(name="trsf_0")
    joint_0 = nodes.create.joint(name="jnt_0", parent=transform_0)
    transform_1 = nodes.create.transform(name="trsf_1", parent=joint_0)
    joint_1 = nodes.create.joint(name="jnt_1", parent=transform_1)

    logger.debug(f"joint_1.ancestors(): {joint_1.ancestors()}")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    logger.debug(f"joint_1.ancestors(): {joint_1.ancestors()}")
    for i, parent in enumerate(joint_1.ancestors()):
        logger.debug(parent)
        logger.debug(f"type(child): {type(parent)}")
        parent.translate.set(1 * i, 2 * i, 3 * i)

    nodes.modifier_manager.do_it_dg()
