# coding: utf-8

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.modifier import ModifierManager
from .......maya.node.operator.node.dg.add_double_linear import AddDoubleLinear

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    attribute_access()
    plug_access()
    get_set()
    get_set_short_name()


# class_access
def attribute_access():
    test_str.title("attribute_access")
    logger.debug(
        "{}: {}".format(
            "AddDoubleLinear",
            AddDoubleLinear,
        )
    )
    logger.debug(
        "{}: {}".format(
            "AddDoubleLinear.input1",
            AddDoubleLinear.input1,
        )
    )
    logger.debug(
        "{}: {}".format(
            "AddDoubleLinear.input1.default_value",
            AddDoubleLinear.input1.default_value,
        )
    )


# instance_access
def plug_access():
    test_str.title("plug_access")
    modifier_manager = ModifierManager()

    node = AddDoubleLinear.create(modifier_manager, name="test")
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node",
            node,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input1",
            node.input1,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input1.plug",
            node.input1.plug,
        )
    )


def get_set():
    test_str.title("get_set")
    modifier_manager = ModifierManager()
    node = AddDoubleLinear.create(modifier_manager, name="test")
    logger.debug(f"node: {node}")

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input1.get()",
            node.input1.get(),
        )
    )
    logger.debug("--set")
    node.input1.set(10.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input1.get()",
            node.input1.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input2.get()",
            node.input2.get(),
        )
    )
    logger.debug("--set")
    node.input2.set(20.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input2.get()",
            node.input2.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output.get()",
            node.output.get(),
        )
    )


def get_set_short_name():
    test_str.title("get_set_short_name")
    modifier_manager = ModifierManager()
    node = AddDoubleLinear.create(modifier_manager, name="test")
    logger.debug(f"node: {node}")

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i1.get()",
            node.i1.get(),
        )
    )
    logger.debug("--set")
    node.i1.set(100.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i1.get()",
            node.i1.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i2.get()",
            node.i2.get(),
        )
    )
    logger.debug("--set")
    node.i2.set(200.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i2.get()",
            node.i2.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.o.get()",
            node.o.get(),
        )
    )
