#pragma once

#include <cmath>

namespace bd_util_nodes {

inline constexpr double kDivisionEpsilon = 1.0e-9;

inline double safeDivisor(double divisor) {
    if (std::abs(divisor) < kDivisionEpsilon) {
        return std::copysign(kDivisionEpsilon, divisor);
    }
    return divisor;
}

inline double safeDivide(double numerator, double divisor) {
    return numerator / safeDivisor(divisor);
}

}  // namespace bd_util_nodes
