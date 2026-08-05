#include <array>

#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/nodes/BdAnyConditionDblLNode.h"
#include "bdUtilNodes/nodes/BdAnyConditionDblLMultiNode.h"
#include "bdUtilNodes/nodes/BdAnyConditionDblNode.h"
#include "bdUtilNodes/nodes/BdAnyConditionDblMultiNode.h"
#include "bdUtilNodes/nodes/BdConditionDblCaseComposeNode.h"
#include "bdUtilNodes/nodes/BdConditionDblExtraComposeNode.h"
#include "bdUtilNodes/nodes/BdConditionDblLCaseComposeNode.h"
#include "bdUtilNodes/nodes/BdConditionDblLExtraComposeNode.h"
#include "bdUtilNodes/nodes/BdDbl3AbsNode.h"
#include "bdUtilNodes/nodes/BdDbl3AddNode.h"
#include "bdUtilNodes/nodes/BdDbl3AddMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3AverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3AverageNode.h"
#include "bdUtilNodes/nodes/BdDbl3ClampNode.h"
#include "bdUtilNodes/nodes/BdDbl3DivideNode.h"
#include "bdUtilNodes/nodes/BdDbl3DivideMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3LerpNode.h"
#include "bdUtilNodes/nodes/BdDbl3MapRangeNode.h"
#include "bdUtilNodes/nodes/BdDbl3MaxNode.h"
#include "bdUtilNodes/nodes/BdDbl3MaxMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3MinNode.h"
#include "bdUtilNodes/nodes/BdDbl3MinMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3NegateNode.h"
#include "bdUtilNodes/nodes/BdDblLerpNode.h"
#include "bdUtilNodes/nodes/BdDblMapRangeNode.h"
#include "bdUtilNodes/nodes/BdDblMaxNode.h"
#include "bdUtilNodes/nodes/BdDblMaxMultiNode.h"
#include "bdUtilNodes/nodes/BdDblMinNode.h"
#include "bdUtilNodes/nodes/BdDblMinMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3MultiplyNode.h"
#include "bdUtilNodes/nodes/BdDbl3MultiplyMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3PowerNode.h"
#include "bdUtilNodes/nodes/BdDbl3PowerMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3SubtractNode.h"
#include "bdUtilNodes/nodes/BdDbl3SubtractMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3WeightedAverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDblAbsNode.h"
#include "bdUtilNodes/nodes/BdDblAddNode.h"
#include "bdUtilNodes/nodes/BdDblAddMultiNode.h"
#include "bdUtilNodes/nodes/BdDblAverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDblAverageNode.h"
#include "bdUtilNodes/nodes/BdDblClampNode.h"
#include "bdUtilNodes/nodes/BdDblDivideNode.h"
#include "bdUtilNodes/nodes/BdDblDivideMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3ValueNode.h"
#include "bdUtilNodes/nodes/BdDblValueNode.h"
#include "bdUtilNodes/nodes/BdDblMultiplyNode.h"
#include "bdUtilNodes/nodes/BdDblMultiplyMultiNode.h"
#include "bdUtilNodes/nodes/BdDblNegateNode.h"
#include "bdUtilNodes/nodes/BdDblPowerNode.h"
#include "bdUtilNodes/nodes/BdDblPowerMultiNode.h"
#include "bdUtilNodes/nodes/BdDblSubtractNode.h"
#include "bdUtilNodes/nodes/BdDblSubtractMultiNode.h"
#include "bdUtilNodes/nodes/BdDblWeightedAverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3WeightedSumMultiNode.h"
#include "bdUtilNodes/nodes/BdDblWeightedSumMultiNode.h"

