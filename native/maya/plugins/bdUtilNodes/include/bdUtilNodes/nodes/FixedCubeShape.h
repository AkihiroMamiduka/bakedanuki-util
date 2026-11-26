#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/FixedCubeFin.h"
#include "bdUtilNodes/nodes/SignedShapeAxes.h"
#ifdef BD_CUBE_PROFILE
#include "CubeDiagnostics.h"
#endif

#include <initializer_list>

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

        // 両ノードで基準形状の設定順と Channel Box の表示順を揃える。
        for (const auto& attribute : {
            firstAxis, secondAxis, limits[0][1], limits[0][0], limits[1][1], limits[1][0],
            limits[2][1], limits[2][0], guideLine,
        }) {
            status = addStaticAttribute(attribute);
            if (!status) return status;
        }
#ifndef BD_CUBE_RESEARCH_FIN
        fin = numeric.create("shapeFin", "sfn", MFnNumericData::kBoolean, false, &status);
        if (!status) return status;
        status = addStaticAttribute(fin);
        if (!status) return status;
#endif
#if !defined(BD_CUBE_RESEARCH_FIN) || defined(BD_CUBE_RESEARCH_FIN_ATTRIBUTES)
        status = finAttributes.create();
        if (!status) return status;
        for (const auto& attribute : {finAttributes.type, finAttributes.height, finAttributes.widthScale}) {
            status = addStaticAttribute(attribute);
            if (!status) return status;
        }
#endif
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
            attribute == limits[2][1] || attribute == limits[2][0] || attribute == guideLine;
#ifndef BD_CUBE_RESEARCH_FIN
        return bodyAttribute || attribute == fin || finAttributes.contains(attribute);
#elif defined(BD_CUBE_RESEARCH_FIN_ATTRIBUTES)
        return bodyAttribute || finAttributes.contains(attribute);
#else
        return bodyAttribute;
#endif
#endif
    }

    bool readPositions(const MObject& object, MPoint (&positions)[vertexCount], bool& drawGuideLine,
        MPoint (&finPositions)[finVertexCount], bool& drawFin) const {
        drawFin = false;
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
#endif
        const auto axes = resolveSignedShapeAxes(first, second);
        const auto firstVector = axes.first.vector();
        const auto secondVector = axes.second.vector();
        const auto thirdVector = firstVector ^ secondVector;
        for (unsigned int i = 0; i < bodyVertexCount; ++i) {
            const auto& original = vertices[i];
            positions[i] = MPoint::origin + firstVector * endpoints[0][original[0] > 0] +
                secondVector * endpoints[1][original[1] > 0] +
                thirdVector * endpoints[2][original[2] > 0];
        }
#ifdef BD_CUBE_RESEARCH_FIN
        FinSettings fin;
#ifdef BD_CUBE_RESEARCH_FIN_ATTRIBUTES
        if (!finAttributes.read(object, fin)) return false;
#endif
        writeFinPositions(positions + bodyVertexCount, fin, firstVector, secondVector, thirdVector, endpoints);
#elif !defined(BD_CUBE_RESEARCH_FIXED_BASE)
        if (drawFin) {
            FinSettings settings;
            if (!finAttributes.read(object, settings)) return false;
            drawFin = settings.height != 0.0;
            if (drawFin) {
                writeFinPositions(finPositions, settings, firstVector, secondVector, thirdVector, endpoints);
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
        MStatus status;
        MFnAttribute fn(attribute, &status);
        if (!status) return status;
        status = fn.setKeyable(false);
        if (!status) return status;
        status = fn.setConnectable(false);
        if (!status) return status;
        status = fn.setChannelBox(true);
        if (!status) return status;
        status = fn.setInternal(true);
        if (!status) return status;
        status = fn.setAffectsAppearance(true);
        if (!status) return status;
        status = fn.setAffectsWorldSpace(true);
        if (!status) return status;
        return MPxNode::addAttribute(attribute);
    }
};

}  // namespace bdUtilNodes::fixedCube
