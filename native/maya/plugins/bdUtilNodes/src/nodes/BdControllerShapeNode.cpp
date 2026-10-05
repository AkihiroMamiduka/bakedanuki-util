#include "bdUtilNodes/nodes/BdControllerShapeNode.h"

#include <array>
#include <cmath>
#include <cstddef>
#include <utility>
#include <vector>

#include <maya/M3dView.h>
#include <maya/MAngle.h>
#include <maya/MColor.h>
#include <maya/MDagPath.h>
#include <maya/MDistance.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MFrameContext.h>
#include <maya/MHWGeometryUtilities.h>
#include <maya/MPxDrawOverride.h>
#include <maya/MPlug.h>
#include <maya/MPoint.h>
#include <maya/MPointArray.h>
#include <maya/MQuaternion.h>
#include <maya/MUIDrawManager.h>
#include <maya/MUserData.h>
#include <maya/MVector.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/RotateAttribute.h"

const MString BdControllerShapeNode::typeName("bdControllerShape");
const MTypeId BdControllerShapeNode::typeId(0x0014271F);
const MString BdControllerShapeNode::drawClassification(
    "drawdb/geometry/bdControllerShape"
);
const MString BdControllerShapeNode::drawRegistrantId(
    "bdControllerShapeDrawOverride"
);

MObject BdControllerShapeNode::shape;
MObject BdControllerShapeNode::shapeRootSize;
MObject BdControllerShapeNode::shapeTranslate;
MObject BdControllerShapeNode::shapeTranslateX;
MObject BdControllerShapeNode::shapeTranslateY;
MObject BdControllerShapeNode::shapeTranslateZ;
MObject BdControllerShapeNode::shapeRotate;
MObject BdControllerShapeNode::shapeRotateX;
MObject BdControllerShapeNode::shapeRotateY;
MObject BdControllerShapeNode::shapeRotateZ;
MObject BdControllerShapeNode::shapeScale;
MObject BdControllerShapeNode::shapeScaleX;
MObject BdControllerShapeNode::shapeScaleY;
MObject BdControllerShapeNode::shapeScaleZ;
MObject BdControllerShapeNode::shapeSize;
MObject BdControllerShapeNode::showShapeOffsetLine;
MObject BdControllerShapeNode::shapeOffsetLineTemplate;

