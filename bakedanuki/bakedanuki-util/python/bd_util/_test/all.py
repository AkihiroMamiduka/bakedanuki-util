# coding: utf-8

# self
from .. import logger as u_logger
import bd_util._test.maya.node.operator.attr.enum
import bd_util._test.maya.node.operator.attr.keyframe
import bd_util._test.maya.node.operator.node.dag._core
import bd_util._test.maya.node.operator.node.dg._core
import bd_util._test.maya.node.operator.node.dg.attr_init_params
import bd_util._test.maya.node.operator.node.dg.extra_attr
import bd_util._test.maya.node.operator.node.dg.plus_minus_average
import bd_util._test.maya.node.operator.node.dg.str_access
import bd_util._test.maya.node.operator.node.dg.wt_add_matrix
import bd_util._test.maya.node.operator.node._core
import bd_util._test.maya.node.operator.node.bd_node
import bd_util._test.maya.node.operator.node.process_speed

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    bd_util._test.maya.node.operator.attr.enum.main()
    bd_util._test.maya.node.operator.attr.keyframe.main()
    bd_util._test.maya.node.operator.node.dag._core.main()
    bd_util._test.maya.node.operator.node.dg._core.main()
    bd_util._test.maya.node.operator.node.dg.attr_init_params.main()
    bd_util._test.maya.node.operator.node.dg.extra_attr.main()
    bd_util._test.maya.node.operator.node.dg.plus_minus_average.main()
    bd_util._test.maya.node.operator.node.dg.str_access.main()
    bd_util._test.maya.node.operator.node.dg.wt_add_matrix.main()
    bd_util._test.maya.node.operator.node._core.main()
    bd_util._test.maya.node.operator.node.bd_node.main()
    bd_util._test.maya.node.operator.node.process_speed.main()

    logger.debug("---- All tests passed. ----")
