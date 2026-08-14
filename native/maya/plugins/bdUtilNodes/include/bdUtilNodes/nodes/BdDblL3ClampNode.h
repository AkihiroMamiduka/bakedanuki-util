#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDblL3ClampNode final : public MPxNode {
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

    static MObject minimum;
    static MObject minimumX;
    static MObject minimumY;
    static MObject minimumZ;

    static MObject maximum;
    static MObject maximumX;
    static MObject maximumY;
    static MObject maximumZ;

    static MObject output;
    static MObject outputX;
    static MObject outputY;
    static MObject outputZ;
};
