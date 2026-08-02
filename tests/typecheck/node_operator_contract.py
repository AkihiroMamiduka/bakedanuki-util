from typing import Literal, assert_type

import bd_util as bdu
from maya.api import OpenMaya as om

from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_add import (
    Input1AttrOperator as AddInput1AttrOperator,
    Input1PlugOperator as AddInput1PlugOperator,
    Input2AttrOperator as AddInput2AttrOperator,
    Input2PlugOperator as AddInput2PlugOperator,
    OutputAttrOperator as AddOutputAttrOperator,
    OutputPlugOperator as AddOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_add_multi import (
    InputAttrOperator as AddMultiInputAttrOperator,
    InputPlugOperator as AddMultiInputPlugOperator,
    OutputAttrOperator as AddMultiOutputAttrOperator,
    OutputPlugOperator as AddMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_div import (
    Input1AttrOperator as DivInput1AttrOperator,
    Input1PlugOperator as DivInput1PlugOperator,
    Input2AttrOperator as DivInput2AttrOperator,
    Input2PlugOperator as DivInput2PlugOperator,
    OutputAttrOperator as DivOutputAttrOperator,
    OutputPlugOperator as DivOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_div_multi import (
    InputAttrOperator as DivMultiInputAttrOperator,
    InputPlugOperator as DivMultiInputPlugOperator,
    OutputAttrOperator as DivMultiOutputAttrOperator,
    OutputPlugOperator as DivMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_max import (
    Input1PlugOperator as MaxInput1PlugOperator,
    Input2PlugOperator as MaxInput2PlugOperator,
    OutputPlugOperator as MaxOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_max_multi import (
    InputPlugOperator as MaxMultiInputPlugOperator,
    OutputPlugOperator as MaxMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_min import (
    Input1PlugOperator as MinInput1PlugOperator,
    Input2PlugOperator as MinInput2PlugOperator,
    OutputPlugOperator as MinOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_min_multi import (
    InputPlugOperator as MinMultiInputPlugOperator,
    OutputPlugOperator as MinMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_value import (
    ValueAttrOperator as Double3ValueAttrOperator,
    ValuePlugOperator as Double3ValuePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_mult import (
    Input1AttrOperator,
    Input1PlugOperator,
    Input2AttrOperator,
    Input2PlugOperator,
    OutputAttrOperator as FixedOutputAttrOperator,
    OutputPlugOperator as FixedOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_mult_multi import (
    InputAttrOperator as MultiInputAttrOperator,
    InputPlugOperator as MultiInputPlugOperator,
    OutputAttrOperator as MultiOutputAttrOperator,
    OutputPlugOperator as MultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_pow import (
    Input1AttrOperator as PowInput1AttrOperator,
    Input1PlugOperator as PowInput1PlugOperator,
    Input2AttrOperator as PowInput2AttrOperator,
    Input2PlugOperator as PowInput2PlugOperator,
    OutputAttrOperator as PowOutputAttrOperator,
    OutputPlugOperator as PowOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_pow_multi import (
    InputAttrOperator as PowMultiInputAttrOperator,
    InputPlugOperator as PowMultiInputPlugOperator,
    OutputAttrOperator as PowMultiOutputAttrOperator,
    OutputPlugOperator as PowMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_sub import (
    Input1AttrOperator as SubInput1AttrOperator,
    Input1PlugOperator as SubInput1PlugOperator,
    Input2AttrOperator as SubInput2AttrOperator,
    Input2PlugOperator as SubInput2PlugOperator,
    OutputAttrOperator as SubOutputAttrOperator,
    OutputPlugOperator as SubOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_sub_multi import (
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
from bd_util.maya.node.operator.node.dg.bd_dbl3_add import (
    BdDbl3Add,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_add_multi import (
    BdDbl3AddMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_div import (
    BdDbl3Div,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_div_multi import (
    BdDbl3DivMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_max import BdDbl3Max
from bd_util.maya.node.operator.node.dg.bd_dbl3_max_multi import BdDbl3MaxMulti
from bd_util.maya.node.operator.node.dg.bd_dbl3_min import BdDbl3Min
from bd_util.maya.node.operator.node.dg.bd_dbl3_min_multi import BdDbl3MinMulti
from bd_util.maya.node.operator.node.dg.bd_dbl3_value import BdDbl3Value
from bd_util.maya.node.operator.node.dg.bd_dbl3_mult import (
    BdDbl3Mult,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_mult_multi import (
    BdDbl3MultMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_pow import (
    BdDbl3Pow,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_pow_multi import (
    BdDbl3PowMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_sub import (
    BdDbl3Sub,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_sub_multi import (
    BdDbl3SubMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_mult import (
    BdDblMult,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_mult_multi import (
    BdDblMultMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_pow import (
    BdDblPow,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_pow_multi import (
    BdDblPowMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_add import (
    BdDblAdd,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_add_multi import (
    BdDblAddMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_div import (
    BdDblDiv,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_div_multi import (
    BdDblDivMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_max import BdDblMax
from bd_util.maya.node.operator.node.dg.bd_dbl_max_multi import BdDblMaxMulti
from bd_util.maya.node.operator.node.dg.bd_dbl_min import BdDblMin
from bd_util.maya.node.operator.node.dg.bd_dbl_min_multi import BdDblMinMulti
from bd_util.maya.node.operator.node.dg.bd_dbl_value import BdDblValue
from bd_util.maya.node.operator.node.dg.bd_dbl_sub import (
    BdDblSub,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_sub_multi import (
    BdDblSubMulti,
)
from bd_util.maya.node.operator.node.dg.compose_matrix import ComposeMatrix
from bd_util.maya.node.operator.node.dg.decompose_matrix import (
    DecomposeMatrix,
)
from bd_util.maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix


def node_accessor_contract(nodes: bdu.Nodes) -> None:
    add_fixed = nodes.create.bdDbl3_Add(name="add_fixed")
    assert_type(add_fixed, BdDbl3Add)
    assert_type(add_fixed.input1, AddInput1PlugOperator)
    assert_type(add_fixed.input2, AddInput2PlugOperator)
    assert_type(add_fixed.output, AddOutputPlugOperator)
    assert_type(add_fixed.output.get(), bdu.Double3)

    add_multi = nodes.create.bdDbl3_AddMulti(name="add_multi")
    assert_type(add_multi, BdDbl3AddMulti)
    assert_type(add_multi.input, AddMultiInputPlugOperator)
    assert_type(add_multi.input[next], AddMultiInputPlugOperator)
    assert_type(add_multi.output, AddMultiOutputPlugOperator)
    assert_type(add_multi.output.get(), bdu.Double3)

    existing_add_fixed = nodes.existing.bdDbl3_Add("existing_add_fixed")
    assert_type(existing_add_fixed, BdDbl3Add)
    existing_add_multi = nodes.existing.bdDbl3_AddMulti("existing_add_multi")
    assert_type(existing_add_multi, BdDbl3AddMulti)

    min_fixed = nodes.create.bdDbl3_Min(name="min_fixed")
    assert_type(min_fixed, BdDbl3Min)
    assert_type(min_fixed.input1, MinInput1PlugOperator)
    assert_type(min_fixed.input2, MinInput2PlugOperator)
    assert_type(min_fixed.output, MinOutputPlugOperator)
    assert_type(min_fixed.output.get(), bdu.Double3)

    min_multi = nodes.create.bdDbl3_MinMulti(name="min_multi")
    assert_type(min_multi, BdDbl3MinMulti)
    assert_type(min_multi.input, MinMultiInputPlugOperator)
    assert_type(min_multi.input[next], MinMultiInputPlugOperator)
    assert_type(min_multi.output, MinMultiOutputPlugOperator)
    assert_type(min_multi.output.get(), bdu.Double3)

    assert_type(nodes.existing.bdDbl3_Min("existing_min"), BdDbl3Min)
    assert_type(
        nodes.existing.bdDbl3_MinMulti("existing_min_multi"),
        BdDbl3MinMulti,
    )

    max_fixed = nodes.create.bdDbl3_Max(name="max_fixed")
    assert_type(max_fixed, BdDbl3Max)
    assert_type(max_fixed.input1, MaxInput1PlugOperator)
    assert_type(max_fixed.input2, MaxInput2PlugOperator)
    assert_type(max_fixed.output, MaxOutputPlugOperator)
    assert_type(max_fixed.output.get(), bdu.Double3)

    max_multi = nodes.create.bdDbl3_MaxMulti(name="max_multi")
    assert_type(max_multi, BdDbl3MaxMulti)
    assert_type(max_multi.input, MaxMultiInputPlugOperator)
    assert_type(max_multi.input[next], MaxMultiInputPlugOperator)
    assert_type(max_multi.output, MaxMultiOutputPlugOperator)
    assert_type(max_multi.output.get(), bdu.Double3)

    assert_type(nodes.existing.bdDbl3_Max("existing_max"), BdDbl3Max)
    assert_type(
        nodes.existing.bdDbl3_MaxMulti("existing_max_multi"),
        BdDbl3MaxMulti,
    )

    div_fixed = nodes.create.bdDbl3_Div(name="div_fixed")
    assert_type(div_fixed, BdDbl3Div)
    assert_type(div_fixed.input1, DivInput1PlugOperator)
    assert_type(div_fixed.input2, DivInput2PlugOperator)
    assert_type(div_fixed.output, DivOutputPlugOperator)
    assert_type(div_fixed.output.get(), bdu.Double3)

    div_multi = nodes.create.bdDbl3_DivMulti(name="div_multi")
    assert_type(div_multi, BdDbl3DivMulti)
    assert_type(div_multi.input, DivMultiInputPlugOperator)
    assert_type(div_multi.input[next], DivMultiInputPlugOperator)
    assert_type(div_multi.output, DivMultiOutputPlugOperator)
    assert_type(div_multi.output.get(), bdu.Double3)

    existing_div_fixed = nodes.existing.bdDbl3_Div("existing_div_fixed")
    assert_type(existing_div_fixed, BdDbl3Div)
    existing_div_multi = nodes.existing.bdDbl3_DivMulti("existing_div_multi")
    assert_type(existing_div_multi, BdDbl3DivMulti)

    double3_value = nodes.create.bdDbl3_Value(name="double3_value")
    assert_type(double3_value, BdDbl3Value)
    assert_type(double3_value.value, Double3ValuePlugOperator)
    assert_type(double3_value.value.valueX.get(), float)
    assert_type(double3_value.value.get(), bdu.Double3)
    existing_double3_value = nodes.existing.bdDbl3_Value(
        "existing_double3_value"
    )
    assert_type(existing_double3_value, BdDbl3Value)

    pow_fixed = nodes.create.bdDbl3_Pow(name="pow_fixed")
    assert_type(pow_fixed, BdDbl3Pow)
    assert_type(pow_fixed.input1, PowInput1PlugOperator)
    assert_type(pow_fixed.input2, PowInput2PlugOperator)
    assert_type(pow_fixed.output, PowOutputPlugOperator)
    assert_type(pow_fixed.output.get(), bdu.Double3)

    pow_multi = nodes.create.bdDbl3_PowMulti(name="pow_multi")
    assert_type(pow_multi, BdDbl3PowMulti)
    assert_type(pow_multi.input, PowMultiInputPlugOperator)
    assert_type(pow_multi.input[next], PowMultiInputPlugOperator)
    assert_type(pow_multi.output, PowMultiOutputPlugOperator)
    assert_type(pow_multi.output.get(), bdu.Double3)

    existing_pow_fixed = nodes.existing.bdDbl3_Pow("existing_pow_fixed")
    assert_type(existing_pow_fixed, BdDbl3Pow)
    existing_pow_multi = nodes.existing.bdDbl3_PowMulti("existing_pow_multi")
    assert_type(existing_pow_multi, BdDbl3PowMulti)

    sub_fixed = nodes.create.bdDbl3_Sub(name="sub_fixed")
    assert_type(sub_fixed, BdDbl3Sub)
    assert_type(sub_fixed.input1, SubInput1PlugOperator)
    assert_type(sub_fixed.input2, SubInput2PlugOperator)
    assert_type(sub_fixed.output, SubOutputPlugOperator)
    assert_type(sub_fixed.output.get(), bdu.Double3)

    sub_multi = nodes.create.bdDbl3_SubMulti(name="sub_multi")
    assert_type(sub_multi, BdDbl3SubMulti)
    assert_type(sub_multi.input, SubMultiInputPlugOperator)
    assert_type(sub_multi.input[next], SubMultiInputPlugOperator)
    assert_type(sub_multi.output, SubMultiOutputPlugOperator)
    assert_type(sub_multi.output.get(), bdu.Double3)

    existing_sub_fixed = nodes.existing.bdDbl3_Sub("existing_sub_fixed")
    assert_type(existing_sub_fixed, BdDbl3Sub)
    existing_sub_multi = nodes.existing.bdDbl3_SubMulti("existing_sub_multi")
    assert_type(existing_sub_multi, BdDbl3SubMulti)

    fixed = nodes.create.bdDbl3_Mult(name="fixed")
    assert_type(fixed, BdDbl3Mult)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    multi = nodes.create.bdDbl3_MultMulti(name="multi")
    assert_type(multi, BdDbl3MultMulti)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[next], MultiInputPlugOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)

    existing_fixed = nodes.existing.bdDbl3_Mult("existing_fixed")
    assert_type(existing_fixed, BdDbl3Mult)
    existing_multi = nodes.existing.bdDbl3_MultMulti("existing_multi")
    assert_type(existing_multi, BdDbl3MultMulti)

    double_fixed = nodes.create.bdDbl_Mult(name="double_fixed")
    assert_type(double_fixed, BdDblMult)
    assert_type(double_fixed.input1, DoublePlugOperator)
    assert_type(double_fixed.input2, DoublePlugOperator)
    assert_type(double_fixed.output, DoublePlugOperator)
    assert_type(double_fixed.output.get(), float)

    double_multi = nodes.create.bdDbl_MultMulti(name="double_multi")
    assert_type(double_multi, BdDblMultMulti)
    assert_type(double_multi.input, DoublePlugOperator)
    assert_type(double_multi.input[next], DoublePlugOperator)
    assert_type(double_multi.output, DoublePlugOperator)
    assert_type(double_multi.output.get(), float)

    existing_double_fixed = nodes.existing.bdDbl_Mult("existing_double_fixed")
    assert_type(existing_double_fixed, BdDblMult)
    existing_double_multi = nodes.existing.bdDbl_MultMulti(
        "existing_double_multi"
    )
    assert_type(existing_double_multi, BdDblMultMulti)

    double_add_fixed = nodes.create.bdDbl_Add(name="double_add_fixed")
    assert_type(double_add_fixed, BdDblAdd)
    assert_type(double_add_fixed.input1, DoublePlugOperator)
    assert_type(double_add_fixed.input2, DoublePlugOperator)
    assert_type(double_add_fixed.output, DoublePlugOperator)
    assert_type(double_add_fixed.output.get(), float)

    double_add_multi = nodes.create.bdDbl_AddMulti(name="double_add_multi")
    assert_type(double_add_multi, BdDblAddMulti)
    assert_type(double_add_multi.input, DoublePlugOperator)
    assert_type(double_add_multi.input[next], DoublePlugOperator)
    assert_type(double_add_multi.output, DoublePlugOperator)
    assert_type(double_add_multi.output.get(), float)

    existing_double_add_fixed = nodes.existing.bdDbl_Add(
        "existing_double_add_fixed"
    )
    assert_type(existing_double_add_fixed, BdDblAdd)
    existing_double_add_multi = nodes.existing.bdDbl_AddMulti(
        "existing_double_add_multi"
    )
    assert_type(existing_double_add_multi, BdDblAddMulti)

    double_min_fixed = nodes.create.bdDbl_Min(name="double_min_fixed")
    assert_type(double_min_fixed, BdDblMin)
    assert_type(double_min_fixed.input1, DoublePlugOperator)
    assert_type(double_min_fixed.input2, DoublePlugOperator)
    assert_type(double_min_fixed.output, DoublePlugOperator)
    assert_type(double_min_fixed.output.get(), float)

    double_min_multi = nodes.create.bdDbl_MinMulti(name="double_min_multi")
    assert_type(double_min_multi, BdDblMinMulti)
    assert_type(double_min_multi.input, DoublePlugOperator)
    assert_type(double_min_multi.input[next], DoublePlugOperator)
    assert_type(double_min_multi.output, DoublePlugOperator)
    assert_type(double_min_multi.output.get(), float)

    assert_type(nodes.existing.bdDbl_Min("existing_double_min"), BdDblMin)
    assert_type(
        nodes.existing.bdDbl_MinMulti("existing_double_min_multi"),
        BdDblMinMulti,
    )

    double_max_fixed = nodes.create.bdDbl_Max(name="double_max_fixed")
    assert_type(double_max_fixed, BdDblMax)
    assert_type(double_max_fixed.input1, DoublePlugOperator)
    assert_type(double_max_fixed.input2, DoublePlugOperator)
    assert_type(double_max_fixed.output, DoublePlugOperator)
    assert_type(double_max_fixed.output.get(), float)

    double_max_multi = nodes.create.bdDbl_MaxMulti(name="double_max_multi")
    assert_type(double_max_multi, BdDblMaxMulti)
    assert_type(double_max_multi.input, DoublePlugOperator)
    assert_type(double_max_multi.input[next], DoublePlugOperator)
    assert_type(double_max_multi.output, DoublePlugOperator)
    assert_type(double_max_multi.output.get(), float)

    assert_type(nodes.existing.bdDbl_Max("existing_double_max"), BdDblMax)
    assert_type(
        nodes.existing.bdDbl_MaxMulti("existing_double_max_multi"),
        BdDblMaxMulti,
    )

    double_div_fixed = nodes.create.bdDbl_Div(name="double_div_fixed")
    assert_type(double_div_fixed, BdDblDiv)
    assert_type(double_div_fixed.input1, DoublePlugOperator)
    assert_type(double_div_fixed.input2, DoublePlugOperator)
    assert_type(double_div_fixed.output, DoublePlugOperator)
    assert_type(double_div_fixed.output.get(), float)

    double_div_multi = nodes.create.bdDbl_DivMulti(name="double_div_multi")
    assert_type(double_div_multi, BdDblDivMulti)
    assert_type(double_div_multi.input, DoublePlugOperator)
    assert_type(double_div_multi.input[next], DoublePlugOperator)
    assert_type(double_div_multi.output, DoublePlugOperator)
    assert_type(double_div_multi.output.get(), float)

    existing_double_div_fixed = nodes.existing.bdDbl_Div(
        "existing_double_div_fixed"
    )
    assert_type(existing_double_div_fixed, BdDblDiv)
    existing_double_div_multi = nodes.existing.bdDbl_DivMulti(
        "existing_double_div_multi"
    )
    assert_type(existing_double_div_multi, BdDblDivMulti)

    double_value = nodes.create.bdDbl_Value(name="double_value")
    assert_type(double_value, BdDblValue)
    assert_type(double_value.value, DoublePlugOperator)
    assert_type(double_value.value.get(), float)
    existing_double_value = nodes.existing.bdDbl_Value("existing_double_value")
    assert_type(existing_double_value, BdDblValue)

    double_pow_fixed = nodes.create.bdDbl_Pow(name="double_pow_fixed")
    assert_type(double_pow_fixed, BdDblPow)
    assert_type(double_pow_fixed.input1, DoublePlugOperator)
    assert_type(double_pow_fixed.input2, DoublePlugOperator)
    assert_type(double_pow_fixed.output, DoublePlugOperator)
    assert_type(double_pow_fixed.output.get(), float)

    double_pow_multi = nodes.create.bdDbl_PowMulti(name="double_pow_multi")
    assert_type(double_pow_multi, BdDblPowMulti)
    assert_type(double_pow_multi.input, DoublePlugOperator)
    assert_type(double_pow_multi.input[next], DoublePlugOperator)
    assert_type(double_pow_multi.output, DoublePlugOperator)
    assert_type(double_pow_multi.output.get(), float)

    existing_double_pow_fixed = nodes.existing.bdDbl_Pow(
        "existing_double_pow_fixed"
    )
    assert_type(existing_double_pow_fixed, BdDblPow)
    existing_double_pow_multi = nodes.existing.bdDbl_PowMulti(
        "existing_double_pow_multi"
    )
    assert_type(existing_double_pow_multi, BdDblPowMulti)

    double_sub_fixed = nodes.create.bdDbl_Sub(name="double_sub_fixed")
    assert_type(double_sub_fixed, BdDblSub)
    assert_type(double_sub_fixed.input1, DoublePlugOperator)
    assert_type(double_sub_fixed.input2, DoublePlugOperator)
    assert_type(double_sub_fixed.output, DoublePlugOperator)
    assert_type(double_sub_fixed.output.get(), float)

    double_sub_multi = nodes.create.bdDbl_SubMulti(name="double_sub_multi")
    assert_type(double_sub_multi, BdDblSubMulti)
    assert_type(double_sub_multi.input, DoublePlugOperator)
    assert_type(double_sub_multi.input[next], DoublePlugOperator)
    assert_type(double_sub_multi.output, DoublePlugOperator)
    assert_type(double_sub_multi.output.get(), float)

    existing_double_sub_fixed = nodes.existing.bdDbl_Sub(
        "existing_double_sub_fixed"
    )
    assert_type(existing_double_sub_fixed, BdDblSub)
    existing_double_sub_multi = nodes.existing.bdDbl_SubMulti(
        "existing_double_sub_multi"
    )
    assert_type(existing_double_sub_multi, BdDblSubMulti)

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


def bd_dbl3_add_descriptor_contract(
    fixed: BdDbl3Add,
    multi: BdDbl3AddMulti,
) -> None:
    assert_type(BdDbl3Add.input1, AddInput1AttrOperator)
    assert_type(fixed.input1, AddInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Add.input2, AddInput2AttrOperator)
    assert_type(fixed.input2, AddInput2PlugOperator)
    assert_type(BdDbl3Add.output, AddOutputAttrOperator)
    assert_type(fixed.output, AddOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3AddMulti.input, AddMultiInputAttrOperator)
    assert_type(multi.input, AddMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3AddMulti.output, AddMultiOutputAttrOperator)
    assert_type(multi.output, AddMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_add_descriptor_contract(
    fixed: BdDblAdd,
    multi: BdDblAddMulti,
) -> None:
    assert_type(BdDblAdd.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblAdd.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblAdd.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblAddMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblAddMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_dbl3_div_descriptor_contract(
    fixed: BdDbl3Div,
    multi: BdDbl3DivMulti,
) -> None:
    assert_type(BdDbl3Div.input1, DivInput1AttrOperator)
    assert_type(fixed.input1, DivInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Div.input2, DivInput2AttrOperator)
    assert_type(fixed.input2, DivInput2PlugOperator)
    assert_type(BdDbl3Div.output, DivOutputAttrOperator)
    assert_type(fixed.output, DivOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3DivMulti.input, DivMultiInputAttrOperator)
    assert_type(multi.input, DivMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3DivMulti.output, DivMultiOutputAttrOperator)
    assert_type(multi.output, DivMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_div_descriptor_contract(
    fixed: BdDblDiv,
    multi: BdDblDivMulti,
) -> None:
    assert_type(BdDblDiv.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblDiv.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblDiv.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblDivMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblDivMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_dbl3_value_descriptor_contract(node: BdDbl3Value) -> None:
    assert_type(BdDbl3Value.value, Double3ValueAttrOperator)
    assert_type(node.value, Double3ValuePlugOperator)
    assert_type(node.value.valueX.get(), float)
    assert_type(node.value.get(), bdu.Double3)


def bd_dbl_value_descriptor_contract(node: BdDblValue) -> None:
    assert_type(BdDblValue.value, DoubleAttrOperator)
    assert_type(node.value, DoublePlugOperator)
    assert_type(node.value.get(), float)


def bd_dbl3_pow_descriptor_contract(
    fixed: BdDbl3Pow,
    multi: BdDbl3PowMulti,
) -> None:
    assert_type(BdDbl3Pow.input1, PowInput1AttrOperator)
    assert_type(fixed.input1, PowInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Pow.input2, PowInput2AttrOperator)
    assert_type(fixed.input2, PowInput2PlugOperator)
    assert_type(BdDbl3Pow.output, PowOutputAttrOperator)
    assert_type(fixed.output, PowOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3PowMulti.input, PowMultiInputAttrOperator)
    assert_type(multi.input, PowMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3PowMulti.output, PowMultiOutputAttrOperator)
    assert_type(multi.output, PowMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_pow_descriptor_contract(
    fixed: BdDblPow,
    multi: BdDblPowMulti,
) -> None:
    assert_type(BdDblPow.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblPow.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblPow.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblPowMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblPowMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_dbl3_sub_descriptor_contract(
    fixed: BdDbl3Sub,
    multi: BdDbl3SubMulti,
) -> None:
    assert_type(BdDbl3Sub.input1, SubInput1AttrOperator)
    assert_type(fixed.input1, SubInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Sub.input2, SubInput2AttrOperator)
    assert_type(fixed.input2, SubInput2PlugOperator)
    assert_type(BdDbl3Sub.output, SubOutputAttrOperator)
    assert_type(fixed.output, SubOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3SubMulti.input, SubMultiInputAttrOperator)
    assert_type(multi.input, SubMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3SubMulti.output, SubMultiOutputAttrOperator)
    assert_type(multi.output, SubMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_sub_descriptor_contract(
    fixed: BdDblSub,
    multi: BdDblSubMulti,
) -> None:
    assert_type(BdDblSub.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblSub.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblSub.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblSubMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblSubMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_dbl3_mult_descriptor_contract(fixed: BdDbl3Mult) -> None:
    assert_type(BdDbl3Mult.input1, Input1AttrOperator)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Mult.input2, Input2AttrOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.input2.input2Z.get(), float)
    assert_type(BdDbl3Mult.output, FixedOutputAttrOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)


def bd_dbl3_mult_multi_descriptor_contract(
    multi: BdDbl3MultMulti,
) -> None:
    assert_type(BdDbl3MultMulti.input, MultiInputAttrOperator)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3MultMulti.output, MultiOutputAttrOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_mult_descriptor_contract(
    fixed: BdDblMult,
    multi: BdDblMultMulti,
) -> None:
    assert_type(BdDblMult.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(fixed.input1.get(), float)
    assert_type(BdDblMult.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblMult.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblMultMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblMultMulti.output, DoubleAttrOperator)
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
