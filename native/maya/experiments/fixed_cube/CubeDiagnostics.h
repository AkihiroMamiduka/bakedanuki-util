#pragma once

namespace cubeResearch::profiling {
enum class Method {
    requiresGeometry, requiresRenderItems, updateDG, updateRenderItems,
    populateGeometry, indexingDirty, streamDirty, bounds, matrixRead, geometryRebuild,
    subSceneRequiresUpdate, subSceneReadState, subSceneReadDisplayState, subSceneUpdate,
    subSceneSetMatrix, subSceneBindGeometry, subSceneUpdateShader, count
};
}

#ifdef BD_CUBE_PROFILE
#include <array>
#include <atomic>
#include <chrono>
#include <sstream>

#include <maya/MArgDatabase.h>
#include <maya/MPxCommand.h>
#include <maya/MSyntax.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MItDependencyNodes.h>
#include <maya/MViewport2Renderer.h>

#ifdef BD_CUBE_DRAW_PROFILE
#include <maya/MDrawContext.h>
#include <maya/MHWGeometry.h>
#include <maya/MShaderManager.h>
#include <maya/MStringArray.h>
#endif

namespace cubeResearch::profiling {
inline std::atomic<bool> active{false};
inline std::array<std::atomic<unsigned long long>, static_cast<int>(Method::count)> calls{};
inline std::array<std::atomic<unsigned long long>, static_cast<int>(Method::count)> nanos{};

#ifdef BD_CUBE_DRAW_PROFILE
enum class DrawMetric {
    callbacks, renderItems, nullItems, consolidatedItems, multiDrawItems,
    multiDrawContexts, mappedSourceGeometries, emptySourceMappings,
    colorPassCallbacks, selectionPassCallbacks, maxItemsPerCallback,
    maxSourcesPerItem, count
};
inline std::array<std::atomic<unsigned long long>, static_cast<int>(DrawMetric::count)> drawCounts{};

inline void addDrawCount(DrawMetric metric, unsigned long long value) {
    drawCounts[static_cast<int>(metric)].fetch_add(value, std::memory_order_relaxed);
}

inline void maxDrawCount(DrawMetric metric, unsigned long long value) {
    auto& counter = drawCounts[static_cast<int>(metric)];
    auto previous = counter.load(std::memory_order_relaxed);
    while (previous < value && !counter.compare_exchange_weak(
        previous, value, std::memory_order_relaxed)) {}
}

// 描画状態やDGへ触れず、callbackへ渡された描画項目だけを観測する。
// callback自体がbatchingへ影響する可能性があり、GPU draw call数や通常版の計時値ではない。
inline void recordDraw(MHWRender::MDrawContext& context,
    const MHWRender::MRenderItemList& items, MHWRender::MShaderInstance*) {
    if (!active.load(std::memory_order_relaxed)) return;
    addDrawCount(DrawMetric::callbacks, 1);
    if (context.isMultiDraw()) addDrawCount(DrawMetric::multiDrawContexts, 1);
    const auto& semantics = context.getPassContext().passSemantics();
    bool colorPass = false;
    bool selectionPass = false;
    for (unsigned int i = 0; i < semantics.length(); ++i) {
        colorPass |= semantics[i] == MHWRender::MPassContext::kColorPassSemantic;
        selectionPass |= semantics[i] == MHWRender::MPassContext::kSelectionPassSemantic;
    }
    if (colorPass) addDrawCount(DrawMetric::colorPassCallbacks, 1);
    if (selectionPass) addDrawCount(DrawMetric::selectionPassCallbacks, 1);
    const auto length = items.length();
    if (length > 0) maxDrawCount(DrawMetric::maxItemsPerCallback, length);
    for (int i = 0; i < length; ++i) {
        const auto* item = items.itemAt(i);
        if (!item) {
            addDrawCount(DrawMetric::nullItems, 1);
            continue;
        }
        addDrawCount(DrawMetric::renderItems, 1);
        if (item->isMultiDraw()) addDrawCount(DrawMetric::multiDrawItems, 1);
        if (item->isConsolidated()) {
            addDrawCount(DrawMetric::consolidatedItems, 1);
            MHWRender::MGeometryIndexMapping mapping;
            item->sourceIndexMapping(mapping);
            const auto sourceCount = mapping.geometryCount();
            if (sourceCount > 0) {
                addDrawCount(DrawMetric::mappedSourceGeometries, sourceCount);
                maxDrawCount(DrawMetric::maxSourcesPerItem, sourceCount);
            } else {
                addDrawCount(DrawMetric::emptySourceMappings, 1);
            }
        }
    }
}
#endif

class Scope {
public:
    explicit Scope(Method method) : method_(method), active_(active.load(std::memory_order_relaxed)) {
        if (active_) started_ = std::chrono::steady_clock::now();
    }
    ~Scope() {
        if (!active_) return;
        const auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(
            std::chrono::steady_clock::now() - started_).count();
        const auto index = static_cast<int>(method_);
        calls[index].fetch_add(1, std::memory_order_relaxed);
        nanos[index].fetch_add(static_cast<unsigned long long>(elapsed), std::memory_order_relaxed);
    }
private:
    Method method_;
    bool active_;
    std::chrono::steady_clock::time_point started_;
};

class Command final : public MPxCommand {
public:
    static void* creator() { return new Command; }
    static MSyntax syntaxCreator() {
        MSyntax value;
        value.addFlag("-r", "-reset");
        value.addFlag("-d", "-dirty");
        return value;
    }
    MStatus doIt(const MArgList& arguments) override {
        MStatus status;
        MArgDatabase args(MPxCommand::syntax(), arguments, &status);
        if (!status) return status;
        if (args.isFlagSet("-d")) {
            for (MItDependencyNodes it(MFn::kPluginLocatorNode); !it.isDone(); it.next()) {
                const auto node = it.thisNode();
                if (MFnDependencyNode(node).typeId().id() == 0x00142720)
                    MHWRender::MRenderer::setGeometryDrawDirty(node, true);
            }
            return MS::kSuccess;
        }
        active.store(false, std::memory_order_relaxed);
        if (args.isFlagSet("-r")) {
            for (auto& value : calls) value.store(0, std::memory_order_relaxed);
            for (auto& value : nanos) value.store(0, std::memory_order_relaxed);
#ifdef BD_CUBE_DRAW_PROFILE
            for (auto& value : drawCounts) value.store(0, std::memory_order_relaxed);
#endif
            active.store(true, std::memory_order_relaxed);
            return MS::kSuccess;
        }
        constexpr const char* names[] = {
            "requiresGeometry", "requiresRenderItems", "updateDG", "updateRenderItems",
            "populateGeometry", "indexingDirty", "streamDirty", "bounds",
            "matrixRead", "geometryRebuild",
            "subSceneRequiresUpdate", "subSceneReadState", "subSceneReadDisplayState",
            "subSceneUpdate", "subSceneSetMatrix", "subSceneBindGeometry", "subSceneUpdateShader"
        };
        static_assert(sizeof(names) / sizeof(*names) == static_cast<int>(Method::count));
        std::ostringstream result;
        result << "{";
        for (int i = 0; i < static_cast<int>(Method::count); ++i) {
            if (i) result << ",";
            result << "\"" << names[i] << "\":{\"calls\":" << calls[i].load()
                << ",\"nanoseconds\":" << nanos[i].load() << "}";
        }
#ifdef BD_CUBE_DRAW_PROFILE
        constexpr const char* drawNames[] = {
            "callbacks", "renderItems", "nullItems", "consolidatedItems", "multiDrawItems",
            "multiDrawContexts", "mappedSourceGeometries", "emptySourceMappings",
            "colorPassCallbacks", "selectionPassCallbacks", "maxItemsPerCallback", "maxSourcesPerItem"
        };
        result << ",\"draw_batches\":{\"schema_version\":1,"
            "\"measurement\":\"stock_shader_pre_draw_callback\",\"scope\":\"all_passes\","
            "\"gpu_draw_call_count\":false,\"performance_comparable\":false,"
            "\"may_change_batching\":true";
        for (int i = 0; i < static_cast<int>(DrawMetric::count); ++i) {
            result << ",\"" << drawNames[i] << "\":" << drawCounts[i].load();
        }
        result << "}";
#endif
        result << "}";
        setResult(MString(result.str().c_str()));
        return MS::kSuccess;
    }
};
}
#else
namespace cubeResearch::profiling {
class Scope {
public:
    explicit Scope(Method) {}
};
}
#endif
