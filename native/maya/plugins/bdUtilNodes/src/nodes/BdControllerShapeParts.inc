// 部品の輪郭と面を同じ座標から作り、全体変形は最後に一度だけ適用する。
using PartGeometry = BdControllerShapeNode::Geometry;

double partLength(const ShapeSettings& settings) {
    return settings.partSize * settings.partLengthScale;
}

double partWidth(const ShapeSettings& settings) {
    return settings.partSize * settings.partWidthScale;
}

double partFinHeight(const ShapeSettings& settings) {
    return settings.partFinHeight * settings.partSize;
}

bool hasPartAdjustment(const ShapeSettings& settings) {
    return settings.partOffset != 0.0 || partLength(settings) != 1.0 || partWidth(settings) != 1.0;
}

short partPreset(short outline, bool filled) {
    for (short index = 0; index < static_cast<short>(kPresetInfo.size()); ++index) {
        if (kPresetInfo[index].outlineIndex == outline && kPresetInfo[index].filled == filled) return index;
    }
    return 0;
}

struct PartBuilder {
    PartGeometry geometry;
    bool filled;

    explicit PartBuilder(bool fill) : filled(fill) {}

    void stroke(const std::vector<MPoint>& points, StrokeStyle style = StrokeStyle::Normal) {
        if (points.size() < 2) return;
        Stroke stroke;
        for (const auto& point : points) stroke.append(point);
        geometry.strokes.push_back(std::move(stroke));
        geometry.strokeStyles.push_back(style);
    }

    void triangle(MPoint a, MPoint b, MPoint c, StrokeStyle style = StrokeStyle::Normal) {
        if (!filled || ((b - a) ^ (c - a)).length() < 1.0e-12) return;
        if (geometry.fillParts.empty() || geometry.fillParts.back().style != style) {
            geometry.fillParts.push_back({MPointArray(), style});
        }
        auto& points = geometry.fillParts.back().triangles;
        points.append(a);
        points.append(b);
        points.append(c);
    }

    void quad(MPoint a, MPoint b, MPoint c, MPoint d, StrokeStyle style = StrokeStyle::Normal) {
        triangle(a, b, c, style);
        triangle(a, c, d, style);
    }

    void polygon(std::vector<MPoint> points, StrokeStyle style = StrokeStyle::Normal) {
        if (!filled || points.size() < 3) return;
        for (std::size_t i = 0; i < points.size() && points.size() > 2;) {
            if ((points[i] - points[(i + 1) % points.size()]).length() < 1.0e-10) {
                points.erase(points.begin() + i);
            } else {
                ++i;
            }
        }
        if (points.size() < 3) return;
        MVector normal;
        for (std::size_t i = 1; i + 1 < points.size(); ++i) {
            normal += (points[i] - points[0]) ^ (points[i + 1] - points[0]);
        }
        if (normal.length() < 1.0e-12) return;
        normal.normalize();
        const auto cross = [&](std::size_t a, std::size_t b, std::size_t c) {
            return ((points[b] - points[a]) ^ (points[c] - points[a])) * normal;
        };
        std::vector<std::size_t> remaining;
        for (std::size_t i = 0; i < points.size(); ++i) remaining.push_back(i);
        while (remaining.size() > 3) {
            bool found = false;
            for (std::size_t i = 0; i < remaining.size(); ++i) {
                const auto a = remaining[(i + remaining.size() - 1) % remaining.size()];
                const auto b = remaining[i];
                const auto c = remaining[(i + 1) % remaining.size()];
                if (cross(a, b, c) <= 1.0e-12) continue;
                bool contains = false;
                for (auto p : remaining) {
                    if (p == a || p == b || p == c) continue;
                    if (cross(a, b, p) > -1.0e-12 && cross(b, c, p) > -1.0e-12 &&
                        cross(c, a, p) > -1.0e-12) {
                        contains = true;
                        break;
                    }
                }
                if (contains) continue;
                triangle(points[a], points[b], points[c], style);
                remaining.erase(remaining.begin() + i);
                found = true;
                break;
            }
            if (!found) {
                // 同一直線上に残った頂点は面積を持たない。
                const auto it = std::find_if(remaining.begin(), remaining.end(), [&](std::size_t b) {
                    const auto i = static_cast<std::size_t>(std::find(remaining.begin(), remaining.end(), b) - remaining.begin());
                    return std::abs(cross(remaining[(i + remaining.size() - 1) % remaining.size()], b,
                        remaining[(i + 1) % remaining.size()])) < 1.0e-12;
                });
                if (it == remaining.end()) break;
                remaining.erase(it);
            }
        }
        if (remaining.size() == 3) triangle(points[remaining[0]], points[remaining[1]], points[remaining[2]], style);
    }

