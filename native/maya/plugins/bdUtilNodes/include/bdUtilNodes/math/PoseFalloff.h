#pragma once

#include <array>
#include <vector>

#include "bdUtilNodes/math/Falloff.h"

namespace bd_util_nodes {

enum class PoseFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
};

struct PoseFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 0.0};
    double innerRadiusRadians = 0.0;
    double outerRadiusRadians = 1.0;
};

struct PoseFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

PoseFalloffStatus evaluatePoseFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::vector<PoseFalloffSample>& samples,
    Falloff falloff,
    std::vector<PoseFalloffWeight>& outputWeights
);

}  // namespace bd_util_nodes
