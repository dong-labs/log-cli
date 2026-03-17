"""groups 命令"""

import typer
from ..db import get_connection
from ..config import PRESET_GROUPS
from dong import json_output
from rich.console import Console
from rich.table import Table

console = Console()


@json_output
def groups():
    """列出所有分组"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT log_group, COUNT(*) as count
        FROM logs
        GROUP BY log_group
        ORDER BY count DESC
    """)
    used_groups = {row["log_group"]: row["count"] for row in cursor.fetchall()}

    all_groups = set(PRESET_GROUPS) | set(used_groups.keys())
    conn.close()

    result = []
    for group in sorted(all_groups):
        count = used_groups.get(group, 0)
        group_type = "preset" if group in PRESET_GROUPS else "custom"
        result.append({
            "name": group,
            "count": count,
            "type": group_type
        })

    return {"groups": result, "total": len(result)}
