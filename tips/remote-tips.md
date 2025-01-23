---
title: "Git 远程操作技巧"
slug: "remote-tips"
sequence: 5
description: "Git 远程仓库操作相关的常用技巧和命令"
status: "published"
---

# 远程操作技巧

## 远程仓库管理

### 查看所有远程引用
```bash
git remote
# 或者
git remote show
```

### 获取远程分支列表
```bash
git branch -r
```

### 获取所有本地和远程分支
```bash
git branch -a
```

## 同步操作

### 同步远程并覆盖本地更改
```bash
git fetch origin && git reset --hard origin/master && git clean -f -d
```

### 拉取时总是使用变基而不是合并
```bash
git config --global pull.rebase true
```

### 推送本地分支到远程同名分支
```bash
git push origin HEAD
```

### 推送并设置上游分支
```bash
git push -u origin <branch-name>
```

## 远程分支清理

### 清理远程已删除分支的本地引用
```bash
git remote prune origin
```

### 删除远程分支
```bash
git push origin --delete <branch-name>
# 或者
git push origin :<branch-name>
```

### 删除远程标签
```bash
git push origin :refs/tags/<tag-name>
```

# 注意事项
- 在覆盖本地更改前确保已备份重要内容
- 使用 force push 时要特别小心
- 定期清理过时的远程引用
- 推送前先同步远程变更