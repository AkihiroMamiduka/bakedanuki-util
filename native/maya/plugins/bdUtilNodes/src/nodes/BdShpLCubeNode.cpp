#include "bdUtilNodes/nodes/BdShpLCubeNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"
#include "bdUtilNodes/nodes/SignedShapeAxes.h"

#include <cstring>

#include <maya/MCacheSchema.h>
#include <maya/MDistance.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnMatrixData.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MNodeCacheSetupInfo.h>
#include <maya/MPlug.h>
#include <maya/MVector.h>
#include <maya/MViewport2Renderer.h>

#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

const MString BdShpLCubeNode::typeName("bdShpL_Cube");
const MTypeId BdShpLCubeNode::typeId(0x00142720);
const MString BdShpLCubeNode::drawClassification("drawdb/geometry/bdShpL_Cube");
const MString BdShpLCubeNode::drawRegistrantId("bdShpLCubeGeometryOverride");

MObject BdShpLCubeNode::shape1stAxis;
MObject BdShpLCubeNode::shape2ndAxis;
MObject BdShpLCubeNode::shapeBaseSpace1stAxisPlus;
MObject BdShpLCubeNode::shapeBaseSpace1stAxisMinus;
MObject BdShpLCubeNode::shapeBaseSpace2ndAxisPlus;
MObject BdShpLCubeNode::shapeBaseSpace2ndAxisMinus;
MObject BdShpLCubeNode::shapeBaseSpace3rdAxisPlus;
MObject BdShpLCubeNode::shapeBaseSpace3rdAxisMinus;
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
MObject BdShpLCubeNode::shapeTransformMatrix;
#endif

BdShpLCubeNode::BdShpLCubeNode() {
    std::memcpy(geometry_.vertices, bdUtilNodes::fixedCube::vertices, sizeof(geometry_.vertices));
    geometry_.bounds = bdUtilNodes::fixedCube::bounds();
}

void* BdShpLCubeNode::creator() {
    return new BdShpLCubeNode;
}

void BdShpLCubeNode::postConstructor() {
    MPxLocatorNode::postConstructor();
    bdUtilNodes::hideLocatorPositionAndScale(thisMObject());
}

#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
void BdShpLCubeNode::copyInternalData(MPxNode* source) {
    MPxLocatorNode::copyInternalData(source);
    // 複製時は Maya が入力値をコピーするため、行列を参照する状態だけ引き継ぐ。
    const auto* cube = static_cast<const BdShpLCubeNode*>(source);
    if (cube && (cube->geometryRevision() & kAnimationUsed)) {
        geometryRevision_.fetch_or(kAnimationUsed, std::memory_order_release);
    }
}
#endif

MStatus BdShpLCubeNode::initialize() {
    MStatus status;
    shape1stAxis = bdUtilNodes::createSignedAxisAttribute("shape1stAxis", "s1a", 0, status);
    if (!status) return status;
    shape2ndAxis = bdUtilNodes::createSignedAxisAttribute("shape2ndAxis", "s2a", 2, status);
    if (!status) return status;
    struct DistanceAttribute { MObject* object; const char* name; const char* shortName; };
    MFnUnitAttribute unitFn;
    for (const auto& value : {
        DistanceAttribute{&shapeBaseSpace1stAxisPlus, "shapeBaseSpace1stAxisPlus", "sbsp1p"},
        DistanceAttribute{&shapeBaseSpace1stAxisMinus, "shapeBaseSpace1stAxisMinus", "sbsp1m"},
        DistanceAttribute{&shapeBaseSpace2ndAxisPlus, "shapeBaseSpace2ndAxisPlus", "sbsp2p"},
        DistanceAttribute{&shapeBaseSpace2ndAxisMinus, "shapeBaseSpace2ndAxisMinus", "sbsp2m"},
        DistanceAttribute{&shapeBaseSpace3rdAxisPlus, "shapeBaseSpace3rdAxisPlus", "sbsp3p"},
        DistanceAttribute{&shapeBaseSpace3rdAxisMinus, "shapeBaseSpace3rdAxisMinus", "sbsp3m"},
    }) {
        *value.object = unitFn.create(value.name, value.shortName,
            MDistance(0.5, MDistance::kCentimeters), &status);
        if (!status) return status;
    }
    for (const auto& attribute : {
        shape1stAxis, shape2ndAxis,
        shapeBaseSpace1stAxisPlus, shapeBaseSpace1stAxisMinus,
        shapeBaseSpace2ndAxisPlus, shapeBaseSpace2ndAxisMinus,
        shapeBaseSpace3rdAxisPlus, shapeBaseSpace3rdAxisMinus,
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
        status = fn.setAffectsWorldSpace(true);
        if (!status) return status;
        status = addAttribute(attribute);
        if (!status) return status;
    }
#ifndef BD_CUBE_RESEARCH_SHAPE_MATRIX
    return MS::kSuccess;
#else
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
#endif
}

bool BdShpLCubeNode::isShapeAttribute(const MObject& attribute) {
    return attribute == shape1stAxis || attribute == shape2ndAxis ||
        attribute == shapeBaseSpace1stAxisPlus || attribute == shapeBaseSpace1stAxisMinus ||
        attribute == shapeBaseSpace2ndAxisPlus || attribute == shapeBaseSpace2ndAxisMinus ||
        attribute == shapeBaseSpace3rdAxisPlus || attribute == shapeBaseSpace3rdAxisMinus;
}

bool BdShpLCubeNode::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    const auto attribute = plug.attribute();
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    if (attribute == shapeTransformMatrix) {
        geometryRevision_.fetch_or(kAnimationUsed, std::memory_order_release);
        dirtyGeometry();
        return false;
    }
#endif
    if (isShapeAttribute(attribute)) {
        dirtyGeometry();
        // 値の保存は通常のdatablockへ委譲し、編集通知だけを保持する。
        return false;
    }
    return MPxLocatorNode::setInternalValue(plug, data);
}

