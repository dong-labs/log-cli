# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Project: log CLI

**记咚咚 (Log)** - 记录日常日志的 CLI 工具

### 核心设计原则

1. **Agent First, Human Second** - 所有命令设计优先考虑 AI 调用
2. **极简主义** - 只做核心功能，不做复杂报表
3. **确定性输出** - 所有命令返回 JSON
4. **边界清晰** - 明确功能边界

### 技术栈

- **语言**: Python 3.11+
- **CLI 框架**: Typer
- **数据库**: SQLite (单文件 `~/.log/log.db`)
- **输出**: 所有命令返回 JSON

### 安装与运行

```bash
# 开发模式安装
pip install -e .

# 运行
jlog init
jlog ls
```

### 项目边界

**做的：** 记录日志、搜索历史
**不做的：** 不做图表、不做分析
