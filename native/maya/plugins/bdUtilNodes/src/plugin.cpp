#include <array>

#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/BdDouble3AddNode.h"
#include "bdUtilNodes/BdDouble3AddMultiNode.h"
#include "bdUtilNodes/BdDouble3MultNode.h"
#include "bdUtilNodes/BdDouble3MultMultiNode.h"
#include "bdUtilNodes/BdDoubleAddNode.h"
#include "bdUtilNodes/BdDoubleAddMultiNode.h"
#include "bdUtilNodes/BdDoubleMultNode.h"
#include "bdUtilNodes/BdDoubleMultMultiNode.h"

namespace {

struct NodeRegistration {
    const MString& typeName;
    const MTypeId& typeId;
    MCreatorFunction creator;
    MInitializeFunction initialize;
};

const std::array<NodeRegistration, 8>& nodeRegistrations() {
    static const std::array<NodeRegistration, 8> registrations = {{
        {
            BdDouble3MultMultiNode::typeName,
            BdDouble3MultMultiNode::typeId,
            BdDouble3MultMultiNode::creator,
            BdDouble3MultMultiNode::initialize,
        },
        {
            BdDouble3MultNode::typeName,
            BdDouble3MultNode::typeId,
            BdDouble3MultNode::creator,
            BdDouble3MultNode::initialize,
        },
        {
            BdDoubleMultMultiNode::typeName,
            BdDoubleMultMultiNode::typeId,
            BdDoubleMultMultiNode::creator,
            BdDoubleMultMultiNode::initialize,
        },
        {
            BdDoubleMultNode::typeName,
            BdDoubleMultNode::typeId,
            BdDoubleMultNode::creator,
            BdDoubleMultNode::initialize,
        },
        {
            BdDouble3AddMultiNode::typeName,
            BdDouble3AddMultiNode::typeId,
            BdDouble3AddMultiNode::creator,
            BdDouble3AddMultiNode::initialize,
        },
        {
            BdDouble3AddNode::typeName,
            BdDouble3AddNode::typeId,
            BdDouble3AddNode::creator,
            BdDouble3AddNode::initialize,
        },
        {
            BdDoubleAddMultiNode::typeName,
            BdDoubleAddMultiNode::typeId,
            BdDoubleAddMultiNode::creator,
            BdDoubleAddMultiNode::initialize,
        },
        {
            BdDoubleAddNode::typeName,
            BdDoubleAddNode::typeId,
            BdDoubleAddNode::creator,
            BdDoubleAddNode::initialize,
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
