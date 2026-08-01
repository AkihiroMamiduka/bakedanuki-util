from typing import Literal, assert_type

import bd_util as bdu
from maya.api import OpenMaya as om

from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr.define.node_attr.bd_add_double3_pair import (
    Input1AttrOperator as AddInput1AttrOperator,
    Input1PlugOperator as AddInput1PlugOperator,
    Input2AttrOperator as AddInput2AttrOperator,
    Input2PlugOperator as AddInput2PlugOperator,
    OutputAttrOperator as AddOutputAttrOperator,
    OutputPlugOperator as AddOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_add_double3_multi import (
    InputAttrOperator as AddMultiInputAttrOperator,
    InputPlugOperator as AddMultiInputPlugOperator,
    OutputAttrOperator as AddMultiOutputAttrOperator,
    OutputPlugOperator as AddMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_div_double3_pair import (
    Input1AttrOperator as DivInput1AttrOperator,
    Input1PlugOperator as DivInput1PlugOperator,
    Input2AttrOperator as DivInput2AttrOperator,
    Input2PlugOperator as DivInput2PlugOperator,
    OutputAttrOperator as DivOutputAttrOperator,
    OutputPlugOperator as DivOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_div_double3_multi import (
    InputAttrOperator as DivMultiInputAttrOperator,
    InputPlugOperator as DivMultiInputPlugOperator,
    OutputAttrOperator as DivMultiOutputAttrOperator,
    OutputPlugOperator as DivMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_mult_double3_pair import (
    Input1AttrOperator,
    Input1PlugOperator,
    Input2AttrOperator,
    Input2PlugOperator,
    OutputAttrOperator as FixedOutputAttrOperator,
    OutputPlugOperator as FixedOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_mult_double3_multi import (
    InputAttrOperator as MultiInputAttrOperator,
    InputPlugOperator as MultiInputPlugOperator,
    OutputAttrOperator as MultiOutputAttrOperator,
    OutputPlugOperator as MultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_pow_double3_pair import (
    Input1AttrOperator as PowInput1AttrOperator,
    Input1PlugOperator as PowInput1PlugOperator,
    Input2AttrOperator as PowInput2AttrOperator,
    Input2PlugOperator as PowInput2PlugOperator,
    OutputAttrOperator as PowOutputAttrOperator,
    OutputPlugOperator as PowOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_pow_double3_multi import (
    InputAttrOperator as PowMultiInputAttrOperator,
    InputPlugOperator as PowMultiInputPlugOperator,
    OutputAttrOperator as PowMultiOutputAttrOperator,
    OutputPlugOperator as PowMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_sub_double3_pair import (
    Input1AttrOperator as SubInput1AttrOperator,
    Input1PlugOperator as SubInput1PlugOperator,
    Input2AttrOperator as SubInput2AttrOperator,
    Input2PlugOperator as SubInput2PlugOperator,
    OutputAttrOperator as SubOutputAttrOperator,
    OutputPlugOperator as SubOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_sub_double3_multi import (
    InputAttrOperator as SubMultiInputAttrOperator,
    InputPlugOperator as SubMultiInputPlugOperator,
    OutputAttrOperator as SubMultiOutputAttrOperator,
    OutputPlugOperator as SubMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.compose_matrix import (
    InputTranslateAttrOperator,
    InputTranslatePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.wt_add_matrix import (
    WtMatrixAttrOperator,
    WtMatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.matrix import (
    MatrixAttrOperator,
    MatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
    ScalarBaseAttrOperator,
    ScalarBasePlugOperator,
    ScalarBaseField,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.double import (
    DoubleAttrOperator,
    DoublePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit import (
    double_linear,
)
from bd_util.maya.node.operator.attr.define.std.dt.matrix import (
    DataMatrixPlugOperator,
)
from bd_util.maya.node.operator.node._core import NodeOperator
from bd_util.maya.node.operator.node.dg._generated.compose_matrix import (
    InputRotateOrderEnumAttrOperator,
    InputRotateOrderEnumPlugOperator,
    InputRotateOrderEnumField,
)
from bd_util.maya.node.operator.node.dg.bd_add_double3_pair import (
    BdAddDouble3Pair,
)
from bd_util.maya.node.operator.node.dg.bd_add_double3_multi import (
    BdAddDouble3Multi,
)
from bd_util.maya.node.operator.node.dg.bd_div_double3_pair import (
    BdDivDouble3Pair,
)
from bd_util.maya.node.operator.node.dg.bd_div_double3_multi import (
    BdDivDouble3Multi,
)
from bd_util.maya.node.operator.node.dg.bd_mult_double3_pair import (
    BdMultDouble3Pair,
)
from bd_util.maya.node.operator.node.dg.bd_mult_double3_multi import (
    BdMultDouble3Multi,
)
from bd_util.maya.node.operator.node.dg.bd_pow_double3_pair import (
    BdPowDouble3Pair,
)
from bd_util.maya.node.operator.node.dg.bd_pow_double3_multi import (
    BdPowDouble3Multi,
)
from bd_util.maya.node.operator.node.dg.bd_sub_double3_pair import (
    BdSubDouble3Pair,
)
from bd_util.maya.node.operator.node.dg.bd_sub_double3_multi import (
    BdSubDouble3Multi,
)
from bd_util.maya.node.operator.node.dg.bd_mult_double_pair import (
    BdMultDoublePair,
)
from bd_util.maya.node.operator.node.dg.bd_mult_double_multi import (
    BdMultDoubleMulti,
)
from bd_util.maya.node.operator.node.dg.bd_pow_double_pair import (
    BdPowDoublePair,
)
from bd_util.maya.node.operator.node.dg.bd_pow_double_multi import (
    BdPowDoubleMulti,
)
from bd_util.maya.node.operator.node.dg.bd_add_double_pair import (
    BdAddDoublePair,
)
from bd_util.maya.node.operator.node.dg.bd_add_double_multi import (
    BdAddDoubleMulti,
)
from bd_util.maya.node.operator.node.dg.bd_div_double_pair import (
    BdDivDoublePair,
)
from bd_util.maya.node.operator.node.dg.bd_div_double_multi import (
    BdDivDoubleMulti,
)
from bd_util.maya.node.operator.node.dg.bd_sub_double_pair import (
    BdSubDoublePair,
)
from bd_util.maya.node.operator.node.dg.bd_sub_double_multi import (
    BdSubDoubleMulti,
)
from bd_util.maya.node.operator.node.dg.compose_matrix import ComposeMatrix
from bd_util.maya.node.operator.node.dg.decompose_matrix import (
    DecomposeMatrix,
)
from bd_util.maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix


def node_accessor_contract(nodes: bdu.Nodes) -> None:
    add_fixed = nodes.create.bdAddDouble3Pair(name="add_fixed")
    assert_type(add_fixed, BdAddDouble3Pair)
    assert_type(add_fixed.input1, AddInput1PlugOperator)
    assert_type(add_fixed.input2, AddInput2PlugOperator)
    assert_type(add_fixed.output, AddOutputPlugOperator)
    assert_type(add_fixed.output.get(), bdu.Double3)

    add_multi = nodes.create.bdAddDouble3Multi(name="add_multi")
    assert_type(add_multi, BdAddDouble3Multi)
    assert_type(add_multi.input, AddMultiInputPlugOperator)
    assert_type(add_multi.input[next], AddMultiInputPlugOperator)
    assert_type(add_multi.output, AddMultiOutputPlugOperator)
    assert_type(add_multi.output.get(), bdu.Double3)

    existing_add_fixed = nodes.existing.bdAddDouble3Pair("existing_add_fixed")
    assert_type(existing_add_fixed, BdAddDouble3Pair)
    existing_add_multi = nodes.existing.bdAddDouble3Multi("existing_add_multi")
    assert_type(existing_add_multi, BdAddDouble3Multi)

    div_fixed = nodes.create.bdDivDouble3Pair(name="div_fixed")
    assert_type(div_fixed, BdDivDouble3Pair)
    assert_type(div_fixed.input1, DivInput1PlugOperator)
    assert_type(div_fixed.input2, DivInput2PlugOperator)
    assert_type(div_fixed.output, DivOutputPlugOperator)
    assert_type(div_fixed.output.get(), bdu.Double3)

    div_multi = nodes.create.bdDivDouble3Multi(name="div_multi")
    assert_type(div_multi, BdDivDouble3Multi)
    assert_type(div_multi.input, DivMultiInputPlugOperator)
    assert_type(div_multi.input[next], DivMultiInputPlugOperator)
    assert_type(div_multi.output, DivMultiOutputPlugOperator)
    assert_type(div_multi.output.get(), bdu.Double3)

    existing_div_fixed = nodes.existing.bdDivDouble3Pair("existing_div_fixed")
    assert_type(existing_div_fixed, BdDivDouble3Pair)
    existing_div_multi = nodes.existing.bdDivDouble3Multi("existing_div_multi")
    assert_type(existing_div_multi, BdDivDouble3Multi)

    pow_fixed = nodes.create.bdPowDouble3Pair(name="pow_fixed")
    assert_type(pow_fixed, BdPowDouble3Pair)
    assert_type(pow_fixed.input1, PowInput1PlugOperator)
    assert_type(pow_fixed.input2, PowInput2PlugOperator)
    assert_type(pow_fixed.output, PowOutputPlugOperator)
    assert_type(pow_fixed.output.get(), bdu.Double3)

    pow_multi = nodes.create.bdPowDouble3Multi(name="pow_multi")
    assert_type(pow_multi, BdPowDouble3Multi)
    assert_type(pow_multi.input, PowMultiInputPlugOperator)
    assert_type(pow_multi.input[next], PowMultiInputPlugOperator)
    assert_type(pow_multi.output, PowMultiOutputPlugOperator)
    assert_type(pow_multi.output.get(), bdu.Double3)

    existing_pow_fixed = nodes.existing.bdPowDouble3Pair("existing_pow_fixed")
    assert_type(existing_pow_fixed, BdPowDouble3Pair)
    existing_pow_multi = nodes.existing.bdPowDouble3Multi("existing_pow_multi")
    assert_type(existing_pow_multi, BdPowDouble3Multi)

    sub_fixed = nodes.create.bdSubDouble3Pair(name="sub_fixed")
    assert_type(sub_fixed, BdSubDouble3Pair)
    assert_type(sub_fixed.input1, SubInput1PlugOperator)
    assert_type(sub_fixed.input2, SubInput2PlugOperator)
    assert_type(sub_fixed.output, SubOutputPlugOperator)
    assert_type(sub_fixed.output.get(), bdu.Double3)

    sub_multi = nodes.create.bdSubDouble3Multi(name="sub_multi")
    assert_type(sub_multi, BdSubDouble3Multi)
    assert_type(sub_multi.input, SubMultiInputPlugOperator)
    assert_type(sub_multi.input[next], SubMultiInputPlugOperator)
    assert_type(sub_multi.output, SubMultiOutputPlugOperator)
    assert_type(sub_multi.output.get(), bdu.Double3)

    existing_sub_fixed = nodes.existing.bdSubDouble3Pair("existing_sub_fixed")
    assert_type(existing_sub_fixed, BdSubDouble3Pair)
    existing_sub_multi = nodes.existing.bdSubDouble3Multi("existing_sub_multi")
    assert_type(existing_sub_multi, BdSubDouble3Multi)

    fixed = nodes.create.bdMultDouble3Pair(name="fixed")
    assert_type(fixed, BdMultDouble3Pair)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    multi = nodes.create.bdMultDouble3Multi(name="multi")
    assert_type(multi, BdMultDouble3Multi)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[next], MultiInputPlugOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)

    existing_fixed = nodes.existing.bdMultDouble3Pair("existing_fixed")
    assert_type(existing_fixed, BdMultDouble3Pair)
    existing_multi = nodes.existing.bdMultDouble3Multi("existing_multi")
    assert_type(existing_multi, BdMultDouble3Multi)

    double_fixed = nodes.create.bdMultDoublePair(name="double_fixed")
    assert_type(double_fixed, BdMultDoublePair)
    assert_type(double_fixed.input1, DoublePlugOperator)
    assert_type(double_fixed.input2, DoublePlugOperator)
    assert_type(double_fixed.output, DoublePlugOperator)
    assert_type(double_fixed.output.get(), float)

    double_multi = nodes.create.bdMultDoubleMulti(name="double_multi")
    assert_type(double_multi, BdMultDoubleMulti)
    assert_type(double_multi.input, DoublePlugOperator)
    assert_type(double_multi.input[next], DoublePlugOperator)
    assert_type(double_multi.output, DoublePlugOperator)
    assert_type(double_multi.output.get(), float)

    existing_double_fixed = nodes.existing.bdMultDoublePair(
        "existing_double_fixed"
    )
    assert_type(existing_double_fixed, BdMultDoublePair)
    existing_double_multi = nodes.existing.bdMultDoubleMulti(
        "existing_double_multi"
    )
    assert_type(existing_double_multi, BdMultDoubleMulti)

    double_add_fixed = nodes.create.bdAddDoublePair(name="double_add_fixed")
    assert_type(double_add_fixed, BdAddDoublePair)
    assert_type(double_add_fixed.input1, DoublePlugOperator)
    assert_type(double_add_fixed.input2, DoublePlugOperator)
    assert_type(double_add_fixed.output, DoublePlugOperator)
    assert_type(double_add_fixed.output.get(), float)

    double_add_multi = nodes.create.bdAddDoubleMulti(name="double_add_multi")
    assert_type(double_add_multi, BdAddDoubleMulti)
    assert_type(double_add_multi.input, DoublePlugOperator)
    assert_type(double_add_multi.input[next], DoublePlugOperator)
    assert_type(double_add_multi.output, DoublePlugOperator)
    assert_type(double_add_multi.output.get(), float)

    existing_double_add_fixed = nodes.existing.bdAddDoublePair(
        "existing_double_add_fixed"
    )
    assert_type(existing_double_add_fixed, BdAddDoublePair)
    existing_double_add_multi = nodes.existing.bdAddDoubleMulti(
        "existing_double_add_multi"
    )
    assert_type(existing_double_add_multi, BdAddDoubleMulti)

    double_div_fixed = nodes.create.bdDivDoublePair(name="double_div_fixed")
    assert_type(double_div_fixed, BdDivDoublePair)
    assert_type(double_div_fixed.input1, DoublePlugOperator)
    assert_type(double_div_fixed.input2, DoublePlugOperator)
    assert_type(double_div_fixed.output, DoublePlugOperator)
    assert_type(double_div_fixed.output.get(), float)

    double_div_multi = nodes.create.bdDivDoubleMulti(name="double_div_multi")
    assert_type(double_div_multi, BdDivDoubleMulti)
    assert_type(double_div_multi.input, DoublePlugOperator)
    assert_type(double_div_multi.input[next], DoublePlugOperator)
    assert_type(double_div_multi.output, DoublePlugOperator)
    assert_type(double_div_multi.output.get(), float)

    existing_double_div_fixed = nodes.existing.bdDivDoublePair(
        "existing_double_div_fixed"
    )
    assert_type(existing_double_div_fixed, BdDivDoublePair)
    existing_double_div_multi = nodes.existing.bdDivDoubleMulti(
        "existing_double_div_multi"
    )
    assert_type(existing_double_div_multi, BdDivDoubleMulti)

    double_pow_fixed = nodes.create.bdPowDoublePair(name="double_pow_fixed")
    assert_type(double_pow_fixed, BdPowDoublePair)
    assert_type(double_pow_fixed.input1, DoublePlugOperator)
    assert_type(double_pow_fixed.input2, DoublePlugOperator)
    assert_type(double_pow_fixed.output, DoublePlugOperator)
    assert_type(double_pow_fixed.output.get(), float)

    double_pow_multi = nodes.create.bdPowDoubleMulti(name="double_pow_multi")
    assert_type(double_pow_multi, BdPowDoubleMulti)
    assert_type(double_pow_multi.input, DoublePlugOperator)
    assert_type(double_pow_multi.input[next], DoublePlugOperator)
    assert_type(double_pow_multi.output, DoublePlugOperator)
    assert_type(double_pow_multi.output.get(), float)

    existing_double_pow_fixed = nodes.existing.bdPowDoublePair(
        "existing_double_pow_fixed"
    )
    assert_type(existing_double_pow_fixed, BdPowDoublePair)
    existing_double_pow_multi = nodes.existing.bdPowDoubleMulti(
        "existing_double_pow_multi"
    )
    assert_type(existing_double_pow_multi, BdPowDoubleMulti)

    double_sub_fixed = nodes.create.bdSubDoublePair(name="double_sub_fixed")
    assert_type(double_sub_fixed, BdSubDoublePair)
    assert_type(double_sub_fixed.input1, DoublePlugOperator)
    assert_type(double_sub_fixed.input2, DoublePlugOperator)
    assert_type(double_sub_fixed.output, DoublePlugOperator)
    assert_type(double_sub_fixed.output.get(), float)

    double_sub_multi = nodes.create.bdSubDoubleMulti(name="double_sub_multi")
    assert_type(double_sub_multi, BdSubDoubleMulti)
    assert_type(double_sub_multi.input, DoublePlugOperator)
    assert_type(double_sub_multi.input[next], DoublePlugOperator)
    assert_type(double_sub_multi.output, DoublePlugOperator)
    assert_type(double_sub_multi.output.get(), float)

    existing_double_sub_fixed = nodes.existing.bdSubDoublePair(
        "existing_double_sub_fixed"
    )
    assert_type(existing_double_sub_fixed, BdSubDoublePair)
    existing_double_sub_multi = nodes.existing.bdSubDoubleMulti(
        "existing_double_sub_multi"
    )
    assert_type(existing_double_sub_multi, BdSubDoubleMulti)

    compose = nodes.create.composeMatrix(name="compose")
    assert_type(compose, ComposeMatrix)

    decompose = nodes.existing.decomposeMatrix("decompose")
    assert_type(decompose, DecomposeMatrix)

    existing = nodes.existing("existing_node")
    assert_type(existing, NodeOperator)


def descriptor_contract(compose: ComposeMatrix) -> None:
    assert_type(ComposeMatrix.outputMatrix, MatrixAttrOperator)
    assert_type(compose.outputMatrix, MatrixPlugOperator)
    assert_type(compose.omat, MatrixPlugOperator)
    assert_type(compose.outputMatrix.get(), om.MMatrix)
    compose.outputMatrix.connect(("target", "input"))
    compose.outputMatrix.disconnect(["target", "input"])

    assert_type(ComposeMatrix.inputTranslate, InputTranslateAttrOperator)
    assert_type(compose.inputTranslate, InputTranslatePlugOperator)
    assert_type(
        compose.inputTranslate.inputTranslateX,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(compose.inputTranslate.inputTranslateX.get(), float)
    assert_type(compose.inputTranslate.get(), bdu.DoubleLinear3)
    assert_type(compose.inputTranslate.value, bdu.DoubleLinear3)
    assert_type(compose.inputTranslate.value_direct, bdu.DoubleLinear3)
    assert_type(compose.inputTranslate.get().x, float)
    assert_type(
        compose.inputTranslate.get().as_tuple(),
        tuple[float, float, float],
    )
    assert_type(
        compose.inputTranslate.inputTranslateX.keyframe,
        KeyframeManager,
    )

    assert_type(
        ComposeMatrix.inputRotateOrder,
        InputRotateOrderEnumAttrOperator,
    )
    assert_type(
        compose.inputRotateOrder,
        InputRotateOrderEnumPlugOperator,
    )
    assert_type(compose.inputRotateOrder.XYZ, Literal[0])
    assert_type(compose.inputRotateOrder.keyframe, KeyframeManager)


def bd_add_double3_pair_descriptor_contract(
    fixed: BdAddDouble3Pair,
    multi: BdAddDouble3Multi,
) -> None:
    assert_type(BdAddDouble3Pair.input1, AddInput1AttrOperator)
    assert_type(fixed.input1, AddInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdAddDouble3Pair.input2, AddInput2AttrOperator)
    assert_type(fixed.input2, AddInput2PlugOperator)
    assert_type(BdAddDouble3Pair.output, AddOutputAttrOperator)
    assert_type(fixed.output, AddOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdAddDouble3Multi.input, AddMultiInputAttrOperator)
    assert_type(multi.input, AddMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdAddDouble3Multi.output, AddMultiOutputAttrOperator)
    assert_type(multi.output, AddMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_add_double_pair_descriptor_contract(
    fixed: BdAddDoublePair,
    multi: BdAddDoubleMulti,
) -> None:
    assert_type(BdAddDoublePair.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdAddDoublePair.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdAddDoublePair.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdAddDoubleMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdAddDoubleMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_div_double3_pair_descriptor_contract(
    fixed: BdDivDouble3Pair,
    multi: BdDivDouble3Multi,
) -> None:
    assert_type(BdDivDouble3Pair.input1, DivInput1AttrOperator)
    assert_type(fixed.input1, DivInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDivDouble3Pair.input2, DivInput2AttrOperator)
    assert_type(fixed.input2, DivInput2PlugOperator)
    assert_type(BdDivDouble3Pair.output, DivOutputAttrOperator)
    assert_type(fixed.output, DivOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDivDouble3Multi.input, DivMultiInputAttrOperator)
    assert_type(multi.input, DivMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDivDouble3Multi.output, DivMultiOutputAttrOperator)
    assert_type(multi.output, DivMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_div_double_pair_descriptor_contract(
    fixed: BdDivDoublePair,
    multi: BdDivDoubleMulti,
) -> None:
    assert_type(BdDivDoublePair.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDivDoublePair.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDivDoublePair.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDivDoubleMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDivDoubleMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_pow_double3_pair_descriptor_contract(
    fixed: BdPowDouble3Pair,
    multi: BdPowDouble3Multi,
) -> None:
    assert_type(BdPowDouble3Pair.input1, PowInput1AttrOperator)
    assert_type(fixed.input1, PowInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdPowDouble3Pair.input2, PowInput2AttrOperator)
    assert_type(fixed.input2, PowInput2PlugOperator)
    assert_type(BdPowDouble3Pair.output, PowOutputAttrOperator)
    assert_type(fixed.output, PowOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdPowDouble3Multi.input, PowMultiInputAttrOperator)
    assert_type(multi.input, PowMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdPowDouble3Multi.output, PowMultiOutputAttrOperator)
    assert_type(multi.output, PowMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_pow_double_pair_descriptor_contract(
    fixed: BdPowDoublePair,
    multi: BdPowDoubleMulti,
) -> None:
    assert_type(BdPowDoublePair.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdPowDoublePair.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdPowDoublePair.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdPowDoubleMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdPowDoubleMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_sub_double3_pair_descriptor_contract(
    fixed: BdSubDouble3Pair,
    multi: BdSubDouble3Multi,
) -> None:
    assert_type(BdSubDouble3Pair.input1, SubInput1AttrOperator)
    assert_type(fixed.input1, SubInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdSubDouble3Pair.input2, SubInput2AttrOperator)
    assert_type(fixed.input2, SubInput2PlugOperator)
    assert_type(BdSubDouble3Pair.output, SubOutputAttrOperator)
    assert_type(fixed.output, SubOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdSubDouble3Multi.input, SubMultiInputAttrOperator)
    assert_type(multi.input, SubMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdSubDouble3Multi.output, SubMultiOutputAttrOperator)
    assert_type(multi.output, SubMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_sub_double_pair_descriptor_contract(
    fixed: BdSubDoublePair,
    multi: BdSubDoubleMulti,
) -> None:
    assert_type(BdSubDoublePair.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdSubDoublePair.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdSubDoublePair.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdSubDoubleMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdSubDoubleMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_mult_double3_pair_descriptor_contract(fixed: BdMultDouble3Pair) -> None:
    assert_type(BdMultDouble3Pair.input1, Input1AttrOperator)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdMultDouble3Pair.input2, Input2AttrOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.input2.input2Z.get(), float)
    assert_type(BdMultDouble3Pair.output, FixedOutputAttrOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)


def bd_mult_double3_multi_descriptor_contract(
    multi: BdMultDouble3Multi,
) -> None:
    assert_type(BdMultDouble3Multi.input, MultiInputAttrOperator)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdMultDouble3Multi.output, MultiOutputAttrOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_mult_double_pair_descriptor_contract(
    fixed: BdMultDoublePair,
    multi: BdMultDoubleMulti,
) -> None:
    assert_type(BdMultDoublePair.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(fixed.input1.get(), float)
    assert_type(BdMultDoublePair.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdMultDoublePair.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdMultDoubleMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdMultDoubleMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def scalar_base_contract(
    attr: InputRotateOrderEnumAttrOperator,
    plug: InputRotateOrderEnumPlugOperator,
    field: InputRotateOrderEnumField,
) -> None:
    scalar_attr: ScalarBaseAttrOperator[InputRotateOrderEnumPlugOperator] = (
        attr
    )
    scalar_plug: ScalarBasePlugOperator[InputRotateOrderEnumAttrOperator] = (
        plug
    )
    scalar_field: ScalarBaseField[
        InputRotateOrderEnumAttrOperator,
        InputRotateOrderEnumPlugOperator,
    ] = field

    assert_type(
        scalar_attr,
        InputRotateOrderEnumAttrOperator,
    )
    assert_type(
        scalar_plug,
        InputRotateOrderEnumPlugOperator,
    )
    assert_type(
        scalar_field,
        InputRotateOrderEnumField,
    )


def multi_compound_contract(nodes: bdu.Nodes) -> None:
    wt_add_matrix = nodes.create.wtAddMatrix(name="wt_add_matrix")
    assert_type(wt_add_matrix, WtAddMatrix)

    assert_type(WtAddMatrix.wtMatrix, WtMatrixAttrOperator)
    assert_type(wt_add_matrix.wtMatrix, WtMatrixPlugOperator)
    assert_type(wt_add_matrix.wtMatrix[0], WtMatrixPlugOperator)
    assert_type(wt_add_matrix.wtMatrix[next], WtMatrixPlugOperator)
    assert_type(
        wt_add_matrix.wtMatrix[next].matrixIn,
        DataMatrixPlugOperator,
    )
    assert_type(
        wt_add_matrix.wtMatrix[next].matrixIn.get(),
        om.MMatrix | None,
    )


def invalid_usage_contract(
    nodes: bdu.Nodes,
    c: ComposeMatrix,
) -> None:
    nodes.create.composeMatrix(
        unknown_option=True  # pyright: ignore[reportCallIssue]
    )
    nodes.existing.decomposeMatrix(123)  # pyright: ignore[reportArgumentType]
    c.outputMatrix.set("not a matrix")  # pyright: ignore[reportArgumentType]
    c.inputTranslate.set("not a vector")  # pyright: ignore[reportArgumentType]
    nodes.create.wtAddMatrix().wtMatrix[
        len
    ]  # pyright: ignore[reportArgumentType]
    c.x  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