    void body(short outline, StrokeStyle style = StrokeStyle::Normal) {
        ShapeSettings base;
        base.shape = partPreset(outline, filled);
        const ShapeTransform transform(base);
        std::vector<StrokeStyle> styles;
        auto strokes = makeStrokes(transform, styles);
        for (std::size_t i = 0; i < strokes.size(); ++i) {
            geometry.strokes.push_back(std::move(strokes[i]));
            geometry.strokeStyles.push_back(style == StrokeStyle::Normal ? styles[i] : style);
        }
        for (auto& part : makeFillParts(transform)) {
            if (style != StrokeStyle::Normal) part.style = style;
            geometry.fillParts.push_back(std::move(part));
        }
    }
};

struct PartPlane {
    MPoint origin;
    MVector side;
    MVector along;

    MPoint point(const MPoint& p) const { return origin + side * p.x + along * p.y; }
    std::vector<MPoint> points(const std::vector<MPoint>& points) const {
        std::vector<MPoint> result;
        for (const auto& p : points) result.push_back(point(p));
        return result;
    }
};

using PartPolygons = std::vector<std::vector<MPoint>>;

PartPolygons outsideConvexPart(std::vector<MPoint> polygon, const std::vector<MPoint>& body) {
    PartPolygons result;
    for (std::size_t edge = 0; edge < body.size() && !polygon.empty(); ++edge) {
        const auto a = body[edge];
        const auto b = body[(edge + 1) % body.size()];
        const double edgeLength = (b - a).length();
        if (edgeLength < 1.0e-10) continue;
        const auto distance = [&](const MPoint& p) {
            const double value = ((b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)) / edgeLength;
            return std::abs(value) < 1.0e-10 ? 0.0 : value;
        };
        std::vector<MPoint> inside;
        std::vector<MPoint> outside;
        for (std::size_t i = 0; i < polygon.size(); ++i) {
            const auto p = polygon[i];
            const auto q = polygon[(i + 1) % polygon.size()];
            const double dp = distance(p);
            const double dq = distance(q);
            if (dp >= 0.0) inside.push_back(p);
            if (dp <= 0.0) outside.push_back(p);
            if ((dp > 0.0 && dq < 0.0) || (dp < 0.0 && dq > 0.0)) {
                const MPoint intersection = p + (q - p) * (dp / (dp - dq));
                inside.push_back(intersection);
                outside.push_back(intersection);
            }
        }
        if (outside.size() >= 3) result.push_back(std::move(outside));
        polygon = std::move(inside);
    }
    return result;
}

double partPolygonArea(const std::vector<MPoint>& polygon) {
    double area = 0.0;
    for (std::size_t i = 0; i < polygon.size(); ++i) {
        const auto& p = polygon[i];
        const auto& q = polygon[(i + 1) % polygon.size()];
        area += p.x * q.y - p.y * q.x;
    }
    return area * 0.5;
}

// 本体の断面を差し引き、半透明面が本体と二重になるのを避ける。
void appendOutsidePart(
    PartBuilder& builder, std::vector<MPoint> polygon, const std::vector<MPoint>& body,
    const PartPlane& plane
) {
    if (!builder.filled) return;
    if (body.size() < 3 || std::abs(partPolygonArea(body)) < 1.0e-12) {
        builder.polygon(plane.points(polygon));
        return;
    }
    bool convex = true;
    for (std::size_t i = 0; i < body.size(); ++i) {
        if (((body[(i + 1) % body.size()] - body[i]) ^
             (body[(i + 2) % body.size()] - body[i])).z < -1.0e-10) convex = false;
    }
    PartPolygons clips;
    if (convex) clips.push_back(body);
    else {
        PartBuilder section(true);
        section.polygon(body);
        for (const auto& part : section.geometry.fillParts) {
            for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
                std::vector<MPoint> triangle = {part.triangles[i], part.triangles[i + 1], part.triangles[i + 2]};
                if (partPolygonArea(triangle) < 0.0) std::reverse(triangle.begin(), triangle.end());
                clips.push_back(std::move(triangle));
            }
        }
    }
    PartPolygons pieces = {std::move(polygon)};
    for (const auto& clip : clips) {
        PartPolygons next;
        for (const auto& piece : pieces) {
            for (auto& outside : outsideConvexPart(piece, clip)) next.push_back(std::move(outside));
        }
        pieces = std::move(next);
    }
    for (const auto& piece : pieces) builder.polygon(plane.points(piece));
}