#include "bdUtilNodes/nodes/BdDblLValueNode.h"
#include "bdUtilNodes/nodes/BdDblL3ValueNode.h"
#include "bdUtilNodes/nodes/BdDblLAddNode.h"
#include "bdUtilNodes/nodes/BdDblLAddMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3AddNode.h"
#include "bdUtilNodes/nodes/BdDblL3AddMultiNode.h"
#include "bdUtilNodes/nodes/BdDblLSubtractNode.h"
#include "bdUtilNodes/nodes/BdDblLSubtractMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3SubtractNode.h"
#include "bdUtilNodes/nodes/BdDblL3SubtractMultiNode.h"
#include "bdUtilNodes/nodes/BdDblLAverageNode.h"
#include "bdUtilNodes/nodes/BdDblLAverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3AverageNode.h"
#include "bdUtilNodes/nodes/BdDblL3AverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDblLMinNode.h"
#include "bdUtilNodes/nodes/BdDblLMinMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3MinNode.h"
#include "bdUtilNodes/nodes/BdDblL3MinMultiNode.h"
#include "bdUtilNodes/nodes/BdDblLMaxNode.h"
#include "bdUtilNodes/nodes/BdDblLMaxMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3MaxNode.h"
#include "bdUtilNodes/nodes/BdDblL3MaxMultiNode.h"
#include "bdUtilNodes/nodes/BdDblLClampNode.h"
#include "bdUtilNodes/nodes/BdDblL3ClampNode.h"
#include "bdUtilNodes/nodes/BdDblLAbsNode.h"
#include "bdUtilNodes/nodes/BdDblL3AbsNode.h"
#include "bdUtilNodes/nodes/BdDblLNegateNode.h"
#include "bdUtilNodes/nodes/BdDblL3NegateNode.h"
#include "bdUtilNodes/nodes/BdDblLLerpNode.h"
#include "bdUtilNodes/nodes/BdDblL3LerpNode.h"
#include "bdUtilNodes/nodes/BdDblLMapRangeNode.h"
#include "bdUtilNodes/nodes/BdDblL3MapRangeNode.h"
#include "bdUtilNodes/nodes/BdDblLWeightedSumMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3WeightedSumMultiNode.h"
#include "bdUtilNodes/nodes/BdDblLWeightedAverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDblL3WeightedAverageMultiNode.h"

