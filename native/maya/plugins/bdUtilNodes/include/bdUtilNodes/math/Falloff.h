#pragma once

#include <algorithm>
#include <cmath>
#include <limits>

namespace bd_util_nodes {

enum class Falloff : short {
    kLinear = 0,
    kCubic = 1,
    kQuintic = 2,
};

inline bool isSupportedFalloff(Falloff falloff) {
    return falloff == Falloff::kLinear
        || falloff == Falloff::kCubic
        || falloff == Falloff::kQuintic;
}

inline bool isValidFalloffRadius(
    double innerRadius,
    double outerRadius
) {
    return std::isfinite(innerRadius) && std::isfinite(outerRadius)
        && innerRadius >= 0.0 && outerRadius > innerRadius;
}

inline double evaluateFalloff(
    Falloff falloff,
    double normalizedDistance
) {
    const double value = std::clamp(normalizedDistance, 0.0, 1.0);
    switch (falloff) {
        case Falloff::kLinear:
            return 1.0 - value;
        case Falloff::kCubic:
            return 1.0 - 3.0 * value * value
                + 2.0 * value * value * value;
        case Falloff::kQuintic:
            return 1.0 - 10.0 * std::pow(value, 3.0)
                + 15.0 * std::pow(value, 4.0)
                - 6.0 * std::pow(value, 5.0);
    }
    return std::numeric_limits<double>::quiet_NaN();
}

inline double evaluateFalloffWeight(
    Falloff falloff,
    double distance,
    double innerRadius,
    double outerRadius
) {
    if (distance <= innerRadius) {
        return 1.0;
    }
    if (distance >= outerRadius) {
        return 0.0;
    }
    return evaluateFalloff(
        falloff,
        (distance - innerRadius) / (outerRadius - innerRadius)
    );
}

}  // namespace bd_util_nodes
