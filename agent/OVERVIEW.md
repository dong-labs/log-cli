# OVERVIEW.md - 项目概览

## 项目信息

| 项目 | 值 |
|------|-----|
| 中文名 | 记咚咚 |
| 英文 ID | log |
| CLI 命令 | jlog |
| 数据目录 | ~/.log/ |
| 项目目录 | repos/dong-labs/log/ |

## 核心功能

| 功能 | 命令 |
|------|------|
| 初始化 | jlog init |
| 记录 | jlog add |
| 列出 | jlog list |
| 获取详情 | jlog get |
| 删除 | jlog delete |
| 查看分组 | jlog groups |
| 设置默认分组 | jlog set-default |

## 分组

| 分组 | 说明 |
|------|------|
| default | 默认 |
| work | 工作 |
| life | 生活 |
| indie | 独立开发 |
| family | 家人 |

## 数据结构

```sql
logs (
    id, content, group,
    created_at, updated_at
)
```

## 开发状态

- [x] CLI 核心
- [x] Agent workspace
- [x] dong-core v0.2.0 重构
- [ ] 测试覆盖
- [ ] PyPI 发布

---

*📔 每一天都值得被记住*
