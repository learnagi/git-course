---
title: "日常开发技巧"
slug: "daily-tips"
sequence: 1
description: "介绍日常开发中常用的 Git 技巧和最佳实践"
status: "published"
---

# 日常开发技巧

本节将介绍在日常开发中经常用到的 Git 技巧，帮助你提高工作效率。

## 基础命令技巧

### 1. 文件操作
- 查看文件状态和变更
- 暂存和提交文件
- 撤销文件修改

### 2. 分支操作
- 快速切换分支
- 创建和删除分支
- 重命名分支

### 3. 提交管理
- 修改最近的提交信息
- 查看提交历史
- 撤销提交操作

### 4. 远程仓库操作
- 同步远程分支
- 管理远程仓库
- 推送和拉取代码

## 实用技巧

1. 使用 git help 查看帮助信息
2. 使用 git status -s 查看简洁状态
3. 使用 git log --oneline 查看简洁历史
4. 使用 git checkout - 快速切换分支

## 配置建议

1. 设置全局用户信息
2. 配置常用别名
3. 设置默认编辑器
4. 配置换行符处理

## 常用命令别名

```bash
# 在 ~/.gitconfig 中配置
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
```

## 部分暂存

使用 `git add -p` 可以交互式地选择要暂存的代码块：

```bash
git add -p file.txt
```

## 储藏修改

临时保存工作区的修改：

```bash
# 储藏修改
git stash save "正在进行的功能开发"

# 查看储藏列表
git stash list

# 恢复最近的储藏
git stash pop
```

## 撤销操作

```bash
# 撤销最近的提交
git reset --soft HEAD^

# 撤销工作区的修改
git checkout -- file.txt
```

## 查看历史

```bash
# 查看某个文件的修改历史
git log -p file.txt

# 查看某人的提交记录
git log --author="用户名"
```

## 快速修复

```bash
# 修改最近的提交信息
git commit --amend

# 快速提交所有修改
git commit -am "提交信息"
```

## 工作区清理

```bash
# 清理未跟踪的文件
git clean -f

# 清理未跟踪的文件和目录
git clean -fd
```

## 技巧提示

1. 经常使用 `git status` 检查工作区状态
2. 提交前使用 `git diff` 检查修改
3. 定期推送到远程仓库备份代码
4. 保持小型、原子化的提交
5. 编写清晰的提交信息