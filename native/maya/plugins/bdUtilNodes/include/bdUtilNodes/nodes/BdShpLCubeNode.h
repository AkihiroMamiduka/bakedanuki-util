#pragma once

#include <maya/MBoundingBox.h>
#include <maya/MObject.h>
#include <maya/MPxLocatorNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

namespace MHWRender {
class MPxGeometryOverride;
}

class BdShpLCubeNode final : public MPxLocatorNode {
public:
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxGeometryOverride* createGeometryOverride(const MObject& node);
    static void cleanupDrawResources();

    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    bool excludeAsLocator() const override;

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;
};
