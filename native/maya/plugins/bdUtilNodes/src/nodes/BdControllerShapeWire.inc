// 焼込み済みの線を順序と配色を保って保持し、未変更時の更新を省く。
class WirePlaybackNotification final {
public:
    MStatus start() {
        // remove失敗で残ったIDは捨てず、状態不明なら従来queryへ戻す。
        value_.store(unknown, std::memory_order_release);
        if (callback_ != 0) return MS::kFailure;
        const MString condition("playingBack");
        MStatus status;
        callback_ = MConditionMessage::addConditionCallback(condition, changed, this, &status);
        if (!status || callback_ == 0) {
            stop();
            return MS::kFailure;
        }
        const bool initial = MConditionMessage::getConditionState(condition, &status);
        if (!status) {
            stop();
            return status;
        }
        int expected = unknown;
        // 登録直後のcallbackが先着していた場合は、初期queryで上書きしない。
        value_.compare_exchange_strong(expected, initial ? 1 : 0, std::memory_order_acq_rel);
        return MS::kSuccess;
    }

    MStatus stop() {
        value_.store(unknown, std::memory_order_release);
        if (callback_ == 0) return MS::kSuccess;
        const auto status = MMessage::removeCallback(callback_);
        if (status) callback_ = 0;
        value_.store(unknown, std::memory_order_release);
        return status;
    }

    bool isPlaying() const {
        const int value = value_.load(std::memory_order_acquire);
        return value == unknown ? MAnimControl::isPlaying() : value != 0;
    }

private:
    static void changed(bool playing, void* clientData) {
        static_cast<WirePlaybackNotification*>(clientData)->value_.store(
            playing ? 1 : 0, std::memory_order_release
        );
    }

    static constexpr int unknown = -1;
    std::atomic<int> value_{unknown};
    MCallbackId callback_ = 0;
};

WirePlaybackNotification& wirePlaybackNotification() {
    static WirePlaybackNotification notification;
    return notification;
}

bool wireIsPlaying() {
    return wirePlaybackNotification().isPlaying();
}

struct WireShader {
    MHWRender::MRenderer* renderer = nullptr;
    const MHWRender::MShaderManager* manager = nullptr;
    MHWRender::MShaderInstance* shader = nullptr;
    MColor color;

    ~WireShader() {
        auto* current = MHWRender::MRenderer::theRenderer();
        if (shader && current == renderer && current &&
            current->getShaderManager() == manager) manager->releaseShader(shader);
    }
};

std::shared_ptr<WireShader> wireShader(
    MHWRender::MRenderer* renderer, const MColor& color
) {
    static std::vector<std::weak_ptr<WireShader>> cache;
    static std::mutex mutex;
    const std::lock_guard<std::mutex> lock(mutex);
    const auto* manager = renderer ? renderer->getShaderManager() : nullptr;
    if (!manager) return nullptr;
    for (auto it = cache.begin(); it != cache.end();) {
        auto value = it->lock();
        if (!value) { it = cache.erase(it); continue; }
        if (value->renderer == renderer && value->manager == manager &&
            value->color == color) return value;
        ++it;
    }
    auto* shader = manager->getStockShader(MHWRender::MShaderManager::k3dSolidShader);
    if (!shader) return nullptr;
    if (!shader->setParameter("solidColor", &color.r)) {
        manager->releaseShader(shader);
        return nullptr;
    }
    auto value = std::make_shared<WireShader>();
    value->renderer = renderer;
    value->manager = manager;
    value->shader = shader;
    value->color = color;
    cache.push_back(value);
    return value;
}

struct WireBatch {
    StrokeStyle style = StrokeStyle::Normal;
    std::unique_ptr<MHWRender::MIndexBuffer> indices;
    std::shared_ptr<WireShader> shader;
    const MHWRender::MRenderItem* item = nullptr;
};

struct WireBuffers {
    MHWRender::MRenderer* renderer = nullptr;
    std::shared_ptr<const BdControllerShapeDrawGeometry> geometry;
    std::shared_ptr<const BdControllerShapeDrawGeometry::Topology> topology;
    std::unique_ptr<MHWRender::MVertexBuffer> vertices;
    std::vector<WireBatch> batches;
    MBoundingBox bounds;
};

