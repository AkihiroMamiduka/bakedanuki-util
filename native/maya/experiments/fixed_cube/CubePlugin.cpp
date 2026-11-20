#include "bdUtilNodes/nodes/BdShpLCubeNode.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <maya/MDrawRegistry.h>
#include <maya/MFnPlugin.h>
#include <maya/MPxDrawOverride.h>
#include <maya/MPxGeometryOverride.h>
#include <maya/MPxSubSceneOverride.h>

MHWRender::MPxDrawOverride* createCubeDrawOverride(const MObject&);
MHWRender::MPxSubSceneOverride* createCubeSubSceneOverride(const MObject&);
void cleanupCubeSubSceneResources();

namespace {
const MTypeId& typeId = BdShpLCubeNode::typeId;
#ifdef BD_CUBE_SUBSCENE
const MString classification("drawdb/subscene/bdShpL_Cube");
#else
const MString& classification = BdShpLCubeNode::drawClassification;
#endif
const MString registrant("bdShpL_CubeResearch");

}

MStatus initializePlugin(MObject object) {
    MStatus status;
    MFnPlugin plugin(object, "bakedanuki", "0.1.0-research", "Any", &status);
    if (!status) return status;
    status = plugin.registerNode(BdShpLCubeNode::typeName, typeId, BdShpLCubeNode::creator,
        BdShpLCubeNode::initialize, MPxNode::kLocatorNode, &classification);
    if (!status) return status;
#ifdef BD_CUBE_SUBSCENE
    status = MHWRender::MDrawRegistry::registerSubSceneOverrideCreator(
        classification, registrant, createCubeSubSceneOverride);
#elif defined(BD_CUBE_DRAW_OVERRIDE)
    status = MHWRender::MDrawRegistry::registerDrawOverrideCreator(
        classification, registrant, createCubeDrawOverride);
#else
    status = MHWRender::MDrawRegistry::registerGeometryOverrideCreator(
        classification, registrant, BdShpLCubeNode::createGeometryOverride);
#endif
    if (!status) plugin.deregisterNode(typeId);
#ifdef BD_CUBE_PROFILE
    if (status) {
        status = plugin.registerCommand("bdCubeProfile",
            cubeResearch::profiling::Command::creator, cubeResearch::profiling::Command::syntaxCreator);
        if (!status) {
#ifdef BD_CUBE_SUBSCENE
            MHWRender::MDrawRegistry::deregisterSubSceneOverrideCreator(classification, registrant);
#elif defined(BD_CUBE_DRAW_OVERRIDE)
            MHWRender::MDrawRegistry::deregisterDrawOverrideCreator(classification, registrant);
#else
            MHWRender::MDrawRegistry::deregisterGeometryOverrideCreator(classification, registrant);
#endif
            plugin.deregisterNode(typeId);
        }
    }
#endif
    return status;
}

MStatus uninitializePlugin(MObject object) {
    MFnPlugin plugin(object);
#ifdef BD_CUBE_SUBSCENE
    MStatus status = MHWRender::MDrawRegistry::deregisterSubSceneOverrideCreator(
        classification, registrant);
#elif defined(BD_CUBE_DRAW_OVERRIDE)
    MStatus status = MHWRender::MDrawRegistry::deregisterDrawOverrideCreator(classification, registrant);
#else
    MStatus status = MHWRender::MDrawRegistry::deregisterGeometryOverrideCreator(
        classification, registrant);
#endif
    if (!status) return status;
    status = plugin.deregisterNode(typeId);
    if (!status) {
#ifdef BD_CUBE_SUBSCENE
        MHWRender::MDrawRegistry::registerSubSceneOverrideCreator(
            classification, registrant, createCubeSubSceneOverride);
#elif defined(BD_CUBE_DRAW_OVERRIDE)
        MHWRender::MDrawRegistry::registerDrawOverrideCreator(classification, registrant, createCubeDrawOverride);
#else
        MHWRender::MDrawRegistry::registerGeometryOverrideCreator(
            classification, registrant, BdShpLCubeNode::createGeometryOverride);
#endif
        return status;
    }
#ifdef BD_CUBE_SUBSCENE
    cleanupCubeSubSceneResources();
#elif !defined(BD_CUBE_DRAW_OVERRIDE)
    BdShpLCubeNode::cleanupDrawResources();
#endif
#ifdef BD_CUBE_PROFILE
    status = plugin.deregisterCommand("bdCubeProfile");
#endif
    return MS::kSuccess;
}
