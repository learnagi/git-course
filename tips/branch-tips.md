---
title: "Git 分支管理技巧"
slug: "branch-tips"
sequence: 1
description: "常用的 Git 分支管理操作技巧和命令"
status: "published"
---

# 分支管理技巧

## 查看分支信息

### 列出所有已合并到 master 的分支
```bash
git branch --merged master
```

### 列出所有分支及其上游分支和最后提交
```bash
git branch -vv
```

### 获取所有远程分支
```bash
git branch -r
```

## 分支操作

### 快速切换到上一个分支
```bash
git checkout -
```

### 删除已经合并到 master 的分支
```bash
git branch --merged master | grep -v '^\*\|\s*master' | xargs -n 1 git branch -d
```

### 删除本地分支
```bash
git branch -d <branch-name>
```

### 删除远程分支
```bash
git push origin --delete <branch-name>
```

### 重命名分支
```bash
git branch -m <old-name> <new-name>
```

## 分支追踪

### 设置上游分支
```bash
git branch -u origin/<branch-name>
```

### 清理远程已删除分支的本地引用
```bash
git remote prune origin
```

# 注意事项
- 删除分支前确保相关更改已经合并或备份
- 重命名分支可能会影响其他开发者的工作
- 定期清理已合并的分支以保持仓库整洁
- 设置上游分支有助于简化推送和拉取操作