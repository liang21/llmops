#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/20 00:16
@Author  : terminator
@File    : config.py
"""
import os
from typing import Any

from loguru import logger

from config.default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    """
    :rtype: Any
    """
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str) -> bool:
    """

    :param key:
    :rtype: bool
    """
    value = _get_env(key)
    return value.lower() == 'true' if value is not None else False


class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = _get_env('WTF_CSRF_ENABLED')

        # 数据库
        self.SQLALCHEMY_DATABASE_URI = _get_env('SQLALCHEMY_DATABASE_URI')
        logger.info(f"SQLALCHEMY_DATABASE_URI: {self.SQLALCHEMY_DATABASE_URI}")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size': int(_get_env('SQLALCHEMY_POOL_SIZE')),
            'pool_recycle': int(_get_env('SQLALCHEMY_POOL_RECYCLE')),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env('SQLALCHEMY_ECHO')
