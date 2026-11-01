// 中心または先端と寸法を保ち、帯幅を受ける断面を円弧へ向ける。
// 楕円の弧長を周期座標へ写し、部品の長さを基準空間の倍率から独立させる。
struct BaseArcMetric {
    static constexpr unsigned int divisions = 1024;
    double y = 1.0;
    double z = 1.0;
    std::array<double, divisions + 1> lengths{};

    double speed(double angle) const {
        return 0.5 * std::hypot(y * std::cos(angle), z * std::sin(angle));
    }

    double integral(double first, double last) const {
        return (last - first) * (speed(first) + 4.0 * speed((first + last) * 0.5) + speed(last)) / 6.0;
    }

    void reset(double nextY, double nextZ) {
        y = nextY;
        z = nextZ;
        lengths[0] = 0.0;
        for (unsigned int i = 1; i <= divisions; ++i) {
            lengths[i] = lengths[i - 1] + integral(2.0 * kPi * (i - 1) / divisions,
                2.0 * kPi * i / divisions);
        }
    }

    double periodScale() const { return lengths.back() / kPi; }

    double position(double angle) const {
        if (y == z) return angle * 0.5;
        const double turns = std::floor(angle / (2.0 * kPi));
        const double local = angle - turns * 2.0 * kPi;
        const unsigned int index = std::min(divisions - 1,
            static_cast<unsigned int>(local * divisions / (2.0 * kPi)));
        const double length = lengths[index] + integral(2.0 * kPi * index / divisions, local);
        return turns * kPi + length / periodScale();
    }

    double angle(double position) const {
        if (y == z) return position * 2.0;
        const double turns = std::floor(position / kPi);
        const double target = (position - turns * kPi) * periodScale();
        const auto found = std::upper_bound(lengths.begin(), lengths.end(), target);
        const unsigned int index = std::min(divisions - 1,
            static_cast<unsigned int>(std::max<std::ptrdiff_t>(0, found - lengths.begin() - 1)));
        const double first = 2.0 * kPi * index / divisions;
        const double last = 2.0 * kPi * (index + 1) / divisions;
        double result = first + (last - first) * (target - lengths[index]) /
            (lengths[index + 1] - lengths[index]);
        for (unsigned int step = 0; step < 3; ++step) {
            result = std::clamp(result - (lengths[index] + integral(first, result) - target) /
                speed(result), first, last);
        }
        return turns * 2.0 * kPi + result;
    }
};

const BaseArcMetric& baseArcMetric(const ShapeSettings& settings) {
    const auto scale = baseSpaceScale(settings);
    const double y = std::abs(scale.y), z = std::abs(scale.z);
    thread_local BaseArcMetric metric;
    if (metric.lengths.back() == 0.0 || metric.y != y || metric.z != z) metric.reset(y, z);
    return metric;
}

MVector baseArcNormal(double angle, const ShapeSettings& settings) {
    return baseSpaceNormalized(inverseBaseSpaceVector(MVector(0.0, std::sin(angle), std::cos(angle)), settings));
}

MPoint baseArcPoint(double angle) {
    return MPoint(0.0, 0.5 * std::sin(angle), 0.5 * std::cos(angle));
}

