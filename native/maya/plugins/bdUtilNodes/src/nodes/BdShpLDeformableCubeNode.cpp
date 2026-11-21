#include "bdUtilNodes/nodes/BdShpLDeformableCubeNode.h"
#include "bdUtilNodes/nodes/FixedCubeShape.h"
#include "bdUtilNodes/nodes/LocatorChannelBox.h"

#include <cstring>

#include <maya/MCacheSchema.h>
#include <maya/MFnMatrixData.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MNodeCacheSetupInfo.h>
#include <maya/MPlug.h>
#include <maya/MViewport2Renderer.h>

const MString BdShpLDeformableCubeNode::typeName("bdShpL_DeformableCube");
const MTypeId BdShpLDeformableCubeNode::typeId(0x00142723);
const MString BdShpLDeformableCubeNode::drawClassification("drawdb/subscene/bdShpL_DeformableCube");
const MString BdShpLDeformableCubeNode::drawRegistrantId("bdShpLDeformableCubeSubSceneOverride");

bdUtilNodes::fixedCube::ShapeAttributes BdShpLDeformableCubeNode::shapeAttributes_;
MObject BdShpLDeformableCubeNode::shapeDeformMatrix;

BdShpLDeformableCubeNode::BdShpLDeformableCubeNode() {
    std::memcpy(baseGeometry_.vertices, bdUtilNodes::fixedCube::vertices, sizeof(baseGeometry_.vertices));
    baseGeometry_.bounds = bdUtilNodes::fixedCube::bounds();
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
    auto bounds = baseDrawGeometry().bounds;
    const auto deformMatrix = shapeDrawMatrix();
    // 基準形状の頂点は軸平行な境界の8隅にある。
    if (deformMatrix != MMatrix::identity) bounds.transformUsing(deformMatrix);
    return bounds;
}

bool BdShpLDeformableCubeNode::excludeAsLocator() const {
    return false;
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
    const std::lock_guard<std::mutex> lock(dataMutex_);
    const auto revision = geometryRevision();
    if (baseGeometry_.revision != revision) {
        MPoint positions[8];
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

MMatrix BdShpLDeformableCubeNode::shapeDrawMatrix() const {
    const bool connected = matrixConnected_.load(std::memory_order_acquire);
    const auto revision = matrixRevision_.load(std::memory_order_acquire);
    if (!connected) {
        const std::lock_guard<std::mutex> lock(dataMutex_);
        if (cachedMatrixRevision_ == revision) return cachedMatrix_;
    }

    MMatrix deformMatrix;
    if (!readShapeMatrix(deformMatrix)) return MMatrix::identity;
    if (!connected) {
        const std::lock_guard<std::mutex> lock(dataMutex_);
        if (matrixRevision_.load(std::memory_order_acquire) == revision) {
            cachedMatrix_ = deformMatrix;
            cachedMatrixRevision_ = revision;
        }
    }
    return deformMatrix;
}
