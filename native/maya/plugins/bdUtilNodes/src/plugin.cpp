#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/BdDouble3MultNode.h"

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
        BdDouble3MultNode::typeName,
        BdDouble3MultNode::typeId,
        BdDouble3MultNode::creator,
        BdDouble3MultNode::initialize,
        MPxNode::kDependNode
    );
    if (!status) {
        status.perror("Failed to register bdDouble3Mult");
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
    }
    return status;
}
