#pragma once

#include <array>
#include <atomic>
#include <cstdint>
#include <memory>
#include <mutex>

#include <maya/MBoundingBox.h>
#include <maya/MMatrix.h>
#include <maya/MPxLocatorNode.h>

namespace MHWRender {
class MPxGeometryOverride;
}

enum class FocusBoundsWire { Box, Square };

template <FocusBoundsWire Wire>
class BdShpLFocusBoundsNode final : public MPxLocatorNode {
public:
    static constexpr unsigned int VertexCount = Wire == FocusBoundsWire::Square ? 4 : 8;

    struct Geometry {
        MBoundingBox bounds;
        float vertices[VertexCount][3]{};
        bool visible = false;
        std::uint64_t revision = 0;
    };

    BdShpLFocusBoundsNode();
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
    void configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const override;
    bool setInternalValue(const MPlug& plug, const MDataHandle& data) override;
    MStatus legalConnection(
        const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
    ) const override;
    MStatus connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
    MStatus connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;

    Geometry previewGeometry() const;
    bool previewNeedsUpdate(std::uint64_t preparedRevision) const {
        const auto revision = previewRevision_.load(std::memory_order_acquire);
        if (preparedRevision & kPreviewVisible) {
            return revision != (preparedRevision & ~kPreviewVisible);
        }
        return (revision & ~kMatrixConnected) != preparedRevision;
    }

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

private:
    struct Preview {
        MBoundingBox bounds;
        bool visible = false;
        std::uint8_t firstAxis = 0;
        std::uint8_t secondAxis = 1;
        std::uint64_t revision = 0;
    };

    struct TransformedBounds {
        MMatrix matrix;
        MBoundingBox bounds;
        std::uint64_t revision = 0;
    };

    static constexpr bool IsPlanar = Wire == FocusBoundsWire::Square;
    static constexpr unsigned int AxisCount = IsPlanar ? 2 : 3;
    static constexpr std::uint64_t kMatrixUsed = std::uint64_t{1} << 63;
    static constexpr std::uint64_t kMatrixConnected = std::uint64_t{1} << 62;
    static constexpr std::uint64_t kPreviewVisible = std::uint64_t{1} << 61;
    static MObject showShape;
    static MObject shape1stAxis;
    static MObject shape2ndAxis;
    static MObject shapeTransformMatrix;
    static std::array<std::array<MObject, 2>, AxisCount> distances;
    static bool isPreviewAttribute(const MObject& attribute);
    static MPoint corner(
        const Preview& preview, const MPoint& lower, const MPoint& upper, unsigned int index
    );

    void dirtyPreview(bool topologyChanged);
    void matrixConnectionChanged(bool connected);
    Preview preview() const;
    MMatrix readShapeMatrix(MStatus& status) const;

    std::atomic<std::uint64_t> previewRevision_{1};
    mutable std::mutex previewMutex_;
    mutable Preview preview_;
    mutable std::unique_ptr<TransformedBounds> transformedBounds_;
};

using BdShpLFocusBoundingBoxNode = BdShpLFocusBoundsNode<FocusBoundsWire::Box>;
using BdShpLFocusBoundingSquareNode = BdShpLFocusBoundsNode<FocusBoundsWire::Square>;

template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingBoxNode::createGeometryOverride(const MObject& node);
template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingSquareNode::createGeometryOverride(const MObject& node);
