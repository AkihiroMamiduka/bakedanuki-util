#pragma once

#include <array>
#include <vector>

#include "bdUtilNodes/math/Falloff.h"

namespace bd_util_nodes {

enum class OrientationFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
};

struct OrientationFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 0.0};
    double innerRadiusRadians = 0.0;
    double outerRadiusRadians = 1.0;
};

struct OrientationFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

OrientationFalloffStatus evaluateOrientationFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::vector<OrientationFalloffSample>& samples,
    Falloff falloff,
    std::vector<OrientationFalloffWeight>& outputWeights
);

}  // namespace bd_util_nodes
