#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <algorithm>

#include <maya/MVector.h>

#ifdef BD_CUBE_RESEARCH_FIN_ATTRIBUTES
#include <maya/MDistance.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#endif

namespace bdUtilNodes::fixedCube {

struct FinSettings {
    bool tapered = false;
    double height = defaultFinHeight;
    double widthScale = defaultFinWidthScale;
};

inline void writeFinPositions(
    MPoint* points, const FinSettings& fin, const MVector& first, const MVector& second,
    const MVector& third, const double (&endpoints)[3][2]
) {
    const double center = (endpoints[0][0] + endpoints[0][1]) * 0.5;
    const double halfWidth = (endpoints[0][1] - endpoints[0][0]) * (fin.widthScale * 0.5);
    const auto face = MPoint::origin + second * endpoints[1][1] +
        third * ((endpoints[2][0] + endpoints[2][1]) * 0.5);
    if (fin.height == 0.0) {
        // 高さ0では退化した線分として同じ頂点数とインデックスを使う。
        const auto root = face + first * center;
        std::fill_n(points, vertexCount - bodyVertexCount, root);
        return;
    }

    const double start = center - halfWidth;
    const double end = center + halfWidth;
    const double low = std::min(endpoints[0][0], endpoints[0][1]);
    const double high = std::max(endpoints[0][0], endpoints[0][1]);
    const double rootStart = fin.tapered ? std::clamp(start, low, high) : start;
    const double rootEnd = fin.tapered ? std::clamp(end, low, high) : end;
    const auto rise = second * (endpoints[1][1] < endpoints[1][0] ? -fin.height : fin.height);
    points[0] = face + first * rootStart;
    points[1] = face + first * start + rise;
    points[2] = face + first * end + (fin.tapered ? MVector::zero : rise);
    points[3] = face + first * rootEnd;
}

#ifdef BD_CUBE_RESEARCH_FIN_ATTRIBUTES
struct FinAttributes {
    MObject type;
    MObject height;
    MObject widthScale;

    MStatus create() {
        MStatus status;
        MFnEnumAttribute enumAttribute;
        type = enumAttribute.create("shapeFinType", "sfnt", 0, &status);
        if (!status) return status;
        status = enumAttribute.addField("Standard", 0);
        if (!status) return status;
        status = enumAttribute.addField("Tapered", 1);
        if (!status) return status;
        MFnUnitAttribute unit;
        height = unit.create("shapeFinHeight", "sfnh", MDistance(defaultFinHeight, MDistance::kCentimeters), &status);
        if (!status) return status;
        MFnNumericAttribute numeric;
        widthScale = numeric.create("shapeFinWidthScale", "sfnws", MFnNumericData::kDouble, defaultFinWidthScale, &status);
        return status;
    }

    bool contains(const MObject& attribute) const {
        return attribute == type || attribute == height || attribute == widthScale;
    }

    bool read(const MObject& object, FinSettings& fin) const {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::finShapeRead);
#endif
        MStatus status;
        fin.tapered = MPlug(object, type).asShort(&status) == 1;
        if (!status) return false;
        fin.height = MPlug(object, height).asMDistance(&status).asCentimeters();
        if (!status) return false;
        fin.widthScale = MPlug(object, widthScale).asDouble(&status);
        return status;
    }
};
#endif

}  // namespace bdUtilNodes::fixedCube
