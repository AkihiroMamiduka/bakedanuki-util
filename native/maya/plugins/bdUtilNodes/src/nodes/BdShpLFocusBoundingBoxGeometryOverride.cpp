#include "bdUtilNodes/nodes/BdShpLFocusBoundingBoxNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"

#include <atomic>
#include <cstring>
#include <iterator>

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
using namespace MHWRender;
namespace cube = bdUtilNodes::fixedCube;

const MString& itemName() {
    static const MString name("bdFocusBoundingBoxWire");
    return name;
}

MRenderItem* createItem(MRenderItemList& list) {
    auto* renderer = MRenderer::theRenderer();
    const auto* shaders = renderer ? renderer->getShaderManager() : nullptr;
    if (!shaders) return nullptr;
    auto* shader = shaders->getStockShader(MShaderManager::k3dSolidShader);
    if (!shader) return nullptr;

    auto color = M3dView::templateColor();
    color.a = 1.0f;
    MRenderItem* item = nullptr;
    if (shader->setParameter("solidColor", &color.r)) {
        item = MRenderItem::Create(itemName(), MRenderItem::NonMaterialSceneItem, MGeometry::kLines);
    }
    const bool bound = item && item->setShader(shader);
    shaders->releaseShader(shader);
    if (!bound) {
        if (item) MRenderItem::Destroy(item);
        return nullptr;
    }

    item->setDrawMode(MGeometry::kAll);
    item->setWantConsolidation(true);
    item->castsShadows(false);
    item->receivesShadows(false);
    item->setExcludedFromPostEffects(true);
    item->setExcludedFromDefaultMaterialOverride(true);
    item->setObjectTypeExclusionFlag(MFrameContext::kExcludePluginShapes);
    item->depthPriority(MRenderItem::sDormantWireDepthPriority);
    item->setSelectionMask(MSelectionMask());
    if (!list.append(item)) {
        MRenderItem::Destroy(item);
        return nullptr;
    }
    return item;
}

class FocusBoundingBoxGeometryOverride final : public MPxGeometryOverride {
    using Node = BdShpLFocusBoundingBoxNode;

public:
    explicit FocusBoundingBoxGeometryOverride(const MObject& node)
        : MPxGeometryOverride(node),
          node_(static_cast<Node*>(MFnDependencyNode(node).userNode())) {}

    DrawAPI supportedDrawAPIs() const override { return kAllDevices; }
    bool hasUIDrawables() const override { return false; }
    bool supportsEvaluationManagerParallelUpdate() const override { return true; }
    bool supportsVP2CustomCaching() const override { return false; }

    bool requiresGeometryUpdate() const override {
        return buffersDirty_.load(std::memory_order_relaxed) ||
            previewNeedsUpdate(previewRevision_.load(std::memory_order_acquire));
    }
    bool requiresUpdateRenderItems(const MDagPath&) const override {
        return previewNeedsUpdate(itemsRevision_.load(std::memory_order_acquire));
    }

    void updateDG() override {
        if (!previewNeedsUpdate(previewRevision_.load(std::memory_order_relaxed))) return;
        const auto geometry = node_->previewGeometry();
        if (!geometry.visible || !geometry_.visible ||
            std::memcmp(geometry.vertices, geometry_.vertices, sizeof(geometry.vertices)) != 0) {
            buffersDirty_.store(geometry.visible, std::memory_order_relaxed);
        }
        geometry_ = geometry;
        previewRevision_.store(geometry_.revision, std::memory_order_release);
    }
    void cleanUp() override {}

    bool isStreamDirty(const MVertexBufferDescriptor&) override {
        return buffersDirty_.load(std::memory_order_relaxed);
    }
    bool isIndexingDirty(const MRenderItem&) override {
        // 寸法の編集時は、既存の render item に対しても頂点と辺を一緒に更新する。
        return buffersDirty_.load(std::memory_order_relaxed);
    }

    void updateRenderItems(const MDagPath& path, MRenderItemList& list) override {
        if (!geometry_.visible) {
            // 通常使用時は DAG の境界だけを保持する。
            if (list.length() != 0) {
                const int index = list.indexOf(itemName());
                if (index >= 0 && !list.removeAt(index)) return;
            }
            itemsRevision_.store(geometry_.revision, std::memory_order_release);
            return;
        }

        const int index = list.indexOf(itemName());
        auto* item = index >= 0 ? list.itemAt(index) : nullptr;
        if (!item) {
            item = createItem(list);
            if (!item) return;
            buffersDirty_.store(true, std::memory_order_relaxed);
        }
        if (item->setBoundingBox(geometry_.bounds)) {
            itemsRevision_.store(geometry_.revision, std::memory_order_release);
        }

        const auto status = MGeometryUtilities::displayStatus(path);
        const auto overrides = path.getDrawOverrideInfo();
        item->enable(path.isVisible() && status != kInvisible && status != kIntermediateObject &&
            (!overrides.fOverrideEnabled || overrides.fEnableVisible));
        item->setHideOnPlayback(overrides.fOverrideEnabled && !overrides.fPlaybackVisible);
    }

    void populateGeometry(
        const MGeometryRequirements& requirements, const MRenderItemList& items, MGeometry& data
    ) override {
        if (!geometry_.visible) return;
        const int index = items.indexOf(itemName());
        const auto* item = index >= 0 ? items.itemAt(index) : nullptr;
        if (!item) return;

        const auto& descriptors = requirements.vertexRequirements();
        bool positionsReady = false;
        for (int i = 0; i < descriptors.length(); ++i) {
            MVertexBufferDescriptor descriptor;
            if (!descriptors.getDescriptor(i, descriptor)) return;
            if (descriptor.semantic() != MGeometry::kPosition) continue;
            if (descriptor.dataType() != MGeometry::kFloat || descriptor.dimension() != 3) return;
            auto* buffer = data.createVertexBuffer(descriptor);
            if (!buffer) return;
            auto* values = static_cast<float*>(buffer->acquire(Node::VertexCount, true));
            if (!values) return;
            std::memcpy(values, geometry_.vertices, sizeof(geometry_.vertices));
            buffer->commit(values);
            positionsReady = true;
        }
        if (!positionsReady) return;

        auto* buffer = data.createIndexBuffer(MGeometry::kUnsignedInt32);
        if (!buffer) return;
        auto* values = buffer->acquire(std::size(cube::indices), true);
        if (!values) return;
        std::memcpy(values, cube::indices, sizeof(cube::indices));
        buffer->commit(values);
        if (item->associateWithIndexBuffer(buffer)) {
            buffersDirty_.store(false, std::memory_order_relaxed);
        }
    }

private:
    bool previewNeedsUpdate(std::uint64_t revision) const {
        return node_ && node_->previewNeedsUpdate(revision);
    }

    Node* node_;
    Node::Geometry geometry_;
    std::atomic<std::uint64_t> previewRevision_{0};
    std::atomic<std::uint64_t> itemsRevision_{0};
    std::atomic<bool> buffersDirty_{false};
};

}  // namespace

MHWRender::MPxGeometryOverride* BdShpLFocusBoundingBoxNode::createGeometryOverride(const MObject& node) {
    return new FocusBoundingBoxGeometryOverride(node);
}
