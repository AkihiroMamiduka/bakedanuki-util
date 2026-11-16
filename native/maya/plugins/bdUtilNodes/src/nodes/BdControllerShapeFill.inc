// 焼込み済みの線と面を保持し、描画状態とGPU資源の寿命を管理する。
struct ControllerFillShader;

auto controllerFillRasterSignature(const MHWRender::MRasterizerStateDesc& value) {
    return std::make_tuple(
        value.fillMode, value.cullMode, value.frontCounterClockwise,
        value.depthBiasIsFloat, value.depthBias, value.depthBiasClamp,
        value.slopeScaledDepthBias, value.depthClipEnable, value.scissorEnable,
        value.multiSampleEnable, value.antialiasedLineEnable
    );
}

auto controllerFillDepthSignature(const MHWRender::MDepthStencilStateDesc& value) {
    return std::make_tuple(
        value.depthEnable, value.depthWriteEnable, value.depthFunc,
        value.stencilEnable, value.stencilReadMask, value.stencilWriteMask,
        value.stencilReferenceVal,
        value.frontFace.stencilPassOp, value.frontFace.stencilFailOp,
        value.frontFace.stencilDepthFailOp, value.frontFace.stencilFunc,
        value.backFace.stencilPassOp, value.backFace.stencilFailOp,
        value.backFace.stencilDepthFailOp, value.backFace.stencilFunc
    );
}

struct ControllerFillRasterState {
    MHWRender::MRenderer* renderer = nullptr;
    MHWRender::MRasterizerStateDesc description;
    const MHWRender::MRasterizerState* state = nullptr;

    ~ControllerFillRasterState() {
        if (state && renderer == MHWRender::MRenderer::theRenderer())
            MHWRender::MStateManager::releaseRasterizerState(state);
    }
};

struct ControllerFillDepthState {
    MHWRender::MRenderer* renderer = nullptr;
    MHWRender::MDepthStencilStateDesc description;
    const MHWRender::MDepthStencilState* state = nullptr;

    ~ControllerFillDepthState() {
        if (state && renderer == MHWRender::MRenderer::theRenderer())
            MHWRender::MStateManager::releaseDepthStencilState(state);
    }
};

struct ControllerFillSavedState {
    MHWRender::MDrawContext* context = nullptr;
    MHWRender::MShaderInstance* shader = nullptr;
    const MHWRender::MRasterizerState* raster = nullptr;
    const MHWRender::MDepthStencilState* depth = nullptr;
};

struct ControllerFillThreadState {
    std::deque<ControllerFillSavedState> saved;
    std::vector<std::unique_ptr<ControllerFillRasterState>> rasters;
    std::vector<std::unique_ptr<ControllerFillDepthState>> depths;
};

struct ControllerFillResources {
    std::mutex mutex;
    std::vector<std::unique_ptr<ControllerFillThreadState>> threads;
    std::vector<std::weak_ptr<ControllerFillShader>> shaders;
    std::atomic<std::size_t> shaderOwners{0};
    std::atomic<bool> healthy{true};
    std::size_t activeDraws = 0;
    std::uint64_t epoch = 1;
    bool closed = false;
};

ControllerFillResources& controllerFillResources() {
    static ControllerFillResources value;
    return value;
}

struct ControllerFillThreadCache {
    ControllerFillThreadState* state;
    std::uint64_t epoch;
};

ControllerFillThreadCache& controllerFillThreadCache() {
    // TLS自身にはMaya資源や非自明なdestructorを持たせない。
    static thread_local ControllerFillThreadCache value{nullptr, 0};
    return value;
}

void controllerFillStateFailure() {
    controllerFillResources().healthy.store(false, std::memory_order_release);
}

bool controllerFillCanCleanupLocked(const ControllerFillResources& resources) {
    if (resources.activeDraws != 0 ||
        resources.shaderOwners.load(std::memory_order_acquire) != 0) return false;
    for (const auto& thread : resources.threads) if (!thread->saved.empty()) return false;
    return true;
}

MStatus controllerFillResourcesCanCleanup() {
    auto& resources = controllerFillResources();
    const std::lock_guard<std::mutex> lock(resources.mutex);
    return controllerFillCanCleanupLocked(resources) ? MS::kSuccess : MS::kFailure;
}

MStatus cleanupControllerFillResources() {
    auto& resources = controllerFillResources();
    const std::lock_guard<std::mutex> lock(resources.mutex);
    if (!controllerFillCanCleanupLocked(resources)) return MS::kFailure;
    resources.closed = true;
    ++resources.epoch;
    resources.shaders.clear();
    resources.threads.clear();
    resources.healthy.store(true, std::memory_order_release);
    return MS::kSuccess;
}

ControllerFillThreadState* controllerFillBeginDraw(
    MHWRender::MDrawContext& context, MHWRender::MShaderInstance* shader
) {
    auto& resources = controllerFillResources();
    const std::lock_guard<std::mutex> lock(resources.mutex);
    if (resources.closed) return nullptr;
    auto& cache = controllerFillThreadCache();
    if (!cache.state || cache.epoch != resources.epoch) {
        auto thread = std::make_unique<ControllerFillThreadState>();
        cache.state = thread.get();
        cache.epoch = resources.epoch;
        resources.threads.push_back(std::move(thread));
    }
    cache.state->saved.push_back({&context, shader, nullptr, nullptr});
    ++resources.activeDraws;
    return cache.state;
}

