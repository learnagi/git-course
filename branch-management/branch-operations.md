---
title: "分支操作命令"
slug: "branch-operations"
sequence: 2
description: "学习 Git 分支的基本操作命令，包括创建、切换、合并等"
is_published: true
estimated_minutes: 20
---

---
title: "Git 分支操作"
slug: "branch-operations"
sequence: 2
description: "学习 Git 分支的基本操作，包括创建、切换、合并等命令"
is_published: true
estimated_minutes: 20
---

# Git 分支操作命令

本节将介绍 Git 分支的各种操作命令，帮助你熟练使用分支功能。

## 查看分支

### 列出本地分支
```bash
# 查看本地分支
git branch

# 查看包含最后一次提交信息的分支列表
git branch -v
```

### 查看远程分支
```bash
# 查看远程分支
git branch -r

# 查看所有分支（本地和远程）
git branch -a
```

## 创建分支

### 创建新分支
```bash
# 创建分支但不切换
git branch <branch-name>

# 创建并切换到新分支
git checkout -b <branch-name>
# 或使用新语法
git switch -c <branch-name>
```

### 基于特定提交创建分支
```bash
# 基于某个提交创建分支
git branch <branch-name> <commit-hash>

# 基于标签创建分支
git branch <branch-name> <tag-name>
```

## 切换分支

### 切换到已有分支
```bash
# 使用 checkout
git checkout <branch-name>

# 使用新的 switch 命令（推荐）
git switch <branch-name>
```

### 切换到上一个分支
```bash
git checkout -
# 或
git switch -
```

## 重命名分支

### 重命名本地分支
```bash
# 重命名当前分支
git branch -m <new-name>

# 重命名指定分支
git branch -m <old-name> <new-name>
```

## 删除分支

### 删除本地分支
```bash
# 删除已合并的分支
git branch -d <branch-name>

# 强制删除分支
git branch -D <branch-name>
```

### 删除远程分支
```bash
git push origin --delete <branch-name>
# 或
git push origin :<branch-name>
```

## 合并分支

### 基本合并
```bash
# 切换到目标分支
git checkout main

# 合并其他分支到当前分支
git merge <source-branch>
```

### 压缩合并
```bash
# 将多个提交压缩成一个
git merge --squash <source-branch>
```

## 变基操作

### 基本变基
```bash
# 将当前分支变基到 main
git rebase main

# 交互式变基
git rebase -i main
```

## 储藏更改

### 储藏操作
```bash
# 储藏当前更改
git stash

# 储藏包含未跟踪的文件
git stash -u

# 储藏时添加说明
git stash save "修改说明"
```

### 管理储藏
```bash
# 查看储藏列表
git stash list

# 应用最近的储藏
git stash apply

# 应用并删除储藏
git stash pop

# 删除储藏
git stash drop stash@{n}
```

## 分支追踪

### 设置上游分支
```bash
# 设置当前分支的上游分支
git branch -u origin/<branch-name>

# 推送并设置上游分支
git push -u origin <branch-name>
```

## 分支比较

### 比较分支差异
```bash
# 比较两个分支的差异
git diff branch1..branch2

# 查看分支合并图
git log --graph --oneline --all
```

## 最佳实践

1. **分支操作**
   - 经常更新本地分支
   - 及时清理已合并分支
   - 使用有意义的分支名

2. **合并策略**
   - 先更新再合并
   - 解决所有冲突
   - 适时使用压缩合并

3. **变基使用**
   - 仅在本地分支使用
   - 避免在公共分支上变基
   - 谨慎使用交互式变基

## 常见问题

1. **分支切换失败**
   - 检查工作区状态
   - 提交或储藏更改
   - 确认分支名称正确

2. **合并冲突**
   - 仔细检查冲突文件
   - 与团队沟通变更
   - 确保合并后代码正确

3. **远程分支操作**
   - 确保有推送权限
   - 先拉取后推送
   - 注意分支保护设置

## 练习

1. 分支基本操作
   - 创建并切换分支
   - 在分支上修改文件
   - 合并分支更改

2. 解决冲突
   - 制造合并冲突
   - 手动解决冲突
   - 完成分支合并

3. 远程分支操作
   - 推送本地分支
   - 跟踪远程分支
   - 删除远程分支