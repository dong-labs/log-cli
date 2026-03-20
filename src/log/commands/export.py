"""导出命令

导出日志数据为 JSON/CSV/Markdown 格式。
"""

import typer
from rich.console import Console
from dong.io import ExporterRegistry

from log.exporter import LogExporter

console = Console()


def export(
    output: str = typer.Option("logs.json", "-o", "--output", help="输出文件"),
    format: str = typer.Option("json", "-f", "--format", help="格式: json/csv/md"),
):
    """
    导出日志数据
    
    Examples:
        dong-log export                      # 导出为 JSON
        dong-log export -o logs.csv -f csv   # 导出为 CSV
        dong-log export -o logs.md -f md     # 导出为 Markdown
    """
    # 确保 exporter 已注册
    if not ExporterRegistry.get("log"):
        ExporterRegistry.register(LogExporter())
    
    exporter = ExporterRegistry.get("log")
    
    # 导出
    if format == "json":
        data = exporter.to_json()
    elif format in ["csv", "csv"]:
        data = exporter.to_csv()
    elif format in ["md", "markdown"]:
        data = exporter.to_markdown()
    else:
        console.print(f"❌ 不支持的格式: {format}", style="red")
        raise typer.Exit(1)
    
    # 写入文件
    with open(output, "w", encoding="utf-8") as f:
        f.write(data)
    
    count = len(exporter.fetch_all())
    console.print(f"✅ 已导出 {count} 条日志到 {output}", style="green")
