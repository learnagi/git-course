---
title: "图形界面工具"
slug: "gui-tools"
description: "了解常用的 Git 图形界面工具"
is_published: true
estimated_minutes: 20
---

# 图形界面工具

本节将介绍常用的 Git 图形界面工具，帮助你更直观地使用 Git。

## 内置图形工具

### gitk

1. 基本用法
```bash
# 启动 gitk
gitk

# 查看特定分支
gitk branch-name

# 查看所有分支
gitk --all
```

2. 高级选项
```bash
# 查看特定文件历史
gitk path/to/file

# 自定义显示
gitk --since="2 weeks ago"

# 过滤提交
gitk --author="username"
```

### git-gui

1. 基本操作
```bash
# 启动 git-gui
git gui

# 浏览器查看
git gui blame file.txt

# 创建新提交
git gui citool
```

2. 自定义配置
```bash
# 配置字体
git config gui.font "font-name 12"
```