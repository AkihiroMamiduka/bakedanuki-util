// 本体の帯と面上の補助輪郭を、PartやFinの寸法から独立して作る。
bool genericWidePlanarOutline(short outline) {
    return outline == 0 || outline == 6 || outline == 8 || outline == 79 || outline == 39;
}

bool genericWideOutline(short outline) {
    return genericWidePlanarOutline(outline) || outline == 19 || outline == 24 || outline == 25 ||
        outline == 33 || outline == 36 || outline == 41 || outline == 43 || outline == 46 ||
        outline == 50 || outline == 51;
}

void appendGenericWideStroke(PartGeometry& geometry, const std::vector<MPoint>& points,
    StrokeStyle style = StrokeStyle::Normal) {
    if (points.size() < 2) return;
    for (std::size_t index = 0; index < geometry.strokes.size(); ++index) {
        const auto& previous = geometry.strokes[index];
        if (geometry.strokeStyles[index] != style || previous.length() != points.size()) continue;
        bool forward = true, backward = true;
        for (std::size_t i = 0; i < points.size(); ++i) {
            forward = forward && (previous[static_cast<unsigned int>(i)] - points[i]).length() < 1e-9;
            backward = backward && (previous[static_cast<unsigned int>(i)] - points[points.size() - 1 - i]).length() < 1e-9;
        }
        if (forward || backward) return;
    }
    Stroke stroke;
    for (const auto& point : points) stroke.append(point);
    geometry.strokes.push_back(std::move(stroke));
    geometry.strokeStyles.push_back(style);
}

void appendGenericWideCircle(PartGeometry& geometry, const MPoint& center,
    const MVector& first, const MVector& second, double radius,
    StrokeStyle style = StrokeStyle::Normal) {
    if (radius <= 1e-12) return;
    std::vector<MPoint> points;
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const double angle = 2.0 * kPi * i / kCircleSegments;
        points.push_back(center + (first * std::cos(angle) + second * std::sin(angle)) * radius);
    }
    points.push_back(points.front());
    appendGenericWideStroke(geometry, points, style);
}

bool genericWidePlane(const PartGeometry& geometry, PartPlane& plane, MVector& normal) {
    for (const auto& stroke : geometry.strokes) {
        if (stroke.length() < 3) continue;
        for (unsigned int i = 1; i + 1 < stroke.length(); ++i) {
            const auto first = stroke[i] - stroke[0];
            const auto second = stroke[i + 1] - stroke[0];
            normal = first ^ second;
            if (normal.length() <= 1e-12) continue;
            normal.normalize();
            const auto side = first.normal();
            plane = {MPoint::origin, side, normal ^ side};
            return true;
        }
    }
    return false;
}

void appendGenericWideBand(WideEndArrowGeometry& band, const Stroke& source,
    const MVector& normal, double halfWidth) {
    std::vector<MPoint> points;
    for (const auto& point : source) {
        if (points.empty() || (point - points.back()).length() > 1e-10) points.push_back(point);
    }
    const bool closed = points.size() > 2 && (points.front() - points.back()).length() < 1e-10;
    if (closed) points.pop_back();
    if (points.size() < 2) return;
    const std::size_t count = points.size();
    std::vector<MVector> offsets;
    std::vector<MVector> previousOffsets, nextOffsets;
    std::vector<bool> bevels;
    for (std::size_t i = 0; i < count; ++i) {
        const auto before = (points[i] - points[(i + count - 1) % count]).normal();
        const auto after = (points[(i + 1) % count] - points[i]).normal();
        previousOffsets.push_back((normal ^ before) * halfWidth);
        nextOffsets.push_back((normal ^ after) * halfWidth);
        bool bevel = false;
        if (!closed && i == 0) offsets.push_back(nextOffsets.back());
        else if (!closed && i + 1 == count) offsets.push_back(previousOffsets.back());
        else {
            const auto first = normal ^ before, second = normal ^ after;
            const double denominator = 1.0 + first * second;
            const auto miter = denominator > 1e-10 ? (first + second) * (halfWidth / denominator)
                : second * halfWidth;
            bevel = denominator <= 1e-10 || miter.length() > halfWidth * 4.0;
            offsets.push_back(miter);
        }
        bevels.push_back(bevel);
    }
    for (std::size_t i = 0; i < (closed ? count : count - 1); ++i) {
        const std::size_t next = (i + 1) % count;
        const auto start = bevels[i] ? nextOffsets[i] : offsets[i];
        const auto end = bevels[next] ? previousOffsets[next] : offsets[next];
        const auto a = points[i] + start, b = points[next] + end;
        const auto c = points[next] - end, d = points[i] - start;
        band.triangles.push_back({a, b, c});
        band.triangles.push_back({a, c, d});
    }
    // 鋭角の接合は辺の帯幅を保ったまま角を切り、長い突起を作らない。
    for (std::size_t i = 0; i < count; ++i) if (bevels[i]) {
        band.triangles.push_back({points[i], points[i] + previousOffsets[i], points[i] + nextOffsets[i]});
        band.triangles.push_back({points[i], points[i] - previousOffsets[i], points[i] - nextOffsets[i]});
    }
}

