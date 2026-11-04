// 基準空間の変更後に表面距離を測り、既存の接合へ渡す座標だけを逆変換する。
struct MetricWideSphereBands {
    static constexpr unsigned int samples = 256;
    std::array<double, 3> radii;
    std::array<std::vector<std::pair<double, double>>, 3> limits;
    std::array<std::vector<MPoint>, 3> boundary;

    MVector acceleration(const MVector& point, const MVector& velocity) const {
        const MVector normal(point.x / (radii[0] * radii[0]), point.y / (radii[1] * radii[1]),
            point.z / (radii[2] * radii[2]));
        const double speed = velocity.x * velocity.x / (radii[0] * radii[0]) +
            velocity.y * velocity.y / (radii[1] * radii[1]) + velocity.z * velocity.z / (radii[2] * radii[2]);
        return normal * (-speed / (normal * normal));
    }

    MPoint trace(MVector point, MVector velocity, double distance) const {
        const double minimum = std::min({radii[0], radii[1], radii[2]});
        const unsigned int steps = static_cast<unsigned int>(std::clamp(std::ceil(distance / (minimum * 0.02)), 8.0, 512.0));
        const double h = distance / steps;
        for (unsigned int i = 0; i < steps; ++i) {
            const auto a = acceleration(point, velocity);
            const auto v2 = velocity + a * (h * 0.5);
            const auto b = acceleration(point + velocity * (h * 0.5), v2);
            const auto v3 = velocity + b * (h * 0.5);
            const auto c = acceleration(point + v2 * (h * 0.5), v3);
            const auto v4 = velocity + c * h;
            const auto d = acceleration(point + v3 * h, v4);
            point += (velocity + v2 * 2.0 + v3 * 2.0 + v4) * (h / 6.0);
            velocity += (a + b * 2.0 + c * 2.0 + d) * (h / 6.0);
            point /= std::sqrt(point.x * point.x / (radii[0] * radii[0]) +
                point.y * point.y / (radii[1] * radii[1]) + point.z * point.z / (radii[2] * radii[2]));
            const MVector normal(point.x / (radii[0] * radii[0]), point.y / (radii[1] * radii[1]),
                point.z / (radii[2] * radii[2]));
            velocity = baseSpaceNormalized(velocity - normal * ((velocity * normal) / (normal * normal)));
        }
        return MPoint(0.5 * point.x / radii[0], 0.5 * point.y / radii[1], 0.5 * point.z / radii[2]);
    }

    explicit MetricWideSphereBands(const ShapeSettings& settings) {
        const auto scale = baseSpaceScale(settings);
        radii = {std::abs(scale.x) * 0.5, std::abs(scale.y) * 0.5, std::abs(scale.z) * 0.5};
        const double distance = std::min(settings.wideWidth * 0.5,
            kPi * 0.5 * std::max({radii[0], radii[1], radii[2]}));
        for (unsigned int axis = 0; axis < 3; ++axis) {
            const unsigned int first = (axis + 1) % 3, second = (axis + 2) % 3;
            for (unsigned int i = 0; i < samples; ++i) {
                const double angle = 2.0 * kPi * i / samples;
                MPoint source;
                setGenericWideCoordinate(source, first, radii[first] * std::cos(angle));
                setGenericWideCoordinate(source, second, radii[second] * std::sin(angle));
                auto point = trace(source - MPoint::origin, nativeAxis(axis), distance);
                double position = std::atan2(genericWideCoordinate(point, second), genericWideCoordinate(point, first));
                if (position < 0.0) position += 2.0 * kPi;
                if (genericWideCoordinate(point, first) * std::cos(angle) +
                    genericWideCoordinate(point, second) * std::sin(angle) <= 1e-12) {
                    point = MPoint::origin + nativeAxis(axis) * 0.5;
                    position = angle;
                }
                boundary[axis].push_back(point);
                limits[axis].push_back({position, std::clamp(std::abs(genericWideCoordinate(point, axis)), 0.0, 0.5)});
            }
            std::sort(limits[axis].begin(), limits[axis].end());
        }
    }

