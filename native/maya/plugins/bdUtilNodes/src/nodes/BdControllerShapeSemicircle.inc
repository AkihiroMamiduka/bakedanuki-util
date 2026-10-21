// 円弧端点と接線を決めてから部品を配置し、角度・Offsetで頭部を変形させない。
const PartPlane kSemicirclePlane{MPoint::origin, MVector(0, 0, 1), MVector(0, 1, 0)};
// この平面では角度の降順が主軸の正回転で、角度の小さい端がEndになる。

std::vector<double> semicircleSampleAngles(double start, double end) {
    std::vector<double> angles = {start};
    const double step = 2.0 * kPi / kCircleSegments;
    for (int index = static_cast<int>(std::floor(start / step)) + 1; index * step < end - 1.0e-12; ++index) {
        angles.push_back(index * step);
    }
    if (end - start > 1.0e-12) angles.push_back(end);
    return angles;
}

MVector semicircleRadial(double angle) {
    const double x = std::cos(angle);
    const double y = std::sin(angle);
    return MVector(std::abs(x) < 1.0e-14 ? 0.0 : x, std::abs(y) < 1.0e-14 ? 0.0 : y, 0.0);
}

MVector semicircleOutward(double angle, bool end) {
    const auto radial = semicircleRadial(angle);
    return end ? MVector(radial.y, -radial.x, 0) : MVector(-radial.y, radial.x, 0);
}

std::vector<MPoint> semicircleArc(const ShapeSettings& settings) {
    std::vector<MPoint> points;
    for (double angle : semicircleSampleAngles(-settings.partOffsetAngle, kPi + settings.partOffsetAngle)) {
        points.push_back(MPoint::origin + semicircleRadial(angle) * 0.5);
    }
    return points;
}

void appendSemicircleArc(PartBuilder& builder, const std::vector<MPoint>& arc) {
    auto points = kSemicirclePlane.points(arc);
    if (points.size() == 1) points.push_back(points.front());
    builder.stroke(points);
}

WideEndArrowGeometry semicircleWidePartGeometry(const ShapeSettings& settings) {
    WideEndArrowGeometry geometry;
    const double endAngle = -settings.partOffsetAngle;
    const double startAngle = kPi + settings.partOffsetAngle;
    const bool startArrow = hasPartAtEnd(settings.shape, true);
    const bool endArrow = hasPartAtEnd(settings.shape, false);
    const double halfSweep = std::max(0.0, (startAngle - endAngle) * 0.5);
    const double depth = 0.1 * std::cos(kPi / 6.0) * partLength(settings);
    const double shaftWidth = 0.025 * std::abs(partWidth(settings));
    const double headWidth = 2.0 * shaftWidth;
    const double outerRadius = 0.5 + shaftWidth;
    const double innerRadius = std::max(0.0, 0.5 - shaftWidth);
    // 長い頭部でも底辺と帯が離れないよう、円弧を切る深さに上限を設ける。
    const double maxJoinDepth = std::sqrt(std::max(0.0, outerRadius * outerRadius - 0.25));
    const double behind = std::min(std::max(0.0, depth - settings.partOffset), maxJoinDepth);
    const auto trim = [&](double radius) {
        return radius > 0.0 ? std::min(halfSweep, std::asin(std::clamp(behind / radius, 0.0, 1.0))) : halfSweep;
    };
    const double outerTrim = trim(outerRadius);
    const double innerTrim = trim(innerRadius);
    std::vector<double> angles = semicircleSampleAngles(endAngle, startAngle);
    if (endArrow) for (double angle : {endAngle + outerTrim, endAngle + innerTrim}) angles.push_back(angle);
    if (startArrow) for (double angle : {startAngle - outerTrim, startAngle - innerTrim}) angles.push_back(angle);
    std::sort(angles.begin(), angles.end());
    angles.erase(std::unique(angles.begin(), angles.end(), [](double a, double b) {
        return std::abs(a - b) < 1.0e-12;
    }), angles.end());
    std::vector<MPoint> outer;
    std::vector<MPoint> inner;
    const auto trimmedAngle = [&](double angle, double trimAngle) {
        const double half = halfSweep - trimAngle;
        return std::clamp(angle, endArrow ? kPi / 2.0 - half : endAngle,
            startArrow ? kPi / 2.0 + half : startAngle);
    };
    for (double angle : angles) {
        outer.push_back(MPoint::origin + semicircleRadial(trimmedAngle(angle, outerTrim)) * outerRadius);
        inner.push_back(MPoint::origin + semicircleRadial(trimmedAngle(angle, innerTrim)) * innerRadius);
    }
    const auto triangle = [&](MPoint a, MPoint b, MPoint c) {
        const double area = ((b - a) ^ (c - a)).z;
        if (std::abs(area) < 1.0e-12) return;
        if (area < 0.0) std::swap(b, c);
        geometry.triangles.push_back({kSemicirclePlane.point(a), kSemicirclePlane.point(b), kSemicirclePlane.point(c)});
    };
    const auto quad = [&](MPoint a, MPoint b, MPoint c, MPoint d) {
        triangle(a, b, c);
        triangle(a, c, d);
    };
    for (std::size_t i = 0; i + 1 < outer.size(); ++i) quad(outer[i], outer[i + 1], inner[i + 1], inner[i]);
    std::array<std::array<MPoint, 5>, 2> heads;
    for (unsigned int i = 0; i < 2; ++i) {
        const bool end = i == 0;
        if (!hasPartAtEnd(settings.shape, !end)) continue;
        const double angle = end ? endAngle : startAngle;
        const MVector radial = semicircleRadial(angle);
        const MVector direction = semicircleOutward(angle, end);
        const MPoint tip = MPoint::origin + radial * 0.5 + direction * settings.partOffset;
        const MPoint base = tip - direction * depth;
        heads[i] = {tip, base + radial * headWidth, base + radial * shaftWidth,
            base - radial * shaftWidth, base - radial * headWidth};
        const MPoint arcOuter = i == 0 ? outer.front() : outer.back();
        const MPoint arcInner = i == 0 ? inner.front() : inner.back();
        quad(arcOuter, arcInner, heads[i][3], heads[i][2]);
        // 頭部の底辺を同一直線に保ち、帯の接続点と共用する。
        for (unsigned int edge = 1; edge < 4; ++edge) triangle(tip, heads[i][edge], heads[i][edge + 1]);
    }
    std::vector<MPoint> boundary;
    if (endArrow) boundary = {heads[0][0], heads[0][1], heads[0][2]};
    boundary.insert(boundary.end(), outer.begin(), outer.end());
    if (startArrow) boundary.insert(boundary.end(), {heads[1][2], heads[1][1], heads[1][0], heads[1][4], heads[1][3]});
    boundary.insert(boundary.end(), inner.rbegin(), inner.rend());
    if (endArrow) boundary.insert(boundary.end(), {heads[0][3], heads[0][4], heads[0][0]});
    else boundary.push_back(outer.front());
    geometry.outline = kSemicirclePlane.points(boundary);
    return geometry;
}

