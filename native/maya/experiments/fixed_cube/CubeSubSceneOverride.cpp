#include "CubeResearch.h"

#include <maya/M3dView.h>
#include <maya/MColor.h>
#include <maya/MDagPath.h>
#include <maya/MFnDagNode.h>
#include <maya/MFrameContext.h>
#include <maya/MHWGeometry.h>
#include <maya/MHWGeometryUtilities.h>
#include <maya/MMatrix.h>
#include <maya/MPxSubSceneOverride.h>
#include <maya/MSelectionMask.h>
#include <maya/MShaderManager.h>
#include <maya/MViewport2Renderer.h>

#include <cstring>
#include <memory>
#include <vector>

namespace {
using namespace MHWRender;

constexpr const char* itemName = "fixedCubeLines";

struct ColorShader {
    MColor color;
    MShaderInstance* shader = nullptr;
};

struct SharedResources {
    MRenderer* renderer = nullptr;
    const MShaderManager* manager = nullptr;
    DrawAPI api = kNone;
    std::unique_ptr<MVertexBuffer> vertices;
    std::unique_ptr<MIndexBuffer> indices;
    std::vector<ColorShader> shaders;
    MBoundingBox bounds = cubeResearch::bounds();

    ~SharedResources() {
        auto* current = MRenderer::theRenderer(false);
        if (current == renderer && current && current->getShaderManager() == manager) {
            for (const auto& entry : shaders) manager->releaseShader(entry.shader);
        }
    }

    bool initialize(MRenderer* value) {
        renderer = value;
        manager = renderer->getShaderManager();
        api = renderer->drawAPI();
        if (!manager) return false;
        const MVertexBufferDescriptor descriptor("", MGeometry::kPosition, MGeometry::kFloat, 3);
        vertices = std::make_unique<MVertexBuffer>(descriptor);
        indices = std::make_unique<MIndexBuffer>(MGeometry::kUnsignedInt32);
        auto* positions = vertices->acquire(8, true);
        if (!positions) return false;
        std::memcpy(positions, cubeResearch::vertices, sizeof(cubeResearch::vertices));
        vertices->commit(positions);
        auto* edges = indices->acquire(24, true);
        if (!edges) return false;
        std::memcpy(edges, cubeResearch::indices, sizeof(cubeResearch::indices));
        indices->commit(edges);
        return true;
    }

    MShaderInstance* shader(const MColor& color) {
        for (const auto& entry : shaders) {
            if (entry.color == color) return entry.shader;
        }
        auto* result = manager->getStockShader(MShaderManager::k3dSolidShader);
        if (!result) return nullptr;
        if (!result->setParameter("solidColor", &color.r)) {
            manager->releaseShader(result);
            return nullptr;
        }
        shaders.push_back({color, result});
        return result;
    }
};

// GPU resource は DLL の終了処理へ残さず、plug-in の unload 時に解放する。
std::vector<std::shared_ptr<SharedResources>>* resourceCache = nullptr;

std::shared_ptr<SharedResources> resourcesFor(MRenderer* renderer) {
    if (!renderer) return nullptr;
    if (!resourceCache) resourceCache = new std::vector<std::shared_ptr<SharedResources>>;
    for (const auto& value : *resourceCache) {
        if (value->renderer == renderer && value->manager == renderer->getShaderManager() &&
            value->api == renderer->drawAPI()) return value;
    }
    auto value = std::make_shared<SharedResources>();
    if (!value->initialize(renderer)) return nullptr;
    resourceCache->push_back(value);
    return value;
}

struct DrawState {
    MDagPath path;
    MMatrix matrix;
    MColor color;
    bool visible = false;
    bool selectable = false;
    bool hideOnPlayback = false;

    bool operator==(const DrawState& other) const {
        return path == other.path && matrix == other.matrix && color == other.color &&
            visible == other.visible && selectable == other.selectable &&
            hideOnPlayback == other.hideOnPlayback;
    }
};

class CubeSubSceneOverride final : public MPxSubSceneOverride {
public:
    explicit CubeSubSceneOverride(const MObject& object)
        : MPxSubSceneOverride(object), object_(object) {}

    DrawAPI supportedDrawAPIs() const override {
        return kOpenGL | kOpenGLCoreProfile | kDirectX11;
    }

    bool requiresUpdate(const MSubSceneContainer& container, const MFrameContext&) const override {
        pending_ = readState();
        auto* renderer = MRenderer::theRenderer();
        return !ready_ || !resources_ || resources_->renderer != renderer ||
            (renderer && (resources_->manager != renderer->getShaderManager() ||
                resources_->api != renderer->drawAPI())) ||
            container.count() != 1 || !(pending_ == current_);
    }

