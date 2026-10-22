// 変形後の端形状を凸半空間で表し、Finの線と面を同じ境界で止める。
struct FinClipPlane {
    MVector normal;
    double distance;
    double value(const MPoint& point) const { return (point - MPoint::origin) * normal - distance; }
};

using FinClipVolume = std::vector<FinClipPlane>;

void addFinClipPlane(FinClipVolume& planes, MVector normal, const MPoint& point, const MPoint& inside) {
    if (normal.length() < 1e-14) return;
    normal.normalize();
    if ((inside - point) * normal > 0) normal = -normal;
    const double distance = (point - MPoint::origin) * normal;
    for (const auto& plane : planes) {
        if ((plane.normal - normal).length() < 1e-9 && std::abs(plane.distance - distance) < 1e-9) return;
    }
    planes.push_back({normal, distance});
}

std::vector<FinClipVolume> finEndClipVolumes(const ShapeSettings& settings, const MBoundingBox& finBounds) {
    std::vector<FinClipVolume> volumes;
    const short outline = outlinePresetIndex(settings.shape);
    if (outline >= 80 && outline <= 103) {
        constexpr std::array<short, 6> bases = {1, 2, 3, 52, 53, 4};
        const auto axes = straightLineAxes(bases[(outline - 80) / 4]);
        const unsigned int kind = (outline - 80) % 4;
        const auto profile = planarEndProfile(kind);
        const unsigned int planeAlong = axes.size() == 2 ? axes.back() : (axes.front() == 0 ? 1 : 0);
        for (auto axis : axes) for (double sign : {-1.0, 1.0}) {
            if (!hasPartAtEnd(settings.shape, sign < 0, static_cast<short>(axis))) continue;
            const auto direction = nativeAxis(axis) * sign;
            const unsigned int other = axes.size() == 2 ? (axis == axes.front() ? axes.back() : axes.front()) : planeAlong;
            std::vector<MPoint> points;
            MBoundingBox bounds;
            MPoint center;
            for (const auto& p : profile) {
                const auto point = MPoint::origin + direction * planarEndAlong(p.x, kind, settings)
                    + nativeAxis(other) * (0.1 * p.y * partWidth(settings));
                points.push_back(point);
                bounds.expand(point);
                center += (point - MPoint::origin) / static_cast<double>(profile.size());
            }
            if (!bounds.intersects(finBounds)) continue;
            MVector normal = (points[1] - points[0]) ^ (points[2] - points[0]);
            if (normal.length() < 1e-14) continue;
            normal.normalize();
            FinClipVolume volume;
            for (std::size_t i = 0; i < points.size(); ++i) {
                addFinClipPlane(volume, (points[(i + 1) % points.size()] - points[i]) ^ normal, points[i], center);
            }
            // 平面の端形状は、その平面にある線・面だけを切る。
            volume.push_back({normal, (points[0] - MPoint::origin) * normal});
            volume.push_back({-normal, -(points[0] - MPoint::origin) * normal});
            volumes.push_back(std::move(volume));
        }
    } else if (hasCrossLineEndSolids(outline) && partLength(settings) != 0 && partWidth(settings) != 0) {
        ShapeSettings component;
        component.shape = crossLineEndSolidPreset(outline);
        component.fill = true;
        const auto parts = makeFillParts(ShapeTransform(component));
        for (unsigned int axis = 0; axis < 3; ++axis) for (double sign : {-1.0, 1.0}) {
            MBoundingBox bounds;
            std::vector<std::array<MPoint, 3>> faces;
            for (const auto& part : parts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
                std::array<MPoint, 3> face;
                for (unsigned int j = 0; j < 3; ++j) {
                    face[j] = crossLineEndSolidPoint(part.triangles[i + j], outline, axis, sign, settings);
                    bounds.expand(face[j]);
                }
                faces.push_back(face);
            }
            if (faces.empty() || !bounds.intersects(finBounds)) continue;
            const auto inside = crossLineEndSolidPoint(MPoint::origin, outline, axis, sign, settings);
            FinClipVolume volume;
            for (const auto& face : faces) addFinClipPlane(volume, (face[1] - face[0]) ^ (face[2] - face[0]), face[0], inside);
            if (volume.size() >= 4) volumes.push_back(std::move(volume));
        }
    }
    return volumes;
}

