---
title: "基本操作实践"
slug: "practice"
sequence: 4
description: "通过实际练习来掌握 Git 的基本操作命令"
is_published: true
estimated_minutes: 30
---

# Git 基本操作实践

本节将通过一系列实践练习，帮助你巩固对 Git 基本操作的理解。

## 练习1：仓库操作

### 创建本地仓库

1. 创建一个新的项目目录：
   ```bash
   mkdir git-practice
   cd git-practice
   ```

2. 初始化 Git 仓库：
   ```bash
   git init
   ```

3. 检查仓库状态：
   ```bash
   git status
   ```

### 配置仓库

1. 设置用户信息：
   ```bash
   git config user.name "你的名字"
   git config user.email "你的邮箱"
   ```

2. 创建 .gitignore 文件：
   ```bash
   echo "*.log" > .gitignore
   echo "build/" >> .gitignore
   ```

## 练习2：文件操作

### 基本文件操作

1. 创建并添加文件：
   ```bash
   echo "# 项目说明" > README.md
   git add README.md
   git commit -m "添加 README 文件"
   ```

2. 修改文件：
   ```bash
   echo "这是一个练习项目" >> README.md
   git diff
   git add README.md
   git commit -m "更新项目说明"
   ```

### 多文件操作

1. 创建多个文件：
   ```bash
   echo "console.log('Hello');" > index.js
   echo "body { margin: 0; }" > styles.css
   ```

2. 分别提交：
   ```bash
   git add index.js
   git commit -m "添加 JavaScript 文件"
   
   git add styles.css
   git commit -m "添加样式文件"
   ```

## 练习3：撤销操作

### 文件修改撤销

1. 修改文件并撤销：
   ```bash
   echo "错误的修改" >> README.md
   git restore README.md
   ```

2. 暂存后撤销：
   ```bash
   echo "待撤销的修改" >> index.js
   git add index.js
   git restore --staged index.js
   ```

### 提交操作

1. 修改最后一次提交：
   ```bash
   echo "新的样式" >> styles.css
   git add styles.css
   git commit --amend --no-edit
   ```

2. 创建和撤销提交：
   ```bash
   echo "测试撤销" > test.txt
   git add test.txt
   git commit -m "添加测试文件"
   git revert HEAD
   ```

## 练习4：分支操作

### 分支管理

1. 创建和切换分支：
   ```bash
   git checkout -b feature
   echo "新功能代码" > feature.js
   git add feature.js
   git commit -m "添加新功能"
   ```

2. 合并分支：
   ```bash
   git checkout main
   git merge feature
   ```

### 解决冲突

1. 创建冲突：
   ```bash
   # 在 main 分支
   echo "main 分支的修改" > conflict.txt
   git add conflict.txt
   git commit -m "main 分支的更改"
   
   # 在 feature 分支
   git checkout feature
   echo "feature 分支的修改" > conflict.txt
   git add conflict.txt
   git commit -m "feature 分支的更改"
   ```

2. 解决冲突：
   ```bash
   git checkout main
   git merge feature
   # 手动解决冲突
   git add conflict.txt
   git commit -m "解决冲突"
   ```

## 练习5：远程仓库操作

### 远程仓库管理

1. 添加远程仓库：
   ```bash
   git remote add origin <repository-url>
   ```

2. 推送到远程：
   ```bash
   git push -u origin main
   ```

3. 从远程拉取：
   ```bash
   git pull origin main
   ```

## 进阶练习

### 储藏操作

1. 储藏更改：
   ```bash
   # 修改文件
   echo "临时修改" >> README.md
   
   # 储藏更改
   git stash save "临时保存修改"
   
   # 恢复更改
   git stash pop
   ```

### 历史查看

1. 查看提交历史：
   ```bash
   git log --oneline --graph
   ```

2. 查看文件历史：
   ```bash
   git log -p README.md
   ```

## 检查清单

完成练习后，确保你能够：

- [ ] 创建和配置 Git 仓库
- [ ] 进行基本的文件操作
- [ ] 使用各种撤销命令
- [ ] 管理分支和解决冲突
- [ ] 操作远程仓库
- [ ] 使用 Git 的高级功能

## 扩展练习

1. 尝试使用 GUI 工具
   - 安装 Git GUI 或其他图形界面工具
   - 使用图形界面完成上述操作

2. 模拟团队协作
   - 创建多个本地仓库
   - 练习推送和拉取操作
   - 处理多人协作场景

3. 自定义 Git 配置
   - 创建 Git 别名
   - 配置 Git 命令的默认行为
   - 设置 Git 的颜色输出 