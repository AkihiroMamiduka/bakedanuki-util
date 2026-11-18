#include "bdUtilNodes/nodes/BdShpLCubeNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#include <cmath>
#include <cstring>

#include <maya/MDistance.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnUnitAttribute.h>
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

namespace {
MVector axisVector(short axis) {
    switch (axis) {
        case 1: return MVector(-1, 0, 0);
        case 2: return MVector(0, 1, 0);
        case 3: return MVector(0, -1, 0);
        case 4: return MVector(0, 0, 1);
        case 5: return MVector(0, 0, -1);
        default: return MVector(1, 0, 0);
    }
}
}

BdShpLCubeNode::BdShpLCubeNode() {
    std::memcpy(geometry_.vertices, bdUtilNodes::fixedCube::vertices, sizeof(geometry_.vertices));
    geometry_.bounds = bdUtilNodes::fixedCube::bounds();
}

void* BdShpLCubeNode::creator() {
    return new BdShpLCubeNode;
}

MStatus BdShpLCubeNode::initialize() {
    MStatus status;
    MFnEnumAttribute enumFn;
    const char* axisNames[] = {"+X", "-X", "+Y", "-Y", "+Z", "-Z"};
    shape1stAxis = enumFn.create("shape1stAxis", "s1a", 0, &status);
    if (!status) return status;
    for (short i = 0; i < 6; ++i) {
        status = enumFn.addField(axisNames[i], i);
        if (!status) return status;
    }
    shape2ndAxis = enumFn.create("shape2ndAxis", "s2a", 2, &status);
    if (!status) return status;
    for (short i = 0; i < 6; ++i) {
        status = enumFn.addField(axisNames[i], i);
        if (!status) return status;
    }
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
    return MS::kSuccess;
}

bool BdShpLCubeNode::isShapeAttribute(const MObject& attribute) {
    return attribute == shape1stAxis || attribute == shape2ndAxis ||
        attribute == shapeBaseSpace1stAxisPlus || attribute == shapeBaseSpace1stAxisMinus ||
        attribute == shapeBaseSpace2ndAxisPlus || attribute == shapeBaseSpace2ndAxisMinus ||
        attribute == shapeBaseSpace3rdAxisPlus || attribute == shapeBaseSpace3rdAxisMinus;
}

bool BdShpLCubeNode::setInternalValue(const MPlug& plug, const MDataHandle& data) {
    if (isShapeAttribute(plug.attribute())) {
        geometryRevision_.fetch_add(1, std::memory_order_release);
        MHWRender::MRenderer::setGeometryDrawDirty(thisMObject(), false);
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

std::uint64_t BdShpLCubeNode::geometryRevision() const {
    return geometryRevision_.load(std::memory_order_acquire);
}

BdShpLCubeNode::Geometry BdShpLCubeNode::geometry() const {
    const std::lock_guard<std::mutex> lock(geometryMutex_);
    const auto revision = geometryRevision();
    if (geometry_.revision == revision) return geometry_;

    MStatus status;
    const auto object = thisMObject();
    const short first = MPlug(object, shape1stAxis).asShort(&status);
    if (!status) return geometry_;
    const short second = MPlug(object, shape2ndAxis).asShort(&status);
    if (!status) return geometry_;
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
            if (!status) return geometry_;
        }
    }
    const auto firstVector = axisVector(first);
    auto secondVector = axisVector(second);
    if ((firstVector ^ secondVector).length() == 0) {
        secondVector = std::abs(firstVector.y) == 1 ? MVector(0, 0, 1) : MVector(0, 1, 0);
    }
    const auto thirdVector = firstVector ^ secondVector;
    Geometry result;
    for (unsigned int i = 0; i < 8; ++i) {
        const auto& original = bdUtilNodes::fixedCube::vertices[i];
        const auto point = MPoint::origin + firstVector * limits[0][original[0] > 0] +
            secondVector * limits[1][original[1] > 0] + thirdVector * limits[2][original[2] > 0];
        result.bounds.expand(point);
        for (unsigned int axis = 0; axis < 3; ++axis) {
            result.vertices[i][axis] = static_cast<float>(point[axis]);
        }
    }
    result.revision = revision;
    geometry_ = result;
    return geometry_;
}

bool BdShpLCubeNode::isBounded() const {
    return true;
}

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
