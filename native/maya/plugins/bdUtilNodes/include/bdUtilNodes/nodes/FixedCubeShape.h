#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/FixedCubeAdjustment.h"
#include "bdUtilNodes/nodes/FixedCubeFin.h"
#include "bdUtilNodes/nodes/SignedShapeAxes.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <initializer_list>
#include <optional>

#include <maya/MDistance.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MPxNode.h>

namespace bdUtilNodes::fixedCube {

struct ShapeAttributes {
    MObject firstAxis;
    MObject secondAxis;
    MObject limits[3][2];
    MObject guideLine;
    MObject offsetLine;
    MObject separators[7];
    AdjustmentAttributes adjustments;
#ifndef BD_CUBE_RESEARCH_FIN
    MObject fin;
#endif
#if !defined(BD_CUBE_RESEARCH_FIN) || defined(BD_CUBE_RESEARCH_FIN_ATTRIBUTES)
    FinAttributes finAttributes;
#endif

    MStatus initialize() {
#ifdef BD_CUBE_RESEARCH_FIXED_BASE
        return MS::kSuccess;
#else
        MStatus status;
        firstAxis = createSignedAxisAttribute("shape1stAxis", "s1a", 0, status);
        if (!status) return status;
        secondAxis = createSignedAxisAttribute("shape2ndAxis", "s2a", 2, status);
        if (!status) return status;

        MFnUnitAttribute unit;
        const char* names[3][2] = {
            {"shapeBaseSpace1stAxisMinus", "shapeBaseSpace1stAxisPlus"},
            {"shapeBaseSpace2ndAxisMinus", "shapeBaseSpace2ndAxisPlus"},
            {"shapeBaseSpace3rdAxisMinus", "shapeBaseSpace3rdAxisPlus"},
        };
        const char* shortNames[3][2] = {
            {"sbsp1m", "sbsp1p"}, {"sbsp2m", "sbsp2p"}, {"sbsp3m", "sbsp3p"},
        };
        for (unsigned int axis = 0; axis < 3; ++axis) {
            for (unsigned int side : {1U, 0U}) {
                limits[axis][side] = unit.create(names[axis][side], shortNames[axis][side],
                    MDistance(0.5, MDistance::kCentimeters), &status);
                if (!status) return status;
            }
        }

        MFnNumericAttribute numeric;
        guideLine = numeric.create("shapeGuideLine", "sgl", MFnNumericData::kBoolean, false, &status);
        if (!status) return status;
        offsetLine = numeric.create("shapeOffsetLine", "sol", MFnNumericData::kBoolean, false, &status);
        if (!status) return status;

#ifndef BD_CUBE_RESEARCH_FIN
        fin = numeric.create("shapeFin", "sfn", MFnNumericData::kBoolean, false, &status);
        if (!status) return status;
#endif
#if !defined(BD_CUBE_RESEARCH_FIN) || defined(BD_CUBE_RESEARCH_FIN_ATTRIBUTES)
        status = finAttributes.create();
        if (!status) return status;
#endif
        status = adjustments.create();
        if (!status) return status;
        MFnEnumAttribute enumAttribute;
        const char* separatorNames[] = {"_", "__", "___", "____", "_____", "______", "_______"};
        for (unsigned int i = 0; i < 7; ++i) {
            separators[i] = enumAttribute.create(separatorNames[i], separatorNames[i], 0, &status);
            if (!status) return status;
            status = enumAttribute.addField("-----------------------------------", 0);
            if (!status) return status;
            status = enumAttribute.setStorable(false);
            if (!status) return status;
            status = enumAttribute.setConnectable(false);
            if (!status) return status;
            status = enumAttribute.setKeyable(false);
            if (!status) return status;
            status = enumAttribute.setChannelBox(true);
            if (!status) return status;
        }
        // 区切りは表示だけに使い、形状の dirty 判定へ含めない。
        status = MPxNode::addAttribute(separators[0]);
        if (!status) return status;
        for (const auto& attribute : {firstAxis, secondAxis}) {
            status = addStaticAttribute(attribute);
            if (!status) return status;
        }
        status = MPxNode::addAttribute(separators[1]);
        if (!status) return status;
        for (unsigned int axis = 0; axis < 3; ++axis) for (unsigned int side : {1U, 0U}) {
            status = addStaticAttribute(limits[axis][side]);
            if (!status) return status;
        }
        status = MPxNode::addAttribute(separators[2]);
        if (!status) return status;
        for (const auto& attribute : adjustments.faceParents) {
            status = addStaticAttribute(attribute);
            if (!status) return status;
        }
        status = MPxNode::addAttribute(separators[3]);
        if (!status) return status;
#ifndef BD_CUBE_RESEARCH_FIN
        status = addStaticAttribute(fin);
        if (!status) return status;
#endif
#if !defined(BD_CUBE_RESEARCH_FIN) || defined(BD_CUBE_RESEARCH_FIN_ATTRIBUTES)
        for (const auto& attribute : {finAttributes.type, finAttributes.height, finAttributes.widthScale}) {
            status = addStaticAttribute(attribute);
            if (!status) return status;
        }
#endif
        status = MPxNode::addAttribute(separators[4]);
        if (!status) return status;
        status = addStaticAttribute(guideLine);
        if (!status) return status;
        status = MPxNode::addAttribute(separators[5]);
        if (!status) return status;
        status = addStaticAttribute(offsetLine);
        if (!status) return status;
        status = MPxNode::addAttribute(separators[6]);
        if (!status) return status;
        for (const auto& attribute : {adjustments.rootSize, adjustments.translate.parent,
            adjustments.rotate.parent, adjustments.scale.parent, adjustments.axisTranslate.parent,
            adjustments.axisRotate.parent, adjustments.axisScale.parent, adjustments.size}) {
            status = addStaticAttribute(attribute);
            if (!status) return status;
        }
        return MS::kSuccess;
#endif
    }

