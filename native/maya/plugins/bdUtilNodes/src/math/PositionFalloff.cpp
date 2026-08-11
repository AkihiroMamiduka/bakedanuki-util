#include "bdUtilNodes/math/PositionFalloff.h"

#include <algorithm>
#include <cmath>
#include <limits>

namespace {

using Position = std::array<double, 3>;

bool isFinitePosition(const Position& position) {
    return std::isfinite(position[0]) && std::isfinite(position[1])
        && std::isfinite(position[2]);
}

bool isValidRadius(double innerRadius, double outerRadius) {
    return std::isfinite(innerRadius) && std::isfinite(outerRadius)
        && innerRadius >= 0.0 && outerRadius > innerRadius;
}

bool isSupportedFalloff(bd_util_nodes::PositionFalloff falloff) {
    using bd_util_nodes::PositionFalloff;
    return falloff == PositionFalloff::kLinear
        || falloff == PositionFalloff::kCubic
        || falloff == PositionFalloff::kQuintic;
}

double evaluateFalloff(
    bd_util_nodes::PositionFalloff falloff,
    double normalizedDistance
) {
    using bd_util_nodes::PositionFalloff;
    const double value = std::clamp(normalizedDistance, 0.0, 1.0);
    switch (falloff) {
        case PositionFalloff::kLinear:
            return 1.0 - value;
        case PositionFalloff::kCubic:
            return 1.0 - 3.0 * value * value
                + 2.0 * value * value * value;
        case PositionFalloff::kQuintic:
            return 1.0 - 10.0 * std::pow(value, 3.0)
                + 15.0 * std::pow(value, 4.0)
                - 6.0 * std::pow(value, 5.0);
    }
    return std::numeric_limits<double>::quiet_NaN();
}

}  // namespace

namespace bd_util_nodes {

PositionFalloffStatus evaluatePositionFalloff(
    const std::array<double, 3>& inputPosition,
    const std::vector<PositionFalloffSample>& samples,
    PositionFalloff falloff,
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
        if (!isValidRadius(sample.innerRadius, sample.outerRadius)) {
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

        double weight = 0.0;
        if (distance <= sample.innerRadius) {
            weight = 1.0;
        } else if (distance < sample.outerRadius) {
            const double normalizedDistance =
                (distance - sample.innerRadius)
                / (sample.outerRadius - sample.innerRadius);
            weight = evaluateFalloff(falloff, normalizedDistance);
        }
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
