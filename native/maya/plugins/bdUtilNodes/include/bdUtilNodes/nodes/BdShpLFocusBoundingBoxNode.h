#pragma once

#include <atomic>
#include <cstdint>
#include <mutex>

#include <maya/MBoundingBox.h>
#include <maya/MPxLocatorNode.h>

namespace MHWRender {
class MPxGeometryOverride;
}

class BdShpLFocusBoundingBoxNode final : public MPxLocatorNode {
public:
    struct Preview {
        MBoundingBox bounds;
        bool visible = false;
        std::uint64_t revision = 0;
    };

    BdShpLFocusBoundingBoxNode();
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxGeometryOverride* createGeometryOverride(const MObject& node);

    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    bool excludeAsLocator() const override;
    void getCacheSetup(
        const MEvaluationNode& evalNode,
        MNodeCacheDisablingInfo& disablingInfo,
        MNodeCacheSetupInfo& cacheSetupInfo,
        MObjectArray& monitoredAttributes
    ) const override;
    bool setInternalValue(const MPlug& plug, const MDataHandle& data) override;
    MStatus legalConnection(
        const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
    ) const override;

    Preview preview() const;
    std::uint64_t previewRevision() const;

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

private:
    static MObject showShape;
    static MObject shapeBaseSpaceXPlus;
    static MObject shapeBaseSpaceXMinus;
    static MObject shapeBaseSpaceYPlus;
    static MObject shapeBaseSpaceYMinus;
    static MObject shapeBaseSpaceZPlus;
    static MObject shapeBaseSpaceZMinus;
    static bool isPreviewAttribute(const MObject& attribute);

    std::atomic<std::uint64_t> previewRevision_{1};
    mutable std::mutex previewMutex_;
    mutable Preview preview_;
};
