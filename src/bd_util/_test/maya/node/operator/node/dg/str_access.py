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

# maya
from maya import cmds
from maya.api import OpenMaya as om

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

    dg_mod = om.MDGModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = PlusMinusAverage.create(dg_mod, name=name)
    dg_mod.doIt()

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'PlusMinusAverage["output1D"]._attr_path',
            PlusMinusAverage["output1D"]._attr_path,
            PlusMinusAverage.output1D._attr_path,
            PlusMinusAverage["output1D"]._attr_path
            == PlusMinusAverage.output1D._attr_path,
        )
    )

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'node["output1D"].plug',
            node["output1D"].plug,
            node.output1D.plug,
            node["output1D"].plug == node.output1D.plug,
        )
    )


# ---------------------------------------------------------------------------
# 2. node["attrName[0]"] : マルチアトリビュートへのインデックス付き文字列アクセス
# ---------------------------------------------------------------------------


def node_multi_attr_with_index():
    test_str.title('2. node["attrName"][0]')

    dg_mod = om.MDGModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = PlusMinusAverage.create(dg_mod, name=name)
    dg_mod.doIt()

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'PlusMinusAverage["input1D"][0]._attr_path',
            PlusMinusAverage["input1D"]._attr_path,
            PlusMinusAverage.input1D._attr_path,
            PlusMinusAverage["input1D"]._attr_path
            == PlusMinusAverage.input1D._attr_path,
        )
    )

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'node["input1D"][0].plug',
            node["input1D"][0].plug,
            node.input1D[0].plug,
            node["input1D"][0].plug == node.input1D[0].plug,
        )
    )


# ---------------------------------------------------------------------------
# 3. node["attrName.subAttr"] : ドット区切りによるサブアトリビュートへの文字列アクセス
# ---------------------------------------------------------------------------


def node_dotted_subattr():
    test_str.title('3. node["attrName.subAttr"]')

    dg_mod = om.MDGModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = PlusMinusAverage.create(dg_mod, name=name)
    dg_mod.doIt()

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'PlusMinusAverage["output3D"]["output3Dx"]._attr_path',
            PlusMinusAverage["output3D"]["output3Dx"]._attr_path,
            PlusMinusAverage.output3D.output3Dx._attr_path,
            PlusMinusAverage["output3D"]["output3Dx"]._attr_path
            == PlusMinusAverage.output3D.output3Dx._attr_path,
        )
    )

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'node["output3D"]["output3Dx"].plug',
            node["output3D"]["output3Dx"].plug,
            node.output3D.output3Dx.plug,
            node["output3D"]["output3Dx"].plug == node.output3D.output3Dx.plug,
        )
    )


# ---------------------------------------------------------------------------
# 4. node["attrName[0].subAttr"] : インデックス + ドット区切りの複合文字列アクセス
# ---------------------------------------------------------------------------


def node_index_and_subattr():
    test_str.title('4. node["attrName[0].subAttr"]')

    dg_mod = om.MDGModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = PlusMinusAverage.create(dg_mod, name=name)
    dg_mod.doIt()

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'PlusMinusAverage["input3D"]["input3Dx"]._attr_path',
            PlusMinusAverage["input3D"]["input3Dx"]._attr_path,
            PlusMinusAverage.input3D.input3Dx._attr_path,
            PlusMinusAverage["input3D"]["input3Dx"]._attr_path
            == PlusMinusAverage.input3D.input3Dx._attr_path,
        )
    )

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'node["input3D"][0]["input3Dx"].plug',
            node["input3D"][0]["input3Dx"].plug,
            node.input3D[0].input3Dx.plug,
            node["input3D"][0]["input3Dx"].plug
            == node.input3D[0].input3Dx.plug,
        )
    )


# ---------------------------------------------------------------------------
# 5. plug["subAttr"] : Plug からのサブアトリビュートへの文字列アクセス
# ---------------------------------------------------------------------------


def plug_string_subattr():
    test_str.title('5. plug["subAttr"]')

    dg_mod = om.MDGModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = PlusMinusAverage.create(dg_mod, name=name)
    dg_mod.doIt()

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'PlusMinusAverage.output3D["output3Dy"]._attr_path',
            PlusMinusAverage.output3D["output3Dy"]._attr_path,
            PlusMinusAverage.output3D.output3Dy._attr_path,
            PlusMinusAverage.output3D["output3Dy"]._attr_path
            == PlusMinusAverage.output3D.output3Dy._attr_path,
        )
    )

    logger.debug(
        "{}: {} (should be {}) -> {}".format(
            'node.output3D["output3Dy"].plug',
            node.output3D["output3Dy"].plug,
            node.output3D.output3Dy.plug,
            node.output3D["output3Dy"].plug == node.output3D.output3Dy.plug,
        )
    )


# ---------------------------------------------------------------------------
# 6. plug 文字列の一致確認
# ---------------------------------------------------------------------------


def plug_string_check():
    test_str.title("6. plug string check")

    dg_mod = om.MDGModifier()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = PlusMinusAverage.create(dg_mod, name=name)
    dg_mod.doIt()

    cases = [
        (
            'PlusMinusAverage["output1D"]',
            PlusMinusAverage["output1D"]._attr_path,
            f"{PlusMinusAverage.output1D._attr_path}",
        ),
        (
            'PlusMinusAverage["input1D"]',
            PlusMinusAverage["input1D"]._attr_path,
            f"{PlusMinusAverage.input1D._attr_path}",
        ),
        (
            'PlusMinusAverage["input3D"]["input3Dx"]',
            PlusMinusAverage["input3D"]["input3Dx"]._attr_path,
            f"{PlusMinusAverage.input3D.input3Dx._attr_path}",
        ),
        (
            'PlusMinusAverage.input3D["input3Dy"]',
            PlusMinusAverage.input3D["input3Dy"]._attr_path,
            f"{PlusMinusAverage.input3D.input3Dy._attr_path}",
        ),
    ]
    for label, result, expected in cases:
        logger.debug(
            "{}: {} (should be {}) -> {}".format(
                label,
                result,
                expected,
                str(result) == expected,
            )
        )

    cases = [
        (
            'node["output1D"]',
            node["output1D"].plug,
            f"{node.name}.output1D",
        ),
        (
            'node["input1D"][0]',
            node["input1D"][0].plug,
            f"{node.name}.input1D[0]",
        ),
        (
            'node["input3D"][0]["input3Dx"]',
            node["input3D"][0]["input3Dx"].plug,
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
            "{}: {} (should be {}) -> {}".format(
                label,
                result,
                expected,
                str(result) == expected,
            )
        )
