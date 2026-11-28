#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#include <atomic>
#include <cstdint>
#include <mutex>
#include <optional>

#include <maya/MAnimControl.h>
#include <maya/MDGContext.h>
#include <maya/MMatrix.h>
#include <maya/MObject.h>
#include <maya/MPxLocatorNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTime.h>
#include <maya/MTypeId.h>

namespace MHWRender {
class MPxSubSceneOverride;
}

namespace bdUtilNodes::fixedCube {
struct ShapeAttributes;
}

class BdShpLDeformableCubeNode : public MPxLocatorNode {
public:
    using Geometry = bdUtilNodes::fixedCube::Geometry;

    struct DrawMatrixCache {
        MMatrix matrix;
        std::uint64_t revision = 0;
        std::optional<MTime> publicationTime;

        bool validAtCurrentTime() const {
            return !publicationTime ||
                (MDGContext::current().isNormal() && MAnimControl::currentTime() == *publicationTime);
        }
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
    bool tryPublishedShapeMatrix(std::uint64_t revision, MMatrix& local, MTime& time) const;
    MMatrix shapeDrawMatrix(
        DrawMatrixCache* drawCache = nullptr, std::uint64_t* connectedReadRevision = nullptr,
        std::optional<MTime>* publicationTime = nullptr
    ) const;

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

protected:
    BdShpLDeformableCubeNode(
        const bdUtilNodes::fixedCube::ShapeAttributes& attributes, const MObject& matrixAttribute);
    static MStatus initializeMatrixAttribute(MObject& matrixAttribute);

private:
    class EvaluationMatrixCache {
    public:
        using Revision = std::atomic<std::uint64_t>;

        struct Value {
            MMatrix matrix;
            MTime time;
        };

        class ReadScope {
        public:
            ReadScope(EvaluationMatrixCache& cache, bool track, bool exclusive = false);
            ~ReadScope();
            ReadScope(const ReadScope&) = delete;
            ReadScope& operator=(const ReadScope&) = delete;

            bool active() const { return active_; }

        private:
            EvaluationMatrixCache& cache_;
            bool active_;
        };

        bool readActive() const;
        bool hasPending(std::uint64_t revision) const;
        void stage(MDataHandle data, std::uint64_t revision, const Revision& current);
        void discard(std::uint64_t revision);
        bool publishPending(std::uint64_t previous, const Revision& current);
        void publishDirect(const MMatrix& deformMatrix, const MTime& time, std::uint64_t revision, const Revision& current);
        std::optional<Value> lookup(std::uint64_t revision, const Revision& current) const;

    private:
        std::atomic<unsigned> activeReads_{0};
        Revision pendingRevision_{0};
        Revision publishedRevision_{0};
        mutable std::mutex mutex_;
        Value pending_;
        Value published_;
    };

    static bdUtilNodes::fixedCube::ShapeAttributes shapeAttributes_;
    static MObject shapeDeformMatrix;

    void dirtyMatrix();
    bool readShapeMatrix(MMatrix& deformMatrix) const;

    std::atomic<std::uint64_t> geometryRevision_{1};
    std::atomic<std::uint64_t> matrixRevision_{1};
    std::atomic<bool> matrixConnected_{false};
    mutable std::mutex dataMutex_;
    mutable EvaluationMatrixCache evaluationMatrixCache_;
    mutable Geometry baseGeometry_;
    mutable MMatrix cachedMatrix_;
    mutable std::uint64_t cachedMatrixRevision_ = 0;
    const bdUtilNodes::fixedCube::ShapeAttributes& attributes_;
    const MObject& matrixAttribute_;
};

#ifndef BD_CUBE_RESEARCH_LEGACY_NAMES
class BdCtrlShpLDeformableSimpleCubeNode final : public BdShpLDeformableCubeNode {
public:
    BdCtrlShpLDeformableSimpleCubeNode();
    static void* creator();
    static MStatus initialize();

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

private:
    static bdUtilNodes::fixedCube::ShapeAttributes shapeAttributes_;
    static MObject shapeDeformMatrix;
};
#endif
