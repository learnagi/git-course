---
title: "Git 工作流实践"
slug: "workflow-practice"
description: "通过实践练习掌握不同的 Git 工作流"
is_published: true
estimated_minutes: 90
---

# Git 工作流实践

本节将通过实际练习帮助你掌握不同的 Git 工作流。

## 练习一：集中式工作流

### 场景
你正在参与一个小型项目，团队使用集中式工作流。

### 任务
1. 克隆远程仓库
2. 在主分支上进行修改
3. 解决可能的冲突
4. 推送修改到远程仓库

### 步骤
```bash
# 克隆仓库
git clone <repository-url>

# 修改文件并提交
git add .
git commit -m "feat: add new feature"

# 获取最新更新并处理冲突
git pull origin main

# 推送修改
git push origin main
```

## 练习二：功能分支工作流

### 场景
你需要开发一个新功能，使用功能分支工作流。

### 任务
1. 创建功能分支
2. 在分支上开发功能
3. 提交 Pull Request
4. 合并到主分支

### 步骤
```bash
# 创建并切换到功能分支
git checkout -b feature/new-feature

# 开发功能并提交
git add .
git commit -m "feat: implement new feature"

# 推送功能分支
git push origin feature/new-feature

# 合并到主分支
git checkout main
git merge feature/new-feature
```

## 练习三：GitFlow 工作流

### 场景
你在一个使用 GitFlow 的项目中工作。

### 任务
1. 从 develop 分支创建功能分支
2. 完成功能开发
3. 创建发布分支
4. 完成发布流程

### 步骤
```bash
# 创建功能分支
git checkout -b feature/new-feature develop

# 完成功能开发
git add .
git commit -m "feat: add new feature"

# 合并到 develop
git checkout develop
git merge --no-ff feature/new-feature

# 创建发布分支
git checkout -b release/1.0.0 develop

# 完成发布
git checkout main
git merge --no-ff release/1.0.0
git tag -a v1.0.0
```

## 练习四：主干开发工作流

### 场景
你在一个采用主干开发模式的团队工作。

### 任务
1. 在主干分支上开发
2. 使用特性开关
3. 处理合并冲突
4. 发布新版本

### 步骤
```bash
# 更新主干分支
git checkout main
git pull origin main

# 开发新功能
git add .
git commit -m "feat: add feature with toggle"

# 创建发布标签
git tag -a v1.0.0
git push origin v1.0.0
```

## 总结

通过这些练习，你应该能够：
1. 理解不同工作流的应用场景
2. 熟练使用各种 Git 命令
3. 处理常见的工作流问题
4. 选择适合团队的工作流模式