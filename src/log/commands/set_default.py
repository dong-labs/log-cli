"""set-default 命令"""

import typer
from pathlib import Path
from ..config import DATA_DIR
from dong import json_output
from rich.console import Console

console = Console()
DEFAULT_GROUP_FILE = DATA_DIR / ".default_group"


@json_output
def set_default(group: str = typer.Argument(..., help="默认分组名称")):
    """设置默认分组"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DEFAULT_GROUP_FILE.write_text(group)
    return {"default_group": group, "message": f"已设置默认分组: {group}"}
