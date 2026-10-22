// 変形後の端形状を凸半空間で表し、Finの線と面を同じ境界で止める。
void trimFinEndParts(const ShapeSettings& settings, PartBuilder& fin) {
    if (!settings.part || !optionPartSupported(outlinePresetIndex(settings.shape))) return;
    trimOptionGeometry(fin.geometry, optionPartClipVolumes(settings), fin.filled);
}
