---
title: "工作流基础"
slug: "workflow-basics"
sequence: 1
description: "了解 Git 工作流的基本概念和常见模式"
is_published: true
estimated_minutes: 15
---

# Git 工作流基础

本节将介绍 Git 工作流的基本概念和常见模式，帮助你理解如何在团队中有效使用 Git。

## 什么是工作流？

工作流是团队在使用版本控制系统时遵循的一套规范和流程，它定义了如何组织分支、何时合并代码以及如何进行代码审查等。

## 常见工作流模式

### 集中式工作流

最简单的工作流模式，所有开发都在主分支上进行：

```bash
# 获取最新代码
git pull origin main

# 提交修改
git commit -m "feature: add new functionality"

# 推送到远程
git push origin main
```

### 功能分支工作流

每个新功能都在专门的分支上开发：

```bash
# 创建功能分支
git checkout -b feature/new-feature

# 开发完成后合并到主分支
git checkout main
git merge feature/new-feature
```

## 工作流最佳实践

1. 保持分支同步
2. 经常提交小的改动
3. 写清晰的提交信息
4. 在合并前进行代码审查
5. 及时删除已合并的分支