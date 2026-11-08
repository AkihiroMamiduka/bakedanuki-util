// 矢印本体の後端部分を一定長に保ち、前側だけを指定した先端へ伸ばす。
bool isArrowBody(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    return outline == 25 || outline == 39 || outline == kDiamondArrowOutline || outline == kArrowSpatialOutline;
}

double arrowBodyFixedLength(const ShapeSettings& settings) {
    return outlinePresetIndex(settings.shape) == 39 ? 0.25 : 0.5;
}

double arrowBodyCoordinate(double coordinate, const ShapeSettings& settings) {
    const unsigned int axis = settings.axisSwap ? 1 : 0;
    const double minus = settings.baseSpaceMinus[axis];
    const double plus = settings.baseSpacePlus[axis];
    const double direction = plus >= minus ? 1.0 : -1.0;
    if (isNotchedArrowBody(settings)) {
        const double relative = coordinate + 0.25;
        const double scale = relative < 0.0 ? arrowRearDepth(settings) / 0.25 : bulkArrowFront(settings) / 0.75;
        return minus + direction * relative * scale;
    }
    if (isCenteredArrowBody(settings)) {
        const double depth = coordinate < 0.0 ? bodyAxisRadius(settings, false) : bulkArrowFront(settings);
        return minus + direction * coordinate * (2.0 * depth);
    }
    const double fixedLength = arrowBodyFixedLength(settings);
    const double shoulder = -0.5 + fixedLength;
    if (coordinate <= shoulder) return minus + direction * (coordinate + 0.5);
    const double joint = minus + direction * fixedLength;
    return joint + (coordinate - shoulder) * ((plus - joint) / (0.5 - shoulder));
}

MPoint bodyBaseSpacePoint(const MPoint& point, const ShapeSettings& settings) {
    const bool swap = settings.axisSwap && !isColorOutline(outlinePresetIndex(settings.shape));
    auto result = baseSpacePoint(presetOrientedPoint(point, settings.shape, swap), settings);
    if (isArrowBody(settings)) result[settings.axisSwap ? 1 : 0] = arrowBodyCoordinate(point.x, settings);
    if (isCapsuleBody(settings)) result[settings.axisSwap ? 1 : 0] = capsuleBodyCoordinate(point.x, settings);
    if (isBulkArrowBody(settings)) result[settings.axisSwap ? 1 : 0] = bulkArrowBodyCoordinate(point.x, settings);
    return result;
}
