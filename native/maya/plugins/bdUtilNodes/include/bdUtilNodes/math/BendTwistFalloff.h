#pragma once

#include <array>
#include <vector>

#include "bdUtilNodes/math/BendTwist.h"
#include "bdUtilNodes/math/Falloff.h"

namespace bd_util_nodes {

enum class BendTwistFalloffMode : short {
    kBendTwist = 0,
    kBendOnly = 1,
};

enum class BendTwistFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kUnsupportedMode = 5,
    kUnsupportedOrder = 6,
    kNumericalFailure = 7,
};

struct BendTwistFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 0.0};
    double bendInnerRadiusRadians = 0.0;
    double bendOuterRadiusRadians = 1.0;
    double twistInnerRadiusRadians = 0.0;
    double twistOuterRadiusRadians = 1.0;
};

struct BendTwistFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

BendTwistFalloffStatus evaluateBendTwistFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::array<double, 4>& axisQuaternion,
    const std::vector<BendTwistFalloffSample>& samples,
    BendTwistOrder order,
    BendTwistFalloffMode mode,
    Falloff falloff,
    std::vector<BendTwistFalloffWeight>& outputWeights
);

}  // namespace bd_util_nodes
