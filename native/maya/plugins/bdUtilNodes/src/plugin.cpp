#include <array>

#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/nodes/BdDbl3AbsNode.h"
#include "bdUtilNodes/nodes/BdDbl3AddNode.h"
#include "bdUtilNodes/nodes/BdDbl3AddMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3AverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3AverageNode.h"
#include "bdUtilNodes/nodes/BdDbl3ClampNode.h"
#include "bdUtilNodes/nodes/BdDbl3ConditionMultiNode.h"
#include "bdUtilNodes/nodes/BdDbl3ConditionNode.h"
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
#include "bdUtilNodes/nodes/BdDblAbsNode.h"
#include "bdUtilNodes/nodes/BdDblAddNode.h"
#include "bdUtilNodes/nodes/BdDblAddMultiNode.h"
#include "bdUtilNodes/nodes/BdDblAverageMultiNode.h"
#include "bdUtilNodes/nodes/BdDblAverageNode.h"
#include "bdUtilNodes/nodes/BdDblClampNode.h"
#include "bdUtilNodes/nodes/BdDblConditionMultiNode.h"
#include "bdUtilNodes/nodes/BdDblConditionNode.h"
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
#include "bdUtilNodes/nodes/BdDbl3WeightedSumMultiNode.h"
#include "bdUtilNodes/nodes/BdDblWeightedSumMultiNode.h"

namespace {

struct NodeRegistration {
    const MString& typeName;
    const MTypeId& typeId;
    MCreatorFunction creator;
    MInitializeFunction initialize;
};

const std::array<NodeRegistration, 50>& nodeRegistrations() {
    static const std::array<NodeRegistration, 50> registrations = {{
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
            BdDbl3ConditionMultiNode::typeName,
            BdDbl3ConditionMultiNode::typeId,
            BdDbl3ConditionMultiNode::creator,
            BdDbl3ConditionMultiNode::initialize,
        },
        {
            BdDbl3ConditionNode::typeName,
            BdDbl3ConditionNode::typeId,
            BdDbl3ConditionNode::creator,
            BdDbl3ConditionNode::initialize,
        },
        {
            BdDblConditionMultiNode::typeName,
            BdDblConditionMultiNode::typeId,
            BdDblConditionMultiNode::creator,
            BdDblConditionMultiNode::initialize,
        },
        {
            BdDblConditionNode::typeName,
            BdDblConditionNode::typeId,
            BdDblConditionNode::creator,
            BdDblConditionNode::initialize,
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
