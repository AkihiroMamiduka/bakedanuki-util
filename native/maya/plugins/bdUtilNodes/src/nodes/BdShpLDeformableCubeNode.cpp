#include "bdUtilNodes/nodes/BdShpLDeformableCubeNode.h"
#include "bdUtilNodes/nodes/FixedCubeShape.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <cstring>

#include <maya/MCacheSchema.h>
#include <maya/MDGContext.h>
#include <maya/MEvaluationNode.h>
#include <maya/MFnMatrixData.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MNodeCacheSetupInfo.h>
#include <maya/MPlug.h>
#include <maya/MViewport2Renderer.h>

#ifdef BD_CUBE_RESEARCH_FIN
const MString BdShpLDeformableCubeNode::typeName("bdShpL_DeformableCubeWithFin");
const MTypeId BdShpLDeformableCubeNode::typeId(0x00142725);
const MString BdShpLDeformableCubeNode::drawClassification("drawdb/subscene/bdShpL_DeformableCubeWithFin");
const MString BdShpLDeformableCubeNode::drawRegistrantId("bdShpLDeformableCubeWithFinSubSceneOverride");
#else
const MString BdShpLDeformableCubeNode::typeName("bdShpL_DeformableCube");
const MTypeId BdShpLDeformableCubeNode::typeId(0x00142723);
const MString BdShpLDeformableCubeNode::drawClassification("drawdb/subscene/bdShpL_DeformableCube");
const MString BdShpLDeformableCubeNode::drawRegistrantId("bdShpLDeformableCubeSubSceneOverride");
#endif

bdUtilNodes::fixedCube::ShapeAttributes BdShpLDeformableCubeNode::shapeAttributes_;
MObject BdShpLDeformableCubeNode::shapeDeformMatrix;

BdShpLDeformableCubeNode::BdShpLDeformableCubeNode() {
#ifdef BD_CUBE_RESEARCH_FIN
    baseGeometry_ = bdUtilNodes::fixedCube::initialGeometry();
#else
    std::memcpy(baseGeometry_.vertices, bdUtilNodes::fixedCube::vertices, sizeof(baseGeometry_.vertices));
    baseGeometry_.bounds = bdUtilNodes::fixedCube::bounds();
#endif
}

void* BdShpLDeformableCubeNode::creator() {
    return new BdShpLDeformableCubeNode;
}

MStatus BdShpLDeformableCubeNode::initialize() {
    MStatus status = shapeAttributes_.initialize();
    if (!status) return status;

    MFnMatrixData matrixData;
    const auto identity = matrixData.create(MMatrix::identity, &status);
    if (!status) return status;
    MFnTypedAttribute attribute;
    shapeDeformMatrix = attribute.create("shapeDeformMatrix", "sdm", MFnData::kMatrix, identity, &status);
    if (!status) return status;
    status = attribute.setKeyable(false);
    if (!status) return status;
    status = attribute.setChannelBox(false);
    if (!status) return status;
    status = attribute.setInternal(true);
    if (!status) return status;
    status = attribute.setAffectsAppearance(true);
    if (!status) return status;
    status = attribute.setAffectsWorldSpace(true);
    if (!status) return status;
    return addAttribute(shapeDeformMatrix);
}

void BdShpLDeformableCubeNode::postConstructor() {
    MPxLocatorNode::postConstructor();
    bdUtilNodes::hideLocatorPositionAndScale(thisMObject());
}

void BdShpLDeformableCubeNode::copyInternalData(MPxNode* source) {
    MPxLocatorNode::copyInternalData(source);
    // 複製先の datablock から、Maya が複製した基準形状と行列を読み直す。
    geometryRevision_.fetch_add(1, std::memory_order_release);
    matrixRevision_.fetch_add(1, std::memory_order_release);
}

bool BdShpLDeformableCubeNode::isBounded() const {
    return true;
}

MBoundingBox BdShpLDeformableCubeNode::boundingBox() const {
#ifdef BD_CUBE_PROFILE
    cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::bounds);
#endif
#ifdef BD_CUBE_RESEARCH_FIN
    const auto geometry = baseDrawGeometry();
    return bdUtilNodes::fixedCube::transformedBounds(geometry, shapeDrawMatrix());
#else
    auto bounds = baseDrawGeometry().bounds;
    const auto deformMatrix = shapeDrawMatrix();
    // 基準形状の頂点は軸平行な境界の8隅にある。
    if (deformMatrix != MMatrix::identity) bounds.transformUsing(deformMatrix);
    return bounds;
#endif
}

bool BdShpLDeformableCubeNode::excludeAsLocator() const {
    return false;
}

MStatus BdShpLDeformableCubeNode::setDependentsDirty(const MPlug& plug, MPlugArray& affected) {
    if (plug.attribute() == shapeDeformMatrix) {
        matrixRevision_.fetch_add(1, std::memory_order_release);
    }
    return MPxLocatorNode::setDependentsDirty(plug, affected);
}

MStatus BdShpLDeformableCubeNode::postEvaluation(
    const MDGContext& context, const MEvaluationNode& evaluationNode, PostEvaluationType evalType
) {
    if (matrixConnected_.load(std::memory_order_acquire) && context.isNormal()) {
        MStatus status;
        const bool dirty = evaluationNode.dirtyPlugExists(shapeDeformMatrix, &status);
        // 通常コンテキストの描画が再取得するよう、評価側では世代だけ進める。
        if (dirty || !status || evalType == kLeaveDirty) {
            matrixRevision_.fetch_add(1, std::memory_order_release);
        }
    }
    return MPxLocatorNode::postEvaluation(context, evaluationNode, evalType);
}

