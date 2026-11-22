#include "bdUtilNodes/nodes/BdShpLCubeNode.h"
#include "bdUtilNodes/nodes/BdShpLDeformableCubeNode.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif
#include <type_traits>

#include <maya/MDrawRegistry.h>
#include <maya/MFnPlugin.h>

#ifdef BD_CUBE_RESEARCH_DUMMY_BOOL_COUNT
#include <string>

#include <maya/MFnNumericAttribute.h>
#endif

namespace {
using MHWRender::MDrawRegistry;

#ifdef BD_CUBE_RESEARCH_DUMMY_BOOL_COUNT
template <typename Node>
MStatus initializeCubeWithDummyBools() {
    auto status = Node::initialize();
    if (!status) return status;

    // 比較用の属性は型の初期化時だけ登録する。
    MFnNumericAttribute numeric;
    for (int index = 0; index < BD_CUBE_RESEARCH_DUMMY_BOOL_COUNT; ++index) {
        const auto suffix = std::to_string(index + 1);
        const auto longName = "researchDummyBool" + suffix;
        const auto shortName = "rdb" + suffix;
        const auto attribute = numeric.create(longName.c_str(), shortName.c_str(), MFnNumericData::kBoolean, false, &status);
        if (!status) return status;
        status = numeric.setKeyable(false);
        if (!status) return status;
        status = numeric.setChannelBox(false);
        if (!status) return status;
        status = numeric.setConnectable(false);
        if (!status) return status;
        status = MPxNode::addAttribute(attribute);
        if (!status) return status;
    }
    return MS::kSuccess;
}
#endif

template <typename Node>
MStatus registerDrawOverride() {
    if constexpr (std::is_same_v<Node, BdShpLCubeNode>) {
        return MDrawRegistry::registerGeometryOverrideCreator(
            Node::drawClassification, Node::drawRegistrantId, Node::createGeometryOverride);
    } else {
        return MDrawRegistry::registerSubSceneOverrideCreator(
            Node::drawClassification, Node::drawRegistrantId, Node::createSubSceneOverride);
    }
}

template <typename Node>
MStatus deregisterDrawOverride() {
    if constexpr (std::is_same_v<Node, BdShpLCubeNode>) {
        return MDrawRegistry::deregisterGeometryOverrideCreator(Node::drawClassification, Node::drawRegistrantId);
    } else {
        return MDrawRegistry::deregisterSubSceneOverrideCreator(Node::drawClassification, Node::drawRegistrantId);
    }
}

template <typename Node>
MStatus registerCube(MFnPlugin& plugin) {
#ifdef BD_CUBE_RESEARCH_DUMMY_BOOL_COUNT
    const auto initialize = initializeCubeWithDummyBools<Node>;
#else
    const auto initialize = Node::initialize;
#endif
    auto status = plugin.registerNode(Node::typeName, Node::typeId, Node::creator,
        initialize, MPxNode::kLocatorNode, &Node::drawClassification);
    if (!status) return status;
    status = registerDrawOverride<Node>();
    if (!status) plugin.deregisterNode(Node::typeId);
    return status;
}

template <typename Node>
MStatus deregisterCube(MFnPlugin& plugin) {
    auto status = deregisterDrawOverride<Node>();
    if (!status) return status;
    status = plugin.deregisterNode(Node::typeId);
    if (!status) registerDrawOverride<Node>();
    return status;
}
}

MStatus initializePlugin(MObject object) {
    MStatus status;
    MFnPlugin plugin(object, "bakedanuki", "0.1.0-research", "Any", &status);
    if (!status) return status;
    status = registerCube<BdShpLCubeNode>(plugin);
    if (!status) return status;
    status = registerCube<BdShpLDeformableCubeNode>(plugin);
    if (!status) {
        deregisterCube<BdShpLCubeNode>(plugin);
        return status;
    }
#ifdef BD_CUBE_PROFILE
    status = plugin.registerCommand("bdCubeProfile", cubeResearch::profiling::Command::creator,
        cubeResearch::profiling::Command::syntaxCreator);
    if (!status) {
        deregisterCube<BdShpLDeformableCubeNode>(plugin);
        deregisterCube<BdShpLCubeNode>(plugin);
    }
#endif
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
    if (status) BdShpLDeformableCubeNode::startDisplayStateMonitoring();
#endif
    return status;
}

MStatus uninitializePlugin(MObject object) {
    MFnPlugin plugin(object);
    auto status = deregisterCube<BdShpLDeformableCubeNode>(plugin);
    if (!status) return status;
    status = deregisterCube<BdShpLCubeNode>(plugin);
    if (!status) {
        registerCube<BdShpLDeformableCubeNode>(plugin);
        return status;
    }
#ifdef BD_CUBE_PROFILE
    status = plugin.deregisterCommand("bdCubeProfile");
    if (!status) {
        registerCube<BdShpLCubeNode>(plugin);
        registerCube<BdShpLDeformableCubeNode>(plugin);
        return status;
    }
#endif
    BdShpLCubeNode::cleanupDrawResources();
    BdShpLDeformableCubeNode::cleanupDrawResources();
    return MS::kSuccess;
}
