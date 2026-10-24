// 曲面を三角形のまま接合し、共有辺を除いた外周だけを輪郭にする。
void appendOptionSurfaceOutline(PartBuilder& builder, const PartGeometry& surface) {
    std::vector<MPoint> vertices;
    for (const auto& part : surface.fillParts) {
        vertices.insert(vertices.end(), part.triangles.begin(), part.triangles.end());
    }
    std::vector<std::array<MPoint, 2>> boundary;
    for (const auto& part : surface.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        for (unsigned int edge = 0; edge < 3; ++edge) {
            const auto a = part.triangles[i + edge];
            const auto b = part.triangles[i + (edge + 1) % 3];
            const auto direction = b - a;
            const double squared = direction * direction;
            if (squared < 1e-20) continue;
            std::vector<double> cuts = {0.0, 1.0};
            for (const auto& vertex : vertices) {
                const double t = ((vertex - a) * direction) / squared;
                if (t > 1e-10 && t < 1.0 - 1e-10 && (vertex - (a + direction * t)).length() < 1e-9) cuts.push_back(t);
            }
            std::sort(cuts.begin(), cuts.end());
            cuts.erase(std::unique(cuts.begin(), cuts.end(), [](double x, double y) { return std::abs(x - y) < 1e-10; }), cuts.end());
            for (std::size_t cut = 1; cut < cuts.size(); ++cut) {
                const std::array<MPoint, 2> segment = {a + direction * cuts[cut - 1], a + direction * cuts[cut]};
                const auto shared = std::find_if(boundary.begin(), boundary.end(), [&](const auto& other) {
                    return ((segment[0] - other[1]).length() < 1e-9 && (segment[1] - other[0]).length() < 1e-9) ||
                        ((segment[0] - other[0]).length() < 1e-9 && (segment[1] - other[1]).length() < 1e-9);
                });
                if (shared == boundary.end()) boundary.push_back(segment);
                else boundary.erase(shared);
            }
        }
    }
    while (!boundary.empty()) {
        std::vector<MPoint> stroke = {boundary.back()[0], boundary.back()[1]};
        boundary.pop_back();
        while (true) {
            const auto next = std::find_if(boundary.begin(), boundary.end(), [&](const auto& edge) {
                return (edge[0] - stroke.back()).length() < 1e-9 || (edge[1] - stroke.back()).length() < 1e-9;
            });
            if (next == boundary.end()) break;
            stroke.push_back(((*next)[0] - stroke.back()).length() < 1e-9 ? (*next)[1] : (*next)[0]);
            boundary.erase(next);
        }
        builder.stroke(stroke);
    }
}

double optionAxialJoinDistance(const ShapeSettings& settings) {
    if (settings.partShape <= 1) return settings.partOffset - 0.1 * std::cos(kPi / 6.0) * partLength(settings);
    if (settings.partShape == 2 || settings.partShape >= 9) return settings.partOffset - 0.1 * partLength(settings);
    return settings.partOffset;
}

bool axialArcTouchesSolid(const std::vector<double>& angles, const OptionHeads& heads) {
    for (std::size_t i = 1; i < angles.size(); ++i) {
        const auto a = kSemicirclePlane.point(MPoint::origin + semicircleRadial(angles[i - 1]) * 0.5);
        const auto b = kSemicirclePlane.point(MPoint::origin + semicircleRadial(angles[i]) * 0.5);
        for (const auto& volume : heads.volumes) {
            double enter = 0.0, leave = 1.0;
            bool intersects = true;
            for (const auto& plane : volume) {
                const double start = plane.value(a);
                const double delta = plane.value(b) - start;
                if (std::abs(delta) < 1e-14) {
                    if (start > 1e-10) { intersects = false; break; }
                } else if (delta > 0) leave = std::min(leave, -start / delta);
                else enter = std::max(enter, -start / delta);
                if (leave < enter - 1e-10) { intersects = false; break; }
            }
            if (intersects) return true;
        }
    }
    return false;
}

