# coding: utf-8

import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


class LogLevel:
    """`logging` の主要なログレベルをまとめた定数。"""

    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """名前に対応するロガーを取得し、未設定なら出力先を構成する。

    Args:
        name: ロガー名。通常は `__name__` を渡す。
        level: 初回構成時のログレベル。既定値は `logging.INFO`。

    Returns:
        同名のロガー。既存のハンドラーがあれば設定は変更しない。
    """
    # 再読み込み時は既存のハンドラーを使い、出力先の重複を防ぐ。
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    # 初回だけログレベルと出力形式を設定する。
    logger.setLevel(level)
    logger.propagate = False

    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setLevel(level)

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
