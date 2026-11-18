#pragma once

#include <atomic>
#include <cstdint>
#include <mutex>

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
    struct Geometry {
        float vertices[8][3];
        MBoundingBox bounds;
        std::uint64_t revision = 0;
    };

    BdShpLCubeNode();
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxGeometryOverride* createGeometryOverride(const MObject& node);
    static void cleanupDrawResources();

    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    void getCacheSetup(
        const MEvaluationNode& evalNode,
        MNodeCacheDisablingInfo& disablingInfo,
        MNodeCacheSetupInfo& cacheSetupInfo,
        MObjectArray& monitoredAttributes
    ) const override;
    bool excludeAsLocator() const override;
    bool setInternalValue(const MPlug& plug, const MDataHandle& data) override;
    MStatus legalConnection(
        const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
    ) const override;
    Geometry geometry() const;
    std::uint64_t geometryRevision() const;
#ifdef BD_CUBE_NODE_PARALLEL
    SchedulingType schedulingType() const override;
#endif

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

    static MObject shape1stAxis;
    static MObject shape2ndAxis;
    static MObject shapeBaseSpace1stAxisPlus;
    static MObject shapeBaseSpace1stAxisMinus;
    static MObject shapeBaseSpace2ndAxisPlus;
    static MObject shapeBaseSpace2ndAxisMinus;
    static MObject shapeBaseSpace3rdAxisPlus;
    static MObject shapeBaseSpace3rdAxisMinus;

private:
    static bool isShapeAttribute(const MObject& attribute);
    std::atomic<std::uint64_t> geometryRevision_{1};
    mutable std::mutex geometryMutex_;
    mutable Geometry geometry_;
};
