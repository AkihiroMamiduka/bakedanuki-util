// 回転後の後端断面で円弧を切り、内外周を同じ接合線へ揃える。
void appendRadialCirclePlaneAngles(std::vector<double>& angles, const OptionClipPlane& plane,
    double radius, double first, double last) {
    if (radius <= 1e-12) return;
    const double ratio = plane.distance / radius;
    if (std::abs(ratio) > 1.0 + 1e-10) return;
    const double phase = std::atan2(plane.normal.y, plane.normal.z);
    const double delta = std::acos(std::clamp(ratio, -1.0, 1.0));
    for (double side : {-1.0, 1.0}) for (int turn = -1; turn <= 1; ++turn) {
        const double angle = phase + side * delta + turn * 2.0 * kPi;
        if (angle > first + 1e-12 && angle < last - 1e-12) angles.push_back(angle);
    }
}

bool appendAdjustedRadialCircle(PartBuilder& builder, const ShapeSettings& settings,
    std::vector<OptionClipVolume>& bodyVolumes) {
    if (!settings.part || settings.partType == 2) return false;
    const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
    if (sweep < 1e-12) return false;
    const double first = (kPi - sweep) * 0.5, last = (kPi + sweep) * 0.5;
    const bool wideBase = outlinePresetIndex(settings.shape) == 111;
    const bool wide = wideBase && settings.wideWidth > 1e-12;
    const double outer = wide ? 0.5 + settings.wideWidth * 0.5 : 0.5;
    const double inner = wide ? std::max(0.0, 0.5 - settings.wideWidth * 0.5) : 0.0;
    std::vector<AxialHeadPlacement> placements;
    for (int index = 0; index < (settings.partType == 1 ? 2 : 1); ++index) {
        const bool atFirst = index == 0;
        placements.push_back(radialHeadPlacement(settings,
            radialCircleEndSite(atFirst ? first : last, atFirst), first, last, atFirst));
    }
    if (std::none_of(placements.begin(), placements.end(), [](const auto& p) { return p.onArc; })) return false;

    auto angles = semicircleSampleAngles(first, last);
    std::vector<OptionClipVolume> cuts;
    for (std::size_t index = 0; index < placements.size(); ++index) {
        const auto& placement = placements[index];
        if (!placement.onArc) continue;
        angles.push_back(placement.angle);
        const double endpointAngle = index == 0 ? first : last;
        const auto original = radialCircleEndSite(endpointAngle, index == 0);
        const auto middle = kSemicirclePlane.point(MPoint::origin +
            semicircleRadial((endpointAngle + placement.angle) * 0.5)) - MPoint::origin;
        cuts.push_back({{-placement.site.along,
            -(placement.base - MPoint::origin) * placement.site.along}, {-middle, 0.0},
            {original.along, 0.0}});
        for (const auto& plane : cuts.back()) {
            appendRadialCirclePlaneAngles(angles, plane, outer, first, last);
            if (wide) appendRadialCirclePlaneAngles(angles, plane, inner, first, last);
        }
    }
    std::sort(angles.begin(), angles.end());
    angles.erase(std::unique(angles.begin(), angles.end(), [](double a, double b) {
        return std::abs(a - b) < 1e-12;
    }), angles.end());
    std::vector<MPoint> outerPoints, innerPoints;
    for (double angle : angles) {
        const auto radial = semicircleRadial(angle);
        outerPoints.push_back(kSemicirclePlane.point(MPoint::origin + radial * outer));
        innerPoints.push_back(kSemicirclePlane.point(MPoint::origin + radial * inner));
    }
    PartBuilder surface(true);
    for (std::size_t index = 1; index < angles.size(); ++index) {
        if (wide) surface.quad(outerPoints[index - 1], outerPoints[index], innerPoints[index], innerPoints[index - 1]);
        else surface.triangle(MPoint::origin, outerPoints[index - 1], outerPoints[index]);
    }
    trimOptionGeometry(surface.geometry, cuts, true);
    if (wide) {
        WideEndArrowGeometry band;
        for (const auto& part : surface.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
            band.triangles.push_back({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
        }
        appendPartTriangleUnion(builder, band, kSemicirclePlane);
    } else {
        PartBuilder line(false);
        line.stroke(outerPoints);
        trimOptionStrokes(line.geometry, cuts);
        mergeOptionGeometry(builder.geometry, std::move(line.geometry));
        if (!wideBase && builder.filled) {
            for (const auto& part : surface.geometry.fillParts) builder.geometry.fillParts.push_back(part);
        }
        if (!settings.fill && !wideBase && settings.partShape <= 1) {
            // 開いたV字の矢印は、円弧から付け根中央を通る軸線でつなぐ。
            for (const auto& placement : placements) if (placement.onArc) {
                const auto tip = placement.site.endpoint + placement.site.along * settings.partOffset;
                builder.stroke({placement.base, tip});
            }
        }
    }
    if (wide || (!wideBase && builder.filled)) {
        for (const auto& part : surface.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
            auto volume = optionPlanarVolume({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
            if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
        }
    }
    return true;
}
