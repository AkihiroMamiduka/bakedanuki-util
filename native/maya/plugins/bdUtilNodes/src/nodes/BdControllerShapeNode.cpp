#include "bdUtilNodes/nodes/BdControllerShapeNode.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <mutex>
#include <utility>
#include <vector>

#include <maya/M3dView.h>
#include <maya/MAngle.h>
#include <maya/MColor.h>
#include <maya/MDagPath.h>
#include <maya/MDistance.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MFrameContext.h>
#include <maya/MHWGeometryUtilities.h>
#include <maya/MMessage.h>
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
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdControllerShapeNode::typeName("bdControllerShape");
const MTypeId BdControllerShapeNode::typeId(0x0014271F);
const MString BdControllerShapeNode::drawClassification(
    "drawdb/geometry/bdControllerShape"
);
const MString BdControllerShapeNode::drawRegistrantId(
    "bdControllerShapeDrawOverride"
);

MObject BdControllerShapeNode::shape;
MObject BdControllerShapeNode::shape1stAxis;
MObject BdControllerShapeNode::shape2ndAxis;
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
MObject BdControllerShapeNode::shapeAxisOffsetLength;
MObject BdControllerShapeNode::shapeAxisOffset;
MObject BdControllerShapeNode::shapeAxisOffsetDirection;
MObject BdControllerShapeNode::shapeAxisTranslate;
MObject BdControllerShapeNode::shapeAxisTranslateX;
MObject BdControllerShapeNode::shapeAxisTranslateY;
MObject BdControllerShapeNode::shapeAxisTranslateZ;
MObject BdControllerShapeNode::shapeAxisRotate;
MObject BdControllerShapeNode::shapeAxisRotateX;
MObject BdControllerShapeNode::shapeAxisRotateY;
MObject BdControllerShapeNode::shapeAxisRotateZ;
MObject BdControllerShapeNode::shapeAxisScale;
MObject BdControllerShapeNode::shapeAxisScaleX;
MObject BdControllerShapeNode::shapeAxisScaleY;
MObject BdControllerShapeNode::shapeAxisScaleZ;
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
    short firstAxis = 4;
    short secondAxis = 2;
    double rootSize = 1.0;
    MVector translate = MVector(0.0, 0.0, 0.0);
    MVector rotateAngles = MVector(0.0, 0.0, 0.0);
    MVector scale = MVector(1.0, 1.0, 1.0);
    double axisOffsetLength = 1.0;
    bool axisOffset = false;
    short axisOffsetDirection = 0;
    MVector axisTranslate = MVector(0.0, 0.0, 0.0);
    MVector axisRotateAngles = MVector(0.0, 0.0, 0.0);
    MVector axisScale = MVector(1.0, 1.0, 1.0);
    double size = 1.0;
    bool showOffsetLine = false;
    bool offsetLineTemplate = false;
};

bool sameVector(const MVector& left, const MVector& right) {
    return left.x == right.x && left.y == right.y && left.z == right.z;
}

bool sameSettings(const ShapeSettings& left, const ShapeSettings& right) {
    return left.shape == right.shape &&
        left.firstAxis == right.firstAxis &&
        left.secondAxis == right.secondAxis &&
        left.rootSize == right.rootSize &&
        sameVector(left.translate, right.translate) &&
        sameVector(left.rotateAngles, right.rotateAngles) &&
        sameVector(left.scale, right.scale) &&
        left.axisOffsetLength == right.axisOffsetLength &&
        left.axisOffset == right.axisOffset &&
        left.axisOffsetDirection == right.axisOffsetDirection &&
        sameVector(left.axisTranslate, right.axisTranslate) &&
        sameVector(left.axisRotateAngles, right.axisRotateAngles) &&
        sameVector(left.axisScale, right.axisScale) &&
        left.size == right.size &&
        left.showOffsetLine == right.showOffsetLine &&
        left.offsetLineTemplate == right.offsetLineTemplate;
}

