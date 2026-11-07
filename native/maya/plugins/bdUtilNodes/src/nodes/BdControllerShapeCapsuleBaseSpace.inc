// 主軸両端を半球の中心へ写し、横断面の平均半径を半球の主軸半径にする。
bool isCapsuleBody(const ShapeSettings& settings) {
    return outlinePresetIndex(settings.shape) == kCapsuleOutline;
}

double bodyAxisRadius(const ShapeSettings& settings, bool plus) {
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    const unsigned int normal = settings.axisSwap ? 1 : 0;
    const auto radius = [&](unsigned int axis) {
        const unsigned int ordinal = axis < normal ? axis : axis - 1;
        const double scale = settings.baseSpaceFaceScale[normal * 4 + (plus ? 0 : 2) + ordinal];
        return std::abs(span[axis]) * 0.5 * std::abs(scale);
    };
    if (outlinePresetIndex(settings.shape) == kDiamondArrowOutline) return radius(2);
    return (radius(settings.axisSwap ? 0 : 1) + radius(2)) * 0.5;
}

double capsuleBodyCoordinate(double coordinate, const ShapeSettings& settings) {
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    const double minus = settings.baseSpaceMinus[axis], plus = settings.baseSpacePlus[axis];
    const double direction = plus >= minus ? 1.0 : -1.0;
    const double cylinder = std::clamp(coordinate, -0.5, 0.5);
    return (minus + plus) * 0.5 + cylinder * (plus - minus) +
        (coordinate - cylinder) * direction * (2.0 * bodyAxisRadius(settings, coordinate >= 0.0));
}

MPoint capsuleProjectedPoint(const MPoint& point) {
    const MPoint center(std::clamp(point.x, -0.5, 0.5), 0, 0);
    const auto normal = point - center;
    const double length = normal.length();
    return length == 0.0 ? point : center + normal * (0.5 / length);
}

std::vector<MPoint> capsuleProfilePoints() {
    std::vector<MPoint> result;
    for (double sign : {1.0, -1.0}) {
        const double first = sign > 0.0 ? -kPi * 0.5 : kPi * 0.5;
        for (unsigned int i = 0; i <= kCircleSegments / 2; ++i) {
            const double angle = first + 2.0 * kPi * i / kCircleSegments;
            result.emplace_back(sign * 0.5 + 0.5 * std::cos(angle), 0.5 * std::sin(angle), 0);
        }
        result.emplace_back(0, sign * 0.5, 0);
    }
    result.push_back(result.front());
    return result;
}