bool updateWireBuffers(
    WireBuffers& value,
    MHWRender::MRenderer* renderer,
    const std::shared_ptr<const BdControllerShapeDrawGeometry>& geometry
) {
    if (!value.vertices) {
        const MHWRender::MVertexBufferDescriptor descriptor(
            "", MHWRender::MGeometry::kPosition, MHWRender::MGeometry::kFloat, 3
        );
        value.vertices = std::make_unique<MHWRender::MVertexBuffer>(descriptor);
    }
    if (value.topology != geometry->topology) {
        std::vector<WireBatch> batches;
        std::vector<std::vector<unsigned int>> indices;
        unsigned int offset = 0;
        // 連続する同styleの線だけをまとめ、交差位置の配色順を変えない。
        for (std::size_t i = 0; i < geometry->strokes.size(); ++i) {
            const auto& info = geometry->topology->strokes[i];
            if (info.lineIndices.length() != 0) {
                if (batches.empty() || batches.back().style != info.style) {
                    batches.emplace_back();
                    batches.back().style = info.style;
                    indices.emplace_back();
                }
                auto& target = indices.back();
                target.reserve(target.size() + info.lineIndices.length());
                for (unsigned int j = 0; j < info.lineIndices.length(); ++j) {
                    target.push_back(offset + info.lineIndices[j]);
                }
            }
            offset += geometry->strokes[i].length();
        }
        for (std::size_t i = 0; i < batches.size(); ++i) {
            auto buffer = std::make_unique<MHWRender::MIndexBuffer>(
                MHWRender::MGeometry::kUnsignedInt32
            );
            const auto& source = indices[i];
            auto* target = static_cast<unsigned int*>(buffer->acquire(
                static_cast<unsigned int>(source.size()), true
            ));
            if (!target) return false;
            std::copy(source.begin(), source.end(), target);
            buffer->commit(target);
            batches[i].indices = std::move(buffer);
        }
        value.batches = std::move(batches);
        value.topology = geometry->topology;
    }
    unsigned int vertexCount = 0;
    for (const auto& stroke : geometry->strokes) vertexCount += stroke.length();
    auto* vertices = static_cast<float*>(value.vertices->acquire(vertexCount, true));
    if (!vertices) return false;
    MBoundingBox bounds;
    std::size_t offset = 0;
    for (const auto& stroke : geometry->strokes) {
        for (unsigned int i = 0; i < stroke.length(); ++i) {
            const auto& point = stroke[i];
            vertices[offset++] = static_cast<float>(point.x);
            vertices[offset++] = static_cast<float>(point.y);
            vertices[offset++] = static_cast<float>(point.z);
            bounds.expand(point);
        }
    }
    value.vertices->commit(vertices);
    value.renderer = renderer;
    value.geometry = geometry;
    value.bounds = bounds;
    return true;
}

auto wireOverrideSignature(const MDAGDrawOverrideInfo& value) {
    return std::make_tuple(
        value.fOverrideEnabled, value.fDisplayType, value.fLOD,
        value.fEnableShading, value.fEnableTexturing,
        value.fEnableVisible, value.fPlaybackVisible
    );
}

struct WireGateContext {
    unsigned int style = 0;
    MUint64 exclusions = 0;

    bool read(const MHWRender::MFrameContext& context) {
        MString destination;
        if (context.renderingDestination(destination) != MHWRender::MFrameContext::k3dViewport) return false;
        // 線が参照する表示bitだけ比較し、camera適用はMayaへ委譲する。
        style = context.getDisplayStyle() & (
            MHWRender::MFrameContext::kSelectionHighlighting |
            MHWRender::MFrameContext::kBoundingBox
        );
        exclusions = context.objectTypeExclusions() & MHWRender::MFrameContext::kExcludePluginShapes;
        return true;
    }

    bool operator==(const WireGateContext& other) const {
        return std::tie(style, exclusions) == std::tie(other.style, other.exclusions);
    }
};

std::size_t& controllerWireOwners() {
    static std::size_t owners = 0;
    return owners;
}

std::mutex& controllerWireMutex() {
    static std::mutex mutex;
    return mutex;
}

class ControllerShapeWire final {
public:
    explicit ControllerShapeWire(const MObject& node)
        : node_(node), ownerNode_(controllerShapeNode(node)) {
        const std::lock_guard<std::mutex> lock(controllerWireMutex());
        auto& owners = controllerWireOwners();
        if (owners == 0) wirePlaybackNotification().start();
        ++owners;
    }

    ~ControllerShapeWire() {
        const std::lock_guard<std::mutex> lock(controllerWireMutex());
        auto& owners = controllerWireOwners();
        --owners;
        if (owners == 0) wirePlaybackNotification().stop();
    }

