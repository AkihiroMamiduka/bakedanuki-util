# coding: utf-8

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ....... import logger as u_logger
from ...... import str as test_str
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
    test_str.title("class_instance_access")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    test_str.separator()
    # node.is_instance = "test"  # error
    logger.debug(
        "{}: {}".format(
            "node.is_instance",
            node.is_instance,
        )
    )

    test_str.separator()
    # node.wtMatrix = "test"  # error
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix",
            node.wtMatrix,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0]",
            node.wtMatrix[0],
        )
    )

    test_str.separator()
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
            "node.wtMatrix[0].matrixIn.plug",
            node.wtMatrix[0].matrixIn.plug,
        )
    )

    test_str.separator()
    # node.wtMatrix.matrixIn = "test"  # error
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn",
            node.wtMatrix[0].weightIn,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn.name",
            node.wtMatrix[0].weightIn.name,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn.plug",
            node.wtMatrix[0].weightIn.plug,
        )
    )


def class_access():
    test_str.title("class_access")
    logger.debug(f"WtAddMatrix: {WtAddMatrix}")

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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
    test_str.title("create")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    logger.debug(f"node: {node}")
    logger.debug(f"type(node): {type(node)}")
    logger.debug(f"node.name: {node.name}")
    logger.debug(f"node.NODE_TYPE: {node.NODE_TYPE}")

    logger.debug(f"node.exists(): {node.exists()}")


def instance_access():
    test_str.title("instance_access")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    logger.debug(f"node: {node}")
    logger.debug(f"type(node): {type(node)}")

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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
    test_str.title("to_string")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    logger.debug(f"str(node): {str(node)}")


def get_set():
    test_str.title("get_set")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    logger.debug(f"node: {node}")

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.matrixSum.get()",
            node.matrixSum.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.get()",
            node.wtMatrix[0].matrixIn.get(),
        )
    )
    node.wtMatrix[0].matrixIn.set_direct(node.matrixSum.value)
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].matrixIn.get()",
            node.wtMatrix[0].matrixIn.get(),
        )
    )
    node.wtMatrix[0].matrixIn.value_direct = [
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

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.wtMatrix[0].weightIn.get()",
            node.wtMatrix[0].weightIn.get(),
        )
    )
    node.wtMatrix[0].weightIn.set_direct(100)
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
    test_str.title("connect_disconnect")
    dg_mod = om.MDGModifier()

    node_name_0 = "test_0"
    if cmds.objExists(node_name_0):
        cmds.delete(node_name_0)
    cmds.createNode("wtAddMatrix", name=node_name_0, skipSelect=True)
    node_0 = WtAddMatrix(dg_mod, name=node_name_0)

    node_name_1 = "test_1"
    if cmds.objExists(node_name_1):
        cmds.delete(node_name_1)
    cmds.createNode("wtAddMatrix", name=node_name_1, skipSelect=True)
    node_1 = WtAddMatrix(dg_mod, name=node_name_1)
    dg_mod.doIt()

    test_str.separator()
    node_0.matrixSum > node_1.wtMatrix[0].matrixIn
    node_0.matrixSum | node_1.wtMatrix[0].matrixIn

    f"{node_0}.matrixSum" > node_1.wtMatrix[0].matrixIn
    f"{node_0}.matrixSum" | node_1.wtMatrix[0].matrixIn

    [str(node_0), "matrixSum"] > node_1.wtMatrix[0].matrixIn
    [str(node_0), "matrixSum"] | node_1.wtMatrix[0].matrixIn

    node_0.matrixSum > f"{node_1}.wtMatrix[0].matrixIn"
    node_0.matrixSum | f"{node_1}.wtMatrix[0].matrixIn"

    node_0.matrixSum > [str(node_1), "wtMatrix[0]", "matrixIn"]
    node_0.matrixSum | [str(node_1), "wtMatrix[0]", "matrixIn"]


def plug_cache():
    test_str.title("plug_cache")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    test_str.separator()
    plug_0 = node.matrixSum
    logger.debug(f"id(plug_0): {id(plug_0)}")
    plug_1 = node.matrixSum
    logger.debug(f"id(plug_1): {id(plug_1)}")

    logger.debug(f"plug_0 is plug_1: {plug_0 is plug_1}")


def short_name_class_access():
    test_str.title("short_name_class_access")

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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
    test_str.title("short_name_instance_access")

    node_name = "test"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    node = WtAddMatrix(dg_mod, name=node_name)
    dg_mod.doIt()

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
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

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.o.get()",
            node.o.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i[0].m.get()",
            node.i[0].m.get(),
        )
    )
    node.i[0].m.set_direct(node.o.value)
    logger.debug(
        "{}: {}".format(
            "node.i[0].m.get()",
            node.i[0].m.get(),
        )
    )
    node.i[0].m.value_direct = [
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
    node.i[0].m.set_direct(node.o.value)
    logger.debug(
        "{}: {}".format(
            "node.i[0].m.get()",
            node.i[0].m.get(),
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i[0].w.get()",
            node.i[0].w.get(),
        )
    )
    node.i[0].w.set_direct(100)
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
    test_str.title("connect_next_index")

    dg_mod = om.MDGModifier()

    node_name = "dst"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dst_node = WtAddMatrix(dg_mod, name=node_name)
    for i in range(5):
        node_name = f"src_{i}"
        if cmds.objExists(node_name):
            cmds.delete(node_name)
        cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
        src_node = WtAddMatrix(dg_mod, name=node_name)
        src_node.matrixSum > dst_node.wtMatrix[next].matrixIn
        logger.debug(
            "src_{}.matrixSum > dst_node.wtMatrix[{}].matrixIn".format(i, i)
        )
    dg_mod.doIt()


def refresh_next_index():
    test_str.title("refresh_next_index")

    node_name = "dst"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    dg_mod = om.MDGModifier()
    dst_node = WtAddMatrix(dg_mod, name=node_name)

    # next 指定でキャッシュを使いながら 3 件接続
    for i in range(3):
        node_name = f"src_{i}"
        if cmds.objExists(node_name):
            cmds.delete(node_name)
        cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
        src_node = WtAddMatrix(dg_mod, name=node_name)
        src_node.matrixSum > dst_node.wtMatrix[next].matrixIn
        logger.debug(
            "src_{}.matrixSum > dst.wtMatrix[{}].matrixIn".format(i, i)
        )
    dg_mod.doIt()

    # このメソッド以外 (cmds.connectAttr 相当) でコネクションが追加された場合を想定し
    # refresh_next_index() でキャッシュをリセットする
    dst_node.wtMatrix.refresh_next_index()
    logger.debug("refresh_next_index() called")

    # リセット後は再スキャンして正しいインデックスから接続される
    node_name = "src_extra"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("wtAddMatrix", name=node_name, skipSelect=True)
    extra_src = WtAddMatrix(dg_mod, name=node_name)
    extra_src.matrixSum > dst_node.wtMatrix[next].matrixIn
    logger.debug(
        "src_extra.matrixSum > dst.wtMatrix[3].matrixIn (after refresh)"
    )
    dg_mod.doIt()
