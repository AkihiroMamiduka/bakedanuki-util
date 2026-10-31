// 立体の表面上に帯を作り、開口へ塗り面や交差の継ぎ目線を残さない。
void clearGenericWideBodyFill(PartGeometry& geometry) {
    geometry.fillParts.erase(std::remove_if(geometry.fillParts.begin(), geometry.fillParts.end(),
        [](const auto& part) { return !part.marker; }), geometry.fillParts.end());
}

PartGeometry genericWideReferenceLines(const ShapeSettings& settings) {
    auto source = settings;
    source.fill = source.wide = source.axisSwap = false;
    source.templateLine = source.templateFill = false;
    source.part = source.fin = source.guideLine = false;
    PartGeometry geometry;
    if (!makeAdjustedPartGeometry(source, geometry)) {
        geometry.strokes = makeStrokes(ShapeTransform(source), geometry.strokeStyles);
    }
    return geometry;
}

void makeGenericWideSolidFaces(const ShapeSettings& settings, PartGeometry& geometry) {
    const auto source = genericWideReferenceFaces(settings);
    std::vector<GenericWideFace> faces;
    std::vector<OptionClipVolume> markers;
    for (const auto& part : source.fillParts) for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
        const auto a = part.triangles[i], b = part.triangles[i + 1], c = part.triangles[i + 2];
        auto normal = (b - a) ^ (c - a);
        if (normal.length() <= 1e-12) continue;
        normal.normalize();
        const double distance = (a - MPoint::origin) * normal;
        auto face = std::find_if(faces.begin(), faces.end(), [&](const auto& previous) {
            return (previous.normal - normal).length() < 1e-9 && std::abs(previous.distance - distance) < 1e-9;
        });
        if (face == faces.end()) {
            faces.push_back({normal, distance, {}, part.style, false});
            face = faces.end() - 1;
        }
        face->vertices.insert(face->vertices.end(), {a, b, c});
        if (!part.marker) { face->style = part.style; face->body = true; }
        else {
            auto volume = optionPlanarVolume({a, b, c});
            if (!volume.empty()) markers.push_back(std::move(volume));
        }
    }
    clearGenericWideBodyFill(geometry);
    PartGeometry lines;
    PartBuilder bands(settings.fill);
    for (const auto& face : faces) {
        if (!face.body) continue;
        const auto origin = face.vertices.front();
        MVector first;
        for (const auto& vertex : face.vertices) {
            if ((vertex - origin).length() > 1e-10) { first = (vertex - origin).normal(); break; }
        }
        const auto second = face.normal ^ first;
        const auto project = [&](const MPoint& point) {
            const auto delta = point - origin;
            return MPoint(delta * first, delta * second, 0);
        };
        const PartPlane plane{origin, first, second};
        std::vector<MPoint> projected;
        for (const auto& vertex : face.vertices) projected.push_back(project(vertex));
        const auto hull = genericWideConvexHull(std::move(projected));
        if (hull.size() < 3) continue;
        const auto inset = insetGenericWideFace(hull, settings.wideWidth * 0.5);
        if (!inset.empty()) {
            auto points = plane.points(inset);
            points.push_back(points.front());
            appendGenericWideStroke(lines, points, face.style);
        }
        if (!settings.fill) continue;
        // 元の三角形を使い、Cornerマーカーの切欠きや面ごとの色を保つ。
        for (const auto& part : source.fillParts) {
            if (part.marker) continue;
            for (unsigned int i = 0; i < part.triangles.length(); i += 3) {
                const auto a = part.triangles[i], b = part.triangles[i + 1], c = part.triangles[i + 2];
                if (std::abs((a - origin) * face.normal) > 1e-9 ||
                    std::abs((b - origin) * face.normal) > 1e-9 ||
                    std::abs((c - origin) * face.normal) > 1e-9) continue;
                const std::vector<MPoint> triangle = {project(a), project(b), project(c)};
                const auto pieces = inset.empty() ? PartPolygons{triangle} : outsideConvexPart(triangle, inset);
                for (const auto& piece : pieces) bands.polygon(plane.points(piece), part.style);
            }
        }
    }
    trimOptionStrokes(lines, markers);
    mergeOptionGeometry(geometry, std::move(lines));
    mergeOptionGeometry(geometry, std::move(bands.geometry));
}

