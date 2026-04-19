# coding: utf-8
from ....... import logger as u_logger
from .......maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    class_instance_access()
    class_access()
    create()
    instance_access()
    to_string()
    get_set()
    connect_disconnect()
    plug_cache()


def class_instance_access():
    logger.debug("===========================================================")
    node = WtAddMatrix("test")

    logger.debug("-----------------------------------------------------------")
    # node.is_instance = "test"  # error
    logger.debug(
        "{}: {}".format(
            "node.is_instance",
            node.is_instance,
        )
    )

    logger.debug("-----------------------------------------------------------")
    # node.wtMatrix = "test"  # error
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix",
            node.wtMatrix,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.matrixIn.name",
            node.wtMatrix,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.matrixIn.plug",
            node.wtMatrix,
        )
    )

    logger.debug("-----------------------------------------------------------")
    # node.wtMatrix.matrixIn = "test"  # error
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.matrixIn",
            node.wtMatrix.matrixIn,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.matrixIn.name",
            node.wtMatrix.matrixIn.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.matrixIn.plug",
            node.wtMatrix.matrixIn.plug,
        )
    )


def class_access():
    logger.debug("===========================================================")
    logger.debug(f"WtAddMatrix: {WtAddMatrix}")

    logger.debug("-----------------------------------------------------------")
    # WtAddMatrix.matrixSum = "test"  # error
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.matrixSum",
            WtAddMatrix.matrixSum,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.matrixSum.name",
            WtAddMatrix.matrixSum.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.matrixSum.type",
            WtAddMatrix.matrixSum.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.matrixSum.attr_path",
            WtAddMatrix.matrixSum._attr_path,
        )
    )

    logger.debug("-----------------------------------------------------------")
    # WtAddMatrix.wtMatrix = "test"  # error
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix",
            WtAddMatrix.wtMatrix,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.name",
            WtAddMatrix.wtMatrix.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.type",
            WtAddMatrix.wtMatrix.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.attr_path",
            WtAddMatrix.wtMatrix._attr_path,
        )
    )

    logger.debug("-----------------------------------------------------------")
    # WtAddMatrix.wtMatrix.matrixIn = "test"  # error
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.matrixIn",
            WtAddMatrix.wtMatrix.matrixIn,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.matrixIn.name",
            WtAddMatrix.wtMatrix.matrixIn.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.matrixIn.type",
            WtAddMatrix.wtMatrix.matrixIn.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.matrixIn.attr_path",
            WtAddMatrix.wtMatrix.matrixIn._attr_path,
        )
    )

    logger.debug("-----------------------------------------------------------")
    # WtAddMatrix.wtMatrix.weightIn = "test"  # error
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.weightIn",
            WtAddMatrix.wtMatrix.weightIn,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.weightIn.name",
            WtAddMatrix.wtMatrix.weightIn.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.weightIn.type",
            WtAddMatrix.wtMatrix.weightIn.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.weightIn.attr_path",
            WtAddMatrix.wtMatrix.weightIn._attr_path,
        )
    )


def create():
    node = WtAddMatrix.create()
    logger.debug("================================")
    logger.debug(f"node: {node}")
    logger.debug(f"type(node): {type(node)}")
    logger.debug(f"node.name: {node.name}")
    logger.debug(f"node.NODE_TYPE: {node.NODE_TYPE}")

    logger.debug(f"node.exists(): {node.exists()}")


