"""tags 命令 - 列出所有标签及数量"""

import typer
from ..db import get_connection
from dong import json_output
from rich.console import Console
from rich.table import Table

console = Console()


@json_output
def tags():
    """列出所有标签及使用数量"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT tags FROM logs WHERE tags IS NOT NULL AND tags != ''")
    rows = cursor.fetchall()

    # 统计标签
    tag_counter = {}
    for row in rows:
        tags_list = row["tags"].split(",") if row["tags"] else []
        for tag in tags_list:
            tag = tag.strip()
            if tag:
                tag_counter[tag] = tag_counter.get(tag, 0) + 1

    conn.close()

    # 按数量排序
    sorted_tags = sorted(tag_counter.items(), key=lambda x: x[1], reverse=True)
    tags_list = [{"tag": tag, "count": count} for tag, count in sorted_tags]

    return {
        "success": True,
        "data": {
            "total_tags": len(tag_counter),
            "total_usages": sum(tag_counter.values()),
            "tags": tags_list,
        }
    }


if __name__ == "__main__":
    tags()
