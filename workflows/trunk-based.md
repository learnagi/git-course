---
title: "主干开发工作流"
slug: "trunk-based"
description: "学习主干开发工作流的使用方法"
is_published: true
estimated_minutes: 60
---

# 主干开发工作流

主干开发（Trunk-Based Development）是一种源代码管理实践，团队成员直接在主干分支（通常是 main 或 master）上进行集成。

## 核心概念

1. 主干优先
   - 所有开发者都在主干分支上工作
   - 频繁集成小规模变更
   - 保持主干分支随时可发布

2. 短生命周期分支
   - 使用短期特性分支（通常不超过 1-2 天）
   - 快速合并回主干分支
   - 避免长期分支带来的合并冲突

## 工作流程

### 日常开发流程

```bash
# 更新主干分支
git checkout main
git pull origin main

# 创建短期特性分支
git checkout -b feature/quick-fix

# 完成开发后合并回主干
git checkout main
git merge feature/quick-fix
git push origin main
```

### 发布流程

```bash
# 从主干创建发布分支
git checkout -b release/1.0.0 main

# 在发布分支上进行最后的测试和修复
git tag -a v1.0.0
git push origin v1.0.0
```

## 持续集成实践

1. 自动化测试
   - 提交前运行单元测试
   - 持续集成系统运行完整测试套件
   - 快速发现并修复问题

2. 特性开关
   - 使用特性开关控制新功能
   - 允许未完成的代码合并到主干
   - 生产环境动态开启/关闭功能

## 最佳实践

1. 保持提交小而频繁
2. 建立强大的自动化测试体系
3. 使用特性开关管理功能发布
4. 实施代码审查和自动化检查
5. 保持良好的团队沟通