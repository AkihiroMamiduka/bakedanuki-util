# coding: utf-8
"""
EnumAttr.enum / EnumPlug.enum アクセスのテスト

テスト項目:
  1. クラスアクセス: PlusMinusAverage.operation.enum が OperationEnum クラスを返す
  2. インスタンスアクセス: node.operation.enum が OperationEnum クラスを返す
  3. クラスアクセスでメンバー参照: PlusMinusAverage.operation.enum.SUM が正しい値を返す
  4. インスタンスアクセスでメンバー参照: node.operation.enum.SUM が正しい値を返す
  5. to_enum_name(): OperationEnum.to_enum_name() の出力値を確認する
  6. 等値比較: PlusMinusAverage.operation.enum.NO_OPERATION == 0 が True であることを確認する
"""

# maya
from maya.api import OpenMaya as om

# self
from ...... import logger as u_logger
from ..... import str as test_str
from ......maya.node.operator.node.dg.plus_minus_average import (
    PlusMinusAverage,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    class_access_returns_enum_class()
    instance_access_returns_enum_class()
    class_access_enum_member()
    instance_access_enum_member()
    to_enum_name_output()
    no_operation_equals_zero()


# ---------------------------------------------------------------------------
# 1. クラスアクセス: PlusMinusAverage.operation が EnumAttr クラスを返す
# ---------------------------------------------------------------------------
def class_access_returns_enum_class():
    test_str.title(
        "1. class access: PlusMinusAverage.operation returns EnumAttr class"
    )

    enum_cls = PlusMinusAverage.operation
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.operation",
            enum_cls,
        )
    )


# ---------------------------------------------------------------------------
# 2. インスタンスアクセス: PlusMinusAverage.operation が EnumAttr クラスを返す
# ---------------------------------------------------------------------------
def instance_access_returns_enum_class():
    test_str.title(
        "2. instance access: PlusMinusAverage.operation returns EnumAttr class"
    )

    mod = om.MDGModifier()
    node = PlusMinusAverage.create(mod, name="test_enum_instance")
    enum_cls = node.operation
    logger.debug(
        "{}: {}".format(
            "node.operation",
            enum_cls,
        )
    )


# ---------------------------------------------------------------------------
# 3. クラスアクセスでメンバー参照
# ---------------------------------------------------------------------------
def class_access_enum_member():
    test_str.title("3. class access: EnumAttr.enum member reference")

    logger.debug(
        "{}: {} (name: {})".format(
            "PlusMinusAverage.operation.NO_OPERATION",
            PlusMinusAverage.operation.NO_OPERATION,
            PlusMinusAverage.operation.name_by_index(
                PlusMinusAverage.operation.NO_OPERATION
            ),
        )
    )

    logger.debug(
        "{}: {} (name: {})".format(
            "PlusMinusAverage.operation.SUM",
            PlusMinusAverage.operation.SUM,
            PlusMinusAverage.operation.name_by_index(
                PlusMinusAverage.operation.SUM
            ),
        )
    )

    logger.debug(
        "{}: {} (name: {})".format(
            "PlusMinusAverage.operation.SUBTRACT",
            PlusMinusAverage.operation.SUBTRACT,
            PlusMinusAverage.operation.name_by_index(
                PlusMinusAverage.operation.SUBTRACT
            ),
        )
    )

    logger.debug(
        "{}: {} (name: {})".format(
            "PlusMinusAverage.operation.AVERAGE",
            PlusMinusAverage.operation.AVERAGE,
            PlusMinusAverage.operation.name_by_index(
                PlusMinusAverage.operation.AVERAGE
            ),
        )
    )


# ---------------------------------------------------------------------------
# 4. インスタンスアクセスでメンバー参照
# ---------------------------------------------------------------------------
def instance_access_enum_member():
    test_str.title("4. instance access: EnumPlug.enum member reference")

    mod = om.MDGModifier()
    node = PlusMinusAverage.create(mod, name="test_enum_member")

    logger.debug(
        "{}: {} (name: {})".format(
            "node.operation.NO_OPERATION",
            node.operation.NO_OPERATION,
            node.operation.name_by_index(node.operation.NO_OPERATION),
        )
    )

    logger.debug(
        "{}: {} (name: {})".format(
            "node.operation.SUM",
            node.operation.SUM,
            node.operation.name_by_index(node.operation.SUM),
        )
    )

    logger.debug(
        "{}: {} (name: {})".format(
            "node.operation.SUBTRACT",
            node.operation.SUBTRACT,
            node.operation.name_by_index(node.operation.SUBTRACT),
        )
    )

    logger.debug(
        "{}: {} (name: {})".format(
            "node.operation.AVERAGE",
            node.operation.AVERAGE,
            node.operation.name_by_index(node.operation.AVERAGE),
        )
    )


# ---------------------------------------------------------------------------
# 5. to_enum_name(): AttributeEnum.to_enum_name() の出力値を確認する
# ---------------------------------------------------------------------------
def to_enum_name_output():
    test_str.title("5. to_enum_name(): AttributeEnum.to_enum_name() output")

    result = PlusMinusAverage.nodeState.enum_full_name()
    expected = "{}:{}:{}:{}:{}:{}".format(
        "Normal",
        "HasNoEffect",
        "Blocking",
        "Waiting-Normal=8",
        "Waiting-HasNoEffect",
        "Waiting-Blocking",
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.nodeState.enum_full_name()",
            result,
        )
    )

    test_str.separator()
    result = PlusMinusAverage.operation.enum_full_name()
    expected = "No operation=0:Sum=1:Subtract=2:Average=3"
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.operation.enum_full_name()",
            result,
        )
    )
    logger.debug(
        "{}: {} (should be True)".format(
            f"== '{expected}'",
            result == expected,
        )
    )


# ---------------------------------------------------------------------------
# 6. 等値比較: no_operation == 0 が True であることを確認する
# ---------------------------------------------------------------------------
def no_operation_equals_zero():
    test_str.title("6. equality: PlusMinusAverage.operation.NO_OPERATION == 0")

    result = PlusMinusAverage.operation.NO_OPERATION == 0
    logger.debug(
        "{}: {} (should be True)".format(
            "PlusMinusAverage.operation.NO_OPERATION == 0",
            result,
        )
    )
