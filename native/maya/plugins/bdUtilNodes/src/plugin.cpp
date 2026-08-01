#include <array>

#include <maya/MFnPlugin.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/BdAddDouble3PairNode.h"
#include "bdUtilNodes/BdAddDouble3MultiNode.h"
#include "bdUtilNodes/BdDivDouble3PairNode.h"
#include "bdUtilNodes/BdDivDouble3MultiNode.h"
#include "bdUtilNodes/BdMultDouble3PairNode.h"
#include "bdUtilNodes/BdMultDouble3MultiNode.h"
#include "bdUtilNodes/BdPowDouble3PairNode.h"
#include "bdUtilNodes/BdPowDouble3MultiNode.h"
#include "bdUtilNodes/BdSubDouble3PairNode.h"
#include "bdUtilNodes/BdSubDouble3MultiNode.h"
#include "bdUtilNodes/BdAddDoublePairNode.h"
#include "bdUtilNodes/BdAddDoubleMultiNode.h"
#include "bdUtilNodes/BdDivDoublePairNode.h"
#include "bdUtilNodes/BdDivDoubleMultiNode.h"
#include "bdUtilNodes/BdMultDoublePairNode.h"
#include "bdUtilNodes/BdMultDoubleMultiNode.h"
#include "bdUtilNodes/BdPowDoublePairNode.h"
#include "bdUtilNodes/BdPowDoubleMultiNode.h"
#include "bdUtilNodes/BdSubDoublePairNode.h"
#include "bdUtilNodes/BdSubDoubleMultiNode.h"

namespace {

struct NodeRegistration {
    const MString& typeName;
    const MTypeId& typeId;
    MCreatorFunction creator;
    MInitializeFunction initialize;
};

const std::array<NodeRegistration, 20>& nodeRegistrations() {
    static const std::array<NodeRegistration, 20> registrations = {{
        {
            BdMultDouble3MultiNode::typeName,
            BdMultDouble3MultiNode::typeId,
            BdMultDouble3MultiNode::creator,
            BdMultDouble3MultiNode::initialize,
        },
        {
            BdMultDouble3PairNode::typeName,
            BdMultDouble3PairNode::typeId,
            BdMultDouble3PairNode::creator,
            BdMultDouble3PairNode::initialize,
        },
        {
            BdMultDoubleMultiNode::typeName,
            BdMultDoubleMultiNode::typeId,
            BdMultDoubleMultiNode::creator,
            BdMultDoubleMultiNode::initialize,
        },
        {
            BdMultDoublePairNode::typeName,
            BdMultDoublePairNode::typeId,
            BdMultDoublePairNode::creator,
            BdMultDoublePairNode::initialize,
        },
        {
            BdAddDouble3MultiNode::typeName,
            BdAddDouble3MultiNode::typeId,
            BdAddDouble3MultiNode::creator,
            BdAddDouble3MultiNode::initialize,
        },
        {
            BdAddDouble3PairNode::typeName,
            BdAddDouble3PairNode::typeId,
            BdAddDouble3PairNode::creator,
            BdAddDouble3PairNode::initialize,
        },
        {
            BdAddDoubleMultiNode::typeName,
            BdAddDoubleMultiNode::typeId,
            BdAddDoubleMultiNode::creator,
            BdAddDoubleMultiNode::initialize,
        },
        {
            BdAddDoublePairNode::typeName,
            BdAddDoublePairNode::typeId,
            BdAddDoublePairNode::creator,
            BdAddDoublePairNode::initialize,
        },
        {
            BdSubDouble3MultiNode::typeName,
            BdSubDouble3MultiNode::typeId,
            BdSubDouble3MultiNode::creator,
            BdSubDouble3MultiNode::initialize,
        },
        {
            BdSubDouble3PairNode::typeName,
            BdSubDouble3PairNode::typeId,
            BdSubDouble3PairNode::creator,
            BdSubDouble3PairNode::initialize,
        },
        {
            BdSubDoubleMultiNode::typeName,
            BdSubDoubleMultiNode::typeId,
            BdSubDoubleMultiNode::creator,
            BdSubDoubleMultiNode::initialize,
        },
        {
            BdSubDoublePairNode::typeName,
            BdSubDoublePairNode::typeId,
            BdSubDoublePairNode::creator,
            BdSubDoublePairNode::initialize,
        },
        {
            BdDivDouble3MultiNode::typeName,
            BdDivDouble3MultiNode::typeId,
            BdDivDouble3MultiNode::creator,
            BdDivDouble3MultiNode::initialize,
        },
        {
            BdDivDouble3PairNode::typeName,
            BdDivDouble3PairNode::typeId,
            BdDivDouble3PairNode::creator,
            BdDivDouble3PairNode::initialize,
        },
        {
            BdDivDoubleMultiNode::typeName,
            BdDivDoubleMultiNode::typeId,
            BdDivDoubleMultiNode::creator,
            BdDivDoubleMultiNode::initialize,
        },
        {
            BdDivDoublePairNode::typeName,
            BdDivDoublePairNode::typeId,
            BdDivDoublePairNode::creator,
            BdDivDoublePairNode::initialize,
        },
        {
            BdPowDouble3MultiNode::typeName,
            BdPowDouble3MultiNode::typeId,
            BdPowDouble3MultiNode::creator,
            BdPowDouble3MultiNode::initialize,
        },
        {
            BdPowDouble3PairNode::typeName,
            BdPowDouble3PairNode::typeId,
            BdPowDouble3PairNode::creator,
            BdPowDouble3PairNode::initialize,
        },
        {
            BdPowDoubleMultiNode::typeName,
            BdPowDoubleMultiNode::typeId,
            BdPowDoubleMultiNode::creator,
            BdPowDoubleMultiNode::initialize,
        },
        {
            BdPowDoublePairNode::typeName,
            BdPowDoublePairNode::typeId,
            BdPowDoublePairNode::creator,
            BdPowDoublePairNode::initialize,
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
