---
title: "GitFlow 工作流"
slug: "gitflow"
description: "深入学习 GitFlow 工作流的使用方法"
is_published: true
estimated_minutes: 60
---

# GitFlow 工作流

GitFlow 是一个非常流行的 Git 分支管理模型，它定义了一套严格的分支使用规范。

## GitFlow 分支类型

1. master/main 分支
   - 存储正式发布的版本
   - 每个提交都应该打上版本标签

2. develop 分支
   - 主要的开发分支
   - 包含最新的开发特性

3. feature 分支
   - 用于开发新功能
   - 从 develop 分支创建
   - 完成后合并回 develop 分支

4. release 分支
   - 准备发布新版本
   - 用于修复 bug 和准备发布文档
   - 完成后同时合并到 master 和 develop

5. hotfix 分支
   - 用于修复生产环境的紧急问题
   - 从 master 分支创建
   - 完成后同时合并到 master 和 develop

## GitFlow 工作流程

### 开发新功能

```bash
# 从 develop 创建 feature 分支
git checkout -b feature/new-feature develop

# 开发完成后合并回 develop
git checkout develop
git merge --no-ff feature/new-feature
git branch -d feature/new-feature
```

### 准备发布版本

```bash
# 从 develop 创建 release 分支
git checkout -b release/1.0.0 develop

# 完成后合并到 master 和 develop
git checkout master
git merge --no-ff release/1.0.0
git tag -a 1.0.0

git checkout develop
git merge --no-ff release/1.0.0

git branch -d release/1.0.0
```

### 修复紧急问题

```bash
# 从 master 创建 hotfix 分支
git checkout -b hotfix/1.0.1 master

# 完成后合并到 master 和 develop
git checkout master
git merge --no-ff hotfix/1.0.1
git tag -a 1.0.1

git checkout develop
git merge --no-ff hotfix/1.0.1

git branch -d hotfix/1.0.1
```

## 最佳实践

1. 严格遵循分支命名规范
2. 保持 master 分支稳定
3. 及时删除已合并的功能分支
4. 使用有意义的提交信息
5. 定期同步 develop 分支的更新