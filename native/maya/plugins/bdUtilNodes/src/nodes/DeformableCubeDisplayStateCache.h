#pragma once

#include <algorithm>
#include <atomic>
#include <cstdint>
#include <memory>
#include <mutex>
#include <unordered_map>
#include <vector>

#include <maya/MCallbackIdArray.h>
#include <maya/MConditionMessage.h>
#include <maya/MDGMessage.h>
#include <maya/MDagMessage.h>
#include <maya/MDagPath.h>
#include <maya/MEventMessage.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MMessage.h>
#include <maya/MModelMessage.h>
#include <maya/MNodeMessage.h>
#include <maya/MObjectHandle.h>
#include <maya/MPlug.h>
#include <maya/MPlugArray.h>
#include <maya/MSceneMessage.h>

namespace bdUtilNodes::deformableCubeDisplay {
class NodeWatch;

inline void removeRegisteredCallbacks(MCallbackIdArray& callbacks) {
    for (unsigned int index = 0; index < callbacks.length(); ++index) {
        MMessage::removeCallback(callbacks[index]);
    }
    callbacks.clear();
}

class DisplayMonitor {
public:
    DisplayMonitor() {
        MStatus status;
        const auto selection = MModelMessage::addCallback(MModelMessage::kActiveListModified,
            displayChanged, this, &status);
        track(selection, status);
        const MString playbackCondition("playingBack");
        const auto playback = MConditionMessage::addConditionCallback(
            playbackCondition, playbackChanged, this, &status);
        if (status && playback != 0) {
            callbacks_.append(playback);
            const bool playing = MConditionMessage::getConditionState(playbackCondition, &status);
            if (status) {
                int expected = -1;
                playing_.compare_exchange_strong(expected, playing ? 1 : 0, std::memory_order_acq_rel);
            }
        }
        constexpr const char* events[] = {
            "PreSelectionChangedTriggered", "SelectModeChanged", "SelectTypeChanged",
            "DisplayColorChanged", "DisplayRGBColorChanged", "ColorIndexChanged",
            "displayLayerChange", "displayLayerManagerChange", "displayLayerVisibilityChanged",
            "renderLayerChange", "renderLayerManagerChange", "ActiveViewChanged", "Undo", "Redo",
        };
        for (const auto* event : events) {
            const auto id = MEventMessage::addEventCallback(event, displayChanged, this, &status);
            track(id, status);
        }
        const auto dag = MDagMessage::addAllDagChangesCallback(dagChanged, this, &status);
        track(dag, status);
        const auto connection = MDGMessage::addConnectionCallback(connectionChanged, this, &status);
        track(connection, status);
        const auto opened = MSceneMessage::addCallback(MSceneMessage::kAfterOpen,
            graphChanged, this, &status);
        track(opened, status);
        const auto created = MSceneMessage::addCallback(MSceneMessage::kAfterNew,
            graphChanged, this, &status);
        track(created, status);
    }

    ~DisplayMonitor();

    DisplayMonitor(const DisplayMonitor&) = delete;
    DisplayMonitor& operator=(const DisplayMonitor&) = delete;

    bool ready() const { return ready_; }
    bool isPlaying() const { return playing_.load(std::memory_order_acquire) == 1; }
    std::uint64_t displayRevision() const { return displayRevision_.load(std::memory_order_acquire); }
    std::uint64_t graphRevision() const { return graphRevision_.load(std::memory_order_acquire); }
    std::shared_ptr<NodeWatch> watch(MObject object);
    bool activateWatches(const std::vector<std::shared_ptr<NodeWatch>>& watches);

    void invalidateDisplay() { displayRevision_.fetch_add(1, std::memory_order_release); }

private:
    void track(MCallbackId id, const MStatus& status) {
        if (status) callbacks_.append(id);
        else ready_ = false;
    }

    static void playbackChanged(bool playing, void* data) {
        static_cast<DisplayMonitor*>(data)->playing_.store(playing ? 1 : 0, std::memory_order_release);
    }

    static void displayChanged(void* data) {
        static_cast<DisplayMonitor*>(data)->invalidateDisplay();
    }