MStatus BdShpLCubeNode::legalConnection(
    const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
) const {
    if (!asSrc && isShapeAttribute(plug.attribute())) {
        isLegal = false;
        return MS::kSuccess;
    }
    return MPxLocatorNode::legalConnection(plug, otherPlug, asSrc, isLegal);
}

void BdShpLCubeNode::dirtyGeometry() {
    geometryRevision_.fetch_add(1, std::memory_order_release);
#ifdef BD_CUBE_DRAW_OVERRIDE
    MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), true);
#else
    MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), false);
#endif
}

#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
void BdShpLCubeNode::setAnimationConnection(bool connected) {
    if (connected) {
        geometryRevision_.fetch_or(kAnimationUsed | kAnimationConnected, std::memory_order_release);
    } else {
        geometryRevision_.fetch_and(~kAnimationConnected, std::memory_order_release);
    }
    dirtyGeometry();
}

MStatus BdShpLCubeNode::connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) {
    if (!asSrc && plug.attribute() == shapeTransformMatrix) setAnimationConnection(true);
    return MPxLocatorNode::connectionMade(plug, otherPlug, asSrc);
}

MStatus BdShpLCubeNode::connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) {
    if (!asSrc && plug.attribute() == shapeTransformMatrix) setAnimationConnection(false);
    return MPxLocatorNode::connectionBroken(plug, otherPlug, asSrc);
}
#endif

std::uint64_t BdShpLCubeNode::geometryRevision() const {
    return geometryRevision_.load(std::memory_order_acquire);
}

BdShpLCubeNode::Geometry BdShpLCubeNode::geometry() const {
#ifndef BD_CUBE_RESEARCH_SHAPE_MATRIX
    const std::lock_guard<std::mutex> lock(geometryMutex_);
    const auto revision = geometryRevision();
#else
    std::unique_lock<std::mutex> lock(geometryMutex_);
    const auto revisionWithFlags = geometryRevision();
    // 接続中は前回描画と同じリビジョンにせず、キャッシュ復元時も入力行列を読む。
    const auto revision = revisionWithFlags & ~kAnimationConnected;
    if (revisionWithFlags & kAnimationUsed) {
        if (!(revisionWithFlags & kAnimationConnected) && animation_ && geometry_.revision == revision) {
            return animation_->useTransformed ? animation_->transformed : geometry_;
        }
        lock.unlock();
        return geometryWithAnimationMatrix(revision);
    }
#endif
    if (geometry_.revision != revision) updateBaseGeometry(revision);
    return geometry_;
}

bool BdShpLCubeNode::updateBaseGeometry(std::uint64_t revision) const {
    MStatus status;
    const auto object = thisMObject();
    const short first = MPlug(object, shape1stAxis).asShort(&status);
    if (!status) return false;
    const short second = MPlug(object, shape2ndAxis).asShort(&status);
    if (!status) return false;
    const MObject distanceAttributes[3][2] = {
        {shapeBaseSpace1stAxisMinus, shapeBaseSpace1stAxisPlus},
        {shapeBaseSpace2ndAxisMinus, shapeBaseSpace2ndAxisPlus},
        {shapeBaseSpace3rdAxisMinus, shapeBaseSpace3rdAxisPlus},
    };
    double limits[3][2];
    for (unsigned int axis = 0; axis < 3; ++axis) {
        for (unsigned int side = 0; side < 2; ++side) {
            limits[axis][side] = MPlug(object, distanceAttributes[axis][side])
                .asMDistance(&status).asCentimeters() * (side == 0 ? -1 : 1);
            if (!status) return false;
        }
    }
    const auto axes = bdUtilNodes::resolveSignedShapeAxes(first, second);
    const auto firstVector = axes.first.vector();
    const auto secondVector = axes.second.vector();
    const auto thirdVector = firstVector ^ secondVector;
    Geometry result;
    for (unsigned int i = 0; i < 8; ++i) {
        const auto& original = bdUtilNodes::fixedCube::vertices[i];
        const auto point = MPoint::origin + firstVector * limits[0][original[0] > 0] +
            secondVector * limits[1][original[1] > 0] + thirdVector * limits[2][original[2] > 0];
#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
        if (animation_) animation_->basePositions[i] = point;
#endif
        result.bounds.expand(point);
        for (unsigned int axis = 0; axis < 3; ++axis) {
            result.vertices[i][axis] = static_cast<float>(point[axis]);
        }
    }
    result.revision = revision;
    geometry_ = result;
    return true;
}