const MHWRender::MRasterizerState* controllerFillRasterState(
    ControllerFillThreadState& thread,
    const MHWRender::MRasterizerStateDesc& description
) {
    auto* renderer = MHWRender::MRenderer::theRenderer();
    if (!renderer) { controllerFillStateFailure(); return nullptr; }
    for (const auto& entry : thread.rasters) {
        if (entry->renderer == renderer &&
            controllerFillRasterSignature(entry->description) == controllerFillRasterSignature(description))
            return entry->state;
    }
    auto entry = std::make_unique<ControllerFillRasterState>();
    entry->renderer = renderer;
    entry->description = description;
    MStatus status;
    entry->state = MHWRender::MStateManager::acquireRasterizerState(description, &status);
    if (!status || !entry->state) { controllerFillStateFailure(); return nullptr; }
    const auto* state = entry->state;
    thread.rasters.push_back(std::move(entry));
    return state;
}

const MHWRender::MDepthStencilState* controllerFillDepthState(
    ControllerFillThreadState& thread,
    const MHWRender::MDepthStencilStateDesc& description
) {
    auto* renderer = MHWRender::MRenderer::theRenderer();
    if (!renderer) { controllerFillStateFailure(); return nullptr; }
    for (const auto& entry : thread.depths) {
        if (entry->renderer == renderer &&
            controllerFillDepthSignature(entry->description) == controllerFillDepthSignature(description))
            return entry->state;
    }
    auto entry = std::make_unique<ControllerFillDepthState>();
    entry->renderer = renderer;
    entry->description = description;
    MStatus status;
    entry->state = MHWRender::MStateManager::acquireDepthStencilState(description, &status);
    if (!status || !entry->state) { controllerFillStateFailure(); return nullptr; }
    const auto* state = entry->state;
    thread.depths.push_back(std::move(entry));
    return state;
}

void controllerFillPreDraw(
    MHWRender::MDrawContext& context, MHWRender::MShaderInstance* shader,
    bool singleSided, bool mirrored
) {
    auto* thread = controllerFillBeginDraw(context, shader);
    if (!thread) return;
    auto& saved = thread->saved.back();
    auto* manager = context.getStateManager();
    if (!manager) { controllerFillStateFailure(); return; }
    bool cullFront = false, cullBack = false;
    const auto& semantics = context.getPassContext().passSemantics();
    for (unsigned int i = 0; i < semantics.length(); ++i) {
        cullFront = cullFront || semantics[i] == MHWRender::MPassContext::kCullFrontSemantic;
        cullBack = cullBack || semantics[i] == MHWRender::MPassContext::kCullBackSemantic;
    }
    // 分割透明passのcullは保ち、片面で不要な裏面passだけを棄却する。
    if (cullFront || cullBack) {
        if (singleSided && cullFront) {
            MStatus status;
            saved.depth = manager->getDepthStencilState(&status);
            if (!status || !saved.depth) { controllerFillStateFailure(); return; }
            auto description = saved.depth->desc(&status);
            if (!status) { controllerFillStateFailure(); return; }
            description.depthEnable = true;
            description.depthWriteEnable = false;
            description.depthFunc = MHWRender::MStateManager::kCompareNever;
            description.stencilEnable = false;
            const auto* state = controllerFillDepthState(*thread, description);
            if (!state || !manager->setDepthStencilState(state)) controllerFillStateFailure();
        }
        return;
    }
    MStatus status;
    saved.raster = manager->getRasterizerState(&status);
    if (!status || !saved.raster) { controllerFillStateFailure(); return; }
    auto description = saved.raster->desc(&status);
    if (!status) { controllerFillStateFailure(); return; }
    description.cullMode = singleSided
        ? (mirrored ? MHWRender::MRasterizerState::kCullFront : MHWRender::MRasterizerState::kCullBack)
        : MHWRender::MRasterizerState::kCullNone;
    const auto* state = controllerFillRasterState(*thread, description);
    if (!state || !manager->setRasterizerState(state)) controllerFillStateFailure();
}

void controllerFillSinglePreDraw(
    MHWRender::MDrawContext& context, const MHWRender::MRenderItemList&,
    MHWRender::MShaderInstance* shader
) {
    controllerFillPreDraw(context, shader, true, false);
}

void controllerFillSingleMirroredPreDraw(
    MHWRender::MDrawContext& context, const MHWRender::MRenderItemList&,
    MHWRender::MShaderInstance* shader
) {
    controllerFillPreDraw(context, shader, true, true);
}

void controllerFillDoublePreDraw(
    MHWRender::MDrawContext& context, const MHWRender::MRenderItemList&,
    MHWRender::MShaderInstance* shader
) {
    controllerFillPreDraw(context, shader, false, false);
}

