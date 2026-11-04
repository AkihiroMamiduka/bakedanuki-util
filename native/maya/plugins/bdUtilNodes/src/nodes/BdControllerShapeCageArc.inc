// Cage上の円周を物理弧長で追い、帯と巻き付けPartで同じ局所frameを使う。
struct CageArcMetric {
    static constexpr unsigned int divisions = 1024;
    ShapeSettings settings;
    bool second = false;
    std::array<double, divisions + 1> lengths{};

    explicit CageArcMetric(const ShapeSettings& source, bool secondPlane = false)
        : settings(source), second(secondPlane) {
        for (unsigned int i = 1; i <= divisions; ++i) {
            lengths[i] = lengths[i - 1] + integral(2.0 * kPi * (i - 1) / divisions,
                2.0 * kPi * i / divisions);
        }
    }

    MPoint canonical(double theta) const {
        const auto point = baseArcPoint(theta);
        return second ? crossCirclePoint(point) : point;
    }

    MPoint basePoint(double theta) const { return cageBaseBodyPoint(canonical(theta), settings); }
    MPoint point(double theta) const { return cagePoint(basePoint(theta), settings); }

    MVector baseTangent(double theta) const {
        auto vector = MVector(0.0, 0.5 * std::cos(theta), -0.5 * std::sin(theta));
        if (second) vector = MVector(vector.z, vector.y, -vector.x);
        return cageBaseBodyPoint(MPoint::origin + vector, settings) -
            cageBaseBodyPoint(MPoint::origin, settings);
    }

    double speed(double theta) const {
        const auto vector = cageVector(basePoint(theta), baseTangent(theta), settings);
        return std::hypot(vector.x, vector.y, vector.z);
    }

    double integral(double first, double last) const {
        return (last - first) * (speed(first) + 4.0 * speed((first + last) * 0.5) + speed(last)) / 6.0;
    }

    bool degenerate() const { return !(lengths.back() > 0.0) || !std::isfinite(lengths.back()); }
    double periodScale() const { return degenerate() ? 1.0 : lengths.back() / kPi; }

    double position(double theta) const {
        if (degenerate()) return theta * 0.5;
        const double turns = std::floor(theta / (2.0 * kPi));
        const double local = theta - turns * 2.0 * kPi;
        const auto index = std::min(divisions - 1,
            static_cast<unsigned int>(local * divisions / (2.0 * kPi)));
        return turns * kPi + (lengths[index] + integral(2.0 * kPi * index / divisions, local)) /
            periodScale();
    }

    double angle(double coordinate) const {
        if (degenerate()) return coordinate * 2.0;
        const double turns = std::floor(coordinate / kPi);
        const double target = (coordinate - turns * kPi) * periodScale();
        const auto found = std::upper_bound(lengths.begin(), lengths.end(), target);
        const auto index = std::min(divisions - 1,
            static_cast<unsigned int>(std::max<std::ptrdiff_t>(0, found - lengths.begin() - 1)));
        double low = 2.0 * kPi * index / divisions;
        double high = 2.0 * kPi * (index + 1) / divisions;
        const double first = low;
        for (unsigned int step = 0; step < 40; ++step) {
            const double middle = (low + high) * 0.5;
            if (lengths[index] + integral(first, middle) < target) low = middle;
            else high = middle;
        }
        return turns * 2.0 * kPi + (low + high) * 0.5;
    }

    MVector tangent(double theta) const {
        auto vector = cageVector(basePoint(theta), baseTangent(theta), settings);
        if (std::hypot(vector.x, vector.y, vector.z) == 0.0) {
            vector = point(theta + 1e-6) - point(theta - 1e-6);
        }
        if (std::hypot(vector.x, vector.y, vector.z) == 0.0) vector = baseTangent(theta);
        if (std::hypot(vector.x, vector.y, vector.z) == 0.0) vector = MVector(0, 1, 0);
        return baseSpaceNormalized(vector);
    }

    MVector binormal(double theta) const {
        const auto center = cageBaseBodyPoint(MPoint::origin, settings);
        auto first = MPoint(0, 1, 0), last = MPoint(0, 0, 1);
        if (second) { first = crossCirclePoint(first); last = crossCirclePoint(last); }
        auto original = (cageBaseBodyPoint(first, settings) - center) ^
            (cageBaseBodyPoint(last, settings) - center);
        if (std::hypot(original.x, original.y, original.z) == 0.0) {
            original = singularBaseSpaceVector(second ? MVector(0, 0, -1) : MVector(1, 0, 0), settings);
        }
        auto vector = cageNormal(basePoint(theta), original, settings);
        const auto along = tangent(theta);
        vector -= along * (vector * along);
        if (std::hypot(vector.x, vector.y, vector.z) == 0.0) {
            vector = original - along * (original * along);
        }
        if (std::hypot(vector.x, vector.y, vector.z) == 0.0) {
            const auto helper = std::abs(along.x) < 0.9 ? MVector(1, 0, 0) : MVector(0, 1, 0);
            vector = helper - along * (helper * along);
        }
        return baseSpaceNormalized(vector);
    }

    MVector normal(double theta) const {
        auto vector = baseSpaceNormalized(binormal(theta) ^ tangent(theta));
        const auto center = cagePoint(cageBaseBodyPoint(MPoint::origin, settings), settings);
        if (vector * (point(theta) - center) < 0.0) vector = -vector;
        return vector;
    }
};
