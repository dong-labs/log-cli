"""add 命令"""

import typer
from datetime import datetime
from ..db import get_connection
from ..config import DEFAULT_GROUP
from dong import json_output, ValidationError
from rich.console import Console

console = Console()


@json_output
def add(
    content: str = typer.Argument(..., help="日志内容"),
    group: str = typer.Option(DEFAULT_GROUP, "--group", "-g", help="分组"),
):
    """记录日志"""
    if not content or not content.strip():
        raise ValidationError("content", "日志内容不能为空")

    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")

    try:
        cursor.execute(
            """
            INSERT INTO logs (content, log_group, date, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (content.strip(), group, date_str, now.isoformat()),
        )
        conn.commit()

        log_id = cursor.lastrowid
        return {
            "id": log_id,
            "content": content,
            "group": group,
            "date": date_str,
            "created_at": now.isoformat(),
        }
    finally:
        conn.close()