    bool ownsItem(const MString& name) const {
        return std::find(itemNames_.begin(), itemNames_.end(), name) != itemNames_.end();
    }

    bool active() const { return active_; }

    bool requiresUpdate(
        const MHWRender::MSubSceneContainer& container,
        const MHWRender::MFrameContext& context, const ShapeDrawData* data,
        bool ready, bool uiDirty, bool visible
    ) const {
        if (!active_ || !ready || uiDirty || !visible || !gateSnapshotReady_ || !data ||
            !(context.getDisplayStyle() & MHWRender::MFrameContext::kSelectionHighlighting)) return true;
        MStatus status;
        MFnDagNode node(node_, &status);
        MDagPath currentPath;
        if (!status || !node.getPath(currentPath) || !currentPath.isValid()) return true;
        const auto world = currentPath.inclusiveMatrix(&status);
        if (!status || world != gateMatrix_) return true;
        // 再生・scrubの通知省略を推測せず、停止後も最初の完全更新を必ず通す。
        if (wireIsPlaying() || MAnimControl::isScrubbing()) {
            timeNeedsUpdate_ = true;
            return true;
        }
        if (timeNeedsUpdate_ || MAnimControl::currentTime() != gateTime_) return true;
        const auto state = ownerNode_->wireUpdateState();
        if (!validState(state, *data) || state.revisions[0] != settingsRevision_.first ||
            state.revisions[2] != settingsRevision_.second) return true;
        if (!currentPath.isVisible(&status) || !status || !(currentPath == gatePath_)) return true;

        // worldが変わる親操作では、appearance queryを重ねず従来更新へ戻す。
        auto* renderer = MHWRender::MRenderer::theRenderer();
        const auto* manager = renderer ? renderer->getShaderManager() : nullptr;
        if (!renderer || !manager || !buffers_ || !buffers_->vertices ||
            !buffers_->geometry || !buffers_->topology || buffers_->renderer != renderer ||
            buffers_->batches.empty() || buffers_->batches.size() > itemNames_.size()) return true;
        for (std::size_t i = 0; i < buffers_->batches.size(); ++i) {
            const auto& batch = buffers_->batches[i];
            const auto* item = container.find(itemNames_[i]);
            if (!batch.shader || batch.shader->renderer != renderer ||
                batch.shader->manager != manager || !batch.indices ||
                !item || item != batch.item || !item->isEnabled()) return true;
        }
        for (std::size_t i = buffers_->batches.size(); i < itemNames_.size(); ++i) {
            if (const auto* item = container.find(itemNames_[i]); item && item->isEnabled()) return true;
        }
        const auto overrides = currentPath.getDrawOverrideInfo();
        if (drawDisplayType(currentPath, overrides) != MDAGDrawOverrideInfo::kDisplayTypeNormal ||
            wireOverrideSignature(overrides) != wireOverrideSignature(data->rawDrawOverrides) ||
            MHWRender::MGeometryUtilities::displayStatus(currentPath) != data->rawDisplayStatus ||
            MHWRender::MGeometryUtilities::wireframeColor(currentPath) != data->color) return true;
        WireGateContext nextContext;
        if (!nextContext.read(context) || !(nextContext == gateContext_)) return true;
        return false;
    }

    void completeUpdate(
        const MHWRender::MSubSceneContainer&,
        const MHWRender::MFrameContext& context, const ShapeDrawData&
    ) {
        gateSnapshotReady_ = false;
        if (!active_ || !ownerNode_ ||
            !(context.getDisplayStyle() & MHWRender::MFrameContext::kSelectionHighlighting)) return;
        // 未arm中も直近の完全更新行列を保ち、静止した完全更新後だけ省略を再開する。
        const bool moved = gateMatrix_ != matrix_;
        gateMatrix_ = matrix_;
        if (moved) return;
        if (wireIsPlaying() || MAnimControl::isScrubbing()) {
            timeNeedsUpdate_ = true;
            return;
        }
        if (!gateContext_.read(context)) return;
        gatePath_ = path_;
        gateTime_ = MAnimControl::currentTime();
        timeNeedsUpdate_ = false;
        gateSnapshotReady_ = true;
    }

    void suspend(MHWRender::MSubSceneContainer& container) {
        for (const auto& name : itemNames_) {
            if (auto* item = container.find(name); item && item->isEnabled()) item->enable(false);
        }
        active_ = false;
        gateSnapshotReady_ = false;
    }