namespace {

struct NodeRegistration {
    const MString& typeName;
    const MTypeId& typeId;
    MCreatorFunction creator;
    MInitializeFunction initialize;
};

const std::array<NodeRegistration, 92>& nodeRegistrations() {
    static const std::array<NodeRegistration, 92> registrations = {{
        {
            BdDbl3MultiplyMultiNode::typeName,
            BdDbl3MultiplyMultiNode::typeId,
            BdDbl3MultiplyMultiNode::creator,
            BdDbl3MultiplyMultiNode::initialize,
        },
        {
            BdDbl3MultiplyNode::typeName,
            BdDbl3MultiplyNode::typeId,
            BdDbl3MultiplyNode::creator,
            BdDbl3MultiplyNode::initialize,
        },
        {
            BdDblMultiplyMultiNode::typeName,
            BdDblMultiplyMultiNode::typeId,
            BdDblMultiplyMultiNode::creator,
            BdDblMultiplyMultiNode::initialize,
        },
        {
            BdDblMultiplyNode::typeName,
            BdDblMultiplyNode::typeId,
            BdDblMultiplyNode::creator,
            BdDblMultiplyNode::initialize,
        },
        {
            BdDbl3AddMultiNode::typeName,
            BdDbl3AddMultiNode::typeId,
            BdDbl3AddMultiNode::creator,
            BdDbl3AddMultiNode::initialize,
        },
        {
            BdDbl3AddNode::typeName,
            BdDbl3AddNode::typeId,
            BdDbl3AddNode::creator,
            BdDbl3AddNode::initialize,
        },
        {
            BdDblAddMultiNode::typeName,
            BdDblAddMultiNode::typeId,
            BdDblAddMultiNode::creator,
            BdDblAddMultiNode::initialize,
        },
        {
            BdDblAddNode::typeName,
            BdDblAddNode::typeId,
            BdDblAddNode::creator,
            BdDblAddNode::initialize,
        },
        {
            BdDbl3SubtractMultiNode::typeName,
            BdDbl3SubtractMultiNode::typeId,
            BdDbl3SubtractMultiNode::creator,
            BdDbl3SubtractMultiNode::initialize,
        },
        {
            BdDbl3SubtractNode::typeName,
            BdDbl3SubtractNode::typeId,
            BdDbl3SubtractNode::creator,
            BdDbl3SubtractNode::initialize,
        },
        {
            BdDblSubtractMultiNode::typeName,
            BdDblSubtractMultiNode::typeId,
            BdDblSubtractMultiNode::creator,
            BdDblSubtractMultiNode::initialize,
        },
        {
            BdDblSubtractNode::typeName,
            BdDblSubtractNode::typeId,
            BdDblSubtractNode::creator,
            BdDblSubtractNode::initialize,
        },
        {
            BdDbl3DivideMultiNode::typeName,
            BdDbl3DivideMultiNode::typeId,
            BdDbl3DivideMultiNode::creator,
            BdDbl3DivideMultiNode::initialize,
        },
        {
            BdDbl3DivideNode::typeName,
            BdDbl3DivideNode::typeId,
            BdDbl3DivideNode::creator,
            BdDbl3DivideNode::initialize,
        },
        {
            BdDblDivideMultiNode::typeName,
            BdDblDivideMultiNode::typeId,
            BdDblDivideMultiNode::creator,
            BdDblDivideMultiNode::initialize,
        },
        {
            BdDblDivideNode::typeName,
            BdDblDivideNode::typeId,
            BdDblDivideNode::creator,
            BdDblDivideNode::initialize,
        },
        {
            BdDbl3PowerMultiNode::typeName,
            BdDbl3PowerMultiNode::typeId,
            BdDbl3PowerMultiNode::creator,
            BdDbl3PowerMultiNode::initialize,
        },
        {
            BdDbl3PowerNode::typeName,
            BdDbl3PowerNode::typeId,
            BdDbl3PowerNode::creator,
            BdDbl3PowerNode::initialize,
        },
        {
            BdDblPowerMultiNode::typeName,
            BdDblPowerMultiNode::typeId,
            BdDblPowerMultiNode::creator,
            BdDblPowerMultiNode::initialize,
        },
        {
            BdDblPowerNode::typeName,
            BdDblPowerNode::typeId,
            BdDblPowerNode::creator,
            BdDblPowerNode::initialize,
        },
        {
            BdDbl3LerpNode::typeName,
            BdDbl3LerpNode::typeId,
            BdDbl3LerpNode::creator,
            BdDbl3LerpNode::initialize,
        },
        {
            BdDblLerpNode::typeName,
            BdDblLerpNode::typeId,
            BdDblLerpNode::creator,
            BdDblLerpNode::initialize,
        },
        {
            BdDbl3WeightedSumMultiNode::typeName,
            BdDbl3WeightedSumMultiNode::typeId,
            BdDbl3WeightedSumMultiNode::creator,
            BdDbl3WeightedSumMultiNode::initialize,
        },
        {
            BdDblWeightedSumMultiNode::typeName,
            BdDblWeightedSumMultiNode::typeId,
            BdDblWeightedSumMultiNode::creator,
            BdDblWeightedSumMultiNode::initialize,
        },
        {
            BdDbl3MinMultiNode::typeName,
            BdDbl3MinMultiNode::typeId,
            BdDbl3MinMultiNode::creator,
            BdDbl3MinMultiNode::initialize,
        },
        {
            BdDbl3MinNode::typeName,
            BdDbl3MinNode::typeId,
            BdDbl3MinNode::creator,
            BdDbl3MinNode::initialize,
        },
        {
            BdDblMinMultiNode::typeName,
            BdDblMinMultiNode::typeId,
            BdDblMinMultiNode::creator,
            BdDblMinMultiNode::initialize,
        },
        {
            BdDblMinNode::typeName,
            BdDblMinNode::typeId,
            BdDblMinNode::creator,
            BdDblMinNode::initialize,
        },
        {
            BdDbl3MaxMultiNode::typeName,
            BdDbl3MaxMultiNode::typeId,
            BdDbl3MaxMultiNode::creator,
            BdDbl3MaxMultiNode::initialize,
        },
        {
            BdDbl3MaxNode::typeName,
            BdDbl3MaxNode::typeId,
            BdDbl3MaxNode::creator,
            BdDbl3MaxNode::initialize,
        },
        {
            BdDblMaxMultiNode::typeName,
            BdDblMaxMultiNode::typeId,
            BdDblMaxMultiNode::creator,
            BdDblMaxMultiNode::initialize,
        },
        {
            BdDblMaxNode::typeName,
            BdDblMaxNode::typeId,
            BdDblMaxNode::creator,
            BdDblMaxNode::initialize,
        },
        {
            BdDbl3ClampNode::typeName,
            BdDbl3ClampNode::typeId,
            BdDbl3ClampNode::creator,
            BdDbl3ClampNode::initialize,
        },
        {
            BdDblClampNode::typeName,
            BdDblClampNode::typeId,
            BdDblClampNode::creator,
            BdDblClampNode::initialize,
        },
        {
            BdDbl3MapRangeNode::typeName,
            BdDbl3MapRangeNode::typeId,
            BdDbl3MapRangeNode::creator,
            BdDbl3MapRangeNode::initialize,
        },
        {
            BdDblMapRangeNode::typeName,
            BdDblMapRangeNode::typeId,
            BdDblMapRangeNode::creator,
            BdDblMapRangeNode::initialize,
        },
        {
            BdDbl3AbsNode::typeName,
            BdDbl3AbsNode::typeId,
            BdDbl3AbsNode::creator,
            BdDbl3AbsNode::initialize,
        },
        {
            BdDblAbsNode::typeName,
            BdDblAbsNode::typeId,
            BdDblAbsNode::creator,
            BdDblAbsNode::initialize,
        },
        {
            BdDbl3NegateNode::typeName,
            BdDbl3NegateNode::typeId,
            BdDbl3NegateNode::creator,
            BdDbl3NegateNode::initialize,
        },
        {
            BdDblNegateNode::typeName,
            BdDblNegateNode::typeId,
            BdDblNegateNode::creator,
            BdDblNegateNode::initialize,
        },
        {
            BdAnyConditionDblNode::typeName,
            BdAnyConditionDblNode::typeId,
            BdAnyConditionDblNode::creator,
            BdAnyConditionDblNode::initialize,
        },
        {
            BdAnyConditionDblMultiNode::typeName,
            BdAnyConditionDblMultiNode::typeId,
            BdAnyConditionDblMultiNode::creator,
            BdAnyConditionDblMultiNode::initialize,
        },
        {
            BdDbl3AverageMultiNode::typeName,
            BdDbl3AverageMultiNode::typeId,
            BdDbl3AverageMultiNode::creator,
            BdDbl3AverageMultiNode::initialize,
        },
        {
            BdDbl3AverageNode::typeName,
            BdDbl3AverageNode::typeId,
            BdDbl3AverageNode::creator,
            BdDbl3AverageNode::initialize,
        },
        {
            BdDblAverageMultiNode::typeName,
            BdDblAverageMultiNode::typeId,
            BdDblAverageMultiNode::creator,
            BdDblAverageMultiNode::initialize,
        },
        {
            BdDblAverageNode::typeName,
            BdDblAverageNode::typeId,
            BdDblAverageNode::creator,
            BdDblAverageNode::initialize,
        },
        {
            BdDbl3WeightedAverageMultiNode::typeName,
            BdDbl3WeightedAverageMultiNode::typeId,
            BdDbl3WeightedAverageMultiNode::creator,
            BdDbl3WeightedAverageMultiNode::initialize,
        },
        {
            BdDblWeightedAverageMultiNode::typeName,
            BdDblWeightedAverageMultiNode::typeId,
            BdDblWeightedAverageMultiNode::creator,
            BdDblWeightedAverageMultiNode::initialize,
        },
        {
            BdDblValueNode::typeName,
            BdDblValueNode::typeId,
            BdDblValueNode::creator,
            BdDblValueNode::initialize,
        },
        {
            BdDbl3ValueNode::typeName,
            BdDbl3ValueNode::typeId,
            BdDbl3ValueNode::creator,
            BdDbl3ValueNode::initialize,
        },
        {
            BdDblLValueNode::typeName,
            BdDblLValueNode::typeId,
            BdDblLValueNode::creator,
            BdDblLValueNode::initialize,
        },
        {
            BdDblL3ValueNode::typeName,
            BdDblL3ValueNode::typeId,
            BdDblL3ValueNode::creator,
            BdDblL3ValueNode::initialize,
        },
        {
            BdDblLAddNode::typeName,
            BdDblLAddNode::typeId,
            BdDblLAddNode::creator,
            BdDblLAddNode::initialize,
        },
        {
            BdDblLAddMultiNode::typeName,
            BdDblLAddMultiNode::typeId,
            BdDblLAddMultiNode::creator,
            BdDblLAddMultiNode::initialize,
        },
        {
            BdDblL3AddNode::typeName,
            BdDblL3AddNode::typeId,
            BdDblL3AddNode::creator,
            BdDblL3AddNode::initialize,
        },
        {
            BdDblL3AddMultiNode::typeName,
            BdDblL3AddMultiNode::typeId,
            BdDblL3AddMultiNode::creator,
            BdDblL3AddMultiNode::initialize,
        },
        {
            BdDblLSubtractNode::typeName,
            BdDblLSubtractNode::typeId,
            BdDblLSubtractNode::creator,
            BdDblLSubtractNode::initialize,
        },
        {
            BdDblLSubtractMultiNode::typeName,
            BdDblLSubtractMultiNode::typeId,
            BdDblLSubtractMultiNode::creator,
            BdDblLSubtractMultiNode::initialize,
        },
        {
            BdDblL3SubtractNode::typeName,
            BdDblL3SubtractNode::typeId,
            BdDblL3SubtractNode::creator,
            BdDblL3SubtractNode::initialize,
        },
        {
            BdDblL3SubtractMultiNode::typeName,
            BdDblL3SubtractMultiNode::typeId,
            BdDblL3SubtractMultiNode::creator,
            BdDblL3SubtractMultiNode::initialize,
        },
        {
            BdDblLAverageNode::typeName,
            BdDblLAverageNode::typeId,
            BdDblLAverageNode::creator,
            BdDblLAverageNode::initialize,
        },
        {
            BdDblLAverageMultiNode::typeName,
            BdDblLAverageMultiNode::typeId,
            BdDblLAverageMultiNode::creator,
            BdDblLAverageMultiNode::initialize,
        },
        {
            BdDblL3AverageNode::typeName,
            BdDblL3AverageNode::typeId,
            BdDblL3AverageNode::creator,
            BdDblL3AverageNode::initialize,
        },
        {
            BdDblL3AverageMultiNode::typeName,
            BdDblL3AverageMultiNode::typeId,
            BdDblL3AverageMultiNode::creator,
            BdDblL3AverageMultiNode::initialize,
        },
        {
            BdDblLMinNode::typeName,
            BdDblLMinNode::typeId,
            BdDblLMinNode::creator,
            BdDblLMinNode::initialize,
        },
        {
            BdDblLMinMultiNode::typeName,
            BdDblLMinMultiNode::typeId,
            BdDblLMinMultiNode::creator,
            BdDblLMinMultiNode::initialize,
        },
        {
            BdDblL3MinNode::typeName,
            BdDblL3MinNode::typeId,
            BdDblL3MinNode::creator,
            BdDblL3MinNode::initialize,
        },
        {
            BdDblL3MinMultiNode::typeName,
            BdDblL3MinMultiNode::typeId,
            BdDblL3MinMultiNode::creator,
            BdDblL3MinMultiNode::initialize,
        },
        {
            BdDblLMaxNode::typeName,
            BdDblLMaxNode::typeId,
            BdDblLMaxNode::creator,
            BdDblLMaxNode::initialize,
        },
        {
            BdDblLMaxMultiNode::typeName,
            BdDblLMaxMultiNode::typeId,
            BdDblLMaxMultiNode::creator,
            BdDblLMaxMultiNode::initialize,
        },
        {
            BdDblL3MaxNode::typeName,
            BdDblL3MaxNode::typeId,
            BdDblL3MaxNode::creator,
            BdDblL3MaxNode::initialize,
        },
        {
            BdDblL3MaxMultiNode::typeName,
            BdDblL3MaxMultiNode::typeId,
            BdDblL3MaxMultiNode::creator,
            BdDblL3MaxMultiNode::initialize,
        },
        {
            BdDblLClampNode::typeName,
            BdDblLClampNode::typeId,
            BdDblLClampNode::creator,
            BdDblLClampNode::initialize,
        },
        {
            BdDblL3ClampNode::typeName,
            BdDblL3ClampNode::typeId,
            BdDblL3ClampNode::creator,
            BdDblL3ClampNode::initialize,
        },
        {
            BdDblLAbsNode::typeName,
            BdDblLAbsNode::typeId,
            BdDblLAbsNode::creator,
            BdDblLAbsNode::initialize,
        },
        {
            BdDblL3AbsNode::typeName,
            BdDblL3AbsNode::typeId,
            BdDblL3AbsNode::creator,
            BdDblL3AbsNode::initialize,
        },
        {
            BdDblLNegateNode::typeName,
            BdDblLNegateNode::typeId,
            BdDblLNegateNode::creator,
            BdDblLNegateNode::initialize,
        },
        {
            BdDblL3NegateNode::typeName,
            BdDblL3NegateNode::typeId,
            BdDblL3NegateNode::creator,
            BdDblL3NegateNode::initialize,
        },
        {
            BdDblLLerpNode::typeName,
            BdDblLLerpNode::typeId,
            BdDblLLerpNode::creator,
            BdDblLLerpNode::initialize,
        },
        {
            BdDblL3LerpNode::typeName,
            BdDblL3LerpNode::typeId,
            BdDblL3LerpNode::creator,
            BdDblL3LerpNode::initialize,
        },
        {
            BdDblLMapRangeNode::typeName,
            BdDblLMapRangeNode::typeId,
            BdDblLMapRangeNode::creator,
            BdDblLMapRangeNode::initialize,
        },
        {
            BdDblL3MapRangeNode::typeName,
            BdDblL3MapRangeNode::typeId,
            BdDblL3MapRangeNode::creator,
            BdDblL3MapRangeNode::initialize,
        },
        {
            BdDblLWeightedSumMultiNode::typeName,
            BdDblLWeightedSumMultiNode::typeId,
            BdDblLWeightedSumMultiNode::creator,
            BdDblLWeightedSumMultiNode::initialize,
        },
        {
            BdDblL3WeightedSumMultiNode::typeName,
            BdDblL3WeightedSumMultiNode::typeId,
            BdDblL3WeightedSumMultiNode::creator,
            BdDblL3WeightedSumMultiNode::initialize,
        },
        {
            BdDblLWeightedAverageMultiNode::typeName,
            BdDblLWeightedAverageMultiNode::typeId,
            BdDblLWeightedAverageMultiNode::creator,
            BdDblLWeightedAverageMultiNode::initialize,
        },
        {
            BdDblL3WeightedAverageMultiNode::typeName,
            BdDblL3WeightedAverageMultiNode::typeId,
            BdDblL3WeightedAverageMultiNode::creator,
            BdDblL3WeightedAverageMultiNode::initialize,
        },
        {
            BdAnyConditionDblLNode::typeName,
            BdAnyConditionDblLNode::typeId,
            BdAnyConditionDblLNode::creator,
            BdAnyConditionDblLNode::initialize,
        },
        {
            BdAnyConditionDblLMultiNode::typeName,
            BdAnyConditionDblLMultiNode::typeId,
            BdAnyConditionDblLMultiNode::creator,
            BdAnyConditionDblLMultiNode::initialize,
        },
        {
            BdConditionDblExtraComposeNode::typeName,
            BdConditionDblExtraComposeNode::typeId,
            BdConditionDblExtraComposeNode::creator,
            BdConditionDblExtraComposeNode::initialize,
        },
        {
            BdConditionDblLExtraComposeNode::typeName,
            BdConditionDblLExtraComposeNode::typeId,
            BdConditionDblLExtraComposeNode::creator,
            BdConditionDblLExtraComposeNode::initialize,
        },
        {
            BdConditionDblCaseComposeNode::typeName,
            BdConditionDblCaseComposeNode::typeId,
            BdConditionDblCaseComposeNode::creator,
            BdConditionDblCaseComposeNode::initialize,
        },
        {
            BdConditionDblLCaseComposeNode::typeName,
            BdConditionDblLCaseComposeNode::typeId,
            BdConditionDblLCaseComposeNode::creator,
            BdConditionDblLCaseComposeNode::initialize,
        },
    }};
    return registrations;
}

}  // namespace

