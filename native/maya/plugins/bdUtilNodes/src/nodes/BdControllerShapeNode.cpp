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
#include <maya/MFnAttribute.h>
#include <maya/MFnData.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnMatrixData.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnNumericData.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MFrameContext.h>
#include <maya/MHWGeometryUtilities.h>
#include <maya/MMessage.h>
#include <maya/MMatrix.h>
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
MObject BdControllerShapeNode::shapeAnimationTransformMatrix;
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
MObject BdControllerShapeNode::shapeLineWidth;
MObject BdControllerShapeNode::shapeTransparency;
MObject BdControllerShapeNode::shapeDrawOnTop;
MObject BdControllerShapeNode::boundsMode;
MObject BdControllerShapeNode::showBoundsPreview;
MObject BdControllerShapeNode::customBounds1stAxis;
MObject BdControllerShapeNode::customBounds2ndAxis;
MObject BdControllerShapeNode::customBoundsRootSize;
MObject BdControllerShapeNode::customBoundsTranslate;
MObject BdControllerShapeNode::customBoundsTranslateX;
MObject BdControllerShapeNode::customBoundsTranslateY;
MObject BdControllerShapeNode::customBoundsTranslateZ;
MObject BdControllerShapeNode::customBoundsRotate;
MObject BdControllerShapeNode::customBoundsRotateX;
MObject BdControllerShapeNode::customBoundsRotateY;
MObject BdControllerShapeNode::customBoundsRotateZ;
MObject BdControllerShapeNode::customBoundsScale;
MObject BdControllerShapeNode::customBoundsScaleX;
MObject BdControllerShapeNode::customBoundsScaleY;
MObject BdControllerShapeNode::customBoundsScaleZ;
MObject BdControllerShapeNode::customBoundsAxisOffsetLength;
MObject BdControllerShapeNode::customBoundsAxisOffset;
MObject BdControllerShapeNode::customBoundsAxisOffsetDirection;
MObject BdControllerShapeNode::customBoundsAxisTranslate;
MObject BdControllerShapeNode::customBoundsAxisTranslateX;
MObject BdControllerShapeNode::customBoundsAxisTranslateY;
MObject BdControllerShapeNode::customBoundsAxisTranslateZ;
MObject BdControllerShapeNode::customBoundsAxisRotate;
MObject BdControllerShapeNode::customBoundsAxisRotateX;
MObject BdControllerShapeNode::customBoundsAxisRotateY;
MObject BdControllerShapeNode::customBoundsAxisRotateZ;
MObject BdControllerShapeNode::customBoundsAxisScale;
MObject BdControllerShapeNode::customBoundsAxisScaleX;
MObject BdControllerShapeNode::customBoundsAxisScaleY;
MObject BdControllerShapeNode::customBoundsAxisScaleZ;
MObject BdControllerShapeNode::customBoundsSize;

