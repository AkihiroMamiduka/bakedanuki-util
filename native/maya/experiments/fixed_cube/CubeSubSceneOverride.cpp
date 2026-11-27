#include "CubeResearch.h"
#include "bdUtilNodes/nodes/BdShpLCubeNode.h"

#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

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

#include <memory>
#include <vector>

namespace {
using namespace MHWRender;
namespace cube = bdUtilNodes::fixedCube;
#ifdef BD_CUBE_PROFILE
using cubeResearch::profiling::Method;
using cubeResearch::profiling::Scope;
#endif

constexpr const char* itemName = "fixedCubeLines";

std::unique_ptr<MVertexBuffer> vertexBuffer(const cube::Geometry& geometry) {
    const MVertexBufferDescriptor descriptor("", MGeometry::kPosition, MGeometry::kFloat, 3);
    auto buffer = std::make_unique<MVertexBuffer>(descriptor);
    auto* positions = buffer->acquire(cube::drawVertexCount(geometry), true);
    if (!positions) return nullptr;
    cube::writeDrawVertices(geometry, positions);
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
    struct LineBuffers {
        std::unique_ptr<MVertexBuffer> vertices;
        std::unique_ptr<MIndexBuffer> indices;
    };
    LineBuffers lines[2][2];
    std::vector<ColorShader> shaders;

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
        return ensureLines(false, false);
    }

    bool ensureLines(bool guide, bool fin) {
        auto& buffers = lines[guide][fin];
        if (buffers.vertices) return true;
        const auto geometry = cube::defaultDrawGeometry(guide, fin);
        auto newVertices = vertexBuffer(geometry);
        if (!newVertices) return false;
        auto newIndices = std::make_unique<MIndexBuffer>(MGeometry::kUnsignedInt32);
        auto* edges = newIndices->acquire(cube::drawIndexCount(geometry), true);
        if (!edges) return false;
        cube::writeDrawIndices(geometry, edges);
        newIndices->commit(edges);
        buffers.vertices = std::move(newVertices);
        buffers.indices = std::move(newIndices);
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
        : MPxSubSceneOverride(object), object_(object),
          node_(static_cast<BdShpLCubeNode*>(MFnDagNode(object).userNode())) {}

    DrawAPI supportedDrawAPIs() const override {
        return kOpenGL | kOpenGLCoreProfile | kDirectX11;
    }

    bool requiresUpdate(const MSubSceneContainer& container, const MFrameContext&) const override {
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneRequiresUpdate);
#endif
        pending_ = readState();
        auto* renderer = MRenderer::theRenderer();
        return !ready_ || !resources_ || resources_->renderer != renderer ||
            (renderer && (resources_->manager != renderer->getShaderManager() ||
                resources_->api != renderer->drawAPI())) ||
            container.count() != 1 || !(pending_ == current_) ||
            !geometryReady_ || (node_ && node_->geometryRevision() != geometry_.revision);
    }

    void update(MSubSceneContainer& container, const MFrameContext&) override {
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneUpdate);
#endif
        if (!node_) return;
        bool geometryChanged = !geometryReady_;
        if (geometryChanged || node_->geometryRevision() != geometry_.revision) {
#if defined(BD_CUBE_SUBSCENE_MATRIX) && defined(BD_CUBE_RESEARCH_SHAPE_MATRIX)
            const auto geometry = node_->baseDrawGeometry();
#else
            const auto geometry = node_->geometry();
#endif
            geometryChanged = geometryChanged ||
                !cube::sameDrawTopology(geometry, geometry_) ||
                !cube::sameDrawVertices(geometry, geometry_) ||
                geometry.bounds.min() != geometry_.bounds.min() || geometry.bounds.max() != geometry_.bounds.max();
            geometry_ = geometry;
            geometryReady_ = true;
        }
        auto* renderer = MRenderer::theRenderer();
        const bool resourcesChanged = !resources_ || resources_->renderer != renderer ||
            (renderer && (resources_->manager != renderer->getShaderManager() ||
                resources_->api != renderer->drawAPI()));
        if (resourcesChanged) {
            container.clear();
            ownedVertices_.reset();
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
#ifdef BD_CUBE_PROFILE
            Scope shaderScope(Method::subSceneUpdateShader);
#endif
            auto* shader = resources_->shader(pending_.color);
            if (!shader || !item->setShader(shader)) {
                fail();
                return;
            }
        }
        if (created || !ready_ || geometryChanged) {
            std::unique_ptr<MVertexBuffer> replacement;
            const bool guide = geometry_.guideLine;
            const bool fin = geometry_.fin() != nullptr;
            if (!resources_->ensureLines(guide, fin)) {
                fail();
                return;
            }
            const auto& shared = resources_->lines[guide][fin];
            auto* vertices = shared.vertices.get();
            if (!cube::hasDefaultDrawVertices(geometry_)) {
                replacement = vertexBuffer(geometry_);
                if (!replacement) {
                    fail();
                    return;
                }
                vertices = replacement.get();
            }
            MVertexBufferArray buffers;
            buffers.addBuffer("positions", vertices);
            MStatus bound;
            {
#ifdef BD_CUBE_PROFILE
                Scope bindScope(Method::subSceneBindGeometry);
#endif
                bound = setGeometryForRenderItem(*item, buffers, *shared.indices, &geometry_.bounds);
            }
            if (!bound) {
                fail();
                return;
            }
            // bind成功まで旧bufferを保持し、既定形状へ戻れば共有bufferを使う。
            ownedVertices_ = std::move(replacement);
        }
        // 親階層を含む行列を明示し、静止時の再設定と geometry upload を省く。
        if (created || !ready_ || pending_.matrix != current_.matrix) {
#ifdef BD_CUBE_PROFILE
            Scope matrixScope(Method::subSceneSetMatrix);
#endif
            if (!item->setMatrix(&pending_.matrix)) {
                fail();
                return;
            }
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
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneReadState);
#endif
        DrawState state;
        MStatus status;
        MFnDagNode node(object_, &status);
        if (!status || !node.getPath(state.path) || !state.path.isValid()) return state;
        state.matrix = state.path.inclusiveMatrix(&status);
        if (!status) return state;
#if defined(BD_CUBE_SUBSCENE_MATRIX) && defined(BD_CUBE_RESEARCH_SHAPE_MATRIX)
        if (node_) state.matrix = node_->shapeDrawMatrix() * state.matrix;
#endif
#ifdef BD_CUBE_PROFILE
        Scope displayScope(Method::subSceneReadDisplayState);
#endif
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
    BdShpLCubeNode* node_ = nullptr;
    std::shared_ptr<SharedResources> resources_;
    std::unique_ptr<MVertexBuffer> ownedVertices_;
    BdShpLCubeNode::Geometry geometry_;
    DrawState current_;
    mutable DrawState pending_;
    bool geometryReady_ = false;
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
