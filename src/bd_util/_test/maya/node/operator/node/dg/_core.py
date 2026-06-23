# coding: utf-8

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.modifier import ModifierManager
from .......maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    attribute_access_get()


def attribute_access_get():
    test_str.title("Testing attribute access")
    modifier_manager = ModifierManager()
    dg = WtAddMatrix.create(modifier_manager, name="test")

    test_str.separator()
    logger.debug("caching: {}".format(dg.caching.get()))
    logger.debug("cch    : {}".format(dg.cch.get()))
    logger.debug("--set")
    dg.caching.set(True)
    modifier_manager.do_it_dg()
    logger.debug("caching: {}".format(dg.caching.get()))
    logger.debug("cch    : {}".format(dg.cch.get()))

    test_str.separator()
    logger.debug("frozen: {}".format(dg.frozen.get()))
    logger.debug("fzn   : {}".format(dg.fzn.get()))
    logger.debug("--set")
    dg.frozen.set(True)
    modifier_manager.do_it_dg()
    logger.debug("frozen: {}".format(dg.frozen.get()))
    logger.debug("fzn   : {}".format(dg.fzn.get()))

    test_str.separator()
    logger.debug(
        "isHistoricallyInteresting: {}".format(
            dg.isHistoricallyInteresting.get()
        )
    )
    logger.debug("ihi                      : {}".format(dg.ihi.get()))
    dg.isHistoricallyInteresting.set(1)
    modifier_manager.do_it_dg()
    logger.debug(
        "isHistoricallyInteresting: {}".format(
            dg.isHistoricallyInteresting.get()
        )
    )
    logger.debug("ihi                      : {}".format(dg.ihi.get()))

    test_str.separator()
    logger.debug("enum_name: {}".format(dg.nodeState.enum_full_name()))
    logger.debug("nodeState: {}".format(dg.nodeState.get()))
    logger.debug("nds      : {}".format(dg.nds.get()))
    logger.debug("name: {}".format(dg.nodeState.name_by_index(dg.nds.get())))
    logger.debug("--set")
    dg.nodeState.set(1)
    modifier_manager.do_it_dg()
    logger.debug("nodeState: {}".format(dg.nodeState.get()))
    logger.debug("nds      : {}".format(dg.nds.get()))
    logger.debug("name: {}".format(dg.nodeState.name_by_index(dg.nds.get())))

    test_str.separator()
    logger.debug("binMembership: {}".format(dg.binMembership.get()))
    logger.debug("bnm          : {}".format(dg.bnm.get()))
    logger.debug("--set")
    dg.binMembership.set("test")
    modifier_manager.do_it_dg()
    logger.debug("binMembership: {}".format(dg.binMembership.get()))
    logger.debug("bnm          : {}".format(dg.bnm.get()))
