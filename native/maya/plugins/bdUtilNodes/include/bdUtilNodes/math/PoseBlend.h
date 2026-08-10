#pragma once

#include <array>
#include <vector>

#include <maya/MQuaternion.h>

namespace bd_util_nodes {

enum class PoseBlendStatus : short {
    kSuccess = 0,
    kInvalidWeight = 1,
    kInvalidTranslate = 2,
    kInvalidRotate = 3,
    kInvalidScale = 4,
    kUnsupportedRotateOrder = 5,
    kNumericalFailure = 6,
};

struct WeightedPoseValue {
    unsigned int logicalIndex = 0;
    std::array<double, 3> translate = {0.0, 0.0, 0.0};
    MQuaternion rotate;
    std::array<double, 3> scale = {1.0, 1.0, 1.0};
    double weight = 0.0;
};

struct PoseBlendResult {
    std::array<double, 3> translate = {0.0, 0.0, 0.0};
    MQuaternion rotate;
    std::array<double, 3> scale = {1.0, 1.0, 1.0};
};

PoseBlendStatus blendPose(
    const std::array<double, 3>& baseTranslate,
    const MQuaternion& baseRotate,
    const std::array<double, 3>& baseScale,
    const std::vector<WeightedPoseValue>& poses,
    PoseBlendResult& result
);

}  // namespace bd_util_nodes

