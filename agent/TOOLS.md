# TOOLS.md - 工具箱

我的核心工具是 `jlog` CLI。

## 命令列表

### 初始化

```bash
jlog init
```

### 记录日志

```bash
jlog add "完成了思咚咚 CLI 开发" --group work
jlog add "看了部电影" --group life
jlog add "独立产品上线" --group indie
```

### 列出日志

```bash
jlog list              # 列出最近日志
jlog list --today      # 今天的日志
jlog list --week       # 本周的日志
jlog list --group work # 按分组筛选
```

### 获取详情

```bash
jlog get 123           # 获取 ID 为 123 的日志详情
```

### 删除日志

```bash
jlog delete 123        # 删除日志
```

### 查看分组

```bash
jlog groups            # 列出所有分组
```

### 设置默认分组

```bash
jlog set-default work  # 设置默认分组为 work
```

## JSON 输出

所有命令支持 `--json` 参数，方便解析：

```bash
jlog add "xxx" --json
jlog list --json
```

---

*📔 工具在手，日志我有*
