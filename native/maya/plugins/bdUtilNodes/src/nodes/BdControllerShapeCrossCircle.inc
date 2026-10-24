// 共通の上方向を保ち、既存の円弧とその端形状を直交する二面へ配置する。
MPoint crossCirclePoint(const MPoint& point) {
    return MPoint(point.z, point.y, -point.x);
}

std::vector<OptionClipVolume> crossCircleClipVolumes(std::vector<OptionClipVolume> volumes) {
    for (auto& volume : volumes) for (auto& plane : volume) {
        plane.normal = MVector(plane.normal.z, plane.normal.y, -plane.normal.x);
    }
    return volumes;
}

void rotateCrossCircleGeometry(PartGeometry& geometry) {
    for (auto& stroke : geometry.strokes) for (auto& point : stroke) point = crossCirclePoint(point);
    for (auto& part : geometry.fillParts) for (auto& point : part.triangles) point = crossCirclePoint(point);
}

bool makeCrossCircleGeometry(const ShapeSettings& settings, PartGeometry& geometry) {
    ShapeSettings first = settings;
    first.shape = partPreset(crossCircleBaseOutline(outlinePresetIndex(settings.shape)));
    ShapeSettings second = first;
    // AtEndとAtApexは代表円だけに付け、AtEndsは両方の円弧端へ付ける。
    second.part = settings.part && settings.partType == 1;
    PartGeometry other;
    makeOptionShapeGeometry(first, geometry);
    makeOptionShapeGeometry(second, other);
    rotateCrossCircleGeometry(other);
    if (settings.part) {
        const auto firstVolumes = optionPartClipVolumes(first);
        const auto secondVolumes = crossCircleClipVolumes(optionPartClipVolumes(second));
        // もう一方の端形状の内部を除き、一致した面は代表円側へ一度だけ残す。
        trimOptionGeometry(geometry, secondVolumes, settings.fill, true);
        trimOptionGeometry(other, firstVolumes, settings.fill);
    }
    mergeOptionGeometry(geometry, std::move(other));
    return true;
}
