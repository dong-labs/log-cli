"""CLI 入口"""

import typer
from .config import LogConfig

app = typer.Typer(
    name="log",
    help="记咚咚 - 记录日常日志",
)

# 导入命令
from .commands import init, add, ls, get, delete, groups, set_default

app.command()(init.init)
app.command()(add.add)
app.command(name="list")(ls.list_logs)
app.command()(get.get)
app.command()(delete.delete)
app.command()(groups.groups)
app.command(name="set-default")(set_default.set_default)

def main():
    app()

if __name__ == "__main__":
    main()
