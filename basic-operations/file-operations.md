---
title: "文件操作"
slug: "file-operations"
sequence: 2
description: "学习 Git 中的文件操作，包括文件状态、添加、提交等基本操作"
is_published: true
estimated_minutes: 15
---

# 文件操作

Git 的文件操作是日常工作中最常用的功能。本节将详细介绍如何在 Git 中进行文件操作。

## 文件状态

### 文件的四种状态
1. Untracked（未跟踪）
2. Unmodified（未修改）
3. Modified（已修改）
4. Staged（已暂存）

### 查看文件状态
```bash
# 查看仓库状态
git status

# 简短格式显示状态
git status -s
```