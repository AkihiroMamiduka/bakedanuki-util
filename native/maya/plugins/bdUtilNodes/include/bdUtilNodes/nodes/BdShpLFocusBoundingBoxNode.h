#pragma once

#include <array>
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
    static constexpr unsigned int VertexCount = 8;

    struct Geometry {
        MBoundingBox bounds;
        float vertices[VertexCount][3]{};
        bool visible = false;
        std::uint64_t revision = 0;
    };

    BdShpLFocusBoundingBoxNode();
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxGeometryOverride* createGeometryOverride(const MObject& node);

    void postConstructor() override;
    void copyInternalData(MPxNode* source) override;
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
    Geometry previewGeometry() const;
    bool previewNeedsUpdate(std::uint64_t preparedRevision) const {
        return previewRevision_.load(std::memory_order_acquire) != preparedRevision;
    }

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

private:
    struct Preview {
        MBoundingBox bounds;
        bool visible = false;
        std::uint64_t revision = 0;
    };

    static constexpr unsigned int AxisCount = 3;
    static MObject showShape;
    static std::array<std::array<MObject, 2>, AxisCount> distances;
    static bool isPreviewAttribute(const MObject& attribute);

    void dirtyPreview(bool topologyChanged);
    Preview preview() const;

    std::atomic<std::uint64_t> previewRevision_{1};
    mutable std::mutex previewMutex_;
    mutable Preview preview_;
};
