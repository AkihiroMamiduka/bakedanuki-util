#include "bdUtilNodes/nodes/BdShpLFocusBoundingBoxNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"

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

const MString BdShpLFocusBoundingBoxNode::typeName("bdShpL_FocusBoundingBox");
const MTypeId BdShpLFocusBoundingBoxNode::typeId(0x00142721);
const MString BdShpLFocusBoundingBoxNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingBox");
const MString BdShpLFocusBoundingBoxNode::drawRegistrantId("bdShpLFocusBoundingBoxGeometryOverride");

MObject BdShpLFocusBoundingBoxNode::showShape;
MObject BdShpLFocusBoundingBoxNode::shapeBaseSpaceXPlus;
MObject BdShpLFocusBoundingBoxNode::shapeBaseSpaceXMinus;
MObject BdShpLFocusBoundingBoxNode::shapeBaseSpaceYPlus;
MObject BdShpLFocusBoundingBoxNode::shapeBaseSpaceYMinus;
MObject BdShpLFocusBoundingBoxNode::shapeBaseSpaceZPlus;
MObject BdShpLFocusBoundingBoxNode::shapeBaseSpaceZMinus;

BdShpLFocusBoundingBoxNode::BdShpLFocusBoundingBoxNode() {
    preview_.bounds = bdUtilNodes::fixedCube::bounds();
}

void* BdShpLFocusBoundingBoxNode::creator() {
    return new BdShpLFocusBoundingBoxNode;
}

void BdShpLFocusBoundingBoxNode::postConstructor() {
    MPxLocatorNode::postConstructor();
    const auto node = thisMObject();
    bdUtilNodes::hideLocatorPositionAndScale(node);

    MStatus status;
    auto overrideEnabled = MFnDependencyNode(node).findPlug("overrideEnabled", false, &status);
    if (status) status = overrideEnabled.setBool(false);
    if (status) status = overrideEnabled.setLocked(true);
    if (!status) status.perror("Failed to set the bdShpL_FocusBoundingBox drawing override default");
}

MStatus BdShpLFocusBoundingBoxNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericFn;
    showShape = numericFn.create("showShape", "ss", MFnNumericData::kBoolean, false, &status);
    if (!status) return status;

    struct DistanceAttribute { MObject* object; const char* name; const char* shortName; };
    MFnUnitAttribute unitFn;
    for (const auto& distance : {
        DistanceAttribute{&shapeBaseSpaceXPlus, "shapeBaseSpaceXPlus", "sbsxp"},
        DistanceAttribute{&shapeBaseSpaceXMinus, "shapeBaseSpaceXMinus", "sbsxm"},
        DistanceAttribute{&shapeBaseSpaceYPlus, "shapeBaseSpaceYPlus", "sbsyp"},
        DistanceAttribute{&shapeBaseSpaceYMinus, "shapeBaseSpaceYMinus", "sbsym"},
        DistanceAttribute{&shapeBaseSpaceZPlus, "shapeBaseSpaceZPlus", "sbszp"},
        DistanceAttribute{&shapeBaseSpaceZMinus, "shapeBaseSpaceZMinus", "sbszm"},
    }) {
        *distance.object = unitFn.create(distance.name, distance.shortName,
            MDistance(0.5, MDistance::kCentimeters), &status);
        if (!status) return status;
    }

    for (const auto& attribute : {
        showShape, shapeBaseSpaceXPlus, shapeBaseSpaceXMinus, shapeBaseSpaceYPlus,
        shapeBaseSpaceYMinus, shapeBaseSpaceZPlus, shapeBaseSpaceZMinus,
    }) {
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
        status = fn.setAffectsWorldSpace(attribute != showShape);
        if (!status) return status;
        status = addAttribute(attribute);
        if (!status) return status;
    }
    return MS::kSuccess;
}

bool BdShpLFocusBoundingBoxNode::isPreviewAttribute(const MObject& attribute) {
    return attribute == showShape ||
        attribute == shapeBaseSpaceXPlus || attribute == shapeBaseSpaceXMinus ||
        attribute == shapeBaseSpaceYPlus || attribute == shapeBaseSpaceYMinus ||
        attribute == shapeBaseSpaceZPlus || attribute == shapeBaseSpaceZMinus;
}

bool BdShpLFocusBoundingBoxNode::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    const auto attribute = plug.attribute();
    if (isPreviewAttribute(attribute)) {
        previewRevision_.fetch_add(1, std::memory_order_release);
        MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), attribute == showShape);
        // Maya に値の保存を委ね、編集後の再描画だけを要求する。
        return false;
    }
    return MPxLocatorNode::setInternalValue(plug, data);
}

MStatus BdShpLFocusBoundingBoxNode::legalConnection(
    const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
) const {
    if (!asSrc && isPreviewAttribute(plug.attribute())) {
        isLegal = false;
        return MS::kSuccess;
    }
    return MPxLocatorNode::legalConnection(plug, otherPlug, asSrc, isLegal);
}

std::uint64_t BdShpLFocusBoundingBoxNode::previewRevision() const {
    return previewRevision_.load(std::memory_order_acquire);
}

BdShpLFocusBoundingBoxNode::Preview BdShpLFocusBoundingBoxNode::preview() const {
    const std::lock_guard<std::mutex> lock(previewMutex_);
    const auto revision = previewRevision();
    if (preview_.revision == revision) return preview_;

    MStatus status;
    const auto object = thisMObject();
    const bool visible = MPlug(object, showShape).asBool(&status);
    if (!status) return preview_;

    const MObject minus[] = {shapeBaseSpaceXMinus, shapeBaseSpaceYMinus, shapeBaseSpaceZMinus};
    const MObject plus[] = {shapeBaseSpaceXPlus, shapeBaseSpaceYPlus, shapeBaseSpaceZPlus};
    MPoint lower, upper;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        const double first = -MPlug(object, minus[axis]).asMDistance(&status).asCentimeters();
        if (!status) return preview_;
        const double second = MPlug(object, plus[axis]).asMDistance(&status).asCentimeters();
        if (!status) return preview_;
        lower[axis] = std::min(first, second);
        upper[axis] = std::max(first, second);
    }
    preview_ = {MBoundingBox(lower, upper), visible, revision};
    return preview_;
}

bool BdShpLFocusBoundingBoxNode::isBounded() const {
    return true;
}

MBoundingBox BdShpLFocusBoundingBoxNode::boundingBox() const {
    return preview().bounds;
}

bool BdShpLFocusBoundingBoxNode::excludeAsLocator() const {
    return false;
}

void BdShpLFocusBoundingBoxNode::getCacheSetup(
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