MVector axisVector(short axis) {
    switch (axis) {
        case 0: return MVector(1.0, 0.0, 0.0);
        case 1: return MVector(-1.0, 0.0, 0.0);
        case 2: return MVector(0.0, 1.0, 0.0);
        case 3: return MVector(0.0, -1.0, 0.0);
        case 4: return MVector(0.0, 0.0, 1.0);
        case 5: return MVector(0.0, 0.0, -1.0);
        default: return MVector(0.0, 0.0, 1.0);
    }
}

MVector axisOffsetVector(short direction) {
    switch (direction) {
        case 0: return MVector(0.0, 0.0, 0.5);
        case 1: return MVector(0.0, 0.0, -0.5);
        case 2: return MVector(0.0, 0.5, 0.0);
        case 3: return MVector(0.0, -0.5, 0.0);
        case 4: return MVector(0.5, 0.0, 0.0);
        case 5: return MVector(-0.5, 0.0, 0.0);
        default: return MVector(0.0, 0.0, 0.5);
    }
}

MVector axisLengthScaledVector(
    const MVector& vector, short direction, double length
) {
    switch (direction) {
        case 2:
        case 3: return MVector(vector.x, vector.y * length, vector.z);
        case 4:
        case 5: return MVector(vector.x * length, vector.y, vector.z);
        default: return MVector(vector.x, vector.y, vector.z * length);
    }
}

struct ShapeTransform {
    const ShapeSettings& settings;
    MQuaternion rotate;
    MQuaternion axisRotate;
    MVector axisX;
    MVector axisY;
    MVector axisZ;
    MVector axisOffset;

    explicit ShapeTransform(const ShapeSettings& source)
        : settings(source),
          rotate(MEulerRotation(
              source.rotateAngles.x,
              source.rotateAngles.y,
              source.rotateAngles.z,
              MEulerRotation::kXYZ
          ).asQuaternion()),
          axisRotate(MEulerRotation(
              source.axisRotateAngles.x,
              source.axisRotateAngles.y,
              source.axisRotateAngles.z,
              MEulerRotation::kXYZ
          ).asQuaternion()),
          axisZ(axisVector(source.firstAxis)),
          axisY(axisVector(source.secondAxis)),
          axisOffset(
              source.axisOffset
                  ? axisOffsetVector(source.axisOffsetDirection)
                  : MVector(0.0, 0.0, 0.0)
          ) {
        if ((axisY ^ axisZ).length() == 0.0) {
            axisY = std::abs(axisZ.y) == 1.0
                ? MVector(0.0, 0.0, 1.0)
                : MVector(0.0, 1.0, 0.0);
        }
        axisX = axisY ^ axisZ;
    }
};

bool readSettings(const MObject& node, ShapeSettings& settings) {
    MStatus status;
    settings.shape = MPlug(node, BdControllerShapeNode::shape).asShort(&status);
    if (!status) {
        return false;
    }
    settings.firstAxis =
        MPlug(node, BdControllerShapeNode::shape1stAxis).asShort(&status);
    if (!status) {
        return false;
    }
    settings.secondAxis =
        MPlug(node, BdControllerShapeNode::shape2ndAxis).asShort(&status);
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
    settings.rotateAngles.x = rotate.child(0).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    settings.rotateAngles.y = rotate.child(1).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    settings.rotateAngles.z = rotate.child(2).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }

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

    settings.axisOffsetLength = std::max(
        0.0,
        MPlug(node, BdControllerShapeNode::shapeAxisOffsetLength)
            .asMDistance(&status)
            .asCentimeters()
    );
    if (!status) {
        return false;
    }
    settings.axisOffset =
        MPlug(node, BdControllerShapeNode::shapeAxisOffset).asBool(&status);
    if (!status) {
        return false;
    }
    settings.axisOffsetDirection = MPlug(
        node, BdControllerShapeNode::shapeAxisOffsetDirection
    ).asShort(&status);
    if (!status) {
        return false;
    }

    const MPlug axisTranslate(node, BdControllerShapeNode::shapeAxisTranslate);
    settings.axisTranslate.x =
        axisTranslate.child(0).asMDistance(&status).asCentimeters();
    if (!status) {
        return false;
    }
    settings.axisTranslate.y =
        axisTranslate.child(1).asMDistance(&status).asCentimeters();
    if (!status) {
        return false;
    }
    settings.axisTranslate.z =
        axisTranslate.child(2).asMDistance(&status).asCentimeters();
    if (!status) {
        return false;
    }

    const MPlug axisRotate(node, BdControllerShapeNode::shapeAxisRotate);
    settings.axisRotateAngles.x =
        axisRotate.child(0).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    settings.axisRotateAngles.y =
        axisRotate.child(1).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }
    settings.axisRotateAngles.z =
        axisRotate.child(2).asMAngle(&status).asRadians();
    if (!status) {
        return false;
    }

    const MPlug axisScale(node, BdControllerShapeNode::shapeAxisScale);
    settings.axisScale.x = axisScale.child(0).asDouble(&status);
    if (!status) {
        return false;
    }
    settings.axisScale.y = axisScale.child(1).asDouble(&status);
    if (!status) {
        return false;
    }
    settings.axisScale.z = axisScale.child(2).asDouble(&status);
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

