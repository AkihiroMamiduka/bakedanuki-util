#include "bdUtilNodes/nodes/BdShpLDeformableCubeNode.h"
#include "bdUtilNodes/nodes/FixedCubeShape.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <cstring>

#include <maya/MCacheSchema.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MEvaluationNode.h>
#include <maya/MFnMatrixData.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MNodeCacheSetupInfo.h>
#include <maya/MPlug.h>
#include <maya/MViewport2Renderer.h>

namespace {
bool readAffineMatrix(const MObject& object, MMatrix& matrix) {
    MStatus status;
    MFnMatrixData matrixData(object, &status);
    if (!status) return false;
    matrix = matrixData.matrix(&status);
    if (!status) return false;

    // 描画と境界の両方に同じローカルのアフィン変換を適用する。
    matrix[0][3] = matrix[1][3] = matrix[2][3] = 0.0;
    matrix[3][3] = 1.0;
    return true;
}
}

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
    shapeAttributes_.lockSeparators(thisMObject());
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
    const auto geometry = baseDrawGeometry();
    return bdUtilNodes::fixedCube::transformedBounds(geometry, shapeDrawMatrix());
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
    std::uint64_t pendingRevision = 0;
    std::uint64_t directRevision = 0;
    if (matrixConnected_.load(std::memory_order_acquire) && context.isNormal()) {
        MStatus status;
        const bool dirty = evaluationNode.dirtyPlugExists(shapeDeformMatrix, &status);
        if (dirty || !status || evalType == kLeaveDirty) {
            const auto previous = matrixRevision_.fetch_add(1, std::memory_order_release);
            if (dirty && status && evalType == kEvaluatedIndirectly && evaluationMatrixCache_.hasPending(previous)
                && MDGContext::current().isNormal()) {
                pendingRevision = previous;
            } else {
                evaluationMatrixCache_.discard(previous);
                if (dirty && status && evalType == kEvaluatedDirectly && MDGContext::current().isNormal()) {
                    directRevision = previous + 1;
                }
            }
        } else {
            evaluationMatrixCache_.discard(shapeMatrixRevision());
        }
    }

    const auto result = MPxLocatorNode::postEvaluation(context, evaluationNode, evalType);
    if (pendingRevision != 0 && (!result || !evaluationMatrixCache_.publishPending(pendingRevision, matrixRevision_))) {
        evaluationMatrixCache_.discard(pendingRevision);
    }
    if (result && directRevision != 0 && matrixConnected_.load(std::memory_order_acquire)
        && MDGContext::current().isNormal() && shapeMatrixRevision() == directRevision) {
        const EvaluationMatrixCache::ReadScope read(evaluationMatrixCache_, true, true);
        if (read.active()) {
            // 評価済みの入力だけを取得し、読み取り中に時刻や世代が変わった値は使わない。
            const auto time = MAnimControl::currentTime();
            MStatus status;
            auto block = forceCache();
            if (block.isClean(shapeDeformMatrix, &status) && status) {
                auto data = block.inputValue(shapeDeformMatrix, &status);
                MMatrix deformMatrix;
                const bool valid = status && readAffineMatrix(data.data(), deformMatrix);
                if (shapeMatrixRevision() == directRevision && MAnimControl::currentTime() == time
                    && MDGContext::current().isNormal() && valid) {
                    evaluationMatrixCache_.publishDirect(deformMatrix, time, directRevision, matrixRevision_);
                }
            }
        }
    }
    return result;
}

bool BdShpLDeformableCubeNode::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    const auto attribute = plug.attribute();
    if (attribute == shapeDeformMatrix) {
        const auto revision = matrixRevision_.fetch_add(1, std::memory_order_release) + 1;
        // 描画自身のプラグ取得で呼ばれた場合は、評価側の候補として保留しない。
        if (matrixConnected_.load(std::memory_order_acquire) && !evaluationMatrixCache_.readActive()
            && MDGContext::current().isNormal()) {
            evaluationMatrixCache_.stage(data, revision, matrixRevision_);
        }
        MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), false);
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
        MPoint finPositions[bdUtilNodes::fixedCube::finVertexCount];
        bool guideLine, fin, preciseBodyBounds;
        if (shapeAttributes_.readPositions(thisMObject(), positions, guideLine, finPositions, fin, &preciseBodyBounds)) {
            baseGeometry_ = bdUtilNodes::fixedCube::geometryFromPositions(
                positions, revision, guideLine, fin ? finPositions : nullptr, preciseBodyBounds);
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
    return status && readAffineMatrix(data, deformMatrix);
}

bool BdShpLDeformableCubeNode::tryPublishedShapeMatrix(
    std::uint64_t revision, MMatrix& local, MTime& time
) const {
    if (!matrixConnected_.load(std::memory_order_acquire)) return false;
    const auto value = evaluationMatrixCache_.lookup(revision, matrixRevision_);
    if (!value) return false;
    local = value->matrix;
    time = value->time;
    return true;
}

