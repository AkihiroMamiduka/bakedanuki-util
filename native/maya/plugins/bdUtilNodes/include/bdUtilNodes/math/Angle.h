#pragma once

#include <cmath>
#include <limits>

namespace bd_util_nodes {

constexpr double kPiRadians =
    3.141592653589793238462643383279502884;
constexpr double kFullRotationRadians = 2.0 * kPiRadians;

inline double wrapAngle(
    double input,
    double minimum,
    double maximum
) {
    if (
        std::isnan(input) ||
        std::isnan(minimum) ||
        std::isnan(maximum)
    ) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    if (maximum <= minimum) {
        return minimum;
    }
    if (
        !std::isfinite(input) ||
        !std::isfinite(minimum) ||
        !std::isfinite(maximum)
    ) {
        return std::numeric_limits<double>::quiet_NaN();
    }

    const double period = maximum - minimum;
    if (!std::isfinite(period)) {
        return std::numeric_limits<double>::quiet_NaN();
    }

    double wrapped = std::fmod(input - minimum, period);
    if (!std::isfinite(wrapped)) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    if (wrapped < 0.0) {
        wrapped += period;
    }

    const double result = minimum + wrapped;
    if (result >= maximum) {
        return minimum;
    }
    return result;
}

inline double shortestAngleDelta(
    double input1,
    double input2
) {
    return wrapAngle(
        input2 - input1,
        -kPiRadians,
        kPiRadians
    );
}

}  // namespace bd_util_nodes
