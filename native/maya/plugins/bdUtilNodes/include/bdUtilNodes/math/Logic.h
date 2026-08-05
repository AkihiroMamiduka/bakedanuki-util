#pragma once

namespace bd_util_nodes {

enum class LogicOperation : short {
    kAnd = 0,
    kOr = 1,
};

inline bool evaluateLogic(
    bool accumulated,
    short operation,
    bool current
) noexcept {
    switch (static_cast<LogicOperation>(operation)) {
        case LogicOperation::kAnd:
            return accumulated && current;
        case LogicOperation::kOr:
            return accumulated || current;
    }
    return false;
}

}  // namespace bd_util_nodes
