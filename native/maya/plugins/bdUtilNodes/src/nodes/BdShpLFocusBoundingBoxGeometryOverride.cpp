#include "bdUtilNodes/nodes/BdShpLFocusBoundingBoxNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"

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

constexpr unsigned int axisCrossIndices[] = {0, 1, 2, 3, 4, 5};
constexpr unsigned int squareIndices[] = {0, 1, 1, 2, 2, 3, 3, 0};
constexpr unsigned int crossIndices[] = {0, 1, 2, 3};

template <FocusBoundsWire Wire>
constexpr const auto& wireIndices() {
    if constexpr (Wire == FocusBoundsWire::Box) return cube::indices;
    else if constexpr (Wire == FocusBoundsWire::CrossLine3Axis) return axisCrossIndices;
    else if constexpr (Wire == FocusBoundsWire::Square) return squareIndices;
    else return crossIndices;
}

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

template <FocusBoundsWire Wire>
class FocusBoundsGeometryOverride final : public MPxGeometryOverride {
    using Node = BdShpLFocusBoundsNode<Wire>;
    static constexpr unsigned int VertexCount = isPlanarFocusWire(Wire) ? 4 :
        (Wire == FocusBoundsWire::CrossLine3Axis ? 6 : std::size(cube::vertices));

public:
    explicit FocusBoundsGeometryOverride(const MObject& node)
        : MPxGeometryOverride(node),
          node_(static_cast<Node*>(MFnDependencyNode(node).userNode())) {}

    DrawAPI supportedDrawAPIs() const override { return kAllDevices; }
    bool hasUIDrawables() const override { return false; }
    bool supportsEvaluationManagerParallelUpdate() const override { return true; }
    bool supportsVP2CustomCaching() const override { return false; }

    bool requiresGeometryUpdate() const override {
        return buffersDirty_.load(std::memory_order_relaxed) ||
            (node_ && node_->previewRevision() != previewRevision_.load(std::memory_order_acquire));
    }
    bool requiresUpdateRenderItems(const MDagPath&) const override {
        return node_ && node_->previewRevision() != itemsRevision_.load(std::memory_order_acquire);
    }

    void updateDG() override {
        if (!node_ || node_->previewRevision() == previewRevision_.load(std::memory_order_relaxed)) {
            return;
        }
        preview_ = node_->preview();
        buffersDirty_.store(preview_.visible, std::memory_order_relaxed);
        previewRevision_.store(preview_.revision, std::memory_order_release);
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
        if (!preview_.visible) {
            // 通常使用時は DAG の境界だけを保持する。
            if (list.length() != 0) {
                const int index = list.indexOf(itemName());
                if (index >= 0 && !list.removeAt(index)) return;
            }
            itemsRevision_.store(preview_.revision, std::memory_order_release);
            return;
        }

        const int index = list.indexOf(itemName());
        auto* item = index >= 0 ? list.itemAt(index) : nullptr;
        if (!item) {
            item = createItem(list);
            if (!item) return;
            buffersDirty_.store(true, std::memory_order_relaxed);
        }
        if (item->setBoundingBox(preview_.bounds)) {
            itemsRevision_.store(preview_.revision, std::memory_order_release);
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
        if (!preview_.visible) return;
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
            auto* values = static_cast<float*>(buffer->acquire(VertexCount, true));
            if (!values) return;
            writePositions(values);
            buffer->commit(values);
            positionsReady = true;
        }
        if (!positionsReady) return;

        auto* buffer = data.createIndexBuffer(MGeometry::kUnsignedInt32);
        if (!buffer) return;
        constexpr auto& indices = wireIndices<Wire>();
        auto* values = buffer->acquire(std::size(indices), true);
        if (!values) return;
        std::memcpy(values, indices, sizeof(indices));
        buffer->commit(values);
        if (item->associateWithIndexBuffer(buffer)) {
            buffersDirty_.store(false, std::memory_order_relaxed);
        }
    }

private:
    void writePositions(float* values) const {
        const auto low = preview_.bounds.min();
        const auto high = preview_.bounds.max();
        if constexpr (Wire == FocusBoundsWire::Box) {
            for (unsigned int vertex = 0; vertex < VertexCount; ++vertex) {
                for (unsigned int axis = 0; axis < 3; ++axis) {
                    const auto coordinate = cube::vertices[vertex][axis] < 0 ? low[axis] : high[axis];
                    values[3 * vertex + axis] = static_cast<float>(coordinate);
                }
            }
        } else if constexpr (Wire == FocusBoundsWire::Square) {
            const auto first = preview_.firstAxis;
            const auto second = preview_.secondAxis;
            const auto normal = 3 - first - second;
            for (unsigned int vertex = 0; vertex < VertexCount; ++vertex) {
                auto* point = values + 3 * vertex;
                point[first] = static_cast<float>(vertex == 1 || vertex == 2 ? high[first] : low[first]);
                point[second] = static_cast<float>(vertex >= 2 ? high[second] : low[second]);
                point[normal] = 0.0f;
            }
        } else {
            const auto center = preview_.bounds.center();
            const unsigned int axes[] = {preview_.firstAxis, preview_.secondAxis, 2};
            for (unsigned int line = 0; line < VertexCount / 2; ++line) {
                auto* start = values + 6 * line;
                auto* end = start + 3;
                for (unsigned int component = 0; component < 3; ++component) {
                    start[component] = static_cast<float>(center[component]);
                    end[component] = start[component];
                }
                const auto axis = axes[line];
                start[axis] = static_cast<float>(low[axis]);
                end[axis] = static_cast<float>(high[axis]);
            }
        }
    }

    Node* node_;
    typename Node::Preview preview_;
    std::atomic<std::uint64_t> previewRevision_{0};
    std::atomic<std::uint64_t> itemsRevision_{0};
    std::atomic<bool> buffersDirty_{false};
};

}  // namespace

template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingBoxNode::createGeometryOverride(const MObject& node) {
    return new FocusBoundsGeometryOverride<FocusBoundsWire::Box>(node);
}

template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingCrossLine3AxisNode::createGeometryOverride(const MObject& node) {
    return new FocusBoundsGeometryOverride<FocusBoundsWire::CrossLine3Axis>(node);
}

template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingSquareNode::createGeometryOverride(const MObject& node) {
    return new FocusBoundsGeometryOverride<FocusBoundsWire::Square>(node);
}

template <>
MHWRender::MPxGeometryOverride* BdShpLFocusBoundingCrossLineNode::createGeometryOverride(const MObject& node) {
    return new FocusBoundsGeometryOverride<FocusBoundsWire::CrossLine>(node);
}
