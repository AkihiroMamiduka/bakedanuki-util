# coding: utf-8
from __future__ import annotations

# maya
from maya import cmds


# self
from ._core import DataTypeAttr, DataTypePlug


class DataMatrixPlug(DataTypePlug["DataMatrixAttr"]):
    def set(
        self,
        vector16: list[
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
        ],  # 4 * 4 を並列に置いた 16
    ):
        """
        matrix をセットする

        Args:
            vector16 (list[
                    float, float, float, float,
                    float, float, float, float,
                    float, float, float, float,
                    float, float, float, float,
                ]): matrix 値
        """
        cmds.setAttr(self.plug, vector16, type="matrix")


class DataMatrixAttr(DataTypeAttr[DataMatrixPlug]):
    DATA_TYPE = "matrix"
    PLUG_CLS = DataMatrixPlug