void controllerFillPostDraw(
    MHWRender::MDrawContext& context, const MHWRender::MRenderItemList&,
    MHWRender::MShaderInstance* shader
) {
    auto& resources = controllerFillResources();
    ControllerFillThreadState* thread = nullptr;
    {
        const std::lock_guard<std::mutex> lock(resources.mutex);
        const auto& cache = controllerFillThreadCache();
        if (cache.epoch == resources.epoch) thread = cache.state;
    }
    if (!thread) return;
    if (thread->saved.empty() || thread->saved.back().context != &context ||
        thread->saved.back().shader != shader) {
        // 未対応のdraw scopeは解放せず、DLL unloadを拒否できる状態を残す。
        controllerFillStateFailure();
        return;
    }
    const auto saved = thread->saved.back();
    auto* manager = context.getStateManager();
    if (saved.raster) {
        if (!manager || !manager->setRasterizerState(saved.raster)) controllerFillStateFailure();
        MHWRender::MStateManager::releaseRasterizerState(saved.raster);
    }
    if (saved.depth) {
        if (!manager || !manager->setDepthStencilState(saved.depth)) controllerFillStateFailure();
        MHWRender::MStateManager::releaseDepthStencilState(saved.depth);
    }
    thread->saved.pop_back();
    const std::lock_guard<std::mutex> lock(resources.mutex);
    --resources.activeDraws;
}

struct ControllerFillShaderData final : public MUserData {
    ControllerFillShaderData(
        MHWRender::MRenderer* valueRenderer, const MHWRender::MShaderManager* valueManager,
        MHWRender::MShaderInstance* valueShader, const MColor& valueColor,
        bool valueFill, bool valueSingleSided, bool valueMirrored
    ) : renderer(valueRenderer), manager(valueManager), shader(valueShader), color(valueColor),
        fill(valueFill), singleSided(valueSingleSided), mirrored(valueMirrored) {
        controllerFillResources().shaderOwners.fetch_add(1, std::memory_order_acq_rel);
    }

    ~ControllerFillShaderData() override {
        auto* current = MHWRender::MRenderer::theRenderer();
        if (shader && current == renderer && current && current->getShaderManager() == manager)
            manager->releaseShader(shader);
        controllerFillResources().shaderOwners.fetch_sub(1, std::memory_order_acq_rel);
    }

    MHWRender::MRenderer* renderer;
    const MHWRender::MShaderManager* manager;
    MHWRender::MShaderInstance* shader;
    MColor color;
    bool fill;
    bool singleSided;
    bool mirrored;
};

struct ControllerFillShader {
    MSharedPtr<ControllerFillShaderData> owner;
};

std::shared_ptr<ControllerFillShader> controllerFillShader(
    MHWRender::MRenderer* renderer, const MColor& color, bool fill, bool singleSided,
    bool mirrored
) {
    mirrored = fill && singleSided && mirrored;
    auto& resources = controllerFillResources();
    const std::lock_guard<std::mutex> lock(resources.mutex);
    const auto* manager = renderer ? renderer->getShaderManager() : nullptr;
    if (resources.closed || !manager) return nullptr;
    for (auto it = resources.shaders.begin(); it != resources.shaders.end();) {
        auto entry = it->lock();
        if (!entry) { it = resources.shaders.erase(it); continue; }
        const auto& data = *entry->owner;
        if (data.renderer == renderer && data.manager == manager && data.color == color &&
            data.fill == fill && data.singleSided == singleSided && data.mirrored == mirrored) return entry;
        ++it;
    }
    auto* shader = manager->getStockShader(
        MHWRender::MShaderManager::k3dSolidShader,
        fill ? (singleSided
            ? (mirrored ? controllerFillSingleMirroredPreDraw : controllerFillSinglePreDraw)
            : controllerFillDoublePreDraw) : nullptr,
        fill ? controllerFillPostDraw : nullptr
    );
    if (!shader) return nullptr;
    MColor shaderColor = color;
    if (fill) {
        shaderColor.r *= color.a;
        shaderColor.g *= color.a;
        shaderColor.b *= color.a;
    }
    if (!shader->setParameter("solidColor", &shaderColor.r) ||
        !shader->setIsTransparent(fill && color.a < 1.0f)) {
        manager->releaseShader(shader);
        return nullptr;
    }
    auto entry = std::make_shared<ControllerFillShader>();
    entry->owner = MSharedPtr<ControllerFillShaderData>::make(
        renderer, manager, shader, color, fill, singleSided, mirrored
    );
    resources.shaders.push_back(entry);
    return entry;
}

struct ControllerFillBatch {
    StrokeStyle style = StrokeStyle::Normal;
    bool fill = false;
    bool marker = false;
    bool singleSided = false;
    MString name;
    std::shared_ptr<MHWRender::MIndexBuffer> indices;
    std::shared_ptr<ControllerFillShader> shader;
    const MHWRender::MRenderItem* item = nullptr;
    bool bindingDirty = true;
};

struct ControllerFillBuffers {
    MHWRender::MRenderer* renderer = nullptr;
    std::shared_ptr<const BdControllerShapeDrawGeometry> geometry;
    std::shared_ptr<const BdControllerShapeDrawGeometry> strokeGeometry;
    std::shared_ptr<const BdControllerShapeDrawGeometry::Topology> topology;
    std::shared_ptr<const BdControllerShapeDrawGeometry::Topology> strokeTopology;
    std::unique_ptr<MHWRender::MVertexBuffer> vertices;
    std::vector<ControllerFillBatch> batches;
    MBoundingBox bounds;
    std::size_t fillCount = 0;
    std::size_t lineCount = 0;
    bool reversed = false;
    bool parityReady = false;
};

