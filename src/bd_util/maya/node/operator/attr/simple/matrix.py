# coding: utf-8

# maya
from maya import cmds

# self
from ...... import logger as u_logger
from .._core import Attr, Plug

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class MatrixPlug(Plug["MatrixAttr"]):
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


class MatrixAttr(Attr[MatrixPlug]):
    ATTR_TYPE = "matrix"
    PLUG_CLS = MatrixPlug
