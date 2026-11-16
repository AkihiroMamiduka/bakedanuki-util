// 球と箱の中心をMinusへ置き、本体の前へ出る先端だけを錐でつなぐ。
bool isBulkArrowBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == kCubeArrowOutline || outline == kSphereArrowOutline ||
        outline == kSquareArrowPlanarOutline || outline == kCircleArrowPlanarOutline;
}

bool isPlanarArrowBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == 39 || outline == kDiamondArrowOutline || outline == kSquareArrowPlanarOutline ||
        outline == kCircleArrowPlanarOutline;
}

bool isSpatialArrowBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == kArrowSpatialOutline || outline == 25 || outline == kCubeArrowOutline || outline == kSphereArrowOutline;
}

bool isNotchedArrowBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == 39 || outline == kArrowSpatialOutline;
}

bool isRoundArrowBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == kCircleArrowPlanarOutline || outline == kSphereArrowOutline;
}

double bulkArrowRearRadius(const ShapeSettings& settings) {
    return bodyAxisRadius(settings, false);
}

double bulkArrowFrontRadius(const ShapeSettings& settings) {
    return bodyAxisRadius(settings, true);
}

bool isCenteredArrowBody(const ShapeSettings& settings) {
    return isPlanarArrowBody(settings) || isSpatialArrowBody(settings);
}

double arrowRearDepth(const ShapeSettings& settings) {
    return bodyAxisRadius(settings, false) * (isNotchedArrowBody(settings) ? 0.5 : 1.0);
}

double arrowMotherFront(const ShapeSettings& settings) {
    return bodyAxisRadius(settings, true) * (isNotchedArrowBody(settings) ? 1.5 : 1.0);
}

double bulkArrowLength(const ShapeSettings& settings) {
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    return std::abs(settings.baseSpacePlus[axis] - settings.baseSpaceMinus[axis]);
}

double bulkArrowFront(const ShapeSettings& settings) {
    return std::max(bulkArrowLength(settings), arrowMotherFront(settings));
}

bool bulkArrowHasHead(const ShapeSettings& settings) {
    return bulkArrowLength(settings) > arrowMotherFront(settings);
}

MPoint bulkArrowBodyCenter(const ShapeSettings&) {
    return MPoint::origin;
}

MPoint bodyNativeCenter(const ShapeSettings& settings) {
    return isNotchedArrowBody(settings) ? MPoint(-0.25, 0, 0) : MPoint::origin;
}

double bulkArrowConeJoin(const ShapeSettings& settings) {
    const double radius = bulkArrowFrontRadius(settings);
    return bulkArrowHasHead(settings) ? radius * radius / bulkArrowLength(settings) : radius;
}

double bulkArrowJoinAngle(const ShapeSettings& settings) {
    const double radius = bulkArrowFrontRadius(settings);
    return bulkArrowHasHead(settings) ? std::acos(std::clamp(radius / bulkArrowLength(settings), 0.0, 1.0)) : 0.0;
}

double bulkArrowBodyCoordinate(double coordinate, const ShapeSettings& settings) {
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    const double minus = settings.baseSpaceMinus[axis], plus = settings.baseSpacePlus[axis];
    return minus + (plus >= minus ? 1.0 : -1.0) * coordinate;
}

std::vector<MPoint> notchedArrowProfilePoints() {
    return {MPoint(0.5, 0, 0), MPoint(-0.25, -0.5, 0), MPoint(-0.5, -0.25, 0),
        MPoint(-0.25, 0, 0), MPoint(-0.5, 0.25, 0), MPoint(-0.25, 0.5, 0), MPoint(0.5, 0, 0)};
}

std::vector<MPoint> bulkArrowProfilePoints(const ShapeSettings& settings) {
    const double rearRadius = bulkArrowRearRadius(settings), frontRadius = bulkArrowFrontRadius(settings);
    const double front = bulkArrowFront(settings);
    if (!isRoundArrowBody(settings)) {
        std::vector<MPoint> result = {MPoint(-rearRadius, -0.5, 0), MPoint(frontRadius, -0.5, 0)};
        if (bulkArrowHasHead(settings)) result.emplace_back(front, 0, 0);
        result.emplace_back(frontRadius, 0.5, 0);
        result.emplace_back(-rearRadius, 0.5, 0);
        result.push_back(result.front());
        return result;
    }
    std::vector<MPoint> result;
    const double first = bulkArrowJoinAngle(settings), last = 2.0 * kPi - first;
    if (bulkArrowHasHead(settings)) result.emplace_back(front, 0, 0);
    const auto at = [&](double angle) {
        const double cosine = std::cos(angle);
        return MPoint((cosine < 0.0 ? rearRadius : frontRadius) * cosine, 0.5 * std::sin(angle), 0);
    };
    result.push_back(at(first));
    for (unsigned int i = 1; i < kCircleSegments; ++i) {
        const double angle = 2.0 * kPi * i / kCircleSegments;
        if (angle > first && angle < last) result.push_back(at(angle));
    }
    result.push_back(at(last));
    if (bulkArrowHasHead(settings)) result.emplace_back(front, 0, 0);
    return result;
}

MPoint bulkArrowProjectedPoint(MPoint point, const ShapeSettings& settings) {
    if (!isRoundArrowBody(settings)) return point;
    const double radius = point.x < 0.0 ? bulkArrowRearRadius(settings) : bulkArrowFrontRadius(settings);
    const double join = bulkArrowConeJoin(settings);
    if (bulkArrowHasHead(settings) && point.x >= join) {
        const double current = std::hypot(point.y, point.z);
        const double target = 0.5 * std::sin(bulkArrowJoinAngle(settings)) *
            (bulkArrowFront(settings) - point.x) / (bulkArrowFront(settings) - join);
        if (current != 0.0) { point.y *= target / current; point.z *= target / current; }
        return point;
    }
    if (radius == 0.0) return point;
    auto normal = MVector(point.x / radius, point.y * 2.0, point.z * 2.0);
    const double length = normal.length();
    if (length == 0.0) return point;
    normal /= length;
    return MPoint(radius * normal.x, 0.5 * normal.y, 0.5 * normal.z);
}
