#pragma once

#include <maya/MBoundingBox.h>
#include <maya/MObject.h>
#include <maya/MPxLocatorNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

namespace MHWRender {
class MPxDrawOverride;
}

class BdControllerShapeNode final : public MPxLocatorNode {
public:
    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxDrawOverride* createDrawOverride(const MObject& node);

    void postConstructor() override;
    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    bool excludeAsLocator() const override;

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

    static MObject shape;
    static MObject shapeRootSize;

    static MObject shapeTranslate;
    static MObject shapeTranslateX;
    static MObject shapeTranslateY;
    static MObject shapeTranslateZ;

    static MObject shapeRotate;
    static MObject shapeRotateX;
    static MObject shapeRotateY;
    static MObject shapeRotateZ;

    static MObject shapeScale;
    static MObject shapeScaleX;
    static MObject shapeScaleY;
    static MObject shapeScaleZ;

    static MObject shapeSize;
};
