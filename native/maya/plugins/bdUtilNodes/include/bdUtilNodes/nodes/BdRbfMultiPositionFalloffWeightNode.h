#pragma once

#include <memory>

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfMultiPositionFalloffWeightNode final : public MPxNode {
public:
    BdRbfMultiPositionFalloffWeightNode();
    ~BdRbfMultiPositionFalloffWeightNode() override;

    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject source;
    static MObject inputPosition;
    static MObject inputPositionX;
    static MObject inputPositionY;
    static MObject inputPositionZ;
    static MObject influence;

    static MObject innerRadius;
    static MObject outerRadius;
    static MObject falloff;

    static MObject pose;
    static MObject sourcePosition;
    static MObject sourcePositionX;
    static MObject sourcePositionY;
    static MObject sourcePositionZ;
    static MObject enabled;
    static MObject useRadiusOverride;
    static MObject innerRadiusOverride;
    static MObject outerRadiusOverride;

    static MObject outputWeight;
    static MObject isValid;
    static MObject falloffStatus;

private:
    struct Cache;
    std::unique_ptr<Cache> cache_;
};
