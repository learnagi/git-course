---
title: "文件操作"
slug: "file-operations"
sequence: 2
description: "学习 Git 的基本文件操作，包括添加、提交、查看状态等"
is_published: true
estimated_minutes: 20
---

# Git 文件操作

Git 的日常使用主要涉及文件的添加、提交和管理。本节将介绍 Git 的基本文件操作命令。

## 文件状态

Git 中的文件有四种状态：
1. Untracked（未跟踪）
2. Unmodified（未修改）
3. Modified（已修改）
4. Staged（已暂存）

## 基本操作命令

### 查看状态

1. 查看仓库状态：
   ```bash
   git status
   ```

2. 查看简短状态：
   ```bash
   git status -s
   ```

### 添加文件

1. 添加单个文件：
   ```bash
   git add filename.txt
   ```

2. 添加多个文件：
   ```bash
   git add file1.txt file2.txt
   ```

3. 添加所有文件：
   ```bash
   git add .
   ```

4. 交互式添加：
   ```bash
   git add -i
   ```

### 提交更改

1. 提交已暂存的更改：
   ```bash
   git commit -m "提交说明"
   ```

2. 跳过暂存直接提交：
   ```bash
   git commit -am "提交说明"
   ```

3. 修改最后一次提交：
   ```bash
   git commit --amend
   ```

### 查看差异

1. 查看工作区和暂存区的差异：
   ```bash
   git diff
   ```

2. 查看暂存区和最新提交的差异：
   ```bash
   git diff --staged
   ```

3. 查看两个提交之间的差异：
   ```bash
   git diff commit1 commit2
   ```

## 文件忽略

### .gitignore 文件

1. 创建 .gitignore 文件：
   ```bash
   touch .gitignore
   ```

2. 常用的忽略规则：
   ```gitignore
   # 忽略所有 .log 文件
   *.log
   
   # 忽略 build 目录
   build/
   
   # 忽略特定文件
   config.ini
   ```

### 忽略已跟踪的文件

1. 从仓库中删除文件但保留本地文件：
   ```bash
   git rm --cached filename
   ```

## 移动和删除文件

### 移动文件

1. 重命名文件：
   ```bash
   git mv old_name new_name
   ```

2. 移动文件到其他目录：
   ```bash
   git mv file.txt directory/
   ```

### 删除文件

1. 从仓库和工作区删除：
   ```bash
   git rm filename
   ```

2. 仅从仓库删除：
   ```bash
   git rm --cached filename
   ```

## 查看历史

1. 查看提交历史：
   ```bash
   git log
   ```

2. 查看简化的历史：
   ```bash
   git log --oneline
   ```

3. 查看文件的修改历史：
   ```bash
   git log -p filename
   ```

## 最佳实践

1. **提交规范**
   - 写清晰的提交信息
   - 保持提交的原子性
   - 及时提交更改

2. **文件组织**
   - 合理使用 .gitignore
   - 保持文件结构清晰
   - 避免提交不必要的文件

3. **差异检查**
   - 提交前检查差异
   - 确保提交内容符合预期
   - 适时使用 git status

## 常见问题

1. 文件未被跟踪
   - 检查 .gitignore 规则
   - 确认文件路径正确
   - 验证 git add 命令

2. 提交失败
   - 检查文件状态
   - 确认用户配置
   - 验证提交信息

3. 文件差异不符合预期
   - 检查工作区状态
   - 确认暂存区内容
   - 验证文件编码

## 练习

1. 创建并提交新文件
2. 修改文件并查看差异
3. 使用 .gitignore 忽略文件
4. 练习移动和删除文件 