void appendOptionAxialCircle(PartBuilder& builder, const ShapeSettings& settings,
    OptionHeads& heads, const std::vector<OptionSite>& sites,
    std::vector<OptionClipVolume>& bodyVolumes) {
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep < 1e-12) return;
    const double start = (kPi - sweep) * 0.5;
    const double end = (kPi + sweep) * 0.5;
    const double halfWidth = settings.wideWidth * 0.5;
    const auto at = [](double angle) { return kSemicirclePlane.point(MPoint::origin + semicircleRadial(angle) * 0.5); };
    double first = start, last = end;
    const bool chordHead = settings.partShape <= 2;
    const bool solidHead = settings.partShape >= 6;
    const bool preserveApex = settings.partType == 2 && settings.partShape >= 3 && settings.partShape <= 5;
    std::vector<AxialHeadPlacement> headPlacements;
    const double joinDistance = optionAxialJoinDistance(settings);
    const double trim = std::min(std::asin(std::clamp(-joinDistance * 2.0, 0.0, 1.0)), sweep * (sites.size() == 2 ? 0.5 : 1.0));
    for (const auto& site : sites) {
        if (site.attached) continue;
        const bool atStart = site.side.x > 0;
        headPlacements.push_back(axialHeadPlacement(settings,
            axialCircleEndSite(atStart ? start : end, atStart), start, end));
        if ((!solidHead || settings.partShape >= 9) && (chordHead || headPlacements.back().onArc)) {
            if (atStart) first = headPlacements.back().angle;
            else last = headPlacements.back().angle;
        } else if (!solidHead) {
            if (atStart) first += trim;
            else last -= trim;
        }
    }
    if (first > last) return;
    auto angles = semicircleSampleAngles(first, last);
    if (solidHead) {
        // 姿勢調整に使った円弧上の断面を含め、立体との実交差を切り取る。
        for (const auto& placement : headPlacements) if (placement.onArc) angles.push_back(placement.angle);
        std::sort(angles.begin(), angles.end());
        angles.erase(std::unique(angles.begin(), angles.end(), [](double a, double b) {
            return std::abs(a - b) < 1e-12;
        }), angles.end());
    }
    const bool solidContact = solidHead && axialArcTouchesSolid(angles, heads);
    if (halfWidth <= 1e-12) {
        std::vector<MPoint> points;
        for (double angle : angles) points.push_back(at(angle));
        std::size_t index = 0;
        for (const auto& site : sites) {
            if (site.attached) continue;
            const auto& placement = headPlacements[index++];
            if (solidContact || placement.onArc) continue;
            const auto join = placement.base;
            if (site.side.x > 0) points.insert(points.begin(), join);
            else points.push_back(join);
        }
        builder.stroke(points);
        if (!preserveApex) trimOptionGeometry(builder.geometry, heads.volumes, builder.filled);
        return;
    }
    PartBuilder surface(true);
    const auto side = nativeAxis(0) * halfWidth;
    for (std::size_t i = 1; i < angles.size(); ++i) {
        const auto a = at(angles[i - 1]), b = at(angles[i]);
        surface.quad(a - side, b - side, b + side, a + side);
    }
    // 頭部の幅が十分にある断面まで帯を延ばし、頭部内部を差し引いて接合する。
    std::size_t index = 0;
    for (const auto& site : sites) {
        if (site.attached) continue;
        const auto& placement = headPlacements[index++];
        if (solidContact || placement.onArc) continue;
        const auto arc = at(site.side.x > 0 ? first : last);
        const auto join = placement.base;
        if ((arc - join).length() < 1e-12) continue;
        if (site.side.x > 0) surface.quad(join - side, arc - side, arc + side, join + side);
        else surface.quad(arc - side, join - side, join + side, arc + side);
    }
    if (!preserveApex) trimOptionGeometry(surface.geometry, heads.volumes, true);
    appendOptionSurfaceOutline(builder, surface.geometry);
    if (!preserveApex) trimOptionStrokes(builder.geometry, heads.volumes);
    for (const auto& part : surface.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        auto volume = optionPlanarVolume({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
        if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
    }
    if (builder.filled) builder.geometry.fillParts = std::move(surface.geometry.fillParts);
}
