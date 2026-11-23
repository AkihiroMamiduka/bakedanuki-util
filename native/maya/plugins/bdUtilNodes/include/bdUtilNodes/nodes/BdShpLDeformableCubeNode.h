#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#include <atomic>
#include <cstdint>
#include <mutex>

#include <maya/MMatrix.h>
#include <maya/MObject.h>
#include <maya/MPxLocatorNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

namespace MHWRender {
class MPxSubSceneOverride;
}

namespace bdUtilNodes::fixedCube {
struct ShapeAttributes;
}

class BdShpLDeformableCubeNode final : public MPxLocatorNode {
public:
    using Geometry = bdUtilNodes::fixedCube::Geometry;

    struct DrawMatrixCache {
        MMatrix matrix;
        std::uint64_t revision = 0;
    };

    BdShpLDeformableCubeNode();
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxSubSceneOverride* createSubSceneOverride(const MObject& node);
    static void startDisplayStateMonitoring();
    static void cleanupDrawResources();

    void postConstructor() override;
    void copyInternalData(MPxNode* source) override;
    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    bool excludeAsLocator() const override;

    MStatus setDependentsDirty(const MPlug& plug, MPlugArray& affected) override;
    MStatus postEvaluation(
        const MDGContext& context, const MEvaluationNode& evaluationNode, PostEvaluationType evalType
    ) override;
    bool setInternalValue(const MPlug& plug, const MDataHandle& data) override;
    MStatus legalConnection(
        const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
    ) const override;
    MStatus connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
    MStatus connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;

    void getCacheSetup(
        const MEvaluationNode& evalNode,
        MNodeCacheDisablingInfo& disablingInfo,
        MNodeCacheSetupInfo& cacheSetupInfo,
        MObjectArray& monitoredAttributes
    ) const override;
    void configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const override;

    Geometry baseDrawGeometry() const;
    std::uint64_t geometryRevision() const;
    std::uint64_t shapeMatrixRevision() const {
        return matrixRevision_.load(std::memory_order_acquire);
    }
    MMatrix shapeDrawMatrix(
        DrawMatrixCache* drawCache = nullptr, std::uint64_t* connectedReadRevision = nullptr
    ) const;

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

private:
    static bdUtilNodes::fixedCube::ShapeAttributes shapeAttributes_;
    static MObject shapeDeformMatrix;

    void dirtyMatrix();
    bool readShapeMatrix(MMatrix& deformMatrix) const;

    std::atomic<std::uint64_t> geometryRevision_{1};
    std::atomic<std::uint64_t> matrixRevision_{1};
    std::atomic<bool> matrixConnected_{false};
    mutable std::mutex dataMutex_;
    mutable Geometry baseGeometry_;
    mutable MMatrix cachedMatrix_;
    mutable std::uint64_t cachedMatrixRevision_ = 0;
};
