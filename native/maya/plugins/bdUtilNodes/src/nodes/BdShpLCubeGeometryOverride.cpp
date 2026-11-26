#include "bdUtilNodes/nodes/BdShpLCubeNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <algorithm>
#include <atomic>
#include <cstring>
#include <memory>
#include <vector>

#include <maya/M3dView.h>
#include <maya/MColor.h>
#include <maya/MDagPath.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFrameContext.h>
#include <maya/MHWGeometry.h>
#include <maya/MHWGeometryUtilities.h>
#include <maya/MPxGeometryOverride.h>
#include <maya/MSelectionMask.h>
#include <maya/MShaderManager.h>
#include <maya/MViewport2Renderer.h>

namespace {

struct CubeShader {
    MHWRender::MRenderer* renderer = nullptr;
    const MHWRender::MShaderManager* manager = nullptr;
    MHWRender::MShaderInstance* shader = nullptr;
    MHWRender::DrawAPI api = MHWRender::kNone;
    MColor color;

    ~CubeShader() {
        auto* current = MHWRender::MRenderer::theRenderer(false);
        if (shader && current == renderer && current &&
            current->getShaderManager() == manager) {
            manager->releaseShader(shader);
        }
    }
};

// shaderをDLL終了時のstatic破棄へ残さず、unload時に明示解放する。
std::vector<std::shared_ptr<CubeShader>>* shaderCache = nullptr;

std::shared_ptr<CubeShader> cubeShader(const MColor& color) {
    auto* renderer = MHWRender::MRenderer::theRenderer();
    const auto* manager = renderer ? renderer->getShaderManager() : nullptr;
    if (!manager) return nullptr;
    if (!shaderCache) shaderCache = new std::vector<std::shared_ptr<CubeShader>>;
    auto& shaders = *shaderCache;
    for (const auto& value : shaders) {
        if (value->renderer == renderer && value->manager == manager &&
            value->api == renderer->drawAPI() && value->color == color) {
            return value;
        }
    }
#ifdef BD_CUBE_DRAW_PROFILE
    auto* shader = manager->getStockShader(MHWRender::MShaderManager::k3dSolidShader,
        cubeResearch::profiling::recordDraw, nullptr);
#else
    auto* shader = manager->getStockShader(MHWRender::MShaderManager::k3dSolidShader);
#endif
    if (!shader) return nullptr;
    if (!shader->setParameter("solidColor", &color.r)) {
        manager->releaseShader(shader);
        return nullptr;
    }
    auto value = std::make_shared<CubeShader>();
    value->renderer = renderer;
    value->manager = manager;
    value->shader = shader;
    value->api = renderer->drawAPI();
    value->color = color;
    shaders.push_back(value);
    return value;
}

class CubeGeometryOverride final : public MHWRender::MPxGeometryOverride {
public:
    explicit CubeGeometryOverride(const MObject& node)
        : MPxGeometryOverride(node),
          node_(static_cast<BdShpLCubeNode*>(MFnDependencyNode(node).userNode())) {
        std::memcpy(geometry_.vertices, bdUtilNodes::fixedCube::vertices, sizeof(geometry_.vertices));
        geometry_.bounds = bdUtilNodes::fixedCube::bounds();
    }

    MHWRender::DrawAPI supportedDrawAPIs() const override {
        return MHWRender::kAllDevices;
    }

    bool hasUIDrawables() const override { return false; }
    bool requiresGeometryUpdate() const override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::requiresGeometry);
#endif
        return geometryDirty_.load(std::memory_order_relaxed) ||
            (node_ && node_->geometryRevision() != geometryRevision_.load(std::memory_order_acquire));
    }
    bool requiresUpdateRenderItems(const MDagPath&) const override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::requiresRenderItems);
#endif
        return node_ && node_->geometryRevision() != boundsRevision_.load(std::memory_order_acquire);
    }
    bool supportsEvaluationManagerParallelUpdate() const override { return true; }
    bool supportsVP2CustomCaching() const override { return false; }

    void updateDG() override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::updateDG);