std::shared_ptr<MHWRender::MIndexBuffer> controllerFillIndexBuffer(
    const std::vector<unsigned int>& source
) {
    auto buffer = std::make_shared<MHWRender::MIndexBuffer>(MHWRender::MGeometry::kUnsignedInt32);
    auto* target = static_cast<unsigned int*>(buffer->acquire(static_cast<unsigned int>(source.size()), true));
    if (!target) return nullptr;
    std::copy(source.begin(), source.end(), target);
    buffer->commit(target);
    return buffer;
}

bool updateControllerFillBuffers(
    ControllerFillBuffers& value, MHWRender::MRenderer* renderer,
    const std::shared_ptr<const BdControllerShapeDrawGeometry>& geometry,
    const std::shared_ptr<const BdControllerShapeDrawGeometry>& strokeGeometry
) {
    std::size_t vertexCount = 0, indexCount = 0;
    for (const auto& points : strokeGeometry->strokes) vertexCount += points.length();
    for (const auto& points : geometry->fillParts) vertexCount += points.length();
    for (const auto& info : strokeGeometry->topology->strokes) indexCount += info.lineIndices.length();
    for (const auto& info : geometry->topology->fillParts) indexCount += info.triangleIndices.length();
    const auto maximum = std::numeric_limits<unsigned int>::max();
    if (vertexCount == 0 || vertexCount > maximum || indexCount > maximum) return false;
    const bool topologyChanged = value.topology != geometry->topology ||
        value.strokeTopology != strokeGeometry->topology;
    const bool parityChanged = !value.parityReady || value.reversed != geometry->reversed;
    const bool verticesChanged = value.geometry != geometry || value.strokeGeometry != strokeGeometry;
    std::vector<ControllerFillBatch> batches;
    std::size_t fillCount = value.fillCount, lineCount = value.lineCount;
    if (topologyChanged || parityChanged) {
        fillCount = lineCount = 0;
        std::vector<std::vector<unsigned int>> sources;
        std::size_t fillOffset = 0;
        for (const auto& points : strokeGeometry->strokes) fillOffset += points.length();
        const auto append = [&](bool fill, StrokeStyle style, bool marker, bool singleSided,
                                const MUintArray& source, std::size_t offset) {
            if (source.length() == 0) return;
            if (batches.empty() || batches.back().fill != fill || batches.back().style != style ||
                batches.back().marker != marker || batches.back().singleSided != singleSided) {
                ControllerFillBatch batch;
                batch.style = style;
                batch.fill = fill;
                batch.marker = marker;
                batch.singleSided = singleSided;
                const auto index = fill ? fillCount++ : lineCount++;
                batch.name = ((fill ? "bdControllerShapeFillSurface" : "bdControllerShapeFillLine") +
                    std::to_string(index)).c_str();
                batches.push_back(std::move(batch));
                sources.emplace_back();
            }
            auto& target = sources.back();
            target.reserve(target.size() + source.length());
            for (unsigned int i = 0; i < source.length(); ++i)
                target.push_back(static_cast<unsigned int>(offset) + source[i]);
        };
        std::size_t offset = fillOffset;
        for (std::size_t i = 0; i < geometry->fillParts.size(); ++i) {
            const auto& info = geometry->topology->fillParts[i];
            append(true, info.style, info.marker, info.singleSided, geometry->fillIndices(i), offset);
            offset += geometry->fillParts[i].length();
        }
        offset = 0;
        for (std::size_t i = 0; i < strokeGeometry->strokes.size(); ++i) {
            const auto& info = strokeGeometry->topology->strokes[i];
            append(false, info.style, false, false, info.lineIndices, offset);
            offset += strokeGeometry->strokes[i].length();
        }
        for (std::size_t i = 0; i < batches.size(); ++i) {
            auto& batch = batches[i];
            const auto previous = std::find_if(value.batches.begin(), value.batches.end(),
                [&](const auto& entry) {
                    return entry.name == batch.name && entry.fill == batch.fill && entry.style == batch.style &&
                        entry.marker == batch.marker && entry.singleSided == batch.singleSided;
                });
            if (previous != value.batches.end()) {
                batch.shader = previous->shader;
                batch.item = previous->item;
                if (!topologyChanged && (!batch.fill || !batch.singleSided || !parityChanged)) {
                    batch.indices = previous->indices;
                    batch.bindingDirty = false;
                }
            }
            if (!batch.indices) {
                batch.indices = controllerFillIndexBuffer(sources[i]);
                if (!batch.indices) return false;
            }
        }
    }
    if (verticesChanged) {
        if (!value.vertices) {
            const MHWRender::MVertexBufferDescriptor descriptor(
                "", MHWRender::MGeometry::kPosition, MHWRender::MGeometry::kFloat, 3
            );
            value.vertices = std::make_unique<MHWRender::MVertexBuffer>(descriptor);
        }
        auto* target = static_cast<float*>(value.vertices->acquire(static_cast<unsigned int>(vertexCount), true));
        if (!target) return false;
        MBoundingBox bounds;
        std::size_t offset = 0;
        const auto append = [&](const MPointArray& points) {
            for (unsigned int i = 0; i < points.length(); ++i) {
                const auto& point = points[i];
                target[offset++] = static_cast<float>(point.x);
                target[offset++] = static_cast<float>(point.y);
                target[offset++] = static_cast<float>(point.z);
                bounds.expand(point);
            }
        };
        for (const auto& points : strokeGeometry->strokes) append(points);
        for (const auto& points : geometry->fillParts) append(points);
        value.vertices->commit(target);
        value.bounds = bounds;
    }
    if (topologyChanged || parityChanged) value.batches = std::move(batches);
    value.renderer = renderer;
    value.geometry = geometry;
    value.strokeGeometry = strokeGeometry;
    value.topology = geometry->topology;
    value.strokeTopology = strokeGeometry->topology;
    value.reversed = geometry->reversed;
    value.parityReady = true;
    value.fillCount = fillCount;
    value.lineCount = lineCount;
    return true;
}