namespace {

constexpr double kPi = 3.14159265358979323846;
constexpr unsigned int kCircleSegments = 64;

using Stroke = MPointArray;
using Strokes = std::vector<Stroke>;

struct ShapeSettings {
    short shape = 0;
    double rootSize = 1.0;
    MVector translate = MVector(0.0, 0.0, 0.0);
    MQuaternion rotate;
    MVector scale = MVector(1.0, 1.0, 1.0);
    double size = 1.0;
    bool showOffsetLine = false;
    bool offsetLineTemplate = false;
};

bool readSettings(const MObject& node, ShapeSettings& settings) {
    MStatus status;
    settings.shape = MPlug(node, BdControllerShapeNode::shape).asShort(&status);
    if (!status) {
        return false;
    }
    settings.rootSize =
        MPlug(node, BdControllerShapeNode::shapeRootSize).asDouble(&status);
    if (!status) {
        return false;
    }

    const MPlug translate(node, BdControllerShapeNode::shapeTranslate);
    settings.translate.x = translate.child(0).asMDistance(&status).asCentimeters();
    if (!status) {
        return false;
    }
    settings.translate.y = translate.child(1).asMDistance(&status).asCentimeters();
    if (!status) {
        return false;
    }
    settings.translate.z = translate.child(2).asMDistance(&status).asCentimeters();
    if (!status) {
        return false;
    }

    const MPlug rotate(node, BdControllerShapeNode::shapeRotate);
    const double rotateX = rotate.child(0).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    const double rotateY = rotate.child(1).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    const double rotateZ = rotate.child(2).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    settings.rotate = MEulerRotation(
        rotateX, rotateY, rotateZ, MEulerRotation::kXYZ
    ).asQuaternion();

    const MPlug scale(node, BdControllerShapeNode::shapeScale);
    settings.scale.x = scale.child(0).asDouble(&status);
    if (!status) {
        return false;
    }
    settings.scale.y = scale.child(1).asDouble(&status);
    if (!status) {
        return false;
    }
    settings.scale.z = scale.child(2).asDouble(&status);
    if (!status) {
        return false;
    }
    settings.size = MPlug(node, BdControllerShapeNode::shapeSize).asDouble(&status);
    if (!status) {
        return false;
    }
    settings.showOffsetLine =
        MPlug(node, BdControllerShapeNode::showShapeOffsetLine).asBool(&status);
    if (!status) {
        return false;
    }
    settings.offsetLineTemplate =
        MPlug(node, BdControllerShapeNode::shapeOffsetLineTemplate).asBool(&status);
    return status == MS::kSuccess;
}

MPoint transformPoint(const MPoint& point, const ShapeSettings& settings) {
    const MVector scaled(
        point.x * settings.size * settings.scale.x,
        point.y * settings.size * settings.scale.y,
        point.z * settings.size * settings.scale.z
    );
    const MVector rotated = scaled.rotateBy(settings.rotate);
    return MPoint(
        settings.rootSize * (settings.translate.x + rotated.x),
        settings.rootSize * (settings.translate.y + rotated.y),
        settings.rootSize * (settings.translate.z + rotated.z)
    );
}

bool hasOffsetLine(const MPoint& endpoint) {
    return endpoint.x != 0.0 || endpoint.y != 0.0 || endpoint.z != 0.0;
}

template <std::size_t Count>
void appendStroke(
    const std::array<MPoint, Count>& points,
    const ShapeSettings& settings,
    Strokes& strokes
) {
    Stroke stroke;
    for (const MPoint& point : points) {
        stroke.append(transformPoint(point, settings));
    }
    strokes.push_back(std::move(stroke));
}

void appendSquare(const ShapeSettings& settings, Strokes& strokes) {
    appendStroke(
        std::array<MPoint, 5>{
            MPoint(-0.5, -0.5, 0.0),
            MPoint(0.5, -0.5, 0.0),
            MPoint(0.5, 0.5, 0.0),
            MPoint(-0.5, 0.5, 0.0),
            MPoint(-0.5, -0.5, 0.0),
        },
        settings,
        strokes
    );
}

void appendCube(const ShapeSettings& settings, Strokes& strokes) {
    const std::array<MPoint, 8> corners = {
        MPoint(-0.5, -0.5, -0.5),
        MPoint(0.5, -0.5, -0.5),
        MPoint(0.5, 0.5, -0.5),
        MPoint(-0.5, 0.5, -0.5),
        MPoint(-0.5, -0.5, 0.5),
        MPoint(0.5, -0.5, 0.5),
        MPoint(0.5, 0.5, 0.5),
        MPoint(-0.5, 0.5, 0.5),
    };
    constexpr std::array<std::array<int, 2>, 12> edges = {{
        {{0, 1}}, {{1, 2}}, {{2, 3}}, {{3, 0}},
        {{4, 5}}, {{5, 6}}, {{6, 7}}, {{7, 4}},
        {{0, 4}}, {{1, 5}}, {{2, 6}}, {{3, 7}},
    }};
    for (const auto& edge : edges) {
        appendStroke(
            std::array<MPoint, 2>{corners[edge[0]], corners[edge[1]]},
            settings,
            strokes
        );
    }
}

void appendCircle(
    double radius,
    const ShapeSettings& settings,
    Strokes& strokes
) {
    Stroke stroke;
    for (unsigned int index = 0; index <= kCircleSegments; ++index) {
        const double angle = 2.0 * kPi * index / kCircleSegments;
        stroke.append(transformPoint(
            MPoint(radius * std::cos(angle), radius * std::sin(angle), 0.0),
            settings
        ));
    }
    strokes.push_back(std::move(stroke));
}

void appendCircleArrow(const ShapeSettings& settings, Strokes& strokes) {
    appendCircle(0.32, settings, strokes);
    appendStroke(
        std::array<MPoint, 4>{
            MPoint(-0.1, 0.38, 0.0),
            MPoint(0.0, 0.5, 0.0),
            MPoint(0.1, 0.38, 0.0),
            MPoint(-0.1, 0.38, 0.0),
        },
        settings,
        strokes
    );
}

Strokes makeStrokes(const ShapeSettings& settings) {
    Strokes strokes;
    switch (settings.shape) {
        case 0:
            appendSquare(settings, strokes);
            break;
        case 1:
            appendCube(settings, strokes);
            break;
        case 2:
            appendCircle(0.5, settings, strokes);
            break;
        case 3:
            appendCircleArrow(settings, strokes);
            break;
        default:
            break;
    }
    return strokes;
}

MBoundingBox boundsForStrokes(const Strokes& strokes) {
    MBoundingBox box;
    bool hasPoint = false;
    for (const Stroke& stroke : strokes) {
        for (unsigned int index = 0; index < stroke.length(); ++index) {
            box.expand(stroke[index]);
            hasPoint = true;
        }
    }
    if (!hasPoint) {
        return MBoundingBox(MPoint::origin, MPoint::origin);
    }
    return box;
}

MBoundingBox nodeBounds(const MObject& node) {
    ShapeSettings settings;
    if (!readSettings(node, settings)) {
        return MBoundingBox(MPoint::origin, MPoint::origin);
    }
    MBoundingBox box = boundsForStrokes(makeStrokes(settings));
    if (settings.showOffsetLine) {
        const MPoint endpoint = transformPoint(MPoint::origin, settings);
        if (hasOffsetLine(endpoint)) {
            box.expand(MPoint::origin);
            box.expand(endpoint);
        }
    }
    return box;
}

struct ShapeDrawData final : public MUserData {
    Strokes strokes;
    MPointArray offsetLine;
    bool offsetLineTemplate = false;
    MColor color;
    MColor offsetLineColor;
};

class ControllerShapeDrawOverride final : public MHWRender::MPxDrawOverride {
public:
    explicit ControllerShapeDrawOverride(const MObject& node)
        : MPxDrawOverride(node, nullptr, true) {}

