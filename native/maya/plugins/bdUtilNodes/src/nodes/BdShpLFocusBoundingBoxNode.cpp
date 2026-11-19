#include "bdUtilNodes/nodes/BdShpLFocusBoundingBoxNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"
#include "bdUtilNodes/nodes/SignedShapeAxes.h"

#include <algorithm>

#include <maya/MAnimControl.h>
#include <maya/MCacheSchema.h>
#include <maya/MDistance.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnMatrixData.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MNodeCacheSetupInfo.h>
#include <maya/MObjectArray.h>
#include <maya/MPlug.h>
#include <maya/MViewport2Renderer.h>

template <> const MString BdShpLFocusBoundingBoxNode::typeName("bdShpL_FocusBoundingBox");
template <> const MTypeId BdShpLFocusBoundingBoxNode::typeId(0x00142721);
template <> const MString BdShpLFocusBoundingBoxNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingBox");
template <> const MString BdShpLFocusBoundingBoxNode::drawRegistrantId("bdShpLFocusBoundingBoxGeometryOverride");

template <> const MString BdShpLFocusBoundingSquareNode::typeName("bdShpL_FocusBoundingSquare");
template <> const MTypeId BdShpLFocusBoundingSquareNode::typeId(0x00142722);
template <> const MString BdShpLFocusBoundingSquareNode::drawClassification("drawdb/geometry/bdShpL_FocusBoundingSquare");
template <> const MString BdShpLFocusBoundingSquareNode::drawRegistrantId("bdShpLFocusBoundingSquareGeometryOverride");

template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::showShape;
template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::shape1stAxis;
template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::shape2ndAxis;
template <FocusBoundsWire Wire> MObject BdShpLFocusBoundsNode<Wire>::shapeTransformMatrix;
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
    preview_.revision = previewRevision_.load(std::memory_order_relaxed);
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
void BdShpLFocusBoundsNode<Wire>::copyInternalData(MPxNode* source) {
    MPxLocatorNode::copyInternalData(source);
    const auto* focus = static_cast<const BdShpLFocusBoundsNode<Wire>*>(source);
    if (focus && (focus->previewRevision_.load(std::memory_order_acquire) & kMatrixUsed)) {
        previewRevision_.fetch_or(kMatrixUsed, std::memory_order_release);
    }
    // Maya がコピーした入力値で、初期化済みの境界を作り直す。
    previewRevision_.fetch_add(1, std::memory_order_release);
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
    MFnMatrixData matrixData;
    const auto identity = matrixData.create(MMatrix::identity, &status);
    if (!status) return status;
    MFnTypedAttribute matrixAttribute;
    shapeTransformMatrix = matrixAttribute.create(
        "shapeTransformMatrix", "stm", MFnData::kMatrix, identity, &status);
    if (!status) return status;
    status = matrixAttribute.setKeyable(false);
    if (!status) return status;
    status = matrixAttribute.setChannelBox(false);
    if (!status) return status;
    status = matrixAttribute.setInternal(true);
    if (!status) return status;
    status = matrixAttribute.setAffectsAppearance(true);
    if (!status) return status;
    status = matrixAttribute.setAffectsWorldSpace(true);
    if (!status) return status;
    return addAttribute(shapeTransformMatrix);
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
    if (attribute == shapeTransformMatrix) {
        previewRevision_.fetch_or(kMatrixUsed, std::memory_order_release);
        dirtyPreview(false);
        return false;
    }
    if (isPreviewAttribute(attribute)) {
        dirtyPreview(attribute == showShape);
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
void BdShpLFocusBoundsNode<Wire>::dirtyPreview(bool topologyChanged) {
    previewRevision_.fetch_add(1, std::memory_order_release);
    MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), topologyChanged);
}

template <FocusBoundsWire Wire>
void BdShpLFocusBoundsNode<Wire>::matrixConnectionChanged(bool connected) {
    if (connected) {
        previewRevision_.fetch_or(kMatrixUsed | kMatrixConnected, std::memory_order_release);
    } else {
        previewRevision_.fetch_and(~kMatrixConnected, std::memory_order_release);
    }
    dirtyPreview(false);
}

template <FocusBoundsWire Wire>
MStatus BdShpLFocusBoundsNode<Wire>::connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) {
    if (!asSrc && plug.attribute() == shapeTransformMatrix) matrixConnectionChanged(true);
    return MPxLocatorNode::connectionMade(plug, otherPlug, asSrc);
}

template <FocusBoundsWire Wire>
MStatus BdShpLFocusBoundsNode<Wire>::connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) {
    if (!asSrc && plug.attribute() == shapeTransformMatrix) matrixConnectionChanged(false);
    return MPxLocatorNode::connectionBroken(plug, otherPlug, asSrc);
}

template <FocusBoundsWire Wire>
typename BdShpLFocusBoundsNode<Wire>::Preview BdShpLFocusBoundsNode<Wire>::preview() const {
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

    bdUtilNodes::SignedShapeAxis axes[3] = {{0, 1.0}, {1, 1.0}, {2, 1.0}};
    if constexpr (IsPlanar) {
        const short first = MPlug(object, shape1stAxis).asShort(&status);
        if (!status) return previous;
        const short second = MPlug(object, shape2ndAxis).asShort(&status);
        if (!status) return previous;
        const auto resolved = bdUtilNodes::resolveSignedShapeAxes(first, second);
        axes[0] = resolved.first;
        axes[1] = resolved.second;
    }
    MPoint lower, upper;
    for (unsigned int axis = 0; axis < AxisCount; ++axis) {
        const auto direction = axes[axis];
        const double first = -MPlug(object, distances[axis][1]).asMDistance(&status).asCentimeters() * direction.sign;
        if (!status) return previous;
        const double second = MPlug(object, distances[axis][0]).asMDistance(&status).asCentimeters() * direction.sign;
        if (!status) return previous;
        lower[direction.component] = std::min(first, second);
        upper[direction.component] = std::max(first, second);
    }
    lock.lock();
    if (previewRevision_.load(std::memory_order_acquire) == revision) {
        preview_ = {MBoundingBox(lower, upper), visible, static_cast<std::uint8_t>(axes[0].component),
            static_cast<std::uint8_t>(axes[1].component), revision};
    }
    return preview_;
}