class ControllerShapeFill final {
public:
    explicit ControllerShapeFill(const MObject& node)
        : node_(node), ownerNode_(controllerShapeNode(node)) {
        auto& resources = controllerFillResources();
        const std::lock_guard<std::mutex> lock(resources.mutex);
        resources.closed = false;
    }

    bool active() const { return active_; }

    bool ownsItem(const MString& name) const {
        return std::find(fillNames_.begin(), fillNames_.end(), name) != fillNames_.end() ||
            std::find(lineNames_.begin(), lineNames_.end(), name) != lineNames_.end();
    }

    void suspend(MHWRender::MSubSceneContainer& container) {
        for (const auto* names : {&fillNames_, &lineNames_}) {
            for (const auto& name : *names) {
                if (auto* item = container.find(name); item && item->isEnabled()) item->enable(false);
            }
        }
        active_ = false;
        gateSnapshotReady_ = false;
    }

    bool requiresUpdate(
        const MHWRender::MSubSceneContainer& container,
        const MHWRender::MFrameContext& context, const ShapeDrawData* data,
        bool ready, bool uiDirty, bool visible
    ) const {
        if (!active_ || !ownerNode_ || !ready || uiDirty || !visible || !gateSnapshotReady_ || !data || !data->geometry ||
            !controllerFillResources().healthy.load(std::memory_order_acquire) ||
            !(context.getDisplayStyle() & MHWRender::MFrameContext::kSelectionHighlighting)) return true;
        MStatus status;
        MFnDagNode node(node_, &status);
        MDagPath path;
        if (!status || !node.getPath(path) || !path.isValid()) return true;
        const auto world = path.inclusiveMatrix(&status);
        if (!status || world != gateMatrix_) return true;
        if (wireIsPlaying() || MAnimControl::isScrubbing()) {
            timeNeedsUpdate_ = true;
            return true;
        }
        if (timeNeedsUpdate_ || MAnimControl::currentTime() != gateTime_) return true;
        const auto state = ownerNode_->wireUpdateState();
        if (!validGateState(state, *data) || state.revisions != gateRevisions_) return true;
        if (!path.isVisible(&status) || !status || !(path == gatePath_)) return true;
        WireGateContext nextContext;
        MMatrix view, projection;
        if (!nextContext.read(context) || !(nextContext == gateContext_) ||
            (context.getDisplayStyle() & gateStyleMask_) != gateStyle_ ||
            context.getTransparencyAlgorithm() != gateTransparency_ ||
            !readGateView(context, view, projection)) return true;
        auto* renderer = MHWRender::MRenderer::theRenderer();
        const auto* manager = renderer ? renderer->getShaderManager() : nullptr;
        const auto appearance = drawAppearance(*data, context.getDisplayStyle());
        const auto strokes = strokeGeometry(*data, appearance);
        if (!renderer || !manager || !buffers_ || !buffers_->vertices || !buffers_->topology ||
            !buffers_->strokeTopology || buffers_->renderer != renderer || !data->geometry ||
            buffers_->geometry != data->geometry->drawGeometry || buffers_->strokeGeometry != strokes ||
            !buffers_->parityReady || buffers_->reversed != buffers_->geometry->reversed) return true;
        for (const auto& batch : buffers_->batches) {
            const auto* item = container.find(batch.name);
            if (!item || item != batch.item || !batch.indices || batch.bindingDirty ||
                item->isEnabled() != enabled(batch, appearance) || !batch.shader || !batch.shader->owner) return true;
            const auto& shader = *batch.shader->owner;
            if (shader.renderer != renderer || shader.manager != manager || !shader.shader ||
                shader.color != batchColor(batch, appearance) ||
                item->getCustomData().get() != batch.shader->owner.get()) return true;
        }
        if (unusedItemsEnabled(container)) return true;
        const auto overrides = path.getDrawOverrideInfo();
        if (drawDisplayType(path, overrides) != MDAGDrawOverrideInfo::kDisplayTypeNormal ||
            wireOverrideSignature(overrides) != wireOverrideSignature(data->rawDrawOverrides) ||
            MHWRender::MGeometryUtilities::displayStatus(path) != data->rawDisplayStatus ||
            MHWRender::MGeometryUtilities::wireframeColor(path) != data->color) return true;
        return false;
    }

    void completeUpdate(
        const MHWRender::MFrameContext& context, const MDagPath& path, const ShapeDrawData& data
    ) {
        gateSnapshotReady_ = false;
        if (!active_ || !ownerNode_ ||
            !(context.getDisplayStyle() & MHWRender::MFrameContext::kSelectionHighlighting)) return;
        const bool moved = gateMatrix_ != matrix_;
        gateMatrix_ = matrix_;
        if (moved) return;
        if (wireIsPlaying() || MAnimControl::isScrubbing()) {
            timeNeedsUpdate_ = true;
            return;
        }
        const auto state = ownerNode_->wireUpdateState();
        MMatrix view, projection;
        if (!validGateState(state, data) || !gateContext_.read(context) ||
            !readGateView(context, view, projection)) return;
        gateRevisions_ = state.revisions;
        gateStyle_ = context.getDisplayStyle() & gateStyleMask_;
        gateTransparency_ = context.getTransparencyAlgorithm();
        gatePath_ = path;
        gateTime_ = MAnimControl::currentTime();
        timeNeedsUpdate_ = false;
        gateSnapshotReady_ = true;
    }

