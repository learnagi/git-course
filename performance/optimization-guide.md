---
title: "Git 性能优化指南"
slug: "optimization-guide"
description: "深入了解 Git 性能优化技巧和最佳实践"
is_published: true
estimated_minutes: 40
---

# Git 性能优化指南

## 仓库优化

### 大文件处理

1. **使用 Git LFS**
```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.psd"
git lfs track "*.zip"

# 查看跟踪状态
git lfs status
```

2. **清理大文件历史**
```bash
# 查找大文件
git rev-list --objects --all | git cat-file --batch-check | sort -k 3 -n -r | head -n 10

# 使用 BFG 清理
bfg --strip-blobs-bigger-than 100M repo.git
```

### 仓库瘦身

1. **垃圾回收**
```bash
# 常规清理
git gc

# 积极清理
git gc --aggressive

# 清理未引用对象
git prune
```

2. **重写历史**
```bash
# 压缩提交
git rebase -i HEAD~10

# 清理远程分支
git remote prune origin
```

## 日常操作优化

### 克隆优化

1. **浅克隆**
```bash
# 最近一次提交
git clone --depth 1 <repository>

# 指定提交次数
git clone --depth 5 <repository>
```

2. **部分克隆**
```bash
# 单分支克隆
git clone --single-branch --branch main <repository>

# 稀疏检出
git clone --filter=blob:none <repository>
```

### 索引优化

1. **配置调优**
```bash
# 启用并行索引预加载
git config core.preloadIndex true

# 设置文件系统监视
git config core.fsmonitor true
```

2. **维护索引**
```bash
# 重建索引
rm .git/index
git reset

# 压缩索引
git repack -ad
```

## 网络优化

### 传输优化

1. **压缩设置**
```bash
# 配置压缩级别
git config --global core.compression 9

# 配置打包限制
git config --global pack.windowMemory "100m"
git config --global pack.packSizeLimit "100m"
```

2. **缓存配置**
```bash
# HTTP 缓存
git config --global http.postBuffer 524288000

# 启用持久连接
git config --global http.keepAlive true
```

### 镜像加速

1. **配置镜像**
```bash
# 添加镜像
git config --global url."https://mirror.git.fun/".insteadOf "https://github.com/"

# 验证配置
git config --get-regexp url.
```

## 监控与诊断

### 性能监控

1. **跟踪命令**
```bash
# 开启跟踪
GIT_TRACE=1 git status

# 详细跟踪
GIT_TRACE_PACKET=1 git pull
```

2. **统计信息**
```bash
# 仓库大小
git count-objects -vH

# 提交统计
git shortlog -sn --all
```

### 问题诊断

1. **常见问题**
   - 克隆速度慢
   - 提交响应慢
   - 分支切换慢
   - 存储空间大

2. **解决方案**
   - 使用浅克隆
   - 配置压缩
   - 清理历史
   - 优化配置

## 最佳实践

1. **仓库管理**
   - 定期清理
   - 合理分割
   - 控制大小

2. **工作流程**
   - 小批量提交
   - 及时清理分支
   - 避免大文件

3. **配置优化**
   - 合理设置
   - 定期更新
   - 监控性能

通过本节的学习，你应该掌握了 Git 性能优化的核心技巧和最佳实践。这些优化方法将帮助你更高效地使用 Git，特别是在处理大型仓库时。