std::vector<double> baseArcIntersectionAngles(const MVector& anchor, double radius,
    double first, double last, const ShapeSettings& settings) {
    std::vector<double> angles;
    const auto value = [&](double angle) {
        const auto delta = baseSpaceVector(baseArcPoint(angle) - MPoint::origin, settings) - anchor;
        return delta * delta - radius * radius;
    };
    const auto derivative = [&](double angle) {
        const auto delta = baseSpaceVector(baseArcPoint(angle) - MPoint::origin, settings) - anchor;
        const auto tangent = baseSpaceVector(MVector(0.0,
            0.5 * std::cos(angle), -0.5 * std::sin(angle)), settings);
        return delta * tangent;
    };
    const auto bisect = [](const auto& function, double low, double high) {
        double lowValue = function(low);
        for (unsigned int step = 0; step < 48; ++step) {
            const double middle = (low + high) * 0.5;
            const double middleValue = function(middle);
            if ((middleValue < 0.0) == (lowValue < 0.0)) {
                low = middle;
                lowValue = middleValue;
            } else high = middle;
        }
        return (low + high) * 0.5;
    };
    // 接触区間が短い場合も、距離の極小点を含む単調区間で交点を挟む。
    std::vector<double> cuts = {first, last};
    constexpr unsigned int samples = 256;
    double a = first, da = derivative(a);
    for (unsigned int i = 1; i <= samples; ++i) {
        const double b = first + (last - first) * i / samples;
        const double db = derivative(b);
        if (da == 0.0) cuts.push_back(a);
        if ((da < 0.0) != (db < 0.0)) cuts.push_back(bisect(derivative, a, b));
        a = b;
        da = db;
    }
    std::sort(cuts.begin(), cuts.end());
    cuts.erase(std::unique(cuts.begin(), cuts.end(), [](double x, double y) {
        return std::abs(x - y) < 1e-13;
    }), cuts.end());
    for (std::size_t i = 0; i < cuts.size(); ++i) {
        const double at = value(cuts[i]);
        if (std::abs(at) <= 1e-13 * std::max(1.0, radius * radius)) angles.push_back(cuts[i]);
        if (i > 0 && (at < 0.0) != (value(cuts[i - 1]) < 0.0)) {
            angles.push_back(bisect(value, cuts[i - 1], cuts[i]));
        }
    }
    return angles;
}

struct AxialHeadPlacement {
    OptionSite site;
    MPoint base;
    double angle;
    bool onArc;
};

double axialHeadJoinLength(const ShapeSettings& settings) {
    const double length = partLength(settings);
    if (settings.partShape <= 1) return 0.1 * std::cos(kPi / 6.0) * length;
    if (settings.partShape == 2 || settings.partShape >= 9) return 0.1 * length;
    const double halfLength = 0.05 * length;
    if (settings.partShape == 3 || settings.partShape == 6) return halfLength;
    const double halfWidth = 0.05 * std::abs(partWidth(settings));
    const double bandHalfWidth = settings.wideWidth * 0.5;
    if (halfWidth <= 1e-12 || bandHalfWidth >= halfWidth) return 0.0;
    const double ratio = bandHalfWidth / halfWidth;
    if (settings.partShape == 4 || settings.partShape == 7) return halfLength * (1.0 - ratio);
    if (settings.partShape == 8) return halfLength * std::sqrt(1.0 - ratio * ratio);

    // Circleは描画に使う多角形の辺から、帯幅を受けられる断面を求める。
    const auto profile = planarEndProfile(2);
    const double side = ratio * 0.5;
    double rear = 0.0;
    for (std::size_t i = 0; i < profile.size(); ++i) {
        const auto a = profile[i], b = profile[(i + 1) % profile.size()];
        if (side < std::min(a.y, b.y) - 1e-12 || side > std::max(a.y, b.y) + 1e-12) continue;
        const double delta = b.y - a.y;
        if (std::abs(delta) < 1e-12) rear = std::min(rear, std::min(a.x, b.x));
        else rear = std::min(rear, a.x + (b.x - a.x) * std::clamp((side - a.y) / delta, 0.0, 1.0));
    }
    return -rear * 0.1 * length;
}