#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
BdShpLCubeNode::Geometry BdShpLCubeNode::geometryWithAnimationMatrix(std::uint64_t revision) const {
    MMatrix animationMatrix = MMatrix::identity;
    {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::matrixRead);
#endif
        MStatus status;
        const auto data = MPlug(thisMObject(), shapeTransformMatrix).asMObject(&status);
        if (status) {
            MFnMatrixData matrixData(data, &status);
            if (status) animationMatrix = matrixData.matrix();
        }
    }
    const std::lock_guard<std::mutex> lock(geometryMutex_);
    const bool needsBase = !animation_ || geometry_.revision != revision;
    if (!animation_) animation_ = std::make_unique<AnimationGeometry>();
    if (needsBase && !updateBaseGeometry(revision)) return geometry_;

    if (animationMatrix == MMatrix::identity) {
        animation_->useTransformed = false;
        return geometry_;
    }
    if (animation_->transformed.revision != revision || animation_->matrix != animationMatrix) {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::geometryRebuild);
#endif
        Geometry result;
        for (unsigned int i = 0; i < 8; ++i) {
            const auto point = animation_->basePositions[i] * animationMatrix;
            result.bounds.expand(point);
            for (unsigned int axis = 0; axis < 3; ++axis) {
                result.vertices[i][axis] = static_cast<float>(point[axis]);
            }
        }
        result.revision = revision;
        animation_->transformed = result;
        animation_->matrix = animationMatrix;
    }
    animation_->useTransformed = true;
    return animation_->transformed;
}
#endif

#if defined(BD_CUBE_RESEARCH_SHAPE_MATRIX) && (defined(BD_CUBE_DRAW_OVERRIDE) || defined(BD_CUBE_SUBSCENE_MATRIX))
BdShpLCubeNode::Geometry BdShpLCubeNode::baseDrawGeometry() const {
    std::unique_lock<std::mutex> lock(geometryMutex_);
    auto revision = geometryRevision();
    if (geometry_.revision != (revision & ~kAnimationConnected)) {
        // 静的編集後は本体の変形済み境界も先に更新する。
        lock.unlock();
        geometry();
        lock.lock();
        revision = geometryRevision();
    }
    auto result = geometry_;
    if (result.revision == (revision & ~kAnimationConnected)) result.revision = revision;
    return result;
}

MMatrix BdShpLCubeNode::shapeDrawMatrix() const {
    if (!(geometryRevision() & kAnimationUsed)) return MMatrix::identity;
    MStatus status;
    const auto data = MPlug(thisMObject(), shapeTransformMatrix).asMObject(&status);
    if (!status) return MMatrix::identity;
    MFnMatrixData matrixData(data, &status);
    if (!status) return MMatrix::identity;
    auto shapeMatrix = matrixData.matrix();
    // 本体は各頂点の変換結果の xyz を採用する。射影成分は DAG の親行列に渡さない。
    shapeMatrix[0][3] = shapeMatrix[1][3] = shapeMatrix[2][3] = 0.0;
    shapeMatrix[3][3] = 1.0;
    return shapeMatrix;
}
#endif

bool BdShpLCubeNode::isBounded() const {
    return true;
}

void BdShpLCubeNode::getCacheSetup(
    const MEvaluationNode& evalNode,
    MNodeCacheDisablingInfo& disablingInfo,
    MNodeCacheSetupInfo& cacheSetupInfo,
    MObjectArray& monitoredAttributes
) const {
    MPxLocatorNode::getCacheSetup(evalNode, disablingInfo, cacheSetupInfo, monitoredAttributes);
    // Cached Playbackで親の姿勢を復元するときも、このlocatorを描画更新の対象にする。
    cacheSetupInfo.setPreference(MNodeCacheSetupInfo::kWantToCacheByDefault, true);
}

#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
void BdShpLCubeNode::configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const {
    MPxLocatorNode::configCache(evalNode, schema);
    // 描画更新から読む入力行列を、接続がある場合はフレームごとに復元する。
    if (geometryRevision() & kAnimationConnected) {
        const auto status = schema.add(shapeTransformMatrix);
        if (!status) status.perror("Could not cache bdShpL_Cube.shapeTransformMatrix");
    }
}
#endif

MBoundingBox BdShpLCubeNode::boundingBox() const {
#ifdef BD_CUBE_PROFILE
    cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::bounds);
#endif
    return geometry().bounds;
}

bool BdShpLCubeNode::excludeAsLocator() const {
    return false;
}

#ifdef BD_CUBE_NODE_PARALLEL
MPxNode::SchedulingType BdShpLCubeNode::schedulingType() const {
    return MPxNode::kParallel;
}
#endif