#endif
        if (!node_ || node_->geometryRevision() == geometryRevision_.load(std::memory_order_relaxed)) return;
        const auto geometry = node_->geometry();
        const bool topologyChanged = geometry.guideLine != geometry_.guideLine;
        if (topologyChanged) indexingDirty_.store(true, std::memory_order_relaxed);
        if (topologyChanged || std::memcmp(geometry.vertices, geometry_.vertices, sizeof(geometry.vertices)) != 0) {
            geometryDirty_.store(true, std::memory_order_relaxed);
        }
        geometry_ = geometry;
        geometryRevision_.store(geometry.revision, std::memory_order_release);
    }
    void cleanUp() override {}

    bool isIndexingDirty(const MHWRender::MRenderItem&) override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::indexingDirty);
#endif
        return indexingDirty_.load(std::memory_order_relaxed);
    }

    bool isStreamDirty(const MHWRender::MVertexBufferDescriptor&) override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::streamDirty);
#endif
        return geometryDirty_.load(std::memory_order_relaxed);
    }

    void updateRenderItems(
        const MDagPath& path, MHWRender::MRenderItemList& list
    ) override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::updateRenderItems);
#endif
        const int index = list.indexOf(itemName());
        auto* item = index >= 0 ? list.itemAt(index) : nullptr;
        const bool created = item == nullptr;
        if (!item) {
            item = MHWRender::MRenderItem::Create(
                itemName(), MHWRender::MRenderItem::NonMaterialSceneItem,
                MHWRender::MGeometry::kLines
            );
            if (!item) return;
            item->setDrawMode(MHWRender::MGeometry::kAll);
            item->setWantConsolidation(true);
            item->castsShadows(false);
            item->receivesShadows(false);
            item->setExcludedFromPostEffects(true);
            item->setExcludedFromDefaultMaterialOverride(true);
            item->setObjectTypeExclusionFlag(MHWRender::MFrameContext::kExcludePluginShapes);
            item->depthPriority(MHWRender::MRenderItem::sDormantWireDepthPriority);
            if (!list.append(item)) {
                MHWRender::MRenderItem::Destroy(item);
                return;
            }
            geometryDirty_.store(true, std::memory_order_relaxed);
            indexingDirty_.store(true, std::memory_order_relaxed);
        }

        if (item->setBoundingBox(geometry_.bounds)) {
            boundsRevision_.store(geometry_.revision, std::memory_order_release);
        }

        const auto status = MHWRender::MGeometryUtilities::displayStatus(path);
        const auto overrides = path.getDrawOverrideInfo();
        const bool templated = path.isTemplated() ||
            status == MHWRender::kTemplate || status == MHWRender::kActiveTemplate;
        const auto displayType = templated ? MDAGDrawOverrideInfo::kDisplayTypeTemplate
            : (overrides.fOverrideEnabled ? overrides.fDisplayType
                : MDAGDrawOverrideInfo::kDisplayTypeNormal);
        const bool selectable = displayType == MDAGDrawOverrideInfo::kDisplayTypeNormal;
        item->setSelectionMask(selectable
            ? MSelectionMask(MSelectionMask::kSelectLocators) : MSelectionMask());
        item->setHideOnPlayback(overrides.fOverrideEnabled && !overrides.fPlaybackVisible);
        const bool visible = path.isVisible() && status != MHWRender::kInvisible &&
            status != MHWRender::kIntermediateObject &&
            (!overrides.fOverrideEnabled || overrides.fEnableVisible);
        if (!visible) {
            item->enable(false);
            return;
        }

        auto color = MHWRender::MGeometryUtilities::wireframeColor(path);
        if (displayType == MDAGDrawOverrideInfo::kDisplayTypeTemplate) {
            color = M3dView::templateColor();
        } else if (displayType == MDAGDrawOverrideInfo::kDisplayTypeReference) {
            color = M3dView::referenceLayerColor();
        }
        color.a = 1.0f;
        auto shader = cubeShader(color);
        if (!shader) {
            item->enable(false);
            return;
        }
        if (renderer_ != shader->renderer || manager_ != shader->manager || api_ != shader->api) {
            renderer_ = shader->renderer;
            manager_ = shader->manager;
            api_ = shader->api;
            geometryDirty_.store(true, std::memory_order_relaxed);
            indexingDirty_.store(true, std::memory_order_relaxed);
        }
        auto binding = std::find_if(bindings_.begin(), bindings_.end(),
            [item](const auto& value) { return value.item == item; });
        if (created || binding == bindings_.end() || binding->shader != shader) {
            if (!item->setShader(shader->shader)) {
                item->enable(false);
                return;
            }
            if (binding == bindings_.end()) bindings_.push_back({item, shader});
            else binding->shader = std::move(shader);
        }
        item->enable(true);
        // 親階層の最終行列はMayaが適用し、ローカル頂点を変換しない。
    }

    void populateGeometry(
        const MHWRender::MGeometryRequirements& requirements,
        const MHWRender::MRenderItemList& renderItems,
        MHWRender::MGeometry& data
    ) override {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::populateGeometry);