    double limit(const MPoint& point, unsigned int axis) const {
        const unsigned int first = (axis + 1) % 3, second = (axis + 2) % 3;
        double angle = std::atan2(genericWideCoordinate(point, second), genericWideCoordinate(point, first));
        if (angle < 0.0) angle += 2.0 * kPi;
        const auto& table = limits[axis];
        auto found = std::upper_bound(table.begin(), table.end(), angle,
            [](double value, const auto& item) { return value < item.first; });
        const auto a = found == table.begin() ? table.back() : *(found - 1);
        const auto b = found == table.end() ? table.front() : *found;
        double low = a.first, high = b.first;
        if (found == table.begin()) low -= 2.0 * kPi;
        if (found == table.end()) high += 2.0 * kPi;
        const double fraction = high - low <= 1e-14 ? 0.0 : (angle - low) / (high - low);
        return a.second + (b.second - a.second) * fraction;
    }

    double value(const MPoint& point, unsigned int axis, double sign) const {
        return genericWideCoordinate(point, axis) - sign * limit(point, axis);
    }

    std::vector<MPoint> clip(const std::vector<MPoint>& polygon, unsigned int axis,
        double sign, bool positive) const {
        std::vector<MPoint> result;
        for (std::size_t i = 0; i < polygon.size(); ++i) {
            const auto a = polygon[i], b = polygon[(i + 1) % polygon.size()];
            const double first = value(a, axis, sign) * (positive ? 1.0 : -1.0);
            const double last = value(b, axis, sign) * (positive ? 1.0 : -1.0);
            if (first >= -1e-12) result.push_back(a);
            if ((first < -1e-12 && last > 1e-12) || (first > 1e-12 && last < -1e-12)) {
                double low = 0.0, high = 1.0;
                for (unsigned int step = 0; step < 28; ++step) {
                    const double t = (low + high) * 0.5;
                    const auto point = genericWideSpherePoint((a - MPoint::origin) * (1.0 - t) + (b - MPoint::origin) * t);
                    if ((value(point, axis, sign) * (positive ? 1.0 : -1.0) < 0.0) == (first < 0.0)) low = t;
                    else high = t;
                }
                const double t = (low + high) * 0.5;
                result.push_back(genericWideSpherePoint((a - MPoint::origin) * (1.0 - t) + (b - MPoint::origin) * t));
            }
        }
        return result;
    }
};

const MetricWideSphereBands& cachedMetricWideSphereBands(const ShapeSettings& settings) {
    thread_local MVector previous;
    thread_local double previousWidth = -1.0;
    thread_local std::unique_ptr<MetricWideSphereBands> cached;
    const auto scale = baseSpaceScale(settings);
    if (!cached || !sameVector(previous, scale) || previousWidth != settings.wideWidth) {
        cached = std::make_unique<MetricWideSphereBands>(settings);
        previous = scale;
        previousWidth = settings.wideWidth;
    }
    return *cached;
}

unsigned int metricWideSphereParentAxis(const MPoint& point, const ShapeSettings& settings) {
    const auto& metric = cachedMetricWideSphereBands(settings);
    unsigned int result = 0;
    double closest = 1e100;
    for (unsigned int axis = 0; axis < 3; ++axis) {
        const double ratio = std::abs(genericWideCoordinate(point, axis)) / std::max(metric.limit(point, axis), 1e-12);
        if (ratio < closest) { closest = ratio; result = axis; }
    }
    return result;
}

