#pragma once

#include <array>
#include <cstdint>
#include <cstring>
#include <memory>
#include <optional>
#include <utility>

#include <maya/MBoundingBox.h>
#include <maya/MPoint.h>
#include <maya/MMatrix.h>

namespace bdUtilNodes::fixedCube {
inline constexpr unsigned int bodyVertexCount = 8;
inline constexpr unsigned int finVertexCount = 4;
inline constexpr unsigned int finIndices[] = {0, 1, 1, 2, 2, 3};
inline constexpr unsigned int finIndexCount = sizeof(finIndices) / sizeof(finIndices[0]);
inline constexpr double defaultFinHeight = 0.5;
inline constexpr double defaultFinWidthScale = 1.0;
inline constexpr float defaultFinVertices[finVertexCount][3] = {
    {-0.5f, 0.5f, 0.0f}, {-0.5f, 1.0f, 0.0f},
    {0.5f, 1.0f, 0.0f}, {0.5f, 0.5f, 0.0f},
};
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
    // ねじれた面でも、四隅を同じ割合で補間した点を面の中央とする。
    constexpr unsigned int faceCorners[][4] = {
        {0, 3, 4, 7}, {1, 2, 5, 6}, {0, 1, 4, 5},
        {2, 3, 6, 7}, {0, 1, 2, 3}, {4, 5, 6, 7},
    };
    auto* values = static_cast<float*>(destination);
    for (unsigned int face = 0; face < 6; ++face) {
        for (unsigned int axis = 0; axis < 3; ++axis) {
            values[(vertexCount + face) * 3 + axis] = static_cast<float>(
                (static_cast<double>(source[faceCorners[face][0]][axis]) +
                 static_cast<double>(source[faceCorners[face][1]][axis]) +
                 static_cast<double>(source[faceCorners[face][2]][axis]) +
                 static_cast<double>(source[faceCorners[face][3]][axis])) * 0.25);
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

struct FinGeometry {
    float vertices[finVertexCount][3];
    MPoint positions[finVertexCount];
};

struct GeometryDetails {
    MBoundingBox bodyBounds;
    std::optional<std::array<MPoint, bodyVertexCount>> exactBody;
    std::optional<FinGeometry> fin;
};

struct Geometry {
    float vertices[vertexCount][3];
    MBoundingBox bounds;
    std::uint64_t revision = 0;
    bool guideLine = false;
#ifdef BD_CUBE_RESEARCH_FIN
    MBoundingBox bodyBounds;
    MPoint finPositions[vertexCount - bodyVertexCount];
#endif
    std::shared_ptr<const GeometryDetails> details;

    const FinGeometry* fin() const {
        return details && details->fin ? &*details->fin : nullptr;
    }
};

inline Geometry geometryFromPositions(
    const MPoint (&positions)[vertexCount], std::uint64_t revision, bool guideLine = false,
    const MPoint* finPositions = nullptr, bool preciseBodyBounds = false
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
    if (!finPositions && !preciseBodyBounds) return result;

    auto details = std::make_shared<GeometryDetails>();
    details->bodyBounds = result.bounds;
    if (preciseBodyBounds) {
        auto& exactBody = details->exactBody.emplace();
        for (unsigned int i = 0; i < bodyVertexCount; ++i) exactBody[i] = positions[i];
    }
    if (finPositions) {
        auto& fin = details->fin.emplace();
        for (unsigned int i = 0; i < finVertexCount; ++i) {
            fin.positions[i] = finPositions[i];
            result.bounds.expand(finPositions[i]);
            for (unsigned int axis = 0; axis < 3; ++axis) {
                fin.vertices[i][axis] = static_cast<float>(finPositions[i][axis]);
            }
        }
    }
    result.details = std::move(details);
    return result;
}

inline Geometry defaultDrawGeometry(bool guideLine, bool fin) {
    MPoint positions[vertexCount];
    for (unsigned int i = 0; i < vertexCount; ++i) {
        positions[i] = MPoint(vertices[i][0], vertices[i][1], vertices[i][2]);
    }
    MPoint finPositions[finVertexCount];
    if (fin) {
        for (unsigned int i = 0; i < finVertexCount; ++i) {
            finPositions[i] = MPoint(defaultFinVertices[i][0], defaultFinVertices[i][1], defaultFinVertices[i][2]);
        }
    }
    return geometryFromPositions(positions, 0, guideLine, fin ? finPositions : nullptr);
}

inline Geometry initialGeometry() {
    return defaultDrawGeometry(false, false);
}

inline unsigned int drawVertexCount(const Geometry& geometry) {
    return drawVertexCount(geometry.guideLine) + (geometry.fin() ? finVertexCount : 0);
}

inline unsigned int drawIndexCount(const Geometry& geometry) {
    return drawIndexCount(geometry.guideLine) + (geometry.fin() ? finIndexCount : 0);
}

inline void writeDrawVertices(const Geometry& geometry, void* destination) {
    writeDrawVertices(geometry.vertices, geometry.guideLine, destination);
    if (const auto* fin = geometry.fin()) {
        auto* values = static_cast<float*>(destination) + drawVertexCount(geometry.guideLine) * 3;
        std::memcpy(values, fin->vertices, sizeof(fin->vertices));
    }
}

inline void writeDrawIndices(const Geometry& geometry, void* destination) {
    writeDrawIndices(geometry.guideLine, destination);
    if (geometry.fin()) {
        auto* values = static_cast<unsigned int*>(destination) + drawIndexCount(geometry.guideLine);
        const auto start = drawVertexCount(geometry.guideLine);
        for (unsigned int i = 0; i < finIndexCount; ++i) values[i] = start + finIndices[i];
    }
}

inline bool sameDrawTopology(const Geometry& left, const Geometry& right) {
    return left.guideLine == right.guideLine && static_cast<bool>(left.fin()) == static_cast<bool>(right.fin());
}

inline bool sameDrawVertices(const Geometry& left, const Geometry& right) {
    const auto* leftFin = left.fin();
    const auto* rightFin = right.fin();
    return std::memcmp(left.vertices, right.vertices, sizeof(left.vertices)) == 0 &&
        static_cast<bool>(leftFin) == static_cast<bool>(rightFin) &&
        (!leftFin || std::memcmp(leftFin->vertices, rightFin->vertices, sizeof(leftFin->vertices)) == 0);
}

inline bool hasDefaultDrawVertices(const Geometry& geometry) {
    const auto* fin = geometry.fin();
    return std::memcmp(geometry.vertices, vertices, sizeof(vertices)) == 0 &&
        (!fin || std::memcmp(fin->vertices, defaultFinVertices, sizeof(defaultFinVertices)) == 0);
}

inline MBoundingBox transformedBounds(const Geometry& geometry, const MMatrix& matrix) {
    if (matrix == MMatrix::identity) return geometry.bounds;
#ifdef BD_CUBE_RESEARCH_FIN
    auto result = geometry.bodyBounds;
#else
    auto result = geometry.details ? geometry.details->bodyBounds : geometry.bounds;
#endif
    if (geometry.details && geometry.details->exactBody) {
        // 回転・面スケール後は実頂点が軸平行の箱の角とは限らない。
        result.clear();
        for (const auto& point : *geometry.details->exactBody) result.expand(point * matrix);
    } else {
        result.transformUsing(matrix);
    }
#ifdef BD_CUBE_RESEARCH_FIN
    for (const auto& point : geometry.finPositions) result.expand(point * matrix);
#endif
    if (const auto* fin = geometry.fin()) {
        for (const auto& point : fin->positions) result.expand(point * matrix);
    }
    return result;
}
}
