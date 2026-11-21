#include "bdUtilNodes/nodes/BdShpLDeformableCubeNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#include <cstring>
#include <memory>
#include <vector>

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

namespace {
using namespace MHWRender;
namespace cube = bdUtilNodes::fixedCube;

const MString& itemName() {
    static const MString name("bdDeformableCubeLines");
    return name;
}

std::unique_ptr<MVertexBuffer> vertexBuffer(const float (&vertices)[8][3]) {
    const MVertexBufferDescriptor descriptor("", MGeometry::kPosition, MGeometry::kFloat, 3);
    auto buffer = std::make_unique<MVertexBuffer>(descriptor);
    auto* positions = buffer->acquire(8, true);
    if (!positions) return nullptr;
    std::memcpy(positions, vertices, sizeof(vertices));
    buffer->commit(positions);
    return buffer;
}

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

    ~SharedResources() {
        if (!shaders.empty() && matches(MRenderer::theRenderer(false))) {
            for (const auto& entry : shaders) manager->releaseShader(entry.shader);
        }
    }

    bool matches(MRenderer* value) const {
        return value && renderer == value && manager == value->getShaderManager() &&
            api == value->drawAPI();
    }

    bool initialize(MRenderer* value) {
        renderer = value;
        manager = renderer->getShaderManager();
        api = renderer->drawAPI();
        if (!manager) return false;
        vertices = vertexBuffer(cube::vertices);
        if (!vertices) return false;
        indices = std::make_unique<MIndexBuffer>(MGeometry::kUnsignedInt32);
        auto* edges = indices->acquire(24, true);
        if (!edges) return false;
        std::memcpy(edges, cube::indices, sizeof(cube::indices));
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

// GPU resource は plug-in の unload 時に明示的に解放する。
std::vector<std::shared_ptr<SharedResources>>* resourceCache = nullptr;

std::shared_ptr<SharedResources> resourcesFor(MRenderer* renderer) {
    if (!renderer) return nullptr;
    if (!resourceCache) resourceCache = new std::vector<std::shared_ptr<SharedResources>>;
    for (const auto& value : *resourceCache) {
        if (value->matches(renderer)) return value;
    }
    auto value = std::make_shared<SharedResources>();
    if (!value->initialize(renderer)) return nullptr;
    resourceCache->push_back(value);
    return value;
}

MRenderItem* createItem(MSubSceneContainer& container) {
    auto* item = MRenderItem::Create(itemName(), MRenderItem::NonMaterialSceneItem, MGeometry::kLines);
    if (!item) return nullptr;
    item->setDrawMode(MGeometry::kAll);
    item->setWantConsolidation(true);
    item->castsShadows(false);
    item->receivesShadows(false);
    item->setExcludedFromPostEffects(true);
    item->setExcludedFromDefaultMaterialOverride(true);
    item->setObjectTypeExclusionFlag(MFrameContext::kExcludePluginShapes);
    item->depthPriority(MRenderItem::sDormantWireDepthPriority);
    if (container.add(item)) return item;
    MRenderItem::Destroy(item);
    return nullptr;
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

class DeformableCubeSubSceneOverride final : public MPxSubSceneOverride {
public:
    explicit DeformableCubeSubSceneOverride(const MObject& object)
        : MPxSubSceneOverride(object), object_(object),
          node_(static_cast<BdShpLDeformableCubeNode*>(MFnDagNode(object).userNode())) {}

    DrawAPI supportedDrawAPIs() const override {
        return kOpenGL | kOpenGLCoreProfile | kDirectX11;
    }

    bool requiresUpdate(const MSubSceneContainer& container, const MFrameContext&) const override {
        if (!node_) return false;
        pending_ = readState();
        return !ready_ || !resources_ || !resources_->matches(MRenderer::theRenderer()) ||
            container.count() != 1 || !(pending_ == current_) ||
            node_->geometryRevision() != geometry_.revision;
    }

    void update(MSubSceneContainer& container, const MFrameContext&) override {
        if (!node_) return;
        auto* renderer = MRenderer::theRenderer();
        if (!resources_ || !resources_->matches(renderer)) {
            container.clear();
            ownedVertices_.reset();
            resources_ = resourcesFor(renderer);
            ready_ = false;
        }
        if (!resources_) return;

        auto* item = container.find(itemName());
        const bool created = item == nullptr;
        if (created) item = createItem(container);
        if (!item) return;

        const bool reinitialize = created || !ready_;
        const auto fail = [&]() {
            item->enable(false);
            ready_ = false;
        };
        if (reinitialize || pending_.color != current_.color) {
            auto* shader = resources_->shader(pending_.color);
            if (!shader || !item->setShader(shader)) {
                fail();
                return;
            }
        }

        bool geometryChanged = false;
        if (!geometryReady_ || node_->geometryRevision() != geometry_.revision) {
            const auto geometry = node_->baseDrawGeometry();
            geometryChanged = !geometryReady_ ||
                std::memcmp(geometry.vertices, geometry_.vertices, sizeof(geometry.vertices)) != 0 ||
                geometry.bounds.min() != geometry_.bounds.min() ||
                geometry.bounds.max() != geometry_.bounds.max();
            geometry_ = geometry;
            geometryReady_ = true;
        }
        if ((reinitialize || geometryChanged) && !bindGeometry(*item)) {
            fail();
            return;
        }

        // 親階層を含む行列を明示し、変形中もローカル頂点バッファを再利用する。
        if ((reinitialize || pending_.matrix != current_.matrix) && !item->setMatrix(&pending_.matrix)) {
            fail();
            return;
        }
        if (reinitialize || pending_.selectable != current_.selectable) {
            item->setSelectionMask(pending_.selectable
                ? MSelectionMask(MSelectionMask::kSelectLocators) : MSelectionMask());
        }
        if (reinitialize || pending_.hideOnPlayback != current_.hideOnPlayback) {
            item->setHideOnPlayback(pending_.hideOnPlayback);
        }
        if (item->isEnabled() != pending_.visible) item->enable(pending_.visible);
        current_ = pending_;
        ready_ = true;
    }

    bool getSelectionPath(const MRenderItem&, MDagPath& path) const override {
        path = ready_ && current_.selectable ? current_.path : MDagPath();
        return true;
    }

private:
    bool bindGeometry(MRenderItem& item) {
        std::unique_ptr<MVertexBuffer> replacement;
        auto* vertices = resources_->vertices.get();
        if (std::memcmp(geometry_.vertices, cube::vertices, sizeof(cube::vertices)) != 0) {
            replacement = vertexBuffer(geometry_.vertices);
            if (!replacement) return false;
            vertices = replacement.get();
        }
        MVertexBufferArray buffers;
        buffers.addBuffer("positions", vertices);
        if (!setGeometryForRenderItem(item, buffers, *resources_->indices, &geometry_.bounds)) {
            return false;
        }
        // 描画との関連付けが完了するまで旧バッファを保持する。
        ownedVertices_ = std::move(replacement);
        return true;
    }

    DrawState readState() const {
        DrawState state;
        MStatus status;
        MFnDagNode node(object_, &status);
        if (!status || !node.getPath(state.path) || !state.path.isValid()) return state;
        const auto parentMatrix = state.path.inclusiveMatrix(&status);
        if (!status) return state;
        state.matrix = node_->shapeDrawMatrix() * parentMatrix;
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
    BdShpLDeformableCubeNode* node_;
    std::shared_ptr<SharedResources> resources_;
    std::unique_ptr<MVertexBuffer> ownedVertices_;
    BdShpLDeformableCubeNode::Geometry geometry_{};
    DrawState current_;
    mutable DrawState pending_;
    bool geometryReady_ = false;
    bool ready_ = false;
};
}

MHWRender::MPxSubSceneOverride* BdShpLDeformableCubeNode::createSubSceneOverride(const MObject& object) {
    return new DeformableCubeSubSceneOverride(object);
}

void BdShpLDeformableCubeNode::cleanupDrawResources() {
    delete resourceCache;
    resourceCache = nullptr;
}
