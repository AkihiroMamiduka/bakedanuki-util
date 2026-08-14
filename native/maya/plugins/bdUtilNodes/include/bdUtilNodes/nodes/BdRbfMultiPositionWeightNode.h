#pragma once

#include <memory>

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfMultiPositionWeightNode final : public MPxNode {
public:
    BdRbfMultiPositionWeightNode();
    ~BdRbfMultiPositionWeightNode() override;

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

    static MObject pose;
    static MObject sourcePosition;
    static MObject sourcePositionX;
    static MObject sourcePositionY;
    static MObject sourcePositionZ;
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
