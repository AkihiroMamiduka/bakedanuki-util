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

#include "BdControllerShapeWidePlanar.inc"

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
    if (makeSimpleWideGearBody(settings, geometry, plane, normal, halfWidth, bodyVolumes)) return;
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

#include "BdControllerShapeWideSolid.inc"

bool applyGenericWideBody(const ShapeSettings& settings, PartGeometry& geometry,
    std::vector<OptionClipVolume>* bodyVolumes = nullptr) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!settings.wide || !genericWideOutline(outline)) return false;
    if (genericWidePlanarOutline(outline)) makeGenericWidePlanarBody(settings, geometry, bodyVolumes);
    else if (settings.wideWidth <= 1e-12) {
        clearGenericWideBodyFill(geometry);
        if (outline == 36) {
            const auto reference = genericWideReferenceLines(settings);
            geometry.strokes = reference.strokes;
            geometry.strokeStyles = reference.strokeStyles;
        }
    } else if (outline == 33 || outline == 46) makeGenericWideSphereBands(settings, geometry);
    else if (outline == 36) makeGenericWideCylinderBands(settings, geometry);
    else if (outline == 43) makeGenericWideConeBands(settings, geometry);
    else makeGenericWideSolidFaces(settings, geometry);
    return true;
}
