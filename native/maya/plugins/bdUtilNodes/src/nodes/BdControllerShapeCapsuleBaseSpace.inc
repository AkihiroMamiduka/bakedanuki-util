// 主軸両端を半球の中心へ写し、横断面の平均半径を半球の主軸半径にする。
bool isCapsuleBody(const ShapeSettings& settings) {
    return outlinePresetIndex(settings.shape) == kCapsuleOutline;
}

double bodyAxisRadius(const ShapeSettings& settings, bool plus) {
    const auto span = settings.baseSpacePlus - settings.baseSpaceMinus;
    const short outline = outlinePresetIndex(settings.shape);
    if (outline == 39 || outline == kDiamondArrowOutline || outline == kSquareArrowPlanarOutline ||
        outline == kCircleArrowPlanarOutline) return std::abs(span.z) * 0.5;
    const unsigned int main = settings.axisSwap ? 1 : 0, transverse = settings.axisSwap ? 0 : 1;
    double first = std::abs(span[transverse]), second = std::abs(span.z);
    if (isCapsuleBody(settings)) {
        const unsigned int side = main * 4 + (plus ? 0 : 2);
        first *= std::abs(settings.baseSpaceFaceScale[side + (transverse < main ? transverse : transverse - 1)]);
        second *= std::abs(settings.baseSpaceFaceScale[side + 1]);
    }
    return (first + second) * 0.25;
}

double capsuleCageCoordinate(double canonicalX) {
    return std::clamp(canonicalX, -0.5, 0.5);
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
