#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <initializer_list>
#include <string>

#include <maya/MAngle.h>
#include <maya/MDistance.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MPoint.h>
#include <maya/MQuaternion.h>
#include <maya/MVector.h>

namespace bdUtilNodes::fixedCube {

inline MStatus configureStaticShapeAttribute(const MObject& attribute) {
    MStatus status;
    MFnAttribute fn(attribute, &status);
    if (!status) return status;
    for (const auto result : {fn.setKeyable(false), fn.setConnectable(false),
        fn.setChannelBox(true), fn.setInternal(true), fn.setAffectsAppearance(true),
        fn.setAffectsWorldSpace(true)}) {
        if (!result) return result;
    }
    return MS::kSuccess;
}

struct AdjustmentSettings {
    std::array<double, 12> faceScale = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    double rootSize = 1.0;
    double size = 1.0;
    MVector translate;
    MVector rotate;
    MVector scale = MVector(1, 1, 1);
    MVector axisTranslate;
    MVector axisRotate;
    MVector axisScale = MVector(1, 1, 1);

    bool hasFaceScale() const {
        return std::any_of(faceScale.begin(), faceScale.end(), [](double value) { return value != 1.0; });
    }
    bool hasTransform() const {
        return rootSize != 1.0 || size != 1.0 || translate != MVector::zero ||
            rotate != MVector::zero || scale != MVector(1, 1, 1) ||
            axisTranslate != MVector::zero || axisRotate != MVector::zero || axisScale != MVector(1, 1, 1);
    }
};

struct FaceWarp {
    const AdjustmentSettings& settings;
    MVector center;
    MVector span;
    bool enabled;

    FaceWarp(const AdjustmentSettings& values, const double (&endpoints)[3][2])
        : settings(values), enabled(values.hasFaceScale()) {
        for (unsigned int axis = 0; axis < 3; ++axis) {
            center[axis] = (endpoints[axis][0] + endpoints[axis][1]) * 0.5;
            span[axis] = endpoints[axis][1] - endpoints[axis][0];
        }
    }

    double faceScale(unsigned int normal, unsigned int component, bool plus) const {
        const auto ordinal = component < normal ? component : component - 1;
        return settings.faceScale[normal * 4 + (plus ? 0 : 2) + ordinal];
    }
    MVector coordinates(const MPoint& point) const {
        MVector result;
        for (unsigned int axis = 0; axis < 3; ++axis) {
            // 潰れた軸では両面の倍率を平均し、同じ位置の角を分離しない。
            result[axis] = span[axis] == 0.0 ? 0.0 : (point[axis] - center[axis]) / span[axis];
        }
        return result;
    }
    double interpolated(unsigned int normal, unsigned int component, double coordinate) const {
        return (0.5 - coordinate) * faceScale(normal, component, false) +
            (0.5 + coordinate) * faceScale(normal, component, true);
    }
    MPoint point(const MPoint& source) const {
        if (!enabled) return source;
        const auto coordinate = coordinates(source);
        auto result = source;
        for (unsigned int axis = 0; axis < 3; ++axis) {
            const auto first = (axis + 1) % 3, second = (axis + 2) % 3;
            const double value = center[axis] + (source[axis] - center[axis]) *
                interpolated(first, axis, coordinate[first]) * interpolated(second, axis, coordinate[second]);
            if (std::isfinite(value)) result[axis] = value;
        }
        return result;
    }
    MVector derivative(const MPoint& source, unsigned int component) const {
        const auto coordinate = coordinates(source);
        MVector result;
        for (unsigned int axis = 0; axis < 3; ++axis) {
            const auto first = (axis + 1) % 3, second = (axis + 2) % 3;
            if (axis == component) {
                result[axis] = interpolated(first, axis, coordinate[first]) *
                    interpolated(second, axis, coordinate[second]);
            } else if (span[component] != 0.0) {
                const auto other = first == component ? second : first;
                result[axis] = (source[axis] - center[axis]) *
                    (faceScale(component, axis, true) - faceScale(component, axis, false)) /
                    span[component] * interpolated(other, axis, coordinate[other]);
            }
        }
        return result;
    }
    MVector secondFaceNormal(const MPoint& source) const {
        const MVector fallback(0, span.y < 0.0 ? -1.0 : 1.0, 0);
        if (span.x == 0.0 || span.z == 0.0) return fallback;
        auto along = derivative(source, 0), across = derivative(source, 2);
        const auto depth = derivative(source, 1);
        const double a = std::hypot(along.x, along.y, along.z);
        const double b = std::hypot(across.x, across.y, across.z);
        const double d = std::hypot(depth.x, depth.y, depth.z);
        if (!std::isfinite(a) || !std::isfinite(b) || !std::isfinite(d) || a == 0.0 || b == 0.0 || d == 0.0) return fallback;
        auto normal = (across / b) ^ (along / a);
        const double length = std::hypot(normal.x, normal.y, normal.z);
        const double orientation = normal * (depth / d);
        if (!std::isfinite(length) || length < 1e-12 || std::abs(orientation) < 1e-12) return fallback;
        normal *= (orientation < 0.0 ? -1.0 : 1.0) * (span.y < 0.0 ? -1.0 : 1.0) / length;
        return normal;
    }
};

struct AdjustmentTransform {
    const AdjustmentSettings& settings;
    MVector first, second, third;
    MQuaternion rotate, axisRotate;
    bool enabled;

