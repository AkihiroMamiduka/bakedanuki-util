#include <array>

#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/BdDbl3AddNode.h"
#include "bdUtilNodes/BdDbl3AddMultiNode.h"
#include "bdUtilNodes/BdDbl3DivNode.h"
#include "bdUtilNodes/BdDbl3DivMultiNode.h"
#include "bdUtilNodes/BdDbl3LerpNode.h"
#include "bdUtilNodes/BdDblLerpNode.h"
#include "bdUtilNodes/BdDbl3MultNode.h"
#include "bdUtilNodes/BdDbl3MultMultiNode.h"
#include "bdUtilNodes/BdDbl3PowNode.h"
#include "bdUtilNodes/BdDbl3PowMultiNode.h"
#include "bdUtilNodes/BdDbl3SubNode.h"
#include "bdUtilNodes/BdDbl3SubMultiNode.h"
#include "bdUtilNodes/BdDblAddNode.h"
#include "bdUtilNodes/BdDblAddMultiNode.h"
#include "bdUtilNodes/BdDblDivNode.h"
#include "bdUtilNodes/BdDblDivMultiNode.h"
#include "bdUtilNodes/BdDbl3ValueNode.h"
#include "bdUtilNodes/BdDblValueNode.h"
#include "bdUtilNodes/BdDblMultNode.h"
#include "bdUtilNodes/BdDblMultMultiNode.h"
#include "bdUtilNodes/BdDblPowNode.h"
#include "bdUtilNodes/BdDblPowMultiNode.h"
#include "bdUtilNodes/BdDblSubNode.h"
#include "bdUtilNodes/BdDblSubMultiNode.h"
#include "bdUtilNodes/BdDbl3WtAddMultiNode.h"
#include "bdUtilNodes/BdDblWtAddMultiNode.h"

namespace {

struct NodeRegistration {
    const MString& typeName;
    const MTypeId& typeId;
    MCreatorFunction creator;
    MInitializeFunction initialize;
};

const std::array<NodeRegistration, 26>& nodeRegistrations() {
    static const std::array<NodeRegistration, 26> registrations = {{
        {
            BdDbl3MultMultiNode::typeName,
            BdDbl3MultMultiNode::typeId,
            BdDbl3MultMultiNode::creator,
            BdDbl3MultMultiNode::initialize,
        },
        {
            BdDbl3MultNode::typeName,
            BdDbl3MultNode::typeId,
            BdDbl3MultNode::creator,
            BdDbl3MultNode::initialize,
        },
        {
            BdDblMultMultiNode::typeName,
            BdDblMultMultiNode::typeId,
            BdDblMultMultiNode::creator,
            BdDblMultMultiNode::initialize,
        },
        {
            BdDblMultNode::typeName,
            BdDblMultNode::typeId,
            BdDblMultNode::creator,
            BdDblMultNode::initialize,
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
            BdDbl3SubMultiNode::typeName,
            BdDbl3SubMultiNode::typeId,
            BdDbl3SubMultiNode::creator,
            BdDbl3SubMultiNode::initialize,
        },
        {
            BdDbl3SubNode::typeName,
            BdDbl3SubNode::typeId,
            BdDbl3SubNode::creator,
            BdDbl3SubNode::initialize,
        },
        {
            BdDblSubMultiNode::typeName,
            BdDblSubMultiNode::typeId,
            BdDblSubMultiNode::creator,
            BdDblSubMultiNode::initialize,
        },
        {
            BdDblSubNode::typeName,
            BdDblSubNode::typeId,
            BdDblSubNode::creator,
            BdDblSubNode::initialize,
        },
        {
            BdDbl3DivMultiNode::typeName,
            BdDbl3DivMultiNode::typeId,
            BdDbl3DivMultiNode::creator,
            BdDbl3DivMultiNode::initialize,
        },
        {
            BdDbl3DivNode::typeName,
            BdDbl3DivNode::typeId,
            BdDbl3DivNode::creator,
            BdDbl3DivNode::initialize,
        },
        {
            BdDblDivMultiNode::typeName,
            BdDblDivMultiNode::typeId,
            BdDblDivMultiNode::creator,
            BdDblDivMultiNode::initialize,
        },
        {
            BdDblDivNode::typeName,
            BdDblDivNode::typeId,
            BdDblDivNode::creator,
            BdDblDivNode::initialize,
        },
        {
            BdDbl3PowMultiNode::typeName,
            BdDbl3PowMultiNode::typeId,
            BdDbl3PowMultiNode::creator,
            BdDbl3PowMultiNode::initialize,
        },
        {
            BdDbl3PowNode::typeName,
            BdDbl3PowNode::typeId,
            BdDbl3PowNode::creator,
            BdDbl3PowNode::initialize,
        },
        {
            BdDblPowMultiNode::typeName,
            BdDblPowMultiNode::typeId,
            BdDblPowMultiNode::creator,
            BdDblPowMultiNode::initialize,
        },
        {
            BdDblPowNode::typeName,
            BdDblPowNode::typeId,
            BdDblPowNode::creator,
            BdDblPowNode::initialize,
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
            BdDbl3WtAddMultiNode::typeName,
            BdDbl3WtAddMultiNode::typeId,
            BdDbl3WtAddMultiNode::creator,
            BdDbl3WtAddMultiNode::initialize,
        },
        {
            BdDblWtAddMultiNode::typeName,
            BdDblWtAddMultiNode::typeId,
            BdDblWtAddMultiNode::creator,
            BdDblWtAddMultiNode::initialize,
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
