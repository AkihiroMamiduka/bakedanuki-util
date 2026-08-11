#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfPositionFalloffWeightNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject inputPosition;
    static MObject inputPositionX;
    static MObject inputPositionY;
    static MObject inputPositionZ;

    static MObject innerRadius;
    static MObject outerRadius;
    static MObject falloff;

    static MObject pose;
    static MObject posePosition;
    static MObject posePositionX;
    static MObject posePositionY;
    static MObject posePositionZ;
    static MObject enabled;
    static MObject useRadiusOverride;
    static MObject innerRadiusOverride;
    static MObject outerRadiusOverride;

    static MObject outputWeight;
    static MObject isValid;
    static MObject falloffStatus;
};
