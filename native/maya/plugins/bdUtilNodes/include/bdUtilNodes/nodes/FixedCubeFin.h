#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/FixedCubeAdjustment.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <algorithm>

#include <maya/MDistance.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MVector.h>

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
        // 高さ0では本体内の一点へ縮退させ、幅設定によって境界を広げない。
        std::fill_n(points, finVertexCount, face + first * center);
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

inline void writeWarpedFinPositions(
    MPoint* points, const FinSettings& fin, const FaceWarp& warp, const double (&endpoints)[3][2]
) {
    if (!warp.enabled) {
        writeFinPositions(points, fin, MVector(1, 0, 0), MVector(0, 1, 0), MVector(0, 0, 1), endpoints);
        return;
    }
    const double center = (endpoints[0][0] + endpoints[0][1]) * 0.5;
    const double halfWidth = (endpoints[0][1] - endpoints[0][0]) * (fin.widthScale * 0.5);
    const double low = std::min(endpoints[0][0], endpoints[0][1]);
    const double high = std::max(endpoints[0][0], endpoints[0][1]);
    const auto face = [&](double x) {
        return MPoint(x, endpoints[1][1], (endpoints[2][0] + endpoints[2][1]) * 0.5);
    };
    if (fin.height == 0.0) {
        std::fill_n(points, finVertexCount, warp.point(face(center)));
        return;
    }
    const double start = center - halfWidth, end = center + halfWidth;
    const auto rise = MVector(0, endpoints[1][1] < endpoints[1][0] ? -fin.height : fin.height, 0);
    points[0] = warp.point(face(fin.tapered ? std::clamp(start, low, high) : start));
    points[1] = warp.point(face(start)) + (fin.tapered ? warp.secondFaceNormal(face(start)) * fin.height : rise);
    points[2] = warp.point(face(end)) + (fin.tapered ? MVector::zero : rise);
    points[3] = warp.point(face(fin.tapered ? std::clamp(end, low, high) : end));
}

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

}  // namespace bdUtilNodes::fixedCube
