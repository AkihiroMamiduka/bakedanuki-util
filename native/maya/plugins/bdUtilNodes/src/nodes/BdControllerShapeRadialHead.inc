// 元の先端または中心を固定し、平面内の直交する二軸を接合点へ向ける。
AxialHeadPlacement radialHeadAtDepth(const ShapeSettings& settings, const OptionSite& original,
    double start, double end, bool first, double depth) {
    if (hasBaseSpaceScale(settings)) {
        const auto originalAlong = baseSpaceNormalized(baseSpaceVector(original.along, settings));
        const auto originalSide = baseSpaceVector(original.side, settings);
        const auto normal = baseSpaceNormalized(originalAlong ^ originalSide);
        const auto anchorVector = baseSpaceVector(original.endpoint - MPoint::origin, settings) +
            originalAlong * settings.partOffset;
        const auto anchor = MPoint::origin + inverseBaseSpaceVector(anchorVector, settings);
        const bool centered = settings.partShape >= 3 && settings.partShape <= 8;
        AxialHeadPlacement result{original, centered ? anchor :
            anchor - inverseBaseSpaceVector(originalAlong * depth, settings), first ? start : end, false};
        if (depth <= 1e-12) return result;
        double nearest = 1e100;
        for (double angle : baseArcIntersectionAngles(anchorVector, depth, start, end, settings)) {
            const auto base = baseArcPoint(angle);
            const auto baseVector = baseSpaceVector(base - MPoint::origin, settings);
            const auto aim = anchorVector - baseVector;
            if (aim.length() < 1e-12) continue;
            const auto direction = baseSpaceNormalized(aim);
            const auto side = baseSpaceNormalized(normal ^ direction);
            if (direction * originalAlong < -1e-10 || side * baseVector < -1e-10) continue;
            const double inward = first ? angle - start : end - angle;
            if (inward > kPi + 1e-10 || inward >= nearest) continue;
            nearest = inward;
            result.site.along = baseSpaceNormalized(inverseBaseSpaceVector(direction, settings));
            result.site.side = baseSpaceNormalized(inverseBaseSpaceVector(side, settings));
            result.site.endpoint = anchor - inverseBaseSpaceVector(direction * settings.partOffset, settings);
            result.base = base;
            result.angle = angle;
            result.onArc = true;
        }
        return result;
    }
    const auto anchor = original.endpoint + original.along * settings.partOffset;
    const bool centered = settings.partShape >= 3 && settings.partShape <= 8;
    AxialHeadPlacement result{original, centered ? anchor : anchor - original.along * depth,
        first ? start : end, false};
    constexpr double radius = 0.5;
    const auto toAnchor = anchor - MPoint::origin;
    const double distance = toAnchor.length();
    if (depth <= 1e-12 || distance < 1e-12 || distance > radius + depth + 1e-10 ||
        distance < std::abs(radius - depth) - 1e-10) return result;
    const double along = (radius * radius + distance * distance - depth * depth) / (2.0 * distance);
    const double fromAnchor = distance - along;
    const double squared = depth < radius
        ? depth * depth - fromAnchor * fromAnchor : radius * radius - along * along;
    if (squared < -1e-10) return result;
    const auto normal = (original.along ^ original.side).normal();
    const auto radial = toAnchor / distance;
    const auto across = normal ^ radial;
    const double height = std::sqrt(std::max(0.0, squared));
    double nearest = 1e100;
    for (double sign : {-1.0, 1.0}) {
        const auto base = MPoint::origin + radial * along + across * (sign * height);
        const auto aim = anchor - base;
        if (aim.length() < 1e-12) continue;
        const auto direction = aim.normal();
        const auto side = (normal ^ direction).normal();
        if (direction * original.along < -1e-10 || side * (base - MPoint::origin) < -1e-10) continue;
        const double rawAngle = std::atan2(base.y, base.z);
        for (int turn = -1; turn <= 1; ++turn) {
            const double candidate = rawAngle + turn * 2.0 * kPi;
            if (candidate < start - 1e-10 || candidate > end + 1e-10) continue;
            const double angle = std::clamp(candidate, start, end);
            const double inward = first ? angle - start : end - angle;
            if (inward > kPi + 1e-10 || inward >= nearest) continue;
            nearest = inward;
            result.site.along = direction;
            result.site.side = side;
            // 共通生成側でOffsetを加えても、元の接線で決めた位置を変えない。
            result.site.endpoint = anchor - direction * settings.partOffset;
            result.base = base;
            result.angle = angle;
            result.onArc = true;
        }
    }
    return result;
}

