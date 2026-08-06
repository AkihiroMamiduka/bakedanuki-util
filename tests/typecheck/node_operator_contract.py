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
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_average import (
    Input1AttrOperator as AverageInput1AttrOperator,
    Input1PlugOperator as AverageInput1PlugOperator,
    Input2AttrOperator as AverageInput2AttrOperator,
    Input2PlugOperator as AverageInput2PlugOperator,
    OutputAttrOperator as AverageOutputAttrOperator,
    OutputPlugOperator as AverageOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_average_multi import (
    InputAttrOperator as AverageMultiInputAttrOperator,
    InputPlugOperator as AverageMultiInputPlugOperator,
    OutputAttrOperator as AverageMultiOutputAttrOperator,
    OutputPlugOperator as AverageMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_weighted_average_multi import (
    InputAttrOperator as Dbl3WeightedAverageInputAttrOperator,
    InputPlugOperator as Dbl3WeightedAverageInputPlugOperator,
    OutputAttrOperator as WeightedAverageOutputAttrOperator,
    OutputPlugOperator as WeightedAverageOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl_weighted_average_multi import (
    InputAttrOperator as DblWeightedAverageInputAttrOperator,
    InputPlugOperator as DblWeightedAverageInputPlugOperator,
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
from bd_util.maya.node.operator.attr.define.node_attr.bd_any_condition_dbl_l_multi import (
    CaseAttrOperator as AnyConditionDblLCaseAttrOperator,
    CasePlugOperator as AnyConditionDblLCasePlugOperator,
    Case_extraAttrOperator as AnyConditionDblLExtraAttrOperator,
    Case_extraPlugOperator as AnyConditionDblLExtraPlugOperator,
    Case_extra_comparisonEnumPlugOperator as AnyConditionDblLExtraComparisonPlugOperator,
    Case_extra_logicEnumPlugOperator as AnyConditionDblLExtraLogicPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_any_condition_dbl_multi import (
    CaseAttrOperator as AnyConditionDblCaseAttrOperator,
    CasePlugOperator as AnyConditionDblCasePlugOperator,
    Case_extraAttrOperator as AnyConditionDblExtraAttrOperator,
    Case_extraPlugOperator as AnyConditionDblExtraPlugOperator,
    Case_extra_comparisonEnumPlugOperator as AnyConditionDblExtraComparisonPlugOperator,
    Case_extra_logicEnumPlugOperator as AnyConditionDblExtraLogicPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_any_condition_dbl import (
    ExtraAttrOperator as AnyConditionDblSingleExtraAttrOperator,
    ExtraPlugOperator as AnyConditionDblSingleExtraPlugOperator,
    Extra_comparisonEnumPlugOperator as AnyConditionDblSingleExtraComparisonPlugOperator,
    Extra_logicEnumPlugOperator as AnyConditionDblSingleExtraLogicPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_any_condition_dbl_l import (
    ExtraAttrOperator as AnyConditionDblLSingleExtraAttrOperator,
    ExtraPlugOperator as AnyConditionDblLSingleExtraPlugOperator,
    Extra_comparisonEnumPlugOperator as AnyConditionDblLSingleExtraComparisonPlugOperator,
    Extra_logicEnumPlugOperator as AnyConditionDblLSingleExtraLogicPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_condition_dbl_case_compose import (
    ExtraAttrOperator as ConditionDblCaseComposeExtraAttrOperator,
    ExtraPlugOperator as ConditionDblCaseComposeExtraPlugOperator,
    OutputAttrOperator as ConditionDblCaseComposeOutputAttrOperator,
    OutputPlugOperator as ConditionDblCaseComposeOutputPlugOperator,
    Output_outputExtraPlugOperator as ConditionDblCaseComposeOutputExtraPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_condition_dbl_extra_compose import (
    OutputAttrOperator as ConditionDblExtraComposeOutputAttrOperator,
    OutputPlugOperator as ConditionDblExtraComposeOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_condition_dbl_l_case_compose import (
    ExtraAttrOperator as ConditionDblLCaseComposeExtraAttrOperator,
    ExtraPlugOperator as ConditionDblLCaseComposeExtraPlugOperator,
    OutputAttrOperator as ConditionDblLCaseComposeOutputAttrOperator,
    OutputPlugOperator as ConditionDblLCaseComposeOutputPlugOperator,
    Output_outputExtraPlugOperator as ConditionDblLCaseComposeOutputExtraPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_condition_dbl_l_extra_compose import (
    OutputAttrOperator as ConditionDblLExtraComposeOutputAttrOperator,
    OutputPlugOperator as ConditionDblLExtraComposeOutputPlugOperator,
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
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl_l3_divide import (
    FactorPlugOperator as DblL3DivideFactorPlugOperator,
    InputPlugOperator as DblL3DivideInputPlugOperator,
    OutputPlugOperator as DblL3DivideOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl_l3_divide_multi import (
    FactorPlugOperator as DblL3DivideMultiFactorPlugOperator,
    InputPlugOperator as DblL3DivideMultiInputPlugOperator,
    OutputPlugOperator as DblL3DivideMultiOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl_l3_multiply import (
    FactorPlugOperator as DblL3MultiplyFactorPlugOperator,
    InputPlugOperator as DblL3MultiplyInputPlugOperator,
    OutputPlugOperator as DblL3MultiplyOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl_l3_multiply_multi import (
    FactorPlugOperator as DblL3MultiplyMultiFactorPlugOperator,
    InputPlugOperator as DblL3MultiplyMultiInputPlugOperator,
    OutputPlugOperator as DblL3MultiplyMultiOutputPlugOperator,
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
from bd_util.maya.node.operator.attr.define.std.at.typed import (
    TypedAttrOperator,
    TypedPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.matrix import (
    DataMatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.custom import (
    Double3PlugOperator,
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
from bd_util.maya.node.operator.node.dg.bd_dbl3_average import BdDbl3Average
from bd_util.maya.node.operator.node.dg.bd_dbl3_average_multi import (
    BdDbl3AverageMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl3_weighted_average_multi import (
    BdDbl3WeightedAverageMulti,
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
from bd_util.maya.node.operator.node.dg.bd_dbl_l_divide import BdDblLDivide
from bd_util.maya.node.operator.node.dg.bd_dbl_l_divide_multi import (
    BdDblLDivideMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l_multiply import (
    BdDblLMultiply,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l_multiply_multi import (
    BdDblLMultiplyMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l3_divide import (
    BdDblL3Divide,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l3_divide_multi import (
    BdDblL3DivideMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l3_multiply import (
    BdDblL3Multiply,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l3_multiply_multi import (
    BdDblL3MultiplyMulti,
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
from bd_util.maya.node.operator.node.dg.bd_dbl_average import BdDblAverage
from bd_util.maya.node.operator.node.dg.bd_dbl_average_multi import (
    BdDblAverageMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_weighted_average_multi import (
    BdDblWeightedAverageMulti,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_clamp import BdDblClamp
from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl import (
    BdAnyConditionDbl,
)
from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_l import (
    BdAnyConditionDblL,
)
from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_l_multi import (
    BdAnyConditionDblLMulti,
)
from bd_util.maya.node.operator.node.dg.bd_any_condition_dbl_multi import (
    BdAnyConditionDblMulti,
)
from bd_util.maya.node.operator.node.dg.bd_condition_dbl_case_compose import (
    BdConditionDblCaseCompose,
)
from bd_util.maya.node.operator.node.dg.bd_condition_dbl_extra_compose import (
    BdConditionDblExtraCompose,
)
from bd_util.maya.node.operator.node.dg.bd_condition_dbl_l_case_compose import (
    BdConditionDblLCaseCompose,
)
from bd_util.maya.node.operator.node.dg.bd_condition_dbl_l_extra_compose import (
    BdConditionDblLExtraCompose,
)
from bd_util.maya.node.operator.node.dg._generated.bd_any_condition_dbl import (
    OperationEnumAttrOperator as AnyConditionDblOperationAttrOperator,
    OperationEnumPlugOperator as AnyConditionDblOperationPlugOperator,
)
from bd_util.maya.node.operator.node.dg._generated.bd_any_condition_dbl_l import (
    OperationEnumAttrOperator as AnyConditionDblLOperationAttrOperator,
    OperationEnumPlugOperator as AnyConditionDblLOperationPlugOperator,
)
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


def condition_contract(nodes: bdu.Nodes) -> None:
    double = nodes.create.bdAny_ConditionDbl(name="double_condition")
    assert_type(double, BdAnyConditionDbl)
    assert_type(double.input, DoublePlugOperator)
    assert_type(double.operation, AnyConditionDblOperationPlugOperator)
    assert_type(double.compare, DoublePlugOperator)
    assert_type(
        BdAnyConditionDbl.extra,
        AnyConditionDblSingleExtraAttrOperator,
    )
    assert_type(double.extra, AnyConditionDblSingleExtraPlugOperator)
    assert_type(double.extra[0], AnyConditionDblSingleExtraPlugOperator)
    assert_type(double.extra[next], AnyConditionDblSingleExtraPlugOperator)
    assert_type(
        double.extra[0].logic,
        AnyConditionDblSingleExtraLogicPlugOperator,
    )
    assert_type(
        double.extra[0].comparison,
        AnyConditionDblSingleExtraComparisonPlugOperator,
    )
    assert_type(double.extra[0].compareValue, DoublePlugOperator)
    assert_type(double.trueValue, TypedPlugOperator)
    assert_type(double.falseValue, TypedPlugOperator)
    assert_type(double.output, TypedPlugOperator)
    assert_type(
        nodes.existing.bdAny_ConditionDbl("existing_double_condition"),
        BdAnyConditionDbl,
    )
    assert_type(
        BdAnyConditionDbl.operation,
        AnyConditionDblOperationAttrOperator,
    )

    double_multi = nodes.create.bdAny_ConditionDblMulti(
        name="double_condition_multi"
    )
    assert_type(double_multi, BdAnyConditionDblMulti)
    assert_type(
        BdAnyConditionDblMulti.case,
        AnyConditionDblCaseAttrOperator,
    )
    assert_type(double_multi.case, AnyConditionDblCasePlugOperator)
    assert_type(double_multi.case[0], AnyConditionDblCasePlugOperator)
    assert_type(double_multi.case[next], AnyConditionDblCasePlugOperator)
    assert_type(double_multi.case[0].compare, DoublePlugOperator)
    assert_type(
        BdAnyConditionDblMulti.case.extra,
        AnyConditionDblExtraAttrOperator,
    )
    assert_type(
        double_multi.case[0].extra,
        AnyConditionDblExtraPlugOperator,
    )
    assert_type(
        double_multi.case[0].extra[0],
        AnyConditionDblExtraPlugOperator,
    )
    assert_type(
        double_multi.case[0].extra[next].logic,
        AnyConditionDblExtraLogicPlugOperator,
    )
    assert_type(
        double_multi.case[0].extra[0].comparison,
        AnyConditionDblExtraComparisonPlugOperator,
    )
    assert_type(
        double_multi.case[0].extra[0].compareValue,
        DoublePlugOperator,
    )
    assert_type(double_multi.case[0].value, TypedPlugOperator)
    assert_type(double_multi.elseValue, TypedPlugOperator)
    assert_type(double_multi.output, TypedPlugOperator)
    assert_type(
        nodes.existing.bdAny_ConditionDblMulti("existing_double_multi"),
        BdAnyConditionDblMulti,
    )

    linear = nodes.create.bdAny_ConditionDblL(name="linear_condition")
    assert_type(linear, BdAnyConditionDblL)
    assert_type(linear.input, double_linear.DoubleLinearPlugOperator)
    assert_type(linear.operation, AnyConditionDblLOperationPlugOperator)
    assert_type(linear.compare, double_linear.DoubleLinearPlugOperator)
    assert_type(
        BdAnyConditionDblL.extra,
        AnyConditionDblLSingleExtraAttrOperator,
    )
    assert_type(linear.extra, AnyConditionDblLSingleExtraPlugOperator)
    assert_type(
        linear.extra[0].logic,
        AnyConditionDblLSingleExtraLogicPlugOperator,
    )
    assert_type(
        linear.extra[0].comparison,
        AnyConditionDblLSingleExtraComparisonPlugOperator,
    )
    assert_type(
        linear.extra[0].compareValue,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(BdAnyConditionDblL.trueValue, TypedAttrOperator)
    assert_type(linear.trueValue, TypedPlugOperator)
    assert_type(linear.falseValue, TypedPlugOperator)
    assert_type(linear.output, TypedPlugOperator)
    assert_type(
        nodes.existing.bdAny_ConditionDblL("existing_linear_condition"),
        BdAnyConditionDblL,
    )
    assert_type(
        BdAnyConditionDblL.operation,
        AnyConditionDblLOperationAttrOperator,
    )

    linear_multi = nodes.create.bdAny_ConditionDblLMulti(
        name="linear_condition_multi"
    )
    assert_type(linear_multi, BdAnyConditionDblLMulti)
    assert_type(
        BdAnyConditionDblLMulti.case,
        AnyConditionDblLCaseAttrOperator,
    )
    assert_type(linear_multi.case, AnyConditionDblLCasePlugOperator)
    assert_type(linear_multi.case[0], AnyConditionDblLCasePlugOperator)
    assert_type(
        linear_multi.case[0].compare,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        BdAnyConditionDblLMulti.case.extra,
        AnyConditionDblLExtraAttrOperator,
    )
    assert_type(
        linear_multi.case[0].extra,
        AnyConditionDblLExtraPlugOperator,
    )
    assert_type(
        linear_multi.case[0].extra[0].logic,
        AnyConditionDblLExtraLogicPlugOperator,
    )
    assert_type(
        linear_multi.case[0].extra[0].comparison,
        AnyConditionDblLExtraComparisonPlugOperator,
    )
    assert_type(
        linear_multi.case[0].extra[0].compareValue,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(linear_multi.case[0].value, TypedPlugOperator)
    assert_type(linear_multi.elseValue, TypedPlugOperator)
    assert_type(linear_multi.output, TypedPlugOperator)
    assert_type(
        nodes.existing.bdAny_ConditionDblLMulti("existing_linear_multi"),
        BdAnyConditionDblLMulti,
    )


def condition_compose_contract(nodes: bdu.Nodes) -> None:
    double_extra = nodes.create.bdConditionDblExtra_Compose(
        name="double_extra_compose"
    )
    assert_type(double_extra, BdConditionDblExtraCompose)
    assert_type(double_extra.compareValue, DoublePlugOperator)
    assert_type(
        BdConditionDblExtraCompose.output,
        ConditionDblExtraComposeOutputAttrOperator,
    )
    assert_type(
        double_extra.output,
        ConditionDblExtraComposeOutputPlugOperator,
    )
    assert_type(
        double_extra.output.outputCompareValue,
        DoublePlugOperator,
    )
    assert_type(
        nodes.existing.bdConditionDblExtra_Compose(
            "existing_double_extra_compose"
        ),
        BdConditionDblExtraCompose,
    )

    double_case = nodes.create.bdConditionDblCase_Compose(
        name="double_case_compose"
    )
    assert_type(double_case, BdConditionDblCaseCompose)
    assert_type(double_case.compare, DoublePlugOperator)
    assert_type(
        BdConditionDblCaseCompose.extra,
        ConditionDblCaseComposeExtraAttrOperator,
    )
    assert_type(
        double_case.extra,
        ConditionDblCaseComposeExtraPlugOperator,
    )
    assert_type(
        double_case.extra[next],
        ConditionDblCaseComposeExtraPlugOperator,
    )
    assert_type(double_case.extra[next].compareValue, DoublePlugOperator)
    assert_type(double_case.value, TypedPlugOperator)
    assert_type(
        BdConditionDblCaseCompose.output,
        ConditionDblCaseComposeOutputAttrOperator,
    )
    assert_type(
        double_case.output,
        ConditionDblCaseComposeOutputPlugOperator,
    )
    assert_type(
        double_case.output.outputExtra[next],
        ConditionDblCaseComposeOutputExtraPlugOperator,
    )
    assert_type(double_case.output.outputValue, TypedPlugOperator)
    assert_type(
        nodes.existing.bdConditionDblCase_Compose(
            "existing_double_case_compose"
        ),
        BdConditionDblCaseCompose,
    )

    linear_extra = nodes.create.bdConditionDblLExtra_Compose(
        name="linear_extra_compose"
    )
    assert_type(linear_extra, BdConditionDblLExtraCompose)
    assert_type(
        linear_extra.compareValue,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        BdConditionDblLExtraCompose.output,
        ConditionDblLExtraComposeOutputAttrOperator,
    )
    assert_type(
        linear_extra.output,
        ConditionDblLExtraComposeOutputPlugOperator,
    )
    assert_type(
        linear_extra.output.outputCompareValue,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        nodes.existing.bdConditionDblLExtra_Compose(
            "existing_linear_extra_compose"
        ),
        BdConditionDblLExtraCompose,
    )

    linear_case = nodes.create.bdConditionDblLCase_Compose(
        name="linear_case_compose"
    )
    assert_type(linear_case, BdConditionDblLCaseCompose)
    assert_type(
        linear_case.compare,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        BdConditionDblLCaseCompose.extra,
        ConditionDblLCaseComposeExtraAttrOperator,
    )
    assert_type(
        linear_case.extra,
        ConditionDblLCaseComposeExtraPlugOperator,
    )
    assert_type(
        linear_case.extra[next].compareValue,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(linear_case.value, TypedPlugOperator)
    assert_type(
        BdConditionDblLCaseCompose.output,
        ConditionDblLCaseComposeOutputAttrOperator,
    )
    assert_type(
        linear_case.output,
        ConditionDblLCaseComposeOutputPlugOperator,
    )
    assert_type(
        linear_case.output.outputExtra[next],
        ConditionDblLCaseComposeOutputExtraPlugOperator,
    )
    assert_type(linear_case.output.outputValue, TypedPlugOperator)
    assert_type(
        nodes.existing.bdConditionDblLCase_Compose(
            "existing_linear_case_compose"
        ),
        BdConditionDblLCaseCompose,
    )


def average_contract(nodes: bdu.Nodes) -> None:
    scalar = nodes.create.bdDbl_Average(name="scalar_average")
    assert_type(scalar, BdDblAverage)
    assert_type(scalar.input1, DoublePlugOperator)
    assert_type(scalar.input2, DoublePlugOperator)
    assert_type(scalar.output, DoublePlugOperator)
    assert_type(
        nodes.existing.bdDbl_Average("existing_scalar_average"),
        BdDblAverage,
    )

    scalar_multi = nodes.create.bdDbl_AverageMulti(name="scalar_average_multi")
    assert_type(scalar_multi, BdDblAverageMulti)
    assert_type(scalar_multi.input, DoublePlugOperator)
    assert_type(scalar_multi.input[0], DoublePlugOperator)
    assert_type(scalar_multi.input[next], DoublePlugOperator)
    assert_type(scalar_multi.output, DoublePlugOperator)
    assert_type(
        nodes.existing.bdDbl_AverageMulti("existing_scalar_average_multi"),
        BdDblAverageMulti,
    )

    vector = nodes.create.bdDbl3_Average(name="vector_average")
    assert_type(vector, BdDbl3Average)
    assert_type(BdDbl3Average.input1, AverageInput1AttrOperator)
    assert_type(vector.input1, AverageInput1PlugOperator)
    assert_type(BdDbl3Average.input2, AverageInput2AttrOperator)
    assert_type(vector.input2, AverageInput2PlugOperator)
    assert_type(BdDbl3Average.output, AverageOutputAttrOperator)
    assert_type(vector.output, AverageOutputPlugOperator)
    assert_type(vector.output.get(), bdu.Double3)
    assert_type(
        nodes.existing.bdDbl3_Average("existing_vector_average"),
        BdDbl3Average,
    )

    vector_multi = nodes.create.bdDbl3_AverageMulti(
        name="vector_average_multi"
    )
    assert_type(vector_multi, BdDbl3AverageMulti)
    assert_type(BdDbl3AverageMulti.input, AverageMultiInputAttrOperator)
    assert_type(vector_multi.input, AverageMultiInputPlugOperator)
    assert_type(vector_multi.input[0], AverageMultiInputPlugOperator)
    assert_type(vector_multi.input[next], AverageMultiInputPlugOperator)
    assert_type(BdDbl3AverageMulti.output, AverageMultiOutputAttrOperator)
    assert_type(vector_multi.output, AverageMultiOutputPlugOperator)
    assert_type(vector_multi.output.get(), bdu.Double3)
    assert_type(
        nodes.existing.bdDbl3_AverageMulti("existing_vector_average_multi"),
        BdDbl3AverageMulti,
    )


def weighted_average_contract(nodes: bdu.Nodes) -> None:
    scalar = nodes.create.bdDbl_WeightedAverageMulti(
        name="scalar_weighted_average"
    )
    assert_type(scalar, BdDblWeightedAverageMulti)
    assert_type(
        BdDblWeightedAverageMulti.input,
        DblWeightedAverageInputAttrOperator,
    )
    assert_type(scalar.input, DblWeightedAverageInputPlugOperator)
    assert_type(scalar.input[0], DblWeightedAverageInputPlugOperator)
    assert_type(scalar.input[next], DblWeightedAverageInputPlugOperator)
    assert_type(scalar.input[next].value, DoublePlugOperator)
    assert_type(scalar.input[next].weight, DoublePlugOperator)
    assert_type(scalar.output, DoublePlugOperator)
    assert_type(
        nodes.existing.bdDbl_WeightedAverageMulti(
            "existing_scalar_weighted_average"
        ),
        BdDblWeightedAverageMulti,
    )

    vector = nodes.create.bdDbl3_WeightedAverageMulti(
        name="vector_weighted_average"
    )
    assert_type(vector, BdDbl3WeightedAverageMulti)
    assert_type(
        BdDbl3WeightedAverageMulti.input,
        Dbl3WeightedAverageInputAttrOperator,
    )
    assert_type(vector.input, Dbl3WeightedAverageInputPlugOperator)
    assert_type(vector.input[0], Dbl3WeightedAverageInputPlugOperator)
    assert_type(vector.input[next], Dbl3WeightedAverageInputPlugOperator)
    assert_type(vector.input[next].value, Double3PlugOperator)
    assert_type(vector.input[next].value.x, DoublePlugOperator)
    assert_type(vector.input[next].weight, DoublePlugOperator)
    assert_type(
        BdDbl3WeightedAverageMulti.output,
        WeightedAverageOutputAttrOperator,
    )
    assert_type(vector.output, WeightedAverageOutputPlugOperator)
    assert_type(vector.output.get(), bdu.Double3)
    assert_type(
        nodes.existing.bdDbl3_WeightedAverageMulti(
            "existing_vector_weighted_average"
        ),
        BdDbl3WeightedAverageMulti,
    )


def double_linear_factor_contract(nodes: bdu.Nodes) -> None:
    scalar_multiply = nodes.create.bdDblL_Multiply(name="scalar_multiply")
    assert_type(scalar_multiply, BdDblLMultiply)
    assert_type(
        scalar_multiply.input,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(scalar_multiply.factor, DoublePlugOperator)
    assert_type(
        scalar_multiply.output,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(scalar_multiply.output.get(), float)
    assert_type(
        nodes.existing.bdDblL_Multiply("existing_scalar_multiply"),
        BdDblLMultiply,
    )

    scalar_multiply_multi = nodes.create.bdDblL_MultiplyMulti(
        name="scalar_multiply_multi"
    )
    assert_type(scalar_multiply_multi, BdDblLMultiplyMulti)
    assert_type(
        scalar_multiply_multi.input,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(scalar_multiply_multi.factor, DoublePlugOperator)
    assert_type(scalar_multiply_multi.factor[next], DoublePlugOperator)
    assert_type(
        scalar_multiply_multi.output,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        nodes.existing.bdDblL_MultiplyMulti("existing_scalar_multiply_multi"),
        BdDblLMultiplyMulti,
    )

    scalar_divide = nodes.create.bdDblL_Divide(name="scalar_divide")
    assert_type(scalar_divide, BdDblLDivide)
    assert_type(
        scalar_divide.input,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(scalar_divide.factor, DoublePlugOperator)
    assert_type(
        scalar_divide.output,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        nodes.existing.bdDblL_Divide("existing_scalar_divide"),
        BdDblLDivide,
    )

    scalar_divide_multi = nodes.create.bdDblL_DivideMulti(
        name="scalar_divide_multi"
    )
    assert_type(scalar_divide_multi, BdDblLDivideMulti)
    assert_type(scalar_divide_multi.factor[next], DoublePlugOperator)
    assert_type(
        scalar_divide_multi.output,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        nodes.existing.bdDblL_DivideMulti("existing_scalar_divide_multi"),
        BdDblLDivideMulti,
    )

    vector_multiply = nodes.create.bdDblL3_Multiply(name="vector_multiply")
    assert_type(vector_multiply, BdDblL3Multiply)
    assert_type(vector_multiply.input, DblL3MultiplyInputPlugOperator)
    assert_type(vector_multiply.factor, DblL3MultiplyFactorPlugOperator)
    assert_type(vector_multiply.factor.factorX, DoublePlugOperator)
    assert_type(vector_multiply.output, DblL3MultiplyOutputPlugOperator)
    assert_type(vector_multiply.output.get(), bdu.DoubleLinear3)
    assert_type(
        nodes.existing.bdDblL3_Multiply("existing_vector_multiply"),
        BdDblL3Multiply,
    )

    vector_multiply_multi = nodes.create.bdDblL3_MultiplyMulti(
        name="vector_multiply_multi"
    )
    assert_type(vector_multiply_multi, BdDblL3MultiplyMulti)
    assert_type(
        vector_multiply_multi.input,
        DblL3MultiplyMultiInputPlugOperator,
    )
    assert_type(
        vector_multiply_multi.factor,
        DblL3MultiplyMultiFactorPlugOperator,
    )
    assert_type(
        vector_multiply_multi.factor[next],
        DblL3MultiplyMultiFactorPlugOperator,
    )
    assert_type(
        vector_multiply_multi.output,
        DblL3MultiplyMultiOutputPlugOperator,
    )
    assert_type(
        nodes.existing.bdDblL3_MultiplyMulti("existing_vector_multiply_multi"),
        BdDblL3MultiplyMulti,
    )

    vector_divide = nodes.create.bdDblL3_Divide(name="vector_divide")
    assert_type(vector_divide, BdDblL3Divide)
    assert_type(vector_divide.input, DblL3DivideInputPlugOperator)
    assert_type(vector_divide.factor, DblL3DivideFactorPlugOperator)
    assert_type(vector_divide.output, DblL3DivideOutputPlugOperator)
    assert_type(
        nodes.existing.bdDblL3_Divide("existing_vector_divide"),
        BdDblL3Divide,
    )

    vector_divide_multi = nodes.create.bdDblL3_DivideMulti(
        name="vector_divide_multi"
    )
    assert_type(vector_divide_multi, BdDblL3DivideMulti)
    assert_type(
        vector_divide_multi.input,
        DblL3DivideMultiInputPlugOperator,
    )
    assert_type(
        vector_divide_multi.factor[next],
        DblL3DivideMultiFactorPlugOperator,
    )
    assert_type(
        vector_divide_multi.output,
        DblL3DivideMultiOutputPlugOperator,
    )
    assert_type(
        nodes.existing.bdDblL3_DivideMulti("existing_vector_divide_multi"),
        BdDblL3DivideMulti,
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
