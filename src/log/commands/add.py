"""add 命令"""

import typer
from datetime import datetime
from ..db import get_connection
from ..config import DEFAULT_GROUP
from dong import json_output, ValidationError
from rich.console import Console

console = Console()


def _is_option_info(value):
    """检查是否是 Typer OptionInfo 对象"""
    return hasattr(value, '__class__') and value.__class__.__name__ == 'OptionInfo'


@json_output
def add(
    content: str = typer.Argument(..., help="日志内容"),
    group: str = typer.Option(DEFAULT_GROUP, "--group", "-g", help="分组"),
    tags: str = typer.Option(None, "--tags", "-t", help="标签，多个用逗号分隔"),
):
    """记录日志"""
    if not content or not content.strip():
        raise ValidationError("content", "日志内容不能为空")

    # 过滤 OptionInfo 对象
    if _is_option_info(group):
        group = DEFAULT_GROUP
    if _is_option_info(tags):
        tags = None

    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")

    # 处理标签
    tags_str = ""
    if tags:
        tags_list = [t.strip() for t in tags.split(",") if t.strip()]
        tags_str = ",".join(tags_list)

    try:
        cursor.execute(
            """
            INSERT INTO logs (content, log_group, date, tags, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (content.strip(), group, date_str, tags_str, now.isoformat()),
        )
        conn.commit()

        log_id = cursor.lastrowid
        return {
            "id": log_id,
            "content": content,
            "group": group,
            "date": date_str,
            "tags": tags_str,
            "created_at": now.isoformat(),
        }
    finally:
        conn.close()
