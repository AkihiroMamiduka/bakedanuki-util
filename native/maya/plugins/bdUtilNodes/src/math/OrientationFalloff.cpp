#include "bdUtilNodes/math/OrientationFalloff.h"

#include <algorithm>
#include <cmath>

namespace {

constexpr double kQuaternionEpsilon = 1.0e-12;
using Quaternion = std::array<double, 4>;

bool normalizeQuaternion(const Quaternion& input, Quaternion& output) {
    const double maximum = std::max({
        std::abs(input[0]),
        std::abs(input[1]),
        std::abs(input[2]),
        std::abs(input[3]),
    });
    if (!std::isfinite(maximum) || maximum <= kQuaternionEpsilon) {
        return false;
    }

    const double x = input[0] / maximum;
    const double y = input[1] / maximum;
    const double z = input[2] / maximum;
    const double w = input[3] / maximum;
    const double length = std::sqrt(x * x + y * y + z * z + w * w);
    if (!std::isfinite(length) || length <= 0.0) {
        return false;
    }

    output = {x / length, y / length, z / length, w / length};
    return true;
}

double quaternionDistance(
    const Quaternion& first,
    const Quaternion& second
) {
    const double dot = std::abs(
        first[0] * second[0] + first[1] * second[1]
        + first[2] * second[2] + first[3] * second[3]
    );
    return 2.0 * std::acos(std::clamp(dot, 0.0, 1.0));
}

}  // namespace

namespace bd_util_nodes {

OrientationFalloffStatus evaluateOrientationFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::vector<OrientationFalloffSample>& samples,
    Falloff falloff,
    std::vector<OrientationFalloffWeight>& outputWeights
) {
    outputWeights.clear();
    if (samples.empty()) {
        return OrientationFalloffStatus::kNoPoses;
    }
    if (!isSupportedFalloff(falloff)) {
        return OrientationFalloffStatus::kUnsupportedFalloff;
    }

    Quaternion normalizedInput;
    if (!normalizeQuaternion(inputQuaternion, normalizedInput)) {
        return OrientationFalloffStatus::kInvalidQuaternion;
    }

    outputWeights.reserve(samples.size());
    for (const OrientationFalloffSample& sample : samples) {
        if (!isValidFalloffRadius(
                sample.innerRadiusRadians,
                sample.outerRadiusRadians
            )) {
            outputWeights.clear();
            return OrientationFalloffStatus::kInvalidRadius;
        }

        Quaternion normalizedPose;
        if (!normalizeQuaternion(sample.quaternion, normalizedPose)) {
            outputWeights.clear();
            return OrientationFalloffStatus::kInvalidQuaternion;
        }

        const double distance = quaternionDistance(
            normalizedInput,
            normalizedPose
        );
        if (!std::isfinite(distance)) {
            outputWeights.clear();
            return OrientationFalloffStatus::kNumericalFailure;
        }
        const double weight = evaluateFalloffWeight(
            falloff,
            distance,
            sample.innerRadiusRadians,
            sample.outerRadiusRadians
        );
        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return OrientationFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return OrientationFalloffStatus::kSuccess;
}

}  // namespace bd_util_nodes
