#pragma once

#include <cstdint>

#include <maya/MBoundingBox.h>
#include <maya/MPoint.h>

namespace bdUtilNodes::fixedCube {
inline constexpr float vertices[8][3] = {
    {-0.5f, -0.5f, -0.5f}, {0.5f, -0.5f, -0.5f},
    {0.5f, 0.5f, -0.5f}, {-0.5f, 0.5f, -0.5f},
    {-0.5f, -0.5f, 0.5f}, {0.5f, -0.5f, 0.5f},
    {0.5f, 0.5f, 0.5f}, {-0.5f, 0.5f, 0.5f},
};
inline constexpr unsigned int indices[24] = {
    0, 1, 1, 2, 2, 3, 3, 0, 4, 5, 5, 6,
    6, 7, 7, 4, 0, 4, 1, 5, 2, 6, 3, 7,
};
inline MBoundingBox bounds() {
    return MBoundingBox(MPoint(-0.5, -0.5, -0.5), MPoint(0.5, 0.5, 0.5));
}

struct Geometry {
    float vertices[8][3];
    MBoundingBox bounds;
    std::uint64_t revision = 0;
};

inline Geometry geometryFromPositions(const MPoint (&positions)[8], std::uint64_t revision) {
    Geometry result;
    for (unsigned int i = 0; i < 8; ++i) {
        const auto& point = positions[i];
        result.bounds.expand(point);
        for (unsigned int axis = 0; axis < 3; ++axis) {
            result.vertices[i][axis] = static_cast<float>(point[axis]);
        }
    }
    result.revision = revision;
    return result;
}
}
