// 生成用の形状から、描画時に再利用する座標と不変の接続情報を分離する。
struct BdControllerShapeDrawGeometry {
    struct StrokeInfo {
        StrokeStyle style = StrokeStyle::Normal;
        bool lineList = false;
        MUintArray lineIndices;
    };
    struct TrianglePlane {
        MVector normal;
        double offset;
        double normalLength;
    };
    struct FillInfo {
        StrokeStyle style = StrokeStyle::Normal;
        bool marker = false;
        bool singleSided = false;
        MUintArray triangleIndices;
        MUintArray reversedTriangleIndices;
        std::vector<TrianglePlane> planes;
    };
    struct Topology {
        std::vector<StrokeInfo> strokes;
        std::vector<FillInfo> fillParts;
        bool singleSided = false;
    };
    std::shared_ptr<const Topology> topology;
    std::vector<MPointArray> strokes;
    std::vector<MPointArray> fillParts;
    MMatrix animationMatrix;
    bool reversed = false;

    const MUintArray& fillIndices(std::size_t partIndex) const {
        const auto& info = topology->fillParts[partIndex];
        return reversed && info.singleSided
            ? info.reversedTriangleIndices : info.triangleIndices;
    }
};
