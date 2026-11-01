// 接合は基準座標で行い、付属物の局所寸法だけを完成後の空間から逆算する。
bool hasBaseSpaceMapping(const ShapeSettings& settings) {
    return !sameVector(settings.baseSpaceMinus, MVector(-0.5, -0.5, -0.5)) ||
        !sameVector(settings.baseSpacePlus, MVector(0.5, 0.5, 0.5));
}

MVector baseSpaceScale(const ShapeSettings& settings) {
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    const bool exchange = hasLegacyPlanarOrientation(outlinePresetIndex(settings.shape)) !=
        (settings.axisSwap && !isColorOutline(outlinePresetIndex(settings.shape)));
    MVector result = exchange ? MVector(span.y, span.x, span.z) : span;
    if (settings.baseSpaceCrossPlane) std::swap(result.x, result.z);
    return result;
}

bool hasBaseSpaceScale(const ShapeSettings& settings) {
    return !sameVector(baseSpaceScale(settings), MVector(1, 1, 1));
}

bool hasSingularBaseSpace(const ShapeSettings& settings) {
    const auto span = baseSpaceScale(settings);
    return span.x == 0.0 || span.y == 0.0 || span.z == 0.0;
}

MVector baseSpaceVector(const MVector& vector, const ShapeSettings& settings) {
    const auto span = baseSpaceScale(settings);
    return MVector(vector.x * span.x, vector.y * span.y, vector.z * span.z);
}

MVector inverseBaseSpaceVector(const MVector& vector, const ShapeSettings& settings) {
    const auto span = baseSpaceScale(settings);
    return MVector(span.x == 0.0 ? 0.0 : vector.x / span.x,
        span.y == 0.0 ? 0.0 : vector.y / span.y,
        span.z == 0.0 ? 0.0 : vector.z / span.z);
}

double baseSpaceDirectionLength(const MVector& direction, const ShapeSettings& settings) {
    const auto vector = baseSpaceVector(direction, settings);
    return std::hypot(vector.x, vector.y, vector.z);
}

MVector baseSpacePartDirection(const MVector& direction, const ShapeSettings& settings) {
    const double length = baseSpaceDirectionLength(direction, settings);
    return length == 0.0 ? direction : direction / length;
}

struct BaseSpacePartFrame {
    MVector along;
    MVector side;
    MVector up;
};

MVector baseSpaceNormalized(const MVector& vector) {
    const double length = std::hypot(vector.x, vector.y, vector.z);
    return length == 0.0 ? MVector::zero : vector / length;
}

BaseSpacePartFrame baseSpacePartFrame(const MVector& along, const MVector& side,
    const MVector& up, const ShapeSettings& settings) {
    if (!hasBaseSpaceScale(settings)) return {along, side, up};
    auto physicalAlong = baseSpaceNormalized(baseSpaceVector(along, settings));
    auto physicalSide = baseSpaceVector(side, settings);
    physicalSide -= physicalAlong * (physicalAlong * physicalSide);
    physicalSide = baseSpaceNormalized(physicalSide);
    auto physicalUp = baseSpaceNormalized(physicalAlong ^ physicalSide);
    if (physicalUp * baseSpaceVector(up, settings) < 0.0) physicalUp = -physicalUp;
    return {inverseBaseSpaceVector(physicalAlong, settings),
        inverseBaseSpaceVector(physicalSide, settings), inverseBaseSpaceVector(physicalUp, settings)};
}

MPoint baseSpacePoint(const MPoint& point, const ShapeSettings& settings) {
    const auto center = (settings.baseSpaceMinus + settings.baseSpacePlus) * 0.5;
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    return MPoint(center.x + point.x * span.x, center.y + point.y * span.y,
        center.z + point.z * span.z);
}

MPoint baseSpaceMetricPoint(const MPoint& point, const ShapeSettings& settings, bool inverse = false) {
    const auto vector = point - MPoint::origin;
    return MPoint::origin + (inverse ? inverseBaseSpaceVector(vector, settings) : baseSpaceVector(vector, settings));
}

void mapBaseSpaceMetricGeometry(BdControllerShapeNode::Geometry& geometry,
    const ShapeSettings& settings, bool inverse = false) {
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point = baseSpaceMetricPoint(point, settings, inverse);
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point = baseSpaceMetricPoint(point, settings, inverse);
}
