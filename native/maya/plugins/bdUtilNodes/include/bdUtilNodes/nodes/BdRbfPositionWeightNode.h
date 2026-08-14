#pragma once

#include <memory>

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfPositionWeightNode final : public MPxNode {
public:
    BdRbfPositionWeightNode();
    ~BdRbfPositionWeightNode() override;

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

    static MObject pose;
    static MObject posePosition;
    static MObject posePositionX;
    static MObject posePositionY;
    static MObject posePositionZ;
    static MObject enabled;

    static MObject kernel;
    static MObject radius;
    static MObject regularization;
    static MObject allowNegativeWeights;

    static MObject outputWeight;
    static MObject isValid;
    static MObject solveStatus;

private:
    struct Cache;
    std::unique_ptr<Cache> cache_;
};
