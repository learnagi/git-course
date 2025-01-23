---
title: "Git 撤销操作"
slug: "undo-operations"
description: "学习 Git 中的各种撤销操作，包括撤销修改、重置提交、变基操作等高级撤销功能"
author: "Git Fun <support@git.fun>"
status: "published"
created_at: "2024-01-01"
updated_at: "2024-01-01"
estimated_minutes: 30
---

# Git 撤销操作

在使用 Git 过程中，经常需要撤销某些操作。本节将介绍 Git 中的各种撤销命令及其使用场景，帮助你更好地管理代码版本。

## 学习目标

- 掌握工作区和暂存区的撤销操作
- 学习如何修改和撤销提交
- 理解储藏（stash）的使用方法
- 掌握高级撤销操作（变基、重置等）

## 基础撤销操作

### 撤销工作区修改

1. 撤销单个文件的修改：
   ```bash
   # 使用传统语法
   git checkout -- filename
   
   # 使用新语法（推荐）
   git restore filename
   ```

2. 撤销所有未暂存的修改：
   ```bash
   # 使用传统语法
   git checkout .
   
   # 使用新语法（推荐）
   git restore .
   ```

### 撤销暂存区修改

1. 取消暂存单个文件：
   ```bash
   # 使用传统语法
   git reset HEAD filename
   
   # 使用新语法（推荐）
   git restore --staged filename
   ```

2. 取消所有暂存：
   ```bash
   # 使用传统语法
   git reset HEAD
   
   # 使用新语法（推荐）
   git restore --staged .
   ```

## 提交操作

### 修改最后一次提交

1. 修改提交信息：
   ```bash
   git commit --amend -m "新的提交信息"
   ```

2. 追加文件到最后一次提交：
   ```bash
   git add forgotten_file
   git commit --amend --no-edit
   ```

### 撤销提交

1. 创建新的提交来撤销之前的提交：
   ```bash
   git revert <commit-hash>
   ```

2. 重置到指定提交：
   ```bash
   # 保留工作区修改
   git reset --soft <commit-hash>
   
   # 重置工作区和暂存区
   git reset --hard <commit-hash>
   ```

## 储藏操作

### 储藏更改

1. 储藏当前更改：
   ```bash
   # 快速储藏
   git stash
   
   # 储藏时添加说明
   git stash save "修改说明"
   
   # 储藏未跟踪的文件
   git stash -u
   ```

### 管理储藏

1. 查看储藏列表：
   ```bash
   git stash list
   ```

2. 应用储藏：
   ```bash
   # 应用最近的储藏
   git stash apply
   
   # 应用指定的储藏
   git stash apply stash@{2}
   
   # 应用并删除储藏
   git stash pop
   ```

3. 删除储藏：
   ```bash
   # 删除最近的储藏
   git stash drop
   
   # 删除指定的储藏
   git stash drop stash@{2}
   
   # 清除所有储藏
   git stash clear
   ```

## 高级撤销操作

### 交互式变基

1. 开始交互式变基：
   ```bash
   git rebase -i <commit-hash>
   ```

2. 常用变基命令：
   - pick：保留提交
   - reword：修改提交信息
   - edit：修改提交内容
   - squash：合并到上一个提交
   - drop：删除提交

### 清理操作

1. 清理未跟踪的文件：
   ```bash
   # 查看将被删除的文件
   git clean -n
   
   # 删除未跟踪的文件
   git clean -f
   
   # 删除未跟踪的文件和目录
   git clean -fd
   ```

## 最佳实践

1. **谨慎使用强制操作**
   - 使用 `--hard` 前要确认
   - 重要操作前先备份
   - 避免强制推送到远程

2. **合理使用储藏**
   - 切换分支前储藏更改
   - 为储藏添加清晰说明
   - 及时清理不需要的储藏

3. **变基注意事项**
   - 不要变基已推送的提交
   - 在变基前创建备份分支
   - 解决冲突后继续变基