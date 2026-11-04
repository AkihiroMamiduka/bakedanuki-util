// 通常の平面形状として、閉じた円と半径方向の帯を作る。
bool isPlanarCircleOutline(short outline) {
    return outline == 116 || outline == 117;
}

MPoint baseSpaceCircleOffsetPoint(const MPoint& point, double offset, const ShapeSettings& settings) {
    const auto radial = point - MPoint::origin;
    const auto normal = baseSpaceNormalized(inverseBaseSpaceVector(radial, settings));
    const double limit = baseSpaceVector(radial, settings) * normal;
    return point + inverseBaseSpaceVector(normal * std::max(offset, -limit), settings);
}

double planarCircleSurfaceOffset(double radius, double side) {
    const double distance = std::min(radius, std::abs(side));
    // 描画に使う円周の線分上へ肩を置き、理想円との近似誤差を残さない。
    for (unsigned int i = 0; i < kCircleSegments / 4; ++i) {
        const double firstAngle = 2.0 * kPi * i / kCircleSegments;
        const double lastAngle = 2.0 * kPi * (i + 1) / kCircleSegments;
        const double firstSide = radius * std::sin(firstAngle);
        const double lastSide = radius * std::sin(lastAngle);
        if (distance > lastSide) continue;
        const double weight = (distance - firstSide) / (lastSide - firstSide);
        return radius * (std::cos(firstAngle) +
            (std::cos(lastAngle) - std::cos(firstAngle)) * weight - 1.0);
    }
    return -radius;
}

double planarCircleMappedSurfaceOffset(const MPoint& endpoint, const MVector& along,
    const MVector& side, double sideDistance, const ShapeSettings& settings) {
    const double radius = (endpoint - MPoint::origin) * along;
    if (!hasBaseSpaceScale(settings)) return planarCircleSurfaceOffset(radius, sideDistance);
    const double offset = outlinePresetIndex(settings.shape) == 117 ? settings.wideWidth * 0.5 : 0.0;
    const auto at = [&](unsigned int index) {
        const double angle = 2.0 * kPi * index / kCircleSegments;
        return baseSpaceCircleOffsetPoint(MPoint(0, 0.5 * std::cos(angle),
            0.5 * std::sin(angle)), offset, settings);
    };
    double result = -radius;
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const auto a = at(i), b = at(i + 1);
        const double first = (a - endpoint) * side, last = (b - endpoint) * side;
        if (sideDistance < std::min(first, last) - 1e-12 ||
            sideDistance > std::max(first, last) + 1e-12) continue;
        const double delta = last - first;
        const auto point = std::abs(delta) <= 1e-12 ? a :
            a + (b - a) * std::clamp((sideDistance - first) / delta, 0.0, 1.0);
        result = std::max(result, (point - endpoint) * along);
    }
    return result;
}

void appendOptionPlanarCircle(PartBuilder& builder, const ShapeSettings& settings,
    std::vector<OptionClipVolume>& bodyVolumes) {
    const bool wide = outlinePresetIndex(settings.shape) == 117;
    const double halfWidth = wide ? settings.wideWidth * 0.5 : 0.0;
    const auto span = baseSpaceScale(settings);
    const double innerRadius = std::max(0.0, std::min(std::abs(span.y), std::abs(span.z)) * 0.5 - halfWidth);
    std::vector<MPoint> outer, inner;
    outer.reserve(kCircleSegments + 1);
    inner.reserve(kCircleSegments + 1);
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const double angle = 2.0 * kPi * i / kCircleSegments;
        const auto radial = nativeAxis(1) * std::cos(angle) + nativeAxis(2) * std::sin(angle);
        const auto center = MPoint::origin + radial * 0.5;
        outer.push_back(baseSpaceCircleOffsetPoint(center, halfWidth, settings));
        inner.push_back(baseSpaceCircleOffsetPoint(center, -halfWidth, settings));
    }
    outer.push_back(outer.front());
    inner.push_back(inner.front());
    builder.stroke(outer);
    if (wide && halfWidth <= 1e-12) return;
    if (!wide || innerRadius <= 1e-12) {
        for (unsigned int i = 0; i < kCircleSegments; ++i) {
            builder.triangle(MPoint::origin, outer[i], outer[i + 1]);
        }
        if (wide || builder.filled || (settings.part && settings.partShape <= 1)) {
            auto volume = optionPlanarVolume(std::vector<MPoint>(outer.begin(), outer.end() - 1));
            if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
        }
        return;
    }
    builder.stroke(inner);
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        builder.quad(outer[i], outer[i + 1], inner[i + 1], inner[i]);
        auto volume = optionPlanarVolume({outer[i], outer[i + 1], inner[i + 1], inner[i]});
        if (!volume.empty()) bodyVolumes.push_back(std::move(volume));
    }
}
