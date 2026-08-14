#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDbl3MapRangeNode final : public MPxNode {
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

    static MObject input;
    static MObject inputX;
    static MObject inputY;
    static MObject inputZ;

    static MObject sourceMinimum;
    static MObject sourceMinimumX;
    static MObject sourceMinimumY;
    static MObject sourceMinimumZ;

    static MObject sourceMaximum;
    static MObject sourceMaximumX;
    static MObject sourceMaximumY;
    static MObject sourceMaximumZ;

    static MObject targetMinimum;
    static MObject targetMinimumX;
    static MObject targetMinimumY;
    static MObject targetMinimumZ;

    static MObject targetMaximum;
    static MObject targetMaximumX;
    static MObject targetMaximumY;
    static MObject targetMaximumZ;

    static MObject clamp;

    static MObject output;
    static MObject outputX;
    static MObject outputY;
    static MObject outputZ;
};
