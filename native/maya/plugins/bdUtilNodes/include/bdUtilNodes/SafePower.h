#pragma once

#include <cmath>

#include "bdUtilNodes/SafeDivision.h"

namespace bd_util_nodes {

inline double safePower(double base, double exponent) {
    if (exponent < 0.0) {
        base = safeDivisor(base);
    }
    return std::pow(base, exponent);
}

}  // namespace bd_util_nodes