    bool update(
        MHWRender::MPxSubSceneOverride& owner, MHWRender::MSubSceneContainer& container,
        const MHWRender::MFrameContext& context, const MDagPath& path, const ShapeDrawData& data
    ) {
        const auto fail = [&]() { suspend(container); return false; };
        if (!supported(path, context, data)) return fail();
        auto* renderer = MHWRender::MRenderer::theRenderer();
        if (!renderer || !renderer->getShaderManager()) return fail();
        const auto& geometry = data.geometry->drawGeometry;
        const auto appearance = drawAppearance(data, context.getDisplayStyle());
        const auto strokes = strokeGeometry(data, appearance);
        const bool topologyChanged = !buffers_ || buffers_->topology != geometry->topology ||
            buffers_->strokeTopology != strokes->topology;
        if (!buffers_ || buffers_->renderer != renderer || topologyChanged) suspend(container);
        if (!buffers_ || buffers_->renderer != renderer) buffers_ = std::make_unique<ControllerFillBuffers>();
        const bool verticesChanged = buffers_->geometry != geometry || buffers_->strokeGeometry != strokes;
        const bool parityChanged = !buffers_->parityReady || buffers_->reversed != geometry->reversed;
        if ((verticesChanged || topologyChanged || parityChanged) &&
            !updateControllerFillBuffers(*buffers_, renderer, geometry, strokes)) return fail();
        const auto matrix = path.inclusiveMatrix();
        const bool matrixChanged = !matrixReady_ || matrix_ != matrix;
        const bool mirrored = matrix.det3x3() < 0.0;
        for (auto& batch : buffers_->batches) {
            auto& names = batch.fill ? fillNames_ : lineNames_;
            if (std::find(names.begin(), names.end(), batch.name) == names.end()) names.push_back(batch.name);
            auto* item = container.find(batch.name);
            const bool created = item == nullptr;
            if (!item) {
                item = MHWRender::MRenderItem::Create(
                    batch.name, batch.fill ? MHWRender::MRenderItem::MaterialSceneItem
                        : MHWRender::MRenderItem::NonMaterialSceneItem,
                    batch.fill ? MHWRender::MGeometry::kTriangles : MHWRender::MGeometry::kLines
                );
                if (!item) return fail();
                item->setDrawMode(static_cast<MHWRender::MGeometry::DrawMode>(
                    MHWRender::MGeometry::kWireframe | MHWRender::MGeometry::kShaded |
                    MHWRender::MGeometry::kTextured
                ));
                item->setSelectionMask(MSelectionMask::kSelectLocators);
                item->setWantConsolidation(true);
                item->castsShadows(false);
                item->receivesShadows(false);
                item->setExcludedFromPostEffects(true);
                item->setExcludedFromDefaultMaterialOverride(true);
                if (!container.add(item)) { MHWRender::MRenderItem::Destroy(item); return fail(); }
            }
            const bool itemChanged = created || batch.item != item;
            const auto color = batchColor(batch, appearance);
            const bool expectedMirror = batch.fill && batch.singleSided && mirrored;
            const auto& current = batch.shader;
            if (itemChanged || !current || !current->owner || current->owner->renderer != renderer ||
                current->owner->manager != renderer->getShaderManager() || current->owner->color != color ||
                current->owner->mirrored != expectedMirror) {
                auto next = controllerFillShader(renderer, color, batch.fill, batch.singleSided, expectedMirror);
                if (!next || !item->setShader(next->owner->shader)) return fail();
                // callback元shaderはitemのcustom dataにも保持し、containerより先に解放しない。
                item->setCustomData(MSharedPtr<MUserData>(next->owner));
                batch.shader = std::move(next);
            }
            if (verticesChanged || batch.bindingDirty || itemChanged) {
                MHWRender::MVertexBufferArray vertices;
                vertices.addBuffer("positions", buffers_->vertices.get());
                if (!batch.indices ||
                    !owner.setGeometryForRenderItem(*item, vertices, *batch.indices, &buffers_->bounds)) {
                    buffers_->geometry.reset();
                    return fail();
                }
                batch.bindingDirty = false;
            }
            if ((matrixChanged || itemChanged) && !item->setMatrix(&matrix)) return fail();
            const auto priority = batch.fill ? MHWRender::MRenderItem::sDormantFilledDepthPriority
                : MHWRender::MRenderItem::sDormantWireDepthPriority;
            if (item->depthPriority() != priority) item->depthPriority(priority);
            const bool draw = enabled(batch, appearance);
            if (item->isEnabled() != draw) item->enable(draw);
            batch.item = item;
        }
        disableUnusedItems(container);
        matrix_ = matrix;
        matrixReady_ = true;
        active_ = true;
        return true;
    }

private:
    static constexpr unsigned int gateStyleMask_ =
        MHWRender::MFrameContext::kSelectionHighlighting | MHWRender::MFrameContext::kBoundingBox |
        MHWRender::MFrameContext::kGouraudShaded | MHWRender::MFrameContext::kFlatShaded;