MMatrix BdShpLDeformableCubeNode::shapeDrawMatrix(
    DrawMatrixCache* drawCache, std::uint64_t* connectedReadRevision,
    std::optional<MTime>* publicationTime
) const {
    if (connectedReadRevision) *connectedReadRevision = 0;
    if (publicationTime) publicationTime->reset();
    const bool connected = matrixConnected_.load(std::memory_order_acquire);
    const auto revision = matrixRevision_.load(std::memory_order_acquire);
    const bool reuseConnected = connected && drawCache && MDGContext::current().isNormal();
    if (reuseConnected) {
        if (drawCache->revision == revision && drawCache->validAtCurrentTime()) return drawCache->matrix;
        if (connectedReadRevision) {
            if (const auto published = evaluationMatrixCache_.lookup(revision, matrixRevision_)) {
                *connectedReadRevision = revision;
                if (publicationTime) *publicationTime = published->time;
                return published->matrix;
            }
        }
    } else if (!connected) {
        const std::lock_guard<std::mutex> lock(dataMutex_);
        if (cachedMatrixRevision_ == revision) {
            if (drawCache) {
                drawCache->revision = revision;
                drawCache->publicationTime.reset();
            }
            return cachedMatrix_;
        }
    }

    MMatrix deformMatrix;
    {
        const EvaluationMatrixCache::ReadScope read(evaluationMatrixCache_, connected);
        if (!readShapeMatrix(deformMatrix)) return MMatrix::identity;
    }
    if (reuseConnected) {
        const auto revisionAfterRead = matrixRevision_.load(std::memory_order_acquire);
        if (connectedReadRevision) *connectedReadRevision = revisionAfterRead;
        if (revisionAfterRead == revision) {
            *drawCache = {deformMatrix, revision, std::nullopt};
        }
    } else if (!connected) {
        const std::lock_guard<std::mutex> lock(dataMutex_);
        if (matrixRevision_.load(std::memory_order_acquire) == revision) {
            cachedMatrix_ = deformMatrix;
            cachedMatrixRevision_ = revision;
            if (drawCache) {
                drawCache->revision = revision;
                drawCache->publicationTime.reset();
            }
        }
    }
    return deformMatrix;
}

BdShpLDeformableCubeNode::EvaluationMatrixCache::ReadScope::ReadScope(
    EvaluationMatrixCache& cache, bool track, bool exclusive
) : cache_(cache), active_(track) {
    if (!active_) return;
    if (exclusive) {
        unsigned expected = 0;
        active_ = cache_.activeReads_.compare_exchange_strong(expected, 1, std::memory_order_acq_rel);
    } else {
        cache_.activeReads_.fetch_add(1, std::memory_order_acq_rel);
    }
}

BdShpLDeformableCubeNode::EvaluationMatrixCache::ReadScope::~ReadScope() {
    if (active_) cache_.activeReads_.fetch_sub(1, std::memory_order_acq_rel);
}

bool BdShpLDeformableCubeNode::EvaluationMatrixCache::readActive() const {
    return activeReads_.load(std::memory_order_acquire) != 0;
}

bool BdShpLDeformableCubeNode::EvaluationMatrixCache::hasPending(std::uint64_t revision) const {
    return revision != 0 && pendingRevision_.load(std::memory_order_acquire) == revision;
}

void BdShpLDeformableCubeNode::EvaluationMatrixCache::stage(
    MDataHandle data, std::uint64_t revision, const Revision& current
) {
    const auto time = MAnimControl::currentTime();
    MMatrix deformMatrix;
    if (!readAffineMatrix(data.data(), deformMatrix)) return;
    // 評価のコールバックでは、同じノードを参照する描画のロックを待たない。
    const std::unique_lock<std::mutex> lock(mutex_, std::try_to_lock);
    if (!lock || revision == 0 || current.load(std::memory_order_acquire) != revision || readActive()) return;
    pending_.matrix = deformMatrix;
    pending_.time = time;
    pendingRevision_.store(revision, std::memory_order_release);
}

void BdShpLDeformableCubeNode::EvaluationMatrixCache::discard(std::uint64_t revision) {
    pendingRevision_.compare_exchange_strong(revision, 0, std::memory_order_acq_rel);
}

bool BdShpLDeformableCubeNode::EvaluationMatrixCache::publishPending(std::uint64_t previous, const Revision& current) {
    const auto time = MAnimControl::currentTime();
    const std::unique_lock<std::mutex> lock(mutex_, std::try_to_lock);
    if (!lock) return false;
    const auto revision = previous + 1;
    if (!pendingRevision_.compare_exchange_strong(previous, 0, std::memory_order_acq_rel)) return false;
    if (revision == 0 || current.load(std::memory_order_acquire) != revision || time != pending_.time) return false;
    published_ = {pending_.matrix, time};
    publishedRevision_.store(revision, std::memory_order_release);
    return true;
}

void BdShpLDeformableCubeNode::EvaluationMatrixCache::publishDirect(
    const MMatrix& deformMatrix, const MTime& time, std::uint64_t revision, const Revision& current
) {
    const std::unique_lock<std::mutex> lock(mutex_, std::try_to_lock);
    if (!lock || revision == 0 || current.load(std::memory_order_acquire) != revision) return;
    published_ = {deformMatrix, time};
    publishedRevision_.store(revision, std::memory_order_release);
}

std::optional<BdShpLDeformableCubeNode::EvaluationMatrixCache::Value>
BdShpLDeformableCubeNode::EvaluationMatrixCache::lookup(std::uint64_t revision, const Revision& current) const {
    if (revision == 0 || publishedRevision_.load(std::memory_order_acquire) != revision) return {};
    const auto time = MAnimControl::currentTime();
    const std::lock_guard<std::mutex> lock(mutex_);
    if (publishedRevision_.load(std::memory_order_relaxed) != revision
        || current.load(std::memory_order_acquire) != revision || time != published_.time) return {};
    return published_;
}
