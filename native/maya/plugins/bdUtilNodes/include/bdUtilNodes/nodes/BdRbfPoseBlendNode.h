#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdRbfPoseBlendNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    MStatus compute(const MPlug& plug, MDataBlock& dataBlock) override;

    SchedulingType schedulingType() const override;

    static const MString typeName;
    static const MTypeId typeId;

    static MObject baseTranslate;
    static MObject baseTranslateX;
    static MObject baseTranslateY;
    static MObject baseTranslateZ;

    static MObject baseRotate;
    static MObject baseRotateX;
    static MObject baseRotateY;
    static MObject baseRotateZ;

    static MObject baseScale;
    static MObject baseScaleX;
    static MObject baseScaleY;
    static MObject baseScaleZ;

    static MObject rotateOrder;

    static MObject pose;
    static MObject poseTranslate;
    static MObject poseTranslateX;
    static MObject poseTranslateY;
    static MObject poseTranslateZ;
    static MObject poseRotate;
    static MObject poseRotateX;
    static MObject poseRotateY;
    static MObject poseRotateZ;
    static MObject poseScale;
    static MObject poseScaleX;
    static MObject poseScaleY;
    static MObject poseScaleZ;
    static MObject enabled;

    static MObject weight;

    static MObject outputTranslate;
    static MObject outputTranslateX;
    static MObject outputTranslateY;
    static MObject outputTranslateZ;

    static MObject outputRotate;
    static MObject outputRotateX;
    static MObject outputRotateY;
    static MObject outputRotateZ;

    static MObject outputQuat;
    static MObject outputQuatX;
    static MObject outputQuatY;
    static MObject outputQuatZ;
    static MObject outputQuatW;

    static MObject outputScale;
    static MObject outputScaleX;
    static MObject outputScaleY;
    static MObject outputScaleZ;

    static MObject isValid;
    static MObject blendStatus;
};

