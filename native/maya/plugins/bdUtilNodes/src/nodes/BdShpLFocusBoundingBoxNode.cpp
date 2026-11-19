#include "bdUtilNodes/nodes/BdShpLFocusBoundingBoxNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"
#include "bdUtilNodes/nodes/SignedShapeAxes.h"

#include <algorithm>

#include <maya/MDistance.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MNodeCacheSetupInfo.h>
#include <maya/MObjectArray.h>
#include <maya/MPlug.h>
#include <maya/MViewport2Renderer.h>

template <> const MString BdShpLFocusBoundingBoxNode::typeName("bdShpL_FocusBoundingBox");
template <> const MTypeId BdShpLFocusBoundingBoxNode::typeId(0x00142721);
template <> const MString BdShpLFocusBoundingBoxNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingBox");
template <> const MString BdShpLFocusBoundingBoxNode::drawRegistrantId("bdShpLFocusBoundingBoxGeometryOverride");

template <> const MString BdShpLFocusBoundingCrossLine3AxisNode::typeName("bdShpL_FocusBoundingCrossLine3Axis");
template <> const MTypeId BdShpLFocusBoundingCrossLine3AxisNode::typeId(0x00142722);
template <> const MString BdShpLFocusBoundingCrossLine3AxisNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingCrossLine3Axis");
template <> const MString BdShpLFocusBoundingCrossLine3AxisNode::drawRegistrantId("bdShpLFocusBoundingCrossLine3AxisGeometryOverride");

template <> const MString BdShpLFocusBoundingSquareNode::typeName("bdShpL_FocusBoundingSquare");
template <> const MTypeId BdShpLFocusBoundingSquareNode::typeId(0x00142723);
template <> const MString BdShpLFocusBoundingSquareNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingSquare");
template <> const MString BdShpLFocusBoundingSquareNode::drawRegistrantId("bdShpLFocusBoundingSquareGeometryOverride");

template <> const MString BdShpLFocusBoundingCrossLineNode::typeName("bdShpL_FocusBoundingCrossLine");
template <> const MTypeId BdShpLFocusBoundingCrossLineNode::typeId(0x00142724);
template <> const MString BdShpLFocusBoundingCrossLineNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingCrossLine");
template <> const MString BdShpLFocusBoundingCrossLineNode::drawRegistrantId("bdShpLFocusBoundingCrossLineGeometryOverride");

template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::showShape;
template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::shape1stAxis;
template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::shape2ndAxis;
template <FocusBoundsWire Wire>
std::array<std::array<MObject, 2>, BdShpLFocusBoundsNode<Wire>::AxisCount>
    BdShpLFocusBoundsNode<Wire>::distances;

template <FocusBoundsWire Wire>
BdShpLFocusBoundsNode<Wire>::BdShpLFocusBoundsNode() {
    if constexpr (IsPlanar) {
        preview_.bounds = MBoundingBox(MPoint(-0.5, -0.5, 0), MPoint(0.5, 0.5, 0));
    } else {
        preview_.bounds = bdUtilNodes::fixedCube::bounds();
    }
}

template <FocusBoundsWire Wire>
void* BdShpLFocusBoundsNode<Wire>::creator() {
    return new BdShpLFocusBoundsNode;
}

template <FocusBoundsWire Wire>
void BdShpLFocusBoundsNode<Wire>::postConstructor() {
    MPxLocatorNode::postConstructor();
    const auto node = thisMObject();
    bdUtilNodes::hideLocatorPositionAndScale(node);

    MStatus status;
    auto overrideEnabled = MFnDependencyNode(node).findPlug("overrideEnabled", false, &status);
    if (status) status = overrideEnabled.setBool(false);
    if (status) status = overrideEnabled.setLocked(true);
    if (!status) status.perror("Failed to set the focus bounding shape drawing override default");
}