MPoint metricWideSphereTemplatePoint(MPoint point, unsigned int axis, const ShapeSettings& settings) {
    const auto& metric = cachedMetricWideSphereBands(settings);
    setGenericWideCoordinate(point, axis, std::abs(genericWideCoordinate(point, axis)));
    double closest = 1e100, position = 0.0;
    for (unsigned int i = 0; i < MetricWideSphereBands::samples; ++i) {
        const auto a = metric.boundary[axis][i], b = metric.boundary[axis][(i + 1) % MetricWideSphereBands::samples];
        const auto edge = baseSpaceVector(b - a, settings);
        const auto delta = baseSpaceVector(point - a, settings);
        const double squared = edge * edge;
        const double fraction = squared <= 1e-24 ? 0.0 : std::clamp((delta * edge) / squared, 0.0, 1.0);
        const auto remainder = delta - edge * fraction;
        if (remainder * remainder < closest) {
            closest = remainder * remainder;
            position = (i + fraction) * 2.0 * kPi / MetricWideSphereBands::samples;
        }
    }
    MPoint result;
    setGenericWideCoordinate(result, (axis + 1) % 3, 0.5 * std::cos(position));
    setGenericWideCoordinate(result, (axis + 2) % 3, 0.5 * std::sin(position));
    return result;
}

