#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDbl3SubtractNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(
        const MPlug& plug,
        MDataBlock& dataBlock
    ) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject input1;
    static MObject input1X;
    static MObject input1Y;
    static MObject input1Z;

    static MObject input2;
    static MObject input2X;
    static MObject input2Y;
    static MObject input2Z;

    static MObject output;
    static MObject outputX;
    static MObject outputY;
    static MObject outputZ;
};
