#pragma once

#include <atomic>
#include <cstdint>
#include <memory>
#include <vector>

#include <maya/MBoundingBox.h>
#include <maya/MMessage.h>
#include <maya/MNodeMessage.h>
#include <maya/MObject.h>
#include <maya/MPoint.h>
#include <maya/MPointArray.h>
#include <maya/MPxLocatorNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

namespace MHWRender {
class MPxDrawOverride;
}

enum class StrokeStyle : unsigned char {
    Normal,
    Template,
    AxisX,
    AxisY,
    AxisZ,
};

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
        struct FillPart {
            MPointArray triangles;
            StrokeStyle style = StrokeStyle::Normal;
        };
        std::vector<MPointArray> strokes;
        std::vector<StrokeStyle> strokeStyles;
        std::vector<FillPart> fillParts;
        std::vector<MPointArray> boundsPreview;
        MPointArray offsetLine;
        MPoint offsetLineEndpoint = MPoint::origin;
        MBoundingBox bounds;
        MBoundingBox focusBounds;
        MBoundingBox drawBounds;
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
    static MObject shapeAnimationTransformMatrix;
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

    static MObject shapeAxisOffsetLength;
    static MObject shapeAxisOffset;
    static MObject shapeAxisOffsetDirection;

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
    static MObject shapeLineWidth;
    static MObject shapeTransparency;
    static MObject shapeFillTransparency;
    static MObject shapeDrawOnTop;

    static MObject boundsMode;
    static MObject showBoundsPreview;
    static MObject customBounds1stAxis;
    static MObject customBounds2ndAxis;
    static MObject customBoundsRootSize;
    static MObject customBoundsTranslate;
    static MObject customBoundsTranslateX;
    static MObject customBoundsTranslateY;
    static MObject customBoundsTranslateZ;
    static MObject customBoundsRotate;
    static MObject customBoundsRotateX;
    static MObject customBoundsRotateY;
    static MObject customBoundsRotateZ;
    static MObject customBoundsScale;
    static MObject customBoundsScaleX;
    static MObject customBoundsScaleY;
    static MObject customBoundsScaleZ;
    static MObject customBoundsAxisOffsetLength;
    static MObject customBoundsAxisOffset;
    static MObject customBoundsAxisOffsetDirection;
    static MObject customBoundsAxisTranslate;
    static MObject customBoundsAxisTranslateX;
    static MObject customBoundsAxisTranslateY;
    static MObject customBoundsAxisTranslateZ;
    static MObject customBoundsAxisRotate;
    static MObject customBoundsAxisRotateX;
    static MObject customBoundsAxisRotateY;
    static MObject customBoundsAxisRotateZ;
    static MObject customBoundsAxisScale;
    static MObject customBoundsAxisScaleX;
    static MObject customBoundsAxisScaleY;
    static MObject customBoundsAxisScaleZ;
    static MObject customBoundsSize;

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
    std::atomic<std::uint64_t> animationRevision_{1};
    std::atomic<std::uint64_t> boundsRevision_{1};
    MCallbackId attributeChangedCallback_ = 0;
};