double genericWideCoordinate(const MPoint& point, unsigned int axis) {
    return axis == 0 ? point.x : axis == 1 ? point.y : point.z;
}

void setGenericWideCoordinate(MPoint& point, unsigned int axis, double value) {
    if (axis == 0) point.x = value;
    else if (axis == 1) point.y = value;
    else point.z = value;
}

MPoint genericWideSpherePoint(const MVector& direction) {
    return MPoint::origin + direction.normal() * 0.5;
}

// 球面と二平面の交点を使い、色境界や帯の縁を球面から浮かせない。
MPoint genericWideSphereCut(const MPoint& a, const MPoint& b, unsigned int axis, double value, double halfBand) {
    const unsigned int first = (axis + 1) % 3, second = (axis + 2) % 3;
    for (const auto fixed : {first, second}) {
        const double previous = genericWideCoordinate(a, fixed);
        if (std::abs(previous - genericWideCoordinate(b, fixed)) > 1e-9 ||
            std::abs(std::abs(previous) - halfBand) > 1e-9) continue;
        MPoint result;
        setGenericWideCoordinate(result, axis, value);
        setGenericWideCoordinate(result, fixed, previous);
        const unsigned int remaining = 3 - axis - fixed;
        const double sign = genericWideCoordinate(a, remaining) + genericWideCoordinate(b, remaining) < 0 ? -1.0 : 1.0;
        setGenericWideCoordinate(result, remaining, sign * std::sqrt(std::max(0.0, 0.25 - value * value - previous * previous)));
        return result;
    }
    const auto normal = (a - MPoint::origin) ^ (b - MPoint::origin);
    const double u = genericWideCoordinate(MPoint::origin + normal, first);
    const double v = genericWideCoordinate(MPoint::origin + normal, second);
    const double squared = u * u + v * v;
    if (squared < 1e-20) return a;
    const double rhs = -genericWideCoordinate(MPoint::origin + normal, axis) * value;
    const double centerU = rhs * u / squared, centerV = rhs * v / squared;
    const double offset = std::sqrt(std::max(0.0, (0.25 - value * value - rhs * rhs / squared) / squared));
    MPoint positive, negative;
    setGenericWideCoordinate(positive, axis, value);
    setGenericWideCoordinate(negative, axis, value);
    setGenericWideCoordinate(positive, first, centerU - v * offset);
    setGenericWideCoordinate(positive, second, centerV + u * offset);
    setGenericWideCoordinate(negative, first, centerU + v * offset);
    setGenericWideCoordinate(negative, second, centerV - u * offset);
    const auto middle = MPoint::origin + ((a - MPoint::origin) + (b - MPoint::origin)) * 0.5;
    return (positive - middle).length() <= (negative - middle).length() ? positive : negative;
}

std::vector<MPoint> clipGenericWideSphere(const std::vector<MPoint>& polygon,
    unsigned int axis, double value, bool positive, double halfBand) {
    std::vector<MPoint> result;
    for (std::size_t i = 0; i < polygon.size(); ++i) {
        const auto a = polygon[i], b = polygon[(i + 1) % polygon.size()];
        const double first = (genericWideCoordinate(a, axis) - value) * (positive ? 1.0 : -1.0);
        const double last = (genericWideCoordinate(b, axis) - value) * (positive ? 1.0 : -1.0);
        if (first >= -1e-12) result.push_back(a);
        if ((first < -1e-12 && last > 1e-12) || (first > 1e-12 && last < -1e-12)) {
            result.push_back(genericWideSphereCut(a, b, axis, value, halfBand));
        }
    }
    return result;
}