bool BdShpLDeformableCubeNode::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    const auto attribute = plug.attribute();
    if (attribute == shapeDeformMatrix) {
        dirtyMatrix();
        return false;
    }
    if (shapeAttributes_.contains(attribute)) {
        geometryRevision_.fetch_add(1, std::memory_order_release);
        MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), false);
        return false;
    }
    return MPxLocatorNode::setInternalValue(plug, data);
}

MStatus BdShpLDeformableCubeNode::legalConnection(
    const MPlug& plug, const MPlug& otherPlug, bool asSrc, bool& isLegal
) const {
    if (!asSrc && shapeAttributes_.contains(plug.attribute())) {
        isLegal = false;
        return MS::kSuccess;
    }
    return MPxLocatorNode::legalConnection(plug, otherPlug, asSrc, isLegal);
}

MStatus BdShpLDeformableCubeNode::connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) {
    if (!asSrc && plug.attribute() == shapeDeformMatrix) {
        matrixConnected_.store(true, std::memory_order_release);
        dirtyMatrix();
    }
    return MPxLocatorNode::connectionMade(plug, otherPlug, asSrc);
}

MStatus BdShpLDeformableCubeNode::connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) {
    if (!asSrc && plug.attribute() == shapeDeformMatrix) {
        matrixConnected_.store(false, std::memory_order_release);
        dirtyMatrix();
    }
    return MPxLocatorNode::connectionBroken(plug, otherPlug, asSrc);
}

void BdShpLDeformableCubeNode::getCacheSetup(
    const MEvaluationNode& evalNode,
    MNodeCacheDisablingInfo& disablingInfo,
    MNodeCacheSetupInfo& cacheSetupInfo,
    MObjectArray& monitoredAttributes
) const {
    MPxLocatorNode::getCacheSetup(evalNode, disablingInfo, cacheSetupInfo, monitoredAttributes);
    cacheSetupInfo.setPreference(MNodeCacheSetupInfo::kWantToCacheByDefault, true);
}

void BdShpLDeformableCubeNode::configCache(const MEvaluationNode& evalNode, MCacheSchema& schema) const {
    MPxLocatorNode::configCache(evalNode, schema);
    // 描画更新が参照する接続済みの入力を、キャッシュからフレームごとに復元する。
    if (matrixConnected_.load(std::memory_order_acquire)) {
        const auto status = schema.add(shapeDeformMatrix);
        if (!status) status.perror("Could not cache bdShpL_DeformableCube.shapeDeformMatrix");
    }
}

std::uint64_t BdShpLDeformableCubeNode::geometryRevision() const {
    return geometryRevision_.load(std::memory_order_acquire);
}

BdShpLDeformableCubeNode::Geometry BdShpLDeformableCubeNode::baseDrawGeometry() const {
#ifdef BD_CUBE_PROFILE
    cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::baseGeometryAccess);
#endif
    const std::lock_guard<std::mutex> lock(dataMutex_);
    const auto revision = geometryRevision();
    if (baseGeometry_.revision != revision) {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope rebuildScope(cubeResearch::profiling::Method::baseGeometryRebuild);
#endif
        MPoint positions[bdUtilNodes::fixedCube::vertexCount];
        if (shapeAttributes_.readPositions(thisMObject(), positions)) {
            baseGeometry_ = bdUtilNodes::fixedCube::geometryFromPositions(positions, revision);
        }
    }
    return baseGeometry_;
}

void BdShpLDeformableCubeNode::dirtyMatrix() {
    matrixRevision_.fetch_add(1, std::memory_order_release);
    MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), false);
}

bool BdShpLDeformableCubeNode::readShapeMatrix(MMatrix& deformMatrix) const {
#ifdef BD_CUBE_PROFILE
    cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::matrixRead);
#endif
    MStatus status;
    const auto data = MPlug(thisMObject(), shapeDeformMatrix).asMObject(&status);
    if (!status) return false;
    MFnMatrixData matrixData(data, &status);
    if (!status) return false;
    deformMatrix = matrixData.matrix(&status);
    if (!status) return false;

    // 描画と境界の両方に同じローカルのアフィン変換を適用する。
    deformMatrix[0][3] = deformMatrix[1][3] = deformMatrix[2][3] = 0.0;
    deformMatrix[3][3] = 1.0;
    return true;
}

MMatrix BdShpLDeformableCubeNode::shapeDrawMatrix(DrawMatrixCache* drawCache) const {
    const bool connected = matrixConnected_.load(std::memory_order_acquire);
    const auto revision = matrixRevision_.load(std::memory_order_acquire);
    const bool reuseConnected = connected && drawCache && MDGContext::current().isNormal();
    if (reuseConnected) {
        if (drawCache->revision == revision) return drawCache->matrix;
    } else if (!connected) {
        const std::lock_guard<std::mutex> lock(dataMutex_);
        if (cachedMatrixRevision_ == revision) return cachedMatrix_;
    }

    MMatrix deformMatrix;
    if (!readShapeMatrix(deformMatrix)) return MMatrix::identity;
    if (reuseConnected) {
        if (matrixRevision_.load(std::memory_order_acquire) == revision) {
            *drawCache = {deformMatrix, revision};
        }
    } else if (!connected) {
        const std::lock_guard<std::mutex> lock(dataMutex_);
        if (matrixRevision_.load(std::memory_order_acquire) == revision) {
            cachedMatrix_ = deformMatrix;
            cachedMatrixRevision_ = revision;
        }
    }
    return deformMatrix;
}
