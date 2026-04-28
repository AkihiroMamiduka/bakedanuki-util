# coding: utf-8
from ....... import logger as u_logger
from .......maya.node.operator.node.dg.add_double_linear import AddDoubleLinear

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    get_set()
    get_set_short_name()


def get_set():
    logger.debug("================================")
    node = AddDoubleLinear.create("test")
    logger.debug(f"node: {node}")

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.input1.get()",
            node.input1.get(),
        )
    )
    logger.debug("--set")
    node.input1.set(100.0)
    logger.debug(
        "{}: {}".format(
            "node.input1.get()",
            node.input1.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.input2.get()",
            node.input2.get(),
        )
    )
    logger.debug("--set")
    node.input2.set(200.0)
    logger.debug(
        "{}: {}".format(
            "node.input2.get()",
            node.input2.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.output.get()",
            node.output.get(),
        )
    )


def get_set_short_name():
    logger.debug("================================")
    node = AddDoubleLinear.create("test")
    logger.debug(f"node: {node}")

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.i1.get()",
            node.i1.get(),
        )
    )
    logger.debug("--set")
    node.i1.set(100.0)
    logger.debug(
        "{}: {}".format(
            "node.i1.get()",
            node.i1.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.i2.get()",
            node.i2.get(),
        )
    )
    logger.debug("--set")
    node.i2.set(200.0)
    logger.debug(
        "{}: {}".format(
            "node.i2.get()",
            node.i2.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.o.get()",
            node.o.get(),
        )
    )
