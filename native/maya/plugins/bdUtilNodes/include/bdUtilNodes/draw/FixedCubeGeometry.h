#pragma once

#include <cstdint>
#include <cstring>

#include <maya/MBoundingBox.h>
#include <maya/MPoint.h>
#ifdef BD_CUBE_RESEARCH_FIN
#include <maya/MMatrix.h>
#endif

namespace bdUtilNodes::fixedCube {
inline constexpr unsigned int bodyVertexCount = 8;
#ifdef BD_CUBE_RESEARCH_FIN
inline constexpr double defaultFinHeight = 0.5;
inline constexpr double defaultFinWidthScale = 1.0;
#endif
inline constexpr float vertices[][3] = {
    {-0.5f, -0.5f, -0.5f}, {0.5f, -0.5f, -0.5f},
    {0.5f, 0.5f, -0.5f}, {-0.5f, 0.5f, -0.5f},
    {-0.5f, -0.5f, 0.5f}, {0.5f, -0.5f, 0.5f},
    {0.5f, 0.5f, 0.5f}, {-0.5f, 0.5f, 0.5f},
#ifdef BD_CUBE_RESEARCH_FIN
    {-0.5f, 0.5f, 0.0f}, {-0.5f, 0.5f + static_cast<float>(defaultFinHeight), 0.0f},
    {0.5f, 0.5f + static_cast<float>(defaultFinHeight), 0.0f}, {0.5f, 0.5f, 0.0f},
#endif
};
inline constexpr unsigned int indices[] = {
    0, 1, 1, 2, 2, 3, 3, 0, 4, 5, 5, 6,
    6, 7, 7, 4, 0, 4, 1, 5, 2, 6, 3, 7,
#ifdef BD_CUBE_RESEARCH_FIN
    8, 9, 9, 10, 10, 11,
#endif
};
inline constexpr unsigned int vertexCount = sizeof(vertices) / sizeof(vertices[0]);
inline constexpr unsigned int indexCount = sizeof(indices) / sizeof(indices[0]);

inline constexpr unsigned int drawVertexCount(bool guideLine) {
    return vertexCount + (guideLine ? 6 : 0);
}

inline constexpr unsigned int drawIndexCount(bool guideLine) {
    return indexCount + (guideLine ? 6 : 0);
}

inline void writeDrawVertices(const float (&source)[vertexCount][3], bool guideLine, void* destination) {
    std::memcpy(destination, source, sizeof(source));
    if (!guideLine) return;
    // 対向面の中央を結び、軸・寸法の反転や縮退でも本体の境界内に収める。
    constexpr unsigned int faceCorners[][2] = {{0, 7}, {1, 6}, {0, 5}, {3, 6}, {0, 2}, {4, 6}};
    auto* values = static_cast<float*>(destination);
    for (unsigned int face = 0; face < 6; ++face) {
        for (unsigned int axis = 0; axis < 3; ++axis) {
            values[(vertexCount + face) * 3 + axis] = static_cast<float>(
                (static_cast<double>(source[faceCorners[face][0]][axis]) +
                 static_cast<double>(source[faceCorners[face][1]][axis])) * 0.5);
        }
    }
}

inline void writeDrawIndices(bool guideLine, void* destination) {
    std::memcpy(destination, indices, sizeof(indices));
    if (!guideLine) return;
    auto* values = static_cast<unsigned int*>(destination);
    for (unsigned int i = 0; i < 6; ++i) values[indexCount + i] = vertexCount + i;
}

inline MBoundingBox bounds() {
#ifdef BD_CUBE_RESEARCH_FIN
    return MBoundingBox(MPoint(-0.5, -0.5, -0.5), MPoint(0.5, 0.5 + defaultFinHeight, 0.5));
#else
    return MBoundingBox(MPoint(-0.5, -0.5, -0.5), MPoint(0.5, 0.5, 0.5));
#endif
}

struct Geometry {
    float vertices[vertexCount][3];
    MBoundingBox bounds;
    std::uint64_t revision = 0;
    bool guideLine = false;
#ifdef BD_CUBE_RESEARCH_FIN
    MBoundingBox bodyBounds;
    MPoint finPositions[vertexCount - bodyVertexCount];
#endif
};

inline Geometry geometryFromPositions(
    const MPoint (&positions)[vertexCount], std::uint64_t revision, bool guideLine = false
) {
    Geometry result;
    for (unsigned int i = 0; i < vertexCount; ++i) {
        const auto& point = positions[i];
        result.bounds.expand(point);
        for (unsigned int axis = 0; axis < 3; ++axis) {
            result.vertices[i][axis] = static_cast<float>(point[axis]);
        }
#ifdef BD_CUBE_RESEARCH_FIN
        if (i == bodyVertexCount - 1) result.bodyBounds = result.bounds;
        if (i >= bodyVertexCount) result.finPositions[i - bodyVertexCount] = point;
#endif
    }
    result.revision = revision;
    result.guideLine = guideLine;
    return result;
}

#ifdef BD_CUBE_RESEARCH_FIN
inline Geometry initialGeometry() {
    MPoint positions[vertexCount];
    for (unsigned int i = 0; i < vertexCount; ++i) {
        positions[i] = MPoint(vertices[i][0], vertices[i][1], vertices[i][2]);
    }
    return geometryFromPositions(positions, 0);
}

inline MBoundingBox transformedBounds(const Geometry& geometry, const MMatrix& matrix) {
    if (matrix == MMatrix::identity) return geometry.bounds;
    auto result = geometry.bodyBounds;
    result.transformUsing(matrix);
    // Finのみが張り出すので、全体の箱を変換すると実際の線より広い範囲になる。
    for (const auto& point : geometry.finPositions) result.expand(point * matrix);
    return result;
}
#endif
}