    AdjustmentTransform(const AdjustmentSettings& values, const MVector& x, const MVector& y, const MVector& z)
        : settings(values), first(x), second(y), third(z),
          enabled(values.hasTransform()) {
        if (values.rotate != MVector::zero)
            rotate = MEulerRotation(values.rotate.x, values.rotate.y, values.rotate.z, MEulerRotation::kXYZ).asQuaternion();
        if (values.axisRotate != MVector::zero)
            axisRotate = MEulerRotation(values.axisRotate.x, values.axisRotate.y, values.axisRotate.z, MEulerRotation::kXYZ).asQuaternion();
    }

    MPoint point(const MPoint& source) const {
        if (!enabled) return MPoint::origin + first * source.x + second * source.y + third * source.z;
        const MVector scaled(source.x * settings.size * settings.axisScale.x,
            source.y * settings.size * settings.axisScale.y, source.z * settings.size * settings.axisScale.z);
        const auto local = scaled.rotateBy(axisRotate) + settings.axisTranslate;
        const auto oriented = first * local.x + second * local.y + third * local.z;
        const MVector outer(oriented.x * settings.scale.x, oriented.y * settings.scale.y, oriented.z * settings.scale.z);
        const auto result = (outer.rotateBy(rotate) + settings.translate) * settings.rootSize;
        return MPoint::origin + result;
    }
};

struct AdjustmentAttributes {
    enum class Kind { distance, angle, number };
    struct Triple {
        MObject parent;
        MObject children[3];
        Kind kind;

        MStatus create(const char* longName, const char* shortName, Kind valueKind) {
            kind = valueKind;
            MStatus status;
            MFnNumericAttribute numeric;
            MFnUnitAttribute unit;
            for (unsigned int axis = 0; axis < 3; ++axis) {
                const auto name = std::string(longName) + "XYZ"[axis];
                const auto shortChild = std::string(shortName) + "xyz"[axis];
                children[axis] = kind == Kind::number
                    ? numeric.create(name.c_str(), shortChild.c_str(), MFnNumericData::kDouble, 1.0, &status)
                    : unit.create(name.c_str(), shortChild.c_str(),
                        kind == Kind::distance ? MFnUnitAttribute::kDistance : MFnUnitAttribute::kAngle, 0.0, &status);
                if (!status) return status;
                status = configureStaticShapeAttribute(children[axis]);
                if (!status) return status;
            }
            parent = numeric.create(longName, shortName, children[0], children[1], children[2], &status);
            return status;
        }
        bool contains(const MObject& attribute) const {
            return attribute == parent || attribute == children[0] || attribute == children[1] || attribute == children[2];
        }
        bool read(const MObject& object, MVector& value) const {
            MStatus status;
            for (unsigned int axis = 0; axis < 3; ++axis) {
                const MPlug plug(object, children[axis]);
                value[axis] = kind == Kind::distance ? plug.asMDistance(&status).asCentimeters()
                    : kind == Kind::angle ? plug.asMAngle(&status).asRadians() : plug.asDouble(&status);
                if (!status) return false;
            }
            return true;
        }
    };

