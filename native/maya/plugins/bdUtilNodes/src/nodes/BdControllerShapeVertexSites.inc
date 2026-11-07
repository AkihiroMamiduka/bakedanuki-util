bool optionVertexPartOutline(short outline) {
    switch (outline) {
        case 6: case 79: case 24: case 25: case 36: case 39: case 41: case 43: case kCapsuleOutline:
        case kDiamondArrowOutline: case kCubeArrowOutline: case kSphereArrowOutline:
            return true;
        default:
            return false;
    }
}

std::vector<MPoint> optionPlanarVertexPoints(short outline) {
    if (outline == 6) {
        return {MPoint(0, 0.5, 0), MPoint(0, -0.37, -0.5), MPoint(0, -0.37, 0.5)};
    }
    if (outline == 79) {
        return {MPoint(0, 0.5, 0), MPoint(0, 0, -0.5),
            MPoint(0, -0.5, 0), MPoint(0, 0, 0.5)};
    }
    if (outline == kDiamondArrowOutline) {
        return {MPoint(0.5, 0, 0), MPoint(0, 0, -0.5), MPoint(-0.5, 0, 0), MPoint(0, 0, 0.5)};
    }
    return {};
}

std::vector<OptionSite> optionVertexPartSites(const ShapeSettings& settings) {
    const short outline = outlinePresetIndex(settings.shape);
    std::vector<OptionSite> sites;
    const auto points = optionPlanarVertexPoints(outline);
    if (outline == kDiamondArrowOutline) {
        sites.push_back({points[0], nativeAxis(0), -nativeAxis(2), true});
        sites.push_back({points[1], -nativeAxis(2), -nativeAxis(0), true});
        sites.push_back({points[2], -nativeAxis(0), nativeAxis(2), true});
        sites.push_back({points[3], nativeAxis(2), nativeAxis(0), true});
    } else if (!points.empty()) {
        for (std::size_t index = 0; index < points.size(); ++index) {
            const auto& point = points[index];
            auto previous = points[(index + points.size() - 1) % points.size()] - point;
            auto next = points[(index + 1) % points.size()] - point;
            previous.normalize();
            next.normalize();
            // 隣接辺の単位方向から、頂角の外向き二等分線を求める。
            auto along = -(previous + next);
            along.normalize();
            sites.push_back({point, along, nativeAxis(outline == kDiamondArrowOutline ? 1 : 0) ^ along, true});
        }
    } else {
        const auto add = [&](unsigned int axis, double sign, const MPoint& point) {
            sites.push_back({point, nativeAxis(axis) * sign,
                directionalPartSide(axis) * sign, true});
        };
        if (isBulkArrowBody(settings)) {
            add(0, 1.0, MPoint(bulkArrowFront(settings), 0, 0));
            add(0, -1.0, MPoint(-bulkArrowRearRadius(settings), 0, 0));
            for (unsigned int axis : {1u, 2u}) for (double sign : {1.0, -1.0}) {
                add(axis, sign, MPoint::origin + nativeAxis(axis) * (0.5 * sign));
            }
        } else if (outline == 24 || outline == 25) {
            for (unsigned int axis = 0; axis < 3; ++axis) {
                for (double sign : {1.0, -1.0}) {
                    add(axis, sign, MPoint::origin + nativeAxis(axis) * (0.5 * sign));
                }
            }
        } else if (outline == 36 || outline == kCapsuleOutline) {
            const double extent = outline == kCapsuleOutline ? 1.0 : 0.5;
            add(0, 1.0, MPoint(extent, 0, 0));
            add(0, -1.0, MPoint(-extent, 0, 0));
        } else if (outline == 39) {
            add(0, 1.0, MPoint(0.5, 0, 0));
            add(2, 1.0, MPoint(-0.25, 0, 0.5));
            add(2, -1.0, MPoint(-0.25, 0, -0.5));
        } else if (outline == 41 || outline == 43) {
            add(0, 1.0, MPoint(0.5, 0, 0));
        }
    }
    if (settings.partType != 1 && sites.size() > 1) sites.resize(1);
    return sites;
}
