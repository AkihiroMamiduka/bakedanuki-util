#pragma once

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
}