    static bool enabled(const ControllerFillBatch& batch, const ShapeDrawAppearance& appearance) {
        return !batch.fill || batch.marker || appearance.shaded;
    }

    static MColor batchColor(const ControllerFillBatch& batch, const ShapeDrawAppearance& appearance) {
        const auto& color = batch.fill && !batch.marker ? appearance.fillColor : appearance.color;
        return axisStyledColor(batch.style, color, appearance.selected, appearance.axisDisplayType);
    }

    static std::shared_ptr<const BdControllerShapeDrawGeometry> strokeGeometry(
        const ShapeDrawData& data, const ShapeDrawAppearance& appearance
    ) {
        const auto& geometry = *data.geometry;
        return (!appearance.shaded || appearance.fillColor.a <= 0.0f) && geometry.wireframeGeometry
            ? geometry.wireframeGeometry->drawGeometry : geometry.drawGeometry;
    }

    bool unusedItemsEnabled(const MHWRender::MSubSceneContainer& container) const {
        for (std::size_t i = buffers_->fillCount; i < fillNames_.size(); ++i)
            if (const auto* item = container.find(fillNames_[i]); item && item->isEnabled()) return true;
        for (std::size_t i = buffers_->lineCount; i < lineNames_.size(); ++i)
            if (const auto* item = container.find(lineNames_[i]); item && item->isEnabled()) return true;
        return false;
    }

    void disableUnusedItems(MHWRender::MSubSceneContainer& container) const {
        for (std::size_t i = buffers_->fillCount; i < fillNames_.size(); ++i)
            if (auto* item = container.find(fillNames_[i]); item && item->isEnabled()) item->enable(false);
        for (std::size_t i = buffers_->lineCount; i < lineNames_.size(); ++i)
            if (auto* item = container.find(lineNames_[i]); item && item->isEnabled()) item->enable(false);
    }

    static bool validGateState(
        const BdControllerShapeNode::WireUpdateState& state, const ShapeDrawData& data
    ) {
        return state.ready && state.value == data.geometry.get() &&
            !state.connectedAnimation && !state.connectedBounds && data.connectedDisplayInputs == 0 &&
            state.revisions[3] != 0 && data.displayRevision == state.revisions[3] &&
            std::all_of(state.revisions.begin(), state.revisions.end(),
                [](std::uint64_t value) { return value != 0; });
    }

    static bool finiteColor(const MColor& color) {
        return std::isfinite(color.r) && std::isfinite(color.g) &&
            std::isfinite(color.b) && std::isfinite(color.a);
    }

    static bool validMatrix(const MMatrix& matrix) {
        for (unsigned int row = 0; row < 4; ++row) for (unsigned int column = 0; column < 4; ++column)
            if (!std::isfinite(matrix[row][column])) return false;
        return matrix[0][3] == 0.0 && matrix[1][3] == 0.0 && matrix[2][3] == 0.0 &&
            matrix[3][3] == 1.0 && !matrix.isSingular();
    }

    static bool readGateView(
        const MHWRender::MFrameContext& context, MMatrix& view, MMatrix& projection
    ) {
        MStatus status;
        view = context.getMatrix(MHWRender::MFrameContext::kViewMtx, &status);
        if (!status || !validMatrix(view) || view.det3x3() <= 0.0) return false;
        projection = context.getMatrix(MHWRender::MFrameContext::kProjectionMtx, &status);
        if (!status) return false;
        for (unsigned int row = 0; row < 4; ++row) for (unsigned int column = 0; column < 4; ++column)
            if (!std::isfinite(projection[row][column])) return false;
        return true;
    }

    static bool validDrawGeometry(const BdControllerShapeDrawGeometry& draw) {
        if (!draw.topology || draw.topology->templateStyled ||
            draw.topology->strokes.size() != draw.strokes.size() ||
            draw.topology->fillParts.size() != draw.fillParts.size()) return false;
        const auto maximum = std::numeric_limits<unsigned int>::max();
        std::size_t vertices = 0, indices = 0;
        const auto pointsValid = [&](const MPointArray& points) {
            vertices += points.length();
            if (vertices > maximum) return false;
            for (unsigned int i = 0; i < points.length(); ++i) {
                const auto& point = points[i];
                if (point.w != 1.0 || !std::isfinite(static_cast<float>(point.x)) ||
                    !std::isfinite(static_cast<float>(point.y)) ||
                    !std::isfinite(static_cast<float>(point.z))) return false;
            }
            return true;
        };
        for (std::size_t i = 0; i < draw.strokes.size(); ++i) {
            const auto& info = draw.topology->strokes[i];
            if (info.style == StrokeStyle::Template || info.style >= StrokeStyle::Count ||
                info.lineIndices.length() % 2 != 0 || !pointsValid(draw.strokes[i])) return false;
            indices += info.lineIndices.length();
            if (indices > maximum) return false;
            for (unsigned int j = 0; j < info.lineIndices.length(); ++j)
                if (info.lineIndices[j] >= draw.strokes[i].length()) return false;
        }
        for (std::size_t i = 0; i < draw.fillParts.size(); ++i) {
            const auto& info = draw.topology->fillParts[i];
            const auto& source = draw.fillIndices(i);
            if (info.style == StrokeStyle::Template || info.style >= StrokeStyle::Count ||
                source.length() % 3 != 0 || !pointsValid(draw.fillParts[i])) return false;
            indices += source.length();
            if (indices > maximum) return false;
            for (unsigned int j = 0; j < source.length(); ++j)
                if (source[j] >= draw.fillParts[i].length()) return false;
        }
        return true;
    }

