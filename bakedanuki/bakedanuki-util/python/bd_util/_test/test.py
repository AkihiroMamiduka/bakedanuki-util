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
    joint_1_a = nodes.create.joint(name="jnt_1_a", parent=transform_1_a)

    transform_0_a_loc = nodes.create.locator(
        name="trsf_0_locatorShape", parent=transform_0_a
    )
    transform_0_a_loc.localScale.set(2, 3, 4)

    _, locator_0_a = nodes.create.with_transform.locator(
        name="loc_0_a", parent=transform_0_a
    )
    locator_0_a.localPosition.set(1, 2, 3)
    locator_0_a.localScale.set(5, 6, 7)

    joint_0_b = nodes.create.joint(name="jnt_0_b", parent=transform_0_a)
    _ = nodes.create.transform(name="trsf_1_b", parent=joint_0_b)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    ancestors = joint_1_a.ancestors(
        until=joint_0_a,
    )
    if not ancestors:
        return

    for dag in ancestors:
        logger.debug(dag)
        logger.debug(f"type(child): {type(dag)}")