bool makeMetricWideSphereBands(const ShapeSettings& settings, PartGeometry& geometry) {
    const auto scale = baseSpaceScale(settings);
    const double minimum = std::min({std::abs(scale.x), std::abs(scale.y), std::abs(scale.z)});
    if (minimum <= 1e-12) return false;
    const bool covered = settings.wideWidth >= kPi * std::max({std::abs(scale.x), std::abs(scale.y), std::abs(scale.z)}) * 0.5;
    if (covered || (std::abs(std::abs(scale.x) - std::abs(scale.y)) < 1e-12 &&
        std::abs(std::abs(scale.x) - std::abs(scale.z)) < 1e-12)) {
        auto source = settings;
        source.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
        source.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        source.wideWidth = covered ? kPi : settings.wideWidth / std::abs(scale.x);
        makeGenericWideSphereBands(source, geometry);
        return true;
    }
    const auto& metric = cachedMetricWideSphereBands(settings);
    const auto reference = genericWideReferenceLines(settings);
    std::array<StrokeStyle, 3> styles = {StrokeStyle::Normal, StrokeStyle::Normal, StrokeStyle::Normal};
    for (std::size_t i = 0; i < reference.strokes.size(); ++i) {
        const auto& stroke = reference.strokes[i];
        if (stroke.length() < 4) continue;
        const auto normal = ((stroke[0] - MPoint::origin) ^ (stroke[stroke.length() / 4] - MPoint::origin)).normal();
        unsigned int axis = std::abs(normal.y) > std::abs(normal.x) ? 1 : 0;
        if (std::abs(normal.z) > std::abs(axis == 0 ? normal.x : normal.y)) axis = 2;
        styles[axis] = reference.strokeStyles[i];
    }
    clearGenericWideBodyFill(geometry);
    geometry.strokes.clear();
    geometry.strokeStyles.clear();
    const auto exposed = [&](const MPoint& point, unsigned int axis) {
        for (unsigned int other = 0; other < 3; ++other) if (other != axis &&
            std::abs(genericWideCoordinate(point, other)) < metric.limit(point, other) - 1e-10) return false;
        return true;
    };
    for (unsigned int axis = 0; axis < 3; ++axis) for (double sign : {-1.0, 1.0}) {
        for (unsigned int i = 0; i < MetricWideSphereBands::samples; ++i) {
            auto a = metric.boundary[axis][i], b = metric.boundary[axis][(i + 1) % MetricWideSphereBands::samples];
            setGenericWideCoordinate(a, axis, genericWideCoordinate(a, axis) * sign);
            setGenericWideCoordinate(b, axis, genericWideCoordinate(b, axis) * sign);
            const bool first = exposed(a, axis), last = exposed(b, axis);
            if (!first && !last) continue;
            if (first != last) {
                double low = 0.0, high = 1.0;
                for (unsigned int step = 0; step < 24; ++step) {
                    const double t = (low + high) * 0.5;
                    const auto point = genericWideSpherePoint((a - MPoint::origin) * (1.0 - t) + (b - MPoint::origin) * t);
                    if (exposed(point, axis) == first) low = t;
                    else high = t;
                }
                const double t = (low + high) * 0.5;
                const auto point = genericWideSpherePoint((a - MPoint::origin) * (1.0 - t) + (b - MPoint::origin) * t);
                if (first) b = point;
                else a = point;
            }
            appendGenericWideStroke(geometry, {a, b}, styles[axis]);
        }
    }
    if (geometry.strokes.empty() && !settings.fill) {
        geometry.strokes = reference.strokes;
        geometry.strokeStyles = reference.strokeStyles;
        return true;
    }
    if (!settings.fill) return true;
    PartBuilder bands(true);
    const auto append = [&](const std::array<MPoint, 3>& triangle) {
        std::vector<GenericWideSpherePiece> pieces = {{std::vector<MPoint>(triangle.begin(), triangle.end()), 0}};
        for (unsigned int axis = 0; axis < 3; ++axis) {
            std::vector<GenericWideSpherePiece> split;
            for (const auto& piece : pieces) {
                auto low = metric.clip(piece.points, axis, -1.0, false);
                auto high = metric.clip(piece.points, axis, 1.0, true);
                auto middle = metric.clip(metric.clip(piece.points, axis, -1.0, true), axis, 1.0, false);
                if (low.size() >= 3) split.push_back({std::move(low), piece.mask});
                if (high.size() >= 3) split.push_back({std::move(high), piece.mask});
                if (middle.size() >= 3) split.push_back({std::move(middle), piece.mask | (1u << axis)});
            }
            pieces = std::move(split);
        }
        constexpr std::array<StrokeStyle, 8> palette = {StrokeStyle::Normal, StrokeStyle::AxisX,
            StrokeStyle::AxisY, StrokeStyle::AxisXY, StrokeStyle::AxisZ, StrokeStyle::AxisXZ, StrokeStyle::AxisYZ, StrokeStyle::AxisXYZ};
        for (const auto& piece : pieces) {
            if (piece.mask == 0) continue;
            unsigned int color = 0;
            for (unsigned int axis = 0; axis < 3; ++axis) if ((piece.mask & (1u << axis)) != 0) {
                if (styles[axis] == StrokeStyle::AxisX) color |= 1;
                else if (styles[axis] == StrokeStyle::AxisY) color |= 2;
                else if (styles[axis] == StrokeStyle::AxisZ) color |= 4;
            }
            for (std::size_t i = 1; i + 1 < piece.points.size(); ++i) bands.triangle(
                piece.points[0], piece.points[i], piece.points[i + 1], palette[color]);
        }
    };
    constexpr unsigned int divisions = 24;
    for (double x : {-1.0, 1.0}) for (double y : {-1.0, 1.0}) for (double z : {-1.0, 1.0}) {
        const auto at = [&](unsigned int i, unsigned int j) {
            return genericWideSpherePoint(MVector(x * i, y * j, z * (divisions - i - j)));
        };
        for (unsigned int i = 0; i < divisions; ++i) for (unsigned int j = 0; j < divisions - i; ++j) {
            append({at(i, j), at(i + 1, j), at(i, j + 1)});
            if (i + j + 1 < divisions) append({at(i + 1, j), at(i + 1, j + 1), at(i, j + 1)});
        }
    }
    mergeGenericWideBandFills(geometry, std::move(bands.geometry));
    return true;
}

struct WideCurveMetric {
    static constexpr unsigned int divisions = 1024;
    std::array<double, divisions + 1> lengths{};

    template<typename Speed>
    static double integral(double first, double last, const Speed& speed) {
        return (last - first) * (speed(first) + 4.0 * speed((first + last) * 0.5) + speed(last)) / 6.0;
    }

    template<typename Speed>
    explicit WideCurveMetric(const Speed& speed) {
        for (unsigned int i = 1; i <= divisions; ++i) lengths[i] = lengths[i - 1] +
            integral(2.0 * kPi * (i - 1) / divisions, 2.0 * kPi * i / divisions, speed);
    }

