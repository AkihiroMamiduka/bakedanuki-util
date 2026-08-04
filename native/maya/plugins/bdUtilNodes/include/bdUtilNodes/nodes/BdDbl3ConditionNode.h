#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDbl3ConditionNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject input;
    static MObject operation;
    static MObject compare;

    static MObject trueValue;
    static MObject trueValueX;
    static MObject trueValueY;
    static MObject trueValueZ;

    static MObject falseValue;
    static MObject falseValueX;
    static MObject falseValueY;
    static MObject falseValueZ;

    static MObject output;
    static MObject outputX;
    static MObject outputY;
    static MObject outputZ;
};