struct GenericWideSpherePiece {
    std::vector<MPoint> points;
    unsigned int mask = 0;
};

void mergeGenericWideBandFills(PartGeometry& geometry, PartGeometry&& bands) {
    std::array<MPointArray, static_cast<std::size_t>(StrokeStyle::Count)> triangles;
    for (const auto& part : bands.fillParts) {
        auto& points = triangles[static_cast<unsigned int>(part.style)];
        for (const auto& point : part.triangles) points.append(point);
    }
    for (unsigned int style = 0; style < triangles.size(); ++style) {
        if (triangles[style].length() != 0) geometry.fillParts.push_back(
            {std::move(triangles[style]), static_cast<StrokeStyle>(style)});
    }
}

void appendGenericWideSphereTriangle(PartBuilder& bands, const std::array<MPoint, 3>& triangle,
    double halfBand, const std::array<StrokeStyle, 3>& styles) {
    std::vector<GenericWideSpherePiece> pieces = {{std::vector<MPoint>(triangle.begin(), triangle.end()), 0}};
    for (unsigned int axis = 0; axis < 3; ++axis) {
        std::vector<GenericWideSpherePiece> split;
        for (const auto& piece : pieces) {
            auto low = clipGenericWideSphere(piece.points, axis, -halfBand, false, halfBand);
            auto high = clipGenericWideSphere(piece.points, axis, halfBand, true, halfBand);
            auto middle = clipGenericWideSphere(piece.points, axis, -halfBand, true, halfBand);
            middle = clipGenericWideSphere(middle, axis, halfBand, false, halfBand);
            if (low.size() >= 3) split.push_back({std::move(low), piece.mask});
            if (high.size() >= 3) split.push_back({std::move(high), piece.mask});
            if (middle.size() >= 3) split.push_back({std::move(middle), piece.mask | (1u << axis)});
        }
        pieces = std::move(split);
    }
    for (const auto& piece : pieces) {
        if (piece.mask == 0) continue;
        unsigned int colorMask = 0;
        for (unsigned int axis = 0; axis < 3; ++axis) if ((piece.mask & (1u << axis)) != 0) {
            if (styles[axis] == StrokeStyle::AxisX) colorMask |= 1;
            else if (styles[axis] == StrokeStyle::AxisY) colorMask |= 2;
            else if (styles[axis] == StrokeStyle::AxisZ) colorMask |= 4;
        }
        constexpr std::array<StrokeStyle, 8> palette = {
            StrokeStyle::Normal, StrokeStyle::AxisX, StrokeStyle::AxisY, StrokeStyle::AxisXY,
            StrokeStyle::AxisZ, StrokeStyle::AxisXZ, StrokeStyle::AxisYZ, StrokeStyle::AxisXYZ,
        };
        const auto style = palette[colorMask];
        for (std::size_t i = 1; i + 1 < piece.points.size(); ++i) {
            bands.triangle(piece.points[0], piece.points[i], piece.points[i + 1], style);
        }
    }
}