MPoint scaledPartPoint(const MPoint& point, const MPoint& pivot, const MVector& direction,
                       const ShapeSettings& settings) {
    const MVector delta = point - pivot;
    const double along = delta * direction;
    return pivot + direction * (along * partLength(settings) + settings.partOffset)
        + (delta - direction * along) * partWidth(settings);
}

double partSurfaceY(const std::vector<MPoint>& section, double x);
std::vector<MPoint> partRoundSection();

void appendAttachedPart(
    PartBuilder& builder, const ShapeSettings& settings, const PartPlane& plane,
    double depth, double halfWidth, double baseAlong, double crossHeight,
    const std::vector<MPoint>& section, bool round
) {
    const double width = halfWidth * partWidth(settings);
    double rootWidth = std::clamp(width, -0.5, 0.5);
    if (round && !section.empty()) {
        double low = section.front().x;
        double high = low;
        for (const auto& p : section) { low = std::min(low, p.x); high = std::max(high, p.x); }
        rootWidth = std::clamp(rootWidth, low, high);
    }
    const double rootY = round ? partSurfaceY(section, rootWidth) : 0.0;
    const double baseY = baseAlong * partLength(settings) + settings.partOffset;
    const MPoint leftRoot(rootWidth, rootY, 0.0);
    const MPoint rightRoot(-rootWidth, rootY, 0.0);
    const MPoint left(width, baseY, 0.0);
    const MPoint right(-width, baseY, 0.0);
    const MPoint tip(0.0, depth * partLength(settings) + settings.partOffset, 0.0);
    builder.stroke(plane.points({leftRoot, left, tip, right, rightRoot}));
    if (partLength(settings) != 0.0 && partWidth(settings) != 0.0) {
        appendOutsidePart(builder, {leftRoot, left, tip, right, rightRoot}, section, plane);
    }
    if (crossHeight != 0.0) {
        const MVector up = plane.along ^ plane.side;
        const PartPlane cross{plane.origin, up, plane.along};
        const MPoint base(0.0, settings.partOffset, 0.0);
        const MPoint arm(crossHeight * partWidth(settings), settings.partOffset, 0.0);
        builder.stroke(cross.points({tip, arm, base}));
        if (partLength(settings) != 0.0 && partWidth(settings) != 0.0) {
            const std::vector<MPoint> crossSection = {
                MPoint(-0.5, -1.0, 0.0), MPoint(0.5, -1.0, 0.0),
                MPoint(0.5, 0.0, 0.0), MPoint(-0.5, 0.0, 0.0),
            };
            const short outline = outlinePresetIndex(settings.shape);
            if ((outline >= 9 && outline <= 18) || outline == 29 || outline == 32) {
                builder.polygon(cross.points({base, arm, tip}));
            } else {
                appendOutsidePart(builder, {base, arm, tip}, round ? partRoundSection() : crossSection, cross);
            }
        }
    }
}

std::vector<MPoint> partRoundSection() {
    std::vector<MPoint> points;
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const double angle = 2.0 * kPi * i / kCircleSegments;
        points.emplace_back(0.5 * std::cos(angle), 0.5 * std::sin(angle) - 0.5, 0.0);
    }
    return points;
}