template <FocusBoundsWire Wire>
MStatus BdShpLFocusBoundsNode<Wire>::initialize() {
    MStatus status;
    MFnNumericAttribute numericFn;
    showShape = numericFn.create("showShape", "ss", MFnNumericData::kBoolean, false, &status);
    if (!status) return status;

    const auto registerPreviewAttribute = [&status](const MObject& attribute, bool affectsBounds) {
        MFnAttribute fn(attribute, &status);
        if (!status) return status;
        status = fn.setKeyable(false);
        if (!status) return status;
        status = fn.setConnectable(false);
        if (!status) return status;
        status = fn.setChannelBox(true);
        if (!status) return status;
        status = fn.setInternal(true);
        if (!status) return status;
        status = fn.setAffectsAppearance(true);
        if (!status) return status;
        status = fn.setAffectsWorldSpace(affectsBounds);
        if (!status) return status;
        return addAttribute(attribute);
    };
    status = registerPreviewAttribute(showShape, false);
    if (!status) return status;

    if constexpr (IsPlanar) {
        shape1stAxis = bdUtilNodes::createSignedAxisAttribute("shape1stAxis", "s1a", 0, status);
        if (!status) return status;
        status = registerPreviewAttribute(shape1stAxis, true);
        if (!status) return status;
        shape2ndAxis = bdUtilNodes::createSignedAxisAttribute("shape2ndAxis", "s2a", 2, status);
        if (!status) return status;
        status = registerPreviewAttribute(shape2ndAxis, true);
        if (!status) return status;
    }

    struct AttributeNames { const char* name; const char* shortName; };
    constexpr AttributeNames xyzNames[3][2] = {
        {{"shapeBaseSpaceXPlus", "sbsxp"}, {"shapeBaseSpaceXMinus", "sbsxm"}},
        {{"shapeBaseSpaceYPlus", "sbsyp"}, {"shapeBaseSpaceYMinus", "sbsym"}},
        {{"shapeBaseSpaceZPlus", "sbszp"}, {"shapeBaseSpaceZMinus", "sbszm"}},
    };
    constexpr AttributeNames planarNames[2][2] = {
        {{"shapeBaseSpace1stAxisPlus", "sbsp1p"}, {"shapeBaseSpace1stAxisMinus", "sbsp1m"}},
        {{"shapeBaseSpace2ndAxisPlus", "sbsp2p"}, {"shapeBaseSpace2ndAxisMinus", "sbsp2m"}},
    };
    const auto* names = IsPlanar ? planarNames : xyzNames;
    MFnUnitAttribute unitFn;
    for (unsigned int axis = 0; axis < AxisCount; ++axis) {
        for (unsigned int side = 0; side < 2; ++side) {
            const auto& name = names[axis][side];
            auto& attribute = distances[axis][side];
            attribute = unitFn.create(name.name, name.shortName, MDistance(0.5, MDistance::kCentimeters), &status);
            if (!status) return status;
            status = registerPreviewAttribute(attribute, true);
            if (!status) return status;
        }
    }
    return MS::kSuccess;
}

template <FocusBoundsWire Wire>
bool BdShpLFocusBoundsNode<Wire>::isPreviewAttribute(const MObject& attribute) {
    if (attribute == showShape) return true;
    if constexpr (IsPlanar) {
        if (attribute == shape1stAxis || attribute == shape2ndAxis) return true;
    }
    for (const auto& sides : distances) {
        if (attribute == sides[0] || attribute == sides[1]) return true;
    }
    return false;
}

template <FocusBoundsWire Wire>
bool BdShpLFocusBoundsNode<Wire>::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    const auto attribute = plug.attribute();
    if (isPreviewAttribute(attribute)) {
        previewRevision_.fetch_add(1, std::memory_order_release);
        MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), attribute == showShape);
        // Maya に値の保存を委ね、編集後の再描画だけを要求する。
        return false;
    }
    return MPxLocatorNode::setInternalValue(plug, data);
}

