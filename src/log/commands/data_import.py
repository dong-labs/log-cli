"""导入命令

从 JSON 文件导入日志数据。
"""

import json
import typer
from rich.console import Console
from rich.table import Table
from dong.io import ImporterRegistry

from log.importer import LogImporter

console = Console()


def import_data(
    file: str = typer.Option(..., "-f", "--file", help="导入文件"),
    merge: bool = typer.Option(False, "--merge", help="合并模式（不删除现有数据）"),
    dry_run: bool = typer.Option(False, "--dry-run", help="预览模式（不实际导入）"),
):
    """
    导入日志数据
    
    Examples:
        dong-log import -f logs.json           # 替换导入
        dong-log import -f logs.json --merge   # 合并导入
        dong-log import -f logs.json --dry-run # 预览
    """
    # 确保 importer 已注册
    if not ImporterRegistry.get("log"):
        ImporterRegistry.register(LogImporter())
    
    # 读取文件
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        console.print(f"❌ 文件不存在: {file}", style="red")
        raise typer.Exit(1)
    except json.JSONDecodeError as e:
        console.print(f"❌ JSON 解析失败: {e}", style="red")
        raise typer.Exit(1)
    
    # 支持 { "log": [...] } 格式
    if isinstance(data, dict) and "log" in data:
        data = data["log"]
    
    if not isinstance(data, list):
        console.print("❌ 数据格式错误，必须是列表", style="red")
        raise typer.Exit(1)
    
    # 验证数据
    importer = ImporterRegistry.get("log")
    is_valid, error_msg = importer.validate(data)
    
    if not is_valid:
        console.print(f"❌ 数据验证失败: {error_msg}", style="red")
        raise typer.Exit(1)
    
    # 预览模式
    if dry_run:
        console.print(f"\n📋 预览: 将导入 {len(data)} 条日志\n")
        
        table = Table(show_header=True, header_style="bold")
        table.add_column("内容", style="cyan")
        table.add_column("分组")
        table.add_column("标签")
        
        for item in data[:10]:  # 只显示前 10 条
            content = item.get("content", "")[:50]
            group = item.get("group", "default")
            tags = ", ".join(item.get("tags", []))
            table.add_row(content, group, tags)
        
        console.print(table)
        
        if len(data) > 10:
            console.print(f"\n... 还有 {len(data) - 10} 条")
        
        return
    
    # 实际导入
    result = importer.import_data(data, merge=merge)
    
    # 显示结果
    mode = "合并" if merge else "替换"
    console.print(f"\n✅ 导入完成（{mode}模式）\n", style="green")
    
    table = Table(show_header=False)
    table.add_row("导入成功", str(result["imported"]), style="green")
    if result["skipped"] > 0:
        table.add_row("跳过重复", str(result["skipped"]), style="yellow")
    table.add_row("总计", str(result["total"]))
    
    console.print(table)
