---
title: "IDE 集成"
slug: "ide-integration"
description: "学习在各种 IDE 中使用 Git"
is_published: true
estimated_minutes: 25
---

# IDE 集成

本节将详细介绍主流 IDE 中的 Git 集成功能，帮助你在开发过程中更高效地使用 Git。

## Visual Studio Code

### 基本设置

1. Git 配置
```json
{
  "git.enabled": true,
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true
}
```

2. 快捷键设置
```json
{
  "key": "ctrl+shift+g",
  "command": "workbench.view.scm"
}
```

### 扩展推荐

1. GitLens
- 行内 blame 信息
- 文件历史
- 分支比较
- 代码导航

2. Git History
- 可视化历史
- 文件历史
- 分支比较
- 搜索功能

3. Git Graph
- 分支图表
- 提交详情
- 分支操作
- 标签管理

### 工作流集成

1. 源代码管理