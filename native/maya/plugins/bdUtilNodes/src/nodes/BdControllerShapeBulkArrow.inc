// 本体の全体を残し、突出した錐との境界を外殻だけで組み立てる。
PartGeometry bulkArrowCanonicalBodyGeometry(const ShapeSettings& settings) {
    PartBuilder builder(true);
    builder.singleSided = true;
    const double rearRadius = bulkArrowRearRadius(settings), frontRadius = bulkArrowFrontRadius(settings);
    const double front = bulkArrowFront(settings);
    if (isPlanarArrowBody(settings)) {
        std::vector<MPoint> profile;
        for (const auto& point : bulkArrowProfilePoints(settings)) profile.emplace_back(point.x, 0, point.y);
        builder.singleSided = false;
        builder.stroke(profile);
        builder.polygon(profile);
        return std::move(builder.geometry);
    }
    const auto triangle = [&](MPoint a, MPoint b, MPoint c) {
        const auto center = a + ((b - a) + (c - a)) / 3.0;
        if (((b - a) ^ (c - a)) * (center - bulkArrowBodyCenter(settings)) < 0.0) std::swap(b, c);
        builder.triangle(a, b, c);
    };
    if (outlinePresetIndex(settings.shape) == kCubeArrowOutline) {
        std::array<MPoint, 4> rear = {MPoint(0, -0.5, -0.5), MPoint(0, 0.5, -0.5),
            MPoint(0, 0.5, 0.5), MPoint(0, -0.5, 0.5)};
        for (auto& point : rear) point.x = -rearRadius;
        auto face = rear;
        for (auto& point : face) point.x = frontRadius;
        const MPoint tip(front, 0, 0);
        const auto quad = [&](const MPoint& a, const MPoint& b, const MPoint& c, const MPoint& d) {
            triangle(a, b, c); triangle(a, c, d);
        };
        quad(rear[0], rear[1], rear[2], rear[3]);
        if (!bulkArrowHasHead(settings)) quad(face[0], face[1], face[2], face[3]);
        for (unsigned int i = 0; i < 4; ++i) {
            const unsigned int next = (i + 1) % 4;
            builder.stroke({rear[i], rear[next]});
            builder.stroke({face[i], face[next]});
            builder.stroke({rear[i], face[i]});
            quad(rear[i], rear[next], face[next], face[i]);
            if (bulkArrowHasHead(settings)) {
                builder.stroke({face[i], tip});
                triangle(face[i], face[next], tip);
            }
        }
        return std::move(builder.geometry);
    }
    const auto profile = bulkArrowProfilePoints(settings);
    builder.stroke(profile);
    std::vector<MPoint> other;
    for (const auto& point : profile) other.emplace_back(point.x, 0, point.y);
    builder.stroke(other);
    const auto circle = [&](double x, double r) {
        std::vector<MPoint> points;
        for (unsigned int i = 0; i <= kCircleSegments; ++i) {
            const double angle = 2.0 * kPi * i / kCircleSegments;
            points.emplace_back(x, r * std::cos(angle), r * std::sin(angle));
        }
        builder.stroke(points);
    };
    circle(0, 0.5);
    const double first = bulkArrowJoinAngle(settings);
    std::vector<std::array<double, 2>> rings = {{-rearRadius, 0}};
    for (unsigned int i = 15; i > 0; --i) {
        const double angle = kPi * i / 16.0;
        if (angle > first) {
            const double cosine = std::cos(angle);
            rings.push_back({(cosine < 0.0 ? rearRadius : frontRadius) * cosine, 0.5 * std::sin(angle)});
        }
    }
    rings.push_back({frontRadius * std::cos(first), 0.5 * std::sin(first)});
    if (bulkArrowHasHead(settings)) rings.push_back({front, 0});
    const auto at = [&](std::size_t ring, unsigned int longitude) {
        const double angle = 2.0 * kPi * longitude / 32.0;
        return MPoint(rings[ring][0], rings[ring][1] * std::cos(angle), rings[ring][1] * std::sin(angle));
    };
    for (std::size_t ring = 1; ring < rings.size(); ++ring) for (unsigned int longitude = 0; longitude < 32; ++longitude) {
        const auto a = at(ring - 1, longitude), b = at(ring, longitude);
        const auto c = at(ring, longitude + 1), d = at(ring - 1, longitude + 1);
        triangle(a, b, c); triangle(a, c, d);
    }
    return std::move(builder.geometry);
}

PartGeometry diamondArrowCanonicalBodyGeometry() {
    PartBuilder builder(true);
    const std::vector<MPoint> points = {MPoint(0.5, 0, 0), MPoint(0, 0, -0.5),
        MPoint(-0.5, 0, 0), MPoint(0, 0, 0.5)};
    auto outline = points;
    outline.push_back(outline.front());
    builder.stroke(outline);
    builder.polygon(points);
    return std::move(builder.geometry);
}

PartGeometry notchedArrowCanonicalBodyGeometry(const ShapeSettings& settings) {
    PartBuilder builder(true);
    for (unsigned int plane = 0; plane < (isSpatialArrowBody(settings) ? 2u : 1u); ++plane) {
        std::vector<MPoint> profile;
        for (const auto& point : notchedArrowProfilePoints()) {
            profile.push_back(plane == 0 ? MPoint(point.x, 0, point.y) : point);
        }
        builder.stroke(profile);
        builder.polygon(profile);
    }
    return std::move(builder.geometry);
}

PartGeometry diamondAxialCanonicalBodyGeometry() {
    PartBuilder builder(true);
    builder.singleSided = true;
    const std::array<MPoint, 4> base = {MPoint(-0.5, 0.5, 0), MPoint(-0.5, 0, 0.5),
        MPoint(-0.5, -0.5, 0), MPoint(-0.5, 0, -0.5)};
    const MPoint tip(0.5, 0, 0), inside(-0.25, 0, 0);
    const auto triangle = [&](MPoint a, MPoint b, MPoint c) {
        if (((b - a) ^ (c - a)) * (a - inside) < 0.0) std::swap(b, c);
        builder.triangle(a, b, c);
    };
    for (unsigned int i = 0; i < 4; ++i) {
        const auto next = (i + 1) % 4;
        builder.stroke({base[i], base[next]});
        builder.stroke({base[i], tip});
        triangle(base[i], base[next], tip);
    }
    triangle(base[0], base[1], base[2]);
    triangle(base[0], base[2], base[3]);
    return std::move(builder.geometry);
}