void makeGenericWideSphereBands(const ShapeSettings& settings, PartGeometry& geometry) {
    const double angle = std::min(settings.wideWidth, kPi * 0.5);
    const double halfBand = 0.5 * std::sin(angle);
    const bool covered = halfBand >= 0.5 / std::sqrt(3.0) - 1e-12;
    const auto reference = genericWideReferenceLines(settings);
    std::array<StrokeStyle, 3> styles = {StrokeStyle::Normal, StrokeStyle::Normal, StrokeStyle::Normal};
    for (std::size_t i = 0; i < reference.strokes.size(); ++i) {
        const auto& stroke = reference.strokes[i];
        if (stroke.length() < 4) continue;
        const auto normal = ((stroke[0] - MPoint::origin) ^ (stroke[stroke.length() / 4] - MPoint::origin)).normal();
        unsigned int axis = 0;
        if (std::abs(normal.y) > std::abs(normal.x)) axis = 1;
        if (std::abs(normal.z) > std::abs(axis == 0 ? normal.x : normal.y)) axis = 2;
        styles[axis] = reference.strokeStyles[i];
    }
    clearGenericWideBodyFill(geometry);
    geometry.strokes.clear();
    geometry.strokeStyles.clear();
    if (covered && !settings.fill) {
        geometry.strokes = reference.strokes;
        geometry.strokeStyles = reference.strokeStyles;
        return;
    }
    // 小円のうち他の帯に覆われる区間を除き、和集合の外周だけを残す。
    if (!covered) for (unsigned int axis = 0; axis < 3; ++axis) {
        const unsigned int first = (axis + 1) % 3, second = (axis + 2) % 3;
        const double radius = std::sqrt(std::max(0.0, 0.25 - halfBand * halfBand));
        std::vector<double> cuts;
        for (unsigned int i = 0; i <= kCircleSegments; ++i) cuts.push_back(2.0 * kPi * i / kCircleSegments);
        const double alpha = std::asin(std::clamp(halfBand / radius, 0.0, 1.0));
        for (int quarter = 0; quarter < 4; ++quarter) {
            cuts.push_back(quarter * kPi * 0.5 + alpha);
            cuts.push_back((quarter + 1) * kPi * 0.5 - alpha);
        }
        std::sort(cuts.begin(), cuts.end());
        cuts.erase(std::unique(cuts.begin(), cuts.end(), [](double a, double b) { return std::abs(a - b) < 1e-10; }), cuts.end());
        for (double sign : {-1.0, 1.0}) for (std::size_t i = 1; i < cuts.size(); ++i) {
            const double middle = (cuts[i - 1] + cuts[i]) * 0.5;
            if (std::abs(radius * std::cos(middle)) < halfBand + 1e-10 ||
                std::abs(radius * std::sin(middle)) < halfBand + 1e-10) continue;
            const auto at = [&](double value) {
                MPoint point;
                setGenericWideCoordinate(point, axis, sign * halfBand);
                setGenericWideCoordinate(point, first, radius * std::cos(value));
                setGenericWideCoordinate(point, second, radius * std::sin(value));
                return point;
            };
            appendGenericWideStroke(geometry, {at(cuts[i - 1]), at(cuts[i])}, styles[axis]);
        }
    }
    if (!settings.fill) return;
    PartBuilder bands(true);
    constexpr unsigned int divisions = 16;
    for (double x : {-1.0, 1.0}) for (double y : {-1.0, 1.0}) for (double z : {-1.0, 1.0}) {
        const auto at = [&](unsigned int i, unsigned int j) {
            return genericWideSpherePoint(MVector(x * i, y * j, z * (divisions - i - j)));
        };
        for (unsigned int i = 0; i < divisions; ++i) for (unsigned int j = 0; j < divisions - i; ++j) {
            appendGenericWideSphereTriangle(bands, {at(i, j), at(i + 1, j), at(i, j + 1)}, halfBand, styles);
            if (i + j + 1 < divisions) appendGenericWideSphereTriangle(bands,
                {at(i + 1, j), at(i + 1, j + 1), at(i, j + 1)}, halfBand, styles);
        }
    }
    mergeGenericWideBandFills(geometry, std::move(bands.geometry));
}

MPoint genericWideCylinderPoint(double x, double angle) {
    return MPoint(x, 0.5 * std::cos(angle), 0.5 * std::sin(angle));
}

