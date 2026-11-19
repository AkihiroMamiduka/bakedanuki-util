#pragma once

#include <maya/MPlug.h>
#include <maya/MPxLocatorNode.h>

namespace bdUtilNodes {

inline void hideLocatorPositionAndScale(const MObject& node) {
    const MObject attributes[] = {
        MPxLocatorNode::localPositionX,
        MPxLocatorNode::localPositionY,
        MPxLocatorNode::localPositionZ,
        MPxLocatorNode::localScaleX,
        MPxLocatorNode::localScaleY,
        MPxLocatorNode::localScaleZ,
    };
    for (const auto& attribute : attributes) {
        const MStatus status = MPlug(node, attribute).setChannelBox(false);
        if (!status) status.perror("Failed to hide locator position or scale in the Channel Box");
    }
}

}
