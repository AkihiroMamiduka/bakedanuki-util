// 面の倍率は共有する角へ乗算し、箱の内外へ三線形に補間する。
bool hasCageMapping(const ShapeSettings& settings) {
    return std::any_of(settings.baseSpaceFaceScale.begin(), settings.baseSpaceFaceScale.end(),
        [](double scale) { return scale != 1.0; });
}

double cageFaceScale(unsigned int normal, unsigned int component, bool plus,
    const ShapeSettings& settings) {
    if (normal == component) return 1.0;
    const unsigned int ordinal = component < normal ? component : component - 1;
    return settings.baseSpaceFaceScale[normal * 4 + (plus ? 0 : 2) + ordinal];
}

MVector cageSpan(const ShapeSettings& settings) {
    auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    if (isCapsuleBody(settings)) {
        // 中心間が0でも残る半球を含め、主軸の倍率面を完成した本体の外端へ置く。
        const unsigned int axis = settings.axisSwap ? 1 : 0;
        span[axis] = (span[axis] >= 0.0 ? 1.0 : -1.0) *
            (std::abs(span[axis]) + bodyAxisRadius(settings, false) + bodyAxisRadius(settings, true));
    }
    if (isCenteredArrowBody(settings)) {
        const unsigned int axis = settings.axisSwap ? 1 : 0;
        span[axis] = (span[axis] >= 0.0 ? 1.0 : -1.0) *
            (bodyAxisRadius(settings, false) + bulkArrowFront(settings));
    }
    return span;
}

MVector cageCenter(const ShapeSettings& settings) {
    auto center = (settings.baseSpaceMinus + settings.baseSpacePlus) * 0.5;
    if (isCapsuleBody(settings)) {
        const unsigned int axis = settings.axisSwap ? 1 : 0;
        const double direction = settings.baseSpacePlus[axis] >= settings.baseSpaceMinus[axis] ? 1.0 : -1.0;
        center[axis] += direction * (bodyAxisRadius(settings, true) - bodyAxisRadius(settings, false)) * 0.5;
    }
    if (isCenteredArrowBody(settings)) {
        const unsigned int axis = settings.axisSwap ? 1 : 0;
        const double direction = settings.baseSpacePlus[axis] >= settings.baseSpaceMinus[axis] ? 1.0 : -1.0;
        center[axis] = settings.baseSpaceMinus[axis] +
            direction * (bulkArrowFront(settings) - bodyAxisRadius(settings, false)) * 0.5;
    }
    return center;
}

MVector cageCoordinates(const MPoint& point, const ShapeSettings& settings) {
    const auto center = cageCenter(settings);
    const auto span = cageSpan(settings);
    MVector result;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        result[axis] = (point[axis] - center[axis]) / (span[axis] == 0.0 ? 1.0 : span[axis]);
    }
    return result;
}

double cageInterpolatedScale(unsigned int normal, unsigned int component, double coordinate,
    const ShapeSettings& settings) {
    return (0.5 - coordinate) * cageFaceScale(normal, component, false, settings) +
        (0.5 + coordinate) * cageFaceScale(normal, component, true, settings);
}

MPoint cagePoint(const MPoint& point, const ShapeSettings& settings) {
    if (!hasCageMapping(settings)) return point;
    const auto center = cageCenter(settings);
    const auto coordinate = cageCoordinates(point, settings);
    auto result = point;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        const unsigned int first = (axis + 1) % 3, second = (axis + 2) % 3;
        const double scale = cageInterpolatedScale(first, axis, coordinate[first], settings) *
            cageInterpolatedScale(second, axis, coordinate[second], settings);
        const double value = center[axis] + (point[axis] - center[axis]) * scale;
        if (std::isfinite(value)) result[axis] = value;
    }
    return result;
}

MVector cageVector(const MPoint& point, const MVector& vector, const ShapeSettings& settings) {
    if (!hasCageMapping(settings)) return vector;
    const auto center = cageCenter(settings);
    const auto span = cageSpan(settings);
    const auto coordinate = cageCoordinates(point, settings);
    MVector result;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        const unsigned int first = (axis + 1) % 3, second = (axis + 2) % 3;
        const double a = cageInterpolatedScale(first, axis, coordinate[first], settings);
        const double b = cageInterpolatedScale(second, axis, coordinate[second], settings);
        const double da = (cageFaceScale(first, axis, true, settings) -
            cageFaceScale(first, axis, false, settings)) / (span[first] == 0.0 ? 1.0 : span[first]);
        const double db = (cageFaceScale(second, axis, true, settings) -
            cageFaceScale(second, axis, false, settings)) / (span[second] == 0.0 ? 1.0 : span[second]);
        const double value = vector[axis] * a * b + (point[axis] - center[axis]) *
            (vector[first] * da * b + vector[second] * db * a);
        result[axis] = std::isfinite(value) ? value : vector[axis];
    }
    return result;
}

double cageDeterminant(const MPoint& point, const ShapeSettings& settings) {
    const auto x = cageVector(point, MVector(1, 0, 0), settings);
    const auto y = cageVector(point, MVector(0, 1, 0), settings);
    const auto z = cageVector(point, MVector(0, 0, 1), settings);
    return (x ^ y) * z;
}

MVector cageNormal(const MPoint& point, const MVector& normal, const ShapeSettings& settings) {
    const auto x = cageVector(point, MVector(1, 0, 0), settings);
    const auto y = cageVector(point, MVector(0, 1, 0), settings);
    const auto z = cageVector(point, MVector(0, 0, 1), settings);
    auto result = (y ^ z) * normal.x + (z ^ x) * normal.y + (x ^ y) * normal.z;
    if ((x ^ y) * z < 0.0) result = -result;
    if (std::hypot(result.x, result.y, result.z) == 0.0) result = cageVector(point, normal, settings);
    if (std::hypot(result.x, result.y, result.z) == 0.0) result = normal;
    return baseSpaceNormalized(result);
}

MPoint cageBaseBodyPoint(const MPoint& point, const ShapeSettings& settings) {
    return bodyBaseSpacePoint(point, settings);
}

MPoint cageBodyPoint(const MPoint& point, const ShapeSettings& settings) {
    return cagePoint(cageBaseBodyPoint(point, settings), settings);
}
