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
    short_name_class_access()
    short_name_instance_access()
    connect_next_index()
    refresh_next_index()


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


def short_name_class_access():
    logger.debug("================================")

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "WtAddMatrix.matrixSum.long_name : {}".format(
            WtAddMatrix.matrixSum.long_name
        )
    )
    logger.debug(
        "WtAddMatrix.matrixSum.short_name: {}".format(
            WtAddMatrix.matrixSum.short_name
        )
    )
    logger.debug(f"id(WtAddMatrix.matrixSum): {id(WtAddMatrix.matrixSum)}")
    logger.debug(f"id(WtAddMatrix.o)        : {id(WtAddMatrix.o)}")

    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.matrixSum is WtAddMatrix.o",
            WtAddMatrix.matrixSum is WtAddMatrix.o,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "WtAddMatrix.matrixSum.long_name : {}".format(
            WtAddMatrix.wtMatrix.long_name
        )
    )
    logger.debug(
        "WtAddMatrix.matrixSum.short_name: {}".format(
            WtAddMatrix.wtMatrix.short_name
        )
    )
    logger.debug(f"id(WtAddMatrix.wtMatrix): {id(WtAddMatrix.wtMatrix)}")
    logger.debug(f"id(WtAddMatrix.i)       : {id(WtAddMatrix.i)}")

    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix is WtAddMatrix.i",
            WtAddMatrix.wtMatrix is WtAddMatrix.i,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "WtAddMatrix.wtMatrix.matrixIn.long_name : {}".format(
            WtAddMatrix.wtMatrix.matrixIn.long_name
        )
    )
    logger.debug(
        "WtAddMatrix.wtMatrix.matrixIn.short_name: {}".format(
            WtAddMatrix.wtMatrix.matrixIn.short_name
        )
    )
    logger.debug(
        "id(WtAddMatrix.wtMatrix.matrixIn): {}".format(
            id(WtAddMatrix.wtMatrix.matrixIn)
        )
    )
    logger.debug("id(WtAddMatrix.i.m)     : {}".format(id(WtAddMatrix.i.m)))

    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.matrixIn is WtAddMatrix.i.m",
            WtAddMatrix.wtMatrix.matrixIn is WtAddMatrix.i.m,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "WtAddMatrix.wtMatrix.weightIn.long_name : {}".format(
            WtAddMatrix.wtMatrix.weightIn.long_name
        )
    )
    logger.debug(
        "WtAddMatrix.wtMatrix.weightIn.short_name: {}".format(
            WtAddMatrix.wtMatrix.weightIn.short_name
        )
    )
    logger.debug(
        "id(WtAddMatrix.wtMatrix.weightIn): {}".format(
            id(WtAddMatrix.wtMatrix.weightIn)
        )
    )
    logger.debug("id(WtAddMatrix.i.w)     : {}".format(id(WtAddMatrix.i.w)))

    logger.debug(
        "{}: {}".format(
            "WtAddMatrix.wtMatrix.weightIn is WtAddMatrix.i.w",
            WtAddMatrix.wtMatrix.weightIn is WtAddMatrix.i.w,
        )
    )


