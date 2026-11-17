#include "bdUtilNodes/nodes/BdShpLCubeNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

const MString BdShpLCubeNode::typeName("bdShpL_Cube");
const MTypeId BdShpLCubeNode::typeId(0x00142720);
const MString BdShpLCubeNode::drawClassification("drawdb/geometry/bdShpL_Cube");
const MString BdShpLCubeNode::drawRegistrantId("bdShpLCubeGeometryOverride");

void* BdShpLCubeNode::creator() {
    return new BdShpLCubeNode;
}

MStatus BdShpLCubeNode::initialize() {
    return MS::kSuccess;
}

bool BdShpLCubeNode::isBounded() const {
    return true;
}

MBoundingBox BdShpLCubeNode::boundingBox() const {
#ifdef BD_CUBE_PROFILE
    cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::bounds);
#endif
    return bdUtilNodes::fixedCube::bounds();
}

bool BdShpLCubeNode::excludeAsLocator() const {
    return false;
}

#ifdef BD_CUBE_NODE_PARALLEL
MPxNode::SchedulingType BdShpLCubeNode::schedulingType() const {
    return MPxNode::kParallel;
}
#endif