    bool contains(const MObject& attribute) const {
#ifdef BD_CUBE_RESEARCH_FIXED_BASE
        (void)attribute;
        return false;
#else
        const bool bodyAttribute = attribute == firstAxis || attribute == secondAxis ||
            attribute == limits[0][1] || attribute == limits[0][0] ||
            attribute == limits[1][1] || attribute == limits[1][0] ||
            attribute == limits[2][1] || attribute == limits[2][0] || attribute == guideLine ||
            attribute == offsetLine || adjustments.contains(attribute);
#ifndef BD_CUBE_RESEARCH_FIN
        return bodyAttribute || attribute == fin || finAttributes.contains(attribute);
#elif defined(BD_CUBE_RESEARCH_FIN_ATTRIBUTES)
        return bodyAttribute || finAttributes.contains(attribute);
#else
        return bodyAttribute;
#endif
#endif
    }

    MStatus lockSeparators(const MObject& object) const {
        for (const auto& attribute : separators) {
            if (attribute.isNull()) continue;
            const auto status = MPlug(object, attribute).setLocked(true);
            if (!status) return status;
        }
        return MS::kSuccess;
    }

    bool readPositions(const MObject& object, MPoint (&positions)[vertexCount], bool& drawGuideLine,
        MPoint (&finPositions)[finVertexCount], bool& drawFin, bool* preciseBodyBounds = nullptr,
        std::optional<OffsetLineGeometry>* drawOffsetLine = nullptr) const {
        drawFin = false;
        if (preciseBodyBounds) *preciseBodyBounds = false;
        if (drawOffsetLine) drawOffsetLine->reset();
        AdjustmentSettings adjustment;
#ifdef BD_CUBE_RESEARCH_FIXED_BASE
        (void)object;
        drawGuideLine = false;
        constexpr short first = 0;
        constexpr short second = 2;
        constexpr double endpoints[3][2] = {{-0.5, 0.5}, {-0.5, 0.5}, {-0.5, 0.5}};
#else
        short first;
        short second;
        double endpoints[3][2];
        if (!readBaseSettings(object, first, second, endpoints, drawGuideLine, drawFin)) return false;
        if (!adjustments.read(object, adjustment)) return false;
#endif
        const auto axes = resolveSignedShapeAxes(first, second);
        const auto firstVector = axes.first.vector();
        const auto secondVector = axes.second.vector();
        const auto thirdVector = firstVector ^ secondVector;
        const FaceWarp warp(adjustment, endpoints);
        const AdjustmentTransform transform(adjustment, firstVector, secondVector, thirdVector);
        if (preciseBodyBounds) *preciseBodyBounds = warp.enabled || transform.enabled;
        for (unsigned int i = 0; i < bodyVertexCount; ++i) {
            const auto& original = vertices[i];
            const MPoint point(endpoints[0][original[0] > 0], endpoints[1][original[1] > 0], endpoints[2][original[2] > 0]);
            positions[i] = transform.point(warp.point(point));
        }
#ifdef BD_CUBE_RESEARCH_FIN
        FinSettings fin;
#ifdef BD_CUBE_RESEARCH_FIN_ATTRIBUTES
        if (!finAttributes.read(object, fin)) return false;
#endif
        writeWarpedFinPositions(positions + bodyVertexCount, fin, warp, endpoints);
        for (unsigned int i = bodyVertexCount; i < vertexCount; ++i) positions[i] = transform.point(positions[i]);
#elif !defined(BD_CUBE_RESEARCH_FIXED_BASE)
        if (drawFin) {
            FinSettings settings;
            if (!finAttributes.read(object, settings)) return false;
            drawFin = settings.height != 0.0;
            if (drawFin) {
                writeWarpedFinPositions(finPositions, settings, warp, endpoints);
                for (auto& point : finPositions) point = transform.point(point);
            }
        }
#endif
#ifndef BD_CUBE_RESEARCH_FIXED_BASE
        if (drawOffsetLine) {
            MStatus status;
            const bool enabled = MPlug(object, offsetLine).asBool(&status);
            if (!status) return false;
            if (enabled) {
                // 面倍率は limits の中点を動かさず、Fin の寸法も終点へ含めない。
                const auto center = transform.point(MPoint::origin + warp.center);
                if (hasOffsetLine(center)) *drawOffsetLine = OffsetLineGeometry{MPoint::origin, center};
            }
        }
#endif
        return true;
    }

private:
#ifndef BD_CUBE_RESEARCH_FIXED_BASE
    bool readBaseSettings(const MObject& object, short& first, short& second,
        double (&endpoints)[3][2], bool& drawGuideLine, bool& drawFin) const {
#ifdef BD_CUBE_PROFILE
        cubeResearch::profiling::Scope scope(cubeResearch::profiling::Method::baseShapeRead);
#endif
        MStatus status;
        first = MPlug(object, firstAxis).asShort(&status);
        if (!status) return false;
        second = MPlug(object, secondAxis).asShort(&status);
        if (!status) return false;

        for (unsigned int axis = 0; axis < 3; ++axis) {
            for (unsigned int side = 0; side < 2; ++side) {
                endpoints[axis][side] = MPlug(object, limits[axis][side])
                    .asMDistance(&status).asCentimeters() * (side == 0 ? -1 : 1);
                if (!status) return false;
            }
        }
        drawGuideLine = MPlug(object, guideLine).asBool(&status);
        if (!status) return false;
#ifndef BD_CUBE_RESEARCH_FIN
        drawFin = MPlug(object, fin).asBool(&status);
        if (!status) return false;
#else
        (void)drawFin;
#endif
        return true;
    }
#endif

    static MStatus addStaticAttribute(const MObject& attribute) {
        const auto status = configureStaticShapeAttribute(attribute);
        if (!status) return status;
        return MPxNode::addAttribute(attribute);
    }
};

}  // namespace bdUtilNodes::fixedCube