template <FocusBoundsWire Wire>
MStatus BdShpLFocusBoundsNode<Wire>::legalConnection(
    const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
) const {
    if (!asSrc && isPreviewAttribute(plug.attribute())) {
        isLegal = false;
        return MS::kSuccess;
    }
    return MPxLocatorNode::legalConnection(plug, otherPlug, asSrc, isLegal);
}

template <FocusBoundsWire Wire>
std::uint64_t BdShpLFocusBoundsNode<Wire>::previewRevision() const {
    return previewRevision_.load(std::memory_order_acquire);
}

template <FocusBoundsWire Wire>
typename BdShpLFocusBoundsNode<Wire>::Preview BdShpLFocusBoundsNode<Wire>::preview() const {
    const std::lock_guard<std::mutex> lock(previewMutex_);
    const auto revision = previewRevision();
    if (preview_.revision == revision) return preview_;

    MStatus status;
    const auto object = thisMObject();
    const bool visible = MPlug(object, showShape).asBool(&status);
    if (!status) return preview_;

    bdUtilNodes::SignedShapeAxis axes[3] = {{0, 1.0}, {1, 1.0}, {2, 1.0}};
    if constexpr (IsPlanar) {
        const short first = MPlug(object, shape1stAxis).asShort(&status);
        if (!status) return preview_;
        const short second = MPlug(object, shape2ndAxis).asShort(&status);
        if (!status) return preview_;
        const auto resolved = bdUtilNodes::resolveSignedShapeAxes(first, second);
        axes[0] = resolved.first;
        axes[1] = resolved.second;
    }
    MPoint lower, upper;
    for (unsigned int axis = 0; axis < AxisCount; ++axis) {
        const auto direction = axes[axis];
        const double first = -MPlug(object, distances[axis][1]).asMDistance(&status).asCentimeters() * direction.sign;
        if (!status) return preview_;
        const double second = MPlug(object, distances[axis][0]).asMDistance(&status).asCentimeters() * direction.sign;
        if (!status) return preview_;
        lower[direction.component] = std::min(first, second);
        upper[direction.component] = std::max(first, second);
    }
    preview_ = {MBoundingBox(lower, upper), visible, static_cast<std::uint8_t>(axes[0].component),
        static_cast<std::uint8_t>(axes[1].component), revision};
    return preview_;
}

template <FocusBoundsWire Wire>
bool BdShpLFocusBoundsNode<Wire>::isBounded() const {
    return true;
}

template <FocusBoundsWire Wire>
MBoundingBox BdShpLFocusBoundsNode<Wire>::boundingBox() const {
    return preview().bounds;
}

template <FocusBoundsWire Wire>
bool BdShpLFocusBoundsNode<Wire>::excludeAsLocator() const {
    return false;
}

template <FocusBoundsWire Wire>
void BdShpLFocusBoundsNode<Wire>::getCacheSetup(
    const MEvaluationNode& evalNode,
    MNodeCacheDisablingInfo& disablingInfo,
    MNodeCacheSetupInfo& cacheSetupInfo,
    MObjectArray& monitoredAttributes
) const {
    MPxLocatorNode::getCacheSetup(evalNode, disablingInfo, cacheSetupInfo, monitoredAttributes);
    // プレビュー表示中は、キャッシュから親の姿勢を復元するフレームでも描画更新する。
    monitoredAttributes.append(showShape);
    cacheSetupInfo.setPreference(MNodeCacheSetupInfo::kWantToCacheByDefault,
        MPlug(thisMObject(), showShape).asBool());
}

template class BdShpLFocusBoundsNode<FocusBoundsWire::Box>;
template class BdShpLFocusBoundsNode<FocusBoundsWire::CrossLine3Axis>;
template class BdShpLFocusBoundsNode<FocusBoundsWire::Square>;
template class BdShpLFocusBoundsNode<FocusBoundsWire::CrossLine>;
