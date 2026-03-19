"""stats 命令 - 统计日志概览"""

import typer
from datetime import datetime, timedelta
from ..db import get_connection
from dong import json_output
from rich.console import Console

console = Console()


@json_output
def stats(
    recent: str = typer.Option(None, "--recent", "-r", help="最近时间范围，如 7d, 30d"),
):
    """统计日志概览"""
    conn = get_connection()
    cursor = conn.cursor()

    # 总数统计
    cursor.execute("SELECT COUNT(*) as total FROM logs")
    total = cursor.fetchone()["total"]

    # 按分组统计
    cursor.execute("""
        SELECT log_group as 'group', COUNT(*) as count
        FROM logs
        GROUP BY log_group
        ORDER BY count DESC
    """)
    by_group = {row["group"]: row["count"] for row in cursor.fetchall()}

    # 按标签统计
    cursor.execute("SELECT tags FROM logs WHERE tags IS NOT NULL AND tags != ''")
    rows = cursor.fetchall()
    tag_counter = {}
    for row in rows:
        tags = row["tags"].split(",") if row["tags"] else []
        for tag in tags:
            tag = tag.strip()
            if tag:
                tag_counter[tag] = tag_counter.get(tag, 0) + 1

    # 最近时间范围统计
    recent_count = 0
    if recent:
        days = 0
        if recent.endswith("d"):
            days = int(recent[:-1])
        elif recent.endswith("w"):
            days = int(recent[:-1]) * 7
        elif recent.endswith("m"):
            days = int(recent[:-1]) * 30

        if days > 0:
            date_threshold = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
            cursor.execute("SELECT COUNT(*) as count FROM logs WHERE date >= ?", (date_threshold,))
            recent_count = cursor.fetchone()["count"]

    conn.close()

    result = {
        "success": True,
        "data": {
            "total": total,
            "by_group": by_group,
            "by_tag": tag_counter,
        }
    }

    if recent:
        result["data"]["recent"] = {
            "period": recent,
            "count": recent_count,
        }

    return result


if __name__ == "__main__":
    stats()
