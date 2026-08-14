#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdEulerDecomposeTwistNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();
    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;
    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject inputRotate;
    static MObject inputRotateX;
    static MObject inputRotateY;
    static MObject inputRotateZ;
    static MObject inputRotateOrder;

    static MObject axisRotate;
    static MObject axisRotateX;
    static MObject axisRotateY;
    static MObject axisRotateZ;
    static MObject axisRotateOrder;

    static MObject outputTwist;
};
