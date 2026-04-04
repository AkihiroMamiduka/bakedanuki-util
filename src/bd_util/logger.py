# coding: utf-8

# builtin
import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


class LogLevel:
    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    指定された name のloggerを取得する

    Args:
        name (str): モジュール名などの logger の名前（基本的に __name__ を渡す）
        level (int, optional): ログレベルを指定する。 Defaults to logging.INFO.

    Returns:
        logging.Logger: logger オブジェクト
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
