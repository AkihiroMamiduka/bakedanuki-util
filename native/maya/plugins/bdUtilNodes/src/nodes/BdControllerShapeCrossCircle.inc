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

bool crossAxialSolidTouchesJoin(const ShapeSettings& settings, bool top) {
    if (!settings.part || settings.partType == 2 || settings.partShape < 6) return false;
    auto filled = settings;
    filled.fill = true;
    const auto heads = makeOptionHeads(filled);
    MBoundingBox bounds;
    bool hasPoints = false;
    for (const auto& part : heads.geometry.fillParts) for (const auto& point : part.triangles) {
        bounds.expand(point);
        hasPoints = true;
    }
    for (const auto& stroke : heads.geometry.strokes) for (const auto& point : stroke) {
        bounds.expand(point);
        hasPoints = true;
    }
    if (!hasPoints) return false;
    const double halfWidth = settings.wideWidth * 0.5;
    const double height = crossAxialJoinHeight(settings);
    return bounds.max().x >= -halfWidth && bounds.min().x <= halfWidth &&
        bounds.max().z >= -halfWidth && bounds.min().z <= halfWidth &&
        (top ? bounds.max().y >= height && bounds.min().y <= 0.5 :
            bounds.min().y <= -height && bounds.max().y >= -0.5);
}

void joinCrossAxialPlane(PartGeometry& geometry, double height) {
    WideEndArrowGeometry flat;
    std::vector<OptionClipVolume> adjoining;
    const auto onPlane = [&](const MPoint& point) { return std::abs(point.y - height) < 1e-9; };
    for (auto& part : geometry.fillParts) {
        MPointArray remaining;
        for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
            const std::array<MPoint, 3> face = {part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]};
            const auto count = std::count_if(face.begin(), face.end(), onPlane);
            if (count == 3 && !part.singleSided) flat.triangles.push_back(face);
            else {
                for (const auto& point : face) remaining.append(point);
                if (count >= 2) {
                    auto volume = optionPlanarVolume({face[0], face[1], face[2]});
                    if (!volume.empty()) adjoining.push_back(std::move(volume));
                }
            }
        }
        part.triangles = std::move(remaining);
    }
    if (flat.triangles.empty()) return;
    PartBuilder joined(true);
    appendPartTriangleUnion(joined, flat, {MPoint(0, height, 0), nativeAxis(0), nativeAxis(2)});
    std::vector<OptionClipVolume> flatVolumes;
    for (const auto& part : joined.geometry.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        auto volume = optionPlanarVolume({part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]});
        if (!volume.empty()) flatVolumes.push_back(std::move(volume));
    }
    // 平面内部の旧輪郭と、曲面へつながる平面の縁は描かない。
    PartBuilder flatLines(false), otherLines(false);
    for (std::size_t index = 0; index < geometry.strokes.size(); ++index) {
        const auto& stroke = geometry.strokes[index];
        for (unsigned int i = 1; i < stroke.length(); ++i) {
            auto& lines = onPlane(stroke[i - 1]) && onPlane(stroke[i]) ? flatLines : otherLines;
            lines.stroke({stroke[i - 1], stroke[i]}, geometry.strokeStyles[index]);
        }
    }
    trimOptionStrokes(flatLines.geometry, flatVolumes);
    geometry.strokes = std::move(otherLines.geometry.strokes);
    geometry.strokeStyles = std::move(otherLines.geometry.strokeStyles);
    mergeOptionGeometry(geometry, std::move(flatLines.geometry));
    trimOptionStrokes(joined.geometry, adjoining);
    mergeOptionGeometry(geometry, std::move(joined.geometry));
}

bool makeCrossCircleGeometry(const ShapeSettings& settings, PartGeometry& geometry) {
    ShapeSettings first = settings;
    first.shape = partPreset(crossCircleBaseOutline(outlinePresetIndex(settings.shape)));
    ShapeSettings second = first;
    // AtEndとAtApexは代表円だけに付け、AtEndsは両方の円弧端へ付ける。
    second.part = settings.part && settings.partType == 1;
    if (outlinePresetIndex(settings.shape) == 115 && settings.wideWidth > 1e-12 && settings.wideWidth < 1.0 - 1e-12) {
        const double sweep = std::clamp(settings.circleAngle, 0.0, 2.0 * kPi);
        const double alpha = std::asin(settings.wideWidth);
        first.crossAxialJoinTop = second.crossAxialJoinTop = sweep >= 2.0 * alpha - 1e-12 &&
            !crossAxialSolidTouchesJoin(first, true) && !crossAxialSolidTouchesJoin(second, true);
        first.crossAxialJoinBottom = second.crossAxialJoinBottom = sweep >= 2.0 * kPi - 1e-12 &&
            !crossAxialSolidTouchesJoin(first, false) && !crossAxialSolidTouchesJoin(second, false);
    }
    PartGeometry other;
    makeOptionShapeGeometry(first, geometry);
    makeOptionShapeGeometry(second, other);
    rotateCrossCircleGeometry(other);
    const bool joinedWrap = optionAxialWrapped(first) &&
        (first.crossAxialJoinTop || first.crossAxialJoinBottom);
    // 巻き付けた主面の共面部分は後段で合成し、細い三角形の反復差分を避ける。
    if (settings.part && !joinedWrap) {
        const auto firstVolumes = optionPartClipVolumes(first);
        const auto secondVolumes = crossCircleClipVolumes(optionPartClipVolumes(second));
        // もう一方の端形状の内部を除き、一致した面は代表円側へ一度だけ残す。
        const bool faces = settings.fill || first.crossAxialJoinTop || first.crossAxialJoinBottom;
        trimOptionGeometry(geometry, secondVolumes, faces, true);
        trimOptionGeometry(other, firstVolumes, faces);
    }
    mergeOptionGeometry(geometry, std::move(other));
    if (first.crossAxialJoinTop) joinCrossAxialPlane(geometry, crossAxialJoinHeight(first));
    if (first.crossAxialJoinBottom) joinCrossAxialPlane(geometry, -crossAxialJoinHeight(first));
    if (!settings.fill) geometry.fillParts.clear();
    return true;
}
