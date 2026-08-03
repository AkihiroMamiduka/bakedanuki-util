from typing import Literal, assert_type

import bd_util as bdu
from maya.api import OpenMaya as om

from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_abs import (
    InputAttrOperator as AbsInputAttrOperator,
    InputPlugOperator as AbsInputPlugOperator,
    OutputAttrOperator as AbsOutputAttrOperator,
    OutputPlugOperator as AbsOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_negate import (
    InputAttrOperator as NegInputAttrOperator,
    InputPlugOperator as NegInputPlugOperator,
    OutputAttrOperator as NegOutputAttrOperator,
    OutputPlugOperator as NegOutputPlugOperator,
)
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
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_clamp import (
    InputAttrOperator as ClampInputAttrOperator,
    InputPlugOperator as ClampInputPlugOperator,
    MaxAttrOperator as ClampMaxAttrOperator,
    MaxPlugOperator as ClampMaxPlugOperator,
    MinAttrOperator as ClampMinAttrOperator,
    MinPlugOperator as ClampMinPlugOperator,
    OutputAttrOperator as ClampOutputAttrOperator,
    OutputPlugOperator as ClampOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_map_range import (
    InputAttrOperator as MapRangeInputAttrOperator,
    InputPlugOperator as MapRangeInputPlugOperator,
    OutputAttrOperator as MapRangeOutputAttrOperator,
    OutputPlugOperator as MapRangeOutputPlugOperator,
    DstMaxAttrOperator as MapRangeDstMaxAttrOperator,
    DstMaxPlugOperator as MapRangeDstMaxPlugOperator,
    DstMinAttrOperator as MapRangeDstMinAttrOperator,
    DstMinPlugOperator as MapRangeDstMinPlugOperator,
    SrcMaxAttrOperator as MapRangeSrcMaxAttrOperator,
    SrcMaxPlugOperator as MapRangeSrcMaxPlugOperator,
    SrcMinAttrOperator as MapRangeSrcMinAttrOperator,
    SrcMinPlugOperator as MapRangeSrcMinPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_divide import (
    Input1AttrOperator as DivInput1AttrOperator,
    Input1PlugOperator as DivInput1PlugOperator,
    Input2AttrOperator as DivInput2AttrOperator,
    Input2PlugOperator as DivInput2PlugOperator,
    OutputAttrOperator as DivOutputAttrOperator,
    OutputPlugOperator as DivOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_divide_multi import (
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
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_multiply import (
    Input1AttrOperator,
    Input1PlugOperator,
    Input2AttrOperator,
    Input2PlugOperator,
    OutputAttrOperator as FixedOutputAttrOperator,
    OutputPlugOperator as FixedOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_multiply_multi import (
    InputAttrOperator as MultiInputAttrOperator,
    InputPlugOperator as MultiInputPlugOperator,
    OutputAttrOperator as MultiOutputAttrOperator,
    OutputPlugOperator as MultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_power import (
    Input1AttrOperator as PowInput1AttrOperator,
    Input1PlugOperator as PowInput1PlugOperator,
    Input2AttrOperator as PowInput2AttrOperator,
    Input2PlugOperator as PowInput2PlugOperator,
    OutputAttrOperator as PowOutputAttrOperator,
    OutputPlugOperator as PowOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_power_multi import (
    InputAttrOperator as PowMultiInputAttrOperator,
    InputPlugOperator as PowMultiInputPlugOperator,
    OutputAttrOperator as PowMultiOutputAttrOperator,
    OutputPlugOperator as PowMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_subtract import (
    Input1AttrOperator as SubInput1AttrOperator,
    Input1PlugOperator as SubInput1PlugOperator,
    Input2AttrOperator as SubInput2AttrOperator,
    Input2PlugOperator as SubInput2PlugOperator,
    OutputAttrOperator as SubOutputAttrOperator,
    OutputPlugOperator as SubOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_subtract_multi import (
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
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolAttrOperator,
    BoolPlugOperator,
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
from bd_util.maya.node.operator.node.dg.bd_dbl3_abs import BdDbl3Abs
from bd_util.maya.node.operator.node.dg.bd_dbl3_add import (
    BdDbl3Add,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_add_multi import (
    BdDbl3AddMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_clamp import BdDbl3Clamp
from bd_util.maya.node.operator.node.dg.bd_dbl3_map_range import (
    BdDbl3MapRange,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_divide import (
    BdDbl3Divide,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_divide_multi import (
    BdDbl3DivideMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_max import BdDbl3Max
from bd_util.maya.node.operator.node.dg.bd_dbl3_max_multi import BdDbl3MaxMulti
from bd_util.maya.node.operator.node.dg.bd_dbl3_min import BdDbl3Min
from bd_util.maya.node.operator.node.dg.bd_dbl3_min_multi import BdDbl3MinMulti
from bd_util.maya.node.operator.node.dg.bd_dbl3_negate import BdDbl3Negate
from bd_util.maya.node.operator.node.dg.bd_dbl3_value import BdDbl3Value
from bd_util.maya.node.operator.node.dg.bd_dbl3_multiply import (
    BdDbl3Multiply,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_multiply_multi import (
    BdDbl3MultiplyMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_power import (
    BdDbl3Power,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_power_multi import (
    BdDbl3PowerMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_subtract import (
    BdDbl3Subtract,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_subtract_multi import (
    BdDbl3SubtractMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_abs import BdDblAbs
from bd_util.maya.node.operator.node.dg.bd_dbl_multiply import (
    BdDblMultiply,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_multiply_multi import (
    BdDblMultiplyMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_power import (
    BdDblPower,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_power_multi import (
    BdDblPowerMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_add import (
    BdDblAdd,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_add_multi import (
    BdDblAddMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_clamp import BdDblClamp
from bd_util.maya.node.operator.node.dg.bd_dbl_map_range import BdDblMapRange
from bd_util.maya.node.operator.node.dg.bd_dbl_divide import (
    BdDblDivide,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_divide_multi import (
    BdDblDivideMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_max import BdDblMax
from bd_util.maya.node.operator.node.dg.bd_dbl_max_multi import BdDblMaxMulti
from bd_util.maya.node.operator.node.dg.bd_dbl_min import BdDblMin
from bd_util.maya.node.operator.node.dg.bd_dbl_min_multi import BdDblMinMulti
from bd_util.maya.node.operator.node.dg.bd_dbl_negate import BdDblNegate
from bd_util.maya.node.operator.node.dg.bd_dbl_value import BdDblValue
from bd_util.maya.node.operator.node.dg.bd_dbl_subtract import (
    BdDblSubtract,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_subtract_multi import (
    BdDblSubtractMulti,
)
from bd_util.maya.node.operator.node.dg.compose_matrix import ComposeMatrix
from bd_util.maya.node.operator.node.dg.decompose_matrix import (
    DecomposeMatrix,
)
from bd_util.maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix


def node_accessor_contract(nodes: bdu.Nodes) -> None:
    absolute = nodes.create.bdDbl3_Abs(name="absolute")
    assert_type(absolute, BdDbl3Abs)
    assert_type(absolute.input, AbsInputPlugOperator)
    assert_type(absolute.output, AbsOutputPlugOperator)
    assert_type(absolute.output.get(), bdu.Double3)
    assert_type(nodes.existing.bdDbl3_Abs("existing_absolute"), BdDbl3Abs)

    negate = nodes.create.bdDbl3_Negate(name="negate")
    assert_type(negate, BdDbl3Negate)
    assert_type(negate.input, NegInputPlugOperator)
    assert_type(negate.output, NegOutputPlugOperator)
    assert_type(negate.output.get(), bdu.Double3)
    assert_type(nodes.existing.bdDbl3_Negate("existing_negate"), BdDbl3Negate)

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

    clamp = nodes.create.bdDbl3_Clamp(name="clamp")
    assert_type(clamp, BdDbl3Clamp)
    assert_type(clamp.input, ClampInputPlugOperator)
    assert_type(clamp.min, ClampMinPlugOperator)
    assert_type(clamp.max, ClampMaxPlugOperator)
    assert_type(clamp.output, ClampOutputPlugOperator)
    assert_type(clamp.output.get(), bdu.Double3)
    assert_type(nodes.existing.bdDbl3_Clamp("existing_clamp"), BdDbl3Clamp)

    map_range = nodes.create.bdDbl3_MapRange(name="map_range")
    assert_type(map_range, BdDbl3MapRange)
    assert_type(map_range.input, MapRangeInputPlugOperator)
    assert_type(map_range.srcMin, MapRangeSrcMinPlugOperator)
    assert_type(map_range.srcMax, MapRangeSrcMaxPlugOperator)
    assert_type(map_range.dstMin, MapRangeDstMinPlugOperator)
    assert_type(map_range.dstMax, MapRangeDstMaxPlugOperator)
    assert_type(map_range.clamp, BoolPlugOperator)
    assert_type(map_range.output, MapRangeOutputPlugOperator)
    assert_type(map_range.output.get(), bdu.Double3)
    assert_type(
        nodes.existing.bdDbl3_MapRange("existing_map_range"),
        BdDbl3MapRange,
    )

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

    div_fixed = nodes.create.bdDbl3_Divide(name="div_fixed")
    assert_type(div_fixed, BdDbl3Divide)
    assert_type(div_fixed.input1, DivInput1PlugOperator)
    assert_type(div_fixed.input2, DivInput2PlugOperator)
    assert_type(div_fixed.output, DivOutputPlugOperator)
    assert_type(div_fixed.output.get(), bdu.Double3)

    div_multi = nodes.create.bdDbl3_DivideMulti(name="div_multi")
    assert_type(div_multi, BdDbl3DivideMulti)
    assert_type(div_multi.input, DivMultiInputPlugOperator)
    assert_type(div_multi.input[next], DivMultiInputPlugOperator)
    assert_type(div_multi.output, DivMultiOutputPlugOperator)
    assert_type(div_multi.output.get(), bdu.Double3)

    existing_div_fixed = nodes.existing.bdDbl3_Divide("existing_div_fixed")
    assert_type(existing_div_fixed, BdDbl3Divide)
    existing_div_multi = nodes.existing.bdDbl3_DivideMulti(
        "existing_div_multi"
    )
    assert_type(existing_div_multi, BdDbl3DivideMulti)

    double3_value = nodes.create.bdDbl3_Value(name="double3_value")
    assert_type(double3_value, BdDbl3Value)
    assert_type(double3_value.value, Double3ValuePlugOperator)
    assert_type(double3_value.value.valueX.get(), float)
    assert_type(double3_value.value.get(), bdu.Double3)
    existing_double3_value = nodes.existing.bdDbl3_Value(
        "existing_double3_value"
    )
    assert_type(existing_double3_value, BdDbl3Value)

    pow_fixed = nodes.create.bdDbl3_Power(name="pow_fixed")
    assert_type(pow_fixed, BdDbl3Power)
    assert_type(pow_fixed.input1, PowInput1PlugOperator)
    assert_type(pow_fixed.input2, PowInput2PlugOperator)
    assert_type(pow_fixed.output, PowOutputPlugOperator)
    assert_type(pow_fixed.output.get(), bdu.Double3)

    pow_multi = nodes.create.bdDbl3_PowerMulti(name="pow_multi")
    assert_type(pow_multi, BdDbl3PowerMulti)
    assert_type(pow_multi.input, PowMultiInputPlugOperator)
    assert_type(pow_multi.input[next], PowMultiInputPlugOperator)
    assert_type(pow_multi.output, PowMultiOutputPlugOperator)
    assert_type(pow_multi.output.get(), bdu.Double3)

    existing_pow_fixed = nodes.existing.bdDbl3_Power("existing_pow_fixed")
    assert_type(existing_pow_fixed, BdDbl3Power)
    existing_pow_multi = nodes.existing.bdDbl3_PowerMulti("existing_pow_multi")
    assert_type(existing_pow_multi, BdDbl3PowerMulti)

    sub_fixed = nodes.create.bdDbl3_Subtract(name="sub_fixed")
    assert_type(sub_fixed, BdDbl3Subtract)
    assert_type(sub_fixed.input1, SubInput1PlugOperator)
    assert_type(sub_fixed.input2, SubInput2PlugOperator)
    assert_type(sub_fixed.output, SubOutputPlugOperator)
    assert_type(sub_fixed.output.get(), bdu.Double3)

    sub_multi = nodes.create.bdDbl3_SubtractMulti(name="sub_multi")
    assert_type(sub_multi, BdDbl3SubtractMulti)
    assert_type(sub_multi.input, SubMultiInputPlugOperator)
    assert_type(sub_multi.input[next], SubMultiInputPlugOperator)
    assert_type(sub_multi.output, SubMultiOutputPlugOperator)
    assert_type(sub_multi.output.get(), bdu.Double3)

    existing_sub_fixed = nodes.existing.bdDbl3_Subtract("existing_sub_fixed")
    assert_type(existing_sub_fixed, BdDbl3Subtract)
    existing_sub_multi = nodes.existing.bdDbl3_SubtractMulti(
        "existing_sub_multi"
    )
    assert_type(existing_sub_multi, BdDbl3SubtractMulti)

    fixed = nodes.create.bdDbl3_Multiply(name="fixed")
    assert_type(fixed, BdDbl3Multiply)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    multi = nodes.create.bdDbl3_MultiplyMulti(name="multi")
    assert_type(multi, BdDbl3MultiplyMulti)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[next], MultiInputPlugOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)

    existing_fixed = nodes.existing.bdDbl3_Multiply("existing_fixed")
    assert_type(existing_fixed, BdDbl3Multiply)
    existing_multi = nodes.existing.bdDbl3_MultiplyMulti("existing_multi")
    assert_type(existing_multi, BdDbl3MultiplyMulti)

    double_absolute = nodes.create.bdDbl_Abs(name="double_absolute")
    assert_type(double_absolute, BdDblAbs)
    assert_type(double_absolute.input, DoublePlugOperator)
    assert_type(double_absolute.output, DoublePlugOperator)
    assert_type(double_absolute.output.get(), float)
    assert_type(
        nodes.existing.bdDbl_Abs("existing_double_absolute"),
        BdDblAbs,
    )

    double_negate = nodes.create.bdDbl_Negate(name="double_negate")
    assert_type(double_negate, BdDblNegate)
    assert_type(double_negate.input, DoublePlugOperator)
    assert_type(double_negate.output, DoublePlugOperator)
    assert_type(double_negate.output.get(), float)
    assert_type(
        nodes.existing.bdDbl_Negate("existing_double_negate"),
        BdDblNegate,
    )

    double_fixed = nodes.create.bdDbl_Multiply(name="double_fixed")
    assert_type(double_fixed, BdDblMultiply)
    assert_type(double_fixed.input1, DoublePlugOperator)
    assert_type(double_fixed.input2, DoublePlugOperator)
    assert_type(double_fixed.output, DoublePlugOperator)
    assert_type(double_fixed.output.get(), float)

    double_multi = nodes.create.bdDbl_MultiplyMulti(name="double_multi")
    assert_type(double_multi, BdDblMultiplyMulti)
    assert_type(double_multi.input, DoublePlugOperator)
    assert_type(double_multi.input[next], DoublePlugOperator)
    assert_type(double_multi.output, DoublePlugOperator)
    assert_type(double_multi.output.get(), float)

    existing_double_fixed = nodes.existing.bdDbl_Multiply(
        "existing_double_fixed"
    )
    assert_type(existing_double_fixed, BdDblMultiply)
    existing_double_multi = nodes.existing.bdDbl_MultiplyMulti(
        "existing_double_multi"
    )
    assert_type(existing_double_multi, BdDblMultiplyMulti)

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

    double_clamp = nodes.create.bdDbl_Clamp(name="double_clamp")
    assert_type(double_clamp, BdDblClamp)
    assert_type(double_clamp.input, DoublePlugOperator)
    assert_type(double_clamp.min, DoublePlugOperator)
    assert_type(double_clamp.max, DoublePlugOperator)
    assert_type(double_clamp.output, DoublePlugOperator)
    assert_type(double_clamp.output.get(), float)
    assert_type(
        nodes.existing.bdDbl_Clamp("existing_double_clamp"),
        BdDblClamp,
    )

    double_map_range = nodes.create.bdDbl_MapRange(name="double_map_range")
    assert_type(double_map_range, BdDblMapRange)
    assert_type(double_map_range.input, DoublePlugOperator)
    assert_type(double_map_range.srcMin, DoublePlugOperator)
    assert_type(double_map_range.srcMax, DoublePlugOperator)
    assert_type(double_map_range.dstMin, DoublePlugOperator)
    assert_type(double_map_range.dstMax, DoublePlugOperator)
    assert_type(double_map_range.clamp, BoolPlugOperator)
    assert_type(double_map_range.output, DoublePlugOperator)
    assert_type(double_map_range.output.get(), float)
    assert_type(
        nodes.existing.bdDbl_MapRange("existing_double_map_range"),
        BdDblMapRange,
    )

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

    double_div_fixed = nodes.create.bdDbl_Divide(name="double_div_fixed")
    assert_type(double_div_fixed, BdDblDivide)
    assert_type(double_div_fixed.input1, DoublePlugOperator)
    assert_type(double_div_fixed.input2, DoublePlugOperator)
    assert_type(double_div_fixed.output, DoublePlugOperator)
    assert_type(double_div_fixed.output.get(), float)

    double_div_multi = nodes.create.bdDbl_DivideMulti(name="double_div_multi")
    assert_type(double_div_multi, BdDblDivideMulti)
    assert_type(double_div_multi.input, DoublePlugOperator)
    assert_type(double_div_multi.input[next], DoublePlugOperator)
    assert_type(double_div_multi.output, DoublePlugOperator)
    assert_type(double_div_multi.output.get(), float)

    existing_double_div_fixed = nodes.existing.bdDbl_Divide(
        "existing_double_div_fixed"
    )
    assert_type(existing_double_div_fixed, BdDblDivide)
    existing_double_div_multi = nodes.existing.bdDbl_DivideMulti(
        "existing_double_div_multi"
    )
    assert_type(existing_double_div_multi, BdDblDivideMulti)

    double_value = nodes.create.bdDbl_Value(name="double_value")
    assert_type(double_value, BdDblValue)
    assert_type(double_value.value, DoublePlugOperator)
    assert_type(double_value.value.get(), float)
    existing_double_value = nodes.existing.bdDbl_Value("existing_double_value")
    assert_type(existing_double_value, BdDblValue)

    double_pow_fixed = nodes.create.bdDbl_Power(name="double_pow_fixed")
    assert_type(double_pow_fixed, BdDblPower)
    assert_type(double_pow_fixed.input1, DoublePlugOperator)
    assert_type(double_pow_fixed.input2, DoublePlugOperator)
    assert_type(double_pow_fixed.output, DoublePlugOperator)
    assert_type(double_pow_fixed.output.get(), float)

    double_pow_multi = nodes.create.bdDbl_PowerMulti(name="double_pow_multi")
    assert_type(double_pow_multi, BdDblPowerMulti)
    assert_type(double_pow_multi.input, DoublePlugOperator)
    assert_type(double_pow_multi.input[next], DoublePlugOperator)
    assert_type(double_pow_multi.output, DoublePlugOperator)
    assert_type(double_pow_multi.output.get(), float)

    existing_double_pow_fixed = nodes.existing.bdDbl_Power(
        "existing_double_pow_fixed"
    )
    assert_type(existing_double_pow_fixed, BdDblPower)
    existing_double_pow_multi = nodes.existing.bdDbl_PowerMulti(
        "existing_double_pow_multi"
    )
    assert_type(existing_double_pow_multi, BdDblPowerMulti)

    double_sub_fixed = nodes.create.bdDbl_Subtract(name="double_sub_fixed")
    assert_type(double_sub_fixed, BdDblSubtract)
    assert_type(double_sub_fixed.input1, DoublePlugOperator)
    assert_type(double_sub_fixed.input2, DoublePlugOperator)
    assert_type(double_sub_fixed.output, DoublePlugOperator)
    assert_type(double_sub_fixed.output.get(), float)

    double_sub_multi = nodes.create.bdDbl_SubtractMulti(
        name="double_sub_multi"
    )
    assert_type(double_sub_multi, BdDblSubtractMulti)
    assert_type(double_sub_multi.input, DoublePlugOperator)
    assert_type(double_sub_multi.input[next], DoublePlugOperator)
    assert_type(double_sub_multi.output, DoublePlugOperator)
    assert_type(double_sub_multi.output.get(), float)

    existing_double_sub_fixed = nodes.existing.bdDbl_Subtract(
        "existing_double_sub_fixed"
    )
    assert_type(existing_double_sub_fixed, BdDblSubtract)
    existing_double_sub_multi = nodes.existing.bdDbl_SubtractMulti(
        "existing_double_sub_multi"
    )
    assert_type(existing_double_sub_multi, BdDblSubtractMulti)

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


def bd_dbl3_abs_descriptor_contract(node: BdDbl3Abs) -> None:
    assert_type(BdDbl3Abs.input, AbsInputAttrOperator)
    assert_type(node.input, AbsInputPlugOperator)
    assert_type(node.input.inputX.get(), float)
    assert_type(BdDbl3Abs.output, AbsOutputAttrOperator)
    assert_type(node.output, AbsOutputPlugOperator)
    assert_type(node.output.get(), bdu.Double3)


def bd_dbl_abs_descriptor_contract(node: BdDblAbs) -> None:
    assert_type(BdDblAbs.input, DoubleAttrOperator)
    assert_type(node.input, DoublePlugOperator)
    assert_type(BdDblAbs.output, DoubleAttrOperator)
    assert_type(node.output, DoublePlugOperator)
    assert_type(node.output.get(), float)


def bd_dbl3_negate_descriptor_contract(node: BdDbl3Negate) -> None:
    assert_type(BdDbl3Negate.input, NegInputAttrOperator)
    assert_type(node.input, NegInputPlugOperator)
    assert_type(node.input.inputX.get(), float)
    assert_type(BdDbl3Negate.output, NegOutputAttrOperator)
    assert_type(node.output, NegOutputPlugOperator)
    assert_type(node.output.get(), bdu.Double3)


def bd_dbl_negate_descriptor_contract(node: BdDblNegate) -> None:
    assert_type(BdDblNegate.input, DoubleAttrOperator)
    assert_type(node.input, DoublePlugOperator)
    assert_type(BdDblNegate.output, DoubleAttrOperator)
    assert_type(node.output, DoublePlugOperator)
    assert_type(node.output.get(), float)


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


def bd_dbl3_clamp_descriptor_contract(node: BdDbl3Clamp) -> None:
    assert_type(BdDbl3Clamp.input, ClampInputAttrOperator)
    assert_type(node.input, ClampInputPlugOperator)
    assert_type(node.input.inputX.get(), float)
    assert_type(BdDbl3Clamp.min, ClampMinAttrOperator)
    assert_type(node.min, ClampMinPlugOperator)
    assert_type(BdDbl3Clamp.max, ClampMaxAttrOperator)
    assert_type(node.max, ClampMaxPlugOperator)
    assert_type(BdDbl3Clamp.output, ClampOutputAttrOperator)
    assert_type(node.output, ClampOutputPlugOperator)
    assert_type(node.output.get(), bdu.Double3)


def bd_dbl_clamp_descriptor_contract(node: BdDblClamp) -> None:
    assert_type(BdDblClamp.input, DoubleAttrOperator)
    assert_type(node.input, DoublePlugOperator)
    assert_type(BdDblClamp.min, DoubleAttrOperator)
    assert_type(node.min, DoublePlugOperator)
    assert_type(BdDblClamp.max, DoubleAttrOperator)
    assert_type(node.max, DoublePlugOperator)
    assert_type(BdDblClamp.output, DoubleAttrOperator)
    assert_type(node.output, DoublePlugOperator)
    assert_type(node.output.get(), float)


def bd_dbl3_map_range_descriptor_contract(node: BdDbl3MapRange) -> None:
    assert_type(BdDbl3MapRange.input, MapRangeInputAttrOperator)
    assert_type(node.input, MapRangeInputPlugOperator)
    assert_type(node.input.inputX.get(), float)
    assert_type(
        BdDbl3MapRange.srcMin,
        MapRangeSrcMinAttrOperator,
    )
    assert_type(node.srcMin, MapRangeSrcMinPlugOperator)
    assert_type(
        BdDbl3MapRange.srcMax,
        MapRangeSrcMaxAttrOperator,
    )
    assert_type(node.srcMax, MapRangeSrcMaxPlugOperator)
    assert_type(
        BdDbl3MapRange.dstMin,
        MapRangeDstMinAttrOperator,
    )
    assert_type(node.dstMin, MapRangeDstMinPlugOperator)
    assert_type(
        BdDbl3MapRange.dstMax,
        MapRangeDstMaxAttrOperator,
    )
    assert_type(node.dstMax, MapRangeDstMaxPlugOperator)
    assert_type(BdDbl3MapRange.clamp, BoolAttrOperator)
    assert_type(node.clamp, BoolPlugOperator)
    assert_type(BdDbl3MapRange.output, MapRangeOutputAttrOperator)
    assert_type(node.output, MapRangeOutputPlugOperator)
    assert_type(node.output.get(), bdu.Double3)


def bd_dbl_map_range_descriptor_contract(node: BdDblMapRange) -> None:
    assert_type(BdDblMapRange.input, DoubleAttrOperator)
    assert_type(node.input, DoublePlugOperator)
    assert_type(BdDblMapRange.srcMin, DoubleAttrOperator)
    assert_type(node.srcMin, DoublePlugOperator)
    assert_type(BdDblMapRange.srcMax, DoubleAttrOperator)
    assert_type(node.srcMax, DoublePlugOperator)
    assert_type(BdDblMapRange.dstMin, DoubleAttrOperator)
    assert_type(node.dstMin, DoublePlugOperator)
    assert_type(BdDblMapRange.dstMax, DoubleAttrOperator)
    assert_type(node.dstMax, DoublePlugOperator)
    assert_type(BdDblMapRange.clamp, BoolAttrOperator)
    assert_type(node.clamp, BoolPlugOperator)
    assert_type(BdDblMapRange.output, DoubleAttrOperator)
    assert_type(node.output, DoublePlugOperator)
    assert_type(node.output.get(), float)


def bd_dbl3_divide_descriptor_contract(
    fixed: BdDbl3Divide,
    multi: BdDbl3DivideMulti,
) -> None:
    assert_type(BdDbl3Divide.input1, DivInput1AttrOperator)
    assert_type(fixed.input1, DivInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Divide.input2, DivInput2AttrOperator)
    assert_type(fixed.input2, DivInput2PlugOperator)
    assert_type(BdDbl3Divide.output, DivOutputAttrOperator)
    assert_type(fixed.output, DivOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3DivideMulti.input, DivMultiInputAttrOperator)
    assert_type(multi.input, DivMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3DivideMulti.output, DivMultiOutputAttrOperator)
    assert_type(multi.output, DivMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_divide_descriptor_contract(
    fixed: BdDblDivide,
    multi: BdDblDivideMulti,
) -> None:
    assert_type(BdDblDivide.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblDivide.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblDivide.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblDivideMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblDivideMulti.output, DoubleAttrOperator)
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


def bd_dbl3_power_descriptor_contract(
    fixed: BdDbl3Power,
    multi: BdDbl3PowerMulti,
) -> None:
    assert_type(BdDbl3Power.input1, PowInput1AttrOperator)
    assert_type(fixed.input1, PowInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Power.input2, PowInput2AttrOperator)
    assert_type(fixed.input2, PowInput2PlugOperator)
    assert_type(BdDbl3Power.output, PowOutputAttrOperator)
    assert_type(fixed.output, PowOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3PowerMulti.input, PowMultiInputAttrOperator)
    assert_type(multi.input, PowMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3PowerMulti.output, PowMultiOutputAttrOperator)
    assert_type(multi.output, PowMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_power_descriptor_contract(
    fixed: BdDblPower,
    multi: BdDblPowerMulti,
) -> None:
    assert_type(BdDblPower.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblPower.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblPower.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblPowerMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblPowerMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_dbl3_subtract_descriptor_contract(
    fixed: BdDbl3Subtract,
    multi: BdDbl3SubtractMulti,
) -> None:
    assert_type(BdDbl3Subtract.input1, SubInput1AttrOperator)
    assert_type(fixed.input1, SubInput1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Subtract.input2, SubInput2AttrOperator)
    assert_type(fixed.input2, SubInput2PlugOperator)
    assert_type(BdDbl3Subtract.output, SubOutputAttrOperator)
    assert_type(fixed.output, SubOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)

    assert_type(BdDbl3SubtractMulti.input, SubMultiInputAttrOperator)
    assert_type(multi.input, SubMultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3SubtractMulti.output, SubMultiOutputAttrOperator)
    assert_type(multi.output, SubMultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_subtract_descriptor_contract(
    fixed: BdDblSubtract,
    multi: BdDblSubtractMulti,
) -> None:
    assert_type(BdDblSubtract.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(BdDblSubtract.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblSubtract.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblSubtractMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblSubtractMulti.output, DoubleAttrOperator)
    assert_type(multi.output, DoublePlugOperator)
    assert_type(multi.output.get(), float)


def bd_dbl3_multiply_descriptor_contract(fixed: BdDbl3Multiply) -> None:
    assert_type(BdDbl3Multiply.input1, Input1AttrOperator)
    assert_type(fixed.input1, Input1PlugOperator)
    assert_type(fixed.input1.input1X.get(), float)
    assert_type(BdDbl3Multiply.input2, Input2AttrOperator)
    assert_type(fixed.input2, Input2PlugOperator)
    assert_type(fixed.input2.input2Z.get(), float)
    assert_type(BdDbl3Multiply.output, FixedOutputAttrOperator)
    assert_type(fixed.output, FixedOutputPlugOperator)
    assert_type(fixed.output.get(), bdu.Double3)


def bd_dbl3_multiply_multi_descriptor_contract(
    multi: BdDbl3MultiplyMulti,
) -> None:
    assert_type(BdDbl3MultiplyMulti.input, MultiInputAttrOperator)
    assert_type(multi.input, MultiInputPlugOperator)
    assert_type(multi.input[0].inputX.get(), float)
    assert_type(BdDbl3MultiplyMulti.output, MultiOutputAttrOperator)
    assert_type(multi.output, MultiOutputPlugOperator)
    assert_type(multi.output.get(), bdu.Double3)


def bd_dbl_multiply_descriptor_contract(
    fixed: BdDblMultiply,
    multi: BdDblMultiplyMulti,
) -> None:
    assert_type(BdDblMultiply.input1, DoubleAttrOperator)
    assert_type(fixed.input1, DoublePlugOperator)
    assert_type(fixed.input1.get(), float)
    assert_type(BdDblMultiply.input2, DoubleAttrOperator)
    assert_type(fixed.input2, DoublePlugOperator)
    assert_type(BdDblMultiply.output, DoubleAttrOperator)
    assert_type(fixed.output, DoublePlugOperator)
    assert_type(fixed.output.get(), float)

    assert_type(BdDblMultiplyMulti.input, DoubleAttrOperator)
    assert_type(multi.input, DoublePlugOperator)
    assert_type(multi.input[0].get(), float)
    assert_type(BdDblMultiplyMulti.output, DoubleAttrOperator)
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
