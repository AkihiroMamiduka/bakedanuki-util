from typing import Literal, assert_type

import bd_util as bdu
from maya.api import OpenMaya as om

from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_add import (
    Input1AttrOperator as AddInput1AttrOperator,
    Input1PlugOperator as AddInput1PlugOperator,
    Input2AttrOperator as AddInput2AttrOperator,
    Input2PlugOperator as AddInput2PlugOperator,
    OutputAttrOperator as AddOutputAttrOperator,
    OutputPlugOperator as AddOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_add_multi import (
    InputAttrOperator as AddMultiInputAttrOperator,
    InputPlugOperator as AddMultiInputPlugOperator,
    OutputAttrOperator as AddMultiOutputAttrOperator,
    OutputPlugOperator as AddMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_div import (
    Input1AttrOperator as DivInput1AttrOperator,
    Input1PlugOperator as DivInput1PlugOperator,
    Input2AttrOperator as DivInput2AttrOperator,
    Input2PlugOperator as DivInput2PlugOperator,
    OutputAttrOperator as DivOutputAttrOperator,
    OutputPlugOperator as DivOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_div_multi import (
    InputAttrOperator as DivMultiInputAttrOperator,
    InputPlugOperator as DivMultiInputPlugOperator,
    OutputAttrOperator as DivMultiOutputAttrOperator,
    OutputPlugOperator as DivMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_mult import (
    Input1AttrOperator,
    Input1PlugOperator,
    Input2AttrOperator,
    Input2PlugOperator,
    OutputAttrOperator as FixedOutputAttrOperator,
    OutputPlugOperator as FixedOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_mult_multi import (
    InputAttrOperator as MultiInputAttrOperator,
    InputPlugOperator as MultiInputPlugOperator,
    OutputAttrOperator as MultiOutputAttrOperator,
    OutputPlugOperator as MultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_sub import (
    Input1AttrOperator as SubInput1AttrOperator,
    Input1PlugOperator as SubInput1PlugOperator,
    Input2AttrOperator as SubInput2AttrOperator,
    Input2PlugOperator as SubInput2PlugOperator,
    OutputAttrOperator as SubOutputAttrOperator,
    OutputPlugOperator as SubOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_double3_sub_multi import (
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
from bd_util.maya.node.operator.node.dg.bd_double3_add import BdDouble3Add
from bd_util.maya.node.operator.node.dg.bd_double3_add_multi import (
    BdDouble3AddMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double3_div import BdDouble3Div
from bd_util.maya.node.operator.node.dg.bd_double3_div_multi import (
    BdDouble3DivMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double3_mult import BdDouble3Mult
from bd_util.maya.node.operator.node.dg.bd_double3_mult_multi import (
    BdDouble3MultMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double3_sub import BdDouble3Sub
from bd_util.maya.node.operator.node.dg.bd_double3_sub_multi import (
    BdDouble3SubMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double_mult import BdDoubleMult
from bd_util.maya.node.operator.node.dg.bd_double_mult_multi import (
    BdDoubleMultMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double_add import BdDoubleAdd
from bd_util.maya.node.operator.node.dg.bd_double_add_multi import (
    BdDoubleAddMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double_div import BdDoubleDiv
from bd_util.maya.node.operator.node.dg.bd_double_div_multi import (
    BdDoubleDivMulti,
)
from bd_util.maya.node.operator.node.dg.bd_double_sub import BdDoubleSub
from bd_util.maya.node.operator.node.dg.bd_double_sub_multi import (
    BdDoubleSubMulti,
)
from bd_util.maya.node.operator.node.dg.compose_matrix import ComposeMatrix
from bd_util.maya.node.operator.node.dg.decompose_matrix import (
    DecomposeMatrix,
)
from bd_util.maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix


def node_accessor_contract(nodes: bdu.Nodes) -> None:
    add_fixed = nodes.create.bdDouble3Add(name="add_fixed")
    assert_type(add_fixed, BdDouble3Add)
    assert_type(add_fixed.input1, AddInput1PlugOperator)
    assert_type(add_fixed.input2, AddInput2PlugOperator)
    assert_type(add_fixed.output, AddOutputPlugOperator)
    assert_type(add_fixed.output.get(), bdu.Double3)

    add_multi = nodes.create.bdDouble3AddMulti(name="add_multi")
    assert_type(add_multi, BdDouble3AddMulti)
    assert_type(add_multi.input, AddMultiInputPlugOperator)
    assert_type(add_multi.input[next], AddMultiInputPlugOperator)
    assert_type(add_multi.output, AddMultiOutputPlugOperator)
    assert_type(add_multi.output.get(), bdu.Double3)

    existing_add_fixed = nodes.existing.bdDouble3Add("existing_add_fixed")
    assert_type(existing_add_fixed, BdDouble3Add)
    existing_add_multi = nodes.existing.bdDouble3AddMulti("existing_add_multi")
    assert_type(existing_add_multi, BdDouble3AddMulti)

    div_fixed = nodes.create.bdDouble3Div(name="div_fixed")
    assert_type(div_fixed, BdDouble3Div)
    assert_type(div_fixed.input1, DivInput1PlugOperator)
    assert_type(div_fixed.input2, DivInput2PlugOperator)
    assert_type(div_fixed.output, DivOutputPlugOperator)
    assert_type(div_fixed.output.get(), bdu.Double3)

    div_multi = nodes.create.bdDouble3DivMulti(name="div_multi")
    assert_type(div_multi, BdDouble3DivMulti)
    assert_type(div_multi.input, DivMultiInputPlugOperator)
    assert_type(div_multi.input[next], DivMultiInputPlugOperator)
    assert_type(div_multi.output, DivMultiOutputPlugOperator)
    assert_type(div_multi.output.get(), bdu.Double3)

    existing_div_fixed = nodes.existing.bdDouble3Div("existing_div_fixed")
    assert_type(existing_div_fixed, BdDouble3Div)
    existing_div_multi = nodes.existing.bdDouble3DivMulti("existing_div_multi")
    assert_type(existing_div_multi, BdDouble3DivMulti)

    sub_fixed = nodes.create.bdDouble3Sub(name="sub_fixed")
    assert_type(sub_fixed, BdDouble3Sub)
    assert_type(sub_fixed.input1, SubInput1PlugOperator)
    assert_type(sub_fixed.input2, SubInput2PlugOperator)
    assert_type(sub_fixed.output, SubOutputPlugOperator)
    assert_type(sub_fixed.output.get(), bdu.Double3)

    sub_multi = nodes.create.bdDouble3SubMulti(name="sub_multi")
    assert_type(sub_multi, BdDouble3SubMulti)
    assert_type(sub_multi.input, SubMultiInputPlugOperator)
    assert_type(sub_multi.input[next], SubMultiInputPlugOperator)
    assert_type(sub_multi.output, SubMultiOutputPlugOperator)
    assert_type(sub_multi.output.get(), bdu.Double3)

    existing_sub_fixed = nodes.existing.bdDouble3Sub("existing_sub_fixed")
    assert_type(existing_sub_fixed, BdDouble3Sub)
    existing_sub_multi = nodes.existing.bdDouble3SubMulti("existing_sub_multi")
    assert_type(existing_sub_multi, BdDouble3SubMulti)

    fixed = nodes.create.bdDouble3Mult(name="fixed")
    assert_type(fixed, BdDouble3Mult)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    multi = nodes.create.bdDouble3MultMulti(name="multi")
    assert_type(multi, BdDouble3MultMulti)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[next], MultiInputPlugOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)

    existing_fixed = nodes.existing.bdDouble3Mult("existing_fixed")
    assert_type(existing_fixed, BdDouble3Mult)
    existing_multi = nodes.existing.bdDouble3MultMulti("existing_multi")
    assert_type(existing_multi, BdDouble3MultMulti)

    double_fixed = nodes.create.bdDoubleMult(name="double_fixed")
    assert_type(double_fixed, BdDoubleMult)
    assert_type(double_fixed.input1, DoublePlugOperator)
    assert_type(double_fixed.input2, DoublePlugOperator)
    assert_type(double_fixed.output, DoublePlugOperator)
    assert_type(double_fixed.output.get(), float)

    double_multi = nodes.create.bdDoubleMultMulti(name="double_multi")
    assert_type(double_multi, BdDoubleMultMulti)
    assert_type(double_multi.input, DoublePlugOperator)
    assert_type(double_multi.input[next], DoublePlugOperator)
    assert_type(double_multi.output, DoublePlugOperator)
    assert_type(double_multi.output.get(), float)

    existing_double_fixed = nodes.existing.bdDoubleMult(
        "existing_double_fixed"
    )
    assert_type(existing_double_fixed, BdDoubleMult)
    existing_double_multi = nodes.existing.bdDoubleMultMulti(
        "existing_double_multi"
    )
    assert_type(existing_double_multi, BdDoubleMultMulti)

    double_add_fixed = nodes.create.bdDoubleAdd(name="double_add_fixed")
    assert_type(double_add_fixed, BdDoubleAdd)
    assert_type(double_add_fixed.input1, DoublePlugOperator)
    assert_type(double_add_fixed.input2, DoublePlugOperator)
    assert_type(double_add_fixed.output, DoublePlugOperator)
    assert_type(double_add_fixed.output.get(), float)

    double_add_multi = nodes.create.bdDoubleAddMulti(name="double_add_multi")
    assert_type(double_add_multi, BdDoubleAddMulti)
    assert_type(double_add_multi.input, DoublePlugOperator)
    assert_type(double_add_multi.input[next], DoublePlugOperator)
    assert_type(double_add_multi.output, DoublePlugOperator)
    assert_type(double_add_multi.output.get(), float)

    existing_double_add_fixed = nodes.existing.bdDoubleAdd(
        "existing_double_add_fixed"
    )
    assert_type(existing_double_add_fixed, BdDoubleAdd)
    existing_double_add_multi = nodes.existing.bdDoubleAddMulti(
        "existing_double_add_multi"
    )
    assert_type(existing_double_add_multi, BdDoubleAddMulti)

    double_div_fixed = nodes.create.bdDoubleDiv(name="double_div_fixed")
    assert_type(double_div_fixed, BdDoubleDiv)
    assert_type(double_div_fixed.input1, DoublePlugOperator)
    assert_type(double_div_fixed.input2, DoublePlugOperator)
    assert_type(double_div_fixed.output, DoublePlugOperator)
    assert_type(double_div_fixed.output.get(), float)

    double_div_multi = nodes.create.bdDoubleDivMulti(name="double_div_multi")
    assert_type(double_div_multi, BdDoubleDivMulti)
    assert_type(double_div_multi.input, DoublePlugOperator)
    assert_type(double_div_multi.input[next], DoublePlugOperator)
    assert_type(double_div_multi.output, DoublePlugOperator)
    assert_type(double_div_multi.output.get(), float)

    existing_double_div_fixed = nodes.existing.bdDoubleDiv(
        "existing_double_div_fixed"
    )
    assert_type(existing_double_div_fixed, BdDoubleDiv)
    existing_double_div_multi = nodes.existing.bdDoubleDivMulti(
        "existing_double_div_multi"
    )
    assert_type(existing_double_div_multi, BdDoubleDivMulti)

    double_sub_fixed = nodes.create.bdDoubleSub(name="double_sub_fixed")
    assert_type(double_sub_fixed, BdDoubleSub)
    assert_type(double_sub_fixed.input1, DoublePlugOperator)
    assert_type(double_sub_fixed.input2, DoublePlugOperator)
    assert_type(double_sub_fixed.output, DoublePlugOperator)
    assert_type(double_sub_fixed.output.get(), float)

    double_sub_multi = nodes.create.bdDoubleSubMulti(name="double_sub_multi")
    assert_type(double_sub_multi, BdDoubleSubMulti)
    assert_type(double_sub_multi.input, DoublePlugOperator)
    assert_type(double_sub_multi.input[next], DoublePlugOperator)
    assert_type(double_sub_multi.output, DoublePlugOperator)
    assert_type(double_sub_multi.output.get(), float)

    existing_double_sub_fixed = nodes.existing.bdDoubleSub(
        "existing_double_sub_fixed"
    )
    assert_type(existing_double_sub_fixed, BdDoubleSub)
    existing_double_sub_multi = nodes.existing.bdDoubleSubMulti(
        "existing_double_sub_multi"
    )
    assert_type(existing_double_sub_multi, BdDoubleSubMulti)

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


def bd_double3_add_descriptor_contract(
    fixed: BdDouble3Add,
    multi: BdDouble3AddMulti,
) -> None:
    assert_type(BdDouble3Add.input1, AddInput1AttrOperator)
    assert_type(fixed.input1, AddInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDouble3Add.input2, AddInput2AttrOperator)
    assert_type(fixed.input2, AddInput2PlugOperator)
    assert_type(BdDouble3Add.output, AddOutputAttrOperator)
    assert_type(fixed.output, AddOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDouble3AddMulti.input, AddMultiInputAttrOperator)
    assert_type(multi.input, AddMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDouble3AddMulti.output, AddMultiOutputAttrOperator)
    assert_type(multi.output, AddMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_double_add_descriptor_contract(
    fixed: BdDoubleAdd,
    multi: BdDoubleAddMulti,
) -> None:
    assert_type(BdDoubleAdd.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDoubleAdd.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDoubleAdd.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDoubleAddMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDoubleAddMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_double3_div_descriptor_contract(
    fixed: BdDouble3Div,
    multi: BdDouble3DivMulti,
) -> None:
    assert_type(BdDouble3Div.input1, DivInput1AttrOperator)
    assert_type(fixed.input1, DivInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDouble3Div.input2, DivInput2AttrOperator)
    assert_type(fixed.input2, DivInput2PlugOperator)
    assert_type(BdDouble3Div.output, DivOutputAttrOperator)
    assert_type(fixed.output, DivOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDouble3DivMulti.input, DivMultiInputAttrOperator)
    assert_type(multi.input, DivMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDouble3DivMulti.output, DivMultiOutputAttrOperator)
    assert_type(multi.output, DivMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_double_div_descriptor_contract(
    fixed: BdDoubleDiv,
    multi: BdDoubleDivMulti,
) -> None:
    assert_type(BdDoubleDiv.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDoubleDiv.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDoubleDiv.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDoubleDivMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDoubleDivMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_double3_sub_descriptor_contract(
    fixed: BdDouble3Sub,
    multi: BdDouble3SubMulti,
) -> None:
    assert_type(BdDouble3Sub.input1, SubInput1AttrOperator)
    assert_type(fixed.input1, SubInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDouble3Sub.input2, SubInput2AttrOperator)
    assert_type(fixed.input2, SubInput2PlugOperator)
    assert_type(BdDouble3Sub.output, SubOutputAttrOperator)
    assert_type(fixed.output, SubOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDouble3SubMulti.input, SubMultiInputAttrOperator)
    assert_type(multi.input, SubMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDouble3SubMulti.output, SubMultiOutputAttrOperator)
    assert_type(multi.output, SubMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_double_sub_descriptor_contract(
    fixed: BdDoubleSub,
    multi: BdDoubleSubMulti,
) -> None:
    assert_type(BdDoubleSub.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDoubleSub.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDoubleSub.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDoubleSubMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDoubleSubMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_double3_mult_descriptor_contract(fixed: BdDouble3Mult) -> None:
    assert_type(BdDouble3Mult.input1, Input1AttrOperator)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDouble3Mult.input2, Input2AttrOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.input2.input2Z.get(), float)
    assert_type(BdDouble3Mult.output, FixedOutputAttrOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)


def bd_double3_mult_multi_descriptor_contract(
    multi: BdDouble3MultMulti,
) -> None:
    assert_type(BdDouble3MultMulti.input, MultiInputAttrOperator)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDouble3MultMulti.output, MultiOutputAttrOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_double_mult_descriptor_contract(
    fixed: BdDoubleMult,
    multi: BdDoubleMultMulti,
) -> None:
    assert_type(BdDoubleMult.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(fixed.input1.get(), float)
    assert_type(BdDoubleMult.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDoubleMult.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDoubleMultMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDoubleMultMulti.output, DoubleAttrOperator)
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
