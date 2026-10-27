// 付属矢印や端形状を除く本体断面へ、通常色のフィンを一枚追加する。
#include "BdControllerShapeFinClip.inc"

void appendShapeFin(const ShapeSettings& settings, PartGeometry& geometry) {
    const short outline = outlinePresetIndex(settings.shape);
    if (isArcOutline(outline)) return;
    const bool tapered = settings.finType == 1;
    PartBuilder builder(settings.fill);
    PartPlane plane{MPoint::origin, MVector(1, 0, 0), MVector(0, 1, 0)};

    // Arrowはくぼみから先端までの矩形と、従来の傾斜した外形を切り替える。
    if (outline == 39) {
        const auto points = tapered
            ? std::vector<MPoint>{MPoint(0.5, 0, 0), MPoint(-0.25, 0.5, 0),
                                 MPoint(-0.5, 0.25, 0), MPoint(-0.25, 0, 0)}
            : std::vector<MPoint>{MPoint(-0.25, 0, 0), MPoint(-0.25, 0.5, 0),
                                 MPoint(0.5, 0.5, 0), MPoint(0.5, 0, 0)};
        std::vector<MPoint> transformed;
        for (const auto& p : points) {
            const double x = 0.125 + (p.x - 0.125) * settings.finWidthScale * settings.finSize;
            transformed.emplace_back(0.5 + (x - 0.5) * partLength(settings) + settings.partOffset,
                p.y * 2.0 * partFinHeight(settings), 0);
        }
        builder.stroke(transformed);
        builder.polygon(transformed);
    } else {
        std::vector<MPoint> section;
        const bool planarCross = outline == 4 || outline == 107 || outline == 59 || outline == 67 ||
            (outline >= 100 && outline <= 103);
        const bool crossXY = outline == 52 || outline == 105 || outline == 57 || outline == 65 ||
            (outline >= 92 && outline <= 95);
        const bool line = outline == 1 || outline == 5 || outline == 45 || outline == 52 || outline == 53 ||
            (outline >= 54 && outline <= 60) || (outline >= 62 && outline <= 67) ||
            (outline >= 69 && outline <= 78) || (outline >= 80 && outline <= 107) ||
            outline == 118 || outline == 119 || planarCross;
        const bool semicircle = outline == 30 || outline == 31 || outline == 32 || outline == 61 || outline == 68;
        const bool planar = outline == 0 || (outline >= 6 && outline <= 18) ||
            (outline >= 27 && outline <= 32) || outline == 79 || (outline >= 108 && outline <= 111) ||
            isPlanarCircleOutline(outline) || semicircle || planarCross;
        if (planar) plane = {MPoint::origin, MVector(0, 1, 0), MVector(1, 0, 0)};
        if (crossXY) plane = {MPoint::origin, MVector(1, 0, 0), MVector(0, 0, 1)};

        const bool pointed = outline == 41 || outline == 43;
        if (planar) {
            double low = -0.5;
            double high = 0.5;
            if (outline == 117) {
                low -= settings.wideWidth * 0.5;
                high += settings.wideWidth * 0.5;
            }
            if (outline == 6 || outline == 7) low = -0.37;
            if (semicircle) low = 0.0;
            section = {MPoint(low, 0, 0), MPoint(high, 0, 0)};
        } else if (outline == 118 || outline == 119) {
            const double halfWidth = settings.wideWidth * 0.5;
            const double extent = std::max(0.5, halfWidth);
            // 高さは中心軸から測り、本体内に入る付け根は後から切り取る。
            section = {MPoint(-extent, 0, 0), MPoint(extent, 0, 0)};
        } else if (line) {
            section = {MPoint(-0.5, 0, 0), MPoint(0.5, 0, 0)};
        } else if (pointed) {
            section = {MPoint(-0.5, -0.5, 0), MPoint(0.5, 0, 0), MPoint(-0.5, 0.5, 0)};
        } else if (outline == 24 || outline == 25) {
            if (outline == 25) {
                PartBuilder body(false);
                section = appendOctahedronPart(body, settings);
            } else {
                section = {MPoint(-0.5, 0, 0), MPoint(0, -0.5, 0),
                           MPoint(0.5, 0, 0), MPoint(0, 0.5, 0)};
            }
        } else if (outline == 33 ||
                   outline == 34 || outline == 35 || outline == 46 || outline == 47 || outline == 48 || outline == 49) {
            for (unsigned int i = 0; i < kCircleSegments; ++i) {
                const double angle = 2.0 * kPi * i / kCircleSegments;
                section.emplace_back(0.5 * std::cos(angle), 0.5 * std::sin(angle), 0);
            }
        } else {
            section = {MPoint(-0.5, -0.5, 0), MPoint(0.5, -0.5, 0),
                       MPoint(0.5, 0.5, 0), MPoint(-0.5, 0.5, 0)};
        }
        if (partPolygonArea(section) < 0) std::reverse(section.begin(), section.end());
        double low = section.front().x;
        double high = low;
        for (const auto& p : section) { low = std::min(low, p.x); high = std::max(high, p.x); }
        if (high - low < 1.0e-10) return;
        const std::vector<double> heights = tapered ? std::vector<double>{0.5, 0}
            : (pointed ? std::vector<double>{0, 0.5} : std::vector<double>{0.5, 0.5});
        // 線形状と平面形状はFinだけを作り、端形状の内側を後から差し引く。
        const bool separate = planar || line || optionPartSupported(outline);
        if (!separate) builder.geometry = std::move(geometry);
        const double tip = 0.5 * partLength(settings) + settings.partOffset;
        const auto outer = outline == 25
            ? std::vector<MPoint>{MPoint(-0.5, 0, 0), MPoint(tip, 0, 0)}
            : std::vector<MPoint>{MPoint(low, 0, 0), MPoint(high, 0, 0)};
        appendFinPart(builder, settings, section, outer, heights,
            outline == 25 ? (tip - 0.5) * 0.5 : (low + high) * 0.5);
        if (!separate) { geometry = std::move(builder.geometry); return; }
    }
    PartBuilder mapped(settings.fill);
    for (std::size_t i = 0; i < builder.geometry.strokes.size(); ++i) {
        Stroke stroke;
        for (const auto& point : builder.geometry.strokes[i]) stroke.append(plane.point(point));
        mapped.geometry.strokes.push_back(std::move(stroke));
        mapped.geometry.strokeStyles.push_back(StrokeStyle::Normal);
    }
    for (const auto& part : builder.geometry.fillParts) {
        MPointArray points;
        for (const auto& point : part.triangles) points.append(plane.point(point));
        mapped.geometry.fillParts.push_back({points, StrokeStyle::Normal});
    }
    if (outline == 118 || outline == 119) trimWideCross3AxisFin(settings, mapped.geometry);
    trimFinEndParts(settings, mapped);
    for (auto& stroke : mapped.geometry.strokes) {
        geometry.strokes.push_back(std::move(stroke));
        geometry.strokeStyles.push_back(StrokeStyle::Normal);
    }
    for (auto& part : mapped.geometry.fillParts) geometry.fillParts.push_back(std::move(part));
}

