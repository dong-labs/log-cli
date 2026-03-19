"""search 命令 - 全文搜索日志"""

import typer
from ..db import get_connection
from dong import json_output
from rich.console import Console

console = Console()


@json_output
def search(
    query: str = typer.Argument(..., help="搜索关键词"),
    limit: int = typer.Option(10, "--limit", "-l", help="返回数量"),
):
    """全文搜索日志内容"""
    conn = get_connection()
    cursor = conn.cursor()

    search_pattern = f"%{query}%"
    cursor.execute(
        """
        SELECT id, content, log_group as 'group', date, created_at
        FROM logs
        WHERE content LIKE ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (search_pattern, limit),
    )
    rows = cursor.fetchall()
    conn.close()

    logs = [dict(row) for row in rows]
    return {
        "success": True,
        "data": {
            "query": query,
            "total": len(logs),
            "items": logs,
        }
    }


if __name__ == "__main__":
    search()
