"""ls 命令"""

import typer
from datetime import datetime, timedelta
from ..db import get_connection
from ..config import DEFAULT_LIMIT
from dong import json_output
from rich.console import Console
from rich.table import Table

console = Console()


@json_output
def list_logs(
    limit: int = typer.Option(DEFAULT_LIMIT, "--limit", "-l", help="显示数量"),
    today: bool = typer.Option(False, "--today", help="只显示今天的"),
    week: bool = typer.Option(False, "--week", help="只显示本周的"),
    group: str = typer.Option(None, "--group", "-g", help="按分组筛选"),
    tag: str = typer.Option(None, "--tag", "-t", help="按标签筛选"),
):
    """列出日志"""
    conn = get_connection()
    cursor = conn.cursor()

    conditions = []
    params = []

    if today:
        conditions.append("date = ?")
        params.append(datetime.now().strftime("%Y-%m-%d"))

    if week:
        week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        conditions.append("date >= ?")
        params.append(week_ago)

    if group:
        conditions.append("log_group = ?")
        params.append(group)

    if tag:
        conditions.append("tags LIKE ?")
        params.append(f"%{tag}%")

    where_clause = " AND ".join(conditions) if conditions else "1=1"
    params.append(limit)

    query = f"""
        SELECT id, content, log_group as 'group', date, tags, created_at
        FROM logs
        WHERE {where_clause}
        ORDER BY created_at DESC
        LIMIT ?
    """

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    logs = [dict(row) for row in rows]
    return {"logs": logs, "total": len(logs)}
