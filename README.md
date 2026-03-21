# 记咚咚

> 📝 记录日常日志的 CLI 工具

[![Version](https://img.shields.io/badge/Version-0.6.0-blue.svg)](https://pypi.org/project/dong-log/)

## 安装

```bash
pipx install dong-log
```

## 快速开始

```bash
# 初始化
dong-log init

# 记录日志
dong-log add "完成了思咚咚 CLI 开发" --group work
dong-log add "看了部电影" --group life
dong-log add "独立产品上线" --group indie

# 列出日志
dong-log list
dong-log list --today
dong-log list --week
dong-log list --group work

# 查看分组
dong-log groups

# 设置默认分组
dong-log set-default work
```

## 命令

| 命令 | 说明 |
|------|------|
| `dong-log init` | 初始化数据库 |
| `dong-log add` | 记录日志 |
| `dong-log list` | 列出日志 |
| `dong-log get` | 获取详情 |
| `dong-log delete` | 删除日志 |
| `dong-log groups` | 查看分组 |
| `dong-log set-default` | 设置默认分组 |

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
~/.dong/log/log.db
```

## License

MIT
