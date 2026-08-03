#pragma once

#include <cmath>

#include "bdUtilNodes/math/Clamp.h"

namespace bd_util_nodes {

inline double mapRange(
    double input,
    double sourceMinimum,
    double sourceMaximum,
    double targetMinimum,
    double targetMaximum,
    bool shouldClamp
) {
    const double values[] = {
        input,
        sourceMinimum,
        sourceMaximum,
        targetMinimum,
        targetMaximum,
    };
    for (const double value : values) {
        if (std::isnan(value)) {
            return value;
        }
    }

    if (sourceMinimum == sourceMaximum) {
        return targetMinimum;
    }

    double parameter = (input - sourceMinimum)
        / (sourceMaximum - sourceMinimum);
    if (shouldClamp) {
        parameter = clamp(parameter, 0.0, 1.0);
    }

    if (std::isnan(parameter)) {
        return parameter;
    }
    if (parameter == 0.0) {
        return targetMinimum;
    }
    if (parameter == 1.0) {
        return targetMaximum;
    }
    return targetMinimum
        + parameter * (targetMaximum - targetMinimum);
}

}  // namespace bd_util_nodes