void appendSemicircleParts(PartBuilder& builder, short outline, const ShapeSettings& settings) {
    const auto arc = semicircleArc(settings);
    if (outline == 68) {
        appendPartTriangleUnion(builder, semicircleWidePartGeometry(settings), kSemicirclePlane);
        return;
    }
    appendSemicircleArc(builder, arc);
    if (outline == 61) {
        const double depth = 0.1 * std::cos(kPi / 6.0) * partLength(settings);
        const double halfWidth = 0.05 * partWidth(settings);
        WideEndArrowGeometry heads;
        for (unsigned int i = 0; i < 2; ++i) {
            const bool end = i == 0;
            if (!hasPartAtEnd(settings.shape, !end)) continue;
            const double angle = end ? -settings.partOffsetAngle : kPi + settings.partOffsetAngle;
            const MVector radial = semicircleRadial(angle);
            const MVector direction = semicircleOutward(angle, end);
            const MPoint endpoint = MPoint::origin + radial * 0.5;
            const MPoint tip = endpoint + direction * settings.partOffset;
            const MPoint base = tip - direction * depth;
            const auto triangle = kSemicirclePlane.points({base + radial * halfWidth, tip, base - radial * halfWidth});
            builder.stroke(triangle);
            if (settings.partOffset != 0.0) builder.stroke(kSemicirclePlane.points({endpoint, tip}));
            heads.triangles.push_back({triangle[0], triangle[1], triangle[2]});
        }
        PartBuilder fills(builder.filled);
        appendPartTriangleUnion(fills, heads, kSemicirclePlane);
        builder.geometry.fillParts = std::move(fills.geometry.fillParts);
        return;
    }
    const auto face = kSemicirclePlane.points(arc);
    for (std::size_t i = 0; i + 1 < face.size(); ++i) {
        builder.triangle(MPoint::origin, face[i + 1], face[i]);
    }
    if (outline == 31 || outline == 32) {
        std::vector<MPoint> section;
        for (const auto& p : arc) section.emplace_back(p.x, p.y - 0.5, 0);
        if (arc.size() > 1 && settings.partOffsetAngle < kPi / 2.0) section.emplace_back(0, -0.5, 0);
        appendAttachedPart(builder, settings,
            {MPoint(0, 0.5, 0), MVector(0, 0, 1), MVector(0, 1, 0)},
            0.125, 0.075, -0.004903810568, outline == 32 ? 0.0625 : 0.0, section, true);
    }
}
