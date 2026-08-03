#pragma once

#include <algorithm>

namespace bd_util_nodes {

inline double clampedLerp(
    double input1,
    double input2,
    double weight
) {
    const double clampedWeight = std::clamp(weight, 0.0, 1.0);
    if (clampedWeight == 0.0) {
        return input1;
    }
    if (clampedWeight == 1.0) {
        return input2;
    }
    return input1 * (1.0 - clampedWeight) + input2 * clampedWeight;
}

}  // namespace bd_util_nodes
