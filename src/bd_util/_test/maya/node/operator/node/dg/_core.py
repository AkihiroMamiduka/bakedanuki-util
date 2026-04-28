# coding: utf-8

# self
from ....... import logger as u_logger
from .......maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def title(title: str):
    text = "-" * 8
    text += f" {title} "
    text = text.ljust(50, "-")
    logger.debug(text)


def sub_separator():
    logger.debug("-" * 2)


def main():
    attribute_access_get()


def attribute_access_get():
    title("Testing attribute access")
    dg = WtAddMatrix.create("test")

    sub_separator()
    logger.debug("caching: {}".format(dg.caching.get()))
    logger.debug("cch    : {}".format(dg.cch.get()))
    logger.debug("--set")
    dg.caching.set(True)
    logger.debug("caching: {}".format(dg.caching.get()))
    logger.debug("cch    : {}".format(dg.cch.get()))

    sub_separator()
    logger.debug("frozen: {}".format(dg.frozen.get()))
    logger.debug("fzn   : {}".format(dg.fzn.get()))
    logger.debug("--set")
    dg.frozen.set(True)
    logger.debug("frozen: {}".format(dg.frozen.get()))
    logger.debug("fzn   : {}".format(dg.fzn.get()))

    sub_separator()
    logger.debug(
        "isHistoricallyInteresting: {}".format(
            dg.isHistoricallyInteresting.get()
        )
    )
    logger.debug("ihi                      : {}".format(dg.ihi.get()))
    dg.isHistoricallyInteresting.set(1)
    logger.debug(
        "isHistoricallyInteresting: {}".format(
            dg.isHistoricallyInteresting.get()
        )
    )
    logger.debug("ihi                      : {}".format(dg.ihi.get()))

    sub_separator()
    logger.debug("enum_name: {}".format(dg.nodeState.enum_name))
    logger.debug("nodeState: {}".format(dg.nodeState.get()))
    logger.debug("nds      : {}".format(dg.nds.get()))
    logger.debug("enum_name: {}".format(dg.nodeState.enum_name[dg.nds.get()]))
    logger.debug("--set")
    dg.nodeState.set(1)
    logger.debug("nodeState: {}".format(dg.nodeState.get()))
    logger.debug("nds      : {}".format(dg.nds.get()))
    logger.debug("enum_name: {}".format(dg.nodeState.enum_name[dg.nds.get()]))

    sub_separator()
    logger.debug("binMembership: {}".format(dg.binMembership.get()))
    logger.debug("bnm          : {}".format(dg.bnm.get()))
    logger.debug("--set")
    dg.binMembership.set("test")
    logger.debug("binMembership: {}".format(dg.binMembership.get()))
    logger.debug("bnm          : {}".format(dg.bnm.get()))
