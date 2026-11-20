#include "CubeResearch.h"
#include "bdUtilNodes/nodes/BdShpLCubeNode.h"

#include <maya/M3dView.h>
#include <maya/MColor.h>
#include <maya/MDagPath.h>
#include <maya/MFnDagNode.h>
#include <maya/MFrameContext.h>
#include <maya/MHWGeometry.h>
#include <maya/MHWGeometryUtilities.h>
#include <maya/MPointArray.h>
#include <maya/MPxDrawOverride.h>
#include <maya/MUIDrawManager.h>
#include <maya/MUintArray.h>
#include <maya/MUserData.h>
#include <maya/MViewport2Renderer.h>

namespace {
using namespace MHWRender;

struct CubeDrawData final : MUserData {
    MPointArray points;
    MColor color;
    std::uint64_t revision = 0;
    bool visible = false;
    bool selectable = false;
};

class CubeDrawOverride final : public MPxDrawOverride {
public:
    explicit CubeDrawOverride(const MObject& object)
        : MPxDrawOverride(object, nullptr, false),
          node_(static_cast<BdShpLCubeNode*>(MFnDagNode(object).userNode())) {}

    DrawAPI supportedDrawAPIs() const override { return kAllDevices; }
    bool hasUIDrawables() const override { return true; }
    bool isBounded(const MDagPath&, const MDagPath&) const override { return true; }

    MBoundingBox boundingBox(const MDagPath&, const MDagPath&) const override {
        return node_ ? baseGeometry().bounds : cubeResearch::bounds();
    }

#ifdef BD_CUBE_RESEARCH_SHAPE_MATRIX
    MMatrix transform(const MDagPath& objPath, const MDagPath&) const override {
        const auto world = objPath.inclusiveMatrix();
        return node_ ? node_->shapeDrawMatrix() * world : world;
    }
#endif

    MUserData* prepareForDraw(
        const MDagPath& objPath, const MDagPath&, const MFrameContext&, MUserData* oldData
    ) override {
        auto* data = static_cast<CubeDrawData*>(oldData);
        if (!data) data = new CubeDrawData();
        data->visible = false;
        if (!node_) return data;

        const auto overrides = objPath.getDrawOverrideInfo();
        const auto status = MGeometryUtilities::displayStatus(objPath);
        data->visible = objPath.isVisible() && status != kInvisible &&
            status != kIntermediateObject && (!overrides.fOverrideEnabled || overrides.fEnableVisible);
        if (!data->visible) return data;

        const bool templated = objPath.isTemplated() || status == kTemplate || status == kActiveTemplate;
        const auto type = templated ? MDAGDrawOverrideInfo::kDisplayTypeTemplate
            : (overrides.fOverrideEnabled ? overrides.fDisplayType : MDAGDrawOverrideInfo::kDisplayTypeNormal);
        data->selectable = type == MDAGDrawOverrideInfo::kDisplayTypeNormal;
        if (type == MDAGDrawOverrideInfo::kDisplayTypeTemplate) {
            data->color = M3dView::templateColor();
        } else if (type == MDAGDrawOverrideInfo::kDisplayTypeReference) {
            data->color = M3dView::referenceLayerColor();
        } else {
            data->color = MGeometryUtilities::wireframeColor(objPath);
        }
        data->color.a = 1.0f;

        if (data->points.length() == 0 || data->revision != node_->geometryRevision()) {
            const auto geometry = baseGeometry();
            data->points.setLength(8);
            for (unsigned int i = 0; i < 8; ++i) {
                const auto& point = geometry.vertices[i];
                data->points[i] = MPoint(point[0], point[1], point[2]);
            }
            data->revision = geometry.revision;
        }
        return data;
    }

    void addUIDrawables(
        const MDagPath&, MUIDrawManager& drawManager, const MFrameContext& frameContext,
        const MUserData* userData
    ) override {
        const auto* data = static_cast<const CubeDrawData*>(userData);
        if (!data || !data->visible ||
            (frameContext.objectTypeExclusions() & MFrameContext::kExcludePluginShapes)) return;

        static const MUintArray lineIndices(cubeResearch::indices, 24);
        drawManager.beginDrawable(data->selectable ? MUIDrawManager::kSelectable : MUIDrawManager::kNonSelectable);
        drawManager.setColor(data->color);
        drawManager.setDepthPriority(MRenderItem::sDormantWireDepthPriority);
        drawManager.mesh(MUIDrawManager::kLines, data->points, nullptr, nullptr, &lineIndices);
        drawManager.endDrawable();
    }

private:
    BdShpLCubeNode::Geometry baseGeometry() const {
#ifndef BD_CUBE_RESEARCH_SHAPE_MATRIX
        return node_->geometry();
#else
        return node_->baseDrawGeometry();
#endif
    }

    BdShpLCubeNode* node_;
};
}

MHWRender::MPxDrawOverride* createCubeDrawOverride(const MObject& object) {
    return new CubeDrawOverride(object);
}
