"""CLI 入口"""

import typer
from .config import LogConfig

app = typer.Typer(
    name="log",
    help="记咚咚 - 记录日常日志",
)

# 导入命令
from .commands import (
    init, add, ls, get, delete, groups, 
    set_default, search, stats, tags,
    export, data_import
)

app.command()(init.init)
app.command()(add.add)
app.command(name="list")(ls.list_logs)
app.command()(get.get)
app.command()(delete.delete)
app.command()(groups.groups)
app.command(name="set-default")(set_default.set_default)
app.command()(search.search)
app.command()(stats.stats)
app.command()(tags.tags)
app.command()(export.export)
app.command(name="import")(data_import.import_data)

def main():
    app()

if __name__ == "__main__":
    main()
