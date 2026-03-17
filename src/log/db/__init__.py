"""数据库层 - 连接管理、版本管理、工具函数"""

from .connection import (
    LogDatabase,
    get_connection,
    close_connection,
    get_cursor,
    get_db_path,
)
from .schema import (
    LogSchemaManager,
    SCHEMA_VERSION,
    get_schema_version,
    set_schema_version,
    is_initialized,
    init_database,
    init_database_old,
)

__all__ = [
    # 数据库类
    "LogDatabase",
    "LogSchemaManager",
    # 连接管理
    "get_connection",
    "close_connection",
    "get_cursor",
    "get_db_path",
    # Schema 管理
    "SCHEMA_VERSION",
    "get_schema_version",
    "set_schema_version",
    "is_initialized",
    "init_database",
    "init_database_old",
]
