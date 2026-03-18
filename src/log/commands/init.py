"""init 命令"""

import typer
from rich.console import Console
from pathlib import Path
from ..db import init_database, get_db_path
from ..config import APP_NAME, VERSION
from dong import json_output, DongError

console = Console()


@json_output
def init(
    yes: bool = typer.Option(False, "--yes", "-y", help="不提示，直接初始化"),
):
    """初始化数据库"""
    db_path = get_db_path()

    if db_path.exists():
        if not yes:
            confirm = typer.confirm(f"{db_path} 已存在，是否覆盖？", default=False)
            if not confirm:
                return {"cancelled": True, "message": "已取消初始化"}

    try:
        init_database()
        return {
            "message": f"{APP_NAME} 初始化成功",
            "db_path": str(db_path),
            "version": VERSION
        }
    except Exception as e:
        raise DongError("INIT_FAILED", str(e))
