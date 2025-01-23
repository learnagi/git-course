---
title: "高级操作命令"
slug: "advanced-operations"
sequence: 1
description: "学习 Git 的高级操作命令，包括重置、变基、cherry-pick 等"
is_published: true
estimated_minutes: 20
---

# Git 高级操作命令

本节将介绍一些 Git 的高级操作命令，这些命令能帮助你更灵活地管理代码版本。

## 重置操作

### git reset
重置当前 HEAD 到指定状态：

```bash
# 软重置 - 保留工作区和暂存区的修改
git reset --soft HEAD^

# 混合重置 - 保留工作区但清除暂存区
git reset --mixed HEAD^

# 硬重置 - 清除所有修改
git reset --hard HEAD^
```

## 变基操作

### git rebase
在另一个分支基础之上重新应用修改：

```bash
# 交互式变基
git rebase -i HEAD~3

# 将当前分支变基到 main
git rebase main
```

## Cherry-Pick

### git cherry-pick
选择性地应用提交：

```bash
# 应用单个提交
git cherry-pick <commit-hash>

# 应用多个提交
git cherry-pick <commit-hash-1> <commit-hash-2>
```