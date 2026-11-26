#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"

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

namespace bdUtilNodes::fixedCube {
struct ShapeAttributes;
}

class BdShpLCubeNode final : public MPxLocatorNode {
public:
    using Geometry = bdUtilNodes::fixedCube::Geometry;

    BdShpLCubeNode();
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxGeometryOverride* createGeometryOverride(const MObject& node);
    static void cleanupDrawResources();

    void postConstructor() override;
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    void copyInternalData(MPxNode* source) override;
#endif
    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    void getCacheSetup(
        const MEvaluationNode& evalNode,
        MNodeCacheDisablingInfo& disablingInfo,
        MNodeCacheSetupInfo& cacheSetupInfo,
        MObjectArray& monitoredAttributes
    ) const override;
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    void configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const override;
#endif
    bool excludeAsLocator() const override;
    bool setInternalValue(const MPlug& plug, const MDataHandle& data) override;
    MStatus legalConnection(
        const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
    ) const override;
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    MStatus connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
    MStatus connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
#endif
    Geometry geometry() const;
    std::uint64_t geometryRevision() const;
#if defined(BD_CUBE_RESEARCH_SHAPE_MATRIX) && (defined(BD_CUBE_DRAW_OVERRIDE) || defined(BD_CUBE_SUBSCENE_MATRIX))
    Geometry baseDrawGeometry() const;
    MMatrix shapeDrawMatrix() const;
#endif
#ifdef BD_CUBE_NODE_PARALLEL
    SchedulingType schedulingType() const override;
#endif

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    static MObject shapeTransformMatrix;
#endif

private:
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    static constexpr std::uint64_t kAnimationUsed = std::uint64_t{1} << 62;
    static constexpr std::uint64_t kAnimationConnected = std::uint64_t{1} << 63;

    struct AnimationGeometry {
        MPoint basePositions[bdUtilNodes::fixedCube::vertexCount];
        MMatrix matrix;
        Geometry transformed;
        bool useTransformed = false;
    };
#endif

    static bdUtilNodes::fixedCube::ShapeAttributes shapeAttributes_;
    void dirtyGeometry();
    bool updateBaseGeometry(std::uint64_t revision) const;
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    void setAnimationConnection(bool connected);
    Geometry geometryWithAnimationMatrix(std::uint64_t revision) const;
#endif

    std::atomic<std::uint64_t> geometryRevision_{1};
    mutable std::mutex geometryMutex_;
    mutable Geometry geometry_;
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    mutable std::unique_ptr<AnimationGeometry> animation_;
#endif
};