void appendGenericWideCapBand(PartBuilder& bands, double x, double halfWidth) {
    const double inner = std::max(0.0, 0.5 - halfWidth);
    for (unsigned int i = 0; i < kCircleSegments; ++i) {
        const double first = 2.0 * kPi * i / kCircleSegments, last = 2.0 * kPi * (i + 1) / kCircleSegments;
        bands.quad(genericWideCylinderPoint(x, first), genericWideCylinderPoint(x, last),
            MPoint(x, inner * std::cos(last), inner * std::sin(last)),
            MPoint(x, inner * std::cos(first), inner * std::sin(first)));
    }
}

template<typename Mapper>
void appendGenericWideMappedLine(PartGeometry& geometry, const std::vector<MPoint>& parameters,
    const Mapper& map) {
    std::vector<MPoint> points;
    for (std::size_t i = 1; i < parameters.size(); ++i) {
        const auto first = parameters[i - 1], last = parameters[i];
        const auto steps = std::max(1, static_cast<int>(std::ceil(std::abs(last.y - first.y) * kCircleSegments / (2.0 * kPi))));
        for (int step = 0; step < steps; ++step) points.push_back(map(first + (last - first) * (static_cast<double>(step) / steps)));
    }
    if (!parameters.empty()) points.push_back(map(parameters.back()));
    appendGenericWideStroke(geometry, points);
}

void makeGenericWideCylinderBands(const ShapeSettings& settings, PartGeometry& geometry) {
    const double halfWidth = settings.wideWidth * 0.5;
    const auto reference = genericWideReferenceLines(settings);
    geometry.strokes.clear();
    geometry.strokeStyles.clear();
    // 母線は帯とTemplate区間の基準として保ち、描画する元線は端円だけにする。
    for (std::size_t index = 0; index < reference.strokes.size(); ++index) {
        const auto& stroke = reference.strokes[index];
        if (stroke.length() < 2 || std::any_of(stroke.begin(), stroke.end(), [&](const MPoint& point) {
            return std::abs(point.x - stroke[0].x) > 1e-10;
        })) continue;
        geometry.strokes.push_back(stroke);
        geometry.strokeStyles.push_back(reference.strokeStyles[index]);
    }
    clearGenericWideBodyFill(geometry);
    PartBuilder bands(settings.fill);
    const double low = std::min(0.0, -0.5 + halfWidth), high = std::max(0.0, 0.5 - halfWidth);
    for (unsigned int quarter = 0; quarter < 4; ++quarter) {
        const double start = quarter * kPi * 0.5, end = (quarter + 1) * kPi * 0.5;
        const double left = start + halfWidth / 0.5, right = end - halfWidth / 0.5;
        const bool hole = low < high - 1e-12 && left < right - 1e-12;
        if (hole) appendGenericWideMappedLine(geometry,
            {MPoint(low, left, 0), MPoint(high, left, 0), MPoint(high, right, 0), MPoint(low, right, 0), MPoint(low, left, 0)},
            [](const MPoint& point) { return genericWideCylinderPoint(point.x, point.y); });
        std::vector<double> angles;
        for (unsigned int i = 0; i <= kCircleSegments / 4; ++i) angles.push_back(start + (end - start) * i / (kCircleSegments / 4));
        if (hole) { angles.push_back(left); angles.push_back(right); }
        std::sort(angles.begin(), angles.end());
        angles.erase(std::unique(angles.begin(), angles.end(), [](double a, double b) { return std::abs(a - b) < 1e-10; }), angles.end());
        for (std::size_t i = 1; i < angles.size(); ++i) {
            const double first = angles[i - 1], last = angles[i], middle = (first + last) * 0.5;
            if (!hole || middle < left || middle > right) bands.quad(genericWideCylinderPoint(-0.5, first),
                genericWideCylinderPoint(0.5, first), genericWideCylinderPoint(0.5, last), genericWideCylinderPoint(-0.5, last));
            else {
                bands.quad(genericWideCylinderPoint(-0.5, first), genericWideCylinderPoint(low, first),
                    genericWideCylinderPoint(low, last), genericWideCylinderPoint(-0.5, last));
                bands.quad(genericWideCylinderPoint(high, first), genericWideCylinderPoint(0.5, first),
                    genericWideCylinderPoint(0.5, last), genericWideCylinderPoint(high, last));
            }
        }
    }
    for (double x : {-0.5, 0.5}) {
        appendGenericWideCircle(geometry, MPoint(x, 0, 0), nativeAxis(1), nativeAxis(2), 0.5 - halfWidth);
        appendGenericWideCapBand(bands, x, halfWidth);
    }
    mergeOptionGeometry(geometry, std::move(bands.geometry));
}