    void update(MSubSceneContainer& container, const MFrameContext&) override {
        auto* renderer = MRenderer::theRenderer();
        const bool resourcesChanged = !resources_ || resources_->renderer != renderer ||
            (renderer && (resources_->manager != renderer->getShaderManager() ||
                resources_->api != renderer->drawAPI()));
        if (resourcesChanged) {
            container.clear();
            resources_ = resourcesFor(renderer);
            ready_ = false;
        }
        if (!resources_) return;

        auto* item = container.find(itemName);
        const bool created = item == nullptr;
        if (created) {
            item = MRenderItem::Create(itemName, MRenderItem::NonMaterialSceneItem, MGeometry::kLines);
            if (!item) return;
            item->setDrawMode(MGeometry::kAll);
            item->setWantConsolidation(true);
            item->castsShadows(false);
            item->receivesShadows(false);
            item->setExcludedFromPostEffects(true);
            item->setExcludedFromDefaultMaterialOverride(true);
            item->setObjectTypeExclusionFlag(MFrameContext::kExcludePluginShapes);
            item->depthPriority(MRenderItem::sDormantWireDepthPriority);
            if (!container.add(item)) {
                MRenderItem::Destroy(item);
                return;
            }
        }

        const auto fail = [&]() {
            item->enable(false);
            ready_ = false;
        };
        if (created || !ready_ || pending_.color != current_.color) {
            auto* shader = resources_->shader(pending_.color);
            if (!shader || !item->setShader(shader)) {
                fail();
                return;
            }
        }
        if (created || !ready_) {
            MVertexBufferArray buffers;
            buffers.addBuffer("positions", resources_->vertices.get());
            if (!setGeometryForRenderItem(*item, buffers, *resources_->indices, &resources_->bounds)) {
                fail();
                return;
            }
        }
        // 親階層を含む行列を明示し、静止時の再設定と geometry upload を省く。
        if ((created || !ready_ || pending_.matrix != current_.matrix) &&
            !item->setMatrix(&pending_.matrix)) {
            fail();
            return;
        }
        if (created || !ready_ || pending_.selectable != current_.selectable) {
            item->setSelectionMask(pending_.selectable
                ? MSelectionMask(MSelectionMask::kSelectLocators) : MSelectionMask());
        }
        if (created || !ready_ || pending_.hideOnPlayback != current_.hideOnPlayback) {
            item->setHideOnPlayback(pending_.hideOnPlayback);
        }
        if (item->isEnabled() != pending_.visible) item->enable(pending_.visible);
        current_ = pending_;
        ready_ = true;
    }

    bool getSelectionPath(const MRenderItem&, MDagPath& path) const override {
        path = current_.selectable ? current_.path : MDagPath();
        return true;
    }

private:
    DrawState readState() const {
        DrawState state;
        MStatus status;
        MFnDagNode node(object_, &status);
        if (!status || !node.getPath(state.path) || !state.path.isValid()) return state;
        state.matrix = state.path.inclusiveMatrix(&status);
        if (!status) return state;
        state.visible = state.path.isVisible(&status) && status && !node.isIntermediateObject();
        const auto overrides = state.path.getDrawOverrideInfo();
        const auto type = state.path.isTemplated() ? MDAGDrawOverrideInfo::kDisplayTypeTemplate
            : (overrides.fOverrideEnabled ? overrides.fDisplayType : MDAGDrawOverrideInfo::kDisplayTypeNormal);
        if (overrides.fOverrideEnabled) state.visible = state.visible && overrides.fEnableVisible;
        state.hideOnPlayback = overrides.fOverrideEnabled && !overrides.fPlaybackVisible;
        state.selectable = state.visible && type == MDAGDrawOverrideInfo::kDisplayTypeNormal;
        state.color = MGeometryUtilities::wireframeColor(state.path);
        if (type == MDAGDrawOverrideInfo::kDisplayTypeTemplate) {
            state.color = M3dView::templateColor();
        } else if (type == MDAGDrawOverrideInfo::kDisplayTypeReference) {
            state.color = M3dView::referenceLayerColor();
        }
        state.color.a = 1.0f;
        return state;
    }

    MObject object_;
    std::shared_ptr<SharedResources> resources_;
    DrawState current_;
    mutable DrawState pending_;
    bool ready_ = false;
};
}

MHWRender::MPxSubSceneOverride* createCubeSubSceneOverride(const MObject& object) {
    return new CubeSubSceneOverride(object);
}

void cleanupCubeSubSceneResources() {
    delete resourceCache;
    resourceCache = nullptr;
}