    bool update(
        MHWRender::MPxSubSceneOverride& owner,
        MHWRender::MSubSceneContainer& container,
        const MHWRender::MFrameContext& context,
        const MDagPath& path, const ShapeDrawData& data
    ) {
        path_ = path;
        const auto fail = [&]() {
            suspend(container);
            return false;
        };
        if (!staticEligible()) return fail();
        const auto appearance = drawAppearance(data, context.getDisplayStyle());
        if (!data.geometry || data.lineWidth != 1.0f || data.opacity != 1.0f ||
            data.drawOnTop || data.activeTemplate || data.boundingBoxLOD ||
            data.displayType != MDAGDrawOverrideInfo::kDisplayTypeNormal ||
            appearance.color.a != 1.0f ||
            (context.getDisplayStyle() & MHWRender::MFrameContext::kBoundingBox) ||
            (context.objectTypeExclusions() & MHWRender::MFrameContext::kExcludePluginShapes)) {
            return fail();
        }
        const auto& geometry = data.geometry->drawGeometry;
        if (checkedGeometry_ != data.geometry) {
            geometryEligible_ = eligibleGeometry(*data.geometry);
            checkedGeometry_ = data.geometry;
        }
        if (!geometryEligible_) return fail();
        auto* renderer = MHWRender::MRenderer::theRenderer();
        if (!renderer) return fail();
        const auto* manager = renderer->getShaderManager();
        if (!manager) return fail();
        // 前形状のitemを止めてから、そのindexとshaderの保持を入れ替える。
        if (!buffers_ || buffers_->renderer != renderer ||
            buffers_->topology != geometry->topology) suspend(container);
        if (!buffers_ || buffers_->renderer != renderer) buffers_ = std::make_unique<WireBuffers>();
        const bool geometryChanged = buffers_->geometry != geometry;
        if (geometryChanged && !updateWireBuffers(*buffers_, renderer, geometry)) return fail();
        const auto matrix = path.inclusiveMatrix();
        const bool matrixChanged = !matrixReady_ || matrix_ != matrix;
        for (std::size_t i = 0; i < buffers_->batches.size(); ++i) {
            auto& batch = buffers_->batches[i];
            if (i == itemNames_.size()) {
                itemNames_.emplace_back(("bdControllerShapeWire" + std::to_string(i)).c_str());
            }
            auto* item = container.find(itemNames_[i]);
            const bool created = item == nullptr;
            if (!item) {
                item = MHWRender::MRenderItem::Create(
                    itemNames_[i], MHWRender::MRenderItem::NonMaterialSceneItem,
                    MHWRender::MGeometry::kLines
                );
                if (!item) return fail();
                item->setDrawMode(static_cast<MHWRender::MGeometry::DrawMode>(
                    MHWRender::MGeometry::kWireframe | MHWRender::MGeometry::kShaded |
                    MHWRender::MGeometry::kTextured
                ));
                item->setSelectionMask(MSelectionMask::kSelectLocators);
                // PluginShapes除外はviewごとにUI経路へ戻し、共有itemの除外flagへ依存しない。
                item->setWantConsolidation(true);
                item->castsShadows(false);
                item->receivesShadows(false);
                item->setExcludedFromPostEffects(true);
                item->setExcludedFromDefaultMaterialOverride(true);
                if (!container.add(item)) {
                    MHWRender::MRenderItem::Destroy(item);
                    return fail();
                }
            }
            const bool itemChanged = created || batch.item != item;
            const auto color = axisStyledColor(
                batch.style, appearance.color, appearance.selected, appearance.axisDisplayType
            );
            if (itemChanged || !batch.shader || batch.shader->renderer != renderer ||
                batch.shader->manager != manager || batch.shader->color != color) {
                auto shader = wireShader(renderer, color);
                if (!shader || !item->setShader(shader->shader)) return fail();
                batch.shader = std::move(shader);
            }
            if (geometryChanged || itemChanged) {
                MHWRender::MVertexBufferArray vertices;
                vertices.addBuffer("positions", buffers_->vertices.get());
                if (!owner.setGeometryForRenderItem(
                        *item, vertices, *batch.indices, &buffers_->bounds)) {
                    buffers_->geometry.reset();
                    return fail();
                }
            }
            if ((matrixChanged || itemChanged) && !item->setMatrix(&matrix)) return fail();
            const auto depth = MHWRender::MRenderItem::sDormantWireDepthPriority;
            if (item->depthPriority() != depth) item->depthPriority(depth);
            if (!item->isEnabled()) item->enable(true);
            batch.item = item;
        }
        for (std::size_t i = buffers_->batches.size(); i < itemNames_.size(); ++i) {
            if (auto* item = container.find(itemNames_[i]); item && item->isEnabled()) item->enable(false);
        }
        matrix_ = matrix;
        matrixReady_ = true;
        active_ = true;
        return true;
    }

private:
    static bool validState(
        const BdControllerShapeNode::WireUpdateState& state, const ShapeDrawData& data
    ) {
        return state.ready && state.value == data.geometry.get() &&
            !state.connectedAnimation && !state.connectedBounds &&
            data.connectedDisplayInputs == 0 && state.revisions[3] != 0 &&
            data.displayRevision == state.revisions[3] &&
            std::all_of(state.revisions.begin(), state.revisions.end(),
                [](std::uint64_t value) { return value != 0; });
    }