void makeGenericWideConeBands(const ShapeSettings& settings, PartGeometry& geometry) {
    const double halfWidth = settings.wideWidth * 0.5;
    const double slant = std::sqrt(1.25), ratio = 0.5 / slant;
    const double sector = ratio * kPi * 0.5, outer = std::max(0.0, slant - halfWidth);
    const bool hole = outer > 1e-12 && halfWidth < outer * std::sin(sector * 0.5) - 1e-12;
    const double alpha = hole ? std::asin(halfWidth / outer) : 0.0;
    const auto reference = genericWideReferenceLines(settings);
    geometry.strokes = reference.strokes;
    geometry.strokeStyles = reference.strokeStyles;
    clearGenericWideBodyFill(geometry);
    PartBuilder bands(settings.fill);
    for (unsigned int quarter = 0; quarter < 4; ++quarter) {
        const double start = quarter * kPi * 0.5;
        const auto map = [&](double distance, double angle) {
            const double fraction = distance / slant, theta = start + angle / ratio;
            return MPoint(0.5 - fraction, 0.5 * fraction * std::cos(theta), 0.5 * fraction * std::sin(theta));
        };
        const auto lower = [&](double angle) {
            return halfWidth / std::max(1e-12, std::min(std::sin(angle), std::sin(sector - angle)));
        };
        std::vector<double> angles;
        for (unsigned int i = 0; i <= kCircleSegments / 4; ++i) angles.push_back(sector * i / (kCircleSegments / 4));
        if (hole) { angles.push_back(alpha); angles.push_back(sector * 0.5); angles.push_back(sector - alpha); }
        std::sort(angles.begin(), angles.end());
        angles.erase(std::unique(angles.begin(), angles.end(), [](double a, double b) { return std::abs(a - b) < 1e-10; }), angles.end());
        std::vector<MPoint> upperLine, lowerLine;
        for (std::size_t i = 1; i < angles.size(); ++i) {
            const double first = angles[i - 1], last = angles[i], middle = (first + last) * 0.5;
            if (!hole || middle < alpha || middle > sector - alpha) bands.triangle(MPoint(0.5, 0, 0), map(slant, first), map(slant, last));
            else {
                bands.triangle(MPoint(0.5, 0, 0), map(std::min(outer, lower(first)), first), map(std::min(outer, lower(last)), last));
                bands.quad(map(outer, first), map(slant, first), map(slant, last), map(outer, last));
                if (upperLine.empty()) {
                    upperLine.push_back(map(outer, first));
                    lowerLine.push_back(map(std::min(outer, lower(first)), first));
                }
                upperLine.push_back(map(outer, last));
                lowerLine.push_back(map(std::min(outer, lower(last)), last));
            }
        }
        if (!upperLine.empty()) {
            upperLine.insert(upperLine.end(), lowerLine.rbegin(), lowerLine.rend());
            upperLine.push_back(upperLine.front());
            appendGenericWideStroke(geometry, upperLine);
        }
    }
    appendGenericWideCircle(geometry, MPoint(-0.5, 0, 0), nativeAxis(1), nativeAxis(2), 0.5 - halfWidth);
    appendGenericWideCapBand(bands, -0.5, halfWidth);
    mergeOptionGeometry(geometry, std::move(bands.geometry));
}
