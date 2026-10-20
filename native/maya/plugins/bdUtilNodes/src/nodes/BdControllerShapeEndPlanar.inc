// 平面の端形状は同じ輪郭から面を作り、接続線を手前の境界で止める。
std::vector<MPoint> planarEndProfile(unsigned int kind) {
    if (kind == 0) return {MPoint(-0.5, -0.5, 0), MPoint(0.5, -0.5, 0),
        MPoint(0.5, 0.5, 0), MPoint(-0.5, 0.5, 0)};
    if (kind == 1) return {MPoint(0.5, 0, 0), MPoint(0, 0.5, 0),
        MPoint(-0.5, 0, 0), MPoint(0, -0.5, 0)};
    if (kind == 3) return {MPoint(0.5, 0, 0), MPoint(-0.5, 0.5, 0), MPoint(-0.5, -0.5, 0)};
    std::vector<MPoint> circle;
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const double angle = 2.0 * kPi * i / kCircleSegments;
        circle.emplace_back(0.5 * std::cos(angle), 0.5 * std::sin(angle), 0);
    }
    return circle;
}

double planarEndAlong(double coordinate, unsigned int kind, const ShapeSettings& settings) {
    const double center = kind == 3 ? 0.45 : 0.5;
    return 0.5 + (center + 0.1 * coordinate - 0.5) * partLength(settings) + settings.partOffset;
}

void appendPlanarEndParts(PartBuilder& builder, short outline, const ShapeSettings& settings) {
    constexpr std::array<short, 6> bases = {1, 2, 3, 52, 53, 4};
    const auto axes = straightLineAxes(bases[(outline - 80) / 4]);
    const unsigned int kind = (outline - 80) % 4;
    const auto profile = planarEndProfile(kind);
    const unsigned int planeSide = axes.front();
    const unsigned int planeAlong = axes.size() == 2 ? axes.back() : (planeSide == 0 ? 1 : 0);
    const PartPlane plane{MPoint::origin, nativeAxis(planeSide), nativeAxis(planeAlong)};
    const MVector normal = plane.side ^ plane.along;
    const double lineEnd = std::max(0.0, std::min(
        planarEndAlong(-0.5, kind, settings), planarEndAlong(0.5, kind, settings)));
    PartBuilder heads(builder.filled);
    std::vector<MBoundingBox> boxes;
    bool overlap = false;
    for (auto axis : axes) {
        const unsigned int other = axes.size() == 2
            ? (axis == axes.front() ? axes.back() : axes.front()) : planeAlong;
        for (double sign : {-1.0, 1.0}) {
            const MVector direction = nativeAxis(axis) * sign;
            const bool decorated = hasPartAtEnd(settings.shape, sign < 0.0, static_cast<short>(axis));
            const double stop = decorated ? lineEnd : 0.5;
            if (stop > 0.0) builder.stroke({MPoint::origin, MPoint::origin + direction * stop});
            if (!decorated) continue;
            std::vector<MPoint> points;
            MBoundingBox box;
            for (const auto& p : profile) {
                const MPoint point = MPoint::origin + direction * planarEndAlong(p.x, kind, settings)
                    + nativeAxis(other) * (0.1 * p.y * partWidth(settings));
                points.push_back(point);
                box.expand(point);
            }
            for (const auto& previous : boxes) overlap = overlap || box.intersects(previous);
            boxes.push_back(box);
            if (((points[1] - points[0]) ^ (points[2] - points[0])) * normal < 0.0) {
                std::reverse(points.begin(), points.end());
            }
            auto closed = points;
            closed.push_back(points.front());
            heads.stroke(closed);
            for (std::size_t i = 1; i + 1 < points.size(); ++i) heads.triangle(points[0], points[i], points[i + 1]);
        }
    }
    for (auto& stroke : heads.geometry.strokes) {
        builder.geometry.strokes.push_back(std::move(stroke));
        builder.geometry.strokeStyles.push_back(StrokeStyle::Normal);
    }
    if (overlap && builder.filled) {
        WideEndArrowGeometry generated;
        for (const auto& part : heads.geometry.fillParts) {
            for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
                generated.triangles.push_back({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
            }
        }
        PartBuilder merged(true);
        appendPartTriangleUnion(merged, generated, plane);
        builder.geometry.fillParts = std::move(merged.geometry.fillParts);
    } else {
        builder.geometry.fillParts = std::move(heads.geometry.fillParts);
    }
}

bool makePlanarEndGeometry(const ShapeSettings& settings, PartGeometry& geometry) {
    const short outline = outlinePresetIndex(settings.shape);
    if (outline < 79 || outline > 103) return false;
    PartBuilder builder(isFilledPreset(settings.shape));
    if (outline == 79) {
        std::vector<MPoint> points;
        const PartPlane plane{MPoint::origin, nativeAxis(1), nativeAxis(2)};
        for (const auto& p : planarEndProfile(1)) points.push_back(plane.point(p));
        builder.polygon(points);
        points.push_back(points.front());
        builder.stroke(points);
    } else {
        appendPlanarEndParts(builder, outline, settings);
    }
    geometry = std::move(builder.geometry);
    return true;
}