MPoint transformPoint(
    const MPoint& point,
    const ShapeTransform& transform,
    bool includeAxisOffset = true
) {
    const ShapeSettings& settings = transform.settings;
    const MVector axisScaled(
        point.x * settings.size * settings.axisScale.x,
        point.y * settings.size * settings.axisScale.y,
        point.z * settings.size * settings.axisScale.z
    );
    const MVector axisLocal = axisLengthScaledVector(
        axisScaled.rotateBy(transform.axisRotate) + settings.axisTranslate +
            (includeAxisOffset ? transform.axisOffset : MVector(0.0, 0.0, 0.0)),
        settings.axisOffsetDirection,
        settings.axisOffsetLength
    );
    const MVector oriented =
        transform.axisX * axisLocal.x +
        transform.axisY * axisLocal.y +
        transform.axisZ * axisLocal.z;
    const MVector scaled(
        oriented.x * settings.scale.x,
        oriented.y * settings.scale.y,
        oriented.z * settings.scale.z
    );
    const MVector rotated = scaled.rotateBy(transform.rotate);
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
    const ShapeTransform& transform,
    Strokes& strokes
) {
    Stroke stroke;
    for (const MPoint& point : points) {
        stroke.append(transformPoint(point, transform));
    }
    strokes.push_back(std::move(stroke));
}

void appendSquare(const ShapeTransform& transform, Strokes& strokes) {
    appendStroke(
        std::array<MPoint, 5>{
            MPoint(-0.5, -0.5, 0.0),
            MPoint(0.5, -0.5, 0.0),
            MPoint(0.5, 0.5, 0.0),
            MPoint(-0.5, 0.5, 0.0),
            MPoint(-0.5, -0.5, 0.0),
        },
        transform,
        strokes
    );
}

void appendCube(const ShapeTransform& transform, Strokes& strokes) {
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
            transform,
            strokes
        );
    }
}

void appendCircle(
    double radius,
    const ShapeTransform& transform,
    Strokes& strokes
) {
    Stroke stroke;
    for (unsigned int index = 0; index <= kCircleSegments; ++index) {
        const double angle = 2.0 * kPi * index / kCircleSegments;
        stroke.append(transformPoint(
            MPoint(radius * std::cos(angle), radius * std::sin(angle), 0.0),
            transform
        ));
    }
    strokes.push_back(std::move(stroke));
}

void appendCircleArrow(const ShapeTransform& transform, Strokes& strokes) {
    appendCircle(0.32, transform, strokes);
    appendStroke(
        std::array<MPoint, 4>{
            MPoint(-0.1, 0.38, 0.0),
            MPoint(0.0, 0.5, 0.0),
            MPoint(0.1, 0.38, 0.0),
            MPoint(-0.1, 0.38, 0.0),
        },
        transform,
        strokes
    );
}

