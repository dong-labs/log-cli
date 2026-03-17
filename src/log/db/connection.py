"""数据库连接管理模块

继承 dong.db.Database，提供 log-cli 专用数据库访问。
"""

import sqlite3
from typing import Iterator
from contextlib import contextmanager

from dong.db import Database as DongDatabase


class LogDatabase(DongDatabase):
    """
    记咚咚数据库类

    继承自 dong.db.Database，提供统一的数据库管理。

    数据库路径: ~/.log/log.db
    """

    @classmethod
    def get_name(cls) -> str:
        """返回 CLI 名称"""
        return "log"


# ============================================================================
# 兼容性函数：保持向后兼容
# ============================================================================

def get_connection(db_path=None):
    """获取数据库连接（兼容函数）

    Args:
        db_path: 已忽略，保留仅为兼容性

    Returns:
        sqlite3.Connection: 数据库连接对象
    """
    return LogDatabase.get_connection()


def close_connection() -> None:
    """关闭数据库连接（兼容函数）"""
    LogDatabase.close_connection()


@contextmanager
def get_cursor() -> Iterator[sqlite3.Cursor]:
    """获取数据库游标的上下文管理器（兼容函数）

    Yields:
        sqlite3.Cursor: 游标对象
    """
    with LogDatabase.get_cursor() as cur:
        yield cur


def get_db_path():
    """获取数据库文件路径（兼容函数）

    Returns:
        Path: 数据库文件路径
    """
    return LogDatabase.get_db_path()
