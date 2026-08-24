# coding:utf-8

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()
    transform_0_a = nodes.create.transform(name="trsf_0")
    joint_0_a = nodes.create.joint(name="jnt_0_a", parent=transform_0_a)
    transform_1_a = nodes.create.transform(name="trsf_1_a", parent=joint_0_a)
    _ = nodes.create.joint(name="jnt_1_a", parent=transform_1_a)

    joint_0_b = nodes.create.joint(name="jnt_0_b", parent=transform_0_a)
    _ = nodes.create.transform(name="trsf_1_b", parent=joint_0_b)

    logger.debug(f"transform_0_a.children(): {transform_0_a.children()}")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    logger.debug(f"transform_0_a.children(): {transform_0_a.children()}")
    for i, child in enumerate(
        transform_0_a.children(filter_type=nodes.types.Joint)
    ):
        if not isinstance(child, nodes.types.Joint):
            continue
        logger.debug(child)
        logger.debug(f"type(child): {type(child)}")
        child.translate.set(1 * i, 2 * i, 3 * i)

    nodes.modifier_manager.do_it_dg()
