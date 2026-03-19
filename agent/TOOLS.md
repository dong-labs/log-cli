# TOOLS.md - 工具箱

我的核心工具是 `dong-log` CLI。

## 安装

```bash
pipx install log-cli
```

## 命令列表

### 初始化

```bash
dong-log init
```

### 记录日志

```bash
dong-log add "完成了思咚咚 CLI 开发" --group work
dong-log add "看了部电影" --group life
dong-log add "独立产品上线" --group indie
dong-log add "新功能发布" --tags "重要,开发"
```

### 列出日志

```bash
dong-log list              # 列出最近日志
dong-log list --today      # 今天的日志
dong-log list --week       # 本周的日志
dong-log list --group work # 按分组筛选
dong-log list --tag "重要" # 按标签筛选
```

### 搜索日志

```bash
dong-log search "inBox"    # 搜索包含 inBox 的日志
dong-log search "AI" --limit 10
```

### 获取详情

```bash
dong-log get 123           # 获取 ID 为 123 的日志详情
```

### 删除日志

```bash
dong-log delete 123        # 删除日志
```

### 查看分组

```bash
dong-log groups            # 列出所有分组
```

### 查看标签

```bash
dong-log tags              # 列出所有标签及数量
```

### 统计信息

```bash
dong-log stats             # 统计日志数量、分组分布、标签分布
dong-log stats --recent 7d # 最近 7 天的统计
```

### 设置默认分组

```bash
dong-log set-default work  # 设置默认分组为 work
```

## JSON 输出

所有命令支持 JSON 输出，方便 AI 解析：

```bash
dong-log add "xxx"
dong-log list
dong-log search "关键词"
dong-log stats
```

## 数据库

数据存储在 `~/.dong/log.db`

---

*📔 工具在手，日志我有*
