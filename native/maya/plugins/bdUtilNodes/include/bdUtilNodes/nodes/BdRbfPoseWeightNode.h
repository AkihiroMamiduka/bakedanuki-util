#pragma once

#include <memory>

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfPoseWeightNode final : public MPxNode {
public:
    BdRbfPoseWeightNode();
    ~BdRbfPoseWeightNode() override;

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

    static MObject pose;
    static MObject poseQuat;
    static MObject poseQuatX;
    static MObject poseQuatY;
    static MObject poseQuatZ;
    static MObject poseQuatW;
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