    template<typename Speed>
    double position(double angle, const Speed& speed) const {
        const double turns = std::floor(angle / (2.0 * kPi));
        const double local = angle - turns * 2.0 * kPi;
        const unsigned int index = std::min(divisions - 1,
            static_cast<unsigned int>(local * divisions / (2.0 * kPi)));
        return turns * lengths.back() + lengths[index] +
            integral(2.0 * kPi * index / divisions, local, speed);
    }

    template<typename Speed>
    double angle(double distance, const Speed& speed) const {
        if (lengths.back() <= 1e-14) return 0.0;
        const double turns = std::floor(distance / lengths.back());
        const double local = distance - turns * lengths.back();
        const auto found = std::upper_bound(lengths.begin(), lengths.end(), local);
        const unsigned int index = std::min(divisions - 1,
            static_cast<unsigned int>(std::max<std::ptrdiff_t>(0, found - lengths.begin() - 1)));
        const double first = 2.0 * kPi * index / divisions, last = 2.0 * kPi * (index + 1) / divisions;
        double result = (first + last) * 0.5;
        for (unsigned int step = 0; step < 6; ++step) result = std::clamp(result -
            (lengths[index] + integral(first, result, speed) - local) / std::max(speed(result), 1e-14), first, last);
        return turns * 2.0 * kPi + result;
    }
};

void appendMetricWideCap(PartBuilder& bands, PartGeometry& geometry, double x,
    double halfWidth, const ShapeSettings& settings) {
    const auto scale = baseSpaceScale(settings);
    const double y = std::abs(scale.y), z = std::abs(scale.z);
    std::vector<MPoint> outer;
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const double angle = 2.0 * kPi * i / kCircleSegments;
        outer.emplace_back(0.5 * y * std::cos(angle), 0.5 * z * std::sin(angle), 0);
    }
    const auto inner = insetGenericWideFace(outer, halfWidth);
    const auto map = [&](const MPoint& point) { return MPoint(x, point.x / y, point.y / z); };
    if (!inner.empty()) {
        std::vector<MPoint> line;
        for (const auto& point : inner) line.push_back(map(point));
        line.push_back(line.front());
        appendGenericWideStroke(geometry, line);
    }
    for (std::size_t i = 0; i < outer.size(); ++i) {
        const std::vector<MPoint> triangle = {MPoint::origin, outer[i], outer[(i + 1) % outer.size()]};
        const auto pieces = inner.empty() ? PartPolygons{triangle} : outsideConvexPart(triangle, inner);
        for (const auto& piece : pieces) {
            std::vector<MPoint> points;
            for (const auto& point : piece) points.push_back(map(point));
            bands.polygon(points);
        }
    }
}

