# coding: utf-8

# builtin
import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


class LogLevel:
    """``logging`` の主要なログレベルをまとめた定数。"""

    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """名前に対応するロガーを取得し、未設定なら出力先を構成する。

    Args:
        name: ロガー名。通常は ``__name__`` を渡す。
        level: 初回構成時のログレベル。既定値は ``logging.INFO``。

    Returns:
        同名のロガー。既存のハンドラーがあれば設定は変更しない。
    """
    # logger を取得する
    logger = logging.getLogger(name)

    # 既に handler が設定されていれば再設定しない（reload 対策）
    if logger.handlers:
        return logger

    # レベルをセット
    logger.setLevel(level)
    # 親 logger に伝播させない（reload 対策）
    logger.propagate = False

    # handler をセット
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setLevel(level)

    # Formatter をセット（レベルに応じて詳細度を変える）
    if level == logging.DEBUG:
        formatter = (
            "%(name)s:"
            + " %(lineno)04d"
            + " [%(funcName)s]"
            + " [%(levelname)s]: %(message)s"
        )
    else:
        formatter = "[%(levelname)s]: %(message)s"
    handler.setFormatter(logging.Formatter(formatter))

    return logger
