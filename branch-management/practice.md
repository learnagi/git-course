---
title: "分支管理实践"
slug: "practice"
sequence: 5
description: "通过实践练习掌握 Git 分支管理的各项操作"
is_published: true
estimated_minutes: 30
---

# Git 分支管理实践

本节将通过一系列实践练习，帮助你掌握 Git 分支管理的各项操作。

## 练习1：基本分支操作

### 创建和切换分支

1. 创建并切换到新分支：
   ```bash
   git checkout -b feature-login
   ```

2. 在新分支上做一些修改：
   ```bash
   echo "添加登录功能" > login.txt
   git add login.txt
   git commit -m "添加登录功能文件"
   ```

3. 切换回主分支：
   ```bash
   git checkout main
   ```

## 练习2：合并分支

### 快进合并

1. 将 feature 分支合并到主分支：
   ```bash
   git checkout main
   git merge feature-login
   ```

### 解决冲突

1. 创建冲突场景：
   ```bash
   # 在主分支修改文件
   echo "主分支的修改" > common.txt
   git add common.txt
   git commit -m "主分支的修改"
   
   # 在特性分支修改同一文件
   git checkout feature-login
   echo "特性分支的修改" > common.txt
   git add common.txt
   git commit -m "特性分支的修改"
   ```

2. 尝试合并并解决冲突：
   ```bash
   git checkout main
   git merge feature-login
   # 手动解决冲突
   git add common.txt
   git commit -m "解决合并冲突"
   ```

## 练习3：分支管理

### 删除分支

1. 删除已合并的分支：
   ```bash
   git branch -d feature-login
   ```

2. 强制删除未合并的分支：
   ```bash
   git branch -D feature-unmerged
   ```

### 远程分支操作

1. 推送本地分支到远程：
   ```bash
   git push origin feature-login
   ```

2. 删除远程分支：
   ```bash
   git push origin --delete feature-login
   ```

## 练习4：分支策略应用

### Git Flow 实践

1. 创建开发分支：
   ```bash
   git checkout -b develop main
   ```

2. 创建特性分支：
   ```bash
   git checkout -b feature/user-auth develop
   ```

3. 完成特性开发后合并回开发分支：
   ```bash
   git checkout develop
   git merge --no-ff feature/user-auth
   ```

## 注意事项

1. 保持分支同步
   - 经常从主分支更新代码
   - 解决冲突时仔细检查

2. 分支命名规范
   - 使用有意义的分支名
   - 遵循团队约定的前缀

3. 及时清理分支
   - 及时删除已合并分支
   - 定期清理过期分支