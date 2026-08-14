#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfOrientationFalloffWeightNode final : public MPxNode {
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

    static MObject innerRadius;
    static MObject outerRadius;
    static MObject falloff;

    static MObject pose;
    static MObject poseQuat;
    static MObject poseQuatX;
    static MObject poseQuatY;
    static MObject poseQuatZ;
    static MObject poseQuatW;
    static MObject enabled;
    static MObject useRadiusOverride;
    static MObject innerRadiusOverride;
    static MObject outerRadiusOverride;

    static MObject outputWeight;
    static MObject isValid;
    static MObject falloffStatus;
};
