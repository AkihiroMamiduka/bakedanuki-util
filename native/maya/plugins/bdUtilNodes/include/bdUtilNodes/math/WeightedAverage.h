#pragma once

namespace bd_util_nodes {

inline double weightedAverage(
    double weightedSum,
    double weightSum
) noexcept {
    return weightSum == 0.0 ? 0.0 : weightedSum / weightSum;
}

}  // namespace bd_util_nodes
