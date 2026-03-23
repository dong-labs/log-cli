"""CLI 入口"""

import typer
from rich.console import Console
from dong import json_output
from . import __version__

console = Console()

app = typer.Typer(
    name="dong-log",
    help="记咚咚 - 记录日常日志",
    no_args_is_help=True,
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """版本号回调函数"""
    if value:
        console.print(f"dong-log {__version__}")
        raise typer.Exit()


@app.callback()
def global_options(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="显示版本号",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """全局选项"""
    pass


@app.command()
@json_output
def init():
    """初始化数据库"""
    from .commands import init
    return init.init()


@app.command()
@json_output
def add(
    content: str = typer.Argument(..., help="日志内容"),
    group: str = typer.Option(None, "--group", "-g", help="分组"),
    tags: str = typer.Option(None, "--tags", "-t", help="标签（逗号分隔）"),
):
    """记录日志"""
    from .commands import add
    return add.add(content=content, group=group, tags=tags)


@app.command()
@json_output
def list(
    limit: int = typer.Option(20, "--limit", "-l", help="返回数量"),
    group: str = typer.Option(None, "--group", "-g", help="按分组筛选"),
    tag: str = typer.Option(None, "--tag", "-t", help="按标签筛选"),
):
    """列出日志"""
    from .commands import ls
    return ls.list_logs(limit=limit, group=group, tag=tag)


@app.command()
@json_output
def get(
    log_id: int = typer.Argument(..., help="日志 ID"),
):
    """获取日志详情"""
    from .commands import get
    return get.get(log_id=log_id)


@app.command()
@json_output
def delete(
    log_id: int = typer.Argument(..., help="日志 ID"),
):
    """删除日志"""
    from .commands import delete
    return delete.delete(log_id=log_id)


@app.command()
@json_output
def groups():
    """列出所有分组"""
    from .commands import groups
    return groups.groups()


@app.command()
@json_output
def set_default(
    group: str = typer.Argument(..., help="默认分组名"),
):
    """设置默认分组"""
    from .commands import set_default
    return set_default.set_default(group=group)


@app.command()
@json_output
def search(
    keyword: str = typer.Argument(..., help="搜索关键词"),
    limit: int = typer.Option(20, "--limit", "-l", help="返回数量"),
):
    """搜索日志"""
    from .commands import search
    return search.search(keyword=keyword, limit=limit)


@app.command()
@json_output
def stats():
    """统计信息"""
    from .commands import stats
    return stats.stats()


@app.command()
@json_output
def tags():
    """列出所有标签"""
    from .commands import tags
    return tags.tags()


@app.command()
def export(
    output: str = typer.Option("log.json", "-o", "--output", help="输出文件"),
    format: str = typer.Option("json", "-f", "--format", help="格式: json/md"),
):
    """导出数据"""
    from .commands import export
    export.export(output=output, format=format)


@app.command(name="import")
def import_data(
    file: str = typer.Option(..., "-f", "--file", help="导入文件"),
    merge: bool = typer.Option(False, "--merge", help="合并模式"),
    dry_run: bool = typer.Option(False, "--dry-run", help="预览模式"),
):
    """导入数据"""
    from .commands import data_import
    data_import.import_data(file=file, merge=merge, dry_run=dry_run)


if __name__ == "__main__":
    app()