    MHWRender::DrawAPI supportedDrawAPIs() const override {
        return MHWRender::kAllDevices;
    }

    bool hasUIDrawables() const override {
        return true;
    }

    bool isBounded(const MDagPath&, const MDagPath&) const override {
        return true;
    }

    MBoundingBox boundingBox(
        const MDagPath& objectPath,
        const MDagPath&
    ) const override {
        return nodeBounds(objectPath.node());
    }

    MUserData* prepareForDraw(
        const MDagPath& objectPath,
        const MDagPath&,
        const MHWRender::MFrameContext&,
        MUserData* oldData
    ) override {
        ShapeDrawData* data = oldData
            ? static_cast<ShapeDrawData*>(oldData)
            : new ShapeDrawData();
        ShapeSettings settings;
        const bool hasSettings = readSettings(objectPath.node(), settings);
        data->strokes = hasSettings ? makeStrokes(settings) : Strokes();
        data->offsetLine.clear();
        data->offsetLineTemplate = hasSettings && settings.offsetLineTemplate;
        if (hasSettings && settings.showOffsetLine) {
            const MPoint endpoint = transformPoint(MPoint::origin, settings);
            if (hasOffsetLine(endpoint)) {
                data->offsetLine.append(MPoint::origin);
                data->offsetLine.append(endpoint);
            }
        }
        data->color = MHWRender::MGeometryUtilities::wireframeColor(objectPath);
        if (data->offsetLine.length() == 2) {
            data->offsetLineColor = data->color;
            if (data->offsetLineTemplate) {
                MStatus colorStatus;
                const MColor templateColor = M3dView::templateColor(&colorStatus);
                if (colorStatus) {
                    data->offsetLineColor = templateColor;
                }
            }
        }
        return data;
    }

