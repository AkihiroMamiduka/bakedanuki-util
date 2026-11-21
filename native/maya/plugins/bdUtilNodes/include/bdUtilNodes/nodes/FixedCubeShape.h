#pragma once

#include "bdUtilNodes/draw/FixedCubeGeometry.h"
#include "bdUtilNodes/nodes/SignedShapeAxes.h"

#include <initializer_list>

#include <maya/MDistance.h>
#include <maya/MFnAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MPxNode.h>

namespace bdUtilNodes::fixedCube {

struct ShapeAttributes {
    MObject firstAxis;
    MObject secondAxis;
    MObject limits[3][2];

    MStatus initialize() {
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

        // 両ノードで基準形状の設定順と Channel Box の表示順を揃える。
        for (const auto& attribute : {
            firstAxis, secondAxis, limits[0][1], limits[0][0], limits[1][1], limits[1][0],
            limits[2][1], limits[2][0],
        }) {
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
            status = MPxNode::addAttribute(attribute);
            if (!status) return status;
        }
        return MS::kSuccess;
    }

    bool contains(const MObject& attribute) const {
        return attribute == firstAxis || attribute == secondAxis ||
            attribute == limits[0][1] || attribute == limits[0][0] ||
            attribute == limits[1][1] || attribute == limits[1][0] ||
            attribute == limits[2][1] || attribute == limits[2][0];
    }

    bool readPositions(const MObject& object, MPoint (&positions)[8]) const {
        MStatus status;
        const short first = MPlug(object, firstAxis).asShort(&status);
        if (!status) return false;
        const short second = MPlug(object, secondAxis).asShort(&status);
        if (!status) return false;

        double endpoints[3][2];
        for (unsigned int axis = 0; axis < 3; ++axis) {
            for (unsigned int side = 0; side < 2; ++side) {
                endpoints[axis][side] = MPlug(object, limits[axis][side])
                    .asMDistance(&status).asCentimeters() * (side == 0 ? -1 : 1);
                if (!status) return false;
            }
        }
        const auto axes = resolveSignedShapeAxes(first, second);
        const auto firstVector = axes.first.vector();
        const auto secondVector = axes.second.vector();
        const auto thirdVector = firstVector ^ secondVector;
        for (unsigned int i = 0; i < 8; ++i) {
            const auto& original = vertices[i];
            positions[i] = MPoint::origin + firstVector * endpoints[0][original[0] > 0] +
                secondVector * endpoints[1][original[1] > 0] +
                thirdVector * endpoints[2][original[2] > 0];
        }
        return true;
    }
};

}  // namespace bdUtilNodes::fixedCube
