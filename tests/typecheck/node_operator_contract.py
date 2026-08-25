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
from bd_util.maya.node.operator.attr.define.node_attr.bd_quat_multiply_multi import (
    InputQuatAttrOperator,
    InputQuatPlugOperator,
    OutputQuatAttrOperator,
    OutputQuatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_quat_compose_bend_twist import (
    InputAttrOperator as BendTwistInputAttrOperator,
    InputPlugOperator as BendTwistInputPlugOperator,
    OutputQuatAttrOperator as BendTwistOutputQuatAttrOperator,
    OutputQuatPlugOperator as BendTwistOutputQuatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_quat_decompose_bend_twist import (
    InputQuatAttrOperator as BendTwistInputQuatAttrOperator,
    InputQuatPlugOperator as BendTwistInputQuatPlugOperator,
    OutputAttrOperator as BendTwistOutputAttrOperator,
    OutputPlugOperator as BendTwistOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_quat_change_basis import (
    AxisQuatAttrOperator as ChangeBasisAxisQuatAttrOperator,
    AxisQuatPlugOperator as ChangeBasisAxisQuatPlugOperator,
    InputQuatAttrOperator as ChangeBasisInputQuatAttrOperator,
    InputQuatPlugOperator as ChangeBasisInputQuatPlugOperator,
    OutputQuatAttrOperator as ChangeBasisOutputQuatAttrOperator,
    OutputQuatPlugOperator as ChangeBasisOutputQuatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_quat_limit_bend_twist import (
    MaxAttrOperator as LimitMaxAttrOperator,
    MaxPlugOperator as LimitMaxPlugOperator,
    MinAttrOperator as LimitMinAttrOperator,
    MinPlugOperator as LimitMinPlugOperator,
    OutputQuatAttrOperator as LimitOutputQuatAttrOperator,
    OutputQuatPlugOperator as LimitOutputQuatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_quat_value import (
    ValueAttrOperator as QuatValueAttrOperator,
    ValuePlugOperator as QuatValuePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_bend_twist_falloff_weight import (
    AxisQuatAttrOperator as RbfBendTwistAxisQuatAttrOperator,
    AxisQuatPlugOperator as RbfBendTwistAxisQuatPlugOperator,
    InputQuatAttrOperator as RbfBendTwistInputQuatAttrOperator,
    InputQuatPlugOperator as RbfBendTwistInputQuatPlugOperator,
    Pose_poseQuatPlugOperator as RbfBendTwistPoseQuatPlugOperator,
    PoseAttrOperator as RbfBendTwistPoseAttrOperator,
    PosePlugOperator as RbfBendTwistPosePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_multi_bend_twist_falloff_weight import (
    Pose_sourceQuatPlugOperator as RbfMultiBendTwistPoseSourceQuatPlugOperator,
    PoseAttrOperator as RbfMultiBendTwistPoseAttrOperator,
    PosePlugOperator as RbfMultiBendTwistPosePlugOperator,
    Source_axisQuatPlugOperator as RbfMultiBendTwistAxisQuatPlugOperator,
    Source_inputQuatPlugOperator as RbfMultiBendTwistInputQuatPlugOperator,
    Source_orderEnumPlugOperator as RbfMultiBendTwistOrderPlugOperator,
    SourceAttrOperator as RbfMultiBendTwistSourceAttrOperator,
    SourcePlugOperator as RbfMultiBendTwistSourcePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_multi_orientation_weight import (
    Pose_sourceQuatPlugOperator as RbfMultiOrientationPoseSourceQuatPlugOperator,
    PoseAttrOperator as RbfMultiOrientationPoseAttrOperator,
    PosePlugOperator as RbfMultiOrientationPosePlugOperator,
    Source_inputQuatPlugOperator as RbfMultiOrientationInputQuatPlugOperator,
    SourceAttrOperator as RbfMultiOrientationSourceAttrOperator,
    SourcePlugOperator as RbfMultiOrientationSourcePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_multi_orientation_falloff_weight import (
    Pose_sourceQuatPlugOperator as RbfMultiOrientationFalloffPoseSourceQuatPlugOperator,
    PoseAttrOperator as RbfMultiOrientationFalloffPoseAttrOperator,
    PosePlugOperator as RbfMultiOrientationFalloffPosePlugOperator,
    Source_inputQuatPlugOperator as RbfMultiOrientationFalloffInputQuatPlugOperator,
    SourceAttrOperator as RbfMultiOrientationFalloffSourceAttrOperator,
    SourcePlugOperator as RbfMultiOrientationFalloffSourcePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_multi_position_falloff_weight import (
    Pose_sourcePositionPlugOperator as RbfMultiPositionFalloffPoseSourcePositionPlugOperator,
    PoseAttrOperator as RbfMultiPositionFalloffPoseAttrOperator,
    PosePlugOperator as RbfMultiPositionFalloffPosePlugOperator,
    Source_inputPositionPlugOperator as RbfMultiPositionFalloffInputPositionPlugOperator,
    SourceAttrOperator as RbfMultiPositionFalloffSourceAttrOperator,
    SourcePlugOperator as RbfMultiPositionFalloffSourcePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_multi_position_weight import (
    Pose_sourcePositionPlugOperator as RbfMultiPositionPoseSourcePositionPlugOperator,
    PoseAttrOperator as RbfMultiPositionPoseAttrOperator,
    PosePlugOperator as RbfMultiPositionPosePlugOperator,
    Source_inputPositionPlugOperator as RbfMultiPositionInputPositionPlugOperator,
    SourceAttrOperator as RbfMultiPositionSourceAttrOperator,
    SourcePlugOperator as RbfMultiPositionSourcePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_orientation_falloff_weight import (
    InputQuatAttrOperator as RbfOrientationFalloffInputQuatAttrOperator,
    InputQuatPlugOperator as RbfOrientationFalloffInputQuatPlugOperator,
    Pose_poseQuatPlugOperator as RbfOrientationFalloffPoseQuatPlugOperator,
    PoseAttrOperator as RbfOrientationFalloffPoseAttrOperator,
    PosePlugOperator as RbfOrientationFalloffPosePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_orientation_weight import (
    InputQuatAttrOperator as RbfInputQuatAttrOperator,
    InputQuatPlugOperator as RbfInputQuatPlugOperator,
    Pose_poseQuatPlugOperator as RbfPoseQuatPlugOperator,
    PoseAttrOperator as RbfPoseAttrOperator,
    PosePlugOperator as RbfPosePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_position_falloff_weight import (
    InputPositionAttrOperator as RbfPositionFalloffInputAttrOperator,
    InputPositionPlugOperator as RbfPositionFalloffInputPlugOperator,
    Pose_positionPlugOperator as RbfPositionFalloffPosePositionPlugOperator,
    PoseAttrOperator as RbfPositionFalloffPoseAttrOperator,
    PosePlugOperator as RbfPositionFalloffPosePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_position_weight import (
    InputPositionAttrOperator as RbfPositionInputAttrOperator,
    InputPositionPlugOperator as RbfPositionInputPlugOperator,
    Pose_positionPlugOperator as RbfPositionPosePositionPlugOperator,
    PoseAttrOperator as RbfPositionPoseAttrOperator,
    PosePlugOperator as RbfPositionPosePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_rbf_pose_blend import (
    BaseRotateAttrOperator as RbfBlendBaseRotateAttrOperator,
    BaseRotatePlugOperator as RbfBlendBaseRotatePlugOperator,
    BaseScaleAttrOperator as RbfBlendBaseScaleAttrOperator,
    BaseScalePlugOperator as RbfBlendBaseScalePlugOperator,
    BaseTranslateAttrOperator as RbfBlendBaseTranslateAttrOperator,
    BaseTranslatePlugOperator as RbfBlendBaseTranslatePlugOperator,
    OutputQuatAttrOperator as RbfBlendOutputQuatAttrOperator,
    OutputQuatPlugOperator as RbfBlendOutputQuatPlugOperator,
    OutputRotateAttrOperator as RbfBlendOutputRotateAttrOperator,
    OutputRotatePlugOperator as RbfBlendOutputRotatePlugOperator,
    OutputScaleAttrOperator as RbfBlendOutputScaleAttrOperator,
    OutputScalePlugOperator as RbfBlendOutputScalePlugOperator,
    OutputTranslateAttrOperator as RbfBlendOutputTranslateAttrOperator,
    OutputTranslatePlugOperator as RbfBlendOutputTranslatePlugOperator,
    Pose_rotatePlugOperator as RbfBlendPoseRotatePlugOperator,
    Pose_scalePlugOperator as RbfBlendPoseScalePlugOperator,
    Pose_translatePlugOperator as RbfBlendPoseTranslatePlugOperator,
    PoseAttrOperator as RbfBlendPoseAttrOperator,
    PosePlugOperator as RbfBlendPosePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_euler_value import (
    ValueAttrOperator as EulerValueAttrOperator,
    ValuePlugOperator as EulerValuePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_euler_decompose_twist import (
    AxisRotateAttrOperator,
    AxisRotatePlugOperator,
    InputRotateAttrOperator,
    InputRotatePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_euler_decompose_bend_twist import (
    AxisRotateAttrOperator as EulerDecomposeAxisRotateAttrOperator,
    AxisRotatePlugOperator as EulerDecomposeAxisRotatePlugOperator,
    InputRotateAttrOperator as EulerDecomposeInputRotateAttrOperator,
    InputRotatePlugOperator as EulerDecomposeInputRotatePlugOperator,
    OutputAttrOperator as EulerDecomposeOutputAttrOperator,
    OutputPlugOperator as EulerDecomposeOutputPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_euler_compose_bend_twist import (
    AxisRotateAttrOperator as EulerComposeAxisRotateAttrOperator,
    AxisRotatePlugOperator as EulerComposeAxisRotatePlugOperator,
    InputAttrOperator as EulerComposeInputAttrOperator,
    InputPlugOperator as EulerComposeInputPlugOperator,
    OutputRotateAttrOperator as EulerComposeOutputRotateAttrOperator,
    OutputRotatePlugOperator as EulerComposeOutputRotatePlugOperator,
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
from bd_util.maya.node.operator.attr.define.node_attr.bd_dbl3_ratio_dbl_l3 import (
    BasePlugOperator as RatioDblL3BasePlugOperator,
    InputPlugOperator as RatioDblL3InputPlugOperator,
    OutputPlugOperator as RatioDblL3OutputPlugOperator,
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
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.float import (
    FloatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.long import (
    LongPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.short import (
    ShortPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolAttrOperator,
    BoolPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.message import (
    MessagePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit import (
    double_linear,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAnglePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.time import (
    TimePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.typed import (
    TypedAttrOperator,
    TypedPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.matrix import (
    DataMatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.mesh import (
    DataMeshPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.nurbs_curve import (
    DataNurbsCurvePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.nurbs_surface import (
    DataNurbsSurfacePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.string import (
    DataStringPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.locator import (
    LocalPositionPlugOperator,
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
from bd_util.maya.node.operator.node.dg.bd_dbl3_ratio_dbl_l3 import (
    BdDbl3RatioDblL3,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_ratio_dbl_l import (
    BdDblRatioDblL,
)
from bd_util.maya.node.operator.node.dg.bd_dbl_l_right_triangle import (
    BdDblLRightTriangle,
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
from bd_util.maya.node.operator.node.dg.bd_quat_multiply_multi import (
    BdQuatMultiplyMulti,
)
from bd_util.maya.node.operator.node.dg.bd_quat_change_basis import (
    BdQuatChangeBasis,
)
from bd_util.maya.node.operator.node.dg._generated.bd_quat_change_basis import (
    DirectionEnumAttrOperator as ChangeBasisDirectionAttrOperator,
    DirectionEnumPlugOperator as ChangeBasisDirectionPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_quat_value import BdQuatValue
from bd_util.maya.node.operator.node.dg.bd_rbf_bend_twist_falloff_weight import (
    BdRbfBendTwistFalloffWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_bend_twist_falloff_weight import (
    FalloffEnumPlugOperator as RbfBendTwistFalloffPlugOperator,
    FalloffStatusEnumPlugOperator as RbfBendTwistFalloffStatusPlugOperator,
    ModeEnumPlugOperator as RbfBendTwistModePlugOperator,
    OrderEnumPlugOperator as RbfBendTwistOrderPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_multi_bend_twist_falloff_weight import (
    BdRbfMultiBendTwistFalloffWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_multi_bend_twist_falloff_weight import (
    FalloffEnumPlugOperator as RbfMultiBendTwistFalloffPlugOperator,
    FalloffStatusEnumPlugOperator as RbfMultiBendTwistFalloffStatusPlugOperator,
    ModeEnumPlugOperator as RbfMultiBendTwistModePlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_multi_orientation_weight import (
    BdRbfMultiOrientationWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_multi_orientation_weight import (
    KernelEnumPlugOperator as RbfMultiOrientationKernelPlugOperator,
    SolveStatusEnumPlugOperator as RbfMultiOrientationSolveStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_multi_orientation_falloff_weight import (
    BdRbfMultiOrientationFalloffWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_multi_orientation_falloff_weight import (
    FalloffEnumPlugOperator as RbfMultiOrientationFalloffPlugOperator,
    FalloffStatusEnumPlugOperator as RbfMultiOrientationFalloffStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_multi_position_falloff_weight import (
    BdRbfMultiPositionFalloffWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_multi_position_falloff_weight import (
    FalloffEnumPlugOperator as RbfMultiPositionFalloffPlugOperator,
    FalloffStatusEnumPlugOperator as RbfMultiPositionFalloffStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_multi_position_weight import (
    BdRbfMultiPositionWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_multi_position_weight import (
    KernelEnumPlugOperator as RbfMultiPositionKernelPlugOperator,
    SolveStatusEnumPlugOperator as RbfMultiPositionSolveStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_orientation_falloff_weight import (
    BdRbfOrientationFalloffWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_orientation_falloff_weight import (
    FalloffEnumPlugOperator as RbfOrientationFalloffPlugOperator,
    FalloffStatusEnumPlugOperator as RbfOrientationFalloffStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_orientation_weight import (
    BdRbfOrientationWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_orientation_weight import (
    KernelEnumPlugOperator as RbfKernelPlugOperator,
    SolveStatusEnumPlugOperator as RbfSolveStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_position_falloff_weight import (
    BdRbfPositionFalloffWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_position_falloff_weight import (
    FalloffEnumPlugOperator as RbfPositionFalloffPlugOperator,
    FalloffStatusEnumPlugOperator as RbfPositionFalloffStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_position_weight import (
    BdRbfPositionWeight,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_position_weight import (
    KernelEnumPlugOperator as RbfPositionKernelPlugOperator,
    SolveStatusEnumPlugOperator as RbfPositionSolveStatusPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_rbf_pose_blend import (
    BdRbfPoseBlend,
)
from bd_util.maya.node.operator.node.dg._generated.bd_rbf_pose_blend import (
    BlendStatusEnumPlugOperator as RbfBlendStatusPlugOperator,
    RotateOrderEnumPlugOperator as RbfBlendRotateOrderPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_euler_value import BdEulerValue
from bd_util.maya.node.operator.node.dg._generated.bd_euler_value import (
    RotateOrderEnumAttrOperator as EulerValueRotateOrderAttrOperator,
    RotateOrderEnumPlugOperator as EulerValueRotateOrderPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_quat_compose_bend_twist import (
    BdQuatComposeBendTwist,
)
from bd_util.maya.node.operator.node.dg.bd_quat_decompose_bend_twist import (
    BdQuatDecomposeBendTwist,
)
from bd_util.maya.node.operator.node.dg.bd_quat_decompose_twist import (
    BdQuatDecomposeTwist,
)
from bd_util.maya.node.operator.node.dg.bd_quat_limit_bend_twist import (
    BdQuatLimitBendTwist,
)
from bd_util.maya.node.operator.node.dg._generated.bd_quat_limit_bend_twist import (
    BendLimitModeEnumAttrOperator as LimitModeAttrOperator,
    BendLimitModeEnumPlugOperator as LimitModePlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_euler_decompose_twist import (
    BdEulerDecomposeTwist,
)
from bd_util.maya.node.operator.node.dg._generated.bd_euler_decompose_twist import (
    AxisRotateOrderEnumAttrOperator as EulerAxisRotateOrderEnumAttrOperator,
    AxisRotateOrderEnumPlugOperator as EulerAxisRotateOrderEnumPlugOperator,
    InputRotateOrderEnumAttrOperator as EulerInputRotateOrderEnumAttrOperator,
    InputRotateOrderEnumPlugOperator as EulerInputRotateOrderEnumPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_euler_decompose_bend_twist import (
    BdEulerDecomposeBendTwist,
)
from bd_util.maya.node.operator.node.dg.bd_euler_limit_bend_twist import (
    BdEulerLimitBendTwist,
)
from bd_util.maya.node.operator.node.dg._generated.bd_euler_decompose_bend_twist import (
    AxisRotateOrderEnumAttrOperator as EulerDecomposeAxisOrderAttrOperator,
    AxisRotateOrderEnumPlugOperator as EulerDecomposeAxisOrderPlugOperator,
    InputRotateOrderEnumAttrOperator as EulerDecomposeInputOrderAttrOperator,
    InputRotateOrderEnumPlugOperator as EulerDecomposeInputOrderPlugOperator,
    OrderEnumAttrOperator as EulerDecomposeOrderAttrOperator,
    OrderEnumPlugOperator as EulerDecomposeOrderPlugOperator,
)
from bd_util.maya.node.operator.node.dg.bd_euler_compose_bend_twist import (
    BdEulerComposeBendTwist,
)
from bd_util.maya.node.operator.node.dg._generated.bd_euler_compose_bend_twist import (
    AxisRotateOrderEnumAttrOperator as EulerComposeAxisOrderAttrOperator,
    AxisRotateOrderEnumPlugOperator as EulerComposeAxisOrderPlugOperator,
    OrderEnumAttrOperator as EulerComposeOrderAttrOperator,
    OrderEnumPlugOperator as EulerComposeOrderPlugOperator,
    OutputRotateOrderEnumAttrOperator as EulerComposeOutputOrderAttrOperator,
    OutputRotateOrderEnumPlugOperator as EulerComposeOutputOrderPlugOperator,
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
from bd_util.maya.node.operator.node.dg._generated.bd_dbl_l_right_triangle import (
    SolveForEnumAttrOperator,
    SolveForEnumPlugOperator,
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
from bd_util.maya.node.operator.node.dag._core import DAG
from bd_util.maya.node.operator.node.dag.shape._core import Shape
from bd_util.maya.node.operator.node.dag.shape.ai_area_light import AiAreaLight
from bd_util.maya.node.operator.node.dag.shape.ai_curve_collector import (
    AiCurveCollector,
)
from bd_util.maya.node.operator.node.dag.shape.ai_light_blocker import (
    AiLightBlocker,
)
from bd_util.maya.node.operator.node.dag.shape.ai_light_portal import (
    AiLightPortal,
)
from bd_util.maya.node.operator.node.dag.shape.ai_mesh_light import AiMeshLight
from bd_util.maya.node.operator.node.dag.shape.ai_photometric_light import (
    AiPhotometricLight,
)
from bd_util.maya.node.operator.node.dag.shape.ai_sky_dome_light import (
    AiSkyDomeLight,
)
from bd_util.maya.node.operator.node.dag.shape.ai_stand_in import AiStandIn
from bd_util.maya.node.operator.node.dag.shape.ai_volume import AiVolume
from bd_util.maya.node.operator.node.dag.shape.ambient_light import (
    AmbientLight,
)
from bd_util.maya.node.operator.node.dag.shape.angle_dimension import (
    AngleDimension,
)
from bd_util.maya.node.operator.node.dag.shape.annotation_shape import (
    AnnotationShape,
)
from bd_util.maya.node.operator.node.dag.shape.arc_length_dimension import (
    ArcLengthDimension,
)
from bd_util.maya.node.operator.node.dag.shape.area_light import AreaLight
from bd_util.maya.node.operator.node.dag.shape.base_lattice import BaseLattice
from bd_util.maya.node.operator.node.dag.shape.bezier_curve import BezierCurve
from bd_util.maya.node.operator.node.dag.shape.camera import Camera
from bd_util.maya.node.operator.node.dag.shape.cluster_flexor_shape import (
    ClusterFlexorShape,
)
from bd_util.maya.node.operator.node.dag.shape.cluster_handle import (
    ClusterHandle,
)
from bd_util.maya.node.operator.node.dag.shape.deform_bend import DeformBend
from bd_util.maya.node.operator.node.dag.shape.deform_flare import DeformFlare
from bd_util.maya.node.operator.node.dag.shape.deform_sine import DeformSine
from bd_util.maya.node.operator.node.dag.shape.deform_squash import (
    DeformSquash,
)
from bd_util.maya.node.operator.node.dag.shape.deform_twist import DeformTwist
from bd_util.maya.node.operator.node.dag.shape.deform_wave import DeformWave
from bd_util.maya.node.operator.node.dag.shape.directed_disc import (
    DirectedDisc,
)
from bd_util.maya.node.operator.node.dag.shape.directional_light import (
    DirectionalLight,
)
from bd_util.maya.node.operator.node.dag.shape.distance_dim_shape import (
    DistanceDimShape,
)
from bd_util.maya.node.operator.node.dag.shape.dropoff_locator import (
    DropoffLocator,
)
from bd_util.maya.node.operator.node.dag.shape.dynamic_constraint import (
    DynamicConstraint,
)
from bd_util.maya.node.operator.node.dag.shape.dyn_holder import DynHolder
from bd_util.maya.node.operator.node.dag.shape.environment_fog import (
    EnvironmentFog,
)
from bd_util.maya.node.operator.node.dag.shape.flexor_shape import FlexorShape
from bd_util.maya.node.operator.node.dag.shape.fluid_shape import FluidShape
from bd_util.maya.node.operator.node.dag.shape.fluid_texture2_d import (
    FluidTexture2D,
)
from bd_util.maya.node.operator.node.dag.shape.fluid_texture3_d import (
    FluidTexture3D,
)
from bd_util.maya.node.operator.node.dag.shape.follicle import Follicle
from bd_util.maya.node.operator.node.dag.shape.geo_connectable import (
    GeoConnectable,
)
from bd_util.maya.node.operator.node.dag.shape.grease_plane import GreasePlane
from bd_util.maya.node.operator.node.dag.shape.grease_plane_render_shape import (
    GreasePlaneRenderShape,
)
from bd_util.maya.node.operator.node.dag.shape.hair_constraint import (
    HairConstraint,
)
from bd_util.maya.node.operator.node.dag.shape.hair_system import HairSystem
from bd_util.maya.node.operator.node.dag.shape.height_field import HeightField
from bd_util.maya.node.operator.node.dag.shape.hik_floor_contact_marker import (
    HikFloorContactMarker,
)
from bd_util.maya.node.operator.node.dag.shape.image_plane import ImagePlane
from bd_util.maya.node.operator.node.dag.shape.implicit_box import ImplicitBox
from bd_util.maya.node.operator.node.dag.shape.implicit_cone import (
    ImplicitCone,
)
from bd_util.maya.node.operator.node.dag.shape.implicit_sphere import (
    ImplicitSphere,
)
from bd_util.maya.node.operator.node.dag.shape.lattice import Lattice
from bd_util.maya.node.operator.node.dag.shape.line_modifier import (
    LineModifier,
)
from bd_util.maya.node.operator.node.dag.shape.locator import Locator
from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh
from bd_util.maya.node.operator.node.dag.shape.motion_trail_shape import (
    MotionTrailShape,
)
from bd_util.maya.node.operator.node.dag.shape.n_cloth import NCloth
from bd_util.maya.node.operator.node.dag.shape.n_particle import NParticle
from bd_util.maya.node.operator.node.dag.shape.n_rigid import NRigid
from bd_util.maya.node.operator.node.dag.shape.nurbs_curve import NurbsCurve
from bd_util.maya.node.operator.node.dag.shape.nurbs_surface import (
    NurbsSurface,
)
from bd_util.maya.node.operator.node.dag.shape.orientation_marker import (
    OrientationMarker,
)
from bd_util.maya.node.operator.node.dag.shape.param_dimension import (
    ParamDimension,
)
from bd_util.maya.node.operator.node.dag.shape.particle import Particle
from bd_util.maya.node.operator.node.dag.shape.pfx_hair import PfxHair
from bd_util.maya.node.operator.node.dag.shape.pfx_toon import PfxToon
from bd_util.maya.node.operator.node.dag.shape.point_light import PointLight
from bd_util.maya.node.operator.node.dag.shape.position_marker import (
    PositionMarker,
)
from bd_util.maya.node.operator.node.dag.shape.render_box import RenderBox
from bd_util.maya.node.operator.node.dag.shape.render_cone import RenderCone
from bd_util.maya.node.operator.node.dag.shape.render_rect import RenderRect
from bd_util.maya.node.operator.node.dag.shape.render_sphere import (
    RenderSphere,
)
from bd_util.maya.node.operator.node.dag.shape.rigid_body import RigidBody
from bd_util.maya.node.operator.node.dag.shape.sketch_plane import SketchPlane
from bd_util.maya.node.operator.node.dag.shape.snapshot_shape import (
    SnapshotShape,
)
from bd_util.maya.node.operator.node.dag.shape.soft_mod_handle import (
    SoftModHandle,
)
from bd_util.maya.node.operator.node.dag.shape.spot_light import SpotLight
from bd_util.maya.node.operator.node.dag.shape.spring import Spring
from bd_util.maya.node.operator.node.dag.shape.stereo_rig_camera import (
    StereoRigCamera,
)
from bd_util.maya.node.operator.node.dag.shape.stroke import Stroke
from bd_util.maya.node.operator.node.dag.shape.subdiv import Subdiv
from bd_util.maya.node.operator.node.dag.shape.ufe_proxy_camera_shape import (
    UfeProxyCameraShape,
)
from bd_util.maya.node.operator.node.dag.shape.volume_light import VolumeLight
from bd_util.maya.node.operator.node.dag.unknown_dag import UnknownDag
from bd_util.maya.node.operator.node.dag.transform._core import Transform
from bd_util.maya.node.operator.node.dag.transform.aim_constraint import (
    AimConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.air_field import AirField
from bd_util.maya.node.operator.node.dag.transform.base_geometry_var_group import (
    BaseGeometryVarGroup,
)
from bd_util.maya.node.operator.node.dag.transform.clip_ghost_shape import (
    ClipGhostShape,
)
from bd_util.maya.node.operator.node.dag.transform.collision_model import (
    CollisionModel,
)
from bd_util.maya.node.operator.node.dag.transform.curve_var_group import (
    CurveVarGroup,
)
from bd_util.maya.node.operator.node.dag.transform.dag_container import (
    DagContainer,
)
from bd_util.maya.node.operator.node.dag.transform.drag_field import DragField
from bd_util.maya.node.operator.node.dag.transform.fluid_emitter import (
    FluidEmitter,
)
from bd_util.maya.node.operator.node.dag.transform.foster_parent import (
    FosterParent,
)
from bd_util.maya.node.operator.node.dag.transform.geometry_constraint import (
    GeometryConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.geometry_var_group import (
    GeometryVarGroup,
)
from bd_util.maya.node.operator.node.dag.transform.gravity_field import (
    GravityField,
)
from bd_util.maya.node.operator.node.dag.transform.hik_effector import (
    HikEffector,
)
from bd_util.maya.node.operator.node.dag.transform.hik_fk_joint import (
    HikFKJoint,
)
from bd_util.maya.node.operator.node.dag.transform.hik_ground_plane import (
    HikGroundPlane,
)
from bd_util.maya.node.operator.node.dag.transform.hik_handle import HikHandle
from bd_util.maya.node.operator.node.dag.transform.hik_ik_effector import (
    HikIKEffector,
)
from bd_util.maya.node.operator.node.dag.transform.ik_effector import (
    IkEffector,
)
from bd_util.maya.node.operator.node.dag.transform.ik_handle import IkHandle
from bd_util.maya.node.operator.node.dag.transform.instancer import Instancer
from bd_util.maya.node.operator.node.dag.transform.joint import Joint
from bd_util.maya.node.operator.node.dag.transform.lod_group import LodGroup
from bd_util.maya.node.operator.node.dag.transform.look_at import LookAt
from bd_util.maya.node.operator.node.dag.transform.mesh_var_group import (
    MeshVarGroup,
)
from bd_util.maya.node.operator.node.dag.transform.normal_constraint import (
    NormalConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.newton_field import (
    NewtonField,
)
from bd_util.maya.node.operator.node.dag.transform.nucleus import Nucleus
from bd_util.maya.node.operator.node.dag.transform.old_normal_constraint import (
    OldNormalConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.old_tangent_constraint import (
    OldTangentConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.orient_constraint import (
    OrientConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.parent_constraint import (
    ParentConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.point_constraint import (
    PointConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.point_emitter import (
    PointEmitter,
)
from bd_util.maya.node.operator.node.dag.transform.place3d_texture import (
    Place3dTexture,
)
from bd_util.maya.node.operator.node.dag.transform.point_on_poly_constraint import (
    PointOnPolyConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.pole_vector_constraint import (
    PoleVectorConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.primitive_falloff import (
    PrimitiveFalloff,
)
from bd_util.maya.node.operator.node.dag.transform.radial_field import (
    RadialField,
)
from bd_util.maya.node.operator.node.dag.transform.rigid_constraint import (
    RigidConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.scale_constraint import (
    ScaleConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.symmetry_constraint import (
    SymmetryConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.subdiv_surface_var_group import (
    SubdivSurfaceVarGroup,
)
from bd_util.maya.node.operator.node.dag.transform.surface_var_group import (
    SurfaceVarGroup,
)
from bd_util.maya.node.operator.node.dag.transform.tangent_constraint import (
    TangentConstraint,
)
from bd_util.maya.node.operator.node.dag.transform.texture_deformer_handle import (
    TextureDeformerHandle,
)
from bd_util.maya.node.operator.node.dag.transform.turbulence_field import (
    TurbulenceField,
)
from bd_util.maya.node.operator.node.dag.transform.uniform_field import (
    UniformField,
)
from bd_util.maya.node.operator.node.dag.transform.ufe_proxy_transform import (
    UfeProxyTransform,
)
from bd_util.maya.node.operator.node.dag.transform.unknown_transform import (
    UnknownTransform,
)
from bd_util.maya.node.operator.node.dag.transform.volume_axis_field import (
    VolumeAxisField,
)
from bd_util.maya.node.operator.node.dag.transform.vortex_field import (
    VortexField,
)


def generic_dag_existing_contract(
    nodes: bdu.Nodes,
    until: DAG,
    optional_until: DAG | None,
) -> None:
    unknown_dag = nodes.existing.unknownDag("existing_unknown_dag")

    assert_type(unknown_dag, UnknownDag)
    assert_type(unknown_dag.visibility, BoolPlugOperator)
    assert_type(unknown_dag.children(), tuple[DAG, ...])
    assert_type(unknown_dag.children(filter_type=None), tuple[DAG, ...])
    assert_type(
        unknown_dag.children(include_shapes=False),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.children(filter_type=nodes.types.DAG),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.children(filter_type=nodes.types.Transform),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.children(
            filter_type=nodes.types.Transform,
            include_shapes=False,
        ),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.children(
            filter_type=nodes.types.Transform,
            include_subclasses=False,
        ),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.children(filter_type=nodes.types.Shape),
        tuple[Shape, ...],
    )
    assert_type(
        unknown_dag.children(filter_type=nodes.types.Locator),
        tuple[Locator, ...],
    )
    assert_type(unknown_dag.ancestors(), tuple[DAG, ...])
    assert_type(unknown_dag.ancestors(filter_type=None), tuple[DAG, ...])
    assert_type(unknown_dag.ancestors(until=None), tuple[DAG, ...])
    assert_type(
        unknown_dag.ancestors(until=until),
        tuple[DAG, ...] | None,
    )
    assert_type(
        unknown_dag.ancestors(until=optional_until),
        tuple[DAG, ...] | None,
    )
    assert_type(
        unknown_dag.ancestors(filter_type=nodes.types.DAG),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.ancestors(filter_type=nodes.types.Transform),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.ancestors(
            filter_type=nodes.types.Transform,
            until=until,
        ),
        tuple[Transform, ...] | None,
    )
    assert_type(
        unknown_dag.ancestors(
            filter_type=nodes.types.Transform,
            until=optional_until,
        ),
        tuple[Transform, ...] | None,
    )
    assert_type(
        unknown_dag.ancestors(
            filter_type=nodes.types.Transform,
            include_subclasses=False,
        ),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.ancestors(filter_type=nodes.types.Shape),
        tuple[Shape, ...],
    )
    assert_type(
        unknown_dag.ancestors(filter_type=nodes.types.Locator),
        tuple[Locator, ...],
    )
    assert_type(unknown_dag.descendants(), tuple[DAG, ...])
    assert_type(unknown_dag.descendants(filter_type=None), tuple[DAG, ...])
    assert_type(
        unknown_dag.descendants(include_shapes=False),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.descendants(filter_type=nodes.types.DAG),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.descendants(filter_type=nodes.types.Transform),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.descendants(
            filter_type=nodes.types.Transform,
            include_shapes=False,
        ),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.descendants(
            filter_type=nodes.types.Transform,
            include_subclasses=False,
        ),
        tuple[Transform, ...],
    )
    assert_type(
        unknown_dag.descendants(filter_type=nodes.types.Shape),
        tuple[Shape, ...],
    )
    assert_type(
        unknown_dag.descendants(filter_type=nodes.types.Locator),
        tuple[Locator, ...],
    )
    assert_type(unknown_dag.descendant_chain(), tuple[DAG, ...])
    assert_type(unknown_dag.descendant_chain(1), tuple[DAG, ...])
    assert_type(
        unknown_dag.descendant_chain(child_index=1),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.descendant_chain(until=None),
        tuple[DAG, ...],
    )
    assert_type(
        unknown_dag.descendant_chain(until=until),
        tuple[DAG, ...] | None,
    )
    assert_type(
        unknown_dag.descendant_chain(
            child_index=1,
            until=until,
        ),
        tuple[DAG, ...] | None,
    )
    assert_type(
        unknown_dag.descendant_chain(until=optional_until),
        tuple[DAG, ...] | None,
    )


def node_types_contract(nodes: bdu.Nodes) -> None:
    assert_type(nodes.types.NodeOperator, type[NodeOperator])
    assert_type(nodes.types.DAG, type[DAG])
    assert_type(nodes.types.Transform, type[Transform])
    assert_type(nodes.types.Shape, type[Shape])
    assert_type(
        nodes.types.BaseGeometryVarGroup,
        type[BaseGeometryVarGroup],
    )
    assert_type(nodes.types.Locator, type[Locator])
    assert_type(nodes.types.UnknownDag, type[UnknownDag])
    assert_type(nodes.types.resolve("locator"), type[NodeOperator])


def transform_existing_contract(nodes: bdu.Nodes) -> None:
    handle = nodes.existing.ikHandle("existing_ik_handle")
    effector = nodes.existing.ikEffector("existing_ik_effector")
    aim_constraint = nodes.existing.aimConstraint("existing_aim_constraint")
    geometry_constraint = nodes.existing.geometryConstraint(
        "existing_geometry_constraint"
    )
    normal_constraint = nodes.existing.normalConstraint(
        "existing_normal_constraint"
    )
    old_normal_constraint = nodes.existing.oldNormalConstraint(
        "existing_old_normal_constraint"
    )
    old_tangent_constraint = nodes.existing.oldTangentConstraint(
        "existing_old_tangent_constraint"
    )
    orient_constraint = nodes.existing.orientConstraint(
        "existing_orient_constraint"
    )
    parent_constraint = nodes.existing.parentConstraint(
        "existing_parent_constraint"
    )
    point_constraint = nodes.existing.pointConstraint(
        "existing_point_constraint"
    )
    point_on_poly_constraint = nodes.existing.pointOnPolyConstraint(
        "existing_point_on_poly_constraint"
    )
    pole_vector_constraint = nodes.existing.poleVectorConstraint(
        "existing_pole_vector_constraint"
    )
    rigid_constraint = nodes.existing.rigidConstraint(
        "existing_rigid_constraint"
    )
    scale_constraint = nodes.existing.scaleConstraint(
        "existing_scale_constraint"
    )
    symmetry_constraint = nodes.existing.symmetryConstraint(
        "existing_symmetry_constraint"
    )
    tangent_constraint = nodes.existing.tangentConstraint(
        "existing_tangent_constraint"
    )
    air_field = nodes.existing.airField("existing_air_field")
    drag_field = nodes.existing.dragField("existing_drag_field")
    fluid_emitter = nodes.existing.fluidEmitter("existing_fluid_emitter")
    gravity_field = nodes.existing.gravityField("existing_gravity_field")
    newton_field = nodes.existing.newtonField("existing_newton_field")
    point_emitter = nodes.existing.pointEmitter("existing_point_emitter")
    radial_field = nodes.existing.radialField("existing_radial_field")
    turbulence_field = nodes.existing.turbulenceField(
        "existing_turbulence_field"
    )
    uniform_field = nodes.existing.uniformField("existing_uniform_field")
    volume_axis_field = nodes.existing.volumeAxisField(
        "existing_volume_axis_field"
    )
    vortex_field = nodes.existing.vortexField("existing_vortex_field")
    collision_model = nodes.existing.collisionModel("existing_collision_model")
    instancer = nodes.existing.instancer("existing_instancer")
    nucleus = nodes.existing.nucleus("existing_nucleus")
    primitive_falloff = nodes.existing.primitiveFalloff(
        "existing_primitive_falloff"
    )
    texture_deformer_handle = nodes.existing.textureDeformerHandle(
        "existing_texture_deformer_handle"
    )
    hik_effector = nodes.existing.hikEffector("existing_hik_effector")
    hik_fk_joint = nodes.existing.hikFKJoint("existing_hik_fk_joint")
    hik_ground_plane = nodes.existing.hikGroundPlane(
        "existing_hik_ground_plane"
    )
    hik_handle = nodes.existing.hikHandle("existing_hik_handle")
    hik_ik_effector = nodes.existing.hikIKEffector("existing_hik_ik_effector")
    clip_ghost_shape = nodes.existing.clipGhostShape(
        "existing_clip_ghost_shape"
    )
    dag_container = nodes.existing.dagContainer("existing_dag_container")
    foster_parent = nodes.existing.fosterParent("existing_foster_parent")
    lod_group = nodes.existing.lodGroup("existing_lod_group")
    look_at = nodes.existing.lookAt("existing_look_at")
    place3d_texture = nodes.existing.place3dTexture("existing_place3d_texture")
    curve_var_group = nodes.existing.curveVarGroup("existing_curve_var_group")
    geometry_var_group = nodes.existing.geometryVarGroup(
        "existing_geometry_var_group"
    )
    mesh_var_group = nodes.existing.meshVarGroup("existing_mesh_var_group")
    subdiv_surface_var_group = nodes.existing.subdivSurfaceVarGroup(
        "existing_subdiv_surface_var_group"
    )
    surface_var_group = nodes.existing.surfaceVarGroup(
        "existing_surface_var_group"
    )
    ufe_proxy_transform = nodes.existing.ufeProxyTransform(
        "existing_ufe_proxy_transform"
    )
    unknown_transform = nodes.existing.unknownTransform(
        "existing_unknown_transform"
    )

    assert_type(handle, IkHandle)
    assert_type(handle.ikBlend, DoublePlugOperator)
    assert_type(effector, IkEffector)
    assert_type(effector.hideDisplay, BoolPlugOperator)
    assert_type(aim_constraint, AimConstraint)
    assert_type(geometry_constraint, GeometryConstraint)
    assert_type(normal_constraint, NormalConstraint)
    assert_type(old_normal_constraint, OldNormalConstraint)
    assert_type(old_tangent_constraint, OldTangentConstraint)
    assert_type(orient_constraint, OrientConstraint)
    assert_type(parent_constraint, ParentConstraint)
    assert_type(parent_constraint.lockOutput, BoolPlugOperator)
    assert_type(point_constraint, PointConstraint)
    assert_type(point_on_poly_constraint, PointOnPolyConstraint)
    assert_type(pole_vector_constraint, PoleVectorConstraint)
    assert_type(rigid_constraint, RigidConstraint)
    assert_type(rigid_constraint.springStiffness, DoublePlugOperator)
    assert_type(scale_constraint, ScaleConstraint)
    assert_type(symmetry_constraint, SymmetryConstraint)
    assert_type(tangent_constraint, TangentConstraint)
    assert_type(air_field, AirField)
    assert_type(air_field.magnitude, DoublePlugOperator)
    assert_type(drag_field, DragField)
    assert_type(fluid_emitter, FluidEmitter)
    assert_type(fluid_emitter.rate, DoublePlugOperator)
    assert_type(gravity_field, GravityField)
    assert_type(newton_field, NewtonField)
    assert_type(point_emitter, PointEmitter)
    assert_type(radial_field, RadialField)
    assert_type(turbulence_field, TurbulenceField)
    assert_type(uniform_field, UniformField)
    assert_type(volume_axis_field, VolumeAxisField)
    assert_type(volume_axis_field.magnitude, DoublePlugOperator)
    assert_type(vortex_field, VortexField)
    assert_type(collision_model, CollisionModel)
    assert_type(collision_model.resilience, DoublePlugOperator)
    assert_type(instancer, Instancer)
    assert_type(instancer.displayPercentage, DoublePlugOperator)
    assert_type(nucleus, Nucleus)
    assert_type(nucleus.gravity, FloatPlugOperator)
    assert_type(primitive_falloff, PrimitiveFalloff)
    assert_type(primitive_falloff.start, DoublePlugOperator)
    assert_type(texture_deformer_handle, TextureDeformerHandle)
    assert_type(texture_deformer_handle.visibility, BoolPlugOperator)
    assert_type(hik_effector, HikEffector)
    assert_type(hik_effector.reachTranslation, DoublePlugOperator)
    assert_type(hik_fk_joint, HikFKJoint)
    assert_type(hik_fk_joint.segmentScaleCompensate, BoolPlugOperator)
    assert_type(hik_ground_plane, HikGroundPlane)
    assert_type(hik_ground_plane.length, DoublePlugOperator)
    assert_type(hik_handle, HikHandle)
    assert_type(hik_handle.ikBlend, DoublePlugOperator)
    assert_type(hik_ik_effector, HikIKEffector)
    assert_type(hik_ik_effector.reachRotation, DoublePlugOperator)

    joint_base: Joint = hik_fk_joint
    ik_handle_base: IkHandle = hik_handle
    assert joint_base is hik_fk_joint
    assert ik_handle_base is hik_handle
    assert_type(clip_ghost_shape, ClipGhostShape)
    assert_type(clip_ghost_shape.showStartPose, BoolPlugOperator)
    assert_type(dag_container, DagContainer)
    assert_type(dag_container.visibility, BoolPlugOperator)
    assert_type(foster_parent, FosterParent)
    assert_type(foster_parent.visibility, BoolPlugOperator)
    assert_type(lod_group, LodGroup)
    assert_type(lod_group.minDistance, DoublePlugOperator)
    assert_type(look_at, LookAt)
    assert_type(look_at.distanceBetween, DoublePlugOperator)
    assert_type(look_at.lockOutput, BoolPlugOperator)
    assert_type(place3d_texture, Place3dTexture)
    assert_type(place3d_texture.visibility, BoolPlugOperator)

    aim_constraint_base: AimConstraint = look_at
    assert aim_constraint_base is look_at
    assert_type(curve_var_group, CurveVarGroup)
    assert_type(curve_var_group.maxCreated, LongPlugOperator)
    assert_type(curve_var_group.create_, DataNurbsCurvePlugOperator)
    assert_type(geometry_var_group, GeometryVarGroup)
    assert_type(geometry_var_group.create_, TypedPlugOperator)
    assert_type(mesh_var_group, MeshVarGroup)
    assert_type(mesh_var_group.create_, DataMeshPlugOperator)
    assert_type(subdiv_surface_var_group, SubdivSurfaceVarGroup)
    assert_type(subdiv_surface_var_group.create_, TypedPlugOperator)
    assert_type(surface_var_group, SurfaceVarGroup)
    assert_type(surface_var_group.create_, DataNurbsSurfacePlugOperator)

    base_geometry_var_group: BaseGeometryVarGroup = curve_var_group
    assert base_geometry_var_group is curve_var_group
    assert_type(ufe_proxy_transform, UfeProxyTransform)
    assert_type(ufe_proxy_transform.ufePath, DataStringPlugOperator)
    assert_type(unknown_transform, UnknownTransform)
    assert_type(unknown_transform.visibility, BoolPlugOperator)


def transform_creation_contract(nodes: bdu.Nodes) -> None:
    parent = nodes.create.transform(name="transform_parent")

    aim_constraint = nodes.create.aimConstraint(parent=parent)
    ik_handle = nodes.create.ikHandle(parent=parent)
    air_field = nodes.create.airField(parent=parent)
    nucleus = nodes.create.nucleus(parent=parent)
    hik_effector = nodes.create.hikEffector(parent=parent)
    dag_container = nodes.create.dagContainer(parent=parent)
    curve_var_group = nodes.create.curveVarGroup(parent=parent)
    ufe_proxy_transform = nodes.create.ufeProxyTransform(parent=parent)
    unknown_transform = nodes.create.unknownTransform(parent=parent)

    assert_type(aim_constraint, AimConstraint)
    assert_type(aim_constraint.lockOutput, BoolPlugOperator)
    assert_type(ik_handle, IkHandle)
    assert_type(ik_handle.ikBlend, DoublePlugOperator)
    assert_type(air_field, AirField)
    assert_type(air_field.magnitude, DoublePlugOperator)
    assert_type(nucleus, Nucleus)
    assert_type(nucleus.gravity, FloatPlugOperator)
    assert_type(hik_effector, HikEffector)
    assert_type(hik_effector.reachTranslation, DoublePlugOperator)
    assert_type(dag_container, DagContainer)
    assert_type(curve_var_group, CurveVarGroup)
    assert_type(curve_var_group.create_, DataNurbsCurvePlugOperator)
    assert_type(ufe_proxy_transform, UfeProxyTransform)
    assert_type(ufe_proxy_transform.ufePath, DataStringPlugOperator)
    assert_type(unknown_transform, UnknownTransform)


def shape_creation_contract(nodes: bdu.Nodes) -> None:
    parent = nodes.create.transform(name="shape_parent")
    assert_type(parent, Transform)

    mesh_transform, created_mesh = nodes.create.with_transform.mesh(
        name="mesh"
    )
    assert_type(mesh_transform, Transform)
    assert_type(created_mesh, Mesh)

    camera_transform, created_camera = nodes.create.with_transform.camera(
        name="camera",
        shape_name="renderCameraShape",
        parent=parent,
    )
    assert_type(camera_transform, Transform)
    assert_type(created_camera, Camera)

    dynamic_transform, dynamic_shape = nodes.create.with_transform.create(
        "mesh", name="dynamicMesh"
    )
    assert_type(dynamic_transform, Transform)
    assert_type(dynamic_shape, Shape)

    mesh = nodes.create.mesh(name="meshShape", parent=parent)
    assert_type(mesh, Mesh)
    assert_type(mesh.inMesh, DataMeshPlugOperator)
    assert_type(mesh.visibility, BoolPlugOperator)

    camera = nodes.create.camera(name="cameraShape", parent=parent)
    assert_type(camera, Camera)
    assert_type(camera.focalLength, DoublePlugOperator)

    locator = nodes.create.locator(name="locatorShape", parent=parent)
    assert_type(locator, Locator)
    assert_type(locator.localPosition, LocalPositionPlugOperator)

    curve = nodes.create.nurbsCurve(name="curveShape", parent=parent)
    assert_type(curve, NurbsCurve)
    assert_type(curve.create_, DataNurbsCurvePlugOperator)

    surface = nodes.create.nurbsSurface(name="surfaceShape", parent=parent)
    assert_type(surface, NurbsSurface)
    assert_type(surface.create_, DataNurbsSurfacePlugOperator)

    base_lattice = nodes.create.baseLattice(
        name="baseLatticeShape",
        parent=parent,
    )
    assert_type(base_lattice, BaseLattice)

    bezier_curve = nodes.create.bezierCurve(
        name="bezierCurveShape",
        parent=parent,
    )
    assert_type(bezier_curve, BezierCurve)
    assert_type(bezier_curve.create_, DataNurbsCurvePlugOperator)

    lattice = nodes.create.lattice(
        name="latticeShape",
        parent=parent,
    )
    assert_type(lattice, Lattice)

    subdiv = nodes.create.subdiv(
        name="subdivShape",
        parent=parent,
    )
    assert_type(subdiv, Subdiv)

    implicit_box = nodes.create.implicitBox(
        name="implicitBoxShape",
        parent=parent,
    )
    assert_type(implicit_box, ImplicitBox)

    implicit_cone = nodes.create.implicitCone(
        name="implicitConeShape",
        parent=parent,
    )
    assert_type(implicit_cone, ImplicitCone)

    implicit_sphere = nodes.create.implicitSphere(
        name="implicitSphereShape",
        parent=parent,
    )
    assert_type(implicit_sphere, ImplicitSphere)
    assert_type(
        implicit_sphere.radius,
        double_linear.DoubleLinearPlugOperator,
    )

    render_box = nodes.create.renderBox(
        name="renderBoxShape",
        parent=parent,
    )
    assert_type(render_box, RenderBox)

    render_cone = nodes.create.renderCone(
        name="renderConeShape",
        parent=parent,
    )
    assert_type(render_cone, RenderCone)

    render_rect = nodes.create.renderRect(
        name="renderRectShape",
        parent=parent,
    )
    assert_type(render_rect, RenderRect)

    render_sphere = nodes.create.renderSphere(
        name="renderSphereShape",
        parent=parent,
    )
    assert_type(render_sphere, RenderSphere)
    assert_type(
        render_sphere.radius,
        double_linear.DoubleLinearPlugOperator,
    )

    angle_dimension = nodes.create.angleDimension(
        name="angleDimensionShape",
        parent=parent,
    )
    assert_type(angle_dimension, AngleDimension)
    assert_type(angle_dimension.angle, DoubleAnglePlugOperator)

    annotation_shape = nodes.create.annotationShape(
        name="annotationShape",
        parent=parent,
    )
    assert_type(annotation_shape, AnnotationShape)
    assert_type(annotation_shape.text, DataStringPlugOperator)

    arc_length_dimension = nodes.create.arcLengthDimension(
        name="arcLengthDimensionShape",
        parent=parent,
    )
    assert_type(arc_length_dimension, ArcLengthDimension)
    assert_type(arc_length_dimension.arcLength, DoublePlugOperator)

    distance_dim_shape = nodes.create.distanceDimShape(
        name="distanceDimShape",
        parent=parent,
    )
    assert_type(distance_dim_shape, DistanceDimShape)
    assert_type(distance_dim_shape.distance, DoublePlugOperator)

    param_dimension = nodes.create.paramDimension(
        name="paramDimensionShape",
        parent=parent,
    )
    assert_type(param_dimension, ParamDimension)
    assert_type(param_dimension.uParamValue, DoublePlugOperator)

    cluster_flexor_shape = nodes.create.clusterFlexorShape(
        name="clusterFlexorShape",
        parent=parent,
    )
    assert_type(cluster_flexor_shape, ClusterFlexorShape)
    assert_type(cluster_flexor_shape.currentDriver, ShortPlugOperator)

    flexor_shape = nodes.create.flexorShape(
        name="flexorShape",
        parent=parent,
    )
    assert_type(flexor_shape, FlexorShape)
    assert_type(flexor_shape.currentDriver, ShortPlugOperator)

    geo_connectable = nodes.create.geoConnectable(
        name="geoConnectableShape",
        parent=parent,
    )
    assert_type(geo_connectable, GeoConnectable)
    assert_type(geo_connectable.doVelocity, BoolPlugOperator)

    cluster_handle = nodes.create.clusterHandle(
        name="clusterHandleShape",
        parent=parent,
    )
    assert_type(cluster_handle, ClusterHandle)
    assert_type(
        cluster_handle.originX,
        double_linear.DoubleLinearPlugOperator,
    )

    directed_disc = nodes.create.directedDisc(
        name="directedDiscShape",
        parent=parent,
    )
    assert_type(directed_disc, DirectedDisc)
    assert_type(directed_disc.primaryVisibility, BoolPlugOperator)

    dropoff_locator = nodes.create.dropoffLocator(
        name="dropoffLocatorShape",
        parent=parent,
    )
    assert_type(dropoff_locator, DropoffLocator)
    assert_type(dropoff_locator.percent, FloatPlugOperator)

    hik_floor_contact_marker = nodes.create.hikFloorContactMarker(
        name="hikFloorContactMarkerShape",
        parent=parent,
    )
    assert_type(hik_floor_contact_marker, HikFloorContactMarker)
    assert_type(hik_floor_contact_marker.markerSize, DoublePlugOperator)

    motion_trail_shape = nodes.create.motionTrailShape(
        name="motionTrailShape",
        parent=parent,
    )
    assert_type(motion_trail_shape, MotionTrailShape)
    assert_type(motion_trail_shape.showFrames, BoolPlugOperator)

    orientation_marker = nodes.create.orientationMarker(
        name="orientationMarkerShape",
        parent=parent,
    )
    assert_type(orientation_marker, OrientationMarker)
    assert_type(orientation_marker.frontTwist, DoubleAnglePlugOperator)

    position_marker = nodes.create.positionMarker(
        name="positionMarkerShape",
        parent=parent,
    )
    assert_type(position_marker, PositionMarker)
    assert_type(position_marker.time, TimePlugOperator)

    soft_mod_handle = nodes.create.softModHandle(
        name="softModHandleShape",
        parent=parent,
    )
    assert_type(soft_mod_handle, SoftModHandle)
    assert_type(
        soft_mod_handle.originX,
        double_linear.DoubleLinearPlugOperator,
    )

    deform_bend = nodes.create.deformBend(
        name="deformBendShape",
        parent=parent,
    )
    assert_type(deform_bend, DeformBend)
    assert_type(deform_bend.curvature, DoubleAnglePlugOperator)

    deform_flare = nodes.create.deformFlare(
        name="deformFlareShape",
        parent=parent,
    )
    assert_type(deform_flare, DeformFlare)
    assert_type(deform_flare.startFlareX, DoublePlugOperator)

    deform_sine = nodes.create.deformSine(
        name="deformSineShape",
        parent=parent,
    )
    assert_type(deform_sine, DeformSine)
    assert_type(deform_sine.amplitude, DoublePlugOperator)

    deform_squash = nodes.create.deformSquash(
        name="deformSquashShape",
        parent=parent,
    )
    assert_type(deform_squash, DeformSquash)
    assert_type(deform_squash.factor, DoublePlugOperator)

    deform_twist = nodes.create.deformTwist(
        name="deformTwistShape",
        parent=parent,
    )
    assert_type(deform_twist, DeformTwist)
    assert_type(deform_twist.startAngle, DoubleAnglePlugOperator)

    deform_wave = nodes.create.deformWave(
        name="deformWaveShape",
        parent=parent,
    )
    assert_type(deform_wave, DeformWave)
    assert_type(deform_wave.maxRadius, DoublePlugOperator)

    environment_fog = nodes.create.environmentFog(
        name="environmentFogShape",
        parent=parent,
    )
    assert_type(environment_fog, EnvironmentFog)
    assert_type(environment_fog.primaryVisibility, BoolPlugOperator)

    fluid_texture_2d = nodes.create.fluidTexture2D(
        name="fluidTexture2DShape",
        parent=parent,
    )
    assert_type(fluid_texture_2d, FluidTexture2D)
    assert_type(fluid_texture_2d.is2d, BoolPlugOperator)

    fluid_texture_3d = nodes.create.fluidTexture3D(
        name="fluidTexture3DShape",
        parent=parent,
    )
    assert_type(fluid_texture_3d, FluidTexture3D)
    assert_type(fluid_texture_3d.is2d, BoolPlugOperator)

    height_field = nodes.create.heightField(
        name="heightFieldShape",
        parent=parent,
    )
    assert_type(height_field, HeightField)
    assert_type(height_field.heightScale, FloatPlugOperator)

    dynamic_constraint = nodes.create.dynamicConstraint(
        name="dynamicConstraintShape",
        parent=parent,
    )
    assert_type(dynamic_constraint, DynamicConstraint)
    assert_type(dynamic_constraint.enable, BoolPlugOperator)

    dyn_holder = nodes.create.dynHolder(
        name="dynHolderShape",
        parent=parent,
    )
    assert_type(dyn_holder, DynHolder)
    assert_type(dyn_holder.connectionsToMe, MessagePlugOperator)

    follicle = nodes.create.follicle(
        name="follicleShape",
        parent=parent,
    )
    assert_type(follicle, Follicle)
    assert_type(follicle.parameterU, DoublePlugOperator)

    hair_constraint = nodes.create.hairConstraint(
        name="hairConstraintShape",
        parent=parent,
    )
    assert_type(hair_constraint, HairConstraint)
    assert_type(hair_constraint.stiffness, DoublePlugOperator)

    hair_system = nodes.create.hairSystem(
        name="hairSystemShape",
        parent=parent,
    )
    assert_type(hair_system, HairSystem)
    assert_type(hair_system.collideStrength, FloatPlugOperator)

    spring = nodes.create.spring(
        name="springShape",
        parent=parent,
    )
    assert_type(spring, Spring)
    assert_type(spring.useStiffnessPS, BoolPlugOperator)

    fluid_shape = nodes.create.fluidShape(
        name="fluidShape",
        parent=parent,
    )
    assert_type(fluid_shape, FluidShape)
    assert_type(fluid_shape.currentTime, TimePlugOperator)

    n_cloth = nodes.create.nCloth(
        name="nClothShape",
        parent=parent,
    )
    assert_type(n_cloth, NCloth)
    assert_type(n_cloth.thickness, FloatPlugOperator)

    n_particle = nodes.create.nParticle(
        name="nParticleShape",
        parent=parent,
    )
    assert_type(n_particle, NParticle)
    assert_type(n_particle.currentTime, TimePlugOperator)

    n_rigid = nodes.create.nRigid(
        name="nRigidShape",
        parent=parent,
    )
    assert_type(n_rigid, NRigid)
    assert_type(n_rigid.thickness, FloatPlugOperator)

    particle = nodes.create.particle(
        name="particleShape",
        parent=parent,
    )
    assert_type(particle, Particle)
    assert_type(particle.currentTime, TimePlugOperator)

    rigid_body = nodes.create.rigidBody(
        name="rigidBodyShape",
        parent=parent,
    )
    assert_type(rigid_body, RigidBody)
    assert_type(rigid_body.mass, DoublePlugOperator)

    grease_plane = nodes.create.greasePlane(
        name="greasePlaneShape",
        parent=parent,
    )
    assert_type(grease_plane, GreasePlane)
    assert_type(grease_plane.lockedToCamera, BoolPlugOperator)

    grease_plane_render_shape = nodes.create.greasePlaneRenderShape(
        name="greasePlaneRenderShape",
        parent=parent,
    )
    assert_type(grease_plane_render_shape, GreasePlaneRenderShape)
    assert_type(
        grease_plane_render_shape.visibleFraction,
        FloatPlugOperator,
    )

    line_modifier = nodes.create.lineModifier(
        name="lineModifierShape",
        parent=parent,
    )
    assert_type(line_modifier, LineModifier)
    assert_type(line_modifier.widthScale, DoublePlugOperator)

    pfx_hair = nodes.create.pfxHair(
        name="pfxHairShape",
        parent=parent,
    )
    assert_type(pfx_hair, PfxHair)
    assert_type(pfx_hair.drawAsMesh, BoolPlugOperator)

    pfx_toon = nodes.create.pfxToon(
        name="pfxToonShape",
        parent=parent,
    )
    assert_type(pfx_toon, PfxToon)
    assert_type(pfx_toon.displayPercent, DoublePlugOperator)

    stroke = nodes.create.stroke(
        name="strokeShape",
        parent=parent,
    )
    assert_type(stroke, Stroke)
    assert_type(stroke.motionBlurred, BoolPlugOperator)

    image_plane = nodes.create.imagePlane(
        name="imagePlaneShape",
        parent=parent,
    )
    assert_type(image_plane, ImagePlane)
    assert_type(image_plane.imageName, DataStringPlugOperator)

    sketch_plane = nodes.create.sketchPlane(
        name="sketchPlaneShape",
        parent=parent,
    )
    assert_type(sketch_plane, SketchPlane)
    assert_type(sketch_plane.primaryVisibility, BoolPlugOperator)

    snapshot_shape = nodes.create.snapshotShape(
        name="snapshotShape",
        parent=parent,
    )
    assert_type(snapshot_shape, SnapshotShape)
    assert_type(snapshot_shape.showFrames, BoolPlugOperator)

    stereo_rig_camera = nodes.create.stereoRigCamera(
        name="stereoRigCameraShape",
        parent=parent,
    )
    assert_type(stereo_rig_camera, StereoRigCamera)
    assert_type(stereo_rig_camera.focalLength, DoublePlugOperator)

    ufe_proxy_camera_shape = nodes.create.ufeProxyCameraShape(
        name="ufeProxyCameraShape",
        parent=parent,
    )
    assert_type(ufe_proxy_camera_shape, UfeProxyCameraShape)
    assert_type(ufe_proxy_camera_shape.focalLength, DoublePlugOperator)

    ambient_light = nodes.create.ambientLight(
        name="ambientLightShape",
        parent=parent,
    )
    assert_type(ambient_light, AmbientLight)

    area_light = nodes.create.areaLight(
        name="areaLightShape",
        parent=parent,
    )
    assert_type(area_light, AreaLight)
    assert_type(area_light.aiExposure, FloatPlugOperator)

    directional_light = nodes.create.directionalLight(
        name="directionalLightShape",
        parent=parent,
    )
    assert_type(directional_light, DirectionalLight)

    point_light = nodes.create.pointLight(
        name="pointLightShape",
        parent=parent,
    )
    assert_type(point_light, PointLight)

    spot_light = nodes.create.spotLight(
        name="spotLightShape",
        parent=parent,
    )
    assert_type(spot_light, SpotLight)

    volume_light = nodes.create.volumeLight(
        name="volumeLightShape",
        parent=parent,
    )
    assert_type(volume_light, VolumeLight)

    ai_area_light = nodes.create.aiAreaLight(
        name="aiAreaLightShape",
        parent=parent,
    )
    assert_type(ai_area_light, AiAreaLight)
    assert_type(ai_area_light.intensity, FloatPlugOperator)

    ai_light_portal = nodes.create.aiLightPortal(
        name="aiLightPortalShape",
        parent=parent,
    )
    assert_type(ai_light_portal, AiLightPortal)

    ai_mesh_light = nodes.create.aiMeshLight(
        name="aiMeshLightShape",
        parent=parent,
    )
    assert_type(ai_mesh_light, AiMeshLight)

    ai_photometric_light = nodes.create.aiPhotometricLight(
        name="aiPhotometricLightShape",
        parent=parent,
    )
    assert_type(ai_photometric_light, AiPhotometricLight)

    ai_sky_dome_light = nodes.create.aiSkyDomeLight(
        name="aiSkyDomeLightShape",
        parent=parent,
    )
    assert_type(ai_sky_dome_light, AiSkyDomeLight)

    ai_curve_collector = nodes.create.aiCurveCollector(
        name="aiCurveCollectorShape",
        parent=parent,
    )
    assert_type(ai_curve_collector, AiCurveCollector)

    ai_light_blocker = nodes.create.aiLightBlocker(
        name="aiLightBlockerShape",
        parent=parent,
    )
    assert_type(ai_light_blocker, AiLightBlocker)

    ai_stand_in = nodes.create.aiStandIn(
        name="aiStandInShape",
        parent=parent,
    )
    assert_type(ai_stand_in, AiStandIn)

    ai_volume = nodes.create.aiVolume(
        name="aiVolumeShape",
        parent=parent,
    )
    assert_type(ai_volume, AiVolume)

    assert_type(nodes.existing.mesh("existing_mesh"), Mesh)
    assert_type(nodes.existing.camera("existing_camera"), Camera)
    assert_type(nodes.existing.locator("existing_locator"), Locator)
    assert_type(nodes.existing.nurbsCurve("existing_curve"), NurbsCurve)
    assert_type(
        nodes.existing.nurbsSurface("existing_surface"),
        NurbsSurface,
    )
    assert_type(
        nodes.existing.ambientLight("existing_ambient_light"),
        AmbientLight,
    )
    assert_type(nodes.existing.nParticle("existing_n_particle"), NParticle)
    assert_type(nodes.existing.aiStandIn("existing_stand_in"), AiStandIn)
    assert_type(
        nodes.existing.baseLattice("existing_base_lattice"),
        BaseLattice,
    )


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

    quat_multi = nodes.create.bdQuat_MultiplyMulti(name="quat_multi")
    assert_type(quat_multi, BdQuatMultiplyMulti)
    assert_type(BdQuatMultiplyMulti.inputQuat, InputQuatAttrOperator)
    assert_type(quat_multi.inputQuat, InputQuatPlugOperator)
    assert_type(quat_multi.inputQuat[next], InputQuatPlugOperator)
    assert_type(BdQuatMultiplyMulti.outputQuat, OutputQuatAttrOperator)
    assert_type(quat_multi.outputQuat, OutputQuatPlugOperator)
    assert_type(quat_multi.outputQuat.get(), bdu.Quat)
    assert_type(
        nodes.existing.bdQuat_MultiplyMulti("existing_quat_multi"),
        BdQuatMultiplyMulti,
    )

    change_basis = nodes.create.bdQuat_ChangeBasis(name="change_basis")
    assert_type(change_basis, BdQuatChangeBasis)
    assert_type(
        BdQuatChangeBasis.inputQuat,
        ChangeBasisInputQuatAttrOperator,
    )
    assert_type(change_basis.inputQuat, ChangeBasisInputQuatPlugOperator)
    assert_type(change_basis.inputQuat.get(), bdu.Quat)
    assert_type(
        BdQuatChangeBasis.axisQuat,
        ChangeBasisAxisQuatAttrOperator,
    )
    assert_type(change_basis.axisQuat, ChangeBasisAxisQuatPlugOperator)
    assert_type(change_basis.axisQuat.get(), bdu.Quat)
    assert_type(
        BdQuatChangeBasis.direction,
        ChangeBasisDirectionAttrOperator,
    )
    assert_type(change_basis.direction, ChangeBasisDirectionPlugOperator)
    assert_type(
        BdQuatChangeBasis.outputQuat,
        ChangeBasisOutputQuatAttrOperator,
    )
    assert_type(change_basis.outputQuat, ChangeBasisOutputQuatPlugOperator)
    assert_type(change_basis.outputQuat.get(), bdu.Quat)
    assert_type(
        nodes.existing.bdQuat_ChangeBasis("existing_change_basis"),
        BdQuatChangeBasis,
    )

    quat_value = nodes.create.bdQuat_Value(name="quat_value")
    assert_type(quat_value, BdQuatValue)
    assert_type(BdQuatValue.value, QuatValueAttrOperator)
    assert_type(quat_value.value, QuatValuePlugOperator)
    assert_type(quat_value.value.get(), bdu.Quat)
    assert_type(
        nodes.existing.bdQuat_Value("existing_quat_value"),
        BdQuatValue,
    )

    rbf_bend_twist_falloff = nodes.create.bdRbf_BendTwistFalloffWeight(
        name="rbf_bend_twist_falloff"
    )
    assert_type(rbf_bend_twist_falloff, BdRbfBendTwistFalloffWeight)
    assert_type(
        BdRbfBendTwistFalloffWeight.inputQuat,
        RbfBendTwistInputQuatAttrOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.inputQuat,
        RbfBendTwistInputQuatPlugOperator,
    )
    assert_type(
        BdRbfBendTwistFalloffWeight.axisQuat,
        RbfBendTwistAxisQuatAttrOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.axisQuat,
        RbfBendTwistAxisQuatPlugOperator,
    )
    assert_type(
        BdRbfBendTwistFalloffWeight.pose,
        RbfBendTwistPoseAttrOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next],
        RbfBendTwistPosePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].poseQuat,
        RbfBendTwistPoseQuatPlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].enabled,
        BoolPlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].useRadiusOverride,
        BoolPlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].bendInnerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].bendOuterRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].twistInnerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.pose[next].twistOuterRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.order,
        RbfBendTwistOrderPlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.mode,
        RbfBendTwistModePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.bendInnerRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.bendOuterRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.twistInnerRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.twistOuterRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.falloff,
        RbfBendTwistFalloffPlugOperator,
    )
    assert_type(
        rbf_bend_twist_falloff.outputWeight[next],
        DoublePlugOperator,
    )
    assert_type(rbf_bend_twist_falloff.isValid, BoolPlugOperator)
    assert_type(
        rbf_bend_twist_falloff.falloffStatus,
        RbfBendTwistFalloffStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_BendTwistFalloffWeight(
            "existing_rbf_bend_twist_falloff"
        ),
        BdRbfBendTwistFalloffWeight,
    )

    rbf_multi_bend_twist_falloff = (
        nodes.create.bdRbf_MultiBendTwistFalloffWeight(
            name="rbf_multi_bend_twist_falloff"
        )
    )
    assert_type(
        rbf_multi_bend_twist_falloff,
        BdRbfMultiBendTwistFalloffWeight,
    )
    assert_type(
        BdRbfMultiBendTwistFalloffWeight.source,
        RbfMultiBendTwistSourceAttrOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.source[next],
        RbfMultiBendTwistSourcePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.source[next].inputQuat,
        RbfMultiBendTwistInputQuatPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.source[next].axisQuat,
        RbfMultiBendTwistAxisQuatPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.source[next].order,
        RbfMultiBendTwistOrderPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.source[next].influence,
        DoublePlugOperator,
    )
    assert_type(
        BdRbfMultiBendTwistFalloffWeight.pose,
        RbfMultiBendTwistPoseAttrOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next],
        RbfMultiBendTwistPosePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].sourceQuat[next],
        RbfMultiBendTwistPoseSourceQuatPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].enabled,
        BoolPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].useRadiusOverride,
        BoolPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].bendInnerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].bendOuterRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].twistInnerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.pose[next].twistOuterRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.mode,
        RbfMultiBendTwistModePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.bendInnerRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.bendOuterRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.twistInnerRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.twistOuterRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.falloff,
        RbfMultiBendTwistFalloffPlugOperator,
    )
    assert_type(
        rbf_multi_bend_twist_falloff.outputWeight[next],
        DoublePlugOperator,
    )
    assert_type(rbf_multi_bend_twist_falloff.isValid, BoolPlugOperator)
    assert_type(
        rbf_multi_bend_twist_falloff.falloffStatus,
        RbfMultiBendTwistFalloffStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_MultiBendTwistFalloffWeight(
            "existing_rbf_multi_bend_twist_falloff"
        ),
        BdRbfMultiBendTwistFalloffWeight,
    )

    rbf_multi_orientation = nodes.create.bdRbf_MultiOrientationWeight(
        name="rbf_multi_orientation"
    )
    assert_type(rbf_multi_orientation, BdRbfMultiOrientationWeight)
    assert_type(
        BdRbfMultiOrientationWeight.source,
        RbfMultiOrientationSourceAttrOperator,
    )
    assert_type(
        rbf_multi_orientation.source[next],
        RbfMultiOrientationSourcePlugOperator,
    )
    assert_type(
        rbf_multi_orientation.source[next].inputQuat,
        RbfMultiOrientationInputQuatPlugOperator,
    )
    assert_type(
        rbf_multi_orientation.source[next].influence,
        DoublePlugOperator,
    )
    assert_type(
        BdRbfMultiOrientationWeight.pose,
        RbfMultiOrientationPoseAttrOperator,
    )
    assert_type(
        rbf_multi_orientation.pose[next],
        RbfMultiOrientationPosePlugOperator,
    )
    assert_type(
        rbf_multi_orientation.pose[next].sourceQuat[next],
        RbfMultiOrientationPoseSourceQuatPlugOperator,
    )
    assert_type(rbf_multi_orientation.pose[next].enabled, BoolPlugOperator)
    assert_type(
        rbf_multi_orientation.kernel,
        RbfMultiOrientationKernelPlugOperator,
    )
    assert_type(rbf_multi_orientation.radius, DoubleAnglePlugOperator)
    assert_type(rbf_multi_orientation.regularization, DoublePlugOperator)
    assert_type(rbf_multi_orientation.allowNegativeWeights, BoolPlugOperator)
    assert_type(rbf_multi_orientation.outputWeight[next], DoublePlugOperator)
    assert_type(rbf_multi_orientation.isValid, BoolPlugOperator)
    assert_type(
        rbf_multi_orientation.solveStatus,
        RbfMultiOrientationSolveStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_MultiOrientationWeight(
            "existing_rbf_multi_orientation"
        ),
        BdRbfMultiOrientationWeight,
    )

    rbf_multi_orientation_falloff = (
        nodes.create.bdRbf_MultiOrientationFalloffWeight(
            name="rbf_multi_orientation_falloff"
        )
    )
    assert_type(
        rbf_multi_orientation_falloff,
        BdRbfMultiOrientationFalloffWeight,
    )
    assert_type(
        BdRbfMultiOrientationFalloffWeight.source,
        RbfMultiOrientationFalloffSourceAttrOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.source[next],
        RbfMultiOrientationFalloffSourcePlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.source[next].inputQuat,
        RbfMultiOrientationFalloffInputQuatPlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.source[next].influence,
        DoublePlugOperator,
    )
    assert_type(
        BdRbfMultiOrientationFalloffWeight.pose,
        RbfMultiOrientationFalloffPoseAttrOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.pose[next],
        RbfMultiOrientationFalloffPosePlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.pose[next].sourceQuat[next],
        RbfMultiOrientationFalloffPoseSourceQuatPlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.pose[next].enabled,
        BoolPlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.pose[next].useRadiusOverride,
        BoolPlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.pose[next].innerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.pose[next].outerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.innerRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.outerRadius,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.falloff,
        RbfMultiOrientationFalloffPlugOperator,
    )
    assert_type(
        rbf_multi_orientation_falloff.outputWeight[next],
        DoublePlugOperator,
    )
    assert_type(rbf_multi_orientation_falloff.isValid, BoolPlugOperator)
    assert_type(
        rbf_multi_orientation_falloff.falloffStatus,
        RbfMultiOrientationFalloffStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_MultiOrientationFalloffWeight(
            "existing_rbf_multi_orientation_falloff"
        ),
        BdRbfMultiOrientationFalloffWeight,
    )

    rbf_multi_position = nodes.create.bdRbf_MultiPositionWeight(
        name="rbf_multi_position"
    )
    assert_type(rbf_multi_position, BdRbfMultiPositionWeight)
    assert_type(
        BdRbfMultiPositionWeight.source,
        RbfMultiPositionSourceAttrOperator,
    )
    assert_type(
        rbf_multi_position.source[next],
        RbfMultiPositionSourcePlugOperator,
    )
    assert_type(
        rbf_multi_position.source[next].inputPosition,
        RbfMultiPositionInputPositionPlugOperator,
    )
    assert_type(rbf_multi_position.source[next].influence, DoublePlugOperator)
    assert_type(
        BdRbfMultiPositionWeight.pose,
        RbfMultiPositionPoseAttrOperator,
    )
    assert_type(
        rbf_multi_position.pose[next],
        RbfMultiPositionPosePlugOperator,
    )
    assert_type(
        rbf_multi_position.pose[next].sourcePosition[next],
        RbfMultiPositionPoseSourcePositionPlugOperator,
    )
    assert_type(rbf_multi_position.pose[next].enabled, BoolPlugOperator)
    assert_type(
        rbf_multi_position.kernel,
        RbfMultiPositionKernelPlugOperator,
    )
    assert_type(
        rbf_multi_position.radius,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(rbf_multi_position.regularization, DoublePlugOperator)
    assert_type(rbf_multi_position.allowNegativeWeights, BoolPlugOperator)
    assert_type(rbf_multi_position.outputWeight[next], DoublePlugOperator)
    assert_type(rbf_multi_position.isValid, BoolPlugOperator)
    assert_type(
        rbf_multi_position.solveStatus,
        RbfMultiPositionSolveStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_MultiPositionWeight(
            "existing_rbf_multi_position"
        ),
        BdRbfMultiPositionWeight,
    )

    rbf_multi_position_falloff = nodes.create.bdRbf_MultiPositionFalloffWeight(
        name="rbf_multi_position_falloff"
    )
    assert_type(
        rbf_multi_position_falloff,
        BdRbfMultiPositionFalloffWeight,
    )
    assert_type(
        BdRbfMultiPositionFalloffWeight.source,
        RbfMultiPositionFalloffSourceAttrOperator,
    )
    assert_type(
        rbf_multi_position_falloff.source[next],
        RbfMultiPositionFalloffSourcePlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.source[next].inputPosition,
        RbfMultiPositionFalloffInputPositionPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.source[next].influence,
        DoublePlugOperator,
    )
    assert_type(
        BdRbfMultiPositionFalloffWeight.pose,
        RbfMultiPositionFalloffPoseAttrOperator,
    )
    assert_type(
        rbf_multi_position_falloff.pose[next],
        RbfMultiPositionFalloffPosePlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.pose[next].sourcePosition[next],
        RbfMultiPositionFalloffPoseSourcePositionPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.pose[next].enabled,
        BoolPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.pose[next].useRadiusOverride,
        BoolPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.pose[next].innerRadiusOverride,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.pose[next].outerRadiusOverride,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.innerRadius,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.outerRadius,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.falloff,
        RbfMultiPositionFalloffPlugOperator,
    )
    assert_type(
        rbf_multi_position_falloff.outputWeight[next],
        DoublePlugOperator,
    )
    assert_type(rbf_multi_position_falloff.isValid, BoolPlugOperator)
    assert_type(
        rbf_multi_position_falloff.falloffStatus,
        RbfMultiPositionFalloffStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_MultiPositionFalloffWeight(
            "existing_rbf_multi_position_falloff"
        ),
        BdRbfMultiPositionFalloffWeight,
    )

    rbf_orientation_falloff = nodes.create.bdRbf_OrientationFalloffWeight(
        name="rbf_orientation_falloff"
    )
    assert_type(rbf_orientation_falloff, BdRbfOrientationFalloffWeight)
    assert_type(
        BdRbfOrientationFalloffWeight.inputQuat,
        RbfOrientationFalloffInputQuatAttrOperator,
    )
    assert_type(
        rbf_orientation_falloff.inputQuat,
        RbfOrientationFalloffInputQuatPlugOperator,
    )
    assert_type(
        BdRbfOrientationFalloffWeight.pose,
        RbfOrientationFalloffPoseAttrOperator,
    )
    assert_type(
        rbf_orientation_falloff.pose[next],
        RbfOrientationFalloffPosePlugOperator,
    )
    assert_type(
        rbf_orientation_falloff.pose[next].poseQuat,
        RbfOrientationFalloffPoseQuatPlugOperator,
    )
    assert_type(rbf_orientation_falloff.pose[next].enabled, BoolPlugOperator)
    assert_type(
        rbf_orientation_falloff.pose[next].useRadiusOverride,
        BoolPlugOperator,
    )
    assert_type(
        rbf_orientation_falloff.pose[next].innerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(
        rbf_orientation_falloff.pose[next].outerRadiusOverride,
        DoubleAnglePlugOperator,
    )
    assert_type(rbf_orientation_falloff.innerRadius, DoubleAnglePlugOperator)
    assert_type(rbf_orientation_falloff.outerRadius, DoubleAnglePlugOperator)
    assert_type(
        rbf_orientation_falloff.falloff,
        RbfOrientationFalloffPlugOperator,
    )
    assert_type(rbf_orientation_falloff.outputWeight[next], DoublePlugOperator)
    assert_type(rbf_orientation_falloff.isValid, BoolPlugOperator)
    assert_type(
        rbf_orientation_falloff.falloffStatus,
        RbfOrientationFalloffStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_OrientationFalloffWeight(
            "existing_rbf_orientation_falloff"
        ),
        BdRbfOrientationFalloffWeight,
    )

    rbf_orientation_weight = nodes.create.bdRbf_OrientationWeight(
        name="rbf_orientation_weight"
    )
    assert_type(rbf_orientation_weight, BdRbfOrientationWeight)
    assert_type(BdRbfOrientationWeight.inputQuat, RbfInputQuatAttrOperator)
    assert_type(rbf_orientation_weight.inputQuat, RbfInputQuatPlugOperator)
    assert_type(BdRbfOrientationWeight.pose, RbfPoseAttrOperator)
    assert_type(rbf_orientation_weight.pose[next], RbfPosePlugOperator)
    assert_type(
        rbf_orientation_weight.pose[next].poseQuat,
        RbfPoseQuatPlugOperator,
    )
    assert_type(rbf_orientation_weight.pose[next].enabled, BoolPlugOperator)
    assert_type(rbf_orientation_weight.kernel, RbfKernelPlugOperator)
    assert_type(rbf_orientation_weight.radius, DoubleAnglePlugOperator)
    assert_type(rbf_orientation_weight.regularization, DoublePlugOperator)
    assert_type(rbf_orientation_weight.allowNegativeWeights, BoolPlugOperator)
    assert_type(rbf_orientation_weight.outputWeight[next], DoublePlugOperator)
    assert_type(rbf_orientation_weight.isValid, BoolPlugOperator)
    assert_type(rbf_orientation_weight.solveStatus, RbfSolveStatusPlugOperator)
    assert_type(
        nodes.existing.bdRbf_OrientationWeight(
            "existing_rbf_orientation_weight"
        ),
        BdRbfOrientationWeight,
    )

    rbf_position_falloff_weight = nodes.create.bdRbf_PositionFalloffWeight(
        name="rbf_position_falloff_weight"
    )
    assert_type(rbf_position_falloff_weight, BdRbfPositionFalloffWeight)
    assert_type(
        BdRbfPositionFalloffWeight.inputPosition,
        RbfPositionFalloffInputAttrOperator,
    )
    assert_type(
        rbf_position_falloff_weight.inputPosition,
        RbfPositionFalloffInputPlugOperator,
    )
    assert_type(
        BdRbfPositionFalloffWeight.pose,
        RbfPositionFalloffPoseAttrOperator,
    )
    assert_type(
        rbf_position_falloff_weight.pose[next],
        RbfPositionFalloffPosePlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.pose[next].position,
        RbfPositionFalloffPosePositionPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.pose[next].enabled, BoolPlugOperator
    )
    assert_type(
        rbf_position_falloff_weight.pose[next].useRadiusOverride,
        BoolPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.pose[next].innerRadiusOverride,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.pose[next].outerRadiusOverride,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.innerRadius,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.outerRadius,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.falloff,
        RbfPositionFalloffPlugOperator,
    )
    assert_type(
        rbf_position_falloff_weight.outputWeight[next],
        DoublePlugOperator,
    )
    assert_type(rbf_position_falloff_weight.isValid, BoolPlugOperator)
    assert_type(
        rbf_position_falloff_weight.falloffStatus,
        RbfPositionFalloffStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_PositionFalloffWeight(
            "existing_rbf_position_falloff_weight"
        ),
        BdRbfPositionFalloffWeight,
    )

    rbf_position_weight = nodes.create.bdRbf_PositionWeight(
        name="rbf_position_weight"
    )
    assert_type(rbf_position_weight, BdRbfPositionWeight)
    assert_type(
        BdRbfPositionWeight.inputPosition,
        RbfPositionInputAttrOperator,
    )
    assert_type(
        rbf_position_weight.inputPosition,
        RbfPositionInputPlugOperator,
    )
    assert_type(
        BdRbfPositionWeight.pose,
        RbfPositionPoseAttrOperator,
    )
    assert_type(
        rbf_position_weight.pose[next],
        RbfPositionPosePlugOperator,
    )
    assert_type(
        rbf_position_weight.pose[next].position,
        RbfPositionPosePositionPlugOperator,
    )
    assert_type(rbf_position_weight.pose[next].enabled, BoolPlugOperator)
    assert_type(
        rbf_position_weight.kernel,
        RbfPositionKernelPlugOperator,
    )
    assert_type(
        rbf_position_weight.radius,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(rbf_position_weight.regularization, DoublePlugOperator)
    assert_type(rbf_position_weight.allowNegativeWeights, BoolPlugOperator)
    assert_type(rbf_position_weight.outputWeight[next], DoublePlugOperator)
    assert_type(rbf_position_weight.isValid, BoolPlugOperator)
    assert_type(
        rbf_position_weight.solveStatus,
        RbfPositionSolveStatusPlugOperator,
    )
    assert_type(
        nodes.existing.bdRbf_PositionWeight("existing_rbf_position_weight"),
        BdRbfPositionWeight,
    )

    rbf_pose_blend = nodes.create.bdRbf_PoseBlend(name="rbf_pose_blend")
    assert_type(rbf_pose_blend, BdRbfPoseBlend)
    assert_type(
        BdRbfPoseBlend.baseTranslate,
        RbfBlendBaseTranslateAttrOperator,
    )
    assert_type(
        rbf_pose_blend.baseTranslate,
        RbfBlendBaseTranslatePlugOperator,
    )
    assert_type(BdRbfPoseBlend.baseRotate, RbfBlendBaseRotateAttrOperator)
    assert_type(
        rbf_pose_blend.baseRotate,
        RbfBlendBaseRotatePlugOperator,
    )
    assert_type(BdRbfPoseBlend.baseScale, RbfBlendBaseScaleAttrOperator)
    assert_type(rbf_pose_blend.baseScale, RbfBlendBaseScalePlugOperator)
    assert_type(
        rbf_pose_blend.rotateOrder,
        RbfBlendRotateOrderPlugOperator,
    )
    assert_type(BdRbfPoseBlend.pose, RbfBlendPoseAttrOperator)
    assert_type(rbf_pose_blend.pose[next], RbfBlendPosePlugOperator)
    assert_type(
        rbf_pose_blend.pose[next].translate,
        RbfBlendPoseTranslatePlugOperator,
    )
    assert_type(
        rbf_pose_blend.pose[next].rotate,
        RbfBlendPoseRotatePlugOperator,
    )
    assert_type(
        rbf_pose_blend.pose[next].scale,
        RbfBlendPoseScalePlugOperator,
    )
    assert_type(rbf_pose_blend.pose[next].enabled, BoolPlugOperator)
    assert_type(rbf_pose_blend.weight[next], DoublePlugOperator)
    assert_type(
        BdRbfPoseBlend.outputTranslate,
        RbfBlendOutputTranslateAttrOperator,
    )
    assert_type(
        rbf_pose_blend.outputTranslate,
        RbfBlendOutputTranslatePlugOperator,
    )
    assert_type(
        BdRbfPoseBlend.outputRotate,
        RbfBlendOutputRotateAttrOperator,
    )
    assert_type(
        rbf_pose_blend.outputRotate,
        RbfBlendOutputRotatePlugOperator,
    )
    assert_type(
        BdRbfPoseBlend.outputQuat,
        RbfBlendOutputQuatAttrOperator,
    )
    assert_type(
        rbf_pose_blend.outputQuat,
        RbfBlendOutputQuatPlugOperator,
    )
    assert_type(
        BdRbfPoseBlend.outputScale,
        RbfBlendOutputScaleAttrOperator,
    )
    assert_type(
        rbf_pose_blend.outputScale,
        RbfBlendOutputScalePlugOperator,
    )
    assert_type(rbf_pose_blend.outputTranslate.get(), bdu.DoubleLinear3)
    assert_type(rbf_pose_blend.outputRotate.get(), bdu.DoubleAngle3)
    assert_type(rbf_pose_blend.outputQuat.get(), bdu.Quat)
    assert_type(rbf_pose_blend.outputScale.get(), bdu.Double3)
    assert_type(rbf_pose_blend.isValid, BoolPlugOperator)
    assert_type(rbf_pose_blend.blendStatus, RbfBlendStatusPlugOperator)
    assert_type(
        nodes.existing.bdRbf_PoseBlend("existing_rbf_pose_blend"),
        BdRbfPoseBlend,
    )

    euler_value = nodes.create.bdEuler_Value(name="euler_value")
    assert_type(euler_value, BdEulerValue)
    assert_type(BdEulerValue.value, EulerValueAttrOperator)
    assert_type(euler_value.value, EulerValuePlugOperator)
    assert_type(euler_value.value.get(), bdu.DoubleAngle3)
    assert_type(
        BdEulerValue.rotateOrder,
        EulerValueRotateOrderAttrOperator,
    )
    assert_type(
        euler_value.rotateOrder,
        EulerValueRotateOrderPlugOperator,
    )
    assert_type(
        nodes.existing.bdEuler_Value("existing_euler_value"),
        BdEulerValue,
    )

    compose_bend_twist = nodes.create.bdQuat_ComposeBendTwist(
        name="compose_bend_twist"
    )
    assert_type(compose_bend_twist, BdQuatComposeBendTwist)
    assert_type(BdQuatComposeBendTwist.input, BendTwistInputAttrOperator)
    assert_type(compose_bend_twist.input, BendTwistInputPlugOperator)
    assert_type(compose_bend_twist.input.get(), bdu.DoubleAngle3)
    assert_type(
        BdQuatComposeBendTwist.outputQuat,
        BendTwistOutputQuatAttrOperator,
    )
    assert_type(
        compose_bend_twist.outputQuat,
        BendTwistOutputQuatPlugOperator,
    )
    assert_type(compose_bend_twist.outputQuat.get(), bdu.Quat)

    decompose_bend_twist = nodes.create.bdQuat_DecomposeBendTwist(
        name="decompose_bend_twist"
    )
    assert_type(decompose_bend_twist, BdQuatDecomposeBendTwist)
    assert_type(
        BdQuatDecomposeBendTwist.inputQuat,
        BendTwistInputQuatAttrOperator,
    )
    assert_type(
        decompose_bend_twist.inputQuat,
        BendTwistInputQuatPlugOperator,
    )
    assert_type(
        BdQuatDecomposeBendTwist.output,
        BendTwistOutputAttrOperator,
    )
    assert_type(
        decompose_bend_twist.output,
        BendTwistOutputPlugOperator,
    )
    assert_type(decompose_bend_twist.output.get(), bdu.DoubleAngle3)
    assert_type(decompose_bend_twist.bendRatio, DoublePlugOperator)
    assert_type(decompose_bend_twist.bendRatio.get(), float)
    decompose_twist = nodes.create.bdQuat_DecomposeTwist(
        name="decompose_twist"
    )
    assert_type(decompose_twist, BdQuatDecomposeTwist)
    assert_type(decompose_twist.outputTwist.get(), float)
    assert_type(
        nodes.existing.bdQuat_ComposeBendTwist("existing_compose_bend_twist"),
        BdQuatComposeBendTwist,
    )
    assert_type(
        nodes.existing.bdQuat_DecomposeBendTwist(
            "existing_decompose_bend_twist"
        ),
        BdQuatDecomposeBendTwist,
    )
    assert_type(
        nodes.existing.bdQuat_DecomposeTwist("existing_decompose_twist"),
        BdQuatDecomposeTwist,
    )

    quat_limit = nodes.create.bdQuat_LimitBendTwist(name="quat_limit")
    assert_type(quat_limit, BdQuatLimitBendTwist)
    assert_type(BdQuatLimitBendTwist.min, LimitMinAttrOperator)
    assert_type(quat_limit.min, LimitMinPlugOperator)
    assert_type(quat_limit.min.get(), bdu.DoubleAngle3)
    assert_type(BdQuatLimitBendTwist.max, LimitMaxAttrOperator)
    assert_type(quat_limit.max, LimitMaxPlugOperator)
    assert_type(BdQuatLimitBendTwist.bendLimitMode, LimitModeAttrOperator)
    assert_type(quat_limit.bendLimitMode, LimitModePlugOperator)
    assert_type(
        BdQuatLimitBendTwist.outputQuat,
        LimitOutputQuatAttrOperator,
    )
    assert_type(quat_limit.outputQuat, LimitOutputQuatPlugOperator)
    assert_type(quat_limit.outputQuat.get(), bdu.Quat)
    assert_type(
        nodes.existing.bdQuat_LimitBendTwist("existing_quat_limit"),
        BdQuatLimitBendTwist,
    )

    euler_limit = nodes.create.bdEuler_LimitBendTwist(name="euler_limit")
    assert_type(euler_limit, BdEulerLimitBendTwist)
    assert_type(euler_limit.output.get(), bdu.DoubleAngle3)
    assert_type(euler_limit.outputRotate.get(), bdu.DoubleAngle3)
    assert_type(
        nodes.existing.bdEuler_LimitBendTwist("existing_euler_limit"),
        BdEulerLimitBendTwist,
    )

    euler_decompose_twist = nodes.create.bdEuler_DecomposeTwist(
        name="euler_decompose_twist"
    )
    assert_type(euler_decompose_twist, BdEulerDecomposeTwist)
    assert_type(BdEulerDecomposeTwist.inputRotate, InputRotateAttrOperator)
    assert_type(euler_decompose_twist.inputRotate, InputRotatePlugOperator)
    assert_type(euler_decompose_twist.inputRotate.get(), bdu.DoubleAngle3)
    assert_type(
        BdEulerDecomposeTwist.inputRotateOrder,
        EulerInputRotateOrderEnumAttrOperator,
    )
    assert_type(
        euler_decompose_twist.inputRotateOrder,
        EulerInputRotateOrderEnumPlugOperator,
    )
    assert_type(BdEulerDecomposeTwist.axisRotate, AxisRotateAttrOperator)
    assert_type(euler_decompose_twist.axisRotate, AxisRotatePlugOperator)
    assert_type(euler_decompose_twist.axisRotate.get(), bdu.DoubleAngle3)
    assert_type(
        BdEulerDecomposeTwist.axisRotateOrder,
        EulerAxisRotateOrderEnumAttrOperator,
    )
    assert_type(
        euler_decompose_twist.axisRotateOrder,
        EulerAxisRotateOrderEnumPlugOperator,
    )
    assert_type(euler_decompose_twist.outputTwist.get(), float)
    assert_type(
        nodes.existing.bdEuler_DecomposeTwist(
            "existing_euler_decompose_twist"
        ),
        BdEulerDecomposeTwist,
    )

    euler_decompose_bend_twist = nodes.create.bdEuler_DecomposeBendTwist(
        name="euler_decompose_bend_twist"
    )
    assert_type(euler_decompose_bend_twist, BdEulerDecomposeBendTwist)
    assert_type(
        BdEulerDecomposeBendTwist.inputRotate,
        EulerDecomposeInputRotateAttrOperator,
    )
    assert_type(
        euler_decompose_bend_twist.inputRotate,
        EulerDecomposeInputRotatePlugOperator,
    )
    assert_type(
        euler_decompose_bend_twist.inputRotate.get(),
        bdu.DoubleAngle3,
    )
    assert_type(
        BdEulerDecomposeBendTwist.inputRotateOrder,
        EulerDecomposeInputOrderAttrOperator,
    )
    assert_type(
        euler_decompose_bend_twist.inputRotateOrder,
        EulerDecomposeInputOrderPlugOperator,
    )
    assert_type(
        BdEulerDecomposeBendTwist.axisRotate,
        EulerDecomposeAxisRotateAttrOperator,
    )
    assert_type(
        euler_decompose_bend_twist.axisRotate,
        EulerDecomposeAxisRotatePlugOperator,
    )
    assert_type(
        BdEulerDecomposeBendTwist.axisRotateOrder,
        EulerDecomposeAxisOrderAttrOperator,
    )
    assert_type(
        euler_decompose_bend_twist.axisRotateOrder,
        EulerDecomposeAxisOrderPlugOperator,
    )
    assert_type(
        BdEulerDecomposeBendTwist.order,
        EulerDecomposeOrderAttrOperator,
    )
    assert_type(
        euler_decompose_bend_twist.order,
        EulerDecomposeOrderPlugOperator,
    )
    assert_type(
        BdEulerDecomposeBendTwist.output,
        EulerDecomposeOutputAttrOperator,
    )
    assert_type(
        euler_decompose_bend_twist.output,
        EulerDecomposeOutputPlugOperator,
    )
    assert_type(euler_decompose_bend_twist.output.get(), bdu.DoubleAngle3)
    assert_type(euler_decompose_bend_twist.bendRatio.get(), float)
    assert_type(
        nodes.existing.bdEuler_DecomposeBendTwist(
            "existing_euler_decompose_bend_twist"
        ),
        BdEulerDecomposeBendTwist,
    )

    euler_compose_bend_twist = nodes.create.bdEuler_ComposeBendTwist(
        name="euler_compose_bend_twist"
    )
    assert_type(euler_compose_bend_twist, BdEulerComposeBendTwist)
    assert_type(
        BdEulerComposeBendTwist.input,
        EulerComposeInputAttrOperator,
    )
    assert_type(
        euler_compose_bend_twist.input,
        EulerComposeInputPlugOperator,
    )
    assert_type(euler_compose_bend_twist.input.get(), bdu.DoubleAngle3)
    assert_type(
        BdEulerComposeBendTwist.axisRotate,
        EulerComposeAxisRotateAttrOperator,
    )
    assert_type(
        euler_compose_bend_twist.axisRotate,
        EulerComposeAxisRotatePlugOperator,
    )
    assert_type(
        BdEulerComposeBendTwist.axisRotateOrder,
        EulerComposeAxisOrderAttrOperator,
    )
    assert_type(
        euler_compose_bend_twist.axisRotateOrder,
        EulerComposeAxisOrderPlugOperator,
    )
    assert_type(
        BdEulerComposeBendTwist.order,
        EulerComposeOrderAttrOperator,
    )
    assert_type(
        euler_compose_bend_twist.order,
        EulerComposeOrderPlugOperator,
    )
    assert_type(
        BdEulerComposeBendTwist.outputRotateOrder,
        EulerComposeOutputOrderAttrOperator,
    )
    assert_type(
        euler_compose_bend_twist.outputRotateOrder,
        EulerComposeOutputOrderPlugOperator,
    )
    assert_type(
        BdEulerComposeBendTwist.outputRotate,
        EulerComposeOutputRotateAttrOperator,
    )
    assert_type(
        euler_compose_bend_twist.outputRotate,
        EulerComposeOutputRotatePlugOperator,
    )
    assert_type(
        euler_compose_bend_twist.outputRotate.get(),
        bdu.DoubleAngle3,
    )
    assert_type(
        nodes.existing.bdEuler_ComposeBendTwist(
            "existing_euler_compose_bend_twist"
        ),
        BdEulerComposeBendTwist,
    )

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
    assert_type(compose.outputMatrix.connect(("target", "input")), None)
    assert_type(compose.outputMatrix.connect_from("source.output"), None)
    assert_type(compose.outputMatrix.disconnect(["target", "input"]), None)
    assert_type(
        compose.outputMatrix.disconnect_from(["source", "output"]), None
    )

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


def double_linear_ratio_contract(nodes: bdu.Nodes) -> None:
    scalar = nodes.create.bdDbl_RatioDblL(name="scalar_ratio")
    assert_type(scalar, BdDblRatioDblL)
    assert_type(scalar.input, double_linear.DoubleLinearPlugOperator)
    assert_type(scalar.base, double_linear.DoubleLinearPlugOperator)
    assert_type(scalar.output, DoublePlugOperator)
    assert_type(scalar.output.get(), float)
    assert_type(
        nodes.existing.bdDbl_RatioDblL("existing_scalar_ratio"),
        BdDblRatioDblL,
    )

    vector = nodes.create.bdDbl3_RatioDblL3(name="vector_ratio")
    assert_type(vector, BdDbl3RatioDblL3)
    assert_type(vector.input, RatioDblL3InputPlugOperator)
    assert_type(vector.input.inputX, double_linear.DoubleLinearPlugOperator)
    assert_type(vector.base, RatioDblL3BasePlugOperator)
    assert_type(vector.base.baseY, double_linear.DoubleLinearPlugOperator)
    assert_type(vector.output, RatioDblL3OutputPlugOperator)
    assert_type(vector.output.outputZ, DoublePlugOperator)
    assert_type(vector.output.get(), bdu.Double3)
    assert_type(
        nodes.existing.bdDbl3_RatioDblL3("existing_vector_ratio"),
        BdDbl3RatioDblL3,
    )


def double_linear_right_triangle_contract(nodes: bdu.Nodes) -> None:
    node = nodes.create.bdDblL_RightTriangle(name="right_triangle")
    assert_type(node, BdDblLRightTriangle)
    assert_type(
        BdDblLRightTriangle.solveFor,
        SolveForEnumAttrOperator,
    )
    assert_type(node.solveFor, SolveForEnumPlugOperator)
    assert_type(node.legA, double_linear.DoubleLinearPlugOperator)
    assert_type(node.legB, double_linear.DoubleLinearPlugOperator)
    assert_type(node.hypotenuse, double_linear.DoubleLinearPlugOperator)
    assert_type(node.output, double_linear.DoubleLinearPlugOperator)
    assert_type(node.output.get(), float)
    assert_type(node.isValid, BoolPlugOperator)
    assert_type(node.isValid.get(), bool)
    assert_type(
        nodes.existing.bdDblL_RightTriangle("existing_right_triangle"),
        BdDblLRightTriangle,
    )


def invalid_usage_contract(
    nodes: bdu.Nodes,
    c: ComposeMatrix,
) -> None:
    nodes.create.composeMatrix(
        unknown_option=True  # pyright: ignore[reportCallIssue]
    )
    nodes.create.mesh()  # pyright: ignore[reportCallIssue]
    nodes.existing.decomposeMatrix(123)  # pyright: ignore[reportArgumentType]
    nodes.existing.unknownDag(
        "invalid_filter"
    ).children(  # pyright: ignore[reportCallIssue]
        filter_type=nodes.types.PlusMinusAverage  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag(
        "invalid_filter"
    ).ancestors(  # pyright: ignore[reportCallIssue]
        filter_type=nodes.types.PlusMinusAverage  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag(
        "invalid_filter"
    ).descendants(  # pyright: ignore[reportCallIssue]
        filter_type=nodes.types.PlusMinusAverage  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag("invalid_filter").children(
        include_subclasses=False  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag("invalid_filter").ancestors(
        include_subclasses=False  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag("invalid_filter").descendants(
        include_subclasses=False  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag("invalid_filter").children(
        include_shapes=0  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag("invalid_filter").descendants(
        include_shapes=0  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag("invalid_filter").ancestors(
        include_shapes=False  # pyright: ignore[reportCallIssue]
    )
    nodes.existing.unknownDag("invalid_filter").descendant_chain(
        child_index="0"  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag(
        "invalid_filter"
    ).ancestors(  # pyright: ignore[reportCallIssue]
        until=nodes.types.Transform  # pyright: ignore[reportArgumentType]
    )
    nodes.existing.unknownDag(
        "invalid_filter"
    ).descendant_chain(  # pyright: ignore[reportCallIssue]
        until=nodes.types.Transform  # pyright: ignore[reportArgumentType]
    )
    c.outputMatrix.set("not a matrix")  # pyright: ignore[reportArgumentType]
    c.inputTranslate.set("not a vector")  # pyright: ignore[reportArgumentType]
    nodes.create.wtAddMatrix().wtMatrix[
        len
    ]  # pyright: ignore[reportArgumentType]
    c.x  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
