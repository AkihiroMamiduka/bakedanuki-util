#pragma once

#include <memory>

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfMultiOrientationFalloffWeightNode final : public MPxNode {
public:
    BdRbfMultiOrientationFalloffWeightNode();
    ~BdRbfMultiOrientationFalloffWeightNode() override;

    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject source;
    static MObject inputQuat;
    static MObject inputQuatX;
    static MObject inputQuatY;
    static MObject inputQuatZ;
    static MObject inputQuatW;
    static MObject influence;

    static MObject innerRadius;
    static MObject outerRadius;
    static MObject falloff;

    static MObject pose;
    static MObject sourceQuat;
    static MObject sourceQuatX;
    static MObject sourceQuatY;
    static MObject sourceQuatZ;
    static MObject sourceQuatW;
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