def short_name_instance_access():
    logger.debug("================================")
    node = WtAddMatrix.create("test")

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "node.matrixSum.long_name : {}".format(node.matrixSum.long_name)
    )
    logger.debug(
        "node.matrixSum.short_name: {}".format(node.matrixSum.short_name)
    )
    logger.debug(f"id(node.matrixSum): {id(node.matrixSum)}")
    logger.debug(f"id(node.o)        : {id(node.o)}")

    logger.debug(
        "{}: {}".format(
            "node.matrixSum is node.o",
            node.matrixSum is node.o,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "node.matrixSum.long_name : {}".format(node.wtMatrix.long_name)
    )
    logger.debug(
        "node.matrixSum.short_name: {}".format(node.wtMatrix.short_name)
    )
    logger.debug(f"id(node.wtMatrix): {id(node.wtMatrix)}")
    logger.debug(f"id(node.i)       : {id(node.i)}")

    logger.debug(
        "{}: {}".format(
            "node.wtMatrix is node.i",
            node.wtMatrix is node.i,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "node.wtMatrix.matrixIn.long_name : {}".format(
            node.wtMatrix.matrixIn.long_name
        )
    )
    logger.debug(
        "node.wtMatrix.matrixIn.short_name: {}".format(
            node.wtMatrix.matrixIn.short_name
        )
    )
    logger.debug(
        "id(node.wtMatrix.matrixIn): {}".format(id(node.wtMatrix.matrixIn))
    )
    logger.debug("id(node.i.m)     : {}".format(id(node.i.m)))

    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.matrixIn is node.i.m",
            node.wtMatrix.matrixIn is node.i.m,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "node.wtMatrix.weightIn.long_name : {}".format(
            node.wtMatrix.weightIn.long_name
        )
    )
    logger.debug(
        "node.wtMatrix.weightIn.short_name: {}".format(
            node.wtMatrix.weightIn.short_name
        )
    )
    logger.debug(
        "id(node.wtMatrix.weightIn): {}".format(id(node.wtMatrix.weightIn))
    )
    logger.debug("id(node.i.w)     : {}".format(id(node.i.w)))

    logger.debug(
        "{}: {}".format(
            "node.wtMatrix.weightIn is node.i.w",
            node.wtMatrix.weightIn is node.i.w,
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.o.get()",
            node.o.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.i[0].m.get()",
            node.i[0].m.get(),
        )
    )
    node.i[0].m.set(node.o.value)
    logger.debug(
        "{}: {}".format(
            "node.i[0].m.get()",
            node.i[0].m.get(),
        )
    )
    node.i[0].m.value = [
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
    node.i[0].m.set(node.o.value)
    logger.debug(
        "{}: {}".format(
            "node.i[0].m.get()",
            node.i[0].m.get(),
        )
    )

    logger.debug("-----------------------------------------------------------")
    logger.debug(
        "{}: {}".format(
            "node.i[0].w.get()",
            node.i[0].w.get(),
        )
    )
    node.i[0].w.set(100)
    logger.debug(
        "{}: {}".format(
            "node.i[0].w.get()",
            node.i[0].w.get(),
        )
    )
    node.i[0].w.value = 200
    logger.debug(
        "{}: {}".format(
            "node.i[0].w.get()",
            node.i[0].w.get(),
        )
    )


def connect_next_index():
    logger.debug("================================")
    dst_node = WtAddMatrix.create("dst")
    for i in range(5):
        src_node = WtAddMatrix.create(f"src_{i}")
        dst_node.wtMatrix.matrixIn.connect_next_index(src_node.matrixSum)
        logger.debug(
            "src_{}.matrixSum > dst_node.wtMatrix[{}].matrixIn".format(i, i)
        )


def refresh_next_index():
    logger.debug("================================")
    dst_node = WtAddMatrix.create("dst2")
    plug = dst_node.wtMatrix.matrixIn

    # connect_next_index でキャッシュを使いながら 3 件接続
    for i in range(3):
        src_node = WtAddMatrix.create(f"src2_{i}")
        plug.connect_next_index(src_node.matrixSum)
        logger.debug(
            "src2_{}.matrixSum > dst2.wtMatrix[{}].matrixIn".format(i, i)
        )

    # このメソッド以外 (cmds.connectAttr 相当) でコネクションが追加された場合を想定し
    # refresh_next_index() でキャッシュをリセットする
    plug.refresh_next_index()
    logger.debug("refresh_next_index() called")

    # リセット後は再スキャンして正しいインデックスから接続される
    extra_src = WtAddMatrix.create("src2_extra")
    plug.connect_next_index(extra_src.matrixSum)
    logger.debug(
        "src2_extra.matrixSum > dst2.wtMatrix[3].matrixIn (after refresh)"
    )
