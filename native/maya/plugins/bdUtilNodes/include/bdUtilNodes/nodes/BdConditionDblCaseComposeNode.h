#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdConditionDblCaseComposeNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject operation;
    static MObject compare;
    static MObject extra;
    static MObject logic;
    static MObject comparison;
    static MObject compareValue;
    static MObject value;

    static MObject output;
    static MObject outputOperation;
    static MObject outputCompare;
    static MObject outputExtra;
    static MObject outputLogic;
    static MObject outputComparison;
    static MObject outputCompareValue;
    static MObject outputValue;
};
