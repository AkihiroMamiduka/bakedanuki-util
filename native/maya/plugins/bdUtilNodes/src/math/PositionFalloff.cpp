#include "bdUtilNodes/math/PositionFalloff.h"

#include <cmath>

namespace {

using Position = std::array<double, 3>;

bool isFinitePosition(const Position& position) {
    return std::isfinite(position[0]) && std::isfinite(position[1])
        && std::isfinite(position[2]);
}

}  // namespace

namespace bd_util_nodes {

PositionFalloffStatus evaluatePositionFalloff(
    const std::array<double, 3>& inputPosition,
    const std::vector<PositionFalloffSample>& samples,
    Falloff falloff,
    std::vector<PositionFalloffWeight>& outputWeights
) {
    outputWeights.clear();
    if (samples.empty()) {
        return PositionFalloffStatus::kNoPoses;
    }
    if (!isSupportedFalloff(falloff)) {
        return PositionFalloffStatus::kUnsupportedFalloff;
    }
    if (!isFinitePosition(inputPosition)) {
        return PositionFalloffStatus::kInvalidPosition;
    }

    outputWeights.reserve(samples.size());
    for (const PositionFalloffSample& sample : samples) {
        if (!isFinitePosition(sample.position)) {
            outputWeights.clear();
            return PositionFalloffStatus::kInvalidPosition;
        }
        if (!isValidFalloffRadius(
                sample.innerRadius,
                sample.outerRadius
            )) {
            outputWeights.clear();
            return PositionFalloffStatus::kInvalidRadius;
        }

        const double distance = std::hypot(
            inputPosition[0] - sample.position[0],
            inputPosition[1] - sample.position[1],
            inputPosition[2] - sample.position[2]
        );
        if (!std::isfinite(distance)) {
            outputWeights.clear();
            return PositionFalloffStatus::kNumericalFailure;
        }

        const double weight = evaluateFalloffWeight(
            falloff,
            distance,
            sample.innerRadius,
            sample.outerRadius
        );
        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return PositionFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return PositionFalloffStatus::kSuccess;
}

}  // namespace bd_util_nodes
