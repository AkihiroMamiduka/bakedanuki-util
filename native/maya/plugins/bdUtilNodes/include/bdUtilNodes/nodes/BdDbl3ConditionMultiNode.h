#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDbl3ConditionMultiNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject input;
    static MObject caseArray;
    static MObject operation;
    static MObject compare;

    static MObject value;
    static MObject valueX;
    static MObject valueY;
    static MObject valueZ;

    static MObject elseValue;
    static MObject elseValueX;
    static MObject elseValueY;
    static MObject elseValueZ;

    static MObject output;
    static MObject outputX;
    static MObject outputY;
    static MObject outputZ;
};
