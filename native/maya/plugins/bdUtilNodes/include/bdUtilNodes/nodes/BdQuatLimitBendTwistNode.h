#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdQuatLimitBendTwistNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();
    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;
    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject inputQuat;
    static MObject inputQuatX;
    static MObject inputQuatY;
    static MObject inputQuatZ;
    static MObject inputQuatW;

    static MObject axisQuat;
    static MObject axisQuatX;
    static MObject axisQuatY;
    static MObject axisQuatZ;
    static MObject axisQuatW;

    static MObject order;
    static MObject bendLimitMode;

    static MObject minimum;
    static MObject minTwist;
    static MObject minBendH;
    static MObject minBendV;

    static MObject maximum;
    static MObject maxTwist;
    static MObject maxBendH;
    static MObject maxBendV;

    static MObject output;
    static MObject outputTwist;
    static MObject outputBendH;
    static MObject outputBendV;

    static MObject outputQuat;
    static MObject outputQuatX;
    static MObject outputQuatY;
    static MObject outputQuatZ;
    static MObject outputQuatW;
};
