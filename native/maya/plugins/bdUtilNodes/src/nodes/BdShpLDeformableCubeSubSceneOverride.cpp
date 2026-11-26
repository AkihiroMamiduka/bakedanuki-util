#include "bdUtilNodes/nodes/BdShpLDeformableCubeNode.h"
#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
#include "DeformableCubeDisplayStateCache.h"
#endif

#include <cstring>
#include <memory>
#include <optional>
#include <utility>
#include <vector>

#include <maya/M3dView.h>
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
#include <maya/MAnimControl.h>
#include <maya/MTime.h>
#endif
#include <maya/MColor.h>
#include <maya/MDagPath.h>
#include <maya/MDGContext.h>
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
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
namespace display = bdUtilNodes::deformableCubeDisplay;
// Maya API を使う監視は plug-in の登録・解除処理で管理する。
display::DisplayMonitor* displayMonitor = nullptr;
#endif
#ifdef BD_CUBE_PROFILE
using cubeResearch::profiling::Method;
using cubeResearch::profiling::Scope;
#endif

const MString& itemName() {
    static const MString name("bdDeformableCubeLines");
    return name;
}

std::unique_ptr<MVertexBuffer> vertexBuffer(const float (&vertices)[cube::vertexCount][3], bool guideLine = false) {
    const MVertexBufferDescriptor descriptor("", MGeometry::kPosition, MGeometry::kFloat, 3);
    auto buffer = std::make_unique<MVertexBuffer>(descriptor);
    auto* positions = buffer->acquire(cube::drawVertexCount(guideLine), true);
    if (!positions) return nullptr;
    cube::writeDrawVertices(vertices, guideLine, positions);
#ifdef BD_CUBE_PROFILE
    Scope scope(Method::subSceneVertexCommit);
#endif
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
    std::unique_ptr<MVertexBuffer> guideVertices;
    std::unique_ptr<MIndexBuffer> guideIndices;
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
        auto* edges = indices->acquire(cube::indexCount, true);
        if (!edges) return false;
        std::memcpy(edges, cube::indices, sizeof(cube::indices));
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneIndexCommit);
#endif
        indices->commit(edges);
        return true;
    }

    bool ensureGuideGeometry() {
        if (guideVertices && guideIndices) return true;
        auto newVertices = vertexBuffer(cube::vertices, true);
        if (!newVertices) return false;
        auto newIndices = std::make_unique<MIndexBuffer>(MGeometry::kUnsignedInt32);
        auto* edges = newIndices->acquire(cube::drawIndexCount(true), true);
        if (!edges) return false;
        cube::writeDrawIndices(true, edges);
        {
#ifdef BD_CUBE_PROFILE
            Scope scope(Method::subSceneIndexCommit);
#endif
            newIndices->commit(edges);
        }
        guideVertices = std::move(newVertices);
        guideIndices = std::move(newIndices);
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

struct DisplayValues {
    MColor color;
    bool visible = false;
    bool selectable = false;
    bool hideOnPlayback = false;

    bool operator==(const DisplayValues& other) const {
        return color == other.color && visible == other.visible && selectable == other.selectable &&
            hideOnPlayback == other.hideOnPlayback;
    }
};

struct DrawState : DisplayValues {
    MDagPath path;
    MMatrix matrix;

    bool operator==(const DrawState& other) const {
        return path == other.path && matrix == other.matrix && DisplayValues::operator==(other);
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

    bool requiresUpdate(const MSubSceneContainer& container, const MFrameContext& frame) const override {
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneRequiresUpdate);
#endif
        if (!node_) return false;
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
        matrixUpdate_ = MatrixUpdate::none;
        transientRevision_ = 0;
        const bool deformChanged = drawMatrixCache_.revision != 0 &&
            (drawMatrixCache_.revision != node_->shapeMatrixRevision() ||
                !drawMatrixCache_.validAtCurrentTime());
        const auto graph = graphRevision();
        MStatus status;
        MMatrix world;
        const bool samePath = graph != 0 && graph == cachedPathRevision_;
        if (deformChanged && samePath && displayMonitor->isPlaying() &&
            prepareDeferred(container, frame, graph)) return true;
        if (samePath) world = cachedPath_.inclusiveMatrix(&status);
        const bool haveWorld = samePath && status;
        if (deformChanged) {
            std::optional<MMatrix> localForThisDraw;
            std::uint64_t connectedReadRevision = 0;
            if (canSkip_ && haveWorld && ready_ && geometryReady_ && resources_ &&
                resources_->matches(MRenderer::theRenderer()) && container.count() == 1 &&
                node_->geometryRevision() == geometry_.revision &&
                current_.path == cachedPath_ && MDGContext::current().isNormal()) {
                const auto displayStyle = frame.getDisplayStyle();
                const auto displayRevision = displayMonitor->displayRevision();
                if (displayCache_.canReuse(displayMonitor, displayStyle,
                        [&] { return MGeometryUtilities::displayStatus(cachedPath_); }) &&
                    displayCache_.cachedValue() == current_) {
                    const auto oldRevision = drawMatrixCache_.revision;
                    std::optional<MTime> publicationTime;
                    const auto local = node_->shapeDrawMatrix(
                        &drawMatrixCache_, &connectedReadRevision, &publicationTime);
                    const auto currentRevision = node_->shapeMatrixRevision();
                    const bool stable = drawMatrixCache_.revision != oldRevision &&
                        drawMatrixCache_.revision == currentRevision;
                    // 評価済みの値や読み取り中に世代が進んだ値は、対応する `update()` で照合する。
                    const bool transient = !stable && connectedReadRevision != 0 &&
                        currentRevision == connectedReadRevision && MDGContext::current().isNormal();
                    if ((stable || transient) &&
                        displayMonitor->displayRevision() == displayRevision &&
                        graphRevision() == graph && frame.getDisplayStyle() == displayStyle) {
                        pendingMatrix_ = local * world;
                        if (pendingMatrix_ != current_.matrix) {
                            localValid_ = false;
                            pendingWorld_ = world;
                            pendingDisplayStyle_ = displayStyle;
                            pendingDisplayRevision_ = displayRevision;
                            if (transient) {
                                transientRevision_ = connectedReadRevision;
                                transientTime_ = MAnimControl::currentTime();
                            }
                            matrixUpdate_ = MatrixUpdate::ready;
                            return true;
                        }
                        if (publicationTime) {
                            const auto* item = container.find(itemName());
                            if (item && item->InternalObjectId() == lastItemId_ &&
                                item->isEnabled() == current_.visible &&
                                MDGContext::current().isNormal() &&
                                MAnimControl::currentTime() == *publicationTime &&
                                node_->shapeMatrixRevision() == connectedReadRevision &&
                                node_->geometryRevision() == geometry_.revision &&
                                graphRevision() == graph &&
                                displayMonitor->displayRevision() == displayRevision &&
                                frame.getDisplayStyle() == displayStyle) {
                                // 描画済みの行列と一致する時刻では、取得済みのローカル行列を引き継ぐ。
                                drawMatrixCache_ = {local, connectedReadRevision, publicationTime};
                                cachedLocal_ = local;
                                lastWorld_ = world;
                                localValid_ = true;
                                return false;
                            }
                        }
                    }
                    if (connectedReadRevision != 0) localForThisDraw.emplace(local);
                }
            }

            // 読み取り中に世代が進んだ行列も、取得後の世代を照合してこの描画内でだけ使う。
            canSkip_ = false;
            localValid_ = false;
            const auto fallbackGraph = localForThisDraw ? graphRevision() : graph;
            const bool reusePath = haveWorld && fallbackGraph == graph;
            const bool reuseLocal = localForThisDraw && reusePath && MDGContext::current().isNormal() &&
                node_->shapeMatrixRevision() == connectedReadRevision;
            pending_ = readState(frame, reusePath ? &cachedPath_ : nullptr, reusePath ? &world : nullptr,
                reuseLocal ? &*localForThisDraw : nullptr);
            if (!reusePath) {
                cachedPathRevision_ = 0;
                if (fallbackGraph != 0 && pending_.path.isValid() && fallbackGraph == graphRevision()) {
                    cachedPath_ = pending_.path;
                    cachedPathRevision_ = fallbackGraph;
                }
            }
        } else {
            const bool available = ready_ && resources_ && resources_->matches(MRenderer::theRenderer()) &&
                container.count() == 1 && node_->geometryRevision() == geometry_.revision;
            if (available && haveWorld && localAndDisplayUnchanged(frame)) {
                if (world == lastWorld_) return false;
                pendingMatrix_ = cachedLocal_ * world;
                if (pendingMatrix_ == current_.matrix) {
                    lastWorld_ = world;
                    return false;
                }
                pendingWorld_ = world;
                pendingDisplayStyle_ = frame.getDisplayStyle();
                pendingDisplayRevision_ = displayMonitor->displayRevision();
                matrixUpdate_ = MatrixUpdate::ready;
                return true;
            }
            readFullState(frame, haveWorld ? &cachedPath_ : nullptr, haveWorld ? &world : nullptr, graph);
            const bool changed = !available || !(pending_ == current_);
            canSkip_ = !changed && cachedPathRevision_ != 0;
            return changed;
        }
#else
        pending_ = readState(frame);
#endif
        return !ready_ || !resources_ || !resources_->matches(MRenderer::theRenderer()) ||
            container.count() != 1 || !(pending_ == current_) ||
            node_->geometryRevision() != geometry_.revision;
    }

    void update(MSubSceneContainer& container, const MFrameContext& frame) override {
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneUpdate);
#endif
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
        const auto transientRevision = std::exchange(transientRevision_, 0);
        const auto matrixUpdate = std::exchange(matrixUpdate_, MatrixUpdate::none);
#endif
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

#ifdef BD_CUBE_CACHE_DISPLAY_STATE
        if (matrixUpdate != MatrixUpdate::none) {
            const auto graph = graphRevision();
            const bool deferred = matrixUpdate == MatrixUpdate::deferred;
            const bool currentItem = ready_ && geometryReady_ && !created && container.count() == 1 &&
                item->InternalObjectId() == lastItemId_ && graph != 0 && graph == cachedPathRevision_ &&
                node_->geometryRevision() == geometry_.revision &&
                displayMonitor->displayRevision() == pendingDisplayRevision_ &&
                frame.getDisplayStyle() == pendingDisplayStyle_ && item->isEnabled() == current_.visible;
            const auto resolved = deferred && currentItem ? resolveDeferred(frame, transientRevision, graph)
                                                         : DeferredResult::rejected;
            if (resolved == DeferredResult::sameMatrix) return;
            if (currentItem && (deferred ? resolved == DeferredResult::ready
                : (transientRevision ? transientStillCurrent(frame, transientRevision)
                    : (drawMatrixCache_.revision == node_->shapeMatrixRevision() &&
                       drawMatrixCache_.validAtCurrentTime())))) {
#ifdef BD_CUBE_PROFILE
                Scope matrixScope(Method::subSceneSetMatrix);
#endif
                if (item->setMatrix(&pendingMatrix_)) {
                    current_.matrix = pendingMatrix_;
                    lastWorld_ = pendingWorld_;
                } else {
                    item->enable(false);
                    ready_ = false;
                    canSkip_ = false;
                }
                return;
            }
            // 判定後にコンテナや表示状態が変わった場合は、現在の状態で描画項目を構成する。
            readFullState(frame, nullptr, nullptr, graphRevision());
        }
        const bool reinitialize = created || !ready_ || item->InternalObjectId() != lastItemId_;
#else
        (void)frame;
        const bool reinitialize = created || !ready_;
#endif
        const auto fail = [&]() {
            item->enable(false);
            ready_ = false;
        };
        if (reinitialize || pending_.color != current_.color) {
#ifdef BD_CUBE_PROFILE
            Scope shaderScope(Method::subSceneUpdateShader);
#endif
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
                geometry.guideLine != geometry_.guideLine ||
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
        if (reinitialize || pending_.matrix != current_.matrix) {
#ifdef BD_CUBE_PROFILE
            Scope matrixScope(Method::subSceneSetMatrix);
#endif
            if (!item->setMatrix(&pending_.matrix)) {
                fail();
                return;
            }
        }
        if (reinitialize || pending_.selectable != current_.selectable) {
            item->setSelectionMask(pending_.selectable
                ? MSelectionMask(MSelectionMask::kSelectLocators) : MSelectionMask());
        }
        if (reinitialize || pending_.hideOnPlayback != current_.hideOnPlayback) {
            item->setHideOnPlayback(pending_.hideOnPlayback);
        }
        if (item->isEnabled() != pending_.visible) item->enable(pending_.visible);
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
        lastItemId_ = item->InternalObjectId();
        canSkip_ = cachedPathRevision_ != 0;
#endif
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
        auto* indices = resources_->indices.get();
        if (geometry_.guideLine) {
            if (!resources_->ensureGuideGeometry()) return false;
            vertices = resources_->guideVertices.get();
            indices = resources_->guideIndices.get();
        }
        if (std::memcmp(geometry_.vertices, cube::vertices, sizeof(cube::vertices)) != 0) {
            replacement = vertexBuffer(geometry_.vertices, geometry_.guideLine);
            if (!replacement) return false;
            vertices = replacement.get();
        }
        MVertexBufferArray buffers;
        buffers.addBuffer("positions", vertices);
        {
#ifdef BD_CUBE_PROFILE
            Scope bindScope(Method::subSceneBindGeometry);
#endif
            if (!setGeometryForRenderItem(item, buffers, *indices, &geometry_.bounds)) {
                return false;
            }
        }
        // 描画との関連付けが完了するまで旧バッファを保持する。
        ownedVertices_ = std::move(replacement);
        return true;
    }

#ifdef BD_CUBE_CACHE_DISPLAY_STATE
    static std::uint64_t graphRevision() {
        return displayMonitor && displayMonitor->ready() ? displayMonitor->graphRevision() : 0;
    }

    enum class MatrixUpdate { none, ready, deferred };
    enum class DeferredResult { rejected, sameMatrix, ready };

    bool prepareDeferred(const MSubSceneContainer& container, const MFrameContext& frame,
        std::uint64_t graph) const {
        if (!canSkip_ || !ready_ || !geometryReady_ || !resources_ ||
            !resources_->matches(MRenderer::theRenderer()) || container.count() != 1 ||
            node_->geometryRevision() != geometry_.revision || !(current_.path == cachedPath_) ||
            !MDGContext::current().isNormal()) return false;
        const auto displayStyle = frame.getDisplayStyle();
        const auto displayRevision = displayMonitor->displayRevision();
        if (!displayCache_.canReuseWithoutStatus(displayMonitor, displayStyle) ||
            !(displayCache_.cachedValue() == current_)) return false;

        const auto revision = node_->shapeMatrixRevision();
        MTime time;
        // プラグへ読みに行かず、評価済みの接続値を取得できた時だけ保留する。
        if (!node_->tryPublishedShapeMatrix(revision, pendingMatrix_, time)) return false;
        if (lastDeferredTime_ && time == *lastDeferredTime_) return false;
        if (graphRevision() != graph || displayMonitor->displayRevision() != displayRevision ||
            node_->shapeMatrixRevision() != revision) return false;

        pendingDisplayStyle_ = displayStyle;
        pendingDisplayRevision_ = displayRevision;
        transientRevision_ = revision;
        transientTime_ = time;
        lastDeferredTime_ = time;
        // 保留中の pendingMatrix_ はローカル行列。ワールド行列と表示状態は update で取得する。
        matrixUpdate_ = MatrixUpdate::deferred;
        return true;
    }

    DeferredResult resolveDeferred(const MFrameContext& frame, std::uint64_t revision, std::uint64_t graph) {
        if (!displayMonitor->isPlaying() || !MDGContext::current().isNormal() ||
            MAnimControl::currentTime() != transientTime_ || node_->shapeMatrixRevision() != revision)
            return DeferredResult::rejected;

        MStatus status;
        const auto world = cachedPath_.inclusiveMatrix(&status);
        if (!status || graphRevision() != graph ||
            !displayCache_.canReuse(displayMonitor, frame.getDisplayStyle(),
                [&] { return MGeometryUtilities::displayStatus(cachedPath_); }) ||
            !(displayCache_.cachedValue() == current_) ||
            !MDGContext::current().isNormal() || MAnimControl::currentTime() != transientTime_ ||
            node_->shapeMatrixRevision() != revision || node_->geometryRevision() != geometry_.revision ||
            graphRevision() != graph || displayMonitor->displayRevision() != pendingDisplayRevision_ ||
            frame.getDisplayStyle() != pendingDisplayStyle_) return DeferredResult::rejected;

        const auto composite = pendingMatrix_ * world;
        if (composite == current_.matrix) {
            drawMatrixCache_ = {pendingMatrix_, revision, transientTime_};
            cachedLocal_ = pendingMatrix_;
            lastWorld_ = world;
            localValid_ = true;
            return DeferredResult::sameMatrix;
        }
        pendingWorld_ = world;
        pendingMatrix_ = composite;
        localValid_ = false;
        return DeferredResult::ready;
    }

    bool transientStillCurrent(const MFrameContext& frame, std::uint64_t revision) const {
        if (!MDGContext::current().isNormal() || MAnimControl::currentTime() != transientTime_) return false;
        MStatus status;
        const auto world = cachedPath_.inclusiveMatrix(&status);
        return status && world == pendingWorld_ &&
            displayCache_.canReuse(displayMonitor, frame.getDisplayStyle(),
                [&] { return MGeometryUtilities::displayStatus(cachedPath_); }) &&
            displayCache_.cachedValue() == current_ && node_->shapeMatrixRevision() == revision &&
            node_->geometryRevision() == geometry_.revision && graphRevision() == cachedPathRevision_ &&
            displayMonitor->displayRevision() == pendingDisplayRevision_;
    }

    bool localAndDisplayUnchanged(const MFrameContext& frame) const {
        return canSkip_ && localValid_ && drawMatrixCache_.revision == node_->shapeMatrixRevision() &&
            drawMatrixCache_.validAtCurrentTime() && MDGContext::current().isNormal() &&
            displayCache_.canReuse(displayMonitor, frame.getDisplayStyle(),
                [&] { return MGeometryUtilities::displayStatus(cachedPath_); });
    }

    void readFullState(const MFrameContext& frame, const MDagPath* path, const MMatrix* world,
        std::uint64_t graph) const {
        localValid_ = false;
        pending_ = readState<true>(frame, path, world);
        cachedPath_ = pending_.path;
        cachedPathRevision_ = cachedPath_.isValid() ? graph : 0;
    }
#endif

    template<bool cacheTransforms = false>
    DrawState readState(const MFrameContext& frame, const MDagPath* knownPath = nullptr,
        const MMatrix* knownWorld = nullptr, const MMatrix* localForThisDraw = nullptr) const {
#ifdef BD_CUBE_PROFILE
        Scope scope(Method::subSceneReadState);
#endif
        DrawState state;
        MStatus status;
        if (knownPath) {
            state.path = *knownPath;
        } else {
            const MFnDagNode node(object_, &status);
            if (!status || !node.getPath(state.path) || !state.path.isValid()) {
                state.path = MDagPath();
                return state;
            }
        }
        const auto parentMatrix = knownWorld ? *knownWorld : state.path.inclusiveMatrix(&status);
        if (!status) {
            state.path = MDagPath();
            return state;
        }
        const auto local = localForThisDraw ? *localForThisDraw : node_->shapeDrawMatrix(&drawMatrixCache_);
        state.matrix = local * parentMatrix;
        const auto readValues = [&] { return readDisplay(state.path, MFnDagNode(object_)); };
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
        if constexpr (cacheTransforms) {
            lastWorld_ = parentMatrix;
            cachedLocal_ = local;
            localValid_ = MDGContext::current().isNormal() && drawMatrixCache_.revision != 0 &&
                drawMatrixCache_.revision == node_->shapeMatrixRevision() &&
                drawMatrixCache_.validAtCurrentTime();
        }
        static_cast<DisplayValues&>(state) = displayCache_.read(
            displayMonitor, state.path, frame.getDisplayStyle(), [&] {
#ifdef BD_CUBE_PROFILE
                Scope scope(Method::subSceneProbeDisplayStatus);
#endif
                // ハイライト解除など、選択コールバックを送らない変化も確認する。
                return MGeometryUtilities::displayStatus(state.path);
            }, readValues
        );
#else
        (void)frame;
        static_cast<DisplayValues&>(state) = readValues();
#endif
        return state;
    }

    static DisplayValues readDisplay(const MDagPath& path, const MFnDagNode& node) {
#ifdef BD_CUBE_PROFILE
        Scope displayScope(Method::subSceneReadDisplayState);
#endif
        DisplayValues state;
        MStatus status;
        state.visible = path.isVisible(&status) && status && !node.isIntermediateObject();
        const auto overrides = path.getDrawOverrideInfo();
        const auto type = path.isTemplated() ? MDAGDrawOverrideInfo::kDisplayTypeTemplate
            : (overrides.fOverrideEnabled ? overrides.fDisplayType : MDAGDrawOverrideInfo::kDisplayTypeNormal);
        if (overrides.fOverrideEnabled) state.visible = state.visible && overrides.fEnableVisible;
        state.hideOnPlayback = overrides.fOverrideEnabled && !overrides.fPlaybackVisible;
        state.selectable = state.visible && type == MDAGDrawOverrideInfo::kDisplayTypeNormal;
        state.color = MGeometryUtilities::wireframeColor(path);
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
    mutable BdShpLDeformableCubeNode::DrawMatrixCache drawMatrixCache_;
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
    mutable display::DisplayCache<DisplayValues> displayCache_;
    mutable MDagPath cachedPath_;
    mutable std::uint64_t cachedPathRevision_ = 0;
    mutable MMatrix lastWorld_;
    mutable MMatrix cachedLocal_;
    mutable MMatrix pendingWorld_;
    mutable MMatrix pendingMatrix_;
    mutable std::uint64_t pendingDisplayRevision_ = 0;
    mutable unsigned int pendingDisplayStyle_ = 0;
    mutable bool localValid_ = false;
    mutable MatrixUpdate matrixUpdate_ = MatrixUpdate::none;
    mutable std::optional<MTime> lastDeferredTime_;
    mutable std::uint64_t transientRevision_ = 0;
    mutable MTime transientTime_;
    MUint64 lastItemId_ = 0;
    mutable bool canSkip_ = false;
#endif
    bool geometryReady_ = false;
    bool ready_ = false;
};
}

MHWRender::MPxSubSceneOverride* BdShpLDeformableCubeNode::createSubSceneOverride(const MObject& object) {
    return new DeformableCubeSubSceneOverride(object);
}

#ifdef BD_CUBE_CACHE_DISPLAY_STATE
void BdShpLDeformableCubeNode::startDisplayStateMonitoring() {
    displayMonitor = new display::DisplayMonitor();
}
#endif

void BdShpLDeformableCubeNode::cleanupDrawResources() {
#ifdef BD_CUBE_CACHE_DISPLAY_STATE
    delete std::exchange(displayMonitor, nullptr);
#endif
    delete resourceCache;
    resourceCache = nullptr;
}