    MObject faceParents[6];
    MObject faceChildren[12];
    MObject rootSize, size;
    Triple translate, rotate, scale, axisTranslate, axisRotate, axisScale;

    MStatus create() {
        MStatus status;
        MFnNumericAttribute numeric;
        const char* axisNames[] = {"1st", "2nd", "3rd"};
        for (unsigned int normal = 0; normal < 3; ++normal) for (unsigned int side = 0; side < 2; ++side) {
            const auto index = normal * 2 + side;
            const auto name = std::string("shapeBaseSpace") + axisNames[normal] + "Axis" + (side == 0 ? "Plus" : "Minus") + "Scale";
            const auto shortName = std::string("sbsp") + "123"[normal] + (side == 0 ? "ps" : "ms");
            unsigned int child = 0;
            for (unsigned int axis = 0; axis < 3; ++axis) {
                if (axis == normal) continue;
                auto& object = faceChildren[index * 2 + child++];
                const auto childName = name + axisNames[axis] + "Axis";
                const auto childShort = shortName + "123"[axis];
                object = numeric.create(childName.c_str(), childShort.c_str(), MFnNumericData::kDouble, 1.0, &status);
                if (!status) return status;
                status = configureStaticShapeAttribute(object);
                if (!status) return status;
            }
            faceParents[index] = numeric.create(name.c_str(), shortName.c_str(), faceChildren[index * 2], faceChildren[index * 2 + 1], MObject::kNullObj, &status);
            if (!status) return status;
        }
        rootSize = numeric.create("shapeRootSize", "srs", MFnNumericData::kDouble, 1.0, &status);
        if (!status) return status;
        size = numeric.create("shapeSize", "ss", MFnNumericData::kDouble, 1.0, &status);
        if (!status) return status;
        for (const auto result : {
            translate.create("shapeTranslate", "st", Kind::distance), rotate.create("shapeRotate", "sr", Kind::angle),
            scale.create("shapeScale", "ssc", Kind::number), axisTranslate.create("shapeAxisTranslate", "sat", Kind::distance),
            axisRotate.create("shapeAxisRotate", "sar", Kind::angle), axisScale.create("shapeAxisScale", "sasc", Kind::number),
        }) if (!result) return result;
        return MS::kSuccess;
    }
    bool contains(const MObject& attribute) const {
        for (const auto& parent : faceParents) if (attribute == parent) return true;
        for (const auto& child : faceChildren) if (attribute == child) return true;
        return attribute == rootSize || attribute == size || translate.contains(attribute) || rotate.contains(attribute) ||
            scale.contains(attribute) || axisTranslate.contains(attribute) || axisRotate.contains(attribute) || axisScale.contains(attribute);
    }
    bool read(const MObject& object, AdjustmentSettings& values) const {
        MStatus status;
        for (unsigned int i = 0; i < values.faceScale.size(); ++i) {
            values.faceScale[i] = MPlug(object, faceChildren[i]).asDouble(&status);
            if (!status) return false;
        }
        values.rootSize = MPlug(object, rootSize).asDouble(&status);
        if (!status) return false;
        values.size = MPlug(object, size).asDouble(&status);
        return status && translate.read(object, values.translate) && rotate.read(object, values.rotate) &&
            scale.read(object, values.scale) && axisTranslate.read(object, values.axisTranslate) &&
            axisRotate.read(object, values.axisRotate) && axisScale.read(object, values.axisScale);
    }
};

}  // namespace bdUtilNodes::fixedCube