// 同じ平面の付属矢印にも重なる部分を差し引き、半透明の二重描画を避ける。
void removeFinFillOverlaps(PartGeometry& geometry, const std::vector<PartGeometry::FillPart>& body) {
    PartBuilder fin(true);
    for (std::size_t partIndex = 0; partIndex < geometry.fillParts.size(); ++partIndex) {
        const auto& part = geometry.fillParts[partIndex];
        const unsigned int start = partIndex < body.size() ? body[partIndex].triangles.length() : 0;
        for (unsigned int index = start; index < part.triangles.length(); index += 3) {
            const auto origin = part.triangles[index];
            const MVector side = (part.triangles[index + 1] - origin).normal();
            const MVector normal = (side ^ (part.triangles[index + 2] - origin)).normal();
            const MVector along = normal ^ side;
            const auto project = [&](const MPoint& point) {
                const auto d = point - origin;
                return MPoint(d * side, d * along, 0);
            };
            PartPolygons pieces = {{project(origin), project(part.triangles[index + 1]), project(part.triangles[index + 2])}};
            for (const auto& base : body) {
                for (unsigned int i = 0; i < base.triangles.length() && !pieces.empty(); i += 3) {
                    const auto a = base.triangles[i];
                    const auto b = base.triangles[i + 1];
                    const auto c = base.triangles[i + 2];
                    if (std::abs((a - origin) * normal) > 1e-9 || std::abs((b - origin) * normal) > 1e-9 ||
                        std::abs((c - origin) * normal) > 1e-9) continue;
                    std::vector<MPoint> clip = {project(a), project(b), project(c)};
                    const double area = partPolygonArea(clip);
                    if (std::abs(area) < 1e-12) continue;
                    if (area < 0) std::reverse(clip.begin(), clip.end());
                    PartPolygons next;
                    for (const auto& piece : pieces) {
                        for (auto& p : outsideConvexPart(piece, clip)) next.push_back(std::move(p));
                    }
                    pieces = std::move(next);
                }
            }
            const PartPlane plane{origin, side, along};
            for (const auto& piece : pieces) fin.polygon(plane.points(piece));
        }
    }
    geometry.fillParts = body;
    for (auto& part : fin.geometry.fillParts) geometry.fillParts.push_back(std::move(part));
}