MStatus initializePlugin(MObject pluginObject) {
    MStatus status;
    MFnPlugin plugin(
        pluginObject,
        "bakedanuki",
        "0.1.0",
        "20250000",
        &status
    );
    if (!status) {
        status.perror("Failed to initialize bdUtilNodes");
        return status;
    }

    const auto& registrations = nodeRegistrations();
    std::size_t registeredCount = 0;
    for (const NodeRegistration& registration : registrations) {
        status = plugin.registerNode(
            registration.typeName,
            registration.typeId,
            registration.creator,
            registration.initialize,
            MPxNode::kDependNode
        );
        if (status) {
            ++registeredCount;
            continue;
        }

        MString message("Failed to register ");
        message += registration.typeName;
        status.perror(message);

        for (std::size_t index = registeredCount; index > 0; --index) {
            const NodeRegistration& registered = registrations[index - 1];
            const MStatus cleanupStatus = plugin.deregisterNode(
                registered.typeId
            );
            if (!cleanupStatus) {
                MString cleanupMessage("Failed to roll back ");
                cleanupMessage += registered.typeName;
                cleanupMessage += " registration";
                cleanupStatus.perror(cleanupMessage);
            }
        }
        return status;
    }

    return MS::kSuccess;
}

MStatus uninitializePlugin(MObject pluginObject) {
    MStatus status;
    MFnPlugin plugin(pluginObject, "bakedanuki", "0.1.0", "20250000", &status);
    if (!status) {
        status.perror("Failed to initialize bdUtilNodes for unload");
        return status;
    }

    const auto& registrations = nodeRegistrations();
    for (std::size_t index = registrations.size(); index > 0; --index) {
        const NodeRegistration& registration = registrations[index - 1];
        status = plugin.deregisterNode(registration.typeId);
        if (!status) {
            MString message("Failed to deregister ");
            message += registration.typeName;
            status.perror(message);
            return status;
        }
    }

    return MS::kSuccess;
}