bool makeMetricWideCylinderBands(const ShapeSettings& settings, PartGeometry& geometry) {
    const auto scale = baseSpaceScale(settings);
    if (std::abs(scale.x * scale.y * scale.z) < 1e-24) return false;
    if (std::abs(std::abs(scale.x) - std::abs(scale.y)) < 1e-12 &&
        std::abs(std::abs(scale.x) - std::abs(scale.z)) < 1e-12) {
        auto source = settings;
        source.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
        source.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        source.wideWidth /= std::abs(scale.x);
        makeGenericWideCylinderBands(source, geometry);
        return true;
    }
    const double halfWidth = settings.wideWidth * 0.5;
    const auto speed = [&](double angle) { return 0.5 * std::hypot(scale.y * std::sin(angle), scale.z * std::cos(angle)); };
    const WideCurveMetric metric(speed);
    const auto reference = genericWideReferenceLines(settings);
    geometry.strokes.clear();
    geometry.strokeStyles.clear();
    for (std::size_t index = 0; index < reference.strokes.size(); ++index) {
        const auto& stroke = reference.strokes[index];
        if (stroke.length() < 2 || std::any_of(stroke.begin(), stroke.end(), [&](const auto& point) {
            return std::abs(point.x - stroke[0].x) > 1e-10;
        })) continue;
        geometry.strokes.push_back(stroke);
        geometry.strokeStyles.push_back(reference.strokeStyles[index]);
    }
    clearGenericWideBodyFill(geometry);
    PartBuilder bands(settings.fill);
    const double inset = halfWidth / std::abs(scale.x);
    const double low = std::min(0.0, -0.5 + inset), high = std::max(0.0, 0.5 - inset);
    for (unsigned int quarter = 0; quarter < 4; ++quarter) {
        const double start = quarter * kPi * 0.5, end = (quarter + 1) * kPi * 0.5;
        const double firstLength = metric.position(start, speed), lastLength = metric.position(end, speed);
        const bool hole = low < high - 1e-12 && lastLength - firstLength > 2.0 * halfWidth + 1e-12;
        const double left = hole ? metric.angle(firstLength + halfWidth, speed) : start;
        const double right = hole ? metric.angle(lastLength - halfWidth, speed) : end;
        if (hole) appendGenericWideMappedLine(geometry,
            {MPoint(low, left, 0), MPoint(high, left, 0), MPoint(high, right, 0), MPoint(low, right, 0), MPoint(low, left, 0)},
            [](const auto& point) { return genericWideCylinderPoint(point.x, point.y); });
        std::vector<double> angles;
        for (unsigned int i = 0; i <= kCircleSegments / 4; ++i) angles.push_back(start + (end - start) * i / (kCircleSegments / 4));
        if (hole) { angles.push_back(left); angles.push_back(right); }
        std::sort(angles.begin(), angles.end());
        for (std::size_t i = 1; i < angles.size(); ++i) {
            const double a = angles[i - 1], b = angles[i], middle = (a + b) * 0.5;
            if (!hole || middle < left || middle > right) bands.quad(genericWideCylinderPoint(-0.5, a),
                genericWideCylinderPoint(0.5, a), genericWideCylinderPoint(0.5, b), genericWideCylinderPoint(-0.5, b));
            else {
                bands.quad(genericWideCylinderPoint(-0.5, a), genericWideCylinderPoint(low, a),
                    genericWideCylinderPoint(low, b), genericWideCylinderPoint(-0.5, b));
                bands.quad(genericWideCylinderPoint(high, a), genericWideCylinderPoint(0.5, a),
                    genericWideCylinderPoint(0.5, b), genericWideCylinderPoint(high, b));
            }
        }
    }
    for (double x : {-0.5, 0.5}) appendMetricWideCap(bands, geometry, x, halfWidth, settings);
    mergeOptionGeometry(geometry, std::move(bands.geometry));
    return true;
}

bool makeMetricWideConeBands(const ShapeSettings& settings, PartGeometry& geometry) {
    const auto scale = baseSpaceScale(settings);
    if (std::abs(scale.x * scale.y * scale.z) < 1e-24) return false;
    if (std::abs(std::abs(scale.x) - std::abs(scale.y)) < 1e-12 &&
        std::abs(std::abs(scale.x) - std::abs(scale.z)) < 1e-12) {
        auto source = settings;
        source.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
        source.baseSpacePlus = MVector(0.5, 0.5, 0.5);
        source.wideWidth /= std::abs(scale.x);
        makeGenericWideConeBands(source, geometry);
        return true;
    }
    const auto generator = [&](double angle) { return MVector(-scale.x, 0.5 * scale.y * std::cos(angle), 0.5 * scale.z * std::sin(angle)); };
    const auto speed = [&](double angle) {
        const auto g = generator(angle);
        const MVector derivative(0, -0.5 * scale.y * std::sin(angle), 0.5 * scale.z * std::cos(angle));
        return (g ^ derivative).length() / (g * g);
    };
    const WideCurveMetric metric(speed);
    const auto reference = genericWideReferenceLines(settings);
    geometry.strokes = reference.strokes;
    geometry.strokeStyles = reference.strokeStyles;
    clearGenericWideBodyFill(geometry);
    PartBuilder bands(settings.fill);
    const double halfWidth = settings.wideWidth * 0.5;
    for (unsigned int quarter = 0; quarter < 4; ++quarter) {
        const double firstAngle = quarter * kPi * 0.5;
        const double firstPosition = metric.position(firstAngle, speed);
        std::vector<MPoint> boundary = {MPoint::origin};
        for (unsigned int i = 0; i <= kCircleSegments / 4; ++i) {
            const double angle = firstAngle + kPi * 0.5 * i / (kCircleSegments / 4);
            const double position = metric.position(angle, speed) - firstPosition;
            const double length = generator(angle).length();
            boundary.emplace_back(length * std::cos(position), length * std::sin(position), 0);
        }
        const auto inset = insetGenericWideFace(boundary, halfWidth);
        const auto map = [&](const MPoint& point) {
            const double length = std::hypot(point.x, point.y);
            if (length <= 1e-14) return MPoint(0.5, 0, 0);
            const double position = std::atan2(point.y, point.x) + firstPosition;
            const double angle = metric.angle(position, speed);
            const double fraction = length / generator(angle).length();
            return MPoint(0.5 - fraction, 0.5 * fraction * std::cos(angle), 0.5 * fraction * std::sin(angle));
        };
        if (!inset.empty()) {
            std::vector<MPoint> line;
            for (std::size_t i = 0; i < inset.size(); ++i) {
                const auto a = inset[i % inset.size()], b = inset[(i + 1) % inset.size()];
                const double angle = std::abs(std::atan2(a.y, a.x) - std::atan2(b.y, b.x));
                const unsigned int steps = std::max(1u, static_cast<unsigned int>(std::ceil(angle * 64.0)));
                for (unsigned int step = 0; step < steps; ++step) line.push_back(map(a + (b - a) * (static_cast<double>(step) / steps)));
            }
            if (!line.empty()) line.push_back(line.front());
            appendGenericWideStroke(geometry, line);
        }
        for (std::size_t i = 2; i < boundary.size(); ++i) {
            const std::vector<MPoint> triangle = {MPoint::origin, boundary[i - 1], boundary[i]};
            const auto pieces = inset.empty() ? PartPolygons{triangle} : outsideConvexPart(triangle, inset);
            for (const auto& piece : pieces) {
                std::vector<MPoint> points;
                for (const auto& point : piece) points.push_back(map(point));
                bands.polygon(points);
            }
        }
    }
    appendMetricWideCap(bands, geometry, -0.5, halfWidth, settings);
    mergeOptionGeometry(geometry, std::move(bands.geometry));
    return true;
}

std::pair<double, double> metricWideConeProjection(const MPoint& point, double generatorAngle,
    const ShapeSettings& settings) {
    const auto scale = baseSpaceScale(settings);
    const auto generator = [&](double angle) { return MVector(-scale.x,
        0.5 * scale.y * std::cos(angle), 0.5 * scale.z * std::sin(angle)); };
    const auto speed = [&](double angle) {
        const auto g = generator(angle);
        return (g ^ MVector(0, -0.5 * scale.y * std::sin(angle),
            0.5 * scale.z * std::cos(angle))).length() / std::max(g * g, 1e-24);
    };
    thread_local MVector previous;
    thread_local std::unique_ptr<WideCurveMetric> cached;
    if (!cached || !sameVector(previous, scale)) {
        cached = std::make_unique<WideCurveMetric>(speed);
        previous = scale;
    }
    if (cached->lengths.back() <= 1e-14) return {std::clamp(0.5 - point.x, 0.0, 1.0), 0.0};
    double angle = std::atan2(point.z, point.y);
    double difference = std::remainder(cached->position(angle, speed) -
        cached->position(generatorAngle, speed), cached->lengths.back());
    const double radius = std::max(0.0, 0.5 - point.x) * generator(angle).length();
    const double length = generator(generatorAngle).length();
    const double along = radius * std::cos(difference);
    const double side = radius * std::sin(difference);
    const double excess = along - std::clamp(along, 0.0, length);
    return {length <= 1e-12 ? 0.0 : std::clamp(along / length, 0.0, 1.0),
        side * side + excess * excess};
}
