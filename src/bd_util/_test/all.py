# coding: utf-8

# self
import bd_util._test.maya.node.operator.attr.enum
import bd_util._test.maya.node.operator.node.dag._core
import bd_util._test.maya.node.operator.node.dg._core
import bd_util._test.maya.node.operator.node.dg.add_double_linear
import bd_util._test.maya.node.operator.node.dg.attr_init_params
import bd_util._test.maya.node.operator.node.dg.extra_attr
import bd_util._test.maya.node.operator.node.dg.plus_minus_average
import bd_util._test.maya.node.operator.node.dg.str_access
import bd_util._test.maya.node.operator.node.dg.wt_add_matrix
import bd_util._test.maya.node.operator.node._core


def main():
    bd_util._test.maya.node.operator.attr.enum.main()
    bd_util._test.maya.node.operator.node.dag._core.main()
    bd_util._test.maya.node.operator.node.dg._core.main()
    bd_util._test.maya.node.operator.node.dg.add_double_linear.main()
    bd_util._test.maya.node.operator.node.dg.attr_init_params.main()
    bd_util._test.maya.node.operator.node.dg.extra_attr.main()
    bd_util._test.maya.node.operator.node.dg.plus_minus_average.main()
    bd_util._test.maya.node.operator.node.dg.str_access.main()
    bd_util._test.maya.node.operator.node.dg.wt_add_matrix.main()
    bd_util._test.maya.node.operator.node._core.main()