void appendSquareParts(PartBuilder& builder, short outline, const ShapeSettings& settings) {
    const bool four = outline >= 15;
    const bool threeD = outline == 10 || outline == 12 || outline == 14 || outline == 16 || outline == 18;
    const bool templated = outline == 17 || outline == 18;
    const PartPlane plane{MPoint::origin, MVector(0, 0, 1), MVector(0, 1, 0)};
    const std::vector<MPoint> square = {MPoint(-0.5, -0.5, 0), MPoint(0.5, -0.5, 0),
        MPoint(0.5, 0.5, 0), MPoint(-0.5, 0.5, 0)};
    builder.polygon(plane.points(square), templated ? StrokeStyle::Template : StrokeStyle::Normal);
    const std::vector<MPoint> section = {MPoint(-0.5, -1, 0), MPoint(0.5, -1, 0),
        MPoint(0.5, 0, 0), MPoint(-0.5, 0, 0)};
    for (unsigned int i = 0; i < 4; ++i) {
        const double angle = i * kPi / 2.0;
        const MVector along = plane.along * std::cos(angle) - plane.side * std::sin(angle);
        const MVector side = plane.side * std::cos(angle) + plane.along * std::sin(angle);
        const PartPlane edge{MPoint::origin + along * 0.5, side, along};
        const bool arrow = i == 0 || four;
        const double halfWidth = i == 0 ? 0.072 : 0.036;
        const double depth = i == 0 ? 0.125 : 0.0625;
        const bool outside = std::max(settings.partOffset, depth * partLength(settings) + settings.partOffset) > 0.0;
        const double root = arrow && outside ? std::min(0.5, std::abs(halfWidth * partWidth(settings))) : 0.0;
        const auto bodyStyle = templated ? StrokeStyle::Template : StrokeStyle::Normal;
        const double corner = templated ? std::max(0.15, root) : root;
        builder.stroke(edge.points({MPoint(-0.5, 0, 0), MPoint(-corner, 0, 0)}), bodyStyle);
        builder.stroke(edge.points({MPoint(corner, 0, 0), MPoint(0.5, 0, 0)}), bodyStyle);
        if (corner > root) {
            builder.stroke(edge.points({MPoint(-corner, 0, 0), MPoint(-root, 0, 0)}));
            builder.stroke(edge.points({MPoint(root, 0, 0), MPoint(corner, 0, 0)}));
        }
        if (arrow) appendAttachedPart(builder, settings, edge, i == 0 ? 0.125 : 0.0625,
            halfWidth, 0.0, threeD ? (i == 0 ? 0.0625 : 0.03125) : 0.0, section, false);
    }
    if (outline >= 11 && outline <= 14) {
        const auto style = outline >= 13 ? StrokeStyle::Template : StrokeStyle::Normal;
        builder.stroke({plane.point(MPoint(0, -0.5, 0)),
            plane.point(MPoint(0, 0.5 + 0.125 * partLength(settings) + settings.partOffset, 0))}, style);
        builder.stroke({plane.point(MPoint(-0.5, 0, 0)), plane.point(MPoint(0.5, 0, 0))}, style);
    }
}

// フィンの付け根に沿う断面。外側の輪郭だけを変形し、付け根は本体に残す。
double partSurfaceY(const std::vector<MPoint>& section, double x) {
    double y = -1.0e100;
    for (std::size_t i = 0; i < section.size(); ++i) {
        const auto a = section[i];
        const auto b = section[(i + 1) % section.size()];
        if (x < std::min(a.x, b.x) - 1.0e-9 || x > std::max(a.x, b.x) + 1.0e-9) continue;
        if (std::abs(a.x - b.x) < 1.0e-10) y = std::max(y, std::max(a.y, b.y));
        else y = std::max(y, a.y + (b.y - a.y) * (x - a.x) / (b.x - a.x));
    }
    return y;
}