namespace {

MObject channelBoxSeparator1;
MObject channelBoxSeparator2;
MObject channelBoxSeparator3;
MObject channelBoxSeparator4;
MObject channelBoxSeparator5;

constexpr double kPi = 3.14159265358979323846;
constexpr unsigned int kCircleSegments = 64;

using Stroke = MPointArray;
using Strokes = std::vector<Stroke>;

struct ShapeSettings {
    short shape = 0;
    short firstAxis = 0;
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

struct ShapeAttributes {
    MObject shape;
    MObject firstAxis;
    MObject secondAxis;
    MObject rootSize;
    MObject translate;
    MObject rotate;
    MObject scale;
    MObject axisOffsetLength;
    MObject axisOffset;
    MObject axisOffsetDirection;
    MObject axisTranslate;
    MObject axisRotate;
    MObject axisScale;
    MObject size;
    MObject showOffsetLine;
    MObject offsetLineTemplate;
};

ShapeAttributes shapeAttributes() {
    return {
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
    };
}

ShapeAttributes customBoundsAttributes() {
    return {
        MObject(),
        BdControllerShapeNode::customBounds1stAxis,
        BdControllerShapeNode::customBounds2ndAxis,
        BdControllerShapeNode::customBoundsRootSize,
        BdControllerShapeNode::customBoundsTranslate,
        BdControllerShapeNode::customBoundsRotate,
        BdControllerShapeNode::customBoundsScale,
        BdControllerShapeNode::customBoundsAxisOffsetLength,
        BdControllerShapeNode::customBoundsAxisOffset,
        BdControllerShapeNode::customBoundsAxisOffsetDirection,
        BdControllerShapeNode::customBoundsAxisTranslate,
        BdControllerShapeNode::customBoundsAxisRotate,
        BdControllerShapeNode::customBoundsAxisScale,
        BdControllerShapeNode::customBoundsSize,
        MObject(),
        MObject(),
    };
}

bool sameVector(const MVector& left, const MVector& right) {
    return left.x == right.x && left.y == right.y && left.z == right.z;
}

bool sameMatrix(const MMatrix& left, const MMatrix& right) {
    for (unsigned int row = 0; row < 4; ++row) {
        for (unsigned int column = 0; column < 4; ++column) {
            if (left[row][column] != right[row][column]) {
                return false;
            }
        }
    }
    return true;
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
        default: return MVector(1.0, 0.0, 0.0);
    }
}

MVector axisOffsetVector(short direction) {
    switch (direction) {
        case 0: return MVector(0.5, 0.0, 0.0);
        case 1: return MVector(-0.5, 0.0, 0.0);
        case 2: return MVector(0.0, 0.5, 0.0);
        case 3: return MVector(0.0, -0.5, 0.0);
        case 4: return MVector(0.0, 0.0, 0.5);
        case 5: return MVector(0.0, 0.0, -0.5);
        default: return MVector(0.5, 0.0, 0.0);
    }
}

MVector axisLengthScaledVector(
    const MVector& vector, short direction, double length
) {
    switch (direction) {
        case 2:
        case 3: return MVector(vector.x, vector.y * length, vector.z);
        case 4:
        case 5: return MVector(vector.x, vector.y, vector.z * length);
        default: return MVector(vector.x * length, vector.y, vector.z);
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
          axisX(axisVector(source.firstAxis)),
          axisY(axisVector(source.secondAxis)),
          axisOffset(
              source.axisOffset
                  ? axisOffsetVector(source.axisOffsetDirection)
                  : MVector(0.0, 0.0, 0.0)
          ) {
        if ((axisX ^ axisY).length() == 0.0) {
            axisY = std::abs(axisX.y) == 1.0
                ? MVector(0.0, 0.0, 1.0)
                : MVector(0.0, 1.0, 0.0);
        }
        axisZ = axisX ^ axisY;
    }
};

bool readSettings(
    const MObject& node,
    const ShapeAttributes& attributes,
    ShapeSettings& settings
) {
    MStatus status;
    if (attributes.shape.isNull()) {
        settings.shape = 1;
    } else {
        settings.shape = MPlug(node, attributes.shape).asShort(&status);
        if (!status) {
            return false;
        }
    }
    settings.firstAxis = MPlug(node, attributes.firstAxis).asShort(&status);
    if (!status) {
        return false;
    }
    settings.secondAxis = MPlug(node, attributes.secondAxis).asShort(&status);
    if (!status) {
        return false;
    }
    settings.rootSize = MPlug(node, attributes.rootSize).asDouble(&status);
    if (!status) {
        return false;
    }

    const MPlug translate(node, attributes.translate);
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

    const MPlug rotate(node, attributes.rotate);
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

    const MPlug scale(node, attributes.scale);
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
        MPlug(node, attributes.axisOffsetLength)
            .asMDistance(&status)
            .asCentimeters()
    );
    if (!status) {
        return false;
    }
    settings.axisOffset = MPlug(node, attributes.axisOffset).asBool(&status);
    if (!status) {
        return false;
    }
    settings.axisOffsetDirection =
        MPlug(node, attributes.axisOffsetDirection).asShort(&status);
    if (!status) {
        return false;
    }

    const MPlug axisTranslate(node, attributes.axisTranslate);
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

    const MPlug axisRotate(node, attributes.axisRotate);
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

    const MPlug axisScale(node, attributes.axisScale);
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

    settings.size = MPlug(node, attributes.size).asDouble(&status);
    if (!status) {
        return false;
    }
    if (attributes.showOffsetLine.isNull()) {
        settings.showOffsetLine = false;
        settings.offsetLineTemplate = false;
    } else {
        settings.showOffsetLine =
            MPlug(node, attributes.showOffsetLine).asBool(&status);
        if (!status) {
            return false;
        }
        settings.offsetLineTemplate =
            MPlug(node, attributes.offsetLineTemplate).asBool(&status);
    }
    return status == MS::kSuccess;
}

bool readAnimationMatrix(const MObject& node, MMatrix& matrix) {
    MStatus status;
    const MObject data = MPlug(
        node, BdControllerShapeNode::shapeAnimationTransformMatrix
    ).asMObject(&status);
    if (!status) {
        return false;
    }
    MFnMatrixData matrixData(data, &status);
    if (!status) {
        return false;
    }
    matrix = matrixData.matrix(&status);
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
        settings.axisOffset ? settings.axisOffsetLength : 1.0
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
            MPoint(0.0, -0.5, 0.5),
            MPoint(0.0, -0.5, -0.5),
            MPoint(0.0, 0.5, -0.5),
            MPoint(0.0, 0.5, 0.5),
            MPoint(0.0, -0.5, 0.5),
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
            MPoint(0.0, radius * std::sin(angle), -radius * std::cos(angle)),
            transform
        ));
    }
    strokes.push_back(std::move(stroke));
}