PartPolygons outsideFinVolume(std::vector<MPoint> polygon, const FinClipVolume& volume) {
    PartPolygons result;
    for (const auto& plane : volume) {
        if (polygon.empty()) break;
        std::vector<MPoint> inside;
        std::vector<MPoint> outside;
        for (std::size_t i = 0; i < polygon.size(); ++i) {
            const auto a = polygon[i];
            const auto b = polygon[(i + 1) % polygon.size()];
            double da = plane.value(a);
            double db = plane.value(b);
            if (std::abs(da) < 1e-10) da = 0;
            if (std::abs(db) < 1e-10) db = 0;
            if (da <= 0) inside.push_back(a);
            if (da >= 0) outside.push_back(a);
            if ((da < 0 && db > 0) || (da > 0 && db < 0)) {
                const auto p = a + (b - a) * (da / (da - db));
                inside.push_back(p);
                outside.push_back(p);
            }
        }
        // 境界だけの面を二重に残さず、体積の外側にある面だけを採る。
        bool positive = false;
        for (const auto& p : polygon) positive = positive || plane.value(p) > 1e-10;
        if (positive && outside.size() >= 3) result.push_back(std::move(outside));
        polygon = std::move(inside);
    }
    return result;
}

void trimFinEndParts(const ShapeSettings& settings, PartBuilder& fin) {
    const short outline = outlinePresetIndex(settings.shape);
    if (!hasCrossLineEndSolids(outline) && (outline < 80 || outline > 103)) return;
    const auto bounds = boundsForGeometry(fin.geometry.strokes, fin.geometry.fillParts);
    const auto volumes = finEndClipVolumes(settings, bounds);
    if (volumes.empty()) return;
    PartBuilder trimmed(fin.filled);
    for (const auto& stroke : fin.geometry.strokes) for (unsigned int i = 1; i < stroke.length(); ++i) {
        std::vector<std::array<MPoint, 2>> segments = {{{stroke[i - 1], stroke[i]}}};
        for (const auto& volume : volumes) {
            std::vector<std::array<MPoint, 2>> next;
            for (const auto& segment : segments) {
                double enter = 0;
                double leave = 1;
                bool intersects = true;
                for (const auto& plane : volume) {
                    const double a = plane.value(segment[0]);
                    const double b = plane.value(segment[1]);
                    const double delta = b - a;
                    if (std::abs(delta) < 1e-14) {
                        if (a > 1e-10) { intersects = false; break; }
                    } else if (delta > 0) leave = std::min(leave, -a / delta);
                    else enter = std::max(enter, -a / delta);
                    if (leave < enter) { intersects = false; break; }
                }
                const auto point = [&](double t) { return segment[0] + (segment[1] - segment[0]) * t; };
                if (!intersects) next.push_back(segment);
                else {
                    if (enter > 1e-10) next.push_back({segment[0], point(enter)});
                    if (leave < 1 - 1e-10) next.push_back({point(leave), segment[1]});
                }
            }
            segments = std::move(next);
        }
        for (const auto& segment : segments) {
            if ((segment[1] - segment[0]).length() > 1e-10) trimmed.stroke({segment[0], segment[1]});
        }
    }
    for (const auto& part : fin.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        PartPolygons pieces = {{part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]}};
        for (const auto& volume : volumes) {
            PartPolygons next;
            for (const auto& piece : pieces) for (auto& p : outsideFinVolume(piece, volume)) next.push_back(std::move(p));
            pieces = std::move(next);
        }
        for (const auto& piece : pieces) trimmed.polygon(piece);
    }
    fin.geometry = std::move(trimmed.geometry);
}
