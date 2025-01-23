---
title: "故障排除"
slug: "troubleshooting"
description: "掌握 Git 常见问题和高级问题的解决方法"
is_published: true
estimated_minutes: 30
---

# 故障排除

本节将介绍 Git 使用中的常见问题及其解决方法。

## 常见问题

### 提交问题

1. 修改最后提交
```bash
# 修改提交信息
git commit --amend -m "feat: correct message"

# 添加遗漏文件
git add forgotten-file.txt
git commit --amend --no-edit

# 修改作者信息
git commit --amend --author="Name <email@example.com>"
```

2. 撤销提交
```bash
# 撤销最后一次提交
git reset HEAD~1

# 保留更改
git reset --soft HEAD~1

# 丢弃更改
git reset --hard HEAD~1
```

### 分支问题

1. 合并冲突
```bash
# 查看冲突文件
git status

# 解决冲突
git mergetool

# 完成合并
git add .
git commit -m "merge: resolve conflicts"
```

2. 变基冲突
```bash
# 开始变基
git rebase main

# 解决冲突
git mergetool

# 继续变基
git rebase --continue

# 放弃变基
git rebase --abort
```

## 高级问题

### 历史问题

1. 历史修改
```bash
# 交互式变基
git rebase -i HEAD~5

# 修改提交
git commit --amend
git rebase --continue

# 压缩提交
git reset --soft HEAD~3
git commit -m "feat: combine three commits"
```

2. 历史分析
```bash
# 查看提交统计
git shortlog -sn

# 分析文件历史
git log --follow -p -- path/to/file

# 查找引入问题的提交
git bisect start
git bisect bad HEAD
git bisect good v1.0
```

### 存储问题

1. Git LFS
```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.psd"
git lfs track "*.zip"

# 迁移现有文件
git lfs migrate import --include="*.psd"
```

2. 存储优化
```bash
# 检查存储
git count-objects -vH

# 压缩存储
git gc --aggressive
git repack -ad
git prune
```