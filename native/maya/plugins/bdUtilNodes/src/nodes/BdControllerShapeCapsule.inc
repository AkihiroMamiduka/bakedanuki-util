// 原型は長さ1の円筒と半径0.5の半球を持ち、主軸写像で指定した長さへ組み立てる。
PartGeometry capsuleCanonicalBodyGeometry(const ShapeSettings& settings) {
    PartBuilder builder(true);
    builder.singleSided = true;
    const auto profile = capsuleProfilePoints();
    builder.stroke(profile);
    std::vector<MPoint> other;
    for (const auto& point : profile) other.emplace_back(point.x, 0, point.y);
    builder.stroke(other);
    std::vector<MPoint> previousCircle;
    for (double center : {-0.5, 0.5}) {
        std::vector<MPoint> circle;
        bool sameCircle = !previousCircle.empty();
        for (unsigned int i = 0; i <= kCircleSegments; ++i) {
            const double angle = 2.0 * kPi * i / kCircleSegments;
            circle.emplace_back(center, 0.5 * std::cos(angle), 0.5 * std::sin(angle));
            if (sameCircle && (cageBodyPoint(circle.back(), settings) -
                cageBodyPoint(previousCircle[i], settings)).length() > 1e-10) sameCircle = false;
        }
        // 中心間が0のときも、接合円を半透明の線で二重描画しない。
        if (!sameCircle) builder.stroke(circle);
        previousCircle = std::move(circle);
    }
    std::vector<std::array<double, 2>> rings;
    for (unsigned int i = 0; i <= 8; ++i) {
        const double angle = -kPi * 0.5 + kPi * i / 16.0;
        rings.push_back({-0.5 + 0.5 * std::sin(angle), 0.5 * std::cos(angle)});
    }
    rings.push_back({0, 0.5});
    rings.push_back({0.5, 0.5});
    for (unsigned int i = 1; i <= 8; ++i) {
        const double angle = kPi * i / 16.0;
        rings.push_back({0.5 + 0.5 * std::sin(angle), 0.5 * std::cos(angle)});
    }
    const auto pointAt = [&](std::size_t ring, unsigned int longitude) {
        const double angle = 2.0 * kPi * longitude / 32.0;
        return MPoint(rings[ring][0], rings[ring][1] * std::cos(angle), rings[ring][1] * std::sin(angle));
    };
    const auto triangle = [&](MPoint a, MPoint b, MPoint c) {
        const auto center = a + ((b - a) + (c - a)) / 3.0;
        const auto outward = center - MPoint(std::clamp(center.x, -0.5, 0.5), 0, 0);
        if (((b - a) ^ (c - a)) * outward < 0.0) std::swap(b, c);
        builder.triangle(a, b, c);
    };
    for (std::size_t ring = 1; ring < rings.size(); ++ring) {
        for (unsigned int longitude = 0; longitude < 32; ++longitude) {
            const auto a = pointAt(ring - 1, longitude), b = pointAt(ring, longitude);
            const auto c = pointAt(ring, longitude + 1), d = pointAt(ring - 1, longitude + 1);
            triangle(a, b, c);
            triangle(a, c, d);
        }
    }
    return std::move(builder.geometry);
}

PartGeometry makeCapsuleFinGeometry(const ShapeSettings& settings) {
    PartBuilder builder(settings.fill);
    auto physical = settings;
    physical.baseSpaceMinus = MVector(-0.5, -0.5, -0.5);
    physical.baseSpacePlus = MVector(0.5, 0.5, 0.5);
    std::vector<MPoint> section;
    const unsigned int alongAxis = settings.axisSwap ? 1 : 0;
    const unsigned int heightAxis = settings.axisSwap ? 0 : 1;
    const auto center = bodyBaseSpacePoint(MPoint::origin, settings);
    const double alongSign = settings.baseSpacePlus[alongAxis] >= settings.baseSpaceMinus[alongAxis] ? 1.0 : -1.0;
    const double heightSign = settings.baseSpacePlus[heightAxis] >= settings.baseSpaceMinus[heightAxis] ? 1.0 : -1.0;
    for (const auto& point : capsuleProfilePoints()) {
        const auto mapped = bodyBaseSpacePoint(point, settings) - center;
        section.emplace_back(mapped[alongAxis] * alongSign, mapped[heightAxis] * heightSign, 0);
    }
    double low = section.front().x, high = low;
    for (const auto& point : section) { low = std::min(low, point.x); high = std::max(high, point.x); }
    appendFinPart(builder, physical, section, {MPoint(low, 0, 0), MPoint(high, 0, 0)},
        settings.finType == 1 ? std::vector<double>{0.5, 0} : std::vector<double>{0.5, 0.5}, 0,
        settings.finTemplate ? StrokeStyle::Template : StrokeStyle::Normal);
    const auto map = [&](const MPoint& point) {
        auto result = center;
        result[alongAxis] += point.x * alongSign;
        result[heightAxis] += point.y * heightSign;
        return result;
    };
    for (auto& stroke : builder.geometry.strokes) for (auto& point : stroke) point = map(point);
    for (auto& part : builder.geometry.fillParts) for (auto& point : part.triangles) point = map(point);
    return std::move(builder.geometry);
}
