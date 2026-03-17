"""get 命令"""

import typer
from ..db import get_connection
from dong import json_output, NotFoundError
from rich.console import Console
from rich.panel import Panel

console = Console()


@json_output
def get(
    log_id: int = typer.Argument(..., help="日志 ID"),
):
    """获取日志详情"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content, log_group as 'group', date, created_at FROM logs WHERE id = ?", (log_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise NotFoundError("Log", log_id, message=f"未找到 ID 为 {log_id} 的日志")

    return dict(row)