template <FocusBoundsWire Wire>
MPoint BdShpLFocusBoundsNode<Wire>::corner(
    const Preview& preview, const MPoint& lower, const MPoint& upper, unsigned int index
) {
    const auto& unit = bdUtilNodes::fixedCube::vertices[index];
    if constexpr (IsPlanar) {
        MPoint point;
        point[preview.firstAxis] = unit[0] < 0 ? lower[preview.firstAxis] : upper[preview.firstAxis];
        point[preview.secondAxis] = unit[1] < 0 ? lower[preview.secondAxis] : upper[preview.secondAxis];
        return point;
    } else {
        return MPoint(unit[0] < 0 ? lower.x : upper.x, unit[1] < 0 ? lower.y : upper.y,
            unit[2] < 0 ? lower.z : upper.z);
    }
}

template <FocusBoundsWire Wire>
MMatrix BdShpLFocusBoundsNode<Wire>::readShapeMatrix(MStatus& status) const {
    const auto data = MPlug(thisMObject(), shapeTransformMatrix).asMObject(&status);
    if (!status) return MMatrix::identity;
    const MFnMatrixData matrixData(data, &status);
    return status ? matrixData.matrix(&status) : MMatrix::identity;
}

template <FocusBoundsWire Wire>
typename BdShpLFocusBoundsNode<Wire>::Geometry BdShpLFocusBoundsNode<Wire>::previewGeometry() const {
    const auto base = preview();
    Geometry geometry;
    geometry.visible = base.visible;
    // 非表示のプレビューは入力行列を読まず、境界は `boundingBox()` に任せる。
    geometry.revision = base.revision & ~kMatrixConnected;
    if (!base.visible) return geometry;
    geometry.revision |= kPreviewVisible;

    MStatus status;
    const auto shapeMatrix = base.revision & kMatrixUsed ? readShapeMatrix(status) : MMatrix::identity;
    const bool transform = status && shapeMatrix != MMatrix::identity;
    if (!transform) geometry.bounds = base.bounds;
    const auto lower = base.bounds.min();
    const auto upper = base.bounds.max();
    for (unsigned int index = 0; index < VertexCount; ++index) {
        auto point = corner(base, lower, upper, index);
        if (transform) {
            point *= shapeMatrix;
            geometry.bounds.expand(point);
        }
        for (unsigned int axis = 0; axis < 3; ++axis) {
            geometry.vertices[index][axis] = static_cast<float>(point[axis]);
        }
    }
    return geometry;
}

template <FocusBoundsWire Wire>
bool BdShpLFocusBoundsNode<Wire>::isBounded() const {
    return true;
}

template <FocusBoundsWire Wire>
MBoundingBox BdShpLFocusBoundsNode<Wire>::boundingBox() const {
    const auto base = preview();
    if (!(base.revision & kMatrixUsed)) return base.bounds;

    const bool connected = (base.revision & kMatrixConnected) != 0;
    // 非表示のフォーカス範囲は、再生中の境界照会では入力行列を評価しない。
    if (connected && !base.visible && MAnimControl::isPlaying()) return base.bounds;
    if (!connected) {
        const std::lock_guard<std::mutex> lock(previewMutex_);
        if (transformedBounds_ && transformedBounds_->revision == base.revision) {
            return transformedBounds_->bounds;
        }
    }

    // 接続中はキャッシュ復元や時間移動で、同じリビジョンにも別の行列が入る。
    MStatus status;
    const auto shapeMatrix = readShapeMatrix(status);
    if (!status) return base.bounds;

    const std::lock_guard<std::mutex> lock(previewMutex_);
    if (!transformedBounds_) transformedBounds_ = std::make_unique<TransformedBounds>();
    auto& cached = *transformedBounds_;
    if (cached.revision != base.revision || cached.matrix != shapeMatrix) {
        MBoundingBox bounds;
        if (shapeMatrix == MMatrix::identity) {
            bounds = base.bounds;
        } else {
            const auto lower = base.bounds.min();
            const auto upper = base.bounds.max();
            for (unsigned int index = 0; index < VertexCount; ++index) {
                bounds.expand(corner(base, lower, upper, index) * shapeMatrix);
            }
        }
        cached = {shapeMatrix, bounds, base.revision};
    }
    return cached.bounds;
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

template <FocusBoundsWire Wire>
void BdShpLFocusBoundsNode<Wire>::configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const {
    MPxLocatorNode::configCache(evalNode, schema);
    if ((previewRevision_.load(std::memory_order_acquire) & kMatrixConnected) &&
        MPlug(thisMObject(), showShape).asBool()) {
        const auto status = schema.add(shapeTransformMatrix);
        if (!status) status.perror("Could not cache the focus shape's shapeTransformMatrix");
    }
}

template class BdShpLFocusBoundsNode<FocusBoundsWire::Box>;
template class BdShpLFocusBoundsNode<FocusBoundsWire::Square>;
