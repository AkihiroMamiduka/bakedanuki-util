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
std::array<std::array<MObject, 2>, BdShpLFocusBoundingBoxNode::AxisCount>
    BdShpLFocusBoundingBoxNode::distances;

BdShpLFocusBoundingBoxNode::BdShpLFocusBoundingBoxNode() {
    preview_.bounds = bdUtilNodes::fixedCube::bounds();
    preview_.revision = previewRevision_.load(std::memory_order_relaxed);
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
    if (!status) status.perror("Failed to set the focus bounding shape drawing override default");
}

void BdShpLFocusBoundingBoxNode::copyInternalData(MPxNode* source) {
    MPxLocatorNode::copyInternalData(source);
    // Maya がコピーした入力値で、初期化済みの境界を作り直す。
    previewRevision_.fetch_add(1, std::memory_order_release);
}

MStatus BdShpLFocusBoundingBoxNode::initialize() {
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

    struct AttributeNames { const char* name; const char* shortName; };
    constexpr AttributeNames names[AxisCount][2] = {
        {{"shapeBaseSpaceXPlus", "sbsxp"}, {"shapeBaseSpaceXMinus", "sbsxm"}},
        {{"shapeBaseSpaceYPlus", "sbsyp"}, {"shapeBaseSpaceYMinus", "sbsym"}},
        {{"shapeBaseSpaceZPlus", "sbszp"}, {"shapeBaseSpaceZMinus", "sbszm"}},
    };
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

bool BdShpLFocusBoundingBoxNode::isPreviewAttribute(const MObject& attribute) {
    if (attribute == showShape) return true;
    for (const auto& sides : distances) {
        if (attribute == sides[0] || attribute == sides[1]) return true;
    }
    return false;
}

bool BdShpLFocusBoundingBoxNode::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    const auto attribute = plug.attribute();
    if (isPreviewAttribute(attribute)) {
        dirtyPreview(attribute == showShape);
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

void BdShpLFocusBoundingBoxNode::dirtyPreview(bool topologyChanged) {
    previewRevision_.fetch_add(1, std::memory_order_release);
    MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), topologyChanged);
}

BdShpLFocusBoundingBoxNode::Preview BdShpLFocusBoundingBoxNode::preview() const {
    std::unique_lock<std::mutex> lock(previewMutex_);
    const auto revision = previewRevision_.load(std::memory_order_acquire);
    if (preview_.revision == revision) return preview_;
    const auto previous = preview_;
    // DG 評価が境界を問い合わせても、同じキャッシュロックを待たせない。
    lock.unlock();

    MStatus status;
    const auto object = thisMObject();
    const bool visible = MPlug(object, showShape).asBool(&status);
    if (!status) return previous;

    MPoint lower, upper;
    for (unsigned int axis = 0; axis < AxisCount; ++axis) {
        const double minus = -MPlug(object, distances[axis][1]).asMDistance(&status).asCentimeters();
        if (!status) return previous;
        const double plus = MPlug(object, distances[axis][0]).asMDistance(&status).asCentimeters();
        if (!status) return previous;
        lower[axis] = std::min(minus, plus);
        upper[axis] = std::max(minus, plus);
    }
    lock.lock();
    if (previewRevision_.load(std::memory_order_acquire) == revision) {
        preview_ = {MBoundingBox(lower, upper), visible, revision};
    }
    return preview_;
}

BdShpLFocusBoundingBoxNode::Geometry BdShpLFocusBoundingBoxNode::previewGeometry() const {
    const auto base = preview();
    Geometry geometry;
    geometry.visible = base.visible;
    geometry.revision = base.revision;
    if (!base.visible) return geometry;

    geometry.bounds = base.bounds;
    const auto lower = base.bounds.min();
    const auto upper = base.bounds.max();
    for (unsigned int index = 0; index < VertexCount; ++index) {
        const auto& unit = bdUtilNodes::fixedCube::vertices[index];
        const MPoint point(unit[0] < 0 ? lower.x : upper.x, unit[1] < 0 ? lower.y : upper.y,
            unit[2] < 0 ? lower.z : upper.z);
        for (unsigned int axis = 0; axis < 3; ++axis) {
            geometry.vertices[index][axis] = static_cast<float>(point[axis]);
        }
    }
    return geometry;
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
