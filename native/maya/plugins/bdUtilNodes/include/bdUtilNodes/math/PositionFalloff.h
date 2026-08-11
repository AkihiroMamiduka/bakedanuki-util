#pragma once

#include <array>
#include <vector>

namespace bd_util_nodes {

enum class PositionFalloff : short {
    kLinear = 0,
    kCubic = 1,
    kQuintic = 2,
};

enum class PositionFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidPosition = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
};

struct PositionFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 3> position = {0.0, 0.0, 0.0};
    double innerRadius = 0.0;
    double outerRadius = 1.0;
};

struct PositionFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

PositionFalloffStatus evaluatePositionFalloff(
    const std::array<double, 3>& inputPosition,
    const std::vector<PositionFalloffSample>& samples,
    PositionFalloff falloff,
    std::vector<PositionFalloffWeight>& outputWeights
);

}  // namespace bd_util_nodes
