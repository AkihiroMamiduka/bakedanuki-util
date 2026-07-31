#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/BdDouble3MultNode.h"
#include "bdUtilNodes/BdDouble3MultMultiNode.h"

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

    status = plugin.registerNode(
        BdDouble3MultMultiNode::typeName,
        BdDouble3MultMultiNode::typeId,
        BdDouble3MultMultiNode::creator,
        BdDouble3MultMultiNode::initialize,
        MPxNode::kDependNode
    );
    if (!status) {
        status.perror("Failed to register bdDouble3MultMulti");
        return status;
    }

    status = plugin.registerNode(
        BdDouble3MultNode::typeName,
        BdDouble3MultNode::typeId,
        BdDouble3MultNode::creator,
        BdDouble3MultNode::initialize,
        MPxNode::kDependNode
    );
    if (!status) {
        status.perror("Failed to register bdDouble3Mult");
        const MStatus cleanupStatus = plugin.deregisterNode(
            BdDouble3MultMultiNode::typeId
        );
        if (!cleanupStatus) {
            cleanupStatus.perror(
                "Failed to roll back bdDouble3MultMulti registration"
            );
        }
    }
    return status;
}

MStatus uninitializePlugin(MObject pluginObject) {
    MStatus status;
    MFnPlugin plugin(pluginObject, "bakedanuki", "0.1.0", "20250000", &status);
    if (!status) {
        status.perror("Failed to initialize bdUtilNodes for unload");
        return status;
    }

    status = plugin.deregisterNode(BdDouble3MultNode::typeId);
    if (!status) {
        status.perror("Failed to deregister bdDouble3Mult");
        return status;
    }

    status = plugin.deregisterNode(BdDouble3MultMultiNode::typeId);
    if (!status) {
        status.perror("Failed to deregister bdDouble3MultMulti");
    }
    return status;
}
