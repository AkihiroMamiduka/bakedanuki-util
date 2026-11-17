#pragma once

namespace cubeResearch::profiling {
enum class Method {
    requiresGeometry, requiresRenderItems, updateDG, updateRenderItems,
    populateGeometry, indexingDirty, streamDirty, bounds, count
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

namespace cubeResearch::profiling {
inline std::atomic<bool> active{false};
inline std::array<std::atomic<unsigned long long>, static_cast<int>(Method::count)> calls{};
inline std::array<std::atomic<unsigned long long>, static_cast<int>(Method::count)> nanos{};

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
            active.store(true, std::memory_order_relaxed);
            return MS::kSuccess;
        }
        constexpr const char* names[] = {
            "requiresGeometry", "requiresRenderItems", "updateDG", "updateRenderItems",
            "populateGeometry", "indexingDirty", "streamDirty", "bounds"
        };
        std::ostringstream result;
        result << "{";
        for (int i = 0; i < static_cast<int>(Method::count); ++i) {
            if (i) result << ",";
            result << "\"" << names[i] << "\":{\"calls\":" << calls[i].load()
                << ",\"nanoseconds\":" << nanos[i].load() << "}";
        }
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
