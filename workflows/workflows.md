---
title: "Git 工作流"
slug: "workflows"
description: "掌握 Git 工作流的基本概念和常见模式"
is_published: true
estimated_minutes: 45
---

# Git 工作流

本节将介绍 Git 工作流的基本概念和常见模式，帮助你理解如何在团队中有效使用 Git。

## 工作流基础

### 什么是工作流？

工作流是团队在使用版本控制系统时遵循的一套规范和流程，它定义了如何组织分支、何时合并代码以及如何进行代码审查等。

### 常见工作流模式

1. 集中式工作流
最简单的工作流模式，所有开发都在主分支上进行：

```bash
# 获取最新代码
git pull origin main

# 提交修改
git commit -m "feature: add new functionality"

# 推送到远程
git push origin main
```

2. 功能分支工作流
每个新功能都在专门的分支上开发：

```bash
# 创建功能分支
git checkout -b feature/new-feature

# 开发完成后合并到主分支
git checkout main
git merge feature/new-feature
```

### 工作流最佳实践

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

## GitFlow 工作流

### 基本概念

1. 分支结构
- main/master：主分支
- develop：开发分支
- feature/*：特性分支
- release/*：发布分支
- hotfix/*：热修复分支
- bugfix/*：bug修复分支

2. 工作流程
```bash
# 初始化 GitFlow
git flow init

# 查看分支
git branch -a
```

### 特性开发

1. 创建特性
```bash
# 使用 git-flow
git flow feature start user-auth

# 传统方式
git checkout -b feature/user-auth develop
```

2. 完成特性
```bash
# 使用 git-flow
git flow feature finish user-auth

# 传统方式
git checkout develop
git merge --no-ff feature/user-auth
git branch -d feature/user-auth
```

### 发布管理

1. 创建发布
```bash
# 使用 git-flow
git flow release start 1.0.0

# 传统方式
git checkout -b release/1.0.0 develop
```

2. 完成发布
```bash
# 使用 git-flow
git flow release finish 1.0.0

# 传统方式
git checkout main
git merge release/1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
```

## 主干开发工作流

### 核心原则

1. 主要特点
- 短生命周期分支
- 频繁集成
- 持续部署
- 特性开关

2. 工作模式
```bash
# 主干开发
git checkout main
git pull
git commit -m "feat: add feature"
git push origin main
```

### 开发流程

1. 短期分支
```bash
# 创建特性分支
git checkout -b feature/quick-fix

# 完成开发
git commit -m "feat: implement quick fix"

# 合并回主干
git checkout main
git merge feature/quick-fix
```

2. 特性开关
```javascript
// 特性开关
const FEATURES = {
  newFeature: process.env.ENABLE_NEW_FEATURE === 'true'
};

if (FEATURES.newFeature) {
  // 新特性代码
} else {
  // 旧代码
}
```

### 持续集成

1. CI 配置
```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Build and test
      run: |
        npm install
        npm test
```

2. 部署流程
```bash
# 自动部署
git push origin main

# 触发 CI/CD 流程
# 1. 运行测试
# 2. 构建应用
# 3. 自动部署
```