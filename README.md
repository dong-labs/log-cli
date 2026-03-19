# 记咚咚

> 📝 记录日常日志的 CLI 工具

## 安装

```bash
pipx install dong-log
```

## 快速开始

```bash
# 初始化
jlog init

# 记录日志
jlog add "完成了思咚咚 CLI 开发" --group work
jlog add "看了部电影" --group life
jlog add "独立产品上线" --group indie

# 列出日志
jlog list
jlog list --today
jlog list --week
jlog list --group work

# 查看分组
jlog groups

# 设置默认分组
jlog set-default work
```

## 命令

| 命令 | 说明 |
|------|------|
| `jlog init` | 初始化数据库 |
| `jlog add` | 记录日志 |
| `jlog list` | 列出日志 |
| `jlog get` | 获取详情 |
| `jlog delete` | 删除日志 |
| `jlog groups` | 查看分组 |
| `jlog set-default` | 设置默认分组 |

## 分组

| 分组 | 说明 |
|------|------|
| default | 默认 |
| work | 工作 |
| life | 生活 |
| indie | 独立开发 |
| family | 家人 |

## 数据存储

```
~/.log/log.db
```

## License

MIT