void appendCircleArrow(const ShapeTransform& transform, Strokes& strokes) {
    appendCircle(0.32, transform, strokes);
    appendStroke(
        std::array<MPoint, 4>{
            MPoint(0.0, 0.38, 0.1),
            MPoint(0.0, 0.5, 0.0),
            MPoint(0.0, 0.38, -0.1),
            MPoint(0.0, 0.38, 0.1),
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

std::shared_ptr<const BdControllerShapeNode::Geometry> makeBaseGeometry(
    const ShapeSettings& settings
) {
    const ShapeTransform transform(settings);
    auto result = std::make_shared<BdControllerShapeNode::Geometry>();
    result->strokes = makeStrokes(transform);
    result->bounds = boundsForStrokes(result->strokes);
    result->offsetLineTemplate = settings.offsetLineTemplate;
    result->offsetLineEndpoint = transformPoint(MPoint::origin, transform, false);
    if (settings.showOffsetLine && hasOffsetLine(result->offsetLineEndpoint)) {
        result->offsetLine.append(MPoint::origin);
        result->offsetLine.append(result->offsetLineEndpoint);
        result->bounds.expand(MPoint::origin);
        result->bounds.expand(result->offsetLineEndpoint);
    }
    return result;
}

std::shared_ptr<const BdControllerShapeNode::Geometry> transformGeometry(
    const BdControllerShapeNode::Geometry& base,
    const MMatrix& matrix,
    bool showOffsetLine
) {
    auto result = std::make_shared<BdControllerShapeNode::Geometry>();
    result->offsetLineTemplate = base.offsetLineTemplate;
    for (const Stroke& baseStroke : base.strokes) {
        Stroke stroke;
        for (unsigned int index = 0; index < baseStroke.length(); ++index) {
            stroke.append(baseStroke[index] * matrix);
        }
        result->strokes.push_back(std::move(stroke));
    }
    result->bounds = boundsForStrokes(result->strokes);
    result->offsetLineEndpoint = base.offsetLineEndpoint * matrix;
    if (showOffsetLine && hasOffsetLine(result->offsetLineEndpoint)) {
        result->offsetLine.append(MPoint::origin);
        result->offsetLine.append(result->offsetLineEndpoint);
        result->bounds.expand(MPoint::origin);
        result->bounds.expand(result->offsetLineEndpoint);
    }
    return result;
}

MBoundingBox centeredShapeBounds(const ShapeSettings& settings) {
    ShapeSettings centered = settings;
    centered.translate = MVector(0.0, 0.0, 0.0);
    centered.axisTranslate = MVector(0.0, 0.0, 0.0);
    centered.showOffsetLine = false;
    const MBoundingBox bounds = makeBaseGeometry(centered)->bounds;
    const MPoint minimum = bounds.min();
    const MPoint maximum = bounds.max();
    const MPoint halfSize(
        (maximum.x - minimum.x) * 0.5,
        (maximum.y - minimum.y) * 0.5,
        (maximum.z - minimum.z) * 0.5
    );
    return MBoundingBox(
        MPoint(-halfSize.x, -halfSize.y, -halfSize.z),
        halfSize
    );
}

std::array<MPoint, 8> boundsCorners(const MBoundingBox& bounds) {
    const MPoint minimum = bounds.min();
    const MPoint maximum = bounds.max();
    return {
        MPoint(minimum.x, minimum.y, minimum.z),
        MPoint(maximum.x, minimum.y, minimum.z),
        MPoint(maximum.x, maximum.y, minimum.z),
        MPoint(minimum.x, maximum.y, minimum.z),
        MPoint(minimum.x, minimum.y, maximum.z),
        MPoint(maximum.x, minimum.y, maximum.z),
        MPoint(maximum.x, maximum.y, maximum.z),
        MPoint(minimum.x, maximum.y, maximum.z),
    };
}

MBoundingBox transformBounds(
    const MBoundingBox& bounds, const MMatrix& matrix
) {
    MBoundingBox result;
    for (const MPoint& corner : boundsCorners(bounds)) {
        result.expand(corner * matrix);
    }
    return result;
}

Strokes boundsStrokes(const MBoundingBox& bounds) {
    const auto corners = boundsCorners(bounds);
    constexpr std::array<std::array<int, 2>, 12> edges = {{
        {{0, 1}}, {{1, 2}}, {{2, 3}}, {{3, 0}},
        {{4, 5}}, {{5, 6}}, {{6, 7}}, {{7, 4}},
        {{0, 4}}, {{1, 5}}, {{2, 6}}, {{3, 7}},
    }};
    Strokes strokes;
    for (const auto& edge : edges) {
        const MPoint& start = corners[edge[0]];
        const MPoint& end = corners[edge[1]];
        if (start == end) {
            continue;
        }
        bool duplicate = false;
        for (const Stroke& existing : strokes) {
            if ((existing[0] == start && existing[1] == end) ||
                (existing[0] == end && existing[1] == start)) {
                duplicate = true;
                break;
            }
        }
        if (duplicate) {
            continue;
        }
        Stroke stroke;
        stroke.append(start);
        stroke.append(end);
        strokes.push_back(std::move(stroke));
    }
    return strokes;
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

bool isBoundsAttribute(const MObject& attribute) {
    for (const MObject& boundsAttribute : {
             BdControllerShapeNode::boundsMode,
             BdControllerShapeNode::showBoundsPreview,
             BdControllerShapeNode::customBounds1stAxis,
             BdControllerShapeNode::customBounds2ndAxis,
             BdControllerShapeNode::customBoundsRootSize,
             BdControllerShapeNode::customBoundsTranslate,
             BdControllerShapeNode::customBoundsTranslateX,
             BdControllerShapeNode::customBoundsTranslateY,
             BdControllerShapeNode::customBoundsTranslateZ,
             BdControllerShapeNode::customBoundsRotate,
             BdControllerShapeNode::customBoundsRotateX,
             BdControllerShapeNode::customBoundsRotateY,
             BdControllerShapeNode::customBoundsRotateZ,
             BdControllerShapeNode::customBoundsScale,
             BdControllerShapeNode::customBoundsScaleX,
             BdControllerShapeNode::customBoundsScaleY,
             BdControllerShapeNode::customBoundsScaleZ,
             BdControllerShapeNode::customBoundsAxisOffsetLength,
             BdControllerShapeNode::customBoundsAxisOffset,
             BdControllerShapeNode::customBoundsAxisOffsetDirection,
             BdControllerShapeNode::customBoundsAxisTranslate,
             BdControllerShapeNode::customBoundsAxisTranslateX,
             BdControllerShapeNode::customBoundsAxisTranslateY,
             BdControllerShapeNode::customBoundsAxisTranslateZ,
             BdControllerShapeNode::customBoundsAxisRotate,
             BdControllerShapeNode::customBoundsAxisRotateX,
             BdControllerShapeNode::customBoundsAxisRotateY,
             BdControllerShapeNode::customBoundsAxisRotateZ,
             BdControllerShapeNode::customBoundsAxisScale,
             BdControllerShapeNode::customBoundsAxisScaleX,
             BdControllerShapeNode::customBoundsAxisScaleY,
             BdControllerShapeNode::customBoundsAxisScaleZ,
             BdControllerShapeNode::customBoundsSize,
         }) {
        if (attribute == boundsAttribute) {
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

bool hasConnectedSettingsInput(
    const MObject& node, const ShapeAttributes& attributes
) {
    for (const MObject& attribute : {
             attributes.shape,
             attributes.firstAxis,
             attributes.secondAxis,
             attributes.rootSize,
             attributes.translate,
             attributes.rotate,
             attributes.scale,
             attributes.axisOffsetLength,
             attributes.axisOffset,
             attributes.axisOffsetDirection,
             attributes.axisTranslate,
             attributes.axisRotate,
             attributes.axisScale,
             attributes.size,
             attributes.showOffsetLine,
             attributes.offsetLineTemplate,
         }) {
        if (!attribute.isNull() &&
            hasIncomingConnection(MPlug(node, attribute))) {
            return true;
        }
    }
    return false;
}

bool hasConnectedBoundsInput(const MObject& node) {
    return hasConnectedSettingsInput(node, customBoundsAttributes()) ||
        hasIncomingConnection(MPlug(node, BdControllerShapeNode::boundsMode)) ||
        hasIncomingConnection(MPlug(
            node, BdControllerShapeNode::showBoundsPreview
        ));
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
        ? geometry->focusBounds
        : MBoundingBox(MPoint::origin, MPoint::origin);
}

MPointArray lineSegments(const Strokes& strokes) {
    MPointArray segments;
    for (const Stroke& stroke : strokes) {
        for (unsigned int index = 1; index < stroke.length(); ++index) {
            segments.append(stroke[index - 1]);
            segments.append(stroke[index]);
        }
    }
    return segments;
}

struct ShapeDrawData final : public MUserData {
    std::shared_ptr<const BdControllerShapeNode::Geometry> geometry;
    MPointArray onTopSegments;
    MColor color;
    MColor offsetLineColor;
    MColor boundsPreviewColor;
    float lineWidth = 1.0f;
    bool drawOnTop = false;
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
        const auto geometry = nodeGeometry(objectPath.node());
        return geometry
            ? geometry->drawBounds
            : MBoundingBox(MPoint::origin, MPoint::origin);
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
        const auto geometry = nodeGeometry(objectPath.node());
        const bool geometryChanged = data->geometry != geometry;
        data->geometry = geometry;
        MStatus status;
        const float lineWidth = MPlug(
            objectPath.node(), BdControllerShapeNode::shapeLineWidth
        ).asFloat(&status);
        data->lineWidth = status && std::isfinite(lineWidth)
            ? std::max(1.0f, lineWidth)
            : 1.0f;
        const float transparency = MPlug(
            objectPath.node(), BdControllerShapeNode::shapeTransparency
        ).asFloat(&status);
        const float opacity = status && std::isfinite(transparency)
            ? 1.0f - std::clamp(transparency, 0.0f, 1.0f)
            : 1.0f;
        const bool wasDrawOnTop = data->drawOnTop;
        data->drawOnTop = MPlug(
            objectPath.node(), BdControllerShapeNode::shapeDrawOnTop
        ).asBool(&status);
        if (!status) {
            data->drawOnTop = false;
        }
        if (data->drawOnTop && (geometryChanged || !wasDrawOnTop)) {
            data->onTopSegments = data->geometry
                ? lineSegments(data->geometry->strokes)
                : MPointArray();
        }
        data->color = MHWRender::MGeometryUtilities::wireframeColor(objectPath);
        if (data->geometry && !data->geometry->boundsPreview.empty()) {
            MStatus colorStatus;
            data->boundsPreviewColor = M3dView::templateColor(&colorStatus);
            if (!colorStatus) {
                data->boundsPreviewColor = data->color;
            }
        }
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
        data->color.a *= opacity;
        if (data->geometry && data->geometry->offsetLine.length() == 2) {
            data->offsetLineColor.a *= opacity;
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
        if (data->lineWidth > 1.0f) {
            drawManager.setLineWidth(data->lineWidth);
        }
        if (data->drawOnTop && data->onTopSegments.length() > 0) {
            drawManager.beginDrawInXray();
            drawManager.mesh(
                MHWRender::MUIDrawManager::kLines, data->onTopSegments
            );
            drawManager.endDrawInXray();
        } else {
            for (const Stroke& stroke : data->geometry->strokes) {
                drawManager.lineStrip(stroke, false);
            }
        }
        drawManager.endDrawable();
        if (data->geometry->offsetLine.length() == 2) {
            drawManager.beginDrawable(
                data->geometry->offsetLineTemplate
                    ? MHWRender::MUIDrawManager::kNonSelectable
                    : MHWRender::MUIDrawManager::kSelectable
            );
            drawManager.setColor(data->offsetLineColor);
            if (data->lineWidth > 1.0f) {
                drawManager.setLineWidth(data->lineWidth);
            }
            if (data->drawOnTop) {
                drawManager.beginDrawInXray();
                drawManager.mesh(
                    MHWRender::MUIDrawManager::kLines,
                    data->geometry->offsetLine
                );
                drawManager.endDrawInXray();
            } else {
                drawManager.lineStrip(data->geometry->offsetLine, false);
            }
            drawManager.endDrawable();
        }
        if (!data->geometry->boundsPreview.empty()) {
            drawManager.beginDrawable(MHWRender::MUIDrawManager::kNonSelectable);
            drawManager.setColor(data->boundsPreviewColor);
            for (const Stroke& stroke : data->geometry->boundsPreview) {
                drawManager.lineStrip(stroke, false);
            }
            drawManager.endDrawable();
        }
    }
};

}  // namespace

struct BdControllerShapeNode::GeometryCache {
    std::mutex mutex;
    ShapeSettings settings;
    ShapeSettings customSettings;
    std::shared_ptr<const Geometry> base;
    std::shared_ptr<const Geometry> shapeValue;
    std::shared_ptr<const Geometry> customBase;
    std::shared_ptr<const Geometry> customValue;
    std::shared_ptr<const Geometry> value;
    MBoundingBox centeredBaseBounds;
    MMatrix animationMatrix = MMatrix::identity;
    std::uint64_t baseRevision = 0;
    std::uint64_t animationRevision = 0;
    std::uint64_t boundsRevision = 0;
    short boundsMode = 0;
    bool showBoundsPreview = false;
    bool hasConnectedInput = false;
    bool hasConnectedAnimationInput = false;
    bool hasConnectedBoundsInput = false;
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
                     MNodeMessage::kConnectionBroken))) {
        return;
    }
    auto* node = static_cast<BdControllerShapeNode*>(clientData);
    if (plug.attribute() == shapeAnimationTransformMatrix) {
        node->animationRevision_.fetch_add(1, std::memory_order_release);
    } else if (isShapeAttribute(plug.attribute())) {
        node->geometryRevision_.fetch_add(1, std::memory_order_release);
    } else if (isBoundsAttribute(plug.attribute())) {
        node->boundsRevision_.fetch_add(1, std::memory_order_release);
    }
}

std::shared_ptr<const BdControllerShapeNode::Geometry>
BdControllerShapeNode::geometry() const {
    GeometryCache& cache = *geometryCache_;
    const std::lock_guard<std::mutex> lock(cache.mutex);
    const std::uint64_t baseRevision = geometryRevision_.load(
        std::memory_order_acquire
    );
    const std::uint64_t animationRevision = animationRevision_.load(
        std::memory_order_acquire
    );
    const std::uint64_t boundsRevision = boundsRevision_.load(
        std::memory_order_acquire
    );
    if (cache.value && cache.baseRevision == baseRevision &&
        cache.animationRevision == animationRevision &&
        cache.boundsRevision == boundsRevision &&
        !cache.hasConnectedInput && !cache.hasConnectedAnimationInput &&
        !cache.hasConnectedBoundsInput &&
        attributeChangedCallback_ != 0) {
        return cache.value;
    }

    bool baseChanged = false;
    if (!cache.base || cache.baseRevision != baseRevision ||
        cache.hasConnectedInput || attributeChangedCallback_ == 0) {
        ShapeSettings settings;
        if (!readSettings(thisMObject(), shapeAttributes(), settings)) {
            return cache.value;
        }
        const bool connected = hasConnectedSettingsInput(
            thisMObject(), shapeAttributes()
        );
        if (!cache.base || !sameSettings(settings, cache.settings)) {
            cache.base = makeBaseGeometry(settings);
            cache.centeredBaseBounds = centeredShapeBounds(settings);
            cache.settings = settings;
            baseChanged = true;
        }
        cache.baseRevision = baseRevision;
        cache.hasConnectedInput = connected;
    }

    bool customBaseChanged = false;
    bool boundsStateChanged = false;
    if (!cache.customBase || cache.boundsRevision != boundsRevision ||
        cache.hasConnectedBoundsInput || attributeChangedCallback_ == 0) {
        MStatus status;
        short mode = MPlug(thisMObject(), boundsMode).asShort(&status);
        if (!status) {
            return cache.value;
        }
        if (mode < 0 || mode > 2) {
            mode = 0;
        }
        const bool showPreview = MPlug(
            thisMObject(), showBoundsPreview
        ).asBool(&status);
        if (!status) {
            return cache.value;
        }
        ShapeSettings customSettings;
        if (!readSettings(
                thisMObject(), customBoundsAttributes(), customSettings
            )) {
            return cache.value;
        }
        if (!cache.customBase ||
            !sameSettings(customSettings, cache.customSettings)) {
            cache.customBase = makeBaseGeometry(customSettings);
            cache.customSettings = customSettings;
            customBaseChanged = true;
        }
        boundsStateChanged = cache.boundsMode != mode ||
            cache.showBoundsPreview != showPreview;
        cache.boundsMode = mode;
        cache.showBoundsPreview = showPreview;
        cache.boundsRevision = boundsRevision;
        cache.hasConnectedBoundsInput = hasConnectedBoundsInput(thisMObject());
    }

    bool animationChanged = false;
    if (!cache.shapeValue || cache.animationRevision != animationRevision ||
        cache.hasConnectedAnimationInput || attributeChangedCallback_ == 0) {
        MMatrix animationMatrix;
        if (!readAnimationMatrix(thisMObject(), animationMatrix)) {
            return cache.value;
        }
        const bool connected = hasIncomingConnection(MPlug(
            thisMObject(), shapeAnimationTransformMatrix
        ));
        if (!sameMatrix(animationMatrix, cache.animationMatrix)) {
            cache.animationMatrix = animationMatrix;
            animationChanged = true;
        }
        cache.animationRevision = animationRevision;
        cache.hasConnectedAnimationInput = connected;
    }

    bool shapeValueChanged = false;
    if (!cache.shapeValue || baseChanged || animationChanged) {
        cache.shapeValue = sameMatrix(
            cache.animationMatrix, MMatrix::identity
        ) ? cache.base : transformGeometry(
            *cache.base,
            cache.animationMatrix,
            cache.settings.showOffsetLine
        );
        shapeValueChanged = true;
    }

    bool customValueChanged = false;
    if (cache.boundsMode == 2) {
        if (!cache.customValue || customBaseChanged || animationChanged) {
            cache.customValue = sameMatrix(
                cache.animationMatrix, MMatrix::identity
            ) ? cache.customBase : transformGeometry(
                *cache.customBase, cache.animationMatrix, false
            );
            customValueChanged = true;
        }
    } else if (customBaseChanged || animationChanged) {
        cache.customValue.reset();
    }

    if (!cache.value || shapeValueChanged || customValueChanged ||
        boundsStateChanged) {
        auto result = std::make_shared<Geometry>(*cache.shapeValue);
        result->focusBounds = cache.boundsMode == 1
            ? transformBounds(cache.centeredBaseBounds, cache.animationMatrix)
            : cache.boundsMode == 2
                ? cache.customValue->bounds
                : result->bounds;
        result->drawBounds = result->bounds;
        if (cache.showBoundsPreview) {
            const MBoundingBox& previewBounds = result->focusBounds;
            result->boundsPreview = boundsStrokes(previewBounds);
            for (const MPoint& corner : boundsCorners(previewBounds)) {
                result->drawBounds.expand(corner);
            }
        }
        cache.value = std::move(result);
    }
    return cache.value;
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
    for (const MObject& attribute : {
             channelBoxSeparator1,
             channelBoxSeparator2,
             channelBoxSeparator3,
             channelBoxSeparator4,
             channelBoxSeparator5,
         }) {
        const MStatus status = MPlug(node, attribute).setLocked(true);
        if (!status) {
            status.perror("Failed to lock bdControllerShape separator");
        }
    }
}

MStatus BdControllerShapeNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnTypedAttribute typedAttributeFn;
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

    for (const auto& axisAttribute : {
             std::pair<MObject*, std::pair<const char*, const char*>>{
                 &shape1stAxis, {"shape1stAxis", "s1a"}},
             std::pair<MObject*, std::pair<const char*, const char*>>{
                 &shape2ndAxis, {"shape2ndAxis", "s2a"}},
         }) {
        const short defaultAxis = axisAttribute.first == &shape1stAxis ? 0 : 2;
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
    }

    MFnMatrixData matrixDataFn;
    const MObject identityMatrix = matrixDataFn.create(MMatrix::identity, &status);
    if (!status) {
        return status;
    }
    shapeAnimationTransformMatrix = typedAttributeFn.create(
        "shapeAnimationTransformMatrix",
        "satm",
        MFnData::kMatrix,
        identityMatrix,
        &status
    );
    if (!status) {
        return status;
    }
    status = typedAttributeFn.setKeyable(false);
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

    shapeLineWidth = numericAttributeFn.create(
        "shapeLineWidth", "slw", MFnNumericData::kFloat, 1.0f, &status
    );
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMin(1.0);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    shapeTransparency = numericAttributeFn.create(
        "shapeTransparency", "stp", MFnNumericData::kFloat, 0.0f, &status
    );
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMax(1.0);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        shapeDrawOnTop,
        "shapeDrawOnTop",
        "sdot",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    boundsMode = enumAttributeFn.create("boundsMode", "bdm", 0, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, short>{"Shape", 0},
             std::pair<const char*, short>{"ShapeCentered", 1},
             std::pair<const char*, short>{"Custom", 2},
         }) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        showBoundsPreview,
        "showBoundsPreview",
        "sbp",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    for (const auto& axisAttribute : {
             std::pair<MObject*, std::pair<const char*, const char*>>{
                 &customBounds1stAxis, {"customBounds1stAxis", "cb1a"}},
             std::pair<MObject*, std::pair<const char*, const char*>>{
                 &customBounds2ndAxis, {"customBounds2ndAxis", "cb2a"}},
         }) {
        const short defaultAxis = axisAttribute.first == &customBounds1stAxis
            ? 0 : 2;
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
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        customBoundsRootSize,
        "customBoundsRootSize",
        "cbrs",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        customBoundsTranslate,
        customBoundsTranslateX,
        customBoundsTranslateY,
        customBoundsTranslateZ,
        "customBoundsTranslate", "cbt",
        "customBoundsTranslateX", "cbtx",
        "customBoundsTranslateY", "cbty",
        "customBoundsTranslateZ", "cbtz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        customBoundsRotate,
        customBoundsRotateX,
        customBoundsRotateY,
        customBoundsRotateZ,
        "customBoundsRotate", "cbr",
        "customBoundsRotateX", "cbrx",
        "customBoundsRotateY", "cbry",
        "customBoundsRotateZ", "cbrz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        customBoundsScale,
        customBoundsScaleX,
        customBoundsScaleY,
        customBoundsScaleZ,
        "customBoundsScale", "cbsc",
        "customBoundsScaleX", "cbscx",
        "customBoundsScaleY", "cbscy",
        "customBoundsScaleZ", "cbscz",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        customBoundsAxisOffsetLength,
        "customBoundsAxisOffsetLength",
        "cbaol",
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

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        customBoundsAxisOffset,
        "customBoundsAxisOffset",
        "cbao",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    customBoundsAxisOffsetDirection = enumAttributeFn.create(
        "customBoundsAxisOffsetDirection", "cbaod", 0, &status
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        customBoundsAxisTranslate,
        customBoundsAxisTranslateX,
        customBoundsAxisTranslateY,
        customBoundsAxisTranslateZ,
        "customBoundsAxisTranslate", "cbat",
        "customBoundsAxisTranslateX", "cbatx",
        "customBoundsAxisTranslateY", "cbaty",
        "customBoundsAxisTranslateZ", "cbatz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        customBoundsAxisRotate,
        customBoundsAxisRotateX,
        customBoundsAxisRotateY,
        customBoundsAxisRotateZ,
        "customBoundsAxisRotate", "cbar",
        "customBoundsAxisRotateX", "cbarx",
        "customBoundsAxisRotateY", "cbary",
        "customBoundsAxisRotateZ", "cbarz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        customBoundsAxisScale,
        customBoundsAxisScaleX,
        customBoundsAxisScaleY,
        customBoundsAxisScaleZ,
        "customBoundsAxisScale", "cbasc",
        "customBoundsAxisScaleX", "cbascx",
        "customBoundsAxisScaleY", "cbascy",
        "customBoundsAxisScaleZ", "cbascz",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        customBoundsSize,
        "customBoundsSize",
        "cbs",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(numericAttributeFn);
    if (!status) {
        return status;
    }

    for (const auto& separator : {
             std::pair<MObject*, const char*>{&channelBoxSeparator1, "_"},
             std::pair<MObject*, const char*>{&channelBoxSeparator2, "__"},
             std::pair<MObject*, const char*>{&channelBoxSeparator3, "___"},
             std::pair<MObject*, const char*>{&channelBoxSeparator4, "____"},
             std::pair<MObject*, const char*>{&channelBoxSeparator5, "_____"},
         }) {
        *separator.first = enumAttributeFn.create(
            separator.second, separator.second, 0, &status
        );
        if (!status) {
            return status;
        }
        status = enumAttributeFn.addField("-----------------------------------", 0);
        if (!status) {
            return status;
        }
        status = enumAttributeFn.setStorable(false);
        if (!status) {
            return status;
        }
        status = enumAttributeFn.setConnectable(false);
        if (!status) {
            return status;
        }
    }

    for (const MObject& attribute : {
             shape,
             shapeDrawOnTop,
             shapeLineWidth,
             shapeTransparency,
             showShapeOffsetLine,
             shapeOffsetLineTemplate,
             channelBoxSeparator1,
             shape1stAxis,
             shape2ndAxis,
             shapeAxisOffset,
             shapeAxisOffsetDirection,
             shapeAxisOffsetLength,
             channelBoxSeparator2,
             shapeRootSize,
             shapeTranslate,
             shapeRotate,
             shapeScale,
             shapeAxisTranslate,
             shapeAxisRotate,
             shapeAxisScale,
             shapeSize,
             channelBoxSeparator3,
             boundsMode,
             showBoundsPreview,
             channelBoxSeparator4,
             customBounds1stAxis,
             customBounds2ndAxis,
             customBoundsAxisOffset,
             customBoundsAxisOffsetDirection,
             customBoundsAxisOffsetLength,
             channelBoxSeparator5,
             customBoundsRootSize,
             customBoundsTranslate,
             customBoundsRotate,
             customBoundsScale,
             customBoundsAxisTranslate,
             customBoundsAxisRotate,
             customBoundsAxisScale,
             customBoundsSize,
             shapeTranslateX,
             shapeTranslateY,
             shapeTranslateZ,
             shapeRotateX,
             shapeRotateY,
             shapeRotateZ,
             shapeScaleX,
             shapeScaleY,
             shapeScaleZ,
             shapeAxisTranslateX,
             shapeAxisTranslateY,
             shapeAxisTranslateZ,
             shapeAxisRotateX,
             shapeAxisRotateY,
             shapeAxisRotateZ,
             shapeAxisScaleX,
             shapeAxisScaleY,
             shapeAxisScaleZ,
             customBoundsTranslateX,
             customBoundsTranslateY,
             customBoundsTranslateZ,
             customBoundsRotateX,
             customBoundsRotateY,
             customBoundsRotateZ,
             customBoundsScaleX,
             customBoundsScaleY,
             customBoundsScaleZ,
             customBoundsAxisTranslateX,
             customBoundsAxisTranslateY,
             customBoundsAxisTranslateZ,
             customBoundsAxisRotateX,
             customBoundsAxisRotateY,
             customBoundsAxisRotateZ,
             customBoundsAxisScaleX,
             customBoundsAxisScaleY,
             customBoundsAxisScaleZ,
         }) {
        MFnAttribute attributeFn(attribute, &status);
        if (!status) {
            return status;
        }
        status = attributeFn.setKeyable(false);
        if (!status) {
            return status;
        }
        status = attributeFn.setChannelBox(true);
        if (!status) {
            return status;
        }
    }

    for (const MObject& attribute : {
             shape,
             shapeAnimationTransformMatrix,
             shapeDrawOnTop,
             shapeLineWidth,
             shapeTransparency,
             showShapeOffsetLine,
             shapeOffsetLineTemplate,
             channelBoxSeparator1,
             shape1stAxis,
             shape2ndAxis,
             shapeAxisOffset,
             shapeAxisOffsetDirection,
             shapeAxisOffsetLength,
             channelBoxSeparator2,
             shapeRootSize,
             shapeTranslate,
             shapeRotate,
             shapeScale,
             shapeAxisTranslate,
             shapeAxisRotate,
             shapeAxisScale,
             shapeSize,
             channelBoxSeparator3,
             boundsMode,
             showBoundsPreview,
             channelBoxSeparator4,
             customBounds1stAxis,
             customBounds2ndAxis,
             customBoundsAxisOffset,
             customBoundsAxisOffsetDirection,
             customBoundsAxisOffsetLength,
             channelBoxSeparator5,
             customBoundsRootSize,
             customBoundsTranslate,
             customBoundsRotate,
             customBoundsScale,
             customBoundsAxisTranslate,
             customBoundsAxisRotate,
             customBoundsAxisScale,
             customBoundsSize,
         }) {
        status = addAttribute(attribute);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
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
