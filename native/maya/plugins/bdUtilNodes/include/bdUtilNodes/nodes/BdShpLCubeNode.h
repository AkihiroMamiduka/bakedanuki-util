#pragma once

#include <atomic>
#include <cstdint>
#include <memory>
#include <mutex>

#include <maya/MBoundingBox.h>
#include <maya/MMatrix.h>
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

    void postConstructor() override;
    void copyInternalData(MPxNode* source) override;
    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    void getCacheSetup(
        const MEvaluationNode& evalNode,
        MNodeCacheDisablingInfo& disablingInfo,
        MNodeCacheSetupInfo& cacheSetupInfo,
        MObjectArray& monitoredAttributes
    ) const override;
    void configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const override;
    bool excludeAsLocator() const override;
    bool setInternalValue(const MPlug& plug, const MDataHandle& data) override;
    MStatus legalConnection(
        const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
    ) const override;
    MStatus connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
    MStatus connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
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
    static MObject shapeTransformMatrix;

private:
    static constexpr std::uint64_t kAnimationUsed = std::uint64_t{1} << 62;
    static constexpr std::uint64_t kAnimationConnected = std::uint64_t{1} << 63;

    struct AnimationGeometry {
        MPoint basePositions[8];
        MMatrix matrix;
        Geometry transformed;
        bool useTransformed = false;
    };

    static bool isShapeAttribute(const MObject& attribute);
    void dirtyGeometry();
    void setAnimationConnection(bool connected);
    bool updateBaseGeometry(std::uint64_t revision) const;
    Geometry geometryWithAnimationMatrix(std::uint64_t revision) const;

    std::atomic<std::uint64_t> geometryRevision_{1};
    mutable std::mutex geometryMutex_;
    mutable Geometry geometry_;
    mutable std::unique_ptr<AnimationGeometry> animation_;
};