    static bool validGeometry(const BdControllerShapeNode::Geometry& geometry) {
        if (!geometry.drawGeometry || !geometry.drawGeometry->topology ||
            !geometry.boundsPreview.empty() || geometry.offsetLine.length() != 0) return false;
        bool hasFill = false;
        for (const auto& part : geometry.drawGeometry->topology->fillParts)
            hasFill = hasFill || part.triangleIndices.length() != 0;
        if (!hasFill || !validDrawGeometry(*geometry.drawGeometry)) return false;
        return !geometry.wireframeGeometry || (geometry.wireframeGeometry->drawGeometry &&
            validDrawGeometry(*geometry.wireframeGeometry->drawGeometry));
    }

    bool supported(
        const MDagPath& path, const MHWRender::MFrameContext& context, const ShapeDrawData& data
    ) {
        // 面のない線形状は、描画先や表示設定を照会する前に除外する。
        if (!data.geometry || !data.geometry->drawGeometry ||
            data.geometry->drawGeometry->fillParts.empty()) return false;
        if (!ownerNode_ || !path.isValid() || !data.geometry || data.lineWidth != 1.0f ||
            data.opacity != 1.0f || data.drawOnTop || data.activeTemplate || data.boundingBoxLOD ||
            data.displayType != MDAGDrawOverrideInfo::kDisplayTypeNormal ||
            !controllerFillResources().healthy.load(std::memory_order_acquire) ||
            (context.getDisplayStyle() & MHWRender::MFrameContext::kBoundingBox) ||
            (context.objectTypeExclusions() & MHWRender::MFrameContext::kExcludePluginShapes)) return false;
        MString destination;
        if (context.renderingDestination(destination) != MHWRender::MFrameContext::k3dViewport) return false;
        const auto appearance = drawAppearance(data, context.getDisplayStyle());
        if (appearance.color.a != 1.0f || !finiteColor(appearance.color) || !finiteColor(appearance.fillColor) ||
            appearance.fillColor.a < 0.0f || appearance.fillColor.a > 1.0f) return false;
        if (checkedGeometry_ != data.geometry) {
            geometryEligible_ = validGeometry(*data.geometry);
            checkedGeometry_ = data.geometry;
        }
        if (!geometryEligible_) return false;
        const auto& topology = data.geometry->drawGeometry->topology;
        if (attachmentTopology_ != topology) {
            attachmentSettingsValid_ = true;
            coloredAttachments_ = false;
            const bool coloredSurface = std::any_of(topology->fillParts.begin(), topology->fillParts.end(),
                [](const auto& part) {
                    return !part.marker && part.style != StrokeStyle::Normal &&
                        part.triangleIndices.length() != 0;
                });
            // 静的topologyの変更時だけ読み、行列アニメーションでは再照会しない。
            if (coloredSurface) {
                MStatus partStatus, finStatus;
                const bool part = MPlug(node_, BdControllerShapeNode::shapePart).asBool(&partStatus);
                const bool fin = MPlug(node_, BdControllerShapeNode::shapeFin).asBool(&finStatus);
                attachmentSettingsValid_ = partStatus && finStatus;
                coloredAttachments_ = part || fin;
            }
            attachmentTopology_ = topology;
        }
        // 複数色の半透明面と付属形状の重なりは、従来UIの描画順を保つ。
        if (!attachmentSettingsValid_ || (coloredAttachments_ &&
            appearance.fillColor.a > 0.0f && appearance.fillColor.a < 1.0f)) return false;
        MStatus status;
        const auto world = path.inclusiveMatrix(&status);
        if (!status || !validMatrix(world) || !validMatrix(data.geometry->drawGeometry->animationMatrix)) return false;
        const auto view = context.getMatrix(MHWRender::MFrameContext::kViewMtx, &status);
        return status && validMatrix(view) && view.det3x3() > 0.0;
    }

    MObject node_;
    const BdControllerShapeNode* ownerNode_;
    std::shared_ptr<const BdControllerShapeNode::Geometry> checkedGeometry_;
    std::shared_ptr<const BdControllerShapeDrawGeometry::Topology> attachmentTopology_;
    std::unique_ptr<ControllerFillBuffers> buffers_;
    std::vector<MString> fillNames_;
    std::vector<MString> lineNames_;
    MMatrix matrix_;
    bool geometryEligible_ = false;
    bool attachmentSettingsValid_ = true;
    bool coloredAttachments_ = false;
    bool matrixReady_ = false;
    bool active_ = false;
    WireGateContext gateContext_;
    std::array<std::uint64_t, 4> gateRevisions_{};
    MMatrix gateMatrix_;
    MDagPath gatePath_;
    MTime gateTime_;
    unsigned int gateStyle_ = 0;
    MHWRender::MFrameContext::TransparencyAlgorithm gateTransparency_ = MHWRender::MFrameContext::kUnsorted;
    bool gateSnapshotReady_ = false;
    mutable bool timeNeedsUpdate_ = true;
};