    static void graphChanged(void* data) {
        auto& monitor = *static_cast<DisplayMonitor*>(data);
        monitor.graphRevision_.fetch_add(1, std::memory_order_release);
        monitor.invalidateDisplay();
    }

    static void dagChanged(MDagMessage::DagMessage, MDagPath&, MDagPath&, void* data) {
        graphChanged(data);
    }

    static void connectionChanged(MPlug&, MPlug&, bool, void* data) { graphChanged(data); }

    MCallbackIdArray callbacks_;
    // 状態が不明な間は通常経路を使う。
    std::atomic<int> playing_{-1};
    std::atomic<std::uint64_t> displayRevision_{1};
    std::atomic<std::uint64_t> graphRevision_{1};
    bool ready_ = true;
    std::mutex watchMutex_;
    std::unordered_multimap<unsigned int, std::weak_ptr<NodeWatch>> watches_;
    std::size_t nextPrune_ = 1024;
};

class NodeWatch {
public:
    NodeWatch(DisplayMonitor& monitor, MObject object) : monitor_(monitor), handle_(object) {
        MStatus status;
        const MFnDependencyNode node(object, &status);
        if (!status) return;
        constexpr const char* roots[] = {
            "visibility", "lodVisibility", "intermediateObject", "template", "ghosting",
            "drawOverride", "useObjectColor", "objectColor", "objectColorRGB", "wireColorRGB",
            "renderLayerInfo", "layerRenderable", "layerOverrideColor",
        };
        for (const auto* name : roots) {
            auto attribute = node.attribute(name, &status);
            if (status) attributes_.push_back(attribute);
        }
        attributesReady_ = true;
    }

    ~NodeWatch() { removeRegisteredCallbacks(callbacks_); }

    NodeWatch(const NodeWatch&) = delete;
    NodeWatch& operator=(const NodeWatch&) = delete;

    const MObjectHandle& handle() const { return handle_; }

    bool hasStaticDisplay() const {
        if (!attributesReady_ || !handle_.isValid()) return false;
        MStatus status;
        const MFnDependencyNode node(handle_.object(), &status);
        if (!status) return false;
        MPlugArray plugs;
        status = node.getConnections(plugs);
        // SDK は有効な未接続ノードについて MS::kFailure を返す。
        if (!status) return status == MS::kFailure && plugs.length() == 0;
        for (unsigned int i = 0; i < plugs.length(); ++i) {
            if (plugs[i].isDestination() && isDisplayPlug(plugs[i])) return false;
        }
        return true;
    }

private:
    friend class DisplayMonitor;

    void deactivate() {
        removeRegisteredCallbacks(callbacks_);
        callbacksReady_ = false;
    }

    bool activate() {
        if (activationAttempted_) return callbacksReady_;
        activationAttempted_ = true;
        if (!handle_.isValid()) return false;
        auto object = handle_.object();
        MStatus status;
        const auto changed = MNodeMessage::addAttributeChangedCallback(object, attributeChanged,
            this, &status);
        if (!status) return false;
        callbacks_.append(changed);
        const auto dirty = MNodeMessage::addNodeDirtyPlugCallback(object, plugDirtied, this, &status);
        if (!status) return false;
        callbacks_.append(dirty);
        callbacksReady_ = true;
        return true;
    }

    bool isDisplayPlug(MPlug plug) const {
        while (plug.isChild()) plug = plug.parent();
        return std::find(attributes_.begin(), attributes_.end(), plug.attribute()) != attributes_.end();
    }

    static void attributeChanged(MNodeMessage::AttributeMessage message, MPlug& plug,
        MPlug&, void* data) {
        if (message & MNodeMessage::kAttributeSet) invalidate(plug, data);
    }

    static void plugDirtied(MObject&, MPlug& plug, void* data) { invalidate(plug, data); }

    static void invalidate(const MPlug& plug, void* data) {
        auto& watch = *static_cast<NodeWatch*>(data);
        if (watch.isDisplayPlug(plug)) watch.monitor_.invalidateDisplay();
    }