AxialHeadPlacement axialHeadPlacement(
    const ShapeSettings& settings, const OptionSite& site, double start, double end
) {
    const bool first = site.side.x > 0;
    const bool centered = settings.partShape >= 3 && settings.partShape <= 8;
    const double length = axialHeadJoinLength(settings);
    if (hasBaseSpaceScale(settings)) {
        const auto originalAlong = baseSpaceNormalized(baseSpaceVector(site.along, settings));
        const auto physicalSide = baseSpaceNormalized(baseSpaceVector(site.side, settings));
        const auto tipVector = baseSpaceVector(site.endpoint - MPoint::origin, settings) +
            originalAlong * settings.partOffset;
        const auto tip = MPoint::origin + inverseBaseSpaceVector(tipVector, settings);
        AxialHeadPlacement result{site, centered ? tip :
            tip - inverseBaseSpaceVector(originalAlong * length, settings), first ? start : end, false};
        if (site.attached || length <= 1e-12 || end - start <= 1e-12) return result;
        if (settings.partShape >= 3 && settings.wideWidth >
            0.1 * std::abs(partWidth(settings)) + 1e-10) return result;
        if (settings.partShape == 8 && std::abs(partLength(settings) -
            std::abs(partHeight(settings))) < 1e-12) return result;
        double nearest = 1e100;
        for (double angle : baseArcIntersectionAngles(tipVector, length, start, end, settings)) {
            const auto base = baseArcPoint(angle);
            const auto baseVector = baseSpaceVector(base - MPoint::origin, settings);
            const auto aim = tipVector - baseVector;
            if (aim.length() < 1e-12) continue;
            const auto direction = baseSpaceNormalized(aim);
            if (direction * originalAlong < -1e-10 ||
                (direction ^ physicalSide) * baseVector < -1e-10) continue;
            const double inward = first ? angle - start : end - angle;
            if (inward > kPi + 1e-10 || inward >= nearest) continue;
            nearest = inward;
            result.site.along = baseSpaceNormalized(inverseBaseSpaceVector(direction, settings));
            result.site.endpoint = tip - inverseBaseSpaceVector(direction * settings.partOffset, settings);
            result.base = base;
            result.angle = angle;
            result.onArc = true;
        }
        return result;
    }
    const auto tip = site.endpoint + site.along * settings.partOffset;
    AxialHeadPlacement result{site, centered ? tip : tip - site.along * length, first ? start : end, false};
    // 負の長さは接線方向の反転を保つ。円弧内側へ回すと正の長さと同形になる。
    if (site.attached || length <= 1e-12 || end - start <= 1e-12) return result;
    if (settings.partShape >= 3 && settings.wideWidth > 0.1 * std::abs(partWidth(settings)) + 1e-10) return result;
    // 長さと高さが等しいSphereは幅軸まわりの回転で形が変わらない。
    if (settings.partShape == 8 && std::abs(partLength(settings) - std::abs(partHeight(settings))) < 1e-12) return result;

    constexpr double radius = 0.5;
    const MVector toTip = tip - MPoint::origin;
    const double distance = toTip.length();
    if (distance < 1e-12 || distance > radius + length + 1e-10 ||
        distance < std::abs(radius - length) - 1e-10) return result;
    const double along = (radius * radius + distance * distance - length * length) / (2.0 * distance);
    const double fromTip = distance - along;
    const double squared = length < radius
        ? length * length - fromTip * fromTip : radius * radius - along * along;
    if (squared < -1e-10) return result;
    const auto radial = toTip / distance;
    const auto across = nativeAxis(0) ^ radial;
    const double height = std::sqrt(std::max(0.0, squared));
    double nearest = 1e100;
    for (double sign : {-1.0, 1.0}) {
        const auto base = MPoint::origin + radial * along + across * (sign * height);
        const auto aim = tip - base;
        if (aim.length() < 1e-12) continue;
        const auto direction = aim.normal();
        // 向きの反転と、Arrow3Dの追加面が半径内側へ立つ交点を除く。
        if (direction * site.along < -1e-10) continue;
        if ((direction ^ site.side) * (base - MPoint::origin) < -1e-10) continue;
        const double rawAngle = std::atan2(base.y, base.z);
        for (int turn = -1; turn <= 1; ++turn) {
            const double candidate = rawAngle + turn * 2.0 * kPi;
            if (candidate < start - 1e-10 || candidate > end + 1e-10) continue;
            const double angle = std::clamp(candidate, start, end);
            const double inward = first ? angle - start : end - angle;
            if (inward > kPi + 1e-10) continue;
            if (inward >= nearest) continue;
            nearest = inward;
            result.site.along = direction;
            // 共通のPart生成側がOffsetを一度だけ適用するよう基準位置を戻す。
            result.site.endpoint = tip - direction * settings.partOffset;
            result.base = base;
            result.angle = angle;
            result.onArc = true;
        }
    }
    return result;
}
