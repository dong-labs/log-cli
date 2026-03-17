"""delete 命令"""

import typer
from ..db import get_connection
from dong import json_output, NotFoundError
from rich.console import Console

console = Console()


@json_output
def delete(
    log_id: int = typer.Argument(..., help="日志 ID"),
    force: bool = typer.Option(False, "--force", "-f", help="强制删除，不提示"),
):
    """删除日志"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs WHERE id = ?", (log_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        raise NotFoundError("Log", log_id, message=f"未找到 ID 为 {log_id} 的日志")

    if not force:
        confirm = typer.confirm(f"确定要删除吗？\n{row['content']}")
        if not confirm:
            conn.close()
            return {"cancelled": True, "message": "已取消删除"}

    cursor.execute("DELETE FROM logs WHERE id = ?", (log_id,))
    conn.commit()
    conn.close()

    return {"deleted": True, "id": log_id}
