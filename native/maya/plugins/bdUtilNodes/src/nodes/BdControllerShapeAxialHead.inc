// 中心または先端と寸法を保ち、帯幅を受ける断面を円弧へ向ける。
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
    const auto tip = site.endpoint + site.along * settings.partOffset;
    AxialHeadPlacement result{site, centered ? tip : tip - site.along * length, first ? start : end, false};
    // 負の長さは接線方向の反転を保つ。円弧内側へ回すと正の長さと同形になる。
    if (site.attached || length <= 1e-12 || end - start <= 1e-12) return result;
    if (settings.partShape >= 3 && settings.wideWidth > 0.1 * std::abs(partWidth(settings)) + 1e-10) return result;
    // 均等なSphereは中心まわりの回転で形が変わらないため、元の姿勢を保つ。
    if (settings.partShape == 8 && std::abs(partLength(settings) - std::abs(partWidth(settings))) < 1e-12) return result;

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
