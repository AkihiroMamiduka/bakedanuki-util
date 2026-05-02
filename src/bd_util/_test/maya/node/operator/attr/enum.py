# coding: utf-8
"""
EnumAttr.enum / EnumPlug.enum アクセスのテスト

テスト項目:
  1. クラスアクセス: PlusMinusAverage.operation.enum が OperationEnum クラスを返す
  2. インスタンスアクセス: node.operation.enum が OperationEnum クラスを返す
  3. クラスアクセスでメンバー参照: PlusMinusAverage.operation.enum.sum が正しい値を返す
  4. インスタンスアクセスでメンバー参照: node.operation.enum.sum が正しい値を返す
  5. to_enum_name(): OperationEnum.to_enum_name() の出力値を確認する
  6. 等値比較: PlusMinusAverage.operation.enum.no_operation == 0 が True であることを確認する
"""

# self
from ...... import logger as u_logger
from ..... import str as test_str
from ......maya.node.operator.node.dg.plus_minus_average import (
    OperationEnum,
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
# 1. クラスアクセス: EnumAttr.enum が OperationEnum クラスを返す
# ---------------------------------------------------------------------------


def class_access_returns_enum_class():
    test_str.title("1. class access: EnumAttr.enum returns OperationEnum class")

    enum_cls = PlusMinusAverage.operation.enum
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.operation.enum",
            enum_cls,
        )
    )
    logger.debug(
        "{}: {} (should be True)".format(
            "is OperationEnum",
            enum_cls is OperationEnum,
        )
    )


# ---------------------------------------------------------------------------
# 2. インスタンスアクセス: EnumPlug.enum が OperationEnum クラスを返す
# ---------------------------------------------------------------------------


def instance_access_returns_enum_class():
    test_str.title(
        "2. instance access: EnumPlug.enum returns OperationEnum class"
    )

    node = PlusMinusAverage.create("test_enum_instance")
    enum_cls = node.operation.enum
    logger.debug(
        "{}: {}".format(
            "node.operation.enum",
            enum_cls,
        )
    )
    logger.debug(
        "{}: {} (should be True)".format(
            "is OperationEnum",
            enum_cls is OperationEnum,
        )
    )


# ---------------------------------------------------------------------------
# 3. クラスアクセスでメンバー参照
# ---------------------------------------------------------------------------


def class_access_enum_member():
    test_str.title("3. class access: EnumAttr.enum member reference")

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "PlusMinusAverage.operation.enum.no_operation",
            PlusMinusAverage.operation.enum.no_operation,
            OperationEnum.no_operation,
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "PlusMinusAverage.operation.enum.sum",
            PlusMinusAverage.operation.enum.sum,
            OperationEnum.sum,
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "PlusMinusAverage.operation.enum.subtract",
            PlusMinusAverage.operation.enum.subtract,
            OperationEnum.subtract,
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "PlusMinusAverage.operation.enum.average",
            PlusMinusAverage.operation.enum.average,
            OperationEnum.average,
        )
    )


# ---------------------------------------------------------------------------
# 4. インスタンスアクセスでメンバー参照
# ---------------------------------------------------------------------------


def instance_access_enum_member():
    test_str.title("4. instance access: EnumPlug.enum member reference")

    node = PlusMinusAverage.create("test_enum_member")

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "node.operation.enum.no_operation",
            node.operation.enum.no_operation,
            OperationEnum.no_operation,
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "node.operation.enum.sum",
            node.operation.enum.sum,
            OperationEnum.sum,
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "node.operation.enum.subtract",
            node.operation.enum.subtract,
            OperationEnum.subtract,
        )
    )

    test_str.separator()
    logger.debug(
        "{}: {} (should be {})".format(
            "node.operation.enum.average",
            node.operation.enum.average,
            OperationEnum.average,
        )
    )


# ---------------------------------------------------------------------------
# 5. to_enum_name(): OperationEnum.to_enum_name() の出力値を確認する
# ---------------------------------------------------------------------------


def to_enum_name_output():
    test_str.title("5. to_enum_name(): OperationEnum.to_enum_name() output")

    result = OperationEnum.to_enum_name()
    expected = "No operation=0:Sum=1:Subtract=2:Average=3"
    logger.debug(
        "{}: {}".format(
            "OperationEnum.to_enum_name()",
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
    test_str.title(
        "6. equality: PlusMinusAverage.operation.enum.no_operation == 0"
    )

    result = PlusMinusAverage.operation.enum.no_operation == 0
    logger.debug(
        "{}: {} (should be True)".format(
            "PlusMinusAverage.operation.enum.no_operation == 0",
            result,
        )
    )
