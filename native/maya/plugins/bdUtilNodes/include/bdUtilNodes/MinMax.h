#pragma once

#include <cmath>

namespace bd_util_nodes {

inline double minimum(double input1, double input2) {
    if (std::isnan(input1)) {
        return input1;
    }
    if (std::isnan(input2)) {
        return input2;
    }
    return std::fmin(input1, input2);
}

inline double maximum(double input1, double input2) {
    if (std::isnan(input1)) {
        return input1;
    }
    if (std::isnan(input2)) {
        return input2;
    }
    return std::fmax(input1, input2);
}

}  // namespace bd_util_nodes