void appendFinPart(PartBuilder& builder, const ShapeSettings& settings,
                   const std::vector<MPoint>& body, const std::vector<MPoint>& outer,
                   const std::vector<double>& heights, double pivotX) {
    if (partFinHeight(settings) == 0.0) return;
    double minX = body.front().x;
    double maxX = minX;
    for (const auto& p : body) { minX = std::min(minX, p.x); maxX = std::max(maxX, p.x); }
    std::vector<MPoint> free;
    for (std::size_t i = 0; i < outer.size(); ++i) {
        const double x = pivotX + (outer[i].x - pivotX) * partWidth(settings);
        const double surfaceX = std::clamp(x, minX, maxX);
        free.emplace_back(x, partSurfaceY(body, surfaceX) + heights[i] * 2.0 * partFinHeight(settings), 0);
    }
    const double firstX = std::clamp(free.front().x, minX, maxX);
    const double lastX = std::clamp(free.back().x, minX, maxX);
    const MPoint first(firstX, partSurfaceY(body, firstX), 0);
    const MPoint last(lastX, partSurfaceY(body, lastX), 0);
    for (std::size_t i = 0; i < builder.geometry.strokes.size();) {
        const auto& stroke = builder.geometry.strokes[i];
        if (stroke.length() == 2 && stroke[0].y == 0.5 && stroke[1].y == 0.5 &&
            stroke[0].z == 0.0 && stroke[1].z == 0.0 && stroke[0].x != stroke[1].x) {
            builder.geometry.strokes.erase(builder.geometry.strokes.begin() + i);
            builder.geometry.strokeStyles.erase(builder.geometry.strokeStyles.begin() + i);
            const double low = std::min(firstX, lastX);
            const double high = std::max(firstX, lastX);
            if (low > minX) builder.stroke({MPoint(minX, 0.5, 0), MPoint(low, 0.5, 0)});
            if (high < maxX) builder.stroke({MPoint(high, 0.5, 0), MPoint(maxX, 0.5, 0)});
            break;
        }
        ++i;
    }
    std::vector<MPoint> polygon = {first};
    polygon.insert(polygon.end(), free.begin(), free.end());
    polygon.push_back(last);
    builder.stroke(polygon);
    std::vector<MPoint> root;
    for (const auto& p : body) {
        if (p.x > std::min(firstX, lastX) && p.x < std::max(firstX, lastX) &&
            std::abs(p.y - partSurfaceY(body, p.x)) < 1.0e-8) root.push_back(p);
    }
    std::sort(root.begin(), root.end(), [&](const MPoint& a, const MPoint& b) {
        return firstX < lastX ? a.x > b.x : a.x < b.x;
    });
    polygon.insert(polygon.end(), root.begin(), root.end());
    if (partWidth(settings) != 0.0) {
        appendOutsidePart(builder, polygon, body, {MPoint::origin, MVector(1, 0, 0), MVector(0, 1, 0)});
    }
}

std::vector<MPoint> appendOctahedronPart(PartBuilder& builder, const ShapeSettings& settings) {
    const double width = 0.5 * partWidth(settings);
    const std::array<MPoint, 4> equator = {MPoint(0, width, 0), MPoint(0, 0, width),
        MPoint(0, -width, 0), MPoint(0, 0, -width)};
    const MPoint tip = scaledPartPoint(MPoint(1.5, 0, 0), MPoint(0.5, 0, 0), MVector(1, 0, 0), settings);
    for (std::size_t i = 0; i < equator.size(); ++i) {
        const auto next = (i + 1) % equator.size();
        builder.stroke({equator[i], tip});
        builder.stroke({equator[i], equator[next]});
        builder.stroke({equator[i], MPoint(-0.5, 0, 0)});
        builder.triangle(MPoint(-0.5, 0, 0), equator[next], equator[i]);
        if (tip.x < 0.0) builder.triangle(tip, equator[next], equator[i]);
        else builder.triangle(tip, equator[i], equator[next]);
    }
    const double extent = std::abs(width);
    return {MPoint(-0.5, 0, 0), MPoint(0, -extent, 0), tip, MPoint(0, extent, 0)};
}

