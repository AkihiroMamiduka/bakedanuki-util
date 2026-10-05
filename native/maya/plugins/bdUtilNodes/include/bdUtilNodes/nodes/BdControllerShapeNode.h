#pragma once

#include <atomic>
#include <cstdint>
#include <memory>
#include <vector>

#include <maya/MBoundingBox.h>
#include <maya/MMessage.h>
#include <maya/MNodeMessage.h>
#include <maya/MObject.h>
#include <maya/MPointArray.h>
#include <maya/MPxLocatorNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

namespace MHWRender {
class MPxDrawOverride;
}

class BdControllerShapeNode final : public MPxLocatorNode {
public:
    BdControllerShapeNode();
    ~BdControllerShapeNode() override;

    static void* creator();
    static MStatus initialize();
    static MHWRender::MPxDrawOverride* createDrawOverride(const MObject& node);

    void postConstructor() override;
    bool isBounded() const override;
    MBoundingBox boundingBox() const override;
    bool excludeAsLocator() const override;

    struct Geometry {
        std::vector<MPointArray> strokes;
        MPointArray offsetLine;
        MBoundingBox bounds;
        bool offsetLineTemplate = false;
    };

    std::shared_ptr<const Geometry> geometry() const;

    static const MString typeName;
    static const MTypeId typeId;
    static const MString drawClassification;
    static const MString drawRegistrantId;

    static MObject shape;
    static MObject shape1stAxis;
    static MObject shape2ndAxis;
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

    static MObject shapeAxisTranslate;
    static MObject shapeAxisTranslateX;
    static MObject shapeAxisTranslateY;
    static MObject shapeAxisTranslateZ;

    static MObject shapeAxisRotate;
    static MObject shapeAxisRotateX;
    static MObject shapeAxisRotateY;
    static MObject shapeAxisRotateZ;

    static MObject shapeAxisScale;
    static MObject shapeAxisScaleX;
    static MObject shapeAxisScaleY;
    static MObject shapeAxisScaleZ;

    static MObject shapeSize;
    static MObject showShapeOffsetLine;
    static MObject shapeOffsetLineTemplate;

private:
    static void onAttributeChanged(
        MNodeMessage::AttributeMessage change,
        MPlug& plug,
        MPlug& otherPlug,
        void* clientData
    );
    struct GeometryCache;
    std::unique_ptr<GeometryCache> geometryCache_;
    std::atomic<std::uint64_t> geometryRevision_{1};
    MCallbackId attributeChangedCallback_ = 0;
};
