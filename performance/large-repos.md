---
title: "大型仓库管理"
slug: "large-repos"
description: "掌握管理大型 Git 仓库的技巧"
is_published: true
estimated_minutes: 25
---

# 大型仓库管理

本节将介绍管理大型 Git 仓库的技巧和方法，帮助你有效处理大规模代码库。

## 仓库分析

### 1. 规模评估

1. 仓库统计
```bash
# 查看仓库大小
du -sh .git

# 统计文件数量
git ls-files | wc -l

# 分析提交历史
git rev-list --count --all
```

2. 性能分析
```bash
# 使用 git-sizer
git-sizer -v

# 分析大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sort -nr -k3
```

### 2. 问题诊断

1. 存储问题
```bash
# 检查松散对象
git count-objects -v

# 分析包文件
git verify-pack -v .git/objects/pack/*.idx |
  sort -k 3 -n |
  tail -10
```

2. 性能问题
```bash
# 操作计时
GIT_TRACE=1 git status

# 内存使用
ps -o rss,command -p $(pgrep -f git)
```

## 优化策略

### 1. 存储优化

1. 清理历史
```bash
# 压缩历史
git gc --aggressive

# 清理大文件
git filter-branch --tree-filter 'rm -f path/to/large/file' HEAD
```

2. 子模块拆分
```bash
# 创建子模块
git submodule add <repository>

# 更新子模块
git submodule update --init --recursive
```

### 2. 访问优化

1. 浅克隆
```bash
# 浅克隆最新版本
git clone --depth 1 <repository>

# 按需获取历史
git fetch --unshallow
```

2. 稀疏检出
```bash
# 启用稀疏检出
git sparse-checkout init

# 设置检出路径
git sparse-checkout set <path>
```