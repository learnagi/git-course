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
   ```bash
   # 定期同步主分支
   git checkout main
   git pull origin main
   git checkout feature-branch
   git rebase main
   ```

2. 经常提交小的改动
   ```bash
   # 小步提交
   git add src/feature.js
   git commit -m "feat: add user validation"
   ```

3. 写清晰的提交信息
   ```bash
   # 使用约定式提交
   git commit -m "feat: add login feature"
   git commit -m "fix: resolve user session bug"
   git commit -m "docs: update API documentation"
   ```

4. 在合并前进行代码审查
   - 创建拉取请求
   - 指定审查者
   - 解决反馈意见
   - 获得批准后合并

5. 及时删除已合并的分支
   ```bash
   # 删除已合并的本地分支
   git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
   ```

## 分支管理策略

### 分支命名规范

```bash
# 功能分支
feature/user-authentication
feature/payment-integration

# 修复分支
fix/login-error
fix/payment-timeout

# 发布分支
release/v1.0.0
release/v1.1.0
```

### 版本发布流程

1. 创建发布分支
```bash
git checkout -b release/v1.0.0 develop
```

2. 准备发布
```bash
# 更新版本号
npm version 1.0.0

# 提交更改
git commit -m "chore: bump version to 1.0.0"
```

3. 完成发布
```bash
# 合并到主分支
git checkout main
git merge release/v1.0.0

# 打标签
git tag -a v1.0.0 -m "Release version 1.0.0"
```