"""数据库 Schema 定义和版本管理

继承 dong.db.SchemaManager，管理 log-cli 的数据库 schema。
"""

from dong.db import SchemaManager

from .connection import LogDatabase


# 当前 Schema 版本
SCHEMA_VERSION = "1.0.0"


class LogSchemaManager(SchemaManager):
    """
    记咚咚 Schema 管理器

    继承自 dong.db.SchemaManager，管理 log 的数据库 schema。
    """

    def __init__(self):
        super().__init__(
            db_class=LogDatabase,
            current_version=SCHEMA_VERSION
        )

    def init_schema(self) -> None:
        """初始化数据库，创建所有必要表"""
        self._create_logs_table()
        self._create_indexes()

    def _create_logs_table(self) -> None:
        """创建 logs 表"""
        with LogDatabase.get_cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    log_group TEXT DEFAULT 'default',
                    date TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def _create_indexes(self) -> None:
        """创建索引"""
        with LogDatabase.get_cursor() as cur:
            cur.execute("CREATE INDEX IF NOT EXISTS idx_logs_group ON logs(log_group)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_logs_date ON logs(date)")


# ============================================================================
# 兼容性函数：保持向后兼容
# ============================================================================

def get_schema_version() -> str | None:
    """获取当前数据库的 Schema 版本"""
    return LogSchemaManager().get_stored_version()


def set_schema_version(version: str) -> None:
    """设置 Schema 版本"""
    LogDatabase.set_meta(LogSchemaManager.VERSION_KEY, version)


def is_initialized() -> bool:
    """检查数据库是否已初始化"""
    return LogSchemaManager().is_initialized()


def init_database() -> None:
    """初始化数据库，创建所有必要表"""
    schema = LogSchemaManager()

    if not schema.is_initialized():
        schema.initialize()
    elif schema.requires_migration():
        stored, current = schema.get_version_delta()
        raise ValueError(
            f"Database version mismatch: expected {current}, got {stored}. "
            f"Please run migration or use --force to reinitialize."
        )


# 保留旧的 init_database 函数签名用于兼容
def init_database_old(db_path=None) -> None:
    """初始化数据库表结构（兼容旧版本）

    Args:
        db_path: 已忽略，保留仅为兼容性
    """
    init_database()
