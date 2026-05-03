# coding: utf-8
"""
Node / Plug の文字列アクセス（__getitem__）のテスト

テスト項目:
  1. node["attrName"]           : トップレベルアトリビュートへの文字列アクセス
  2. node["attrName[0]"]        : マルチアトリビュートへのインデックス付き文字列アクセス
  3. node["attrName.subAttr"]   : ドット区切りによるサブアトリビュートへの文字列アクセス
  4. node["attrName[0].subAttr"]: インデックス + ドット区切りの複合文字列アクセス
  5. plug["subAttr"]            : Plug からのサブアトリビュートへの文字列アクセス
  6. plug 文字列の一致確認       : 取得した Plug の plug 文字列が期待値と一致するか
"""

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.operator.node.dg.plus_minus_average import (
    PlusMinusAverage,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    node_simple_attr()
    node_multi_attr_with_index()
    node_dotted_subattr()
    node_index_and_subattr()
    plug_string_subattr()
    plug_string_check()


# ---------------------------------------------------------------------------
# 1. node["attrName"] : トップレベルアトリビュートへの文字列アクセス
# ---------------------------------------------------------------------------


def node_simple_attr():
    test_str.title('1. node["attrName"]')

    node = PlusMinusAverage.create("test_str_access_1")

    plug_str = node["output1D"]
    plug_attr = node.output1D

    logger.debug(
        '{}: {} (should be {})'.format(
            'node["output1D"].plug',
            plug_str.plug,
            plug_attr.plug,
        )
    )
    logger.debug(
        '{}: {} (should be True)'.format(
            "plug equal",
            plug_str.plug == plug_attr.plug,
        )
    )


# ---------------------------------------------------------------------------
# 2. node["attrName[0]"] : マルチアトリビュートへのインデックス付き文字列アクセス
# ---------------------------------------------------------------------------


def node_multi_attr_with_index():
    test_str.title('2. node["attrName[0]"]')

    node = PlusMinusAverage.create("test_str_access_2")

    plug_str = node["input1D[0]"]
    plug_attr = node.input1D[0]

    logger.debug(
        '{}: {} (should be {})'.format(
            'node["input1D[0]"].plug',
            plug_str.plug,
            plug_attr.plug,
        )
    )
    logger.debug(
        '{}: {} (should be True)'.format(
            "plug equal",
            plug_str.plug == plug_attr.plug,
        )
    )


# ---------------------------------------------------------------------------
# 3. node["attrName.subAttr"] : ドット区切りによるサブアトリビュートへの文字列アクセス
# ---------------------------------------------------------------------------


def node_dotted_subattr():
    test_str.title('3. node["attrName.subAttr"]')

    node = PlusMinusAverage.create("test_str_access_3")

    plug_str = node["output3D.output3Dx"]
    plug_attr = node.output3D.output3Dx

    logger.debug(
        '{}: {} (should be {})'.format(
            'node["output3D.output3Dx"].plug',
            plug_str.plug,
            plug_attr.plug,
        )
    )
    logger.debug(
        '{}: {} (should be True)'.format(
            "plug equal",
            plug_str.plug == plug_attr.plug,
        )
    )


# ---------------------------------------------------------------------------
# 4. node["attrName[0].subAttr"] : インデックス + ドット区切りの複合文字列アクセス
# ---------------------------------------------------------------------------


def node_index_and_subattr():
    test_str.title('4. node["attrName[0].subAttr"]')

    node = PlusMinusAverage.create("test_str_access_4")

    plug_str = node["input3D[0].input3Dx"]
    plug_attr = node.input3D[0].input3Dx

    logger.debug(
        '{}: {} (should be {})'.format(
            'node["input3D[0].input3Dx"].plug',
            plug_str.plug,
            plug_attr.plug,
        )
    )
    logger.debug(
        '{}: {} (should be True)'.format(
            "plug equal",
            plug_str.plug == plug_attr.plug,
        )
    )


# ---------------------------------------------------------------------------
# 5. plug["subAttr"] : Plug からのサブアトリビュートへの文字列アクセス
# ---------------------------------------------------------------------------


def plug_string_subattr():
    test_str.title('5. plug["subAttr"]')

    node = PlusMinusAverage.create("test_str_access_5")

    plug_str = node.output3D["output3Dy"]
    plug_attr = node.output3D.output3Dy

    logger.debug(
        '{}: {} (should be {})'.format(
            'node.output3D["output3Dy"].plug',
            plug_str.plug,
            plug_attr.plug,
        )
    )
    logger.debug(
        '{}: {} (should be True)'.format(
            "plug equal",
            plug_str.plug == plug_attr.plug,
        )
    )


# ---------------------------------------------------------------------------
# 6. plug 文字列の一致確認
# ---------------------------------------------------------------------------


def plug_string_check():
    test_str.title("6. plug string check")

    node = PlusMinusAverage.create("test_str_access_6")

    cases = [
        ('node["output1D"]', node["output1D"].plug, f"{node.name}.output1D"),
        ('node["input1D[0]"]', node["input1D[0]"].plug, f"{node.name}.input1D[0]"),
        (
            'node["input3D[0].input3Dx"]',
            node["input3D[0].input3Dx"].plug,
            f"{node.name}.input3D[0].input3Dx",
        ),
        (
            'node.input3D[0]["input3Dy"]',
            node.input3D[0]["input3Dy"].plug,
            f"{node.name}.input3D[0].input3Dy",
        ),
    ]

    for label, result, expected in cases:
        logger.debug(
            "{}: {} (should be {}) match={}".format(
                label,
                result,
                expected,
                result == expected,
            )
        )