void makeGenericWidePlanarBody(const ShapeSettings& settings, PartGeometry& geometry,
    std::vector<OptionClipVolume>* bodyVolumes) {
    const double halfWidth = settings.wideWidth * 0.5;
    if (halfWidth <= 1e-12) {
        geometry.fillParts.clear();
        return;
    }
    PartPlane plane;
    MVector normal;
    if (!genericWidePlane(geometry, plane, normal)) {
        PartGeometry reference;
        reference.strokes = makeStrokes(ShapeTransform(settings), reference.strokeStyles);
        if (!genericWidePlane(reference, plane, normal)) {
            geometry.fillParts.clear();
            return;
        }
    }
    WideEndArrowGeometry band;
    for (const auto& stroke : geometry.strokes) appendGenericWideBand(band, stroke, normal, halfWidth);
    if (band.triangles.empty()) {
        geometry.fillParts.clear();
        return;
    }
    PartBuilder result(true);
    appendPartTriangleUnion(result, band, plane);
    if (bodyVolumes) {
        for (const auto& part : result.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
            auto volume = optionPlanarVolume({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
            if (!volume.empty()) bodyVolumes->push_back(std::move(volume));
        }
    }
    if (!settings.fill) result.geometry.fillParts.clear();
    geometry = std::move(result.geometry);
}

struct GenericWideFace {
    MVector normal;
    double distance;
    std::vector<MPoint> vertices;
    StrokeStyle style;
    bool body = false;
};

std::vector<MPoint> genericWideConvexHull(std::vector<MPoint> points) {
    std::sort(points.begin(), points.end(), [](const auto& a, const auto& b) {
        return a.x < b.x || (a.x == b.x && a.y < b.y);
    });
    points.erase(std::unique(points.begin(), points.end(), [](const auto& a, const auto& b) {
        return (a - b).length() < 1e-10;
    }), points.end());
    if (points.size() < 3) return {};
    const auto turn = [](const MPoint& a, const MPoint& b, const MPoint& c) {
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    };
    std::vector<MPoint> hull;
    for (const auto& point : points) {
        while (hull.size() >= 2 && turn(hull[hull.size() - 2], hull.back(), point) <= 1e-12) hull.pop_back();
        hull.push_back(point);
    }
    const auto lower = hull.size();
    for (std::size_t i = points.size() - 1; i-- > 0;) {
        const auto& point = points[i];
        while (hull.size() > lower && turn(hull[hull.size() - 2], hull.back(), point) <= 1e-12) hull.pop_back();
        hull.push_back(point);
    }
    hull.pop_back();
    return hull;
}

std::vector<MPoint> insetGenericWideFace(const std::vector<MPoint>& boundary, double distance) {
    auto polygon = boundary;
    for (std::size_t i = 0; i < boundary.size() && !polygon.empty(); ++i) {
        const auto a = boundary[i];
        const auto edge = boundary[(i + 1) % boundary.size()] - a;
        const double length = edge.length();
        if (length <= 1e-12) continue;
        const auto value = [&](const MPoint& point) {
            return (edge.x * (point.y - a.y) - edge.y * (point.x - a.x)) / length - distance;
        };
        std::vector<MPoint> clipped;
        for (std::size_t j = 0; j < polygon.size(); ++j) {
            const auto p = polygon[j], q = polygon[(j + 1) % polygon.size()];
            const double first = value(p), last = value(q);
            if (first >= -1e-12) clipped.push_back(p);
            if ((first < 0 && last > 0) || (first > 0 && last < 0)) clipped.push_back(p + (q - p) * (first / (first - last)));
        }
        polygon = std::move(clipped);
    }
    return polygon.size() >= 3 && std::abs(partPolygonArea(polygon)) > 1e-12 ? polygon : std::vector<MPoint>{};
}

PartGeometry genericWideReferenceFaces(const ShapeSettings& settings) {
    auto source = settings;
    source.fill = true;
    source.wide = false;
    source.axisSwap = false;
    source.templateLine = source.templateFill = false;
    source.part = source.fin = source.guideLine = false;
    PartGeometry geometry;
    if (!makeAdjustedPartGeometry(source, geometry)) geometry.fillParts = makeFillParts(ShapeTransform(source));
    return geometry;
}

void appendGenericWideFaceInsets(const ShapeSettings& settings, PartGeometry& geometry) {
    const auto source = genericWideReferenceFaces(settings);
    std::vector<GenericWideFace> faces;
    std::vector<OptionClipVolume> markers;
    for (const auto& part : source.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        const auto a = part.triangles[i], b = part.triangles[i + 1], c = part.triangles[i + 2];
        auto normal = (b - a) ^ (c - a);
        if (normal.length() <= 1e-12) continue;
        normal.normalize();
        const double distance = (a - MPoint::origin) * normal;
        auto face = std::find_if(faces.begin(), faces.end(), [&](const auto& previous) {
            return (previous.normal - normal).length() < 1e-9 && std::abs(previous.distance - distance) < 1e-9;
        });
        if (face == faces.end()) {
            faces.push_back({normal, distance, {}, part.style, false});
            face = faces.end() - 1;
        }
        face->vertices.insert(face->vertices.end(), {a, b, c});
        if (!part.marker) { face->style = part.style; face->body = true; }
        else {
            auto volume = optionPlanarVolume({a, b, c});
            if (!volume.empty()) markers.push_back(std::move(volume));
        }
    }
    PartGeometry added;
    for (const auto& face : faces) {
        if (!face.body) continue;
        const auto origin = face.vertices.front();
        MVector first;
        for (const auto& vertex : face.vertices) {
            if ((vertex - origin).length() > 1e-10) { first = (vertex - origin).normal(); break; }
        }
        const auto second = face.normal ^ first;
        std::vector<MPoint> projected;
        for (const auto& vertex : face.vertices) {
            const auto delta = vertex - origin;
            projected.emplace_back(delta * first, delta * second, 0);
        }
        const auto hull = genericWideConvexHull(std::move(projected));
        if (hull.size() < 3) continue;
        const auto inset = insetGenericWideFace(hull, settings.wideWidth * 0.5);
        if (inset.empty()) continue;
        std::vector<MPoint> points;
        for (const auto& point : inset) points.push_back(origin + first * point.x + second * point.y);
        points.push_back(points.front());
        appendGenericWideStroke(added, points, face.style);
    }
    trimOptionStrokes(added, markers);
    mergeOptionGeometry(geometry, std::move(added));
}

void appendGenericWideSphere(const ShapeSettings& settings, PartGeometry& geometry) {
    constexpr double radius = 0.5;
    const double angle = settings.wideWidth * 0.5 / radius;
    if (angle >= kPi * 0.5 - 1e-12) return;
    const double offset = radius * std::sin(angle), circleRadius = radius * std::cos(angle);
    const auto originals = geometry.strokes;
    const auto styles = geometry.strokeStyles;
    for (std::size_t index = 0; index < originals.size(); ++index) {
        const auto& stroke = originals[index];
        if (stroke.length() < 4 || (stroke[0] - stroke[stroke.length() - 1]).length() > 1e-9) continue;
        const auto first = (stroke[0] - MPoint::origin).normal();
        auto normal = first ^ (stroke[stroke.length() / 4] - MPoint::origin);
        if (normal.length() <= 1e-12) continue;
        normal.normalize();
        const auto second = normal ^ first;
        for (double sign : {-1.0, 1.0}) appendGenericWideCircle(geometry,
            MPoint::origin + normal * (offset * sign), first, second, circleRadius, styles[index]);
    }
}

struct GenericWideGenerator {
    double angle;
    StrokeStyle style;
};

std::vector<GenericWideGenerator> genericWideGenerators(const PartGeometry& geometry, bool cone) {
    std::vector<GenericWideGenerator> generators;
    for (std::size_t index = 0; index < geometry.strokes.size(); ++index) {
        const auto& stroke = geometry.strokes[index];
        for (unsigned int i = 1; i < stroke.length(); ++i) {
            const auto a = stroke[i - 1], b = stroke[i];
            if (std::abs(a.x - b.x) <= 1e-10) continue;
            const auto radial = cone && a.y * a.y + a.z * a.z < 1e-12 ? b : a;
            if (radial.y * radial.y + radial.z * radial.z < 1e-12) continue;
            const double angle = std::atan2(radial.z, radial.y);
            if (std::any_of(generators.begin(), generators.end(), [&](const auto& previous) {
                return std::abs(std::sin((previous.angle - angle) * 0.5)) < 1e-9;
            })) continue;
            generators.push_back({angle, geometry.strokeStyles[index]});
        }
    }
    return generators;
}

void appendGenericWideCylinder(const ShapeSettings& settings, PartGeometry& geometry) {
    constexpr double radius = 0.5;
    const double distance = settings.wideWidth * 0.5;
    const auto generators = genericWideGenerators(geometry, false);
    for (double sign : {-1.0, 1.0}) {
        if (distance < 0.5 - 1e-12) appendGenericWideCircle(geometry,
            MPoint(sign * (0.5 - distance), 0, 0), nativeAxis(1), nativeAxis(2), radius);
        appendGenericWideCircle(geometry, MPoint(sign * 0.5, 0, 0), nativeAxis(1), nativeAxis(2), radius - distance);
    }
    if (distance >= kPi * radius - 1e-12) return;
    for (const auto& generator : generators) for (double sign : {-1.0, 1.0}) {
        const double angle = generator.angle + sign * distance / radius;
        const double y = radius * std::cos(angle), z = radius * std::sin(angle);
        appendGenericWideStroke(geometry, {MPoint(-0.5, y, z), MPoint(0.5, y, z)}, generator.style);
    }
}

void appendGenericWideCone(const ShapeSettings& settings, PartGeometry& geometry) {
    constexpr double radius = 0.5;
    const double distance = settings.wideWidth * 0.5;
    const double slant = std::sqrt(1.0 + radius * radius);
    const double ratio = radius / slant;
    const auto generators = genericWideGenerators(geometry, true);
    appendGenericWideCircle(geometry, MPoint(-0.5, 0, 0), nativeAxis(1), nativeAxis(2), radius - distance);
    if (distance < slant - 1e-12) appendGenericWideCircle(geometry,
        MPoint(-0.5 + distance / slant, 0, 0), nativeAxis(1), nativeAxis(2), radius * (1.0 - distance / slant));
    // 円錐の展開面で母線から一定距離の平行線を取り、最短側の周回だけを戻す。
    const double maximumAngle = std::min(kPi * 0.5, kPi * ratio);
    const double firstSlant = distance / std::sin(maximumAngle);
    if (firstSlant >= slant - 1e-12) return;
    for (const auto& generator : generators) for (double sign : {-1.0, 1.0}) {
        std::vector<MPoint> points;
        for (unsigned int i = 0; i <= kCircleSegments; ++i) {
            const double along = firstSlant + (slant - firstSlant) * i / kCircleSegments;
            const double angle = generator.angle + sign * std::asin(std::clamp(distance / along, 0.0, 1.0)) / ratio;
            const double position = along / slant;
            points.emplace_back(0.5 - position, radius * position * std::cos(angle), radius * position * std::sin(angle));
        }
        appendGenericWideStroke(geometry, points, generator.style);
    }
}

bool applyGenericWideBody(const ShapeSettings& settings, PartGeometry& geometry,
    std::vector<OptionClipVolume>* bodyVolumes = nullptr) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.wide || !genericWideOutline(outline)) return false;
    if (genericWidePlanarOutline(outline)) makeGenericWidePlanarBody(settings, geometry, bodyVolumes);
    else if (settings.wideWidth > 1e-12) {
        if (outline == 33 || outline == 46) appendGenericWideSphere(settings, geometry);
        else if (outline == 36) appendGenericWideCylinder(settings, geometry);
        else if (outline == 43) appendGenericWideCone(settings, geometry);
        else appendGenericWideFaceInsets(settings, geometry);
    }
    return true;
}
