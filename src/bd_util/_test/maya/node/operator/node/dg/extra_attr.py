# coding: utf-8
"""
extra=True の Attr を使った自動 addAttr() 機能のテスト・デモ
"""

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.operator.node.dag.transform._core import Transform
from .......maya.node.operator.attr.extra.add_attr import AddAttr

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


# class TestEnumAttrOperator(AddAttr.at.enum_attr_operator):
class TestEnumAttrOperator(AddAttr.define.at.enum.attr_operator):
    __slots__ = ()

    ALPHA = 0
    BETA = 1
    GAMMA = 2

    NAME_MAP = {
        ALPHA: "Alpha",
        BETA: "Beta",
        GAMMA: "Gamma",
    }


class TestEnumPlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    ALPHA = 0
    BETA = 1
    GAMMA = 2


class TestEnumField(
    AddAttr.define.at.enum.field[TestEnumAttrOperator, TestEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TestEnumAttrOperator
    PLUG_CLS = TestEnumPlugOperator


class MyTransform(Transform):

    # インスタンス生成時に自動 addAttr() される
    # at
    #   bool
    testBool = AddAttr.at.bool(
        default_value=False,
    )
    tbool = testBool
    #   char
    testChar = AddAttr.at.char(
        default_value=50,
        min_value=-128,
        max_value=127,
        soft_min_value=-128,
        soft_max_value=127,
    )
    tchar = testChar
    #   byte
    testByte = AddAttr.at.byte(
        default_value=50,
        min_value=0,
        max_value=255,
        soft_min_value=0,
        soft_max_value=255,
    )
    tbyte = testByte
    #   short
    testShort = AddAttr.at.short(
        default_value=10000,
        min_value=-32768,
        max_value=32767,
        soft_min_value=-30000,
        soft_max_value=30000,
    )
    tshort = testShort
    #   long
    testLong = AddAttr.at.long(
        default_value=1000000000,
        min_value=-2147483648,
        max_value=2147483647,
        soft_min_value=-2000000000,
        soft_max_value=2000000000,
    )
    tlong = testLong
    #   long_long_int
    testLongLongInt = AddAttr.at.long_long_int(
        default_value=1000000000000000000,
        soft_min_value=-9223372036854775808,
        soft_max_value=9223372036854773760,
    )
    tlongLongInt = testLongLongInt
    #   float
    testFloat = AddAttr.at.float(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tfloat = testFloat
    #   double
    testDouble = AddAttr.at.double(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tdouble = testDouble
    #   double_linear
    testDoubleLinear = AddAttr.at.double_linear(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tdouble_linear = testDoubleLinear
    #   double_angle
    testDoubleAngle = AddAttr.at.double_angle(
        default_value=45,
        min_value=-720,
        max_value=720,
        soft_min_value=-360,
        soft_max_value=360,
    )
    tdouble_angle = testDoubleAngle

    #   enum
    testEnum = TestEnumField()
    tenm = testEnum

    # dt
    #   matrix
    testDataMatrix = AddAttr.dt.matrix()
    tdmatrix = testDataMatrix

    # time
    testTime = AddAttr.at.time(
        default_value=12.345,
    )
    ttime = testTime

    # api.OpenMaya でアトリビュートを作成できないタイプ


def main():
    extra_attrs_class_access()
    extra_attrs_instance_access()
    auto_add_attr_on_init()
    no_auto_add_attr()
    manual_add_attr_via_plug()


def extra_attrs_class_access():
    test_str.title("extra=True: class access properties")
    logger.debug(
        "{}: {}".format(
            "MyTransform._extra_attributes",
            MyTransform._extra_attributes,
        )
    )
    for attr in MyTransform._extra_attributes:
        logger.debug("  attr: {}, extra: {}".format(attr, attr.extra))


def extra_attrs_instance_access():
    test_str.title("extra=True: instance access properties")

    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = MyTransform.create(dg_mod, dag_mod=dag_mod, name="test")
    dag_mod.doIt()
    dg_mod.doIt()
    logger.debug(
        "{}: {}".format(
            "node._extra_attributes",
            node._extra_attributes,
        )
    )
    for attr in node._extra_attributes:
        logger.debug("  attr: {}, extra: {}".format(attr, attr.extra))


def auto_add_attr_on_init():
    test_str.title("extra=True: instance access properties")

    node_name = "test_auto_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    # ノードを作成
    cmds.createNode("transform", name=node_name, skipSelect=True)

    # Node インスタンス生成 → extra=True の Attr が自動 addAttr() される
    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    node = MyTransform(dg_mod, dag_mod=dag_mod, name=node_name)

    logger.debug(
        "node.testDouble plug exists: {}".format(
            cmds.objExists(f"{node_name}.testDouble")
        )
    )
    logger.debug(
        "node.testDataMatrix plug exists: {}".format(
            cmds.objExists(f"{node_name}.testDataMatrix")
        )
    )

    # Plug 経由でアクセス
    logger.debug(
        "{}: {}".format(
            "node.testDouble.plug",
            node.testDouble.plug,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.testDataMatrix.plug",
            node.testDataMatrix.plug,
        )
    )


def no_auto_add_attr():
    test_str.title(
        "3. extra=True: auto_add_attr=False prevents auto addAttr()"
    )

    node_name = "test_no_auto_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)

    # auto_add_attr=False → addAttr() されない
    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    MyTransform(dg_mod, dag_mod=dag_mod, name=node_name, auto_add_attr=False)

    logger.debug(
        "node.testDouble plug exists (should be False): {}".format(
            cmds.objExists(f"{node_name}.testDouble")
        )
    )


def manual_add_attr_via_plug():
    test_str.title("4. extra=True: manual addAttr() via Plug")

    node_name = "test_manual_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)

    # auto_add_attr=False でインスタンス化
    dg_mod = om.MDGModifier()
    dag_mod = om.MDagModifier()
    node = MyTransform(
        dg_mod, dag_mod=dag_mod, name=node_name, auto_add_attr=False
    )

    # Plug 経由で任意タイミングに addAttr()
    #   double
    attr = "testDouble"
    logger.debug(
        "node.{} plug exists before add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    node.testDouble.add_attr()
    logger.debug(
        "node.{} plug exists after manual add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    # matrix
    attr = "testDataMatrix"
    logger.debug(
        "node.{} plug exists before add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    node.testDataMatrix.add_attr()
    logger.debug(
        "node.{} plug exists after manual add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    # enum
    attr = "testEnum"
    logger.debug(
        "node.{} plug exists before add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    node.testEnum.add_attr()
    logger.debug(
        "node.{} plug exists after manual add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