double radialHeadBandExtent(const AxialHeadPlacement& placement, double halfWidth,
    const ShapeSettings& settings) {
    if (halfWidth <= 1e-12) return 0.0;
    if (hasBaseSpaceScale(settings)) {
        const auto side = baseSpaceNormalized(baseSpaceVector(placement.site.side, settings));
        const auto along = baseSpaceNormalized(baseSpaceVector(placement.site.along, settings));
        const auto base = baseSpaceVector(placement.base - MPoint::origin, settings);
        const auto roots = [&](double offset) {
            std::vector<double> values;
            const auto point = [&](double angle) {
                return baseSpaceVector(baseSpaceCircleOffsetPoint(baseArcPoint(angle), offset, settings) - MPoint::origin, settings);
            };
            const auto value = [&](double angle) { return (point(angle) - base) * along; };
            double first = 0.0, firstValue = value(first);
            for (unsigned int i = 1; i <= 256; ++i) {
                const double last = 2.0 * kPi * i / 256, lastValue = value(last);
                if (std::abs(firstValue) < 1e-12) values.push_back((point(first) - base) * side);
                if ((firstValue < 0.0) != (lastValue < 0.0)) {
                    double low = first, high = last;
                    for (unsigned int step = 0; step < 40; ++step) {
                        const double middle = (low + high) * 0.5;
                        if ((value(middle) < 0.0) == (firstValue < 0.0)) low = middle;
                        else high = middle;
                    }
                    values.push_back((point((low + high) * 0.5) - base) * side);
                }
                first = last;
                firstValue = lastValue;
            }
            std::sort(values.begin(), values.end());
            return values;
        };
        const auto outer = roots(halfWidth), inner = roots(-halfWidth);
        const auto positive = std::find_if(outer.begin(), outer.end(), [](double value) { return value >= -1e-10; });
        if (positive == outer.end()) return 1e100;
        const auto negative = std::find_if(inner.rbegin(), inner.rend(), [](double value) { return value <= 1e-10; });
        if (negative == inner.rend()) return std::max(*positive, -outer.front());
        return std::max(*positive, -*negative);
    }
    const auto radial = placement.base - MPoint::origin;
    const double projected = radial * placement.site.side;
    const double outer = 0.5 + halfWidth;
    const double inner = std::max(0.0, 0.5 - halfWidth);
    const double outerSquared = projected * projected + outer * outer - 0.25;
    const double innerSquared = projected * projected + inner * inner - 0.25;
    const double outerRoot = std::sqrt(std::max(0.0, outerSquared));
    // 斜めの断面が内周へ届かない場合、幅一定の帯としては受けられない。
    if (inner > 1e-12 && innerSquared < -1e-12) return 1e100;
    const double inward = inner > 1e-12
        ? projected - std::sqrt(std::max(0.0, innerSquared)) : projected + outerRoot;
    return std::max(inward, outerRoot - projected);
}

double radialHeadSectionExtent(const ShapeSettings& settings, double depth, double halfLength) {
    const double halfWidth = 0.05 * std::abs(partWidth(settings));
    if (settings.partShape == 3 || settings.partShape == 6) return halfWidth;
    if (settings.partShape == 4 || settings.partShape == 7) {
        return halfWidth * std::max(0.0, 1.0 - depth / halfLength);
    }
    // 円は実際の多角形、Sphereはその中央断面に使う32角形で判定する。
    const auto profile = planarEndProfile(2);
    const std::size_t stride = settings.partShape == 8 ? 2 : 1;
    const double along = -0.5 * depth / halfLength;
    double extent = 0.0;
    for (std::size_t i = 0; i < profile.size(); i += stride) {
        const auto a = profile[i], b = profile[(i + stride) % profile.size()];
        if (along < std::min(a.x, b.x) - 1e-12 || along > std::max(a.x, b.x) + 1e-12) continue;
        const double delta = b.x - a.x;
        const double side = std::abs(delta) < 1e-12 ? std::max(std::abs(a.y), std::abs(b.y))
            : std::abs(a.y + (b.y - a.y) * std::clamp((along - a.x) / delta, 0.0, 1.0));
        extent = std::max(extent, side * 2.0 * halfWidth);
    }
    return extent;
}

AxialHeadPlacement radialHeadPlacement(const ShapeSettings& settings, const OptionSite& original,
    double start, double end, bool first) {
    const double length = partLength(settings);
    const bool centered = settings.partShape >= 3 && settings.partShape <= 8;
    const double maximum = (settings.partShape <= 1 ? 0.1 * std::cos(kPi / 6.0)
        : centered ? 0.05 : 0.1) * length;
    const auto along = hasBaseSpaceScale(settings)
        ? baseSpacePartDirection(original.along, settings) : original.along;
    const auto anchor = original.endpoint + along * settings.partOffset;
    AxialHeadPlacement fallback{original, centered ? anchor : anchor - along * maximum,
        first ? start : end, false};
    if (original.attached || maximum <= 1e-12 || end - start <= 1e-12 || !std::isfinite(maximum)) return fallback;
    if (settings.partShape == 8 && std::abs(length - std::abs(partWidth(settings))) < 1e-12) return fallback;
    const auto candidate = radialHeadAtDepth(settings, original, start, end, first, maximum);
    // 先端型は底面中心で接合できる。帯より狭い底面も実際の交差でつなぐ。
    if (!centered) return candidate;
    const short outline = outlinePresetIndex(settings.shape);
    const double halfWidth = outline == 111 || crossCircleBaseOutline(outline) == 111
        ? std::max(0.0, settings.wideWidth) * 0.5 : 0.0;
    if (halfWidth <= 1e-12) return candidate;
    const auto fits = [&](const AxialHeadPlacement& placement, double depth) {
        return placement.onArc && radialHeadBandExtent(placement, halfWidth, settings) <=
            radialHeadSectionExtent(settings, depth, maximum) + 1e-10;
    };
    if (fits(candidate, maximum)) return candidate;
    // 最も後ろで帯を受ける断面を探し、見つかった区間だけを精密化する。
    double previous = maximum;
    for (unsigned int i = 1; i <= 64; ++i) {
        const double depth = maximum * (1.0 - static_cast<double>(i) / 65.0);
        auto result = radialHeadAtDepth(settings, original, start, end, first, depth);
        if (!fits(result, depth)) { previous = depth; continue; }
        double low = depth, high = previous;
        for (unsigned int step = 0; step < 32; ++step) {
            const double middle = (low + high) * 0.5;
            auto refined = radialHeadAtDepth(settings, original, start, end, first, middle);
            if (fits(refined, middle)) { low = middle; result = refined; }
            else high = middle;
        }
        return result;
    }
    return fallback;
}