Strokes makeStrokes(const ShapeTransform& transform) {
    Strokes strokes;
    switch (transform.settings.shape) {
        case 0:
            appendSquare(transform, strokes);
            break;
        case 1:
            appendCube(transform, strokes);
            break;
        case 2:
            appendCircle(0.5, transform, strokes);
            break;
        case 3:
            appendCircleArrow(transform, strokes);
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

bool isShapeAttribute(const MObject& attribute) {
    for (const MObject& shapeAttribute : {
             BdControllerShapeNode::shape,
             BdControllerShapeNode::shape1stAxis,
             BdControllerShapeNode::shape2ndAxis,
             BdControllerShapeNode::shapeRootSize,
             BdControllerShapeNode::shapeTranslate,
             BdControllerShapeNode::shapeTranslateX,
             BdControllerShapeNode::shapeTranslateY,
             BdControllerShapeNode::shapeTranslateZ,
             BdControllerShapeNode::shapeRotate,
             BdControllerShapeNode::shapeRotateX,
             BdControllerShapeNode::shapeRotateY,
             BdControllerShapeNode::shapeRotateZ,
             BdControllerShapeNode::shapeScale,
             BdControllerShapeNode::shapeScaleX,
             BdControllerShapeNode::shapeScaleY,
             BdControllerShapeNode::shapeScaleZ,
             BdControllerShapeNode::shapeAxisOffsetLength,
             BdControllerShapeNode::shapeAxisOffset,
             BdControllerShapeNode::shapeAxisOffsetDirection,
             BdControllerShapeNode::shapeAxisTranslate,
             BdControllerShapeNode::shapeAxisTranslateX,
             BdControllerShapeNode::shapeAxisTranslateY,
             BdControllerShapeNode::shapeAxisTranslateZ,
             BdControllerShapeNode::shapeAxisRotate,
             BdControllerShapeNode::shapeAxisRotateX,
             BdControllerShapeNode::shapeAxisRotateY,
             BdControllerShapeNode::shapeAxisRotateZ,
             BdControllerShapeNode::shapeAxisScale,
             BdControllerShapeNode::shapeAxisScaleX,
             BdControllerShapeNode::shapeAxisScaleY,
             BdControllerShapeNode::shapeAxisScaleZ,
             BdControllerShapeNode::shapeSize,
             BdControllerShapeNode::showShapeOffsetLine,
             BdControllerShapeNode::shapeOffsetLineTemplate,
         }) {
        if (attribute == shapeAttribute) {
            return true;
        }
    }
    return false;
}

bool hasIncomingConnection(const MPlug& plug) {
    if (plug.isDestination()) {
        return true;
    }
    for (unsigned int child = 0; child < plug.numChildren(); ++child) {
        if (hasIncomingConnection(plug.child(child))) {
            return true;
        }
    }
    return false;
}

bool hasConnectedShapeInput(const MObject& node) {
    for (const MObject& attribute : {
             BdControllerShapeNode::shape,
             BdControllerShapeNode::shape1stAxis,
             BdControllerShapeNode::shape2ndAxis,
             BdControllerShapeNode::shapeRootSize,
             BdControllerShapeNode::shapeTranslate,
             BdControllerShapeNode::shapeRotate,
             BdControllerShapeNode::shapeScale,
             BdControllerShapeNode::shapeAxisOffsetLength,
             BdControllerShapeNode::shapeAxisOffset,
             BdControllerShapeNode::shapeAxisOffsetDirection,
             BdControllerShapeNode::shapeAxisTranslate,
             BdControllerShapeNode::shapeAxisRotate,
             BdControllerShapeNode::shapeAxisScale,
             BdControllerShapeNode::shapeSize,
             BdControllerShapeNode::showShapeOffsetLine,
             BdControllerShapeNode::shapeOffsetLineTemplate,
         }) {
        if (hasIncomingConnection(MPlug(node, attribute))) {
            return true;
        }
    }
    return false;
}

std::shared_ptr<const BdControllerShapeNode::Geometry> nodeGeometry(
    const MObject& object
) {
    MStatus status;
    MFnDependencyNode dependencyNode(object, &status);
    if (!status) {
        return nullptr;
    }
    MPxNode* userNode = dependencyNode.userNode(&status);
    if (!status || !userNode) {
        return nullptr;
    }
    return static_cast<BdControllerShapeNode*>(userNode)->geometry();
}

MBoundingBox nodeBounds(const MObject& node) {
    const auto geometry = nodeGeometry(node);
    return geometry
        ? geometry->bounds
        : MBoundingBox(MPoint::origin, MPoint::origin);
}

struct ShapeDrawData final : public MUserData {
    std::shared_ptr<const BdControllerShapeNode::Geometry> geometry;
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
        data->geometry = nodeGeometry(objectPath.node());
        data->color = MHWRender::MGeometryUtilities::wireframeColor(objectPath);
        if (data->geometry && data->geometry->offsetLine.length() == 2) {
            data->offsetLineColor = data->color;
            if (data->geometry->offsetLineTemplate) {
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
        if (!data || !data->geometry) {
            return;
        }
        drawManager.beginDrawable();
        drawManager.setColor(data->color);
        for (const Stroke& stroke : data->geometry->strokes) {
            drawManager.lineStrip(stroke, false);
        }
        drawManager.endDrawable();
        if (data->geometry->offsetLine.length() == 2) {
            drawManager.beginDrawable(
                data->geometry->offsetLineTemplate
                    ? MHWRender::MUIDrawManager::kNonSelectable
                    : MHWRender::MUIDrawManager::kSelectable
            );
            drawManager.setColor(data->offsetLineColor);
            drawManager.lineStrip(data->geometry->offsetLine, false);
            drawManager.endDrawable();
        }
    }
};

}  // namespace

struct BdControllerShapeNode::GeometryCache {
    std::mutex mutex;
    ShapeSettings settings;
    std::shared_ptr<const Geometry> value;
    std::uint64_t revision = 0;
    bool hasConnectedInput = false;
};

BdControllerShapeNode::BdControllerShapeNode()
    : geometryCache_(std::make_unique<GeometryCache>()) {}

BdControllerShapeNode::~BdControllerShapeNode() {
    if (attributeChangedCallback_ != 0) {
        MMessage::removeCallback(attributeChangedCallback_);
    }
}

void BdControllerShapeNode::onAttributeChanged(
    MNodeMessage::AttributeMessage change,
    MPlug& plug,
    MPlug&,
    void* clientData
) {
    if (!(change & (MNodeMessage::kAttributeSet |
                     MNodeMessage::kConnectionMade |
                     MNodeMessage::kConnectionBroken)) ||
        !isShapeAttribute(plug.attribute())) {
        return;
    }
    auto* node = static_cast<BdControllerShapeNode*>(clientData);
    node->geometryRevision_.fetch_add(1, std::memory_order_release);
}

std::shared_ptr<const BdControllerShapeNode::Geometry>
BdControllerShapeNode::geometry() const {
    GeometryCache& cache = *geometryCache_;
    const std::lock_guard<std::mutex> lock(cache.mutex);
    const std::uint64_t revision = geometryRevision_.load(
        std::memory_order_acquire
    );
    if (cache.value && cache.revision == revision &&
        !cache.hasConnectedInput && attributeChangedCallback_ != 0) {
        return cache.value;
    }

    ShapeSettings settings;
    if (!readSettings(thisMObject(), settings)) {
        return cache.value;
    }
    const bool connected = hasConnectedShapeInput(thisMObject());
    if (cache.value && sameSettings(settings, cache.settings)) {
        cache.revision = revision;
        cache.hasConnectedInput = connected;
        return cache.value;
    }

    const ShapeTransform transform(settings);
    auto result = std::make_shared<Geometry>();
    result->strokes = makeStrokes(transform);
    result->bounds = boundsForStrokes(result->strokes);
    result->offsetLineTemplate = settings.offsetLineTemplate;
    if (settings.showOffsetLine) {
        const MPoint endpoint = transformPoint(MPoint::origin, transform, false);
        if (hasOffsetLine(endpoint)) {
            result->offsetLine.append(MPoint::origin);
            result->offsetLine.append(endpoint);
            result->bounds.expand(MPoint::origin);
            result->bounds.expand(endpoint);
        }
    }
    cache.settings = settings;
    cache.value = result;
    cache.revision = revision;
    cache.hasConnectedInput = connected;
    return result;
}

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
    MObject node = thisMObject();
    MStatus callbackStatus;
    attributeChangedCallback_ = MNodeMessage::addAttributeChangedCallback(
        node,
        onAttributeChanged,
        this,
        &callbackStatus
    );
    if (!callbackStatus) {
        callbackStatus.perror("Failed to watch bdControllerShape attributes");
    }
    for (const MObject& attribute : {
             localPositionX,
             localPositionY,
             localPositionZ,
             localScaleX,
             localScaleY,
             localScaleZ,
         }) {
        const MStatus status = MPlug(node, attribute).setChannelBox(false);
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

    for (const auto& axisAttribute : {
             std::pair<MObject*, std::pair<const char*, const char*>>{
                 &shape1stAxis, {"shape1stAxis", "s1a"}},
             std::pair<MObject*, std::pair<const char*, const char*>>{
                 &shape2ndAxis, {"shape2ndAxis", "s2a"}},
         }) {
        const short defaultAxis = axisAttribute.first == &shape1stAxis ? 4 : 2;
        *axisAttribute.first = enumAttributeFn.create(
            axisAttribute.second.first,
            axisAttribute.second.second,
            defaultAxis,
            &status
        );
        if (!status) {
            return status;
        }
        for (const auto& field : {
                 std::pair<const char*, short>{"+X", 0},
                 std::pair<const char*, short>{"-X", 1},
                 std::pair<const char*, short>{"+Y", 2},
                 std::pair<const char*, short>{"-Y", 3},
                 std::pair<const char*, short>{"+Z", 4},
                 std::pair<const char*, short>{"-Z", 5},
             }) {
            status = enumAttributeFn.addField(field.first, field.second);
            if (!status) {
                return status;
            }
        }
        enumAttributeFn.setKeyable(true);
        status = addAttribute(*axisAttribute.first);
        if (!status) {
            return status;
        }
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

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        shapeAxisOffsetLength,
        "shapeAxisOffsetLength",
        "saol",
        1.0
    );
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeAxisOffsetLength);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        shapeAxisOffset,
        "shapeAxisOffset",
        "sao",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeAxisOffset);
    if (!status) {
        return status;
    }

    shapeAxisOffsetDirection = enumAttributeFn.create(
        "shapeAxisOffsetDirection", "saod", 0, &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, short>{"+1stAxis", 0},
             std::pair<const char*, short>{"-1stAxis", 1},
             std::pair<const char*, short>{"+2ndAxis", 2},
             std::pair<const char*, short>{"-2ndAxis", 3},
             std::pair<const char*, short>{"+3rdAxis", 4},
             std::pair<const char*, short>{"-3rdAxis", 5},
         }) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    enumAttributeFn.setKeyable(true);
    status = addAttribute(shapeAxisOffsetDirection);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        shapeAxisTranslate,
        shapeAxisTranslateX,
        shapeAxisTranslateY,
        shapeAxisTranslateZ,
        "shapeAxisTranslate",
        "sat",
        "shapeAxisTranslateX",
        "satx",
        "shapeAxisTranslateY",
        "saty",
        "shapeAxisTranslateZ",
        "satz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeAxisTranslate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        shapeAxisRotate,
        shapeAxisRotateX,
        shapeAxisRotateY,
        shapeAxisRotateZ,
        "shapeAxisRotate",
        "sar",
        "shapeAxisRotateX",
        "sarx",
        "shapeAxisRotateY",
        "sary",
        "shapeAxisRotateZ",
        "sarz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeAxisRotate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        shapeAxisScale,
        shapeAxisScaleX,
        shapeAxisScaleY,
        shapeAxisScaleZ,
        "shapeAxisScale",
        "sasc",
        "shapeAxisScaleX",
        "sascx",
        "shapeAxisScaleY",
        "sascy",
        "shapeAxisScaleZ",
        "sascz",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(shapeAxisScale);
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