// 頭部が帯や他の頭部へ重なるときは面の和集合と外周を作る。
void appendPartTriangleUnion(PartBuilder& builder, const WideEndArrowGeometry& generated, const PartPlane& plane) {
    PartPolygons occupied;
    for (const auto& face : generated.triangles) {
        std::vector<MPoint> triangle;
        for (const auto& p : face) {
            const MVector vector = p - MPoint::origin;
            triangle.emplace_back(vector * plane.side, vector * plane.along, 0);
        }
        const double area = partPolygonArea(triangle);
        if (std::abs(area) < 1.0e-12) continue;
        if (area < 0.0) std::reverse(triangle.begin(), triangle.end());
        PartPolygons pieces = {std::move(triangle)};
        for (const auto& clip : occupied) {
            PartPolygons next;
            for (const auto& piece : pieces) {
                for (auto& outside : outsideConvexPart(piece, clip)) {
                    if (std::abs(partPolygonArea(outside)) > 1.0e-12) next.push_back(std::move(outside));
                }
            }
            pieces = std::move(next);
            if (pieces.empty()) break;
        }
        for (auto& piece : pieces) occupied.push_back(std::move(piece));
    }
    std::vector<MPoint> vertices;
    for (const auto& polygon : occupied) vertices.insert(vertices.end(), polygon.begin(), polygon.end());
    std::vector<std::array<MPoint, 2>> boundary;
    for (const auto& polygon : occupied) {
        builder.polygon(plane.points(polygon));
        for (std::size_t i = 0; i < polygon.size(); ++i) {
            const auto p = polygon[i];
            const auto q = polygon[(i + 1) % polygon.size()];
            const MVector direction = q - p;
            const double squared = direction * direction;
            if (squared < 1.0e-20) continue;
            std::vector<double> cuts = {0.0, 1.0};
            for (const auto& v : vertices) {
                const double t = ((v - p) * direction) / squared;
                if (t > 1.0e-10 && t < 1.0 - 1.0e-10 &&
                    (v - (p + direction * t)).length() < 1.0e-9) cuts.push_back(t);
            }
            std::sort(cuts.begin(), cuts.end());
            cuts.erase(std::unique(cuts.begin(), cuts.end(), [](double a, double b) {
                return std::abs(a - b) < 1.0e-10;
            }), cuts.end());
            for (std::size_t cut = 0; cut + 1 < cuts.size(); ++cut) {
                const std::array<MPoint, 2> edge = {p + direction * cuts[cut], p + direction * cuts[cut + 1]};
                const auto found = std::find_if(boundary.begin(), boundary.end(), [&](const auto& other) {
                    return (edge[0] - other[1]).length() < 1.0e-9 && (edge[1] - other[0]).length() < 1.0e-9;
                });
                if (found != boundary.end()) boundary.erase(found);
                else boundary.push_back(edge);
            }
        }
    }
    if (boundary.empty()) builder.stroke(generated.outline);
    else for (const auto& edge : boundary) builder.stroke(plane.points({edge[0], edge[1]}));
}

void appendWidePartUnion(PartBuilder& builder, short outline, const ShapeSettings& settings) {
    constexpr std::array<std::array<unsigned int, 2>, 6> planes = {{{0, 1}, {1, 0}, {2, 0},
        {0, 1}, {0, 2}, {1, 2}}};
    const auto& axes = planes[outline - 62];
    appendPartTriangleUnion(builder, wideEndArrowGeometry(outline, settings),
        {MPoint::origin, nativeAxis(axes[0]), nativeAxis(axes[1])});
}

#include "BdControllerShapeSemicircle.inc"