#endif
        // 位置だけの変更では辺の接続を再利用し、資源の再要求時は両方を用意する。
        bool positionsReady = false;
        const auto& descriptors = requirements.vertexRequirements();
        for (int i = 0; i < descriptors.length(); ++i) {
            MHWRender::MVertexBufferDescriptor descriptor;
            if (!descriptors.getDescriptor(i, descriptor)) return;
            if (descriptor.semantic() != MHWRender::MGeometry::kPosition) continue;
            if (descriptor.dataType() != MHWRender::MGeometry::kFloat || descriptor.dimension() != 3) return;
            auto* buffer = data.createVertexBuffer(descriptor);
            if (!buffer) return;
            auto* values = buffer->acquire(bdUtilNodes::fixedCube::drawVertexCount(geometry_.guideLine), true);
            if (!values) return;
            bdUtilNodes::fixedCube::writeDrawVertices(geometry_.vertices, geometry_.guideLine, values);
            {
#ifdef BD_CUBE_PROFILE
                cubeResearch::profiling::Scope commitScope(cubeResearch::profiling::Method::geometryVertexCommit);
#endif
                buffer->commit(values);
            }
            positionsReady = true;
        }
        if (!positionsReady) return;
        auto* buffer = data.indexBufferCount() > 0 ? data.indexBuffer(0) : nullptr;
        if (indexingDirty_.load(std::memory_order_relaxed) || !buffer) {
            if (!buffer) buffer = data.createIndexBuffer(MHWRender::MGeometry::kUnsignedInt32);
            if (!buffer) return;
            auto* values = buffer->acquire(bdUtilNodes::fixedCube::drawIndexCount(geometry_.guideLine), true);
            if (!values) return;
            bdUtilNodes::fixedCube::writeDrawIndices(geometry_.guideLine, values);
#ifdef BD_CUBE_PROFILE
            cubeResearch::profiling::Scope commitScope(cubeResearch::profiling::Method::geometryIndexCommit);
#endif
            buffer->commit(values);
        }
        bool associated = false;
        for (int i = 0; i < renderItems.length(); ++i) {
            const auto* item = renderItems.itemAt(i);
            if (!item || item->name() != itemName()) continue;
            if (!item->associateWithIndexBuffer(buffer)) return;
            associated = true;
        }
        if (associated) {
            geometryDirty_.store(false, std::memory_order_relaxed);
            indexingDirty_.store(false, std::memory_order_relaxed);
        }
    }

private:
    struct Binding {
        const MHWRender::MRenderItem* item;
        std::shared_ptr<CubeShader> shader;
    };

    static const MString& itemName() {
        static const MString name("bdCubeGeometryWire");
        return name;
    }

    std::vector<Binding> bindings_;
    BdShpLCubeNode* node_;
    BdShpLCubeNode::Geometry geometry_;
    std::atomic<std::uint64_t> geometryRevision_{0};
    std::atomic<std::uint64_t> boundsRevision_{0};
    MHWRender::MRenderer* renderer_ = nullptr;
    const MHWRender::MShaderManager* manager_ = nullptr;
    MHWRender::DrawAPI api_ = MHWRender::kNone;
    std::atomic<bool> geometryDirty_{true};
    std::atomic<bool> indexingDirty_{true};
};

}  // namespace

MHWRender::MPxGeometryOverride* BdShpLCubeNode::createGeometryOverride(const MObject& node) {
    return new CubeGeometryOverride(node);
}

void BdShpLCubeNode::cleanupDrawResources() {
    delete shaderCache;
    shaderCache = nullptr;
}