def instance_access():
    logger.debug("================================")
    node = WtAddMatrix.create("test")
    logger.debug(f"node: {node}")
    logger.debug(f"type(node): {type(node)}")

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.matrixSum",
            node.matrixSum,
        )
    )
    logger.debug(
        "{}: {}".format(
            "type(node.matrixSum)",
            type(node.matrixSum),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.matrixSum.name",
            node.matrixSum.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.matrixSum.type",
            node.matrixSum.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.matrixSum._attr_path",
            node.matrixSum._attr_path,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.matrixSum.plug",
            node.matrixSum.plug,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix",
            node.wtMatrix,
        )
    )
    logger.debug(
        "{}: {}".format(
            "type(node.wtMatrix)",
            type(node.wtMatrix),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.name",
            node.wtMatrix.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.type",
            node.wtMatrix.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix._attr_path",
            node.wtMatrix._attr_path,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.plug",
            node.wtMatrix.plug,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0]",
            node.wtMatrix[0],
        )
    )
    logger.debug(
        "{}: {}".format(
            "type(node.wtMatrix[0])",
            type(node.wtMatrix[0]),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].name",
            node.wtMatrix[0].name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].type",
            node.wtMatrix[0].type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0]._attr_path",
            node.wtMatrix[0]._attr_path,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].plug",
            node.wtMatrix[0].plug,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn",
            node.wtMatrix[0].matrixIn,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.name",
            node.wtMatrix[0].matrixIn.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.type",
            node.wtMatrix[0].matrixIn.type,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn._attr_path",
            node.wtMatrix[0].matrixIn._attr_path,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.plug",
            node.wtMatrix[0].matrixIn.plug,
        )
    )


def to_string():
    logger.debug("================================")
    node = WtAddMatrix.create()
    logger.debug(f"str(node): {str(node)}")


def get_set():
    logger.debug("================================")
    node = WtAddMatrix.create("test")
    logger.debug(f"node: {node}")

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.matrixSum.get()",
            node.matrixSum.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.get()",
            node.wtMatrix[0].matrixIn.get(),
        )
    )
    node.wtMatrix[0].matrixIn.set(node.matrixSum.value)
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.get()",
            node.wtMatrix[0].matrixIn.get(),
        )
    )
    node.wtMatrix[0].matrixIn.value = [
        10,
        0,
        0,
        0,
        0,
        20,
        0,
        0,
        0,
        0,
        30,
        0,
        0,
        0,
        0,
        1,
    ]
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.get()",
            node.wtMatrix[0].matrixIn.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn.get()",
            node.wtMatrix[0].weightIn.get(),
        )
    )
    node.wtMatrix[0].weightIn.set(100)
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn.get()",
            node.wtMatrix[0].weightIn.get(),
        )
    )
    node.wtMatrix[0].weightIn.value = 200
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn.get()",
            node.wtMatrix[0].weightIn.get(),
        )
    )


def connect_disconnect():
    logger.debug("================================")
    node_0 = WtAddMatrix.create("test_0")
    node_1 = WtAddMatrix.create("test_1")

    logger.debug("-----------------------------------------------------------")
    node_0.matrixSum > node_1.wtMatrix[0].matrixIn
    node_0.matrixSum | node_1.wtMatrix[0].matrixIn

    f"{node_0}.matrixSum" > node_1.wtMatrix[0].matrixIn
    f"{node_0}.matrixSum" | node_1.wtMatrix[0].matrixIn

    [node_0, "matrixSum"] > node_1.wtMatrix[0].matrixIn
    [node_0, "matrixSum"] | node_1.wtMatrix[0].matrixIn

    node_0.matrixSum > f"{node_1}.wtMatrix[0].matrixIn"
    node_0.matrixSum | f"{node_1}.wtMatrix[0].matrixIn"

    node_0.matrixSum > [node_1, "wtMatrix[0]", "matrixIn"]
    node_0.matrixSum | [node_1, "wtMatrix[0]", "matrixIn"]


def plug_cache():
    logger.debug("================================")
    node = WtAddMatrix("test")

    logger.debug("-----------------------------------------------------------")
    plug_0 = node.matrixSum
    logger.debug(f"id(plug_0): {id(plug_0)}")
    plug_1 = node.matrixSum
    logger.debug(f"id(plug_1): {id(plug_1)}")

    logger.debug(f"plug_0 is plug_1: {plug_0 is plug_1}")
