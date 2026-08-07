#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdQuatComposeBendTwistNode final : public MPxNode {
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

    static MObject axisQuat;
    static MObject axisQuatX;
    static MObject axisQuatY;
    static MObject axisQuatZ;
    static MObject axisQuatW;

    static MObject order;

    static MObject outputQuat;
    static MObject outputQuatX;
    static MObject outputQuatY;
    static MObject outputQuatZ;
    static MObject outputQuatW;
};
