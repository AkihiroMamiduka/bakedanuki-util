# coding: utf-8
"""
Attr クラスの __init__ 引数拡張と各プロパティのテスト・デモ

テスト項目:
    1. extra=True のプロパティがクラスアクセスで格納値を返す
    2. extra=True のプロパティがインスタンスアクセスで格納値を返す
    3. add_attr() が defaultValue / minValue / maxValue を正しく addAttr() へ渡す
    4. add_attr() が softMinValue / softMaxValue を正しく addAttr() へ渡す
    5. EnumAttr で enum_name を指定して addAttr() される
    6. readable=False / writable=False が addAttr() へ渡される
    7. DataStringAttr が dataType を使って addAttr() される
    8. extra=False のプロパティが cmds.attributeQuery から値を取得する
"""

# maya
from maya import cmds

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.modifier import ModifierManager
from .......maya.node.operator.node.dag.transform._core import Transform
from .......maya.node.operator.attr.define.std.at.scalar.numeric import (
    double as double_attr,
)
from .......maya.node.operator.attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .......maya.node.operator.attr.define.std.dt.string import (
    DataStringField,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

# ---------------------------------------------------------------------------
# テスト用 Node クラス定義
# ---------------------------------------------------------------------------


class MyEnumPlug(EnumPlugOperator):
    ALPHA = 0
    BETA = 1
    GAMMA = 2


class MyEnumAttr(EnumAttrOperator):
    PLUG_CLS = MyEnumPlug

    ALPHA = 0
    BETA = 1
    GAMMA = 2

    NAME_MAP = {
        ALPHA: "Alpha",
        BETA: "Beta",
        GAMMA: "Gamma",
    }


class MyEnumField(EnumField[MyEnumAttr, MyEnumPlug]):
    ATTR_CLS = MyEnumAttr
    PLUG_CLS = MyEnumPlug


class MyNode(Transform):
    # extra=True: init 引数で各種情報を保持する
    myDouble = double_attr.DoubleField(
        extra=True,
        default_value=1.0,
        min_value=0.0,
        max_value=10.0,
        soft_min_value=0.5,
        soft_max_value=9.5,
    )
    md = myDouble

    myEnum = MyEnumField(
        extra=True,
    )
    me = myEnum

    myReadOnly = double_attr.DoubleField(
        extra=True,
        readable=True,
        writable=False,
    )

    myString = DataStringField(extra=True)
    ms = myString

    # extra=False: Maya ノード既存アトリビュート (translateX) へのアクセス用
    translateX = double_attr.DoubleField()
    tx = translateX


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main():
    extra_true_class_access_properties()
    extra_true_instance_access_properties()
    add_attr_default_min_max()
    add_attr_soft_min_max()
    add_attr_enum_name()
    add_attr_readable_writable()
    add_attr_data_type_string()
    extra_false_query_properties()


# ---------------------------------------------------------------------------
# 1. extra=True: クラスアクセスでプロパティが格納値を返す
# ---------------------------------------------------------------------------


def extra_true_class_access_properties():
    test_str.title("1. extra=True: class access properties")

    attr = MyNode.myDouble
    logger.debug("{}: {}".format("MyNode.myDouble.extra", attr.extra))
    logger.debug(
        "{}: {}".format("MyNode.myDouble.default_value", attr.default_value)
    )
    logger.debug("{}: {}".format("MyNode.myDouble.min_value", attr.min_value))
    logger.debug("{}: {}".format("MyNode.myDouble.max_value", attr.max_value))
    logger.debug(
        "{}: {}".format("MyNode.myDouble.soft_min_value", attr.soft_min_value)
    )
    logger.debug(
        "{}: {}".format("MyNode.myDouble.soft_max_value", attr.soft_max_value)
    )

    enum_attr = MyNode.myEnum
    logger.debug(
        "{}: {}".format("MyNode.myEnum.enum_name", enum_attr.enum_full_name)
    )

    readonly_attr = MyNode.myReadOnly
    logger.debug(
        "{}: {}".format("MyNode.myReadOnly.readable", readonly_attr.readable)
    )
    logger.debug(
        "{}: {}".format("MyNode.myReadOnly.writable", readonly_attr.writable)
    )

    string_attr = MyNode.myString
    logger.debug(
        "{}: {}".format(
            "MyNode.myString.is_data_type", string_attr.is_data_type
        )
    )


# ---------------------------------------------------------------------------
# 2. extra=True: インスタンスアクセスでプロパティが格納値を返す
# ---------------------------------------------------------------------------


def extra_true_instance_access_properties():
    test_str.title("2. extra=True: instance access properties")

    # myDouble
    # extra=True の Attr はノードインスタンス生成後もクラス経由でアクセスし、
    # 格納値をそのまま返すことを確認する
    double_attr = MyNode.myDouble
    logger.debug(
        "{}: {}".format(
            "MyNode.myDouble.default_value (should be 1.0)",
            double_attr.default_value,
        )
    )
    logger.debug(
        "{}: {}".format(
            "MyNode.myDouble.min_value (should be 0.0)",
            double_attr.min_value,
        )
    )
    logger.debug(
        "{}: {}".format(
            "MyNode.myDouble.max_value (should be 10.0)",
            double_attr.max_value,
        )
    )
    logger.debug(
        "{}: {}".format(
            "MyNode.myDouble.soft_min_value (should be 0.5)",
            double_attr.soft_min_value,
        )
    )
    logger.debug(
        "{}: {}".format(
            "MyNode.myDouble.soft_max_value (should be 9.5)",
            double_attr.soft_max_value,
        )
    )

    # myEnum
    enum_attr = MyNode.myEnum
    logger.debug(
        "{}: {}".format(
            "MyNode.myEnum.enum_name (should be 'Alpha:Beta:Gamma')",
            enum_attr.enum_full_name,
        )
    )

    # myReadOnly
    readonly_attr = MyNode.myReadOnly
    logger.debug(
        "{}: {}".format(
            "MyNode.myReadOnly.readable (should be True)",
            readonly_attr.readable,
        )
    )
    logger.debug(
        "{}: {}".format(
            "MyNode.myReadOnly.writable (should be False)",
            readonly_attr.writable,
        )
    )


# ---------------------------------------------------------------------------
# 3. add_attr() が defaultValue / minValue / maxValue を正しく渡す
# ---------------------------------------------------------------------------


def add_attr_default_min_max():
    test_str.title("3. add_attr(): defaultValue / minValue / maxValue")

    # ノードを作成
    node_name = "test_extra_true_props"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("transform", name=node_name, skipSelect=True)
    modifier_manager = ModifierManager()
    MyNode(modifier_manager, name=node_name)
    modifier_manager.do_it_dg()

    exists = cmds.objExists(f"{node_name}.myDouble")
    logger.debug(
        "{}: {} (should be True)".format(
            f"{node_name}.myDouble exists", exists
        )
    )

    default_val = cmds.attributeQuery(
        "myDouble", node=node_name, listDefault=True
    )
    logger.debug("{}: {} (should be [1.0])".format("listDefault", default_val))

    min_val = cmds.attributeQuery("myDouble", node=node_name, minimum=True)
    logger.debug("{}: {} (should be [0.0])".format("minimum", min_val))

    max_val = cmds.attributeQuery("myDouble", node=node_name, maximum=True)
    logger.debug("{}: {} (should be [10.0])".format("maximum", max_val))


# ---------------------------------------------------------------------------
# 4. add_attr() が softMinValue / softMaxValue を正しく渡す
# ---------------------------------------------------------------------------


def add_attr_soft_min_max():
    test_str.title("4. add_attr(): softMinValue / softMaxValue")

    node_name = "test_add_attr_soft"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("transform", name=node_name, skipSelect=True)
    modifier_manager = ModifierManager()
    MyNode(modifier_manager, name=node_name)
    modifier_manager.do_it_dg()

    soft_min = cmds.attributeQuery("myDouble", node=node_name, softMin=True)
    logger.debug("{}: {} (should be [0.5])".format("softMin", soft_min))

    soft_max = cmds.attributeQuery("myDouble", node=node_name, softMax=True)
    logger.debug("{}: {} (should be [9.5])".format("softMax", soft_max))


# ---------------------------------------------------------------------------
# 5. EnumAttr で enum_name を指定して addAttr() される
# ---------------------------------------------------------------------------


def add_attr_enum_name():
    test_str.title("5. add_attr(): EnumAttr with enum_name")

    node_name = "test_add_attr_enum"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    modifier_manager = ModifierManager()
    MyNode.create(modifier_manager, name=node_name)
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()

    exists = cmds.objExists(f"{node_name}.myEnum")
    logger.debug(
        "{}: {} (should be True)".format(f"{node_name}.myEnum exists", exists)
    )

    enum_val = cmds.attributeQuery("myEnum", node=node_name, listEnum=True)
    logger.debug(
        "{}: {} (should be ['Alpha:Beta:Gamma'])".format("listEnum", enum_val)
    )


# ---------------------------------------------------------------------------
# 6. readable=False / writable=False が addAttr() へ渡される
# ---------------------------------------------------------------------------


def add_attr_readable_writable():
    test_str.title("6. add_attr(): readable / writable")

    node_name = "test_add_attr_rw"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("transform", name=node_name, skipSelect=True)
    modifier_manager = ModifierManager()
    MyNode(modifier_manager, name=node_name)
    modifier_manager.do_it_dg()

    exists = cmds.objExists(f"{node_name}.myReadOnly")
    logger.debug(
        "{}: {} (should be True)".format(
            f"{node_name}.myReadOnly exists", exists
        )
    )

    readable = cmds.attributeQuery("myReadOnly", node=node_name, readable=True)
    logger.debug("{}: {} (should be True)".format("readable", readable))

    writable = cmds.attributeQuery("myReadOnly", node=node_name, writable=True)
    logger.debug("{}: {} (should be False)".format("writable", writable))


# ---------------------------------------------------------------------------
# 7. DataStringAttr が dataType を使って addAttr() される
# ---------------------------------------------------------------------------


def add_attr_data_type_string():
    test_str.title("7. add_attr(): DataStringAttr uses dataType")

    node_name = "test_add_attr_string"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("transform", name=node_name, skipSelect=True)
    modifier_manager = ModifierManager()
    MyNode(modifier_manager, name=node_name)
    modifier_manager.do_it_dg()

    exists = cmds.objExists(f"{node_name}.myString")
    logger.debug(
        "{}: {} (should be True)".format(
            f"{node_name}.myString exists", exists
        )
    )

    attr_type = cmds.attributeQuery(
        "myString", node=node_name, attributeType=True
    )
    logger.debug(
        "{}: {} (should be 'typed')".format("attributeType", attr_type)
    )

    logger.debug(
        "{}: {}".format(
            "MyNode.myString.is_data_type", MyNode.myString.is_data_type
        )
    )
    logger.debug(
        "{}: {}".format("MyNode.myString.DATA_TYPE", MyNode.myString.DATA_TYPE)
    )


# ---------------------------------------------------------------------------
# 8. extra=False のプロパティが cmds.attributeQuery から値を取得する
# ---------------------------------------------------------------------------


def extra_false_query_properties():
    test_str.title("8. extra=False: properties query from cmds.attributeQuery")

    node_name = "test_extra_false_query"
    if cmds.objExists(node_name):
        cmds.delete(node_name)
    cmds.createNode("transform", name=node_name, skipSelect=True)
    modifier_manager = ModifierManager()
    MyNode(modifier_manager, name=node_name)
    modifier_manager.do_it_dg()

    # translateX は transform に標準で存在する extra=False アトリビュート
    attr = MyNode.translateX

    logger.debug("{}: {}".format("MyNode.translateX.extra", attr.extra))

    logger.debug(
        "{}: {}".format(
            "translateX.default_value (via cmds.attributeQuery)",
            attr.default_value,
        )
    )

    logger.debug(
        "{}: {}".format(
            "translateX.readable (via cmds.attributeQuery)", attr.readable
        )
    )

    logger.debug(
        "{}: {}".format(
            "translateX.writable (via cmds.attributeQuery)", attr.writable
        )
    )

    logger.debug(
        "{}: {}".format(
            "translateX.min_value (via cmds.attributeQuery)", attr.min_value
        )
    )