    DisplayMonitor& monitor_;
    MObjectHandle handle_;
    std::vector<MObject> attributes_;
    MCallbackIdArray callbacks_;
    bool attributesReady_ = false;
    bool activationAttempted_ = false;
    bool callbacksReady_ = false;
};

inline DisplayMonitor::~DisplayMonitor() {
    removeRegisteredCallbacks(callbacks_);
    const std::lock_guard<std::mutex> lock(watchMutex_);
    // 表示キャッシュが残っていてもノードの通知を解除してから監視を破棄する。
    for (const auto& entry : watches_) {
        if (auto watcher = entry.second.lock()) watcher->deactivate();
    }
}

inline std::shared_ptr<NodeWatch> DisplayMonitor::watch(MObject object) {
    const std::lock_guard<std::mutex> lock(watchMutex_);
    if (watches_.size() >= nextPrune_) {
        for (auto it = watches_.begin(); it != watches_.end();) {
            if (it->second.expired()) it = watches_.erase(it);
            else ++it;
        }
        nextPrune_ = watches_.size() + 1024;
    }
    const MObjectHandle handle(object);
    const auto hash = handle.hashCode();
    const auto range = watches_.equal_range(hash);
    for (auto it = range.first; it != range.second; ++it) {
        if (auto existing = it->second.lock(); existing && existing->handle() == handle) {
            return existing;
        }
    }
    auto result = std::make_shared<NodeWatch>(*this, object);
    watches_.emplace(hash, result);
    return result;
}

inline bool DisplayMonitor::activateWatches(const std::vector<std::shared_ptr<NodeWatch>>& watches) {
    const std::lock_guard<std::mutex> lock(watchMutex_);
    for (const auto& watch : watches) {
        if (!watch->activate()) return false;
    }
    return true;
}

template <typename DisplayValues>
class DisplayCache {
public:
    bool canReuseWithoutStatus(const DisplayMonitor* monitor, unsigned int displayStyle) const {
        return monitor && monitor->ready() && cacheable_ && valid_ &&
            monitor->graphRevision() == graph_ && monitor->displayRevision() == appearance_ &&
            displayStyle == displayStyle_;
    }

    template <typename Probe>
    bool canReuse(const DisplayMonitor* monitor, unsigned int displayStyle, Probe probe) const {
        return canReuseWithoutStatus(monitor, displayStyle) &&
            static_cast<unsigned int>(probe()) == displayStatus_;
    }

    const DisplayValues& cachedValue() const { return value_; }

    template <typename Probe, typename Read>
    DisplayValues read(DisplayMonitor* monitor, const MDagPath& path, unsigned int displayStyle,
        Probe probe, Read readDisplay) {
        if (!monitor || !monitor->ready()) return readDisplay();
        const auto graph = monitor->graphRevision();
        if (graph != graph_ || !(path == path_)) {
            // 表示属性が接続されているパスは毎回読み、監視はキャッシュするパスだけに登録する。
            std::vector<std::shared_ptr<NodeWatch>> watches;
            cacheable_ = true;
            for (auto ancestor = path; ancestor.length() > 0; ancestor.pop()) {
                auto watcher = monitor->watch(ancestor.node());
                if (!watcher->hasStaticDisplay()) {
                    cacheable_ = false;
                    break;
                }
                watches.push_back(std::move(watcher));
            }
            if (cacheable_) cacheable_ = monitor->activateWatches(watches);
            if (!cacheable_) watches.clear();
            watches_.swap(watches);
            graph_ = graph;
            path_ = path;
            valid_ = false;
        }
        if (!cacheable_) return readDisplay();

        const auto appearance = monitor->displayRevision();
        const auto displayStatus = static_cast<unsigned int>(probe());
        if (valid_ && appearance == appearance_ && displayStyle == displayStyle_ &&
            displayStatus == displayStatus_) return value_;
        value_ = readDisplay();
        appearance_ = appearance;
        displayStyle_ = displayStyle;
        displayStatus_ = displayStatus;
        valid_ = true;
        return value_;
    }

private:
    MDagPath path_;
    std::vector<std::shared_ptr<NodeWatch>> watches_;
    DisplayValues value_{};
    std::uint64_t graph_ = 0;
    std::uint64_t appearance_ = 0;
    unsigned int displayStyle_ = 0;
    unsigned int displayStatus_ = 0;
    bool cacheable_ = false;
    bool valid_ = false;
};
}
