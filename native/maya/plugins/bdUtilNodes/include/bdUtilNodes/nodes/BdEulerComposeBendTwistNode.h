#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdEulerComposeBendTwistNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();
    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;
    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject input;
    static MObject inputTwist;
    static MObject inputBendH;
    static MObject inputBendV;

    static MObject axisRotate;
    static MObject axisRotateX;
    static MObject axisRotateY;
    static MObject axisRotateZ;
    static MObject axisRotateOrder;

    static MObject order;
    static MObject outputRotateOrder;

    static MObject outputRotate;
    static MObject outputRotateX;
    static MObject outputRotateY;
    static MObject outputRotateZ;
};
