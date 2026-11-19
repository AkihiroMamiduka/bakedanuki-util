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

enum class FocusBoundsWire { Box, CrossLine3Axis, Square, CrossLine };

constexpr bool isPlanarFocusWire(FocusBoundsWire wire) {
    return wire == FocusBoundsWire::Square || wire == FocusBoundsWire::CrossLine;
}

template <FocusBoundsWire Wire>
class BdShpLFocusBoundsNode final : public MPxLocatorNode {
public:
    struct Preview {
        MBoundingBox bounds;
        bool visible = false;
        std::uint8_t firstAxis = 0;
        std::uint8_t secondAxis = 1;
        std::uint64_t revision = 0;
    };

    BdShpLFocusBoundsNode();
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxGeometryOverride* createGeometryOverride(const MObject& node);

    void postConstructor() override;
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
    static constexpr bool IsPlanar = isPlanarFocusWire(Wire);
    static constexpr unsigned int AxisCount = IsPlanar ? 2 : 3;
    static MObject showShape;
    static MObject shape1stAxis;
    static MObject shape2ndAxis;
    static std::array<std::array<MObject, 2>, AxisCount> distances;
    static bool isPreviewAttribute(const MObject& attribute);

    std::atomic<std::uint64_t> previewRevision_{1};
    mutable std::mutex previewMutex_;
    mutable Preview preview_;
};

using BdShpLFocusBoundingBoxNode = BdShpLFocusBoundsNode<FocusBoundsWire::Box>;
using BdShpLFocusBoundingCrossLine3AxisNode = BdShpLFocusBoundsNode<FocusBoundsWire::CrossLine3Axis>;
using BdShpLFocusBoundingSquareNode = BdShpLFocusBoundsNode<FocusBoundsWire::Square>;
using BdShpLFocusBoundingCrossLineNode = BdShpLFocusBoundsNode<FocusBoundsWire::CrossLine>;

template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingBoxNode::createGeometryOverride(const MObject& node);
template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingCrossLine3AxisNode::createGeometryOverride(const MObject& node);
template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingSquareNode::createGeometryOverride(const MObject& node);
template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingCrossLineNode::createGeometryOverride(const MObject& node);