    void addUIDrawables(
        const MDagPath&,
        MHWRender::MUIDrawManager& drawManager,
        const MHWRender::MFrameContext& frameContext,
        const MUserData* userData
    ) override {
        if (frameContext.objectTypeExclusions() &
            MHWRender::MFrameContext::kExcludePluginShapes) {
            return;
        }
        const ShapeDrawData* data = static_cast<const ShapeDrawData*>(userData);
        if (!data) {
            return;
        }
        drawManager.beginDrawable();
        drawManager.setColor(data->color);
        for (const Stroke& stroke : data->strokes) {
            drawManager.lineStrip(stroke, false);
        }
        drawManager.endDrawable();
        if (data->offsetLine.length() == 2) {
            drawManager.beginDrawable(
                data->offsetLineTemplate
                    ? MHWRender::MUIDrawManager::kNonSelectable
                    : MHWRender::MUIDrawManager::kSelectable
            );
            drawManager.setColor(data->offsetLineColor);
            drawManager.lineStrip(data->offsetLine, false);
            drawManager.endDrawable();
        }
    }
};

}  // namespace

void* BdControllerShapeNode::creator() {
    return new BdControllerShapeNode();
}

MHWRender::MPxDrawOverride* BdControllerShapeNode::createDrawOverride(
    const MObject& node
) {
    return new ControllerShapeDrawOverride(node);
}

void BdControllerShapeNode::postConstructor() {
    MPxLocatorNode::postConstructor();
    for (const MObject& attribute : {
             localPositionX,
             localPositionY,
             localPositionZ,
             localScaleX,
             localScaleY,
             localScaleZ,
         }) {
        const MStatus status = MPlug(thisMObject(), attribute).setChannelBox(false);
        if (!status) {
            status.perror("Failed to hide bdControllerShape locator attribute");
        }
    }
}

MStatus BdControllerShapeNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    shape = enumAttributeFn.create("shape", "sh", 0, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, short>{"Square", 0},
             std::pair<const char*, short>{"Cube", 1},
             std::pair<const char*, short>{"Circle", 2},
             std::pair<const char*, short>{"CircleArrow", 3},
         }) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    enumAttributeFn.setKeyable(true);
    status = addAttribute(shape);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn, shapeRootSize, "shapeRootSize", "srs", 1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeRootSize);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        shapeTranslate,
        shapeTranslateX,
        shapeTranslateY,
        shapeTranslateZ,
        "shapeTranslate",
        "st",
        "shapeTranslateX",
        "stx",
        "shapeTranslateY",
        "sty",
        "shapeTranslateZ",
        "stz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeTranslate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        shapeRotate,
        shapeRotateX,
        shapeRotateY,
        shapeRotateZ,
        "shapeRotate",
        "sr",
        "shapeRotateX",
        "srx",
        "shapeRotateY",
        "sry",
        "shapeRotateZ",
        "srz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeRotate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        shapeScale,
        shapeScaleX,
        shapeScaleY,
        shapeScaleZ,
        "shapeScale",
        "ssc",
        "shapeScaleX",
        "sscx",
        "shapeScaleY",
        "sscy",
        "shapeScaleZ",
        "sscz",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeScale);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn, shapeSize, "shapeSize", "ss", 1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeSize);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        showShapeOffsetLine,
        "showShapeOffsetLine",
        "ssol",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(showShapeOffsetLine);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        shapeOffsetLineTemplate,
        "shapeOffsetLineTemplate",
        "solt",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    return addAttribute(shapeOffsetLineTemplate);
}

bool BdControllerShapeNode::isBounded() const {
    return true;
}

MBoundingBox BdControllerShapeNode::boundingBox() const {
    return nodeBounds(thisMObject());
}

bool BdControllerShapeNode::excludeAsLocator() const {
    return false;
}