    bool staticEligible() {
        if (!ownerNode_) return false;
        const auto revision = ownerNode_->wireSettingsRevision();
        if (revision.first == 0 || revision.second == 0) return false;
        if (settingsReady_ && settingsRevision_ == revision) return staticEligible_;
        settingsRevision_ = revision;
        settingsReady_ = true;
        staticEligible_ = true;
        MStatus status;
        const std::array<MObject, 14> flags = {
            BdControllerShapeNode::shapeWide,
            BdControllerShapeNode::shapeTemplateLine, BdControllerShapeNode::shapeTemplateLineInvert,
            BdControllerShapeNode::shapeTemplateFill, BdControllerShapeNode::shapePartTemplate,
            BdControllerShapeNode::shapeFinTemplate, BdControllerShapeNode::shapeGuideLineTemplate,
            BdControllerShapeNode::shapeFill, BdControllerShapeNode::shapePart,
            BdControllerShapeNode::shapeFin, BdControllerShapeNode::shapeGuideLine,
            BdControllerShapeNode::shapeOffsetLine, BdControllerShapeNode::shapeOffsetLineTemplate,
            BdControllerShapeNode::showBoundsPreview,
        };
        for (const auto& flag : flags) {
            const bool value = MPlug(node_, flag).asBool(&status);
            staticEligible_ = staticEligible_ && status && !value;
        }
        return staticEligible_;
    }

    static bool eligibleGeometry(const BdControllerShapeNode::Geometry& geometry) {
        const auto& draw = geometry.drawGeometry;
        if (!draw || !draw->topology || draw->strokes.empty() ||
            draw->topology->strokes.size() != draw->strokes.size() ||
            !draw->fillParts.empty() || !draw->topology->fillParts.empty() ||
            draw->topology->templateStyled || geometry.wireframeGeometry ||
            !geometry.boundsPreview.empty() || geometry.offsetLine.length() != 0) return false;
        const auto maximum = std::numeric_limits<unsigned int>::max();
        std::size_t vertices = 0;
        std::size_t indices = 0;
        for (std::size_t i = 0; i < draw->strokes.size(); ++i) {
            const auto& stroke = draw->topology->strokes[i];
            const auto& points = draw->strokes[i];
            if (stroke.style == StrokeStyle::Template || stroke.style >= StrokeStyle::Count ||
                stroke.lineIndices.length() % 2 != 0) return false;
            vertices += points.length();
            indices += stroke.lineIndices.length();
            if (vertices > maximum || indices > maximum) return false;
            for (unsigned int j = 0; j < stroke.lineIndices.length(); ++j) {
                if (stroke.lineIndices[j] >= points.length()) return false;
            }
            for (unsigned int j = 0; j < points.length(); ++j) {
                const auto& point = points[j];
                if (!std::isfinite(point.x) || !std::isfinite(point.y) ||
                    !std::isfinite(point.z) || point.w != 1.0) return false;
            }
        }
        return vertices != 0 && indices != 0;
    }

    MObject node_;
    const BdControllerShapeNode* ownerNode_;
    MDagPath path_;
    std::pair<std::uint64_t, std::uint64_t> settingsRevision_{0, 0};
    std::shared_ptr<const BdControllerShapeNode::Geometry> checkedGeometry_;
    std::unique_ptr<WireBuffers> buffers_;
    std::vector<MString> itemNames_;
    MMatrix matrix_;
    bool settingsReady_ = false;
    bool staticEligible_ = false;
    bool geometryEligible_ = false;
    bool active_ = false;
    bool matrixReady_ = false;
    WireGateContext gateContext_;
    MMatrix gateMatrix_;
    MDagPath gatePath_;
    MTime gateTime_;
    bool gateSnapshotReady_ = false;
    mutable bool timeNeedsUpdate_ = true;
};