bool makeAdjustedPartGeometry(const ShapeSettings& settings, PartGeometry& geometry) {
    const short outline = outlinePresetIndex(settings.shape);
    const bool semicircle = outline == 30 || outline == 31 || outline == 32 || outline == 61 || outline == 68;
    const bool fin = outline == 22 || outline == 23 || outline == 26 || outline == 37 ||
        outline == 38 || outline == 40 || outline == 42 || outline == 44;
    if (!hasPartAdjustment(settings) && (!semicircle || settings.partOffsetAngle == 0.0) &&
        (!fin || partFinHeight(settings) == 0.5)) return false;
    PartBuilder builder(isFilledPreset(settings.shape));
    if (semicircle) {
        if (outline == 30 && settings.partOffsetAngle == 0.0) return false;
        appendSemicircleParts(builder, outline, settings);
    } else if (outline >= 62 && outline <= 67) {
        const double depth = 0.1 * std::cos(kPi / 6.0) * partLength(settings);
        const double shoulder = 0.5 + settings.partOffset - depth;
        const double headWidth = 0.05 * std::abs(partWidth(settings));
        const bool overlap = depth < 0.0 || shoulder < 0.0 ||
            (outline >= 65 && headWidth >= shoulder);
        if (!overlap) return false;
        appendWidePartUnion(builder, outline, settings);
    } else if (outline >= 9 && outline <= 18) {
        appendSquareParts(builder, outline, settings);
    } else if (outline == 20 || outline == 21 || outline == 28 || outline == 29 ||
               outline == 34 || outline == 35 || outline == 48 || outline == 49) {
        const bool cube = outline == 20 || outline == 21;
        const bool circle = outline == 28 || outline == 29;
        const bool threeD = outline == 21 || outline == 29 || outline == 35 || outline == 49;
        builder.body(cube ? 19 : (circle ? 27 : (outline >= 48 ? 46 : 33)));
        const PartPlane plane = circle
            ? PartPlane{MPoint(0, 0.5, 0), MVector(0, 0, 1), MVector(0, 1, 0)}
            : PartPlane{MPoint(0.5, 0, 0), MVector(0, 0, -1), MVector(1, 0, 0)};
        const std::vector<MPoint> rectangle = {MPoint(-0.5, -1, 0), MPoint(0.5, -1, 0),
            MPoint(0.5, 0, 0), MPoint(-0.5, 0, 0)};
        appendAttachedPart(builder, settings, plane, 0.125, cube ? 0.072 : 0.075,
            cube ? 0.0 : -0.004903810568, threeD ? 0.0625 : 0.0, cube ? rectangle : partRoundSection(), !cube);
    } else if (outline == 39 || outline == 40 || outline == 7) {
        if (outline == 7) {
            builder.body(6);
            const MPoint tip(0, 0.5, 0);
            const MPoint base(0, -0.37, 0);
            const MPoint side(0.5, -0.37, 0);
            const auto mapped = [&](const MPoint& p) { return scaledPartPoint(p, tip, MVector(0, 1, 0), settings); };
            const std::vector<MPoint> polygon = {tip, mapped(tip), mapped(side), mapped(base), base};
            builder.stroke(polygon);
            if (partLength(settings) != 0.0 && partWidth(settings) != 0.0) builder.polygon(polygon);
        } else {
            builder.body(39);
            for (auto& stroke : builder.geometry.strokes) {
                for (unsigned int i = 0; i < stroke.length(); ++i) stroke[i] = scaledPartPoint(stroke[i], MPoint(0.5, 0, 0), MVector(1, 0, 0), settings);
            }
            if (partLength(settings) == 0.0 || partWidth(settings) == 0.0) builder.geometry.fillParts.clear();
            for (auto& part : builder.geometry.fillParts) {
                for (unsigned int i = 0; i < part.triangles.length(); ++i) part.triangles[i] = scaledPartPoint(part.triangles[i], MPoint(0.5, 0, 0), MVector(1, 0, 0), settings);
            }
            if (outline == 40 && partFinHeight(settings) != 0.0) {
                std::vector<MPoint> finPoints;
                for (const auto& point : {MPoint(0.5, 0, 0), MPoint(-0.25, 0.5, 0),
                                         MPoint(-0.5, 0.25, 0), MPoint(-0.25, 0, 0)}) {
                    finPoints.emplace_back(0.5 + (point.x - 0.5) * partLength(settings) + settings.partOffset,
                        point.y * 2.0 * partFinHeight(settings), 0);
                }
                builder.stroke(finPoints);
                builder.polygon(finPoints);
            }
        }
    } else if (outline == 22 || outline == 23 || outline == 37 || outline == 38 || outline == 42 || outline == 44) {
        const bool pointed = outline == 42 || outline == 44;
        builder.body(outline == 22 || outline == 23 ? 19 : (outline == 37 || outline == 38 ? 36 : (outline == 42 ? 41 : 43)));
        const std::vector<MPoint> body = pointed
            ? std::vector<MPoint>{MPoint(-0.5, -0.5, 0), MPoint(0.5, 0, 0), MPoint(-0.5, 0.5, 0)}
            : std::vector<MPoint>{MPoint(-0.5, -0.5, 0), MPoint(0.5, -0.5, 0), MPoint(0.5, 0.5, 0), MPoint(-0.5, 0.5, 0)};
        const bool arrow = outline == 23 || outline == 38;
        appendFinPart(builder, settings, body, {MPoint(-0.5, 0, 0), MPoint(0.5, 0, 0)},
            pointed ? std::vector<double>{0, 0.5} : (arrow ? std::vector<double>{0.5, 0} : std::vector<double>{0.5, 0.5}), 0.0);
    } else if (outline == 25 || outline == 26) {
        const auto body = appendOctahedronPart(builder, settings);
        if (outline == 26) {
            const double tip = 0.5 + partLength(settings) + settings.partOffset;
            appendFinPart(builder, settings, body,
                {MPoint(-0.5, 0.5, 0), MPoint(tip, 0.5, 0)}, {0.5, 0.5}, (tip - 0.5) * 0.5);
        }
    } else {
        return false;
    }
    geometry = std::move(builder.geometry);
    return true;
}
