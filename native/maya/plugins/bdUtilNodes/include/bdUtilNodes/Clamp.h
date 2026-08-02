#pragma once

#include "bdUtilNodes/MinMax.h"

namespace bd_util_nodes {

inline double clamp(
    double input,
    double minimumValue,
    double maximumValue
) {
    const double lower = minimum(minimumValue, maximumValue);
    const double upper = maximum(minimumValue, maximumValue);
    return minimum(maximum(input, lower), upper);
}

}  // namespace bd_util_nodes
