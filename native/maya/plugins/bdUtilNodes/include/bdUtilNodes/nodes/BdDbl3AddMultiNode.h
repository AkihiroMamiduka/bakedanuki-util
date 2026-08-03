#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDbl3AddMultiNode final : public MPxNode {
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

    static MObject output;
    static MObject outputX;
    static MObject outputY;
    static MObject outputZ;
